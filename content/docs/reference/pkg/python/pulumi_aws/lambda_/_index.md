---
title: Module lambda_
---

<div class="section" id="lambda">
<h1><a class="reference internal" href="#lambda">lambda</a><a class="headerlink" href="#lambda" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_aws.lambda_"></span><dl class="class">
<dt id="pulumi_aws.lambda_.Alias">
<em class="property">class </em><code class="descclassname">pulumi_aws.lambda_.</code><code class="descname">Alias</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>function_name=None</em>, <em>function_version=None</em>, <em>name=None</em>, <em>routing_config=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lambda_.Alias" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a Lambda function alias. Creates an alias that points to the specified Lambda function version.</p>
<p>For information about Lambda and how to use it, see [What is AWS Lambda?][1]
For information about function aliases, see [CreateAlias][2] and [AliasRoutingConfiguration][3] in the API docs.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the alias.</li>
<li><strong>function_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The function ARN of the Lambda function for which you want to create an alias.</li>
<li><strong>function*version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Lambda function version for which you are creating the alias. Pattern: <code class="docutils literal notranslate"><span class="pre">(\$LATEST|[0-9]+)</span></code>.</p>
</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name for the alias you are creating. Pattern: <cite>(?!^[0-9]+$)([a-zA-Z0-9-*]+)</cite></li>
<li><strong>routing_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The Lambda alias’ route configuration settings. Fields documented below</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lambda_alias.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lambda_alias.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.lambda_.Alias.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Alias.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) identifying your Lambda function alias.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Alias.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Alias.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the alias.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Alias.function_name">
<code class="descname">function_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Alias.function_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The function ARN of the Lambda function for which you want to create an alias.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Alias.function_version">
<code class="descname">function_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Alias.function_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Lambda function version for which you are creating the alias. Pattern: <code class="docutils literal notranslate"><span class="pre">(\$LATEST|[0-9]+)</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Alias.invoke_arn">
<code class="descname">invoke_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Alias.invoke_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN to be used for invoking Lambda Function from API Gateway - to be used in <cite>``apigateway.Integration`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/api_gateway_integration.html">https://www.terraform.io/docs/providers/aws/r/api_gateway_integration.html</a>&gt;`_’s <code class="docutils literal notranslate"><span class="pre">uri</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Alias.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Alias.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name for the alias you are creating. Pattern: <code class="docutils literal notranslate"><span class="pre">(?!^[0-9]+$)([a-zA-Z0-9-_]+)</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Alias.routing_config">
<code class="descname">routing_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Alias.routing_config" title="Permalink to this definition">¶</a></dt>
<dd><p>The Lambda alias’ route configuration settings. Fields documented below</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_aws.lambda_.Alias.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>arn=None</em>, <em>description=None</em>, <em>function_name=None</em>, <em>function_version=None</em>, <em>invoke_arn=None</em>, <em>name=None</em>, <em>routing_config=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lambda_.Alias.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Alias resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] arn: The Amazon Resource Name (ARN) identifying your Lambda function alias.
:param pulumi.Input[str] description: Description of the alias.
:param pulumi.Input[str] function_name: The function ARN of the Lambda function for which you want to create an alias.
:param pulumi.Input[str] function_version: Lambda function version for which you are creating the alias. Pattern: <code class="docutils literal notranslate"><span class="pre">(\$LATEST|[0-9]+)</span></code>.
:param pulumi.Input[str] invoke_arn: The ARN to be used for invoking Lambda Function from API Gateway - to be used in <cite>``apigateway.Integration`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/api_gateway_integration.html">https://www.terraform.io/docs/providers/aws/r/api_gateway_integration.html</a>&gt;`_’s <code class="docutils literal notranslate"><span class="pre">uri</span></code>
:param pulumi.Input[str] name: Name for the alias you are creating. Pattern: <code class="docutils literal notranslate"><span class="pre">(?!^[0-9]+$)([a-zA-Z0-9-_]+)</span></code>
:param pulumi.Input[dict] routing_config: The Lambda alias’ route configuration settings. Fields documented below</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lambda_alias.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lambda_alias.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.lambda_.Alias.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lambda_.Alias.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.lambda_.Alias.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lambda_.Alias.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.lambda_.AwaitableGetFunctionResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.lambda_.</code><code class="descname">AwaitableGetFunctionResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>dead_letter_config=None</em>, <em>description=None</em>, <em>environment=None</em>, <em>function_name=None</em>, <em>handler=None</em>, <em>invoke_arn=None</em>, <em>kms_key_arn=None</em>, <em>last_modified=None</em>, <em>layers=None</em>, <em>memory_size=None</em>, <em>qualified_arn=None</em>, <em>qualifier=None</em>, <em>reserved_concurrent_executions=None</em>, <em>role=None</em>, <em>runtime=None</em>, <em>source_code_hash=None</em>, <em>source_code_size=None</em>, <em>tags=None</em>, <em>timeout=None</em>, <em>tracing_config=None</em>, <em>version=None</em>, <em>vpc_config=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lambda_.AwaitableGetFunctionResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.lambda_.AwaitableGetInvocationResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.lambda_.</code><code class="descname">AwaitableGetInvocationResult</code><span class="sig-paren">(</span><em>function_name=None</em>, <em>input=None</em>, <em>qualifier=None</em>, <em>result=None</em>, <em>result_map=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lambda_.AwaitableGetInvocationResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.lambda_.AwaitableGetLayerVersionResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.lambda_.</code><code class="descname">AwaitableGetLayerVersionResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>compatible_runtime=None</em>, <em>compatible_runtimes=None</em>, <em>created_date=None</em>, <em>description=None</em>, <em>layer_arn=None</em>, <em>layer_name=None</em>, <em>license_info=None</em>, <em>source_code_hash=None</em>, <em>source_code_size=None</em>, <em>version=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lambda_.AwaitableGetLayerVersionResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.lambda_.EventSourceMapping">
<em class="property">class </em><code class="descclassname">pulumi_aws.lambda_.</code><code class="descname">EventSourceMapping</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>batch_size=None</em>, <em>enabled=None</em>, <em>event_source_arn=None</em>, <em>function_name=None</em>, <em>starting_position=None</em>, <em>starting_position_timestamp=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lambda_.EventSourceMapping" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Lambda event source mapping. This allows Lambda functions to get events from Kinesis, DynamoDB and SQS.</p>
<p>For information about Lambda and how to use it, see [What is AWS Lambda?][1].
For information about event source mappings, see [CreateEventSourceMapping][2] in the API docs.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>batch_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The largest number of records that Lambda will retrieve from your event source at the time of invocation. Defaults to <code class="docutils literal notranslate"><span class="pre">100</span></code> for DynamoDB and Kinesis, <code class="docutils literal notranslate"><span class="pre">10</span></code> for SQS.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines if the mapping will be enabled on creation. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
<li><strong>event_source_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The event source ARN - can either be a Kinesis or DynamoDB stream.</li>
<li><strong>function_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or the ARN of the Lambda function that will be subscribing to events.</li>
<li><strong>starting_position</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The position in the stream where AWS Lambda should start reading. Must be one of <code class="docutils literal notranslate"><span class="pre">AT_TIMESTAMP</span></code> (Kinesis only), <code class="docutils literal notranslate"><span class="pre">LATEST</span></code> or <code class="docutils literal notranslate"><span class="pre">TRIM_HORIZON</span></code> if getting events from Kinesis or DynamoDB. Must not be provided if getting events from SQS. More information about these positions can be found in the <a class="reference external" href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_GetShardIterator.html">AWS DynamoDB Streams API Reference</a> and <a class="reference external" href="https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetShardIterator.html#Kinesis-GetShardIterator-request-ShardIteratorType">AWS Kinesis API Reference</a>.</li>
<li><strong>starting_position_timestamp</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A timestamp in <a class="reference external" href="https://tools.ietf.org/html/rfc3339#section-5.8">RFC3339 format</a> of the data record which to start reading when using <code class="docutils literal notranslate"><span class="pre">starting_position</span></code> set to <code class="docutils literal notranslate"><span class="pre">AT_TIMESTAMP</span></code>. If a record with this exact timestamp does not exist, the next later record is chosen. If the timestamp is older than the current trim horizon, the oldest available record is chosen.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lambda_event_source_mapping.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lambda_event_source_mapping.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.lambda_.EventSourceMapping.batch_size">
<code class="descname">batch_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.EventSourceMapping.batch_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The largest number of records that Lambda will retrieve from your event source at the time of invocation. Defaults to <code class="docutils literal notranslate"><span class="pre">100</span></code> for DynamoDB and Kinesis, <code class="docutils literal notranslate"><span class="pre">10</span></code> for SQS.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.EventSourceMapping.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.EventSourceMapping.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines if the mapping will be enabled on creation. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.EventSourceMapping.event_source_arn">
<code class="descname">event_source_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.EventSourceMapping.event_source_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The event source ARN - can either be a Kinesis or DynamoDB stream.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.EventSourceMapping.function_arn">
<code class="descname">function_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.EventSourceMapping.function_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The the ARN of the Lambda function the event source mapping is sending events to. (Note: this is a computed value that differs from <code class="docutils literal notranslate"><span class="pre">function_name</span></code> above.)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.EventSourceMapping.function_name">
<code class="descname">function_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.EventSourceMapping.function_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or the ARN of the Lambda function that will be subscribing to events.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.EventSourceMapping.last_modified">
<code class="descname">last_modified</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.EventSourceMapping.last_modified" title="Permalink to this definition">¶</a></dt>
<dd><p>The date this resource was last modified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.EventSourceMapping.last_processing_result">
<code class="descname">last_processing_result</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.EventSourceMapping.last_processing_result" title="Permalink to this definition">¶</a></dt>
<dd><p>The result of the last AWS Lambda invocation of your Lambda function.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.EventSourceMapping.starting_position">
<code class="descname">starting_position</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.EventSourceMapping.starting_position" title="Permalink to this definition">¶</a></dt>
<dd><p>The position in the stream where AWS Lambda should start reading. Must be one of <code class="docutils literal notranslate"><span class="pre">AT_TIMESTAMP</span></code> (Kinesis only), <code class="docutils literal notranslate"><span class="pre">LATEST</span></code> or <code class="docutils literal notranslate"><span class="pre">TRIM_HORIZON</span></code> if getting events from Kinesis or DynamoDB. Must not be provided if getting events from SQS. More information about these positions can be found in the <a class="reference external" href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_GetShardIterator.html">AWS DynamoDB Streams API Reference</a> and <a class="reference external" href="https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetShardIterator.html#Kinesis-GetShardIterator-request-ShardIteratorType">AWS Kinesis API Reference</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.EventSourceMapping.starting_position_timestamp">
<code class="descname">starting_position_timestamp</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.EventSourceMapping.starting_position_timestamp" title="Permalink to this definition">¶</a></dt>
<dd><p>A timestamp in <a class="reference external" href="https://tools.ietf.org/html/rfc3339#section-5.8">RFC3339 format</a> of the data record which to start reading when using <code class="docutils literal notranslate"><span class="pre">starting_position</span></code> set to <code class="docutils literal notranslate"><span class="pre">AT_TIMESTAMP</span></code>. If a record with this exact timestamp does not exist, the next later record is chosen. If the timestamp is older than the current trim horizon, the oldest available record is chosen.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.EventSourceMapping.state">
<code class="descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.EventSourceMapping.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The state of the event source mapping.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.EventSourceMapping.state_transition_reason">
<code class="descname">state_transition_reason</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.EventSourceMapping.state_transition_reason" title="Permalink to this definition">¶</a></dt>
<dd><p>The reason the event source mapping is in its current state.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.EventSourceMapping.uuid">
<code class="descname">uuid</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.EventSourceMapping.uuid" title="Permalink to this definition">¶</a></dt>
<dd><p>The UUID of the created event source mapping.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_aws.lambda_.EventSourceMapping.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>batch_size=None</em>, <em>enabled=None</em>, <em>event_source_arn=None</em>, <em>function_arn=None</em>, <em>function_name=None</em>, <em>last_modified=None</em>, <em>last_processing_result=None</em>, <em>starting_position=None</em>, <em>starting_position_timestamp=None</em>, <em>state=None</em>, <em>state_transition_reason=None</em>, <em>uuid=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lambda_.EventSourceMapping.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EventSourceMapping resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[float] batch_size: The largest number of records that Lambda will retrieve from your event source at the time of invocation. Defaults to <code class="docutils literal notranslate"><span class="pre">100</span></code> for DynamoDB and Kinesis, <code class="docutils literal notranslate"><span class="pre">10</span></code> for SQS.
:param pulumi.Input[bool] enabled: Determines if the mapping will be enabled on creation. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.
:param pulumi.Input[str] event_source_arn: The event source ARN - can either be a Kinesis or DynamoDB stream.
:param pulumi.Input[str] function_arn: The the ARN of the Lambda function the event source mapping is sending events to. (Note: this is a computed value that differs from <code class="docutils literal notranslate"><span class="pre">function_name</span></code> above.)
:param pulumi.Input[str] function_name: The name or the ARN of the Lambda function that will be subscribing to events.
:param pulumi.Input[str] last_modified: The date this resource was last modified.
:param pulumi.Input[str] last_processing_result: The result of the last AWS Lambda invocation of your Lambda function.
:param pulumi.Input[str] starting_position: The position in the stream where AWS Lambda should start reading. Must be one of <code class="docutils literal notranslate"><span class="pre">AT_TIMESTAMP</span></code> (Kinesis only), <code class="docutils literal notranslate"><span class="pre">LATEST</span></code> or <code class="docutils literal notranslate"><span class="pre">TRIM_HORIZON</span></code> if getting events from Kinesis or DynamoDB. Must not be provided if getting events from SQS. More information about these positions can be found in the <a class="reference external" href="https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_streams_GetShardIterator.html">AWS DynamoDB Streams API Reference</a> and <a class="reference external" href="https://docs.aws.amazon.com/kinesis/latest/APIReference/API_GetShardIterator.html#Kinesis-GetShardIterator-request-ShardIteratorType">AWS Kinesis API Reference</a>.
:param pulumi.Input[str] starting_position_timestamp: A timestamp in <a class="reference external" href="https://tools.ietf.org/html/rfc3339#section-5.8">RFC3339 format</a> of the data record which to start reading when using <code class="docutils literal notranslate"><span class="pre">starting_position</span></code> set to <code class="docutils literal notranslate"><span class="pre">AT_TIMESTAMP</span></code>. If a record with this exact timestamp does not exist, the next later record is chosen. If the timestamp is older than the current trim horizon, the oldest available record is chosen.
:param pulumi.Input[str] state: The state of the event source mapping.
:param pulumi.Input[str] state_transition_reason: The reason the event source mapping is in its current state.
:param pulumi.Input[str] uuid: The UUID of the created event source mapping.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lambda_event_source_mapping.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lambda_event_source_mapping.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.lambda_.EventSourceMapping.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lambda_.EventSourceMapping.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.lambda_.EventSourceMapping.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lambda_.EventSourceMapping.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.lambda_.Function">
<em class="property">class </em><code class="descclassname">pulumi_aws.lambda_.</code><code class="descname">Function</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>dead_letter_config=None</em>, <em>description=None</em>, <em>environment=None</em>, <em>code=None</em>, <em>name=None</em>, <em>handler=None</em>, <em>kms_key_arn=None</em>, <em>layers=None</em>, <em>memory_size=None</em>, <em>publish=None</em>, <em>reserved_concurrent_executions=None</em>, <em>role=None</em>, <em>runtime=None</em>, <em>s3_bucket=None</em>, <em>s3_key=None</em>, <em>s3_object_version=None</em>, <em>source_code_hash=None</em>, <em>tags=None</em>, <em>timeout=None</em>, <em>tracing_config=None</em>, <em>vpc_config=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lambda_.Function" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Lambda Function resource. Lambda allows you to trigger execution of code in response to events in AWS. The Lambda Function itself includes source code and runtime configuration.</p>
<p>For information about Lambda and how to use it, see [What is AWS Lambda?][1]</p>
<p>AWS Lambda expects source code to be provided as a deployment package whose structure varies depending on which <code class="docutils literal notranslate"><span class="pre">runtime</span></code> is in use.
See [Runtimes][6] for the valid values of <code class="docutils literal notranslate"><span class="pre">runtime</span></code>. The expected structure of the deployment package can be found in
[the AWS Lambda documentation for each runtime][8].</p>
<p>Once you have created your deployment package you can specify it either directly as a local file (using the <code class="docutils literal notranslate"><span class="pre">filename</span></code> argument) or
indirectly via Amazon S3 (using the <code class="docutils literal notranslate"><span class="pre">s3_bucket</span></code>, <code class="docutils literal notranslate"><span class="pre">s3_key</span></code> and <code class="docutils literal notranslate"><span class="pre">s3_object_version</span></code> arguments). When providing the deployment
package via S3 it may be useful to use the <code class="docutils literal notranslate"><span class="pre">s3.BucketObject</span></code> resource to upload it.</p>
<p>For larger deployment packages it is recommended by Amazon to upload via S3, since the S3 API has better support for uploading
large files efficiently.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>dead_letter*config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>Nested block to configure the function’s <em>dead letter queue</em>. See details below.</p>
</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of what your Lambda Function does.</li>
<li><strong>environment</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The Lambda environment’s configuration settings. Fields documented below.</li>
<li><strong>code</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.Archive</em><em>]</em>) – The path to the function’s deployment package within the local filesystem. If defined, The <cite>s3*`</cite>-prefixed options cannot be used.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for your Lambda Function.</li>
<li><strong>handler</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The function [entrypoint][3] in your code.</li>
<li><strong>kms_key_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN for the KMS encryption key.</li>
<li><strong>layers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. See [Lambda Layers][10]</li>
<li><strong>memory_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Amount of memory in MB your Lambda Function can use at runtime. Defaults to``128<a href="#id11"><span class="problematic" id="id12">``</span></a>. See [Limits][5]</li>
<li><strong>publish</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to publish creation/change as new Lambda Function Version. Defaults to``false<a href="#id13"><span class="problematic" id="id14">``</span></a>.</li>
<li><strong>reserved_concurrent_executions</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of reserved concurrent executions for this lambda function. A value of``0<code class="docutils literal notranslate"><span class="pre">disables</span> <span class="pre">lambda</span> <span class="pre">from</span> <span class="pre">being</span> <span class="pre">triggered</span> <span class="pre">and</span></code>-1<code class="docutils literal notranslate"><span class="pre">removes</span> <span class="pre">any</span> <span class="pre">concurrency</span> <span class="pre">limitations.</span> <span class="pre">Defaults</span> <span class="pre">to</span> <span class="pre">Unreserved</span> <span class="pre">Concurrency</span> <span class="pre">Limits</span></code>-1<a href="#id15"><span class="problematic" id="id16">``</span></a>. See [Managing Concurrency][9]</li>
<li><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model][4] for more details.</li>
<li><strong>runtime</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – See [Runtimes][6] for valid values.</li>
<li><strong>s3_bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The S3 bucket location containing the function’s deployment package. Conflicts with``filename<a href="#id17"><span class="problematic" id="id18">``</span></a>. This bucket must reside in the same AWS region where you are creating the Lambda function.</li>
<li><strong>s3_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The S3 key of an object containing the function’s deployment package. Conflicts with``filename<a href="#id19"><span class="problematic" id="id20">``</span></a>.</li>
<li><strong>s3_object_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The object version containing the function’s deployment package. Conflicts with``filename<a href="#id21"><span class="problematic" id="id22">``</span></a>.</li>
<li><strong>source_code_hash</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either``filename<code class="docutils literal notranslate"><span class="pre">or</span></code>s3_key<code class="docutils literal notranslate"><span class="pre">.</span> <span class="pre">The</span> <span class="pre">usual</span> <span class="pre">way</span> <span class="pre">to</span> <span class="pre">set</span> <span class="pre">this</span> <span class="pre">is</span></code>filebase64sha256(“file.zip”)<code class="docutils literal notranslate"><span class="pre">(this</span> <span class="pre">provider</span> <span class="pre">0.11.12</span> <span class="pre">and</span> <span class="pre">later)</span> <span class="pre">or</span></code>base64sha256(file(“file.zip”))<a href="#id23"><span class="problematic" id="id24">``</span></a>(this provider 0.11.11 and earlier), where “file.zip” is the local filename of the lambda function source archive.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the object.</li>
<li><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of time your Lambda Function has to run in seconds. Defaults to``3`. See [Limits][5]</li>
<li><strong>vpc_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC][7]</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lambda_function.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lambda_function.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.lambda_.Function.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Function.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) identifying your Lambda Function.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Function.dead_letter_config">
<code class="descname">dead_letter_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Function.dead_letter_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested block to configure the function’s <em>dead letter queue</em>. See details below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Function.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Function.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of what your Lambda Function does.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Function.environment">
<code class="descname">environment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Function.environment" title="Permalink to this definition">¶</a></dt>
<dd><p>The Lambda environment’s configuration settings. Fields documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Function.code">
<code class="descname">code</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Function.code" title="Permalink to this definition">¶</a></dt>
<dd><p>The path to the function’s deployment package within the local filesystem. If defined, The <code class="docutils literal notranslate"><span class="pre">s3_</span></code>-prefixed options cannot be used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Function.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Function.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for your Lambda Function.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Function.handler">
<code class="descname">handler</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Function.handler" title="Permalink to this definition">¶</a></dt>
<dd><p>The function [entrypoint][3] in your code.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Function.invoke_arn">
<code class="descname">invoke_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Function.invoke_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN to be used for invoking Lambda Function from API Gateway - to be used in <cite>``apigateway.Integration`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/api_gateway_integration.html">https://www.terraform.io/docs/providers/aws/r/api_gateway_integration.html</a>&gt;`_’s <code class="docutils literal notranslate"><span class="pre">uri</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Function.kms_key_arn">
<code class="descname">kms_key_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Function.kms_key_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for the KMS encryption key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Function.last_modified">
<code class="descname">last_modified</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Function.last_modified" title="Permalink to this definition">¶</a></dt>
<dd><p>The date this resource was last modified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Function.layers">
<code class="descname">layers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Function.layers" title="Permalink to this definition">¶</a></dt>
<dd><p>List of Lambda Layer Version ARNs (maximum of 5) to attach to your Lambda Function. See [Lambda Layers][10]</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Function.memory_size">
<code class="descname">memory_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Function.memory_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Amount of memory in MB your Lambda Function can use at runtime. Defaults to <code class="docutils literal notranslate"><span class="pre">128</span></code>. See [Limits][5]</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Function.publish">
<code class="descname">publish</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Function.publish" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to publish creation/change as new Lambda Function Version. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Function.qualified_arn">
<code class="descname">qualified_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Function.qualified_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) identifying your Lambda Function Version
(if versioning is enabled via <code class="docutils literal notranslate"><span class="pre">publish</span> <span class="pre">=</span> <span class="pre">true</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Function.reserved_concurrent_executions">
<code class="descname">reserved_concurrent_executions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Function.reserved_concurrent_executions" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of reserved concurrent executions for this lambda function. A value of <code class="docutils literal notranslate"><span class="pre">0</span></code> disables lambda from being triggered and <code class="docutils literal notranslate"><span class="pre">-1</span></code> removes any concurrency limitations. Defaults to Unreserved Concurrency Limits <code class="docutils literal notranslate"><span class="pre">-1</span></code>. See [Managing Concurrency][9]</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Function.role">
<code class="descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Function.role" title="Permalink to this definition">¶</a></dt>
<dd><p>IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model][4] for more details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Function.runtime">
<code class="descname">runtime</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Function.runtime" title="Permalink to this definition">¶</a></dt>
<dd><p>See [Runtimes][6] for valid values.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Function.s3_bucket">
<code class="descname">s3_bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Function.s3_bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The S3 bucket location containing the function’s deployment package. Conflicts with <code class="docutils literal notranslate"><span class="pre">filename</span></code>. This bucket must reside in the same AWS region where you are creating the Lambda function.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Function.s3_key">
<code class="descname">s3_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Function.s3_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The S3 key of an object containing the function’s deployment package. Conflicts with <code class="docutils literal notranslate"><span class="pre">filename</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Function.s3_object_version">
<code class="descname">s3_object_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Function.s3_object_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The object version containing the function’s deployment package. Conflicts with <code class="docutils literal notranslate"><span class="pre">filename</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Function.source_code_hash">
<code class="descname">source_code_hash</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Function.source_code_hash" title="Permalink to this definition">¶</a></dt>
<dd><p>Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either <code class="docutils literal notranslate"><span class="pre">filename</span></code> or <code class="docutils literal notranslate"><span class="pre">s3_key</span></code>. The usual way to set this is <code class="docutils literal notranslate"><span class="pre">filebase64sha256(&quot;file.zip&quot;)</span></code> (this provider 0.11.12 and later) or <code class="docutils literal notranslate"><span class="pre">base64sha256(file(&quot;file.zip&quot;))</span></code> (this provider 0.11.11 and earlier), where “file.zip” is the local filename of the lambda function source archive.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Function.source_code_size">
<code class="descname">source_code_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Function.source_code_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size in bytes of the function .zip file.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Function.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Function.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the object.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Function.timeout">
<code class="descname">timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Function.timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of time your Lambda Function has to run in seconds. Defaults to <code class="docutils literal notranslate"><span class="pre">3</span></code>. See [Limits][5]</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Function.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Function.version" title="Permalink to this definition">¶</a></dt>
<dd><p>Latest published version of your Lambda Function.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Function.vpc_config">
<code class="descname">vpc_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Function.vpc_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC][7]</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_aws.lambda_.Function.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>arn=None</em>, <em>dead_letter_config=None</em>, <em>description=None</em>, <em>environment=None</em>, <em>code=None</em>, <em>name=None</em>, <em>handler=None</em>, <em>invoke_arn=None</em>, <em>kms_key_arn=None</em>, <em>last_modified=None</em>, <em>layers=None</em>, <em>memory_size=None</em>, <em>publish=None</em>, <em>qualified_arn=None</em>, <em>reserved_concurrent_executions=None</em>, <em>role=None</em>, <em>runtime=None</em>, <em>s3_bucket=None</em>, <em>s3_key=None</em>, <em>s3_object_version=None</em>, <em>source_code_hash=None</em>, <em>source_code_size=None</em>, <em>tags=None</em>, <em>timeout=None</em>, <em>tracing_config=None</em>, <em>version=None</em>, <em>vpc_config=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lambda_.Function.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Function resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] arn: The Amazon Resource Name (ARN) identifying your Lambda Function.
:param pulumi.Input[dict] dead_letter<em>config: Nested block to configure the function’s *dead letter queue</em>. See details below.
:param pulumi.Input[str] description: Description of what your Lambda Function does.
:param pulumi.Input[dict] environment: The Lambda environment’s configuration settings. Fields documented below.
:param pulumi.Input[pulumi.Archive] code: The path to the function’s deployment package within the local filesystem. If defined, The <cite>s3*`</cite>-prefixed options cannot be used.
:param pulumi.Input[str] name: A unique name for your Lambda Function.
:param pulumi.Input[str] handler: The function [entrypoint][3] in your code.
:param pulumi.Input[str] invoke_arn: The ARN to be used for invoking Lambda Function from API Gateway - to be used in [<code class="docutils literal notranslate"><span class="pre">\</span> <span class="pre">apigateway.Integration\</span> <span class="pre">``](https://www.terraform.io/docs/providers/aws/r/api_gateway_integration.html)'s</span></code>uri<code class="docutils literal notranslate"><span class="pre">:param</span> <span class="pre">pulumi.Input[str]</span> <span class="pre">kms_key_arn:</span> <span class="pre">The</span> <span class="pre">ARN</span> <span class="pre">for</span> <span class="pre">the</span> <span class="pre">KMS</span> <span class="pre">encryption</span> <span class="pre">key.</span>
<span class="pre">:param</span> <span class="pre">pulumi.Input[str]</span> <span class="pre">last_modified:</span> <span class="pre">The</span> <span class="pre">date</span> <span class="pre">this</span> <span class="pre">resource</span> <span class="pre">was</span> <span class="pre">last</span> <span class="pre">modified.</span>
<span class="pre">:param</span> <span class="pre">pulumi.Input[list]</span> <span class="pre">layers:</span> <span class="pre">List</span> <span class="pre">of</span> <span class="pre">Lambda</span> <span class="pre">Layer</span> <span class="pre">Version</span> <span class="pre">ARNs</span> <span class="pre">(maximum</span> <span class="pre">of</span> <span class="pre">5)</span> <span class="pre">to</span> <span class="pre">attach</span> <span class="pre">to</span> <span class="pre">your</span> <span class="pre">Lambda</span> <span class="pre">Function.</span> <span class="pre">See</span> <span class="pre">[Lambda</span> <span class="pre">Layers][10]</span>
<span class="pre">:param</span> <span class="pre">pulumi.Input[float]</span> <span class="pre">memory_size:</span> <span class="pre">Amount</span> <span class="pre">of</span> <span class="pre">memory</span> <span class="pre">in</span> <span class="pre">MB</span> <span class="pre">your</span> <span class="pre">Lambda</span> <span class="pre">Function</span> <span class="pre">can</span> <span class="pre">use</span> <span class="pre">at</span> <span class="pre">runtime.</span> <span class="pre">Defaults</span> <span class="pre">to</span></code>128<code class="docutils literal notranslate"><span class="pre">.</span> <span class="pre">See</span> <span class="pre">[Limits][5]</span>
<span class="pre">:param</span> <span class="pre">pulumi.Input[bool]</span> <span class="pre">publish:</span> <span class="pre">Whether</span> <span class="pre">to</span> <span class="pre">publish</span> <span class="pre">creation/change</span> <span class="pre">as</span> <span class="pre">new</span> <span class="pre">Lambda</span> <span class="pre">Function</span> <span class="pre">Version.</span> <span class="pre">Defaults</span> <span class="pre">to</span></code>false<a href="#id25"><span class="problematic" id="id26">``</span></a>.
:param pulumi.Input[str] qualified_arn: The Amazon Resource Name (ARN) identifying your Lambda Function Version</p>
<blockquote>
<div>(if versioning is enabled via``publish = true<a href="#id27"><span class="problematic" id="id28">``</span></a>).</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>reserved_concurrent_executions</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of reserved concurrent executions for this lambda function. A value of``0<code class="docutils literal notranslate"><span class="pre">disables</span> <span class="pre">lambda</span> <span class="pre">from</span> <span class="pre">being</span> <span class="pre">triggered</span> <span class="pre">and</span></code>-1<code class="docutils literal notranslate"><span class="pre">removes</span> <span class="pre">any</span> <span class="pre">concurrency</span> <span class="pre">limitations.</span> <span class="pre">Defaults</span> <span class="pre">to</span> <span class="pre">Unreserved</span> <span class="pre">Concurrency</span> <span class="pre">Limits</span></code>-1<a href="#id29"><span class="problematic" id="id30">``</span></a>. See [Managing Concurrency][9]</li>
<li><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IAM role attached to the Lambda Function. This governs both who / what can invoke your Lambda Function, as well as what resources our Lambda Function has access to. See [Lambda Permission Model][4] for more details.</li>
<li><strong>runtime</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – See [Runtimes][6] for valid values.</li>
<li><strong>s3_bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The S3 bucket location containing the function’s deployment package. Conflicts with``filename<a href="#id31"><span class="problematic" id="id32">``</span></a>. This bucket must reside in the same AWS region where you are creating the Lambda function.</li>
<li><strong>s3_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The S3 key of an object containing the function’s deployment package. Conflicts with``filename<a href="#id33"><span class="problematic" id="id34">``</span></a>.</li>
<li><strong>s3_object_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The object version containing the function’s deployment package. Conflicts with``filename<a href="#id35"><span class="problematic" id="id36">``</span></a>.</li>
<li><strong>source_code_hash</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either``filename<code class="docutils literal notranslate"><span class="pre">or</span></code>s3_key<code class="docutils literal notranslate"><span class="pre">.</span> <span class="pre">The</span> <span class="pre">usual</span> <span class="pre">way</span> <span class="pre">to</span> <span class="pre">set</span> <span class="pre">this</span> <span class="pre">is</span></code>filebase64sha256(“file.zip”)<code class="docutils literal notranslate"><span class="pre">(this</span> <span class="pre">provider</span> <span class="pre">0.11.12</span> <span class="pre">and</span> <span class="pre">later)</span> <span class="pre">or</span></code>base64sha256(file(“file.zip”))<a href="#id37"><span class="problematic" id="id38">``</span></a>(this provider 0.11.11 and earlier), where “file.zip” is the local filename of the lambda function source archive.</li>
<li><strong>source_code_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size in bytes of the function .zip file.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the object.</li>
<li><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The amount of time your Lambda Function has to run in seconds. Defaults to``3`. See [Limits][5]</li>
<li><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Latest published version of your Lambda Function.</li>
<li><strong>vpc_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Provide this to allow your function to access your VPC. Fields documented below. See [Lambda in VPC][7]</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lambda_function.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lambda_function.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.lambda_.Function.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lambda_.Function.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.lambda_.Function.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lambda_.Function.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.lambda_.GetFunctionResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.lambda_.</code><code class="descname">GetFunctionResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>dead_letter_config=None</em>, <em>description=None</em>, <em>environment=None</em>, <em>function_name=None</em>, <em>handler=None</em>, <em>invoke_arn=None</em>, <em>kms_key_arn=None</em>, <em>last_modified=None</em>, <em>layers=None</em>, <em>memory_size=None</em>, <em>qualified_arn=None</em>, <em>qualifier=None</em>, <em>reserved_concurrent_executions=None</em>, <em>role=None</em>, <em>runtime=None</em>, <em>source_code_hash=None</em>, <em>source_code_size=None</em>, <em>tags=None</em>, <em>timeout=None</em>, <em>tracing_config=None</em>, <em>version=None</em>, <em>vpc_config=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lambda_.GetFunctionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getFunction.</p>
<dl class="attribute">
<dt id="pulumi_aws.lambda_.GetFunctionResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.GetFunctionResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Unqualified (no <code class="docutils literal notranslate"><span class="pre">:QUALIFIER</span></code> or <code class="docutils literal notranslate"><span class="pre">:VERSION</span></code> suffix) Amazon Resource Name (ARN) identifying your Lambda Function. See also <code class="docutils literal notranslate"><span class="pre">qualified_arn</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.GetFunctionResult.dead_letter_config">
<code class="descname">dead_letter_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.GetFunctionResult.dead_letter_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Configure the function’s <em>dead letter queue</em>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.GetFunctionResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.GetFunctionResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of what your Lambda Function does.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.GetFunctionResult.environment">
<code class="descname">environment</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.GetFunctionResult.environment" title="Permalink to this definition">¶</a></dt>
<dd><p>The Lambda environment’s configuration settings.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.GetFunctionResult.handler">
<code class="descname">handler</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.GetFunctionResult.handler" title="Permalink to this definition">¶</a></dt>
<dd><p>The function entrypoint in your code.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.GetFunctionResult.invoke_arn">
<code class="descname">invoke_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.GetFunctionResult.invoke_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN to be used for invoking Lambda Function from API Gateway.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.GetFunctionResult.kms_key_arn">
<code class="descname">kms_key_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.GetFunctionResult.kms_key_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN for the KMS encryption key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.GetFunctionResult.last_modified">
<code class="descname">last_modified</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.GetFunctionResult.last_modified" title="Permalink to this definition">¶</a></dt>
<dd><p>The date this resource was last modified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.GetFunctionResult.layers">
<code class="descname">layers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.GetFunctionResult.layers" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Lambda Layer ARNs attached to your Lambda Function.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.GetFunctionResult.memory_size">
<code class="descname">memory_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.GetFunctionResult.memory_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Amount of memory in MB your Lambda Function can use at runtime.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.GetFunctionResult.qualified_arn">
<code class="descname">qualified_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.GetFunctionResult.qualified_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Qualified (<code class="docutils literal notranslate"><span class="pre">:QUALIFIER</span></code> or <code class="docutils literal notranslate"><span class="pre">:VERSION</span></code> suffix) Amazon Resource Name (ARN) identifying your Lambda Function. See also <code class="docutils literal notranslate"><span class="pre">arn</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.GetFunctionResult.reserved_concurrent_executions">
<code class="descname">reserved_concurrent_executions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.GetFunctionResult.reserved_concurrent_executions" title="Permalink to this definition">¶</a></dt>
<dd><p>The amount of reserved concurrent executions for this lambda function or <code class="docutils literal notranslate"><span class="pre">-1</span></code> if unreserved.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.GetFunctionResult.role">
<code class="descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.GetFunctionResult.role" title="Permalink to this definition">¶</a></dt>
<dd><p>IAM role attached to the Lambda Function.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.GetFunctionResult.runtime">
<code class="descname">runtime</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.GetFunctionResult.runtime" title="Permalink to this definition">¶</a></dt>
<dd><p>The runtime environment for the Lambda function..</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.GetFunctionResult.source_code_hash">
<code class="descname">source_code_hash</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.GetFunctionResult.source_code_hash" title="Permalink to this definition">¶</a></dt>
<dd><p>Base64-encoded representation of raw SHA-256 sum of the zip file.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.GetFunctionResult.source_code_size">
<code class="descname">source_code_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.GetFunctionResult.source_code_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size in bytes of the function .zip file.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.GetFunctionResult.timeout">
<code class="descname">timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.GetFunctionResult.timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The function execution time at which Lambda should terminate the function.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.GetFunctionResult.tracing_config">
<code class="descname">tracing_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.GetFunctionResult.tracing_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Tracing settings of the function.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.GetFunctionResult.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.GetFunctionResult.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the Lambda function.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.GetFunctionResult.vpc_config">
<code class="descname">vpc_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.GetFunctionResult.vpc_config" title="Permalink to this definition">¶</a></dt>
<dd><p>VPC configuration associated with your Lambda function.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.GetFunctionResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.GetFunctionResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.lambda_.GetInvocationResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.lambda_.</code><code class="descname">GetInvocationResult</code><span class="sig-paren">(</span><em>function_name=None</em>, <em>input=None</em>, <em>qualifier=None</em>, <em>result=None</em>, <em>result_map=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lambda_.GetInvocationResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getInvocation.</p>
<dl class="attribute">
<dt id="pulumi_aws.lambda_.GetInvocationResult.result">
<code class="descname">result</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.GetInvocationResult.result" title="Permalink to this definition">¶</a></dt>
<dd><p>String result of the lambda function invocation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.GetInvocationResult.result_map">
<code class="descname">result_map</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.GetInvocationResult.result_map" title="Permalink to this definition">¶</a></dt>
<dd><p>This field is set only if result is a map of primitive types, where the map is string keys and string values.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.GetInvocationResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.GetInvocationResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.lambda_.GetLayerVersionResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.lambda_.</code><code class="descname">GetLayerVersionResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>compatible_runtime=None</em>, <em>compatible_runtimes=None</em>, <em>created_date=None</em>, <em>description=None</em>, <em>layer_arn=None</em>, <em>layer_name=None</em>, <em>license_info=None</em>, <em>source_code_hash=None</em>, <em>source_code_size=None</em>, <em>version=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lambda_.GetLayerVersionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getLayerVersion.</p>
<dl class="attribute">
<dt id="pulumi_aws.lambda_.GetLayerVersionResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.GetLayerVersionResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the Lambda Layer with version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.GetLayerVersionResult.compatible_runtimes">
<code class="descname">compatible_runtimes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.GetLayerVersionResult.compatible_runtimes" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of [Runtimes][1] the specific Lambda Layer version is compatible with.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.GetLayerVersionResult.created_date">
<code class="descname">created_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.GetLayerVersionResult.created_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The date this resource was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.GetLayerVersionResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.GetLayerVersionResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the specific Lambda Layer version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.GetLayerVersionResult.layer_arn">
<code class="descname">layer_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.GetLayerVersionResult.layer_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the Lambda Layer without version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.GetLayerVersionResult.license_info">
<code class="descname">license_info</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.GetLayerVersionResult.license_info" title="Permalink to this definition">¶</a></dt>
<dd><p>License info associated with the specific Lambda Layer version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.GetLayerVersionResult.source_code_hash">
<code class="descname">source_code_hash</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.GetLayerVersionResult.source_code_hash" title="Permalink to this definition">¶</a></dt>
<dd><p>Base64-encoded representation of raw SHA-256 sum of the zip file.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.GetLayerVersionResult.source_code_size">
<code class="descname">source_code_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.GetLayerVersionResult.source_code_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size in bytes of the function .zip file.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.GetLayerVersionResult.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.GetLayerVersionResult.version" title="Permalink to this definition">¶</a></dt>
<dd><p>This Lamba Layer version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.GetLayerVersionResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.GetLayerVersionResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.lambda_.LayerVersion">
<em class="property">class </em><code class="descclassname">pulumi_aws.lambda_.</code><code class="descname">LayerVersion</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>compatible_runtimes=None</em>, <em>description=None</em>, <em>code=None</em>, <em>layer_name=None</em>, <em>license_info=None</em>, <em>s3_bucket=None</em>, <em>s3_key=None</em>, <em>s3_object_version=None</em>, <em>source_code_hash=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lambda_.LayerVersion" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Lambda Layer Version resource. Lambda Layers allow you to reuse shared bits of code across multiple lambda functions.</p>
<p>For information about Lambda Layers and how to use them, see [AWS Lambda Layers][1]</p>
<p>AWS Lambda Layers expect source code to be provided as a deployment package whose structure varies depending on which <code class="docutils literal notranslate"><span class="pre">compatible_runtimes</span></code> this layer specifies.
See [Runtimes][2] for the valid values of <code class="docutils literal notranslate"><span class="pre">compatible_runtimes</span></code>.</p>
<p>Once you have created your deployment package you can specify it either directly as a local file (using the <code class="docutils literal notranslate"><span class="pre">filename</span></code> argument) or
indirectly via Amazon S3 (using the <code class="docutils literal notranslate"><span class="pre">s3_bucket</span></code>, <code class="docutils literal notranslate"><span class="pre">s3_key</span></code> and <code class="docutils literal notranslate"><span class="pre">s3_object_version</span></code> arguments). When providing the deployment
package via S3 it may be useful to use the <code class="docutils literal notranslate"><span class="pre">s3.BucketObject</span></code> resource to upload it.</p>
<p>For larger deployment packages it is recommended by Amazon to upload via S3, since the S3 API has better support for uploading
large files efficiently.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>compatible*runtimes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>A list of [Runtimes][2] this layer is compatible with. Up to 5 runtimes can be specified.</p>
</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of what your Lambda Layer does.</li>
<li><strong>code</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.Archive</em><em>]</em>) – The path to the function’s deployment package within the local filesystem. If defined, The <cite>s3*`</cite>-prefixed options cannot be used.</li>
<li><strong>layer_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for your Lambda Layer</li>
<li><strong>license_info</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – License info for your Lambda Layer. See [License Info][3].</li>
<li><strong>s3_bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The S3 bucket location containing the function’s deployment package. Conflicts with``filename<a href="#id41"><span class="problematic" id="id42">``</span></a>. This bucket must reside in the same AWS region where you are creating the Lambda function.</li>
<li><strong>s3_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The S3 key of an object containing the function’s deployment package. Conflicts with``filename<a href="#id43"><span class="problematic" id="id44">``</span></a>.</li>
<li><strong>s3_object_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The object version containing the function’s deployment package. Conflicts with``filename<a href="#id45"><span class="problematic" id="id46">``</span></a>.</li>
<li><strong>source_code_hash</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either``filename<code class="docutils literal notranslate"><span class="pre">or</span></code>s3_key<code class="docutils literal notranslate"><span class="pre">.</span> <span class="pre">The</span> <span class="pre">usual</span> <span class="pre">way</span> <span class="pre">to</span> <span class="pre">set</span> <span class="pre">this</span> <span class="pre">is</span></code>${filebase64sha256(“file.zip”)}<code class="docutils literal notranslate"><span class="pre">(this</span> <span class="pre">provider</span> <span class="pre">0.11.12</span> <span class="pre">or</span> <span class="pre">later)</span> <span class="pre">or</span></code>${base64sha256(file(“file.zip”))}` (this provider 0.11.11 and earlier), where “file.zip” is the local filename of the lambda layer source archive.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lambda_layer_version.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lambda_layer_version.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.lambda_.LayerVersion.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.LayerVersion.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the Lambda Layer with version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.LayerVersion.compatible_runtimes">
<code class="descname">compatible_runtimes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.LayerVersion.compatible_runtimes" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of [Runtimes][2] this layer is compatible with. Up to 5 runtimes can be specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.LayerVersion.created_date">
<code class="descname">created_date</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.LayerVersion.created_date" title="Permalink to this definition">¶</a></dt>
<dd><p>The date this resource was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.LayerVersion.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.LayerVersion.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of what your Lambda Layer does.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.LayerVersion.code">
<code class="descname">code</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.LayerVersion.code" title="Permalink to this definition">¶</a></dt>
<dd><p>The path to the function’s deployment package within the local filesystem. If defined, The <code class="docutils literal notranslate"><span class="pre">s3_</span></code>-prefixed options cannot be used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.LayerVersion.layer_arn">
<code class="descname">layer_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.LayerVersion.layer_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the Lambda Layer without version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.LayerVersion.layer_name">
<code class="descname">layer_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.LayerVersion.layer_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for your Lambda Layer</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.LayerVersion.license_info">
<code class="descname">license_info</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.LayerVersion.license_info" title="Permalink to this definition">¶</a></dt>
<dd><p>License info for your Lambda Layer. See [License Info][3].</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.LayerVersion.s3_bucket">
<code class="descname">s3_bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.LayerVersion.s3_bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The S3 bucket location containing the function’s deployment package. Conflicts with <code class="docutils literal notranslate"><span class="pre">filename</span></code>. This bucket must reside in the same AWS region where you are creating the Lambda function.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.LayerVersion.s3_key">
<code class="descname">s3_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.LayerVersion.s3_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The S3 key of an object containing the function’s deployment package. Conflicts with <code class="docutils literal notranslate"><span class="pre">filename</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.LayerVersion.s3_object_version">
<code class="descname">s3_object_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.LayerVersion.s3_object_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The object version containing the function’s deployment package. Conflicts with <code class="docutils literal notranslate"><span class="pre">filename</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.LayerVersion.source_code_hash">
<code class="descname">source_code_hash</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.LayerVersion.source_code_hash" title="Permalink to this definition">¶</a></dt>
<dd><p>Used to trigger updates. Must be set to a base64-encoded SHA256 hash of the package file specified with either <code class="docutils literal notranslate"><span class="pre">filename</span></code> or <code class="docutils literal notranslate"><span class="pre">s3_key</span></code>. The usual way to set this is <code class="docutils literal notranslate"><span class="pre">${filebase64sha256(&quot;file.zip&quot;)}</span></code> (this provider 0.11.12 or later) or <code class="docutils literal notranslate"><span class="pre">${base64sha256(file(&quot;file.zip&quot;))}</span></code> (this provider 0.11.11 and earlier), where “file.zip” is the local filename of the lambda layer source archive.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.LayerVersion.source_code_size">
<code class="descname">source_code_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.LayerVersion.source_code_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size in bytes of the function .zip file.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.LayerVersion.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.LayerVersion.version" title="Permalink to this definition">¶</a></dt>
<dd><p>This Lamba Layer version.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_aws.lambda_.LayerVersion.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>arn=None</em>, <em>compatible_runtimes=None</em>, <em>created_date=None</em>, <em>description=None</em>, <em>code=None</em>, <em>layer_arn=None</em>, <em>layer_name=None</em>, <em>license_info=None</em>, <em>s3_bucket=None</em>, <em>s3_key=None</em>, <em>s3_object_version=None</em>, <em>source_code_hash=None</em>, <em>source_code_size=None</em>, <em>version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lambda_.LayerVersion.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LayerVersion resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] arn: The Amazon Resource Name (ARN) of the Lambda Layer with version.
:param pulumi.Input[list] compatible_runtimes: A list of [Runtimes][2] this layer is compatible with. Up to 5 runtimes can be specified.
:param pulumi.Input[str] created<em>date: The date this resource was created.
:param pulumi.Input[str] description: Description of what your Lambda Layer does.
:param pulumi.Input[pulumi.Archive] code: The path to the function’s deployment package within the local filesystem. If defined, The `s3</em><code class="docutils literal notranslate"><span class="pre">-prefixed</span> <span class="pre">options</span> <span class="pre">cannot</span> <span class="pre">be</span> <span class="pre">used.</span>
<span class="pre">:param</span> <span class="pre">pulumi.Input[str]</span> <span class="pre">layer_arn:</span> <span class="pre">The</span> <span class="pre">Amazon</span> <span class="pre">Resource</span> <span class="pre">Name</span> <span class="pre">(ARN)</span> <span class="pre">of</span> <span class="pre">the</span> <span class="pre">Lambda</span> <span class="pre">Layer</span> <span class="pre">without</span> <span class="pre">version.</span>
<span class="pre">:param</span> <span class="pre">pulumi.Input[str]</span> <span class="pre">layer_name:</span> <span class="pre">A</span> <span class="pre">unique</span> <span class="pre">name</span> <span class="pre">for</span> <span class="pre">your</span> <span class="pre">Lambda</span> <span class="pre">Layer</span>
<span class="pre">:param</span> <span class="pre">pulumi.Input[str]</span> <span class="pre">license_info:</span> <span class="pre">License</span> <span class="pre">info</span> <span class="pre">for</span> <span class="pre">your</span> <span class="pre">Lambda</span> <span class="pre">Layer.</span> <span class="pre">See</span> <span class="pre">[License</span> <span class="pre">Info][3].</span>
<span class="pre">:param</span> <span class="pre">pulumi.Input[str]</span> <span class="pre">s3_bucket:</span> <span class="pre">The</span> <span class="pre">S3</span> <span class="pre">bucket</span> <span class="pre">location</span> <span class="pre">containing</span> <span class="pre">the</span> <span class="pre">function's</span> <span class="pre">deployment</span> <span class="pre">package.</span> <span class="pre">Conflicts</span> <span class="pre">with</span></code>filename<code class="docutils literal notranslate"><span class="pre">.</span> <span class="pre">This</span> <span class="pre">bucket</span> <span class="pre">must</span> <span class="pre">reside</span> <span class="pre">in</span> <span class="pre">the</span> <span class="pre">same</span> <span class="pre">AWS</span> <span class="pre">region</span> <span class="pre">where</span> <span class="pre">you</span> <span class="pre">are</span> <span class="pre">creating</span> <span class="pre">the</span> <span class="pre">Lambda</span> <span class="pre">function.</span>
<span class="pre">:param</span> <span class="pre">pulumi.Input[str]</span> <span class="pre">s3_key:</span> <span class="pre">The</span> <span class="pre">S3</span> <span class="pre">key</span> <span class="pre">of</span> <span class="pre">an</span> <span class="pre">object</span> <span class="pre">containing</span> <span class="pre">the</span> <span class="pre">function's</span> <span class="pre">deployment</span> <span class="pre">package.</span> <span class="pre">Conflicts</span> <span class="pre">with</span></code>filename<code class="docutils literal notranslate"><span class="pre">.</span>
<span class="pre">:param</span> <span class="pre">pulumi.Input[str]</span> <span class="pre">s3_object_version:</span> <span class="pre">The</span> <span class="pre">object</span> <span class="pre">version</span> <span class="pre">containing</span> <span class="pre">the</span> <span class="pre">function's</span> <span class="pre">deployment</span> <span class="pre">package.</span> <span class="pre">Conflicts</span> <span class="pre">with</span></code>filename<code class="docutils literal notranslate"><span class="pre">.</span>
<span class="pre">:param</span> <span class="pre">pulumi.Input[str]</span> <span class="pre">source_code_hash:</span> <span class="pre">Used</span> <span class="pre">to</span> <span class="pre">trigger</span> <span class="pre">updates.</span> <span class="pre">Must</span> <span class="pre">be</span> <span class="pre">set</span> <span class="pre">to</span> <span class="pre">a</span> <span class="pre">base64-encoded</span> <span class="pre">SHA256</span> <span class="pre">hash</span> <span class="pre">of</span> <span class="pre">the</span> <span class="pre">package</span> <span class="pre">file</span> <span class="pre">specified</span> <span class="pre">with</span> <span class="pre">either</span></code>filename<code class="docutils literal notranslate"><span class="pre">or</span></code>s3_key<code class="docutils literal notranslate"><span class="pre">.</span> <span class="pre">The</span> <span class="pre">usual</span> <span class="pre">way</span> <span class="pre">to</span> <span class="pre">set</span> <span class="pre">this</span> <span class="pre">is</span></code>${filebase64sha256(“file.zip”)}<code class="docutils literal notranslate"><span class="pre">(this</span> <span class="pre">provider</span> <span class="pre">0.11.12</span> <span class="pre">or</span> <span class="pre">later)</span> <span class="pre">or</span></code>${base64sha256(file(“file.zip”))}` (this provider 0.11.11 and earlier), where “file.zip” is the local filename of the lambda layer source archive.
:param pulumi.Input[float] source_code_size: The size in bytes of the function .zip file.
:param pulumi.Input[str] version: This Lamba Layer version.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lambda_layer_version.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lambda_layer_version.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.lambda_.LayerVersion.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lambda_.LayerVersion.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.lambda_.LayerVersion.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lambda_.LayerVersion.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.lambda_.Permission">
<em class="property">class </em><code class="descclassname">pulumi_aws.lambda_.</code><code class="descname">Permission</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>action=None</em>, <em>event_source_token=None</em>, <em>function=None</em>, <em>principal=None</em>, <em>qualifier=None</em>, <em>source_account=None</em>, <em>source_arn=None</em>, <em>statement_id=None</em>, <em>statement_id_prefix=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lambda_.Permission" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a Lambda permission to allow external sources invoking the Lambda function
(e.g. CloudWatch Event Rule, SNS or S3).</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS Lambda action you want to allow in this statement. (e.g. <code class="docutils literal notranslate"><span class="pre">lambda:InvokeFunction</span></code>)</li>
<li><strong>event_source_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Event Source Token to validate.  Used with [Alexa Skills][1].</li>
<li><strong>function</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Lambda function whose resource policy you are updating</li>
<li><strong>principal</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The principal who is getting this permission.
e.g. <code class="docutils literal notranslate"><span class="pre">s3.amazonaws.com</span></code>, an AWS account ID, or any valid AWS service principal
such as <code class="docutils literal notranslate"><span class="pre">events.amazonaws.com</span></code> or <code class="docutils literal notranslate"><span class="pre">sns.amazonaws.com</span></code>.</li>
<li><strong>qualifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Query parameter to specify function version or alias name.
The permission will then apply to the specific qualified ARN.
e.g. <code class="docutils literal notranslate"><span class="pre">arn:aws:lambda:aws-region:acct-id:function:function-name:2</span></code></li>
<li><strong>source_account</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This parameter is used for S3 and SES. The AWS account ID (without a hyphen) of the source owner.</li>
<li><strong>source_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When granting Amazon S3 or CloudWatch Events permission to
invoke your function, you should specify this field with the Amazon Resource Name (ARN)
for the S3 Bucket or CloudWatch Events Rule as its value.  This ensures that only events
generated from the specified bucket or rule can invoke the function.
API Gateway ARNs have a unique structure described
<a class="reference external" href="http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-control-access-using-iam-policies-to-invoke-api.html">here</a>.</li>
<li><strong>statement_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique statement identifier. By default generated by this provider.</li>
<li><strong>statement_id_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A statement identifier prefix. This provider will generate a unique suffix. Conflicts with <code class="docutils literal notranslate"><span class="pre">statement_id</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lambda_permission.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lambda_permission.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.lambda_.Permission.action">
<code class="descname">action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Permission.action" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS Lambda action you want to allow in this statement. (e.g. <code class="docutils literal notranslate"><span class="pre">lambda:InvokeFunction</span></code>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Permission.event_source_token">
<code class="descname">event_source_token</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Permission.event_source_token" title="Permalink to this definition">¶</a></dt>
<dd><p>The Event Source Token to validate.  Used with [Alexa Skills][1].</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Permission.function">
<code class="descname">function</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Permission.function" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the Lambda function whose resource policy you are updating</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Permission.principal">
<code class="descname">principal</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Permission.principal" title="Permalink to this definition">¶</a></dt>
<dd><p>The principal who is getting this permission.
e.g. <code class="docutils literal notranslate"><span class="pre">s3.amazonaws.com</span></code>, an AWS account ID, or any valid AWS service principal
such as <code class="docutils literal notranslate"><span class="pre">events.amazonaws.com</span></code> or <code class="docutils literal notranslate"><span class="pre">sns.amazonaws.com</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Permission.qualifier">
<code class="descname">qualifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Permission.qualifier" title="Permalink to this definition">¶</a></dt>
<dd><p>Query parameter to specify function version or alias name.
The permission will then apply to the specific qualified ARN.
e.g. <code class="docutils literal notranslate"><span class="pre">arn:aws:lambda:aws-region:acct-id:function:function-name:2</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Permission.source_account">
<code class="descname">source_account</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Permission.source_account" title="Permalink to this definition">¶</a></dt>
<dd><p>This parameter is used for S3 and SES. The AWS account ID (without a hyphen) of the source owner.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Permission.source_arn">
<code class="descname">source_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Permission.source_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>When granting Amazon S3 or CloudWatch Events permission to
invoke your function, you should specify this field with the Amazon Resource Name (ARN)
for the S3 Bucket or CloudWatch Events Rule as its value.  This ensures that only events
generated from the specified bucket or rule can invoke the function.
API Gateway ARNs have a unique structure described
<a class="reference external" href="http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-control-access-using-iam-policies-to-invoke-api.html">here</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Permission.statement_id">
<code class="descname">statement_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Permission.statement_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique statement identifier. By default generated by this provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.lambda_.Permission.statement_id_prefix">
<code class="descname">statement_id_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.lambda_.Permission.statement_id_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>A statement identifier prefix. This provider will generate a unique suffix. Conflicts with <code class="docutils literal notranslate"><span class="pre">statement_id</span></code>.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_aws.lambda_.Permission.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>action=None</em>, <em>event_source_token=None</em>, <em>function=None</em>, <em>principal=None</em>, <em>qualifier=None</em>, <em>source_account=None</em>, <em>source_arn=None</em>, <em>statement_id=None</em>, <em>statement_id_prefix=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lambda_.Permission.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Permission resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] action: The AWS Lambda action you want to allow in this statement. (e.g. <code class="docutils literal notranslate"><span class="pre">lambda:InvokeFunction</span></code>)
:param pulumi.Input[str] event_source_token: The Event Source Token to validate.  Used with [Alexa Skills][1].
:param pulumi.Input[str] function: Name of the Lambda function whose resource policy you are updating
:param pulumi.Input[str] principal: The principal who is getting this permission.</p>
<blockquote>
<div>e.g. <code class="docutils literal notranslate"><span class="pre">s3.amazonaws.com</span></code>, an AWS account ID, or any valid AWS service principal
such as <code class="docutils literal notranslate"><span class="pre">events.amazonaws.com</span></code> or <code class="docutils literal notranslate"><span class="pre">sns.amazonaws.com</span></code>.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>qualifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Query parameter to specify function version or alias name.
The permission will then apply to the specific qualified ARN.
e.g. <code class="docutils literal notranslate"><span class="pre">arn:aws:lambda:aws-region:acct-id:function:function-name:2</span></code></li>
<li><strong>source_account</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This parameter is used for S3 and SES. The AWS account ID (without a hyphen) of the source owner.</li>
<li><strong>source_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>When granting Amazon S3 or CloudWatch Events permission to
invoke your function, you should specify this field with the Amazon Resource Name (ARN)
for the S3 Bucket or CloudWatch Events Rule as its value.  This ensures that only events
generated from the specified bucket or rule can invoke the function.
API Gateway ARNs have a unique structure described
<a class="reference external" href="http://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-control-access-using-iam-policies-to-invoke-api.html">here</a>.</p>
</li>
<li><strong>statement_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique statement identifier. By default generated by this provider.</li>
<li><strong>statement_id_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A statement identifier prefix. This provider will generate a unique suffix. Conflicts with <code class="docutils literal notranslate"><span class="pre">statement_id</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lambda_permission.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/lambda_permission.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.lambda_.Permission.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lambda_.Permission.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.lambda_.Permission.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lambda_.Permission.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.lambda_.get_function">
<code class="descclassname">pulumi_aws.lambda_.</code><code class="descname">get_function</code><span class="sig-paren">(</span><em>function_name=None</em>, <em>qualifier=None</em>, <em>tags=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lambda_.get_function" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about a Lambda Function.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/lambda_function.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/lambda_function.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.lambda_.get_invocation">
<code class="descclassname">pulumi_aws.lambda_.</code><code class="descname">get_invocation</code><span class="sig-paren">(</span><em>function_name=None</em>, <em>input=None</em>, <em>qualifier=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lambda_.get_invocation" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to invoke custom lambda functions as data source.
The lambda function is invoked with <a class="reference external" href="https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html#API_Invoke_RequestSyntax">RequestResponse</a>
invocation type.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/lambda_invocation.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/lambda_invocation.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_aws.lambda_.get_layer_version">
<code class="descclassname">pulumi_aws.lambda_.</code><code class="descname">get_layer_version</code><span class="sig-paren">(</span><em>compatible_runtime=None</em>, <em>layer_name=None</em>, <em>version=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.lambda_.get_layer_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides information about a Lambda Layer Version.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/lambda_layer_version.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/lambda_layer_version.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
