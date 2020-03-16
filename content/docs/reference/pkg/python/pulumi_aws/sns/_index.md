---
title: Module sns
title_tag: Module sns | Package pulumi_aws | Python SDK
linktitle: sns
notitle: true
---

<div class="section" id="sns">
<h1>sns<a class="headerlink" href="#sns" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.sns"></span><dl class="class">
<dt id="pulumi_aws.sns.AwaitableGetTopicResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.sns.</code><code class="sig-name descname">AwaitableGetTopicResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.AwaitableGetTopicResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_aws.sns.GetTopicResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.sns.</code><code class="sig-name descname">GetTopicResult</code><span class="sig-paren">(</span><em class="sig-param">arn=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.GetTopicResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getTopic.</p>
<dl class="attribute">
<dt id="pulumi_aws.sns.GetTopicResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.GetTopicResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to the ARN of the found topic, suitable for referencing in other resources that support SNS topics.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.GetTopicResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.GetTopicResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.sns.PlatformApplication">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.sns.</code><code class="sig-name descname">PlatformApplication</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">event_delivery_failure_topic_arn=None</em>, <em class="sig-param">event_endpoint_created_topic_arn=None</em>, <em class="sig-param">event_endpoint_deleted_topic_arn=None</em>, <em class="sig-param">event_endpoint_updated_topic_arn=None</em>, <em class="sig-param">failure_feedback_role_arn=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">platform=None</em>, <em class="sig-param">platform_credential=None</em>, <em class="sig-param">platform_principal=None</em>, <em class="sig-param">success_feedback_role_arn=None</em>, <em class="sig-param">success_feedback_sample_rate=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.PlatformApplication" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SNS platform application resource</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sns_platform_application.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sns_platform_application.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>event_delivery_failure_topic_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SNS Topic triggered when a delivery to any of the platform endpoints associated with your platform application encounters a permanent failure.</p></li>
<li><p><strong>event_endpoint_created_topic_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SNS Topic triggered when a new platform endpoint is added to your platform application.</p></li>
<li><p><strong>event_endpoint_deleted_topic_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SNS Topic triggered when an existing platform endpoint is deleted from your platform application.</p></li>
<li><p><strong>event_endpoint_updated_topic_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SNS Topic triggered when an existing platform endpoint is changed from your platform application.</p></li>
<li><p><strong>failure_feedback_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM role permitted to receive failure feedback for this application.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The friendly name for the SNS platform application</p></li>
<li><p><strong>platform</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The platform that the app is registered with. See [Platform][1] for supported platforms.</p></li>
<li><p><strong>platform_credential</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Application Platform credential. See [Credential][1] for type of credential required for platform. The value of this attribute when stored into the state is only a hash of the real value, so therefore it is not practical to use this as an attribute for other resources.</p></li>
<li><p><strong>platform_principal</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Application Platform principal. See [Principal][2] for type of principal required for platform. The value of this attribute when stored into the state is only a hash of the real value, so therefore it is not practical to use this as an attribute for other resources.</p></li>
<li><p><strong>success_feedback_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM role permitted to receive success feedback for this application.</p></li>
<li><p><strong>success_feedback_sample_rate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The percentage of success to sample (0-100)</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.sns.PlatformApplication.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.PlatformApplication.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the SNS platform application</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.PlatformApplication.event_delivery_failure_topic_arn">
<code class="sig-name descname">event_delivery_failure_topic_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.PlatformApplication.event_delivery_failure_topic_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>SNS Topic triggered when a delivery to any of the platform endpoints associated with your platform application encounters a permanent failure.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.PlatformApplication.event_endpoint_created_topic_arn">
<code class="sig-name descname">event_endpoint_created_topic_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.PlatformApplication.event_endpoint_created_topic_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>SNS Topic triggered when a new platform endpoint is added to your platform application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.PlatformApplication.event_endpoint_deleted_topic_arn">
<code class="sig-name descname">event_endpoint_deleted_topic_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.PlatformApplication.event_endpoint_deleted_topic_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>SNS Topic triggered when an existing platform endpoint is deleted from your platform application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.PlatformApplication.event_endpoint_updated_topic_arn">
<code class="sig-name descname">event_endpoint_updated_topic_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.PlatformApplication.event_endpoint_updated_topic_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>SNS Topic triggered when an existing platform endpoint is changed from your platform application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.PlatformApplication.failure_feedback_role_arn">
<code class="sig-name descname">failure_feedback_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.PlatformApplication.failure_feedback_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM role permitted to receive failure feedback for this application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.PlatformApplication.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.PlatformApplication.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The friendly name for the SNS platform application</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.PlatformApplication.platform">
<code class="sig-name descname">platform</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.PlatformApplication.platform" title="Permalink to this definition">¶</a></dt>
<dd><p>The platform that the app is registered with. See [Platform][1] for supported platforms.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.PlatformApplication.platform_credential">
<code class="sig-name descname">platform_credential</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.PlatformApplication.platform_credential" title="Permalink to this definition">¶</a></dt>
<dd><p>Application Platform credential. See [Credential][1] for type of credential required for platform. The value of this attribute when stored into the state is only a hash of the real value, so therefore it is not practical to use this as an attribute for other resources.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.PlatformApplication.platform_principal">
<code class="sig-name descname">platform_principal</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.PlatformApplication.platform_principal" title="Permalink to this definition">¶</a></dt>
<dd><p>Application Platform principal. See [Principal][2] for type of principal required for platform. The value of this attribute when stored into the state is only a hash of the real value, so therefore it is not practical to use this as an attribute for other resources.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.PlatformApplication.success_feedback_role_arn">
<code class="sig-name descname">success_feedback_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.PlatformApplication.success_feedback_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM role permitted to receive success feedback for this application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.PlatformApplication.success_feedback_sample_rate">
<code class="sig-name descname">success_feedback_sample_rate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.PlatformApplication.success_feedback_sample_rate" title="Permalink to this definition">¶</a></dt>
<dd><p>The percentage of success to sample (0-100)</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.sns.PlatformApplication.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">event_delivery_failure_topic_arn=None</em>, <em class="sig-param">event_endpoint_created_topic_arn=None</em>, <em class="sig-param">event_endpoint_deleted_topic_arn=None</em>, <em class="sig-param">event_endpoint_updated_topic_arn=None</em>, <em class="sig-param">failure_feedback_role_arn=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">platform=None</em>, <em class="sig-param">platform_credential=None</em>, <em class="sig-param">platform_principal=None</em>, <em class="sig-param">success_feedback_role_arn=None</em>, <em class="sig-param">success_feedback_sample_rate=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.PlatformApplication.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PlatformApplication resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the SNS platform application</p></li>
<li><p><strong>event_delivery_failure_topic_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SNS Topic triggered when a delivery to any of the platform endpoints associated with your platform application encounters a permanent failure.</p></li>
<li><p><strong>event_endpoint_created_topic_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SNS Topic triggered when a new platform endpoint is added to your platform application.</p></li>
<li><p><strong>event_endpoint_deleted_topic_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SNS Topic triggered when an existing platform endpoint is deleted from your platform application.</p></li>
<li><p><strong>event_endpoint_updated_topic_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SNS Topic triggered when an existing platform endpoint is changed from your platform application.</p></li>
<li><p><strong>failure_feedback_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM role permitted to receive failure feedback for this application.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The friendly name for the SNS platform application</p></li>
<li><p><strong>platform</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The platform that the app is registered with. See [Platform][1] for supported platforms.</p></li>
<li><p><strong>platform_credential</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Application Platform credential. See [Credential][1] for type of credential required for platform. The value of this attribute when stored into the state is only a hash of the real value, so therefore it is not practical to use this as an attribute for other resources.</p></li>
<li><p><strong>platform_principal</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Application Platform principal. See [Principal][2] for type of principal required for platform. The value of this attribute when stored into the state is only a hash of the real value, so therefore it is not practical to use this as an attribute for other resources.</p></li>
<li><p><strong>success_feedback_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM role permitted to receive success feedback for this application.</p></li>
<li><p><strong>success_feedback_sample_rate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The percentage of success to sample (0-100)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.sns.PlatformApplication.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.PlatformApplication.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sns.PlatformApplication.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.PlatformApplication.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sns.SmsPreferences">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.sns.</code><code class="sig-name descname">SmsPreferences</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">default_sender_id=None</em>, <em class="sig-param">default_sms_type=None</em>, <em class="sig-param">delivery_status_iam_role_arn=None</em>, <em class="sig-param">delivery_status_success_sampling_rate=None</em>, <em class="sig-param">monthly_spend_limit=None</em>, <em class="sig-param">usage_report_s3_bucket=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.SmsPreferences" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a way to set SNS SMS preferences.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sns_sms_preferences.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sns_sms_preferences.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_sender_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string, such as your business brand, that is displayed as the sender on the receiving device.</p></li>
<li><p><strong>default_sms_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of SMS message that you will send by default. Possible values are: Promotional, Transactional</p></li>
<li><p><strong>delivery_status_iam_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the IAM role that allows Amazon SNS to write logs about SMS deliveries in CloudWatch Logs.</p></li>
<li><p><strong>delivery_status_success_sampling_rate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The percentage of successful SMS deliveries for which Amazon SNS will write logs in CloudWatch Logs. The value must be between 0 and 100.</p></li>
<li><p><strong>monthly_spend_limit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum amount in USD that you are willing to spend each month to send SMS messages.</p></li>
<li><p><strong>usage_report_s3_bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Amazon S3 bucket to receive daily SMS usage reports from Amazon SNS.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.sns.SmsPreferences.default_sender_id">
<code class="sig-name descname">default_sender_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.SmsPreferences.default_sender_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A string, such as your business brand, that is displayed as the sender on the receiving device.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.SmsPreferences.default_sms_type">
<code class="sig-name descname">default_sms_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.SmsPreferences.default_sms_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of SMS message that you will send by default. Possible values are: Promotional, Transactional</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.SmsPreferences.delivery_status_iam_role_arn">
<code class="sig-name descname">delivery_status_iam_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.SmsPreferences.delivery_status_iam_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the IAM role that allows Amazon SNS to write logs about SMS deliveries in CloudWatch Logs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.SmsPreferences.delivery_status_success_sampling_rate">
<code class="sig-name descname">delivery_status_success_sampling_rate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.SmsPreferences.delivery_status_success_sampling_rate" title="Permalink to this definition">¶</a></dt>
<dd><p>The percentage of successful SMS deliveries for which Amazon SNS will write logs in CloudWatch Logs. The value must be between 0 and 100.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.SmsPreferences.monthly_spend_limit">
<code class="sig-name descname">monthly_spend_limit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.SmsPreferences.monthly_spend_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum amount in USD that you are willing to spend each month to send SMS messages.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.SmsPreferences.usage_report_s3_bucket">
<code class="sig-name descname">usage_report_s3_bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.SmsPreferences.usage_report_s3_bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Amazon S3 bucket to receive daily SMS usage reports from Amazon SNS.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.sns.SmsPreferences.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">default_sender_id=None</em>, <em class="sig-param">default_sms_type=None</em>, <em class="sig-param">delivery_status_iam_role_arn=None</em>, <em class="sig-param">delivery_status_success_sampling_rate=None</em>, <em class="sig-param">monthly_spend_limit=None</em>, <em class="sig-param">usage_report_s3_bucket=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.SmsPreferences.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SmsPreferences resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_sender_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string, such as your business brand, that is displayed as the sender on the receiving device.</p></li>
<li><p><strong>default_sms_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of SMS message that you will send by default. Possible values are: Promotional, Transactional</p></li>
<li><p><strong>delivery_status_iam_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the IAM role that allows Amazon SNS to write logs about SMS deliveries in CloudWatch Logs.</p></li>
<li><p><strong>delivery_status_success_sampling_rate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The percentage of successful SMS deliveries for which Amazon SNS will write logs in CloudWatch Logs. The value must be between 0 and 100.</p></li>
<li><p><strong>monthly_spend_limit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum amount in USD that you are willing to spend each month to send SMS messages.</p></li>
<li><p><strong>usage_report_s3_bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Amazon S3 bucket to receive daily SMS usage reports from Amazon SNS.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.sns.SmsPreferences.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.SmsPreferences.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sns.SmsPreferences.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.SmsPreferences.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sns.Topic">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.sns.</code><code class="sig-name descname">Topic</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application_failure_feedback_role_arn=None</em>, <em class="sig-param">application_success_feedback_role_arn=None</em>, <em class="sig-param">application_success_feedback_sample_rate=None</em>, <em class="sig-param">delivery_policy=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">http_failure_feedback_role_arn=None</em>, <em class="sig-param">http_success_feedback_role_arn=None</em>, <em class="sig-param">http_success_feedback_sample_rate=None</em>, <em class="sig-param">kms_master_key_id=None</em>, <em class="sig-param">lambda_failure_feedback_role_arn=None</em>, <em class="sig-param">lambda_success_feedback_role_arn=None</em>, <em class="sig-param">lambda_success_feedback_sample_rate=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">policy=None</em>, <em class="sig-param">sqs_failure_feedback_role_arn=None</em>, <em class="sig-param">sqs_success_feedback_role_arn=None</em>, <em class="sig-param">sqs_success_feedback_sample_rate=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.Topic" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SNS topic resource</p>
<p>The <code class="docutils literal notranslate"><span class="pre">&lt;endpoint&gt;_success_feedback_role_arn</span></code> and <code class="docutils literal notranslate"><span class="pre">&lt;endpoint&gt;_failure_feedback_role_arn</span></code> arguments are used to give Amazon SNS write access to use CloudWatch Logs on your behalf. The <code class="docutils literal notranslate"><span class="pre">&lt;endpoint&gt;_success_feedback_sample_rate</span></code> argument is for specifying the sample rate percentage (0-100) of successfully delivered messages. After you configure the  <code class="docutils literal notranslate"><span class="pre">&lt;endpoint&gt;_failure_feedback_role_arn</span></code> argument, then all failed message deliveries generate CloudWatch Logs.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sns_topic.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sns_topic.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_failure_feedback_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IAM role for failure feedback</p></li>
<li><p><strong>application_success_feedback_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM role permitted to receive success feedback for this topic</p></li>
<li><p><strong>application_success_feedback_sample_rate</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Percentage of success to sample</p></li>
<li><p><strong>delivery_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SNS delivery policy. More on <a class="reference external" href="https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html">AWS documentation</a></p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name for the SNS topic</p></li>
<li><p><strong>http_failure_feedback_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IAM role for failure feedback</p></li>
<li><p><strong>http_success_feedback_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM role permitted to receive success feedback for this topic</p></li>
<li><p><strong>http_success_feedback_sample_rate</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Percentage of success to sample</p></li>
<li><p><strong>kms_master_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of an AWS-managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see <a class="reference external" href="https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms">Key Terms</a></p></li>
<li><p><strong>lambda_failure_feedback_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IAM role for failure feedback</p></li>
<li><p><strong>lambda_success_feedback_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM role permitted to receive success feedback for this topic</p></li>
<li><p><strong>lambda_success_feedback_sample_rate</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Percentage of success to sample</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The friendly name for the SNS topic. By default generated by this provider.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The friendly name for the SNS topic. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>sqs_failure_feedback_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IAM role for failure feedback</p></li>
<li><p><strong>sqs_success_feedback_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM role permitted to receive success feedback for this topic</p></li>
<li><p><strong>sqs_success_feedback_sample_rate</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Percentage of success to sample</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.application_failure_feedback_role_arn">
<code class="sig-name descname">application_failure_feedback_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.application_failure_feedback_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>IAM role for failure feedback</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.application_success_feedback_role_arn">
<code class="sig-name descname">application_success_feedback_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.application_success_feedback_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM role permitted to receive success feedback for this topic</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.application_success_feedback_sample_rate">
<code class="sig-name descname">application_success_feedback_sample_rate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.application_success_feedback_sample_rate" title="Permalink to this definition">¶</a></dt>
<dd><p>Percentage of success to sample</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the SNS topic, as a more obvious property (clone of id)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.delivery_policy">
<code class="sig-name descname">delivery_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.delivery_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The SNS delivery policy. More on <a class="reference external" href="https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html">AWS documentation</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name for the SNS topic</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.http_failure_feedback_role_arn">
<code class="sig-name descname">http_failure_feedback_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.http_failure_feedback_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>IAM role for failure feedback</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.http_success_feedback_role_arn">
<code class="sig-name descname">http_success_feedback_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.http_success_feedback_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM role permitted to receive success feedback for this topic</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.http_success_feedback_sample_rate">
<code class="sig-name descname">http_success_feedback_sample_rate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.http_success_feedback_sample_rate" title="Permalink to this definition">¶</a></dt>
<dd><p>Percentage of success to sample</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.kms_master_key_id">
<code class="sig-name descname">kms_master_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.kms_master_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of an AWS-managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see <a class="reference external" href="https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms">Key Terms</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.lambda_failure_feedback_role_arn">
<code class="sig-name descname">lambda_failure_feedback_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.lambda_failure_feedback_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>IAM role for failure feedback</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.lambda_success_feedback_role_arn">
<code class="sig-name descname">lambda_success_feedback_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.lambda_success_feedback_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM role permitted to receive success feedback for this topic</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.lambda_success_feedback_sample_rate">
<code class="sig-name descname">lambda_success_feedback_sample_rate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.lambda_success_feedback_sample_rate" title="Permalink to this definition">¶</a></dt>
<dd><p>Percentage of success to sample</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The friendly name for the SNS topic. By default generated by this provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.name_prefix">
<code class="sig-name descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The friendly name for the SNS topic. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.sqs_failure_feedback_role_arn">
<code class="sig-name descname">sqs_failure_feedback_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.sqs_failure_feedback_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>IAM role for failure feedback</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.sqs_success_feedback_role_arn">
<code class="sig-name descname">sqs_success_feedback_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.sqs_success_feedback_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM role permitted to receive success feedback for this topic</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.sqs_success_feedback_sample_rate">
<code class="sig-name descname">sqs_success_feedback_sample_rate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.sqs_success_feedback_sample_rate" title="Permalink to this definition">¶</a></dt>
<dd><p>Percentage of success to sample</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Key-value mapping of resource tags</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.sns.Topic.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">application_failure_feedback_role_arn=None</em>, <em class="sig-param">application_success_feedback_role_arn=None</em>, <em class="sig-param">application_success_feedback_sample_rate=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">delivery_policy=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">http_failure_feedback_role_arn=None</em>, <em class="sig-param">http_success_feedback_role_arn=None</em>, <em class="sig-param">http_success_feedback_sample_rate=None</em>, <em class="sig-param">kms_master_key_id=None</em>, <em class="sig-param">lambda_failure_feedback_role_arn=None</em>, <em class="sig-param">lambda_success_feedback_role_arn=None</em>, <em class="sig-param">lambda_success_feedback_sample_rate=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_prefix=None</em>, <em class="sig-param">policy=None</em>, <em class="sig-param">sqs_failure_feedback_role_arn=None</em>, <em class="sig-param">sqs_success_feedback_role_arn=None</em>, <em class="sig-param">sqs_success_feedback_sample_rate=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.Topic.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Topic resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>application_failure_feedback_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IAM role for failure feedback</p></li>
<li><p><strong>application_success_feedback_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM role permitted to receive success feedback for this topic</p></li>
<li><p><strong>application_success_feedback_sample_rate</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Percentage of success to sample</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the SNS topic, as a more obvious property (clone of id)</p></li>
<li><p><strong>delivery_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The SNS delivery policy. More on <a class="reference external" href="https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html">AWS documentation</a></p>
</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name for the SNS topic</p></li>
<li><p><strong>http_failure_feedback_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IAM role for failure feedback</p></li>
<li><p><strong>http_success_feedback_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM role permitted to receive success feedback for this topic</p></li>
<li><p><strong>http_success_feedback_sample_rate</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Percentage of success to sample</p></li>
<li><p><strong>kms_master_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The ID of an AWS-managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see <a class="reference external" href="https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms">Key Terms</a></p>
</p></li>
<li><p><strong>lambda_failure_feedback_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IAM role for failure feedback</p></li>
<li><p><strong>lambda_success_feedback_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM role permitted to receive success feedback for this topic</p></li>
<li><p><strong>lambda_success_feedback_sample_rate</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Percentage of success to sample</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The friendly name for the SNS topic. By default generated by this provider.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The friendly name for the SNS topic. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>sqs_failure_feedback_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IAM role for failure feedback</p></li>
<li><p><strong>sqs_success_feedback_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM role permitted to receive success feedback for this topic</p></li>
<li><p><strong>sqs_success_feedback_sample_rate</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Percentage of success to sample</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key-value mapping of resource tags</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.sns.Topic.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.Topic.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sns.Topic.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.Topic.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sns.TopicPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.sns.</code><code class="sig-name descname">TopicPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">policy=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.TopicPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SNS topic policy resource</p>
<blockquote>
<div><p><strong>NOTE:</strong> If a Principal is specified as just an AWS account ID rather than an ARN, AWS silently converts it to the ARN for the root user, causing future deployments to differ. To avoid this problem, just specify the full ARN, e.g. <code class="docutils literal notranslate"><span class="pre">arn:aws:iam::123456789012:root</span></code></p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sns_topic_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sns_topic_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the SNS topic</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.sns.TopicPolicy.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.TopicPolicy.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the SNS topic</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.sns.TopicPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">policy=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.TopicPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TopicPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the SNS topic</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.sns.TopicPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.TopicPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sns.TopicPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.TopicPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sns.TopicSubscription">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.sns.</code><code class="sig-name descname">TopicSubscription</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">confirmation_timeout_in_minutes=None</em>, <em class="sig-param">delivery_policy=None</em>, <em class="sig-param">endpoint=None</em>, <em class="sig-param">endpoint_auto_confirms=None</em>, <em class="sig-param">filter_policy=None</em>, <em class="sig-param">protocol=None</em>, <em class="sig-param">raw_message_delivery=None</em>, <em class="sig-param">topic=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.TopicSubscription" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div><p>Provides a resource for subscribing to SNS topics. Requires that an SNS topic exist for the subscription to attach to.</p>
</div></blockquote>
<p>This resource allows you to automatically place messages sent to SNS topics in SQS queues, send them as HTTP(S) POST requests
to a given endpoint, send SMS messages, or notify devices / applications. The most likely use case will
probably be SQS queues.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If the SNS topic and SQS queue are in different AWS regions, it is important for the “sns.TopicSubscription” to use an AWS provider that is in the same region of the SNS topic. If the “sns.TopicSubscription” is using a provider with a different region than the SNS topic, the subscription will fail to create.</p>
<p><strong>NOTE:</strong> Setup of cross-account subscriptions from SNS topics to SQS queues requires the provider to have access to BOTH accounts.</p>
<p><strong>NOTE:</strong> If SNS topic and SQS queue are in different AWS accounts but the same region it is important for the “sns.TopicSubscription” to use the AWS provider of the account with the SQS queue. If “sns.TopicSubscription” is using a Provider with a different account than the SQS queue, the provider creates the subscriptions but does not keep state and tries to re-create the subscription at every apply.</p>
<p><strong>NOTE:</strong> If SNS topic and SQS queue are in different AWS accounts and different AWS regions it is important to recognize that the subscription needs to be initiated from the account with the SQS queue but in the region of the SNS topic.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sns_topic_subscription.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sns_topic_subscription.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>confirmation_timeout_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Integer indicating number of minutes to wait in retying mode for fetching subscription arn before marking it as failure. Only applicable for http and https protocols (default is 1 minute).</p></li>
<li><p><strong>delivery_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – JSON String with the delivery policy (retries, backoff, etc.) that will be used in the subscription - this only applies to HTTP/S subscriptions. Refer to the <a class="reference external" href="https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html">SNS docs</a> for more details.</p></li>
<li><p><strong>endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint to send data to, the contents will vary with the protocol. (see below for more information)</p></li>
<li><p><strong>endpoint_auto_confirms</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean indicating whether the end point is capable of <a class="reference external" href="http://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.html#SendMessageToHttp.prepare">auto confirming subscription</a> e.g., PagerDuty (default is false)</p></li>
<li><p><strong>filter_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>JSON String with the filter policy that will be used in the subscription to filter messages seen by the target resource. Refer to the <a class="reference external" href="https://docs.aws.amazon.com/sns/latest/dg/message-filtering.html">SNS docs</a> for more details.</p>
</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol to use. The possible values for this are: <code class="docutils literal notranslate"><span class="pre">sqs</span></code>, <code class="docutils literal notranslate"><span class="pre">sms</span></code>, <code class="docutils literal notranslate"><span class="pre">lambda</span></code>, <code class="docutils literal notranslate"><span class="pre">application</span></code>. (<code class="docutils literal notranslate"><span class="pre">http</span></code> or <code class="docutils literal notranslate"><span class="pre">https</span></code> are partially supported, see below) (<code class="docutils literal notranslate"><span class="pre">email</span></code> is an option but is unsupported, see below).</p></li>
<li><p><strong>raw_message_delivery</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean indicating whether or not to enable raw message delivery (the original message is directly passed, not wrapped in JSON with the original message in the message property) (default is false).</p></li>
<li><p><strong>topic</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The ARN of the SNS topic to subscribe to</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_aws.sns.TopicSubscription.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.TopicSubscription.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the subscription stored as a more user-friendly property</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.TopicSubscription.confirmation_timeout_in_minutes">
<code class="sig-name descname">confirmation_timeout_in_minutes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.TopicSubscription.confirmation_timeout_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>Integer indicating number of minutes to wait in retying mode for fetching subscription arn before marking it as failure. Only applicable for http and https protocols (default is 1 minute).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.TopicSubscription.delivery_policy">
<code class="sig-name descname">delivery_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.TopicSubscription.delivery_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>JSON String with the delivery policy (retries, backoff, etc.) that will be used in the subscription - this only applies to HTTP/S subscriptions. Refer to the <a class="reference external" href="https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html">SNS docs</a> for more details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.TopicSubscription.endpoint">
<code class="sig-name descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.TopicSubscription.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint to send data to, the contents will vary with the protocol. (see below for more information)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.TopicSubscription.endpoint_auto_confirms">
<code class="sig-name descname">endpoint_auto_confirms</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.TopicSubscription.endpoint_auto_confirms" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean indicating whether the end point is capable of <a class="reference external" href="http://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.html#SendMessageToHttp.prepare">auto confirming subscription</a> e.g., PagerDuty (default is false)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.TopicSubscription.filter_policy">
<code class="sig-name descname">filter_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.TopicSubscription.filter_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>JSON String with the filter policy that will be used in the subscription to filter messages seen by the target resource. Refer to the <a class="reference external" href="https://docs.aws.amazon.com/sns/latest/dg/message-filtering.html">SNS docs</a> for more details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.TopicSubscription.protocol">
<code class="sig-name descname">protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.TopicSubscription.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol to use. The possible values for this are: <code class="docutils literal notranslate"><span class="pre">sqs</span></code>, <code class="docutils literal notranslate"><span class="pre">sms</span></code>, <code class="docutils literal notranslate"><span class="pre">lambda</span></code>, <code class="docutils literal notranslate"><span class="pre">application</span></code>. (<code class="docutils literal notranslate"><span class="pre">http</span></code> or <code class="docutils literal notranslate"><span class="pre">https</span></code> are partially supported, see below) (<code class="docutils literal notranslate"><span class="pre">email</span></code> is an option but is unsupported, see below).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.TopicSubscription.raw_message_delivery">
<code class="sig-name descname">raw_message_delivery</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.TopicSubscription.raw_message_delivery" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean indicating whether or not to enable raw message delivery (the original message is directly passed, not wrapped in JSON with the original message in the message property) (default is false).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.TopicSubscription.topic">
<code class="sig-name descname">topic</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.TopicSubscription.topic" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the SNS topic to subscribe to</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.sns.TopicSubscription.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">arn=None</em>, <em class="sig-param">confirmation_timeout_in_minutes=None</em>, <em class="sig-param">delivery_policy=None</em>, <em class="sig-param">endpoint=None</em>, <em class="sig-param">endpoint_auto_confirms=None</em>, <em class="sig-param">filter_policy=None</em>, <em class="sig-param">protocol=None</em>, <em class="sig-param">raw_message_delivery=None</em>, <em class="sig-param">topic=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.TopicSubscription.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TopicSubscription resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the subscription stored as a more user-friendly property</p></li>
<li><p><strong>confirmation_timeout_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Integer indicating number of minutes to wait in retying mode for fetching subscription arn before marking it as failure. Only applicable for http and https protocols (default is 1 minute).</p></li>
<li><p><strong>delivery_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>JSON String with the delivery policy (retries, backoff, etc.) that will be used in the subscription - this only applies to HTTP/S subscriptions. Refer to the <a class="reference external" href="https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html">SNS docs</a> for more details.</p>
</p></li>
<li><p><strong>endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint to send data to, the contents will vary with the protocol. (see below for more information)</p></li>
<li><p><strong>endpoint_auto_confirms</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>Boolean indicating whether the end point is capable of <a class="reference external" href="http://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.html#SendMessageToHttp.prepare">auto confirming subscription</a> e.g., PagerDuty (default is false)</p>
</p></li>
<li><p><strong>filter_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>JSON String with the filter policy that will be used in the subscription to filter messages seen by the target resource. Refer to the <a class="reference external" href="https://docs.aws.amazon.com/sns/latest/dg/message-filtering.html">SNS docs</a> for more details.</p>
</p></li>
<li><p><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol to use. The possible values for this are: <code class="docutils literal notranslate"><span class="pre">sqs</span></code>, <code class="docutils literal notranslate"><span class="pre">sms</span></code>, <code class="docutils literal notranslate"><span class="pre">lambda</span></code>, <code class="docutils literal notranslate"><span class="pre">application</span></code>. (<code class="docutils literal notranslate"><span class="pre">http</span></code> or <code class="docutils literal notranslate"><span class="pre">https</span></code> are partially supported, see below) (<code class="docutils literal notranslate"><span class="pre">email</span></code> is an option but is unsupported, see below).</p></li>
<li><p><strong>raw_message_delivery</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean indicating whether or not to enable raw message delivery (the original message is directly passed, not wrapped in JSON with the original message in the message property) (default is false).</p></li>
<li><p><strong>topic</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The ARN of the SNS topic to subscribe to</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.sns.TopicSubscription.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.TopicSubscription.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sns.TopicSubscription.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.TopicSubscription.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sns.get_topic">
<code class="sig-prename descclassname">pulumi_aws.sns.</code><code class="sig-name descname">get_topic</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.get_topic" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ARN of a topic in AWS Simple Notification
Service (SNS). By using this data source, you can reference SNS topics
without having to hard code the ARNs as input.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/sns_topic.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/sns_topic.html.markdown</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The friendly name of the topic to match.</p>
</dd>
</dl>
</dd></dl>

</div>
