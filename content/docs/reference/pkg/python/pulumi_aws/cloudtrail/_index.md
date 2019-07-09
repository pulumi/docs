---
---

<div class="section" id="cloudtrail">
<h1>cloudtrail<a class="headerlink" href="#cloudtrail" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_aws.cloudtrail"></span><dl class="class">
<dt id="pulumi_aws.cloudtrail.GetServiceAccountResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.cloudtrail.</code><code class="descname">GetServiceAccountResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>region=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudtrail.GetServiceAccountResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getServiceAccount.</p>
<dl class="attribute">
<dt id="pulumi_aws.cloudtrail.GetServiceAccountResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudtrail.GetServiceAccountResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the AWS CloudTrail service account in the selected region.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudtrail.GetServiceAccountResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudtrail.GetServiceAccountResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.cloudtrail.Trail">
<em class="property">class </em><code class="descclassname">pulumi_aws.cloudtrail.</code><code class="descname">Trail</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>cloud_watch_logs_group_arn=None</em>, <em>cloud_watch_logs_role_arn=None</em>, <em>enable_log_file_validation=None</em>, <em>enable_logging=None</em>, <em>event_selectors=None</em>, <em>include_global_service_events=None</em>, <em>is_multi_region_trail=None</em>, <em>is_organization_trail=None</em>, <em>kms_key_id=None</em>, <em>name=None</em>, <em>s3_bucket_name=None</em>, <em>s3_key_prefix=None</em>, <em>sns_topic_name=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a CloudTrail resource.</p>
<blockquote>
<div><p><em>NOTE:</em> For a multi-region trail, this resource must be in the home region of the trail.</p>
<p><em>NOTE:</em> For an organization trail, this resource must be in the master account of the organization.</p>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>cloud_watch_logs_group_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a log group name using an Amazon Resource Name (ARN),
that represents the log group to which CloudTrail logs will be delivered.</li>
<li><strong>cloud_watch_logs_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the role for the CloudWatch Logs
endpoint to assume to write to a user’s log group.</li>
<li><strong>enable_log_file_validation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether log file integrity validation is enabled.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>enable_logging</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enables logging for the trail. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.
Setting this to <code class="docutils literal notranslate"><span class="pre">false</span></code> will pause logging.</li>
<li><strong>event_selectors</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies an event selector for enabling data event logging. Fields documented below. Please note the <a class="reference external" href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/WhatIsCloudTrail-Limits.html">CloudTrail limits</a> when configuring these.</li>
<li><strong>include_global_service_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the trail is publishing events
from global services such as IAM to the log files. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
<li><strong>is_multi_region_trail</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the trail is created in the current
region or in all regions. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>is_organization_trail</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the trail is an AWS Organizations trail. Organization trails log events for the master account and all member accounts. Can only be created in the organization master account. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the KMS key ARN to use to encrypt the logs delivered by CloudTrail.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the trail.</li>
<li><strong>s3_bucket_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the S3 bucket designated for publishing log files.</li>
<li><strong>s3_key_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the S3 key prefix that follows
the name of the bucket you have designated for log file delivery.</li>
<li><strong>sns_topic_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Amazon SNS topic
defined for notification of log file delivery.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the trail</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudtrail.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/cloudtrail.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.cloudtrail.Trail.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name of the trail.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudtrail.Trail.cloud_watch_logs_group_arn">
<code class="descname">cloud_watch_logs_group_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail.cloud_watch_logs_group_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a log group name using an Amazon Resource Name (ARN),
that represents the log group to which CloudTrail logs will be delivered.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudtrail.Trail.cloud_watch_logs_role_arn">
<code class="descname">cloud_watch_logs_role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail.cloud_watch_logs_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the role for the CloudWatch Logs
endpoint to assume to write to a user’s log group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudtrail.Trail.enable_log_file_validation">
<code class="descname">enable_log_file_validation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail.enable_log_file_validation" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether log file integrity validation is enabled.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudtrail.Trail.enable_logging">
<code class="descname">enable_logging</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail.enable_logging" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables logging for the trail. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.
Setting this to <code class="docutils literal notranslate"><span class="pre">false</span></code> will pause logging.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudtrail.Trail.event_selectors">
<code class="descname">event_selectors</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail.event_selectors" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies an event selector for enabling data event logging. Fields documented below. Please note the <a class="reference external" href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/WhatIsCloudTrail-Limits.html">CloudTrail limits</a> when configuring these.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudtrail.Trail.home_region">
<code class="descname">home_region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail.home_region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which the trail was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudtrail.Trail.include_global_service_events">
<code class="descname">include_global_service_events</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail.include_global_service_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the trail is publishing events
from global services such as IAM to the log files. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudtrail.Trail.is_multi_region_trail">
<code class="descname">is_multi_region_trail</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail.is_multi_region_trail" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the trail is created in the current
region or in all regions. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudtrail.Trail.is_organization_trail">
<code class="descname">is_organization_trail</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail.is_organization_trail" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the trail is an AWS Organizations trail. Organization trails log events for the master account and all member accounts. Can only be created in the organization master account. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudtrail.Trail.kms_key_id">
<code class="descname">kms_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the KMS key ARN to use to encrypt the logs delivered by CloudTrail.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudtrail.Trail.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the trail.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudtrail.Trail.s3_bucket_name">
<code class="descname">s3_bucket_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail.s3_bucket_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the S3 bucket designated for publishing log files.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudtrail.Trail.s3_key_prefix">
<code class="descname">s3_key_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail.s3_key_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the S3 key prefix that follows
the name of the bucket you have designated for log file delivery.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudtrail.Trail.sns_topic_name">
<code class="descname">sns_topic_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail.sns_topic_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Amazon SNS topic
defined for notification of log file delivery.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cloudtrail.Trail.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the trail</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cloudtrail.Trail.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudtrail.Trail.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudtrail.get_service_account">
<code class="descclassname">pulumi_aws.cloudtrail.</code><code class="descname">get_service_account</code><span class="sig-paren">(</span><em>region=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudtrail.get_service_account" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the Account ID of the <a class="reference external" href="http://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-supported-regions.html">AWS CloudTrail Service Account</a>
in a given region for the purpose of allowing CloudTrail to store trail data in S3.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/cloudtrail_service_account.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/cloudtrail_service_account.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
