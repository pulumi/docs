---
title: Module appautoscaling
---

<div class="section" id="appautoscaling">
<h1>appautoscaling<a class="headerlink" href="#appautoscaling" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.appautoscaling"></span><dl class="class">
<dt id="pulumi_aws.appautoscaling.Policy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.appautoscaling.</code><code class="sig-name descname">Policy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">alarms=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">policy_type=None</em>, <em class="sig-param">resource_id=None</em>, <em class="sig-param">scalable_dimension=None</em>, <em class="sig-param">service_namespace=None</em>, <em class="sig-param">step_scaling_policy_configuration=None</em>, <em class="sig-param">target_tracking_scaling_policy_configuration=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appautoscaling.Policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Application AutoScaling Policy resource.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">target_value</span></code> - (Required) The target value for the metric.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disable_scale_in</span></code> - (Optional) Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won’t remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scale_in_cooldown</span></code> - (Optional) The amount of time, in seconds, after a scale in activity completes before another scale in activity can start.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scale_out_cooldown</span></code> - (Optional) The amount of time, in seconds, after a scale out activity completes before another scale out activity can start.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customized_metric_specification</span></code> - (Optional) A custom CloudWatch metric. Documentation can be found  at: <a class="reference external" href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CustomizedMetricSpecification.html">AWS Customized Metric Specification</a>. See supported fields below.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">predefined_metric_specification</span></code> - (Optional) A predefined metric. See supported fields below.</p></li>
</ul>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dimensions</span></code> - (Optional) The dimensions of the metric.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metric_name</span></code> - (Required) The name of the metric.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">namespace</span></code> - (Required) The namespace of the metric.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">statistic</span></code> - (Required) The statistic of the metric.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unit</span></code> - (Optional) The unit of the metric.</p></li>
</ul>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">predefined_metric_type</span></code> - (Required) The metric type.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource_label</span></code> - (Optional) Reserved for future use.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy.</p></li>
<li><p><strong>policy_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – For DynamoDB, only <code class="docutils literal notranslate"><span class="pre">TargetTrackingScaling</span></code> is supported. For Amazon ECS, Spot Fleet, and Amazon RDS, both <code class="docutils literal notranslate"><span class="pre">StepScaling</span></code> and <code class="docutils literal notranslate"><span class="pre">TargetTrackingScaling</span></code> are supported. For any other service, only <code class="docutils literal notranslate"><span class="pre">StepScaling</span></code> is supported. Defaults to <code class="docutils literal notranslate"><span class="pre">StepScaling</span></code>.</p></li>
<li><p><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource type and unique identifier string for the resource associated with the scaling policy. Documentation can be found in the <code class="docutils literal notranslate"><span class="pre">ResourceId</span></code> parameter at: <a class="reference external" href="http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters">AWS Application Auto Scaling API Reference</a></p></li>
<li><p><strong>scalable_dimension</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The scalable dimension of the scalable target. Documentation can be found in the <code class="docutils literal notranslate"><span class="pre">ScalableDimension</span></code> parameter at: <a class="reference external" href="http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters">AWS Application Auto Scaling API Reference</a></p>
</p></li>
<li><p><strong>service_namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The AWS service namespace of the scalable target. Documentation can be found in the <code class="docutils literal notranslate"><span class="pre">ServiceNamespace</span></code> parameter at: <a class="reference external" href="http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters">AWS Application Auto Scaling API Reference</a></p>
</p></li>
<li><p><strong>step_scaling_policy_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Step scaling policy configuration, requires <code class="docutils literal notranslate"><span class="pre">policy_type</span> <span class="pre">=</span> <span class="pre">&quot;StepScaling&quot;</span></code> (default). See supported fields below.</p></li>
<li><p><strong>target_tracking_scaling_policy_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A target tracking policy, requires <code class="docutils literal notranslate"><span class="pre">policy_type</span> <span class="pre">=</span> <span class="pre">&quot;TargetTrackingScaling&quot;</span></code>. See supported fields below.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appautoscaling_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appautoscaling_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.Policy.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.Policy.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN assigned by AWS to the scaling policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.Policy.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.Policy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.Policy.policy_type">
<code class="sig-name descname">policy_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.Policy.policy_type" title="Permalink to this definition">¶</a></dt>
<dd><p>For DynamoDB, only <code class="docutils literal notranslate"><span class="pre">TargetTrackingScaling</span></code> is supported. For Amazon ECS, Spot Fleet, and Amazon RDS, both <code class="docutils literal notranslate"><span class="pre">StepScaling</span></code> and <code class="docutils literal notranslate"><span class="pre">TargetTrackingScaling</span></code> are supported. For any other service, only <code class="docutils literal notranslate"><span class="pre">StepScaling</span></code> is supported. Defaults to <code class="docutils literal notranslate"><span class="pre">StepScaling</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.Policy.resource_id">
<code class="sig-name descname">resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.Policy.resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource type and unique identifier string for the resource associated with the scaling policy. Documentation can be found in the <code class="docutils literal notranslate"><span class="pre">ResourceId</span></code> parameter at: <a class="reference external" href="http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters">AWS Application Auto Scaling API Reference</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.Policy.scalable_dimension">
<code class="sig-name descname">scalable_dimension</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.Policy.scalable_dimension" title="Permalink to this definition">¶</a></dt>
<dd><p>The scalable dimension of the scalable target. Documentation can be found in the <code class="docutils literal notranslate"><span class="pre">ScalableDimension</span></code> parameter at: <a class="reference external" href="http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters">AWS Application Auto Scaling API Reference</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.Policy.service_namespace">
<code class="sig-name descname">service_namespace</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.Policy.service_namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS service namespace of the scalable target. Documentation can be found in the <code class="docutils literal notranslate"><span class="pre">ServiceNamespace</span></code> parameter at: <a class="reference external" href="http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters">AWS Application Auto Scaling API Reference</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.Policy.step_scaling_policy_configuration">
<code class="sig-name descname">step_scaling_policy_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.Policy.step_scaling_policy_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Step scaling policy configuration, requires <code class="docutils literal notranslate"><span class="pre">policy_type</span> <span class="pre">=</span> <span class="pre">&quot;StepScaling&quot;</span></code> (default). See supported fields below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.Policy.target_tracking_scaling_policy_configuration">
<code class="sig-name descname">target_tracking_scaling_policy_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.Policy.target_tracking_scaling_policy_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>A target tracking policy, requires <code class="docutils literal notranslate"><span class="pre">policy_type</span> <span class="pre">=</span> <span class="pre">&quot;TargetTrackingScaling&quot;</span></code>. See supported fields below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.appautoscaling.Policy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">alarms=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">policy_type=None</em>, <em class="sig-param">resource_id=None</em>, <em class="sig-param">scalable_dimension=None</em>, <em class="sig-param">service_namespace=None</em>, <em class="sig-param">step_scaling_policy_configuration=None</em>, <em class="sig-param">target_tracking_scaling_policy_configuration=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appautoscaling.Policy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Policy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] arn: The ARN assigned by AWS to the scaling policy.
:param pulumi.Input[str] name: The name of the policy.
:param pulumi.Input[str] policy_type: For DynamoDB, only <code class="docutils literal notranslate"><span class="pre">TargetTrackingScaling</span></code> is supported. For Amazon ECS, Spot Fleet, and Amazon RDS, both <code class="docutils literal notranslate"><span class="pre">StepScaling</span></code> and <code class="docutils literal notranslate"><span class="pre">TargetTrackingScaling</span></code> are supported. For any other service, only <code class="docutils literal notranslate"><span class="pre">StepScaling</span></code> is supported. Defaults to <code class="docutils literal notranslate"><span class="pre">StepScaling</span></code>.
:param pulumi.Input[str] resource_id: The resource type and unique identifier string for the resource associated with the scaling policy. Documentation can be found in the <code class="docutils literal notranslate"><span class="pre">ResourceId</span></code> parameter at: <a class="reference external" href="http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters">AWS Application Auto Scaling API Reference</a>
:param pulumi.Input[str] scalable_dimension: The scalable dimension of the scalable target. Documentation can be found in the <code class="docutils literal notranslate"><span class="pre">ScalableDimension</span></code> parameter at: <a class="reference external" href="http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters">AWS Application Auto Scaling API Reference</a>
:param pulumi.Input[str] service_namespace: The AWS service namespace of the scalable target. Documentation can be found in the <code class="docutils literal notranslate"><span class="pre">ServiceNamespace</span></code> parameter at: <a class="reference external" href="http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters">AWS Application Auto Scaling API Reference</a>
:param pulumi.Input[dict] step_scaling_policy_configuration: Step scaling policy configuration, requires <code class="docutils literal notranslate"><span class="pre">policy_type</span> <span class="pre">=</span> <span class="pre">&quot;StepScaling&quot;</span></code> (default). See supported fields below.
:param pulumi.Input[dict] target_tracking_scaling_policy_configuration: A target tracking policy, requires <code class="docutils literal notranslate"><span class="pre">policy_type</span> <span class="pre">=</span> <span class="pre">&quot;TargetTrackingScaling&quot;</span></code>. See supported fields below.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appautoscaling_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appautoscaling_policy.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.appautoscaling.Policy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appautoscaling.Policy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appautoscaling.Policy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appautoscaling.Policy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appautoscaling.ScheduledAction">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.appautoscaling.</code><code class="sig-name descname">ScheduledAction</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">end_time=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_id=None</em>, <em class="sig-param">scalable_dimension=None</em>, <em class="sig-param">scalable_target_action=None</em>, <em class="sig-param">schedule=None</em>, <em class="sig-param">service_namespace=None</em>, <em class="sig-param">start_time=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appautoscaling.ScheduledAction" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Application AutoScaling ScheduledAction resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>end_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date and time for the scheduled action to end. Specify the following format: 2006-01-02T15:04:05Z</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the scheduled action.</p></li>
<li><p><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The identifier of the resource associated with the scheduled action. Documentation can be found in the parameter at: <a class="reference external" href="https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ResourceId">AWS Application Auto Scaling API Reference</a></p>
</p></li>
<li><p><strong>scalable_dimension</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The scalable dimension. Documentation can be found in the parameter at: <a class="reference external" href="https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ScalableDimension">AWS Application Auto Scaling API Reference</a> Example: ecs:service:DesiredCount</p>
</p></li>
<li><p><strong>scalable_target_action</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The new minimum and maximum capacity. You can set both values or just one. See below</p></li>
<li><p><strong>schedule</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The schedule for this action. The following formats are supported: At expressions - at(yyyy-mm-ddThh:mm:ss), Rate expressions - rate(valueunit), Cron expressions - cron(fields). In UTC. Documentation can be found in the parameter at: <a class="reference external" href="https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-Schedule">AWS Application Auto Scaling API Reference</a></p>
</p></li>
<li><p><strong>service_namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The namespace of the AWS service. Documentation can be found in the parameter at: <a class="reference external" href="https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ServiceNamespace">AWS Application Auto Scaling API Reference</a> Example: ecs</p>
</p></li>
<li><p><strong>start_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date and time for the scheduled action to start. Specify the following format: 2006-01-02T15:04:05Z</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appautoscaling_scheduled_action.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appautoscaling_scheduled_action.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.ScheduledAction.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.ScheduledAction.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the scheduled action.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.ScheduledAction.end_time">
<code class="sig-name descname">end_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.ScheduledAction.end_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The date and time for the scheduled action to end. Specify the following format: 2006-01-02T15:04:05Z</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.ScheduledAction.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.ScheduledAction.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the scheduled action.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.ScheduledAction.resource_id">
<code class="sig-name descname">resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.ScheduledAction.resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifier of the resource associated with the scheduled action. Documentation can be found in the parameter at: <a class="reference external" href="https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ResourceId">AWS Application Auto Scaling API Reference</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.ScheduledAction.scalable_dimension">
<code class="sig-name descname">scalable_dimension</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.ScheduledAction.scalable_dimension" title="Permalink to this definition">¶</a></dt>
<dd><p>The scalable dimension. Documentation can be found in the parameter at: <a class="reference external" href="https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ScalableDimension">AWS Application Auto Scaling API Reference</a> Example: ecs:service:DesiredCount</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.ScheduledAction.scalable_target_action">
<code class="sig-name descname">scalable_target_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.ScheduledAction.scalable_target_action" title="Permalink to this definition">¶</a></dt>
<dd><p>The new minimum and maximum capacity. You can set both values or just one. See below</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.ScheduledAction.schedule">
<code class="sig-name descname">schedule</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.ScheduledAction.schedule" title="Permalink to this definition">¶</a></dt>
<dd><p>The schedule for this action. The following formats are supported: At expressions - at(yyyy-mm-ddThh:mm:ss), Rate expressions - rate(valueunit), Cron expressions - cron(fields). In UTC. Documentation can be found in the parameter at: <a class="reference external" href="https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-Schedule">AWS Application Auto Scaling API Reference</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.ScheduledAction.service_namespace">
<code class="sig-name descname">service_namespace</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.ScheduledAction.service_namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>The namespace of the AWS service. Documentation can be found in the parameter at: <a class="reference external" href="https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ServiceNamespace">AWS Application Auto Scaling API Reference</a> Example: ecs</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.ScheduledAction.start_time">
<code class="sig-name descname">start_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.ScheduledAction.start_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The date and time for the scheduled action to start. Specify the following format: 2006-01-02T15:04:05Z</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.appautoscaling.ScheduledAction.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">end_time=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_id=None</em>, <em class="sig-param">scalable_dimension=None</em>, <em class="sig-param">scalable_target_action=None</em>, <em class="sig-param">schedule=None</em>, <em class="sig-param">service_namespace=None</em>, <em class="sig-param">start_time=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appautoscaling.ScheduledAction.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ScheduledAction resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] arn: The Amazon Resource Name (ARN) of the scheduled action.
:param pulumi.Input[str] end_time: The date and time for the scheduled action to end. Specify the following format: 2006-01-02T15:04:05Z
:param pulumi.Input[str] name: The name of the scheduled action.
:param pulumi.Input[str] resource_id: The identifier of the resource associated with the scheduled action. Documentation can be found in the parameter at: <a class="reference external" href="https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ResourceId">AWS Application Auto Scaling API Reference</a>
:param pulumi.Input[str] scalable_dimension: The scalable dimension. Documentation can be found in the parameter at: <a class="reference external" href="https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ScalableDimension">AWS Application Auto Scaling API Reference</a> Example: ecs:service:DesiredCount
:param pulumi.Input[dict] scalable_target_action: The new minimum and maximum capacity. You can set both values or just one. See below
:param pulumi.Input[str] schedule: The schedule for this action. The following formats are supported: At expressions - at(yyyy-mm-ddThh:mm:ss), Rate expressions - rate(valueunit), Cron expressions - cron(fields). In UTC. Documentation can be found in the parameter at: <a class="reference external" href="https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-Schedule">AWS Application Auto Scaling API Reference</a>
:param pulumi.Input[str] service_namespace: The namespace of the AWS service. Documentation can be found in the parameter at: <a class="reference external" href="https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ServiceNamespace">AWS Application Auto Scaling API Reference</a> Example: ecs
:param pulumi.Input[str] start_time: The date and time for the scheduled action to start. Specify the following format: 2006-01-02T15:04:05Z</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appautoscaling_scheduled_action.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appautoscaling_scheduled_action.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.appautoscaling.ScheduledAction.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appautoscaling.ScheduledAction.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appautoscaling.ScheduledAction.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appautoscaling.ScheduledAction.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appautoscaling.Target">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.appautoscaling.</code><code class="sig-name descname">Target</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">max_capacity=None</em>, <em class="sig-param">min_capacity=None</em>, <em class="sig-param">resource_id=None</em>, <em class="sig-param">role_arn=None</em>, <em class="sig-param">scalable_dimension=None</em>, <em class="sig-param">service_namespace=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appautoscaling.Target" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Application AutoScaling ScalableTarget resource. To manage policies which get attached to the target, see the <cite>``appautoscaling.Policy`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy.html">https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy.html</a>&gt;`_.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>max_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The max capacity of the scalable target.</p></li>
<li><p><strong>min_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The min capacity of the scalable target.</p></li>
<li><p><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The resource type and unique identifier string for the resource associated with the scaling policy. Documentation can be found in the <code class="docutils literal notranslate"><span class="pre">ResourceId</span></code> parameter at: <a class="reference external" href="https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters">AWS Application Auto Scaling API Reference</a></p>
</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the IAM role that allows Application
AutoScaling to modify your scalable target on your behalf.</p></li>
<li><p><strong>scalable_dimension</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The scalable dimension of the scalable target. Documentation can be found in the <code class="docutils literal notranslate"><span class="pre">ScalableDimension</span></code> parameter at: <a class="reference external" href="https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters">AWS Application Auto Scaling API Reference</a></p>
</p></li>
<li><p><strong>service_namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The AWS service namespace of the scalable target. Documentation can be found in the <code class="docutils literal notranslate"><span class="pre">ServiceNamespace</span></code> parameter at: <a class="reference external" href="https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters">AWS Application Auto Scaling API Reference</a></p>
</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appautoscaling_target.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appautoscaling_target.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.Target.max_capacity">
<code class="sig-name descname">max_capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.Target.max_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The max capacity of the scalable target.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.Target.min_capacity">
<code class="sig-name descname">min_capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.Target.min_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The min capacity of the scalable target.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.Target.resource_id">
<code class="sig-name descname">resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.Target.resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource type and unique identifier string for the resource associated with the scaling policy. Documentation can be found in the <code class="docutils literal notranslate"><span class="pre">ResourceId</span></code> parameter at: <a class="reference external" href="https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters">AWS Application Auto Scaling API Reference</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.Target.role_arn">
<code class="sig-name descname">role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.Target.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the IAM role that allows Application
AutoScaling to modify your scalable target on your behalf.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.Target.scalable_dimension">
<code class="sig-name descname">scalable_dimension</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.Target.scalable_dimension" title="Permalink to this definition">¶</a></dt>
<dd><p>The scalable dimension of the scalable target. Documentation can be found in the <code class="docutils literal notranslate"><span class="pre">ScalableDimension</span></code> parameter at: <a class="reference external" href="https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters">AWS Application Auto Scaling API Reference</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.Target.service_namespace">
<code class="sig-name descname">service_namespace</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.Target.service_namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS service namespace of the scalable target. Documentation can be found in the <code class="docutils literal notranslate"><span class="pre">ServiceNamespace</span></code> parameter at: <a class="reference external" href="https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters">AWS Application Auto Scaling API Reference</a></p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.appautoscaling.Target.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">max_capacity=None</em>, <em class="sig-param">min_capacity=None</em>, <em class="sig-param">resource_id=None</em>, <em class="sig-param">role_arn=None</em>, <em class="sig-param">scalable_dimension=None</em>, <em class="sig-param">service_namespace=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appautoscaling.Target.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Target resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[float] max_capacity: The max capacity of the scalable target.
:param pulumi.Input[float] min_capacity: The min capacity of the scalable target.
:param pulumi.Input[str] resource_id: The resource type and unique identifier string for the resource associated with the scaling policy. Documentation can be found in the <code class="docutils literal notranslate"><span class="pre">ResourceId</span></code> parameter at: <a class="reference external" href="https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters">AWS Application Auto Scaling API Reference</a>
:param pulumi.Input[str] role_arn: The ARN of the IAM role that allows Application</p>
<blockquote>
<div><p>AutoScaling to modify your scalable target on your behalf.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>scalable_dimension</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The scalable dimension of the scalable target. Documentation can be found in the <code class="docutils literal notranslate"><span class="pre">ScalableDimension</span></code> parameter at: <a class="reference external" href="https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters">AWS Application Auto Scaling API Reference</a></p>
</p></li>
<li><p><strong>service_namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The AWS service namespace of the scalable target. Documentation can be found in the <code class="docutils literal notranslate"><span class="pre">ServiceNamespace</span></code> parameter at: <a class="reference external" href="https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters">AWS Application Auto Scaling API Reference</a></p>
</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appautoscaling_target.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appautoscaling_target.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.appautoscaling.Target.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appautoscaling.Target.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appautoscaling.Target.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appautoscaling.Target.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
