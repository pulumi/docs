---
---

<div class="section" id="module-pulumi_aws.appautoscaling">
<span id="appautoscaling"></span><h1>appautoscaling<a class="headerlink" href="#module-pulumi_aws.appautoscaling" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.appautoscaling.Policy">
<em class="property">class </em><code class="descclassname">pulumi_aws.appautoscaling.</code><code class="descname">Policy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>alarms=None</em>, <em>name=None</em>, <em>policy_type=None</em>, <em>resource_id=None</em>, <em>scalable_dimension=None</em>, <em>service_namespace=None</em>, <em>step_scaling_policy_configuration=None</em>, <em>target_tracking_scaling_policy_configuration=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appautoscaling.Policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Application AutoScaling Policy resource.</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">target_value</span></code> - (Required) The target value for the metric.</li>
<li><code class="docutils literal notranslate"><span class="pre">disable_scale_in</span></code> - (Optional) Indicates whether scale in by the target tracking policy is disabled. If the value is true, scale in is disabled and the target tracking policy won’t remove capacity from the scalable resource. Otherwise, scale in is enabled and the target tracking policy can remove capacity from the scalable resource. The default value is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><code class="docutils literal notranslate"><span class="pre">scale_in_cooldown</span></code> - (Optional) The amount of time, in seconds, after a scale in activity completes before another scale in activity can start.</li>
<li><code class="docutils literal notranslate"><span class="pre">scale_out_cooldown</span></code> - (Optional) The amount of time, in seconds, after a scale out activity completes before another scale out activity can start.</li>
<li><code class="docutils literal notranslate"><span class="pre">customized_metric_specification</span></code> - (Optional) A custom CloudWatch metric. Documentation can be found  at: <a class="reference external" href="https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CustomizedMetricSpecification.html">AWS Customized Metric Specification</a>. See supported fields below.</li>
<li><code class="docutils literal notranslate"><span class="pre">predefined_metric_specification</span></code> - (Optional) A predefined metric. See supported fields below.</li>
</ul>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">dimensions</span></code> - (Optional) The dimensions of the metric.</li>
<li><code class="docutils literal notranslate"><span class="pre">metric_name</span></code> - (Required) The name of the metric.</li>
<li><code class="docutils literal notranslate"><span class="pre">namespace</span></code> - (Required) The namespace of the metric.</li>
<li><code class="docutils literal notranslate"><span class="pre">statistic</span></code> - (Required) The statistic of the metric.</li>
<li><code class="docutils literal notranslate"><span class="pre">unit</span></code> - (Optional) The unit of the metric.</li>
</ul>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">predefined_metric_type</span></code> - (Required) The metric type.</li>
<li><code class="docutils literal notranslate"><span class="pre">resource_label</span></code> - (Optional) Reserved for future use.</li>
</ul>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the policy.</li>
<li><strong>policy_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – For DynamoDB, only <code class="docutils literal notranslate"><span class="pre">TargetTrackingScaling</span></code> is supported. For Amazon ECS, Spot Fleet, and Amazon RDS, both <code class="docutils literal notranslate"><span class="pre">StepScaling</span></code> and <code class="docutils literal notranslate"><span class="pre">TargetTrackingScaling</span></code> are supported. For any other service, only <code class="docutils literal notranslate"><span class="pre">StepScaling</span></code> is supported. Defaults to <code class="docutils literal notranslate"><span class="pre">StepScaling</span></code>.</li>
<li><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource type and unique identifier string for the resource associated with the scaling policy. Documentation can be found in the <code class="docutils literal notranslate"><span class="pre">ResourceId</span></code> parameter at: <a class="reference external" href="http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters">AWS Application Auto Scaling API Reference</a></li>
<li><strong>scalable_dimension</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The scalable dimension of the scalable target. Documentation can be found in the <code class="docutils literal notranslate"><span class="pre">ScalableDimension</span></code> parameter at: <a class="reference external" href="http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters">AWS Application Auto Scaling API Reference</a></p>
</li>
<li><strong>service_namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The AWS service namespace of the scalable target. Documentation can be found in the <code class="docutils literal notranslate"><span class="pre">ServiceNamespace</span></code> parameter at: <a class="reference external" href="http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters">AWS Application Auto Scaling API Reference</a></p>
</li>
<li><strong>step_scaling_policy_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Step scaling policy configuration, requires <code class="docutils literal notranslate"><span class="pre">policy_type</span> <span class="pre">=</span> <span class="pre">&quot;StepScaling&quot;</span></code> (default). See supported fields below.</li>
<li><strong>target_tracking_scaling_policy_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A target tracking policy, requires <code class="docutils literal notranslate"><span class="pre">policy_type</span> <span class="pre">=</span> <span class="pre">&quot;TargetTrackingScaling&quot;</span></code>. See supported fields below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appautoscaling_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appautoscaling_policy.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.Policy.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.Policy.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN assigned by AWS to the scaling policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.Policy.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.Policy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.Policy.policy_type">
<code class="descname">policy_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.Policy.policy_type" title="Permalink to this definition">¶</a></dt>
<dd><p>For DynamoDB, only <code class="docutils literal notranslate"><span class="pre">TargetTrackingScaling</span></code> is supported. For Amazon ECS, Spot Fleet, and Amazon RDS, both <code class="docutils literal notranslate"><span class="pre">StepScaling</span></code> and <code class="docutils literal notranslate"><span class="pre">TargetTrackingScaling</span></code> are supported. For any other service, only <code class="docutils literal notranslate"><span class="pre">StepScaling</span></code> is supported. Defaults to <code class="docutils literal notranslate"><span class="pre">StepScaling</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.Policy.resource_id">
<code class="descname">resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.Policy.resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource type and unique identifier string for the resource associated with the scaling policy. Documentation can be found in the <code class="docutils literal notranslate"><span class="pre">ResourceId</span></code> parameter at: <a class="reference external" href="http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters">AWS Application Auto Scaling API Reference</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.Policy.scalable_dimension">
<code class="descname">scalable_dimension</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.Policy.scalable_dimension" title="Permalink to this definition">¶</a></dt>
<dd><p>The scalable dimension of the scalable target. Documentation can be found in the <code class="docutils literal notranslate"><span class="pre">ScalableDimension</span></code> parameter at: <a class="reference external" href="http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters">AWS Application Auto Scaling API Reference</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.Policy.service_namespace">
<code class="descname">service_namespace</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.Policy.service_namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS service namespace of the scalable target. Documentation can be found in the <code class="docutils literal notranslate"><span class="pre">ServiceNamespace</span></code> parameter at: <a class="reference external" href="http://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters">AWS Application Auto Scaling API Reference</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.Policy.step_scaling_policy_configuration">
<code class="descname">step_scaling_policy_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.Policy.step_scaling_policy_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>Step scaling policy configuration, requires <code class="docutils literal notranslate"><span class="pre">policy_type</span> <span class="pre">=</span> <span class="pre">&quot;StepScaling&quot;</span></code> (default). See supported fields below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.Policy.target_tracking_scaling_policy_configuration">
<code class="descname">target_tracking_scaling_policy_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.Policy.target_tracking_scaling_policy_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>A target tracking policy, requires <code class="docutils literal notranslate"><span class="pre">policy_type</span> <span class="pre">=</span> <span class="pre">&quot;TargetTrackingScaling&quot;</span></code>. See supported fields below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.appautoscaling.Policy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appautoscaling.Policy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appautoscaling.Policy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appautoscaling.Policy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appautoscaling.ScheduledAction">
<em class="property">class </em><code class="descclassname">pulumi_aws.appautoscaling.</code><code class="descname">ScheduledAction</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>end_time=None</em>, <em>name=None</em>, <em>resource_id=None</em>, <em>scalable_dimension=None</em>, <em>scalable_target_action=None</em>, <em>schedule=None</em>, <em>service_namespace=None</em>, <em>start_time=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appautoscaling.ScheduledAction" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Application AutoScaling ScheduledAction resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>end_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date and time for the scheduled action to end. Specify the following format: 2006-01-02T15:04:05Z</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the scheduled action.</li>
<li><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The identifier of the resource associated with the scheduled action. Documentation can be found in the parameter at: <a class="reference external" href="https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ResourceId">AWS Application Auto Scaling API Reference</a></p>
</li>
<li><strong>scalable_dimension</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The scalable dimension. Documentation can be found in the parameter at: <a class="reference external" href="https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ScalableDimension">AWS Application Auto Scaling API Reference</a> Example: ecs:service:DesiredCount</p>
</li>
<li><strong>scalable_target_action</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The new minimum and maximum capacity. You can set both values or just one. See below</li>
<li><strong>schedule</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The schedule for this action. The following formats are supported: At expressions - at(yyyy-mm-ddThh:mm:ss), Rate expressions - rate(valueunit), Cron expressions - cron(fields). In UTC. Documentation can be found in the parameter at: <a class="reference external" href="https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-Schedule">AWS Application Auto Scaling API Reference</a></p>
</li>
<li><strong>service_namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The namespace of the AWS service. Documentation can be found in the parameter at: <a class="reference external" href="https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ServiceNamespace">AWS Application Auto Scaling API Reference</a> Example: ecs</p>
</li>
<li><strong>start_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The date and time for the scheduled action to start. Specify the following format: 2006-01-02T15:04:05Z</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appautoscaling_scheduled_action.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appautoscaling_scheduled_action.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.ScheduledAction.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.ScheduledAction.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the scheduled action.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.ScheduledAction.end_time">
<code class="descname">end_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.ScheduledAction.end_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The date and time for the scheduled action to end. Specify the following format: 2006-01-02T15:04:05Z</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.ScheduledAction.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.ScheduledAction.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the scheduled action.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.ScheduledAction.resource_id">
<code class="descname">resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.ScheduledAction.resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifier of the resource associated with the scheduled action. Documentation can be found in the parameter at: <a class="reference external" href="https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ResourceId">AWS Application Auto Scaling API Reference</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.ScheduledAction.scalable_dimension">
<code class="descname">scalable_dimension</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.ScheduledAction.scalable_dimension" title="Permalink to this definition">¶</a></dt>
<dd><p>The scalable dimension. Documentation can be found in the parameter at: <a class="reference external" href="https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ScalableDimension">AWS Application Auto Scaling API Reference</a> Example: ecs:service:DesiredCount</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.ScheduledAction.scalable_target_action">
<code class="descname">scalable_target_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.ScheduledAction.scalable_target_action" title="Permalink to this definition">¶</a></dt>
<dd><p>The new minimum and maximum capacity. You can set both values or just one. See below</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.ScheduledAction.schedule">
<code class="descname">schedule</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.ScheduledAction.schedule" title="Permalink to this definition">¶</a></dt>
<dd><p>The schedule for this action. The following formats are supported: At expressions - at(yyyy-mm-ddThh:mm:ss), Rate expressions - rate(valueunit), Cron expressions - cron(fields). In UTC. Documentation can be found in the parameter at: <a class="reference external" href="https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-Schedule">AWS Application Auto Scaling API Reference</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.ScheduledAction.service_namespace">
<code class="descname">service_namespace</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.ScheduledAction.service_namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>The namespace of the AWS service. Documentation can be found in the parameter at: <a class="reference external" href="https://docs.aws.amazon.com/ApplicationAutoScaling/latest/APIReference/API_PutScheduledAction.html#ApplicationAutoScaling-PutScheduledAction-request-ServiceNamespace">AWS Application Auto Scaling API Reference</a> Example: ecs</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.ScheduledAction.start_time">
<code class="descname">start_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.ScheduledAction.start_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The date and time for the scheduled action to start. Specify the following format: 2006-01-02T15:04:05Z</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.appautoscaling.ScheduledAction.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appautoscaling.ScheduledAction.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appautoscaling.ScheduledAction.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appautoscaling.ScheduledAction.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appautoscaling.Target">
<em class="property">class </em><code class="descclassname">pulumi_aws.appautoscaling.</code><code class="descname">Target</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>max_capacity=None</em>, <em>min_capacity=None</em>, <em>resource_id=None</em>, <em>role_arn=None</em>, <em>scalable_dimension=None</em>, <em>service_namespace=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appautoscaling.Target" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an Application AutoScaling ScalableTarget resource. To manage policies which get attached to the target, see the <cite>``aws_appautoscaling_policy`</cite> resource &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy.html">https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy.html</a>&gt;`_.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>max_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The max capacity of the scalable target.</li>
<li><strong>min_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The min capacity of the scalable target.</li>
<li><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The resource type and unique identifier string for the resource associated with the scaling policy. Documentation can be found in the <code class="docutils literal notranslate"><span class="pre">ResourceId</span></code> parameter at: <a class="reference external" href="https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters">AWS Application Auto Scaling API Reference</a></p>
</li>
<li><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the IAM role that allows Application
AutoScaling to modify your scalable target on your behalf.</li>
<li><strong>scalable_dimension</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The scalable dimension of the scalable target. Documentation can be found in the <code class="docutils literal notranslate"><span class="pre">ScalableDimension</span></code> parameter at: <a class="reference external" href="https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters">AWS Application Auto Scaling API Reference</a></p>
</li>
<li><strong>service_namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The AWS service namespace of the scalable target. Documentation can be found in the <code class="docutils literal notranslate"><span class="pre">ServiceNamespace</span></code> parameter at: <a class="reference external" href="https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters">AWS Application Auto Scaling API Reference</a></p>
</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appautoscaling_target.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appautoscaling_target.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.Target.max_capacity">
<code class="descname">max_capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.Target.max_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The max capacity of the scalable target.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.Target.min_capacity">
<code class="descname">min_capacity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.Target.min_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The min capacity of the scalable target.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.Target.resource_id">
<code class="descname">resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.Target.resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource type and unique identifier string for the resource associated with the scaling policy. Documentation can be found in the <code class="docutils literal notranslate"><span class="pre">ResourceId</span></code> parameter at: <a class="reference external" href="https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters">AWS Application Auto Scaling API Reference</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.Target.role_arn">
<code class="descname">role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.Target.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the IAM role that allows Application
AutoScaling to modify your scalable target on your behalf.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.Target.scalable_dimension">
<code class="descname">scalable_dimension</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.Target.scalable_dimension" title="Permalink to this definition">¶</a></dt>
<dd><p>The scalable dimension of the scalable target. Documentation can be found in the <code class="docutils literal notranslate"><span class="pre">ScalableDimension</span></code> parameter at: <a class="reference external" href="https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters">AWS Application Auto Scaling API Reference</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.appautoscaling.Target.service_namespace">
<code class="descname">service_namespace</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.appautoscaling.Target.service_namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS service namespace of the scalable target. Documentation can be found in the <code class="docutils literal notranslate"><span class="pre">ServiceNamespace</span></code> parameter at: <a class="reference external" href="https://docs.aws.amazon.com/autoscaling/application/APIReference/API_RegisterScalableTarget.html#API_RegisterScalableTarget_RequestParameters">AWS Application Auto Scaling API Reference</a></p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.appautoscaling.Target.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appautoscaling.Target.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.appautoscaling.Target.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.appautoscaling.Target.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
