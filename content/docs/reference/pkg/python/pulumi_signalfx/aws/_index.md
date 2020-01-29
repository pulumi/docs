---
title: Module aws
title_tag: Module aws | Package pulumi_signalfx | Python SDK
linktitle: aws
notitle: true
---

<div class="section" id="aws">
<h1>aws<a class="headerlink" href="#aws" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-signalfx">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-signalfx/issues">pulumi/pulumi-signalfx repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-signalfx/issues">terraform-providers/terraform-provider-signalfx repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_signalfx.aws"></span><dl class="class">
<dt id="pulumi_signalfx.aws.ExternalIntegration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_signalfx.aws.</code><code class="sig-name descname">ExternalIntegration</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.aws.ExternalIntegration" title="Permalink to this definition">¶</a></dt>
<dd><p>SignalFx AWS CloudWatch integrations using Role ARNs. For help with this integration see <a class="reference external" href="https://docs.signalfx.com/en/latest/integrations/amazon-web-services.html#connect-to-aws">Connect to AWS CloudWatch</a>.</p>
<p><strong>Note:</strong> When managing integrations you’ll need to use an admin token to authenticate the SignalFx provider.</p>
<blockquote>
<div><p><strong>WARNING</strong> This resource implements a part of a workflow. You must use it with <code class="docutils literal notranslate"><span class="pre">aws.Integration</span></code>. Check with SignalFx support for your realm’s AWS account id.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this integration</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-signalfx/blob/master/website/docs/r/aws_external_integration.html.markdown">https://github.com/terraform-providers/terraform-provider-signalfx/blob/master/website/docs/r/aws_external_integration.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_signalfx.aws.ExternalIntegration.external_id">
<code class="sig-name descname">external_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.ExternalIntegration.external_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The external ID to use with your IAM role and with <code class="docutils literal notranslate"><span class="pre">aws.Integration</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.aws.ExternalIntegration.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.ExternalIntegration.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of this integration</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.aws.ExternalIntegration.signalfx_aws_account">
<code class="sig-name descname">signalfx_aws_account</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.ExternalIntegration.signalfx_aws_account" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS Account ARN to use with your policies/roles, provided by SignalFx.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_signalfx.aws.ExternalIntegration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">external_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">signalfx_aws_account=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.aws.ExternalIntegration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ExternalIntegration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>external_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The external ID to use with your IAM role and with <code class="docutils literal notranslate"><span class="pre">aws.Integration</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this integration</p></li>
<li><p><strong>signalfx_aws_account</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS Account ARN to use with your policies/roles, provided by SignalFx.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-signalfx/blob/master/website/docs/r/aws_external_integration.html.markdown">https://github.com/terraform-providers/terraform-provider-signalfx/blob/master/website/docs/r/aws_external_integration.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_signalfx.aws.ExternalIntegration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.aws.ExternalIntegration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.aws.ExternalIntegration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.aws.ExternalIntegration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.aws.Integration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_signalfx.aws.</code><code class="sig-name descname">Integration</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">custom_cloudwatch_namespaces=None</em>, <em class="sig-param">custom_namespace_sync_rules=None</em>, <em class="sig-param">enable_aws_usage=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">external_id=None</em>, <em class="sig-param">import_cloud_watch=None</em>, <em class="sig-param">integration_id=None</em>, <em class="sig-param">key=None</em>, <em class="sig-param">namespace_sync_rules=None</em>, <em class="sig-param">poll_rate=None</em>, <em class="sig-param">regions=None</em>, <em class="sig-param">role_arn=None</em>, <em class="sig-param">services=None</em>, <em class="sig-param">token=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.aws.Integration" title="Permalink to this definition">¶</a></dt>
<dd><p>SignalFx AWS CloudWatch integrations. For help with this integration see <a class="reference external" href="https://docs.signalfx.com/en/latest/integrations/amazon-web-services.html#monitor-amazon-web-services">Monitoring Amazon Web Services</a>.</p>
<p><strong>Note:</strong> When managing integrations you’ll need to use an admin token to authenticate the SignalFx provider.</p>
<blockquote>
<div><p><strong>WARNING</strong> This resource implements a part of a workflow. You must use it with one of either <code class="docutils literal notranslate"><span class="pre">aws.ExternalIntegration</span></code> or <code class="docutils literal notranslate"><span class="pre">aws.TokenIntegration</span></code>.</p>
</div></blockquote>
<p>Fields that expect an AWS service/namespace will work with one of: “AWS/ApiGateway” “AWS/AppStream” “AWS/AutoScaling” “AWS/Billing” “AWS/CloudFront” “AWS/CloudSearch” “AWS/Events” “AWS/Logs” “AWS/Connect” “AWS/DMS” “AWS/DX” “AWS/DynamoDB” “AWS/EC2” “AWS/EC2Spot” “AWS/ECS” “AWS/ElasticBeanstalk” “AWS/EBS” “AWS/EFS” “AWS/ELB” “AWS/ApplicationELB” “AWS/NetworkELB” “AWS/ElasticTranscoder” “AWS/ElastiCache” “AWS/ES” “AWS/ElasticMapReduce” “AWS/GameLift” “AWS/Inspector” “AWS/IoT” “AWS/KMS” “AWS/KinesisAnalytics” “AWS/Firehose” “AWS/Kinesis” “AWS/KinesisVideo” “AWS/Lambda” “AWS/Lex” “AWS/ML” “AWS/OpsWorks” “AWS/Polly” “AWS/Redshift” “AWS/RDS” “AWS/Route53” “AWS/SageMaker” “AWS/DDoSProtection” “AWS/SES” “AWS/SNS” “AWS/SQS” “AWS/S3” “AWS/SWF” “AWS/States” “AWS/StorageGateway” “AWS/Translate” “AWS/NATGateway” “AWS/VPN (VPN)” “WAF” “AWS/WorkSpaces”.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>custom_cloudwatch_namespaces</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of custom AWS CloudWatch namespaces to monitor. Custom namespaces contain custom metrics that you define in AWS; SignalFx imports the metrics so you can monitor them.</p></li>
<li><p><strong>custom_namespace_sync_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Each element controls the data collected by SignalFx for the specified namespace. Conflicts with the <code class="docutils literal notranslate"><span class="pre">custom_cloudwatch_namespaces</span></code> property.</p></li>
<li><p><strong>enable_aws_usage</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag that controls how SignalFx imports usage metrics from AWS to use with AWS Cost Optimizer. If <code class="docutils literal notranslate"><span class="pre">true</span></code>, SignalFx imports the metrics.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the integration is enabled.</p></li>
<li><p><strong>external_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <code class="docutils literal notranslate"><span class="pre">external_id</span></code> property from one of a <code class="docutils literal notranslate"><span class="pre">aws.ExternalIntegration</span></code> or <code class="docutils literal notranslate"><span class="pre">aws.TokenIntegration</span></code></p></li>
<li><p><strong>import_cloud_watch</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag that controls how SignalFx imports Cloud Watch metrics. If true, SignalFx imports Cloud Watch metrics from AWS.</p></li>
<li><p><strong>integration_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of one of a <code class="docutils literal notranslate"><span class="pre">aws.ExternalIntegration</span></code> or <code class="docutils literal notranslate"><span class="pre">aws.TokenIntegration</span></code>.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If you specify <code class="docutils literal notranslate"><span class="pre">auth_method</span> <span class="pre">=</span> <span class="pre">&quot;SecurityToken&quot;</span></code> in your request to create an AWS integration object, use this property to specify the key.</p></li>
<li><p><strong>namespace_sync_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Each element in the array is an object that contains an AWS namespace name and a filter that controls the data that SignalFx collects for the namespace. Conflicts with the <code class="docutils literal notranslate"><span class="pre">services</span></code> property. If you don’t specify either property, SignalFx syncs all data in all AWS namespaces.</p></li>
<li><p><strong>poll_rate</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – AWS poll rate (in seconds). One of <code class="docutils literal notranslate"><span class="pre">60</span></code> or <code class="docutils literal notranslate"><span class="pre">300</span></code>.</p></li>
<li><p><strong>regions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of AWS regions that SignalFx should monitor.</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Role ARN that you add to an existing AWS integration object. <strong>Note</strong>: Ensure you use the <code class="docutils literal notranslate"><span class="pre">arn</span></code> property of your role, not the id!</p></li>
<li><p><strong>services</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of AWS services that you want SignalFx to monitor. Each element is a string designating an AWS service. Conflicts with <code class="docutils literal notranslate"><span class="pre">namespace_sync_rule</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>custom_namespace_sync_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">defaultAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Controls the SignalFx default behavior for processing data from an AWS namespace. If you do specify a filter, use this property to control how SignalFx treats data that doesn’t match the filter. The available actions are one of <code class="docutils literal notranslate"><span class="pre">&quot;Include&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Exclude&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filterAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Controls how SignalFx processes data from a custom AWS namespace. The available actions are one of <code class="docutils literal notranslate"><span class="pre">&quot;Include&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Exclude&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filterSource</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Expression that selects the data that SignalFx should sync for the custom namespace associated with this sync rule. The expression uses the syntax defined for the SignalFlow <code class="docutils literal notranslate"><span class="pre">filter()</span></code> function; it can be any valid SignalFlow filter expression.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An AWS custom namespace having custom AWS metrics that you want to sync with SignalFx. See the AWS documentation on publishing metrics for more information.</p></li>
</ul>
<p>The <strong>namespace_sync_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">defaultAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Controls the SignalFx default behavior for processing data from an AWS namespace. If you do specify a filter, use this property to control how SignalFx treats data that doesn’t match the filter. The available actions are one of <code class="docutils literal notranslate"><span class="pre">&quot;Include&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Exclude&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filterAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Controls how SignalFx processes data from a custom AWS namespace. The available actions are one of <code class="docutils literal notranslate"><span class="pre">&quot;Include&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Exclude&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filterSource</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Expression that selects the data that SignalFx should sync for the custom namespace associated with this sync rule. The expression uses the syntax defined for the SignalFlow <code class="docutils literal notranslate"><span class="pre">filter()</span></code> function; it can be any valid SignalFlow filter expression.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An AWS custom namespace having custom AWS metrics that you want to sync with SignalFx. See the AWS documentation on publishing metrics for more information.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-signalfx/blob/master/website/docs/r/aws_integration.html.markdown">https://github.com/terraform-providers/terraform-provider-signalfx/blob/master/website/docs/r/aws_integration.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_signalfx.aws.Integration.custom_cloudwatch_namespaces">
<code class="sig-name descname">custom_cloudwatch_namespaces</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.Integration.custom_cloudwatch_namespaces" title="Permalink to this definition">¶</a></dt>
<dd><p>List of custom AWS CloudWatch namespaces to monitor. Custom namespaces contain custom metrics that you define in AWS; SignalFx imports the metrics so you can monitor them.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.aws.Integration.custom_namespace_sync_rules">
<code class="sig-name descname">custom_namespace_sync_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.Integration.custom_namespace_sync_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>Each element controls the data collected by SignalFx for the specified namespace. Conflicts with the <code class="docutils literal notranslate"><span class="pre">custom_cloudwatch_namespaces</span></code> property.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">defaultAction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Controls the SignalFx default behavior for processing data from an AWS namespace. If you do specify a filter, use this property to control how SignalFx treats data that doesn’t match the filter. The available actions are one of <code class="docutils literal notranslate"><span class="pre">&quot;Include&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Exclude&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filterAction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Controls how SignalFx processes data from a custom AWS namespace. The available actions are one of <code class="docutils literal notranslate"><span class="pre">&quot;Include&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Exclude&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filterSource</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Expression that selects the data that SignalFx should sync for the custom namespace associated with this sync rule. The expression uses the syntax defined for the SignalFlow <code class="docutils literal notranslate"><span class="pre">filter()</span></code> function; it can be any valid SignalFlow filter expression.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An AWS custom namespace having custom AWS metrics that you want to sync with SignalFx. See the AWS documentation on publishing metrics for more information.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.aws.Integration.enable_aws_usage">
<code class="sig-name descname">enable_aws_usage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.Integration.enable_aws_usage" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag that controls how SignalFx imports usage metrics from AWS to use with AWS Cost Optimizer. If <code class="docutils literal notranslate"><span class="pre">true</span></code>, SignalFx imports the metrics.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.aws.Integration.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.Integration.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the integration is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.aws.Integration.external_id">
<code class="sig-name descname">external_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.Integration.external_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">external_id</span></code> property from one of a <code class="docutils literal notranslate"><span class="pre">aws.ExternalIntegration</span></code> or <code class="docutils literal notranslate"><span class="pre">aws.TokenIntegration</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.aws.Integration.import_cloud_watch">
<code class="sig-name descname">import_cloud_watch</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.Integration.import_cloud_watch" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag that controls how SignalFx imports Cloud Watch metrics. If true, SignalFx imports Cloud Watch metrics from AWS.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.aws.Integration.integration_id">
<code class="sig-name descname">integration_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.Integration.integration_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of one of a <code class="docutils literal notranslate"><span class="pre">aws.ExternalIntegration</span></code> or <code class="docutils literal notranslate"><span class="pre">aws.TokenIntegration</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.aws.Integration.key">
<code class="sig-name descname">key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.Integration.key" title="Permalink to this definition">¶</a></dt>
<dd><p>If you specify <code class="docutils literal notranslate"><span class="pre">auth_method</span> <span class="pre">=</span> <span class="pre">&quot;SecurityToken&quot;</span></code> in your request to create an AWS integration object, use this property to specify the key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.aws.Integration.namespace_sync_rules">
<code class="sig-name descname">namespace_sync_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.Integration.namespace_sync_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>Each element in the array is an object that contains an AWS namespace name and a filter that controls the data that SignalFx collects for the namespace. Conflicts with the <code class="docutils literal notranslate"><span class="pre">services</span></code> property. If you don’t specify either property, SignalFx syncs all data in all AWS namespaces.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">defaultAction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Controls the SignalFx default behavior for processing data from an AWS namespace. If you do specify a filter, use this property to control how SignalFx treats data that doesn’t match the filter. The available actions are one of <code class="docutils literal notranslate"><span class="pre">&quot;Include&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Exclude&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filterAction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Controls how SignalFx processes data from a custom AWS namespace. The available actions are one of <code class="docutils literal notranslate"><span class="pre">&quot;Include&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Exclude&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filterSource</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Expression that selects the data that SignalFx should sync for the custom namespace associated with this sync rule. The expression uses the syntax defined for the SignalFlow <code class="docutils literal notranslate"><span class="pre">filter()</span></code> function; it can be any valid SignalFlow filter expression.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - An AWS custom namespace having custom AWS metrics that you want to sync with SignalFx. See the AWS documentation on publishing metrics for more information.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.aws.Integration.poll_rate">
<code class="sig-name descname">poll_rate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.Integration.poll_rate" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS poll rate (in seconds). One of <code class="docutils literal notranslate"><span class="pre">60</span></code> or <code class="docutils literal notranslate"><span class="pre">300</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.aws.Integration.regions">
<code class="sig-name descname">regions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.Integration.regions" title="Permalink to this definition">¶</a></dt>
<dd><p>List of AWS regions that SignalFx should monitor.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.aws.Integration.role_arn">
<code class="sig-name descname">role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.Integration.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Role ARN that you add to an existing AWS integration object. <strong>Note</strong>: Ensure you use the <code class="docutils literal notranslate"><span class="pre">arn</span></code> property of your role, not the id!</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.aws.Integration.services">
<code class="sig-name descname">services</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.Integration.services" title="Permalink to this definition">¶</a></dt>
<dd><p>List of AWS services that you want SignalFx to monitor. Each element is a string designating an AWS service. Conflicts with <code class="docutils literal notranslate"><span class="pre">namespace_sync_rule</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_signalfx.aws.Integration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">custom_cloudwatch_namespaces=None</em>, <em class="sig-param">custom_namespace_sync_rules=None</em>, <em class="sig-param">enable_aws_usage=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">external_id=None</em>, <em class="sig-param">import_cloud_watch=None</em>, <em class="sig-param">integration_id=None</em>, <em class="sig-param">key=None</em>, <em class="sig-param">namespace_sync_rules=None</em>, <em class="sig-param">poll_rate=None</em>, <em class="sig-param">regions=None</em>, <em class="sig-param">role_arn=None</em>, <em class="sig-param">services=None</em>, <em class="sig-param">token=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.aws.Integration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Integration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>custom_cloudwatch_namespaces</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of custom AWS CloudWatch namespaces to monitor. Custom namespaces contain custom metrics that you define in AWS; SignalFx imports the metrics so you can monitor them.</p></li>
<li><p><strong>custom_namespace_sync_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Each element controls the data collected by SignalFx for the specified namespace. Conflicts with the <code class="docutils literal notranslate"><span class="pre">custom_cloudwatch_namespaces</span></code> property.</p></li>
<li><p><strong>enable_aws_usage</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag that controls how SignalFx imports usage metrics from AWS to use with AWS Cost Optimizer. If <code class="docutils literal notranslate"><span class="pre">true</span></code>, SignalFx imports the metrics.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the integration is enabled.</p></li>
<li><p><strong>external_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <code class="docutils literal notranslate"><span class="pre">external_id</span></code> property from one of a <code class="docutils literal notranslate"><span class="pre">aws.ExternalIntegration</span></code> or <code class="docutils literal notranslate"><span class="pre">aws.TokenIntegration</span></code></p></li>
<li><p><strong>import_cloud_watch</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag that controls how SignalFx imports Cloud Watch metrics. If true, SignalFx imports Cloud Watch metrics from AWS.</p></li>
<li><p><strong>integration_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of one of a <code class="docutils literal notranslate"><span class="pre">aws.ExternalIntegration</span></code> or <code class="docutils literal notranslate"><span class="pre">aws.TokenIntegration</span></code>.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If you specify <code class="docutils literal notranslate"><span class="pre">auth_method</span> <span class="pre">=</span> <span class="pre">&quot;SecurityToken&quot;</span></code> in your request to create an AWS integration object, use this property to specify the key.</p></li>
<li><p><strong>namespace_sync_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Each element in the array is an object that contains an AWS namespace name and a filter that controls the data that SignalFx collects for the namespace. Conflicts with the <code class="docutils literal notranslate"><span class="pre">services</span></code> property. If you don’t specify either property, SignalFx syncs all data in all AWS namespaces.</p></li>
<li><p><strong>poll_rate</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – AWS poll rate (in seconds). One of <code class="docutils literal notranslate"><span class="pre">60</span></code> or <code class="docutils literal notranslate"><span class="pre">300</span></code>.</p></li>
<li><p><strong>regions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of AWS regions that SignalFx should monitor.</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Role ARN that you add to an existing AWS integration object. <strong>Note</strong>: Ensure you use the <code class="docutils literal notranslate"><span class="pre">arn</span></code> property of your role, not the id!</p></li>
<li><p><strong>services</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of AWS services that you want SignalFx to monitor. Each element is a string designating an AWS service. Conflicts with <code class="docutils literal notranslate"><span class="pre">namespace_sync_rule</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>custom_namespace_sync_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">defaultAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Controls the SignalFx default behavior for processing data from an AWS namespace. If you do specify a filter, use this property to control how SignalFx treats data that doesn’t match the filter. The available actions are one of <code class="docutils literal notranslate"><span class="pre">&quot;Include&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Exclude&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filterAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Controls how SignalFx processes data from a custom AWS namespace. The available actions are one of <code class="docutils literal notranslate"><span class="pre">&quot;Include&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Exclude&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filterSource</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Expression that selects the data that SignalFx should sync for the custom namespace associated with this sync rule. The expression uses the syntax defined for the SignalFlow <code class="docutils literal notranslate"><span class="pre">filter()</span></code> function; it can be any valid SignalFlow filter expression.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An AWS custom namespace having custom AWS metrics that you want to sync with SignalFx. See the AWS documentation on publishing metrics for more information.</p></li>
</ul>
<p>The <strong>namespace_sync_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">defaultAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Controls the SignalFx default behavior for processing data from an AWS namespace. If you do specify a filter, use this property to control how SignalFx treats data that doesn’t match the filter. The available actions are one of <code class="docutils literal notranslate"><span class="pre">&quot;Include&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Exclude&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filterAction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Controls how SignalFx processes data from a custom AWS namespace. The available actions are one of <code class="docutils literal notranslate"><span class="pre">&quot;Include&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Exclude&quot;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filterSource</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Expression that selects the data that SignalFx should sync for the custom namespace associated with this sync rule. The expression uses the syntax defined for the SignalFlow <code class="docutils literal notranslate"><span class="pre">filter()</span></code> function; it can be any valid SignalFlow filter expression.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - An AWS custom namespace having custom AWS metrics that you want to sync with SignalFx. See the AWS documentation on publishing metrics for more information.</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-signalfx/blob/master/website/docs/r/aws_integration.html.markdown">https://github.com/terraform-providers/terraform-provider-signalfx/blob/master/website/docs/r/aws_integration.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_signalfx.aws.Integration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.aws.Integration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.aws.Integration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.aws.Integration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.aws.TokenIntegration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_signalfx.aws.</code><code class="sig-name descname">TokenIntegration</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.aws.TokenIntegration" title="Permalink to this definition">¶</a></dt>
<dd><p>SignalFx AWS CloudWatch integrations using security tokens. For help with this integration see <a class="reference external" href="https://docs.signalfx.com/en/latest/integrations/amazon-web-services.html#connect-to-aws">Connect to AWS CloudWatch</a>.</p>
<p><strong>Note:</strong> When managing integrations you’ll need to use an admin token to authenticate the SignalFx provider.</p>
<blockquote>
<div><p><strong>WARNING</strong> This resource implements a part of a workflow. You must use it with <code class="docutils literal notranslate"><span class="pre">aws.Integration</span></code>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this integration</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-signalfx/blob/master/website/docs/r/aws_token_integration.html.markdown">https://github.com/terraform-providers/terraform-provider-signalfx/blob/master/website/docs/r/aws_token_integration.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_signalfx.aws.TokenIntegration.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.TokenIntegration.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of this integration</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_signalfx.aws.TokenIntegration.signalfx_aws_account">
<code class="sig-name descname">signalfx_aws_account</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_signalfx.aws.TokenIntegration.signalfx_aws_account" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS Account ARN to use with your policies/roles, provided by SignalFx.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_signalfx.aws.TokenIntegration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">signalfx_aws_account=None</em>, <em class="sig-param">token_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.aws.TokenIntegration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TokenIntegration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this integration</p></li>
<li><p><strong>signalfx_aws_account</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS Account ARN to use with your policies/roles, provided by SignalFx.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-signalfx/blob/master/website/docs/r/aws_token_integration.html.markdown">https://github.com/terraform-providers/terraform-provider-signalfx/blob/master/website/docs/r/aws_token_integration.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_signalfx.aws.TokenIntegration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.aws.TokenIntegration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.aws.TokenIntegration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.aws.TokenIntegration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
