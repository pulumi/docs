<div class="section" id="module-pulumi_aws.sns">
<span id="sns"></span><h1>sns<a class="headerlink" href="#module-pulumi_aws.sns" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.sns.GetTopicResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.sns.</code><code class="descname">GetTopicResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.GetTopicResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getTopic.</p>
<dl class="attribute">
<dt id="pulumi_aws.sns.GetTopicResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.GetTopicResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to the ARN of the found topic, suitable for referencing in other resources that support SNS topics.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.GetTopicResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.GetTopicResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.sns.PlatformApplication">
<em class="property">class </em><code class="descclassname">pulumi_aws.sns.</code><code class="descname">PlatformApplication</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>event_delivery_failure_topic_arn=None</em>, <em>event_endpoint_created_topic_arn=None</em>, <em>event_endpoint_deleted_topic_arn=None</em>, <em>event_endpoint_updated_topic_arn=None</em>, <em>failure_feedback_role_arn=None</em>, <em>name=None</em>, <em>platform=None</em>, <em>platform_credential=None</em>, <em>platform_principal=None</em>, <em>success_feedback_role_arn=None</em>, <em>success_feedback_sample_rate=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.PlatformApplication" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SNS platform application resource</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>event_delivery_failure_topic_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SNS Topic triggered when a delivery to any of the platform endpoints associated with your platform application encounters a permanent failure.</li>
<li><strong>event_endpoint_created_topic_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SNS Topic triggered when a new platform endpoint is added to your platform application.</li>
<li><strong>event_endpoint_deleted_topic_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SNS Topic triggered when an existing platform endpoint is deleted from your platform application.</li>
<li><strong>event_endpoint_updated_topic_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SNS Topic triggered when an existing platform endpoint is changed from your platform application.</li>
<li><strong>failure_feedback_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM role permitted to receive failure feedback for this application.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The friendly name for the SNS platform application</li>
<li><strong>platform</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The platform that the app is registered with. See [Platform][1] for supported platforms.</li>
<li><strong>platform_credential</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Application Platform credential. See [Credential][1] for type of credential required for platform. The value of this attribute when stored into the Terraform state is only a hash of the real value, so therefore it is not practical to use this as an attribute for other resources.</li>
<li><strong>platform_principal</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Application Platform principal. See [Principal][2] for type of principal required for platform. The value of this attribute when stored into the Terraform state is only a hash of the real value, so therefore it is not practical to use this as an attribute for other resources.</li>
<li><strong>success_feedback_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM role permitted to receive success feedback for this application.</li>
<li><strong>success_feedback_sample_rate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The percentage of success to sample (0-100)</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.sns.PlatformApplication.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.PlatformApplication.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the SNS platform application</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.PlatformApplication.event_delivery_failure_topic_arn">
<code class="descname">event_delivery_failure_topic_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.PlatformApplication.event_delivery_failure_topic_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>SNS Topic triggered when a delivery to any of the platform endpoints associated with your platform application encounters a permanent failure.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.PlatformApplication.event_endpoint_created_topic_arn">
<code class="descname">event_endpoint_created_topic_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.PlatformApplication.event_endpoint_created_topic_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>SNS Topic triggered when a new platform endpoint is added to your platform application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.PlatformApplication.event_endpoint_deleted_topic_arn">
<code class="descname">event_endpoint_deleted_topic_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.PlatformApplication.event_endpoint_deleted_topic_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>SNS Topic triggered when an existing platform endpoint is deleted from your platform application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.PlatformApplication.event_endpoint_updated_topic_arn">
<code class="descname">event_endpoint_updated_topic_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.PlatformApplication.event_endpoint_updated_topic_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>SNS Topic triggered when an existing platform endpoint is changed from your platform application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.PlatformApplication.failure_feedback_role_arn">
<code class="descname">failure_feedback_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.PlatformApplication.failure_feedback_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM role permitted to receive failure feedback for this application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.PlatformApplication.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.PlatformApplication.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The friendly name for the SNS platform application</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.PlatformApplication.platform">
<code class="descname">platform</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.PlatformApplication.platform" title="Permalink to this definition">¶</a></dt>
<dd><p>The platform that the app is registered with. See [Platform][1] for supported platforms.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.PlatformApplication.platform_credential">
<code class="descname">platform_credential</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.PlatformApplication.platform_credential" title="Permalink to this definition">¶</a></dt>
<dd><p>Application Platform credential. See [Credential][1] for type of credential required for platform. The value of this attribute when stored into the Terraform state is only a hash of the real value, so therefore it is not practical to use this as an attribute for other resources.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.PlatformApplication.platform_principal">
<code class="descname">platform_principal</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.PlatformApplication.platform_principal" title="Permalink to this definition">¶</a></dt>
<dd><p>Application Platform principal. See [Principal][2] for type of principal required for platform. The value of this attribute when stored into the Terraform state is only a hash of the real value, so therefore it is not practical to use this as an attribute for other resources.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.PlatformApplication.success_feedback_role_arn">
<code class="descname">success_feedback_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.PlatformApplication.success_feedback_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM role permitted to receive success feedback for this application.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.PlatformApplication.success_feedback_sample_rate">
<code class="descname">success_feedback_sample_rate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.PlatformApplication.success_feedback_sample_rate" title="Permalink to this definition">¶</a></dt>
<dd><p>The percentage of success to sample (0-100)</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.sns.PlatformApplication.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.PlatformApplication.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sns.PlatformApplication.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.PlatformApplication.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sns.SmsPreferences">
<em class="property">class </em><code class="descclassname">pulumi_aws.sns.</code><code class="descname">SmsPreferences</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>default_sender_id=None</em>, <em>default_sms_type=None</em>, <em>delivery_status_iam_role_arn=None</em>, <em>delivery_status_success_sampling_rate=None</em>, <em>monthly_spend_limit=None</em>, <em>usage_report_s3_bucket=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.SmsPreferences" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a way to set SNS SMS preferences.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>default_sender_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string, such as your business brand, that is displayed as the sender on the receiving device.</li>
<li><strong>default_sms_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of SMS message that you will send by default. Possible values are: Promotional, Transactional</li>
<li><strong>delivery_status_iam_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the IAM role that allows Amazon SNS to write logs about SMS deliveries in CloudWatch Logs.</li>
<li><strong>delivery_status_success_sampling_rate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The percentage of successful SMS deliveries for which Amazon SNS will write logs in CloudWatch Logs. The value must be between 0 and 100.</li>
<li><strong>monthly_spend_limit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum amount in USD that you are willing to spend each month to send SMS messages.</li>
<li><strong>usage_report_s3_bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Amazon S3 bucket to receive daily SMS usage reports from Amazon SNS.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.sns.SmsPreferences.default_sender_id">
<code class="descname">default_sender_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.SmsPreferences.default_sender_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A string, such as your business brand, that is displayed as the sender on the receiving device.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.SmsPreferences.default_sms_type">
<code class="descname">default_sms_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.SmsPreferences.default_sms_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of SMS message that you will send by default. Possible values are: Promotional, Transactional</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.SmsPreferences.delivery_status_iam_role_arn">
<code class="descname">delivery_status_iam_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.SmsPreferences.delivery_status_iam_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the IAM role that allows Amazon SNS to write logs about SMS deliveries in CloudWatch Logs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.SmsPreferences.delivery_status_success_sampling_rate">
<code class="descname">delivery_status_success_sampling_rate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.SmsPreferences.delivery_status_success_sampling_rate" title="Permalink to this definition">¶</a></dt>
<dd><p>The percentage of successful SMS deliveries for which Amazon SNS will write logs in CloudWatch Logs. The value must be between 0 and 100.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.SmsPreferences.monthly_spend_limit">
<code class="descname">monthly_spend_limit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.SmsPreferences.monthly_spend_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum amount in USD that you are willing to spend each month to send SMS messages.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.SmsPreferences.usage_report_s3_bucket">
<code class="descname">usage_report_s3_bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.SmsPreferences.usage_report_s3_bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Amazon S3 bucket to receive daily SMS usage reports from Amazon SNS.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.sns.SmsPreferences.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.SmsPreferences.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sns.SmsPreferences.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.SmsPreferences.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sns.Topic">
<em class="property">class </em><code class="descclassname">pulumi_aws.sns.</code><code class="descname">Topic</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>application_failure_feedback_role_arn=None</em>, <em>application_success_feedback_role_arn=None</em>, <em>application_success_feedback_sample_rate=None</em>, <em>delivery_policy=None</em>, <em>display_name=None</em>, <em>http_failure_feedback_role_arn=None</em>, <em>http_success_feedback_role_arn=None</em>, <em>http_success_feedback_sample_rate=None</em>, <em>kms_master_key_id=None</em>, <em>lambda_failure_feedback_role_arn=None</em>, <em>lambda_success_feedback_role_arn=None</em>, <em>lambda_success_feedback_sample_rate=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>policy=None</em>, <em>sqs_failure_feedback_role_arn=None</em>, <em>sqs_success_feedback_role_arn=None</em>, <em>sqs_success_feedback_sample_rate=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.Topic" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SNS topic resource</p>
<p>The <code class="docutils literal notranslate"><span class="pre">&lt;endpoint&gt;_success_feedback_role_arn</span></code> and <code class="docutils literal notranslate"><span class="pre">&lt;endpoint&gt;_failure_feedback_role_arn</span></code> arguments are used to give Amazon SNS write access to use CloudWatch Logs on your behalf. The <code class="docutils literal notranslate"><span class="pre">&lt;endpoint&gt;_success_feedback_sample_rate</span></code> argument is for specifying the sample rate percentage (0-100) of successfully delivered messages. After you configure the  <code class="docutils literal notranslate"><span class="pre">&lt;endpoint&gt;_failure_feedback_role_arn</span></code> argument, then all failed message deliveries generate CloudWatch Logs.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>application_failure_feedback_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IAM role for failure feedback</li>
<li><strong>application_success_feedback_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM role permitted to receive success feedback for this topic</li>
<li><strong>application_success_feedback_sample_rate</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Percentage of success to sample</li>
<li><strong>delivery_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SNS delivery policy. More on <a class="reference external" href="https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html">AWS documentation</a></li>
<li><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name for the SNS topic</li>
<li><strong>http_failure_feedback_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IAM role for failure feedback</li>
<li><strong>http_success_feedback_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM role permitted to receive success feedback for this topic</li>
<li><strong>http_success_feedback_sample_rate</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Percentage of success to sample</li>
<li><strong>kms_master_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of an AWS-managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see <a class="reference external" href="https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms">Key Terms</a></li>
<li><strong>lambda_failure_feedback_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IAM role for failure feedback</li>
<li><strong>lambda_success_feedback_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM role permitted to receive success feedback for this topic</li>
<li><strong>lambda_success_feedback_sample_rate</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Percentage of success to sample</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The friendly name for the SNS topic. By default generated by Terraform.</li>
<li><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The friendly name for the SNS topic. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</li>
<li><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fully-formed AWS policy as JSON. For more information about building AWS IAM policy documents with Terraform, see the <a class="reference external" href="https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html">AWS IAM Policy Document Guide</a>.</li>
<li><strong>sqs_failure_feedback_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – IAM role for failure feedback</li>
<li><strong>sqs_success_feedback_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The IAM role permitted to receive success feedback for this topic</li>
<li><strong>sqs_success_feedback_sample_rate</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Percentage of success to sample</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.application_failure_feedback_role_arn">
<code class="descname">application_failure_feedback_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.application_failure_feedback_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>IAM role for failure feedback</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.application_success_feedback_role_arn">
<code class="descname">application_success_feedback_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.application_success_feedback_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM role permitted to receive success feedback for this topic</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.application_success_feedback_sample_rate">
<code class="descname">application_success_feedback_sample_rate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.application_success_feedback_sample_rate" title="Permalink to this definition">¶</a></dt>
<dd><p>Percentage of success to sample</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the SNS topic, as a more obvious property (clone of id)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.delivery_policy">
<code class="descname">delivery_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.delivery_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The SNS delivery policy. More on <a class="reference external" href="https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html">AWS documentation</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.display_name">
<code class="descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name for the SNS topic</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.http_failure_feedback_role_arn">
<code class="descname">http_failure_feedback_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.http_failure_feedback_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>IAM role for failure feedback</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.http_success_feedback_role_arn">
<code class="descname">http_success_feedback_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.http_success_feedback_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM role permitted to receive success feedback for this topic</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.http_success_feedback_sample_rate">
<code class="descname">http_success_feedback_sample_rate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.http_success_feedback_sample_rate" title="Permalink to this definition">¶</a></dt>
<dd><p>Percentage of success to sample</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.kms_master_key_id">
<code class="descname">kms_master_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.kms_master_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of an AWS-managed customer master key (CMK) for Amazon SNS or a custom CMK. For more information, see <a class="reference external" href="https://docs.aws.amazon.com/sns/latest/dg/sns-server-side-encryption.html#sse-key-terms">Key Terms</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.lambda_failure_feedback_role_arn">
<code class="descname">lambda_failure_feedback_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.lambda_failure_feedback_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>IAM role for failure feedback</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.lambda_success_feedback_role_arn">
<code class="descname">lambda_success_feedback_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.lambda_success_feedback_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM role permitted to receive success feedback for this topic</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.lambda_success_feedback_sample_rate">
<code class="descname">lambda_success_feedback_sample_rate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.lambda_success_feedback_sample_rate" title="Permalink to this definition">¶</a></dt>
<dd><p>Percentage of success to sample</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The friendly name for the SNS topic. By default generated by Terraform.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.name_prefix">
<code class="descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The friendly name for the SNS topic. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.policy">
<code class="descname">policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The fully-formed AWS policy as JSON. For more information about building AWS IAM policy documents with Terraform, see the <a class="reference external" href="https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html">AWS IAM Policy Document Guide</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.sqs_failure_feedback_role_arn">
<code class="descname">sqs_failure_feedback_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.sqs_failure_feedback_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>IAM role for failure feedback</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.sqs_success_feedback_role_arn">
<code class="descname">sqs_success_feedback_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.sqs_success_feedback_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The IAM role permitted to receive success feedback for this topic</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.Topic.sqs_success_feedback_sample_rate">
<code class="descname">sqs_success_feedback_sample_rate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.Topic.sqs_success_feedback_sample_rate" title="Permalink to this definition">¶</a></dt>
<dd><p>Percentage of success to sample</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.sns.Topic.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.Topic.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sns.Topic.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.Topic.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sns.TopicPolicy">
<em class="property">class </em><code class="descclassname">pulumi_aws.sns.</code><code class="descname">TopicPolicy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>arn=None</em>, <em>policy=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.TopicPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an SNS topic policy resource</p>
<blockquote>
<div><strong>NOTE:</strong> If a Principal is specified as just an AWS account ID rather than an ARN, AWS silently converts it to the ARN for the root user, causing future terraform plans to differ. To avoid this problem, just specify the full ARN, e.g. <code class="docutils literal notranslate"><span class="pre">arn:aws:iam::123456789012:root</span></code></div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the SNS topic</li>
<li><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The fully-formed AWS policy as JSON. For more information about building AWS IAM policy documents with Terraform, see the <a class="reference external" href="https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html">AWS IAM Policy Document Guide</a>.</p>
</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.sns.TopicPolicy.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.TopicPolicy.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the SNS topic</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.TopicPolicy.policy">
<code class="descname">policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.TopicPolicy.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The fully-formed AWS policy as JSON. For more information about building AWS IAM policy documents with Terraform, see the <a class="reference external" href="https://www.terraform.io/docs/providers/aws/guides/iam-policy-documents.html">AWS IAM Policy Document Guide</a>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.sns.TopicPolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.TopicPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sns.TopicPolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.TopicPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sns.TopicSubscription">
<em class="property">class </em><code class="descclassname">pulumi_aws.sns.</code><code class="descname">TopicSubscription</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>confirmation_timeout_in_minutes=None</em>, <em>delivery_policy=None</em>, <em>endpoint=None</em>, <em>endpoint_auto_confirms=None</em>, <em>filter_policy=None</em>, <em>protocol=None</em>, <em>raw_message_delivery=None</em>, <em>topic=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.TopicSubscription" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div>Provides a resource for subscribing to SNS topics. Requires that an SNS topic exist for the subscription to attach to.</div></blockquote>
<p>This resource allows you to automatically place messages sent to SNS topics in SQS queues, send them as HTTP(S) POST requests
to a given endpoint, send SMS messages, or notify devices / applications. The most likely use case for Terraform users will
probably be SQS queues.</p>
<blockquote>
<div><p><strong>NOTE:</strong> If the SNS topic and SQS queue are in different AWS regions, it is important for the “aws_sns_topic_subscription” to use an AWS provider that is in the same region of the SNS topic. If the “aws_sns_topic_subscription” is using a provider with a different region than the SNS topic, terraform will fail to create the subscription.</p>
<p><strong>NOTE:</strong> Setup of cross-account subscriptions from SNS topics to SQS queues requires Terraform to have access to BOTH accounts.</p>
<p><strong>NOTE:</strong> If SNS topic and SQS queue are in different AWS accounts but the same region it is important for the “aws_sns_topic_subscription” to use the AWS provider of the account with the SQS queue. If “aws_sns_topic_subscription” is using a Provider with a different account than the SNS topic, terraform creates the subscriptions but does not keep state and tries to re-create the subscription at every apply.</p>
<p><strong>NOTE:</strong> If SNS topic and SQS queue are in different AWS accounts and different AWS regions it is important to recognize that the subscription needs to be initiated from the account with the SQS queue but in the region of the SNS topic.</p>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>confirmation_timeout_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Integer indicating number of minutes to wait in retying mode for fetching subscription arn before marking it as failure. Only applicable for http and https protocols (default is 1 minute).</li>
<li><strong>delivery_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – JSON String with the delivery policy (retries, backoff, etc.) that will be used in the subscription - this only applies to HTTP/S subscriptions. Refer to the <a class="reference external" href="https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html">SNS docs</a> for more details.</li>
<li><strong>endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint to send data to, the contents will vary with the protocol. (see below for more information)</li>
<li><strong>endpoint_auto_confirms</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean indicating whether the end point is capable of <a class="reference external" href="http://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.html#SendMessageToHttp.prepare">auto confirming subscription</a> e.g., PagerDuty (default is false)</li>
<li><strong>filter_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>JSON String with the filter policy that will be used in the subscription to filter messages seen by the target resource. Refer to the <a class="reference external" href="https://docs.aws.amazon.com/sns/latest/dg/message-filtering.html">SNS docs</a> for more details.</p>
</li>
<li><strong>protocol</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protocol to use. The possible values for this are: <code class="docutils literal notranslate"><span class="pre">sqs</span></code>, <code class="docutils literal notranslate"><span class="pre">sms</span></code>, <code class="docutils literal notranslate"><span class="pre">lambda</span></code>, <code class="docutils literal notranslate"><span class="pre">application</span></code>. (<code class="docutils literal notranslate"><span class="pre">http</span></code> or <code class="docutils literal notranslate"><span class="pre">https</span></code> are partially supported, see below) (<code class="docutils literal notranslate"><span class="pre">email</span></code> is option but unsupported, see below).</li>
<li><strong>raw_message_delivery</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean indicating whether or not to enable raw message delivery (the original message is directly passed, not wrapped in JSON with the original message in the message property) (default is false).</li>
<li><strong>topic</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the SNS topic to subscribe to</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.sns.TopicSubscription.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.TopicSubscription.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the subscription stored as a more user-friendly property</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.TopicSubscription.confirmation_timeout_in_minutes">
<code class="descname">confirmation_timeout_in_minutes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.TopicSubscription.confirmation_timeout_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>Integer indicating number of minutes to wait in retying mode for fetching subscription arn before marking it as failure. Only applicable for http and https protocols (default is 1 minute).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.TopicSubscription.delivery_policy">
<code class="descname">delivery_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.TopicSubscription.delivery_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>JSON String with the delivery policy (retries, backoff, etc.) that will be used in the subscription - this only applies to HTTP/S subscriptions. Refer to the <a class="reference external" href="https://docs.aws.amazon.com/sns/latest/dg/DeliveryPolicies.html">SNS docs</a> for more details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.TopicSubscription.endpoint">
<code class="descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.TopicSubscription.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint to send data to, the contents will vary with the protocol. (see below for more information)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.TopicSubscription.endpoint_auto_confirms">
<code class="descname">endpoint_auto_confirms</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.TopicSubscription.endpoint_auto_confirms" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean indicating whether the end point is capable of <a class="reference external" href="http://docs.aws.amazon.com/sns/latest/dg/SendMessageToHttp.html#SendMessageToHttp.prepare">auto confirming subscription</a> e.g., PagerDuty (default is false)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.TopicSubscription.filter_policy">
<code class="descname">filter_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.TopicSubscription.filter_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>JSON String with the filter policy that will be used in the subscription to filter messages seen by the target resource. Refer to the <a class="reference external" href="https://docs.aws.amazon.com/sns/latest/dg/message-filtering.html">SNS docs</a> for more details.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.TopicSubscription.protocol">
<code class="descname">protocol</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.TopicSubscription.protocol" title="Permalink to this definition">¶</a></dt>
<dd><p>The protocol to use. The possible values for this are: <code class="docutils literal notranslate"><span class="pre">sqs</span></code>, <code class="docutils literal notranslate"><span class="pre">sms</span></code>, <code class="docutils literal notranslate"><span class="pre">lambda</span></code>, <code class="docutils literal notranslate"><span class="pre">application</span></code>. (<code class="docutils literal notranslate"><span class="pre">http</span></code> or <code class="docutils literal notranslate"><span class="pre">https</span></code> are partially supported, see below) (<code class="docutils literal notranslate"><span class="pre">email</span></code> is option but unsupported, see below).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.TopicSubscription.raw_message_delivery">
<code class="descname">raw_message_delivery</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.TopicSubscription.raw_message_delivery" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean indicating whether or not to enable raw message delivery (the original message is directly passed, not wrapped in JSON with the original message in the message property) (default is false).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sns.TopicSubscription.topic">
<code class="descname">topic</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sns.TopicSubscription.topic" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the SNS topic to subscribe to</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.sns.TopicSubscription.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.TopicSubscription.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sns.TopicSubscription.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.TopicSubscription.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sns.get_topic">
<code class="descclassname">pulumi_aws.sns.</code><code class="descname">get_topic</code><span class="sig-paren">(</span><em>name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sns.get_topic" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ARN of a topic in AWS Simple Notification
Service (SNS). By using this data source, you can reference SNS topics
without having to hard code the ARNs as input.</p>
</dd></dl>

</div>
