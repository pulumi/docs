---
title: Module cloudtrail
title_tag: Module cloudtrail | Package pulumi_aws | Python SDK
linktitle: cloudtrail
notitle: true
---

<div class="section" id="cloudtrail">
<h1>cloudtrail<a class="headerlink" href="#cloudtrail" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.cloudtrail"></span><dl class="py class">
<dt id="pulumi_aws.cloudtrail.AwaitableGetServiceAccountResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cloudtrail.</code><code class="sig-name descname">AwaitableGetServiceAccountResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudtrail.AwaitableGetServiceAccountResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.cloudtrail.GetServiceAccountResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cloudtrail.</code><code class="sig-name descname">GetServiceAccountResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudtrail.GetServiceAccountResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getServiceAccount.</p>
<dl class="py attribute">
<dt id="pulumi_aws.cloudtrail.GetServiceAccountResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudtrail.GetServiceAccountResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the AWS CloudTrail service account in the selected region.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudtrail.GetServiceAccountResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudtrail.GetServiceAccountResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.cloudtrail.Trail">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.cloudtrail.</code><code class="sig-name descname">Trail</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_watch_logs_group_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_watch_logs_role_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_log_file_validation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_logging</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">event_selectors</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">include_global_service_events</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_multi_region_trail</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_organization_trail</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">s3_bucket_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">s3_key_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sns_topic_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a CloudTrail resource.</p>
<blockquote>
<div><p><em>NOTE:</em> For a multi-region trail, this resource must be in the home region of the trail.</p>
<p><em>NOTE:</em> For an organization trail, this resource must be in the master account of the organization.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cloud_watch_logs_group_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a log group name using an Amazon Resource Name (ARN),
that represents the log group to which CloudTrail logs will be delivered.</p></li>
<li><p><strong>cloud_watch_logs_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the role for the CloudWatch Logs
endpoint to assume to write to a user’s log group.</p></li>
<li><p><strong>enable_log_file_validation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether log file integrity validation is enabled.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>enable_logging</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enables logging for the trail. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.
Setting this to <code class="docutils literal notranslate"><span class="pre">false</span></code> will pause logging.</p></li>
<li><p><strong>event_selectors</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies an event selector for enabling data event logging. Fields documented below. Please note the <a class="reference external" href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/WhatIsCloudTrail-Limits.html">CloudTrail limits</a> when configuring these.</p></li>
<li><p><strong>include_global_service_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the trail is publishing events
from global services such as IAM to the log files. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>is_multi_region_trail</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the trail is created in the current
region or in all regions. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>is_organization_trail</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the trail is an AWS Organizations trail. Organization trails log events for the master account and all member accounts. Can only be created in the organization master account. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the KMS key ARN to use to encrypt the logs delivered by CloudTrail.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the trail.</p></li>
<li><p><strong>s3_bucket_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the S3 bucket designated for publishing log files.</p></li>
<li><p><strong>s3_key_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the S3 key prefix that follows
the name of the bucket you have designated for log file delivery.</p></li>
<li><p><strong>sns_topic_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Amazon SNS topic
defined for notification of log file delivery.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the trail</p></li>
</ul>
</dd>
</dl>
<p>The <strong>event_selectors</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataResources</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies logging data events. Fields documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The resource type in which you want to log data events. You can specify only the following value: “AWS::S3::Object”, “AWS::Lambda::Function”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of ARN for the specified S3 buckets and object prefixes..</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeManagementEvents</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specify if you want your event selector to include management events for your trail.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">readWriteType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specify if you want your trail to log read-only events, write-only events, or all. By default, the value is All. You can specify only the following value: “ReadOnly”, “WriteOnly”, “All”. Defaults to <code class="docutils literal notranslate"><span class="pre">All</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_aws.cloudtrail.Trail.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name of the trail.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudtrail.Trail.cloud_watch_logs_group_arn">
<code class="sig-name descname">cloud_watch_logs_group_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail.cloud_watch_logs_group_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a log group name using an Amazon Resource Name (ARN),
that represents the log group to which CloudTrail logs will be delivered.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudtrail.Trail.cloud_watch_logs_role_arn">
<code class="sig-name descname">cloud_watch_logs_role_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail.cloud_watch_logs_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the role for the CloudWatch Logs
endpoint to assume to write to a user’s log group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudtrail.Trail.enable_log_file_validation">
<code class="sig-name descname">enable_log_file_validation</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail.enable_log_file_validation" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether log file integrity validation is enabled.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudtrail.Trail.enable_logging">
<code class="sig-name descname">enable_logging</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail.enable_logging" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables logging for the trail. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.
Setting this to <code class="docutils literal notranslate"><span class="pre">false</span></code> will pause logging.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudtrail.Trail.event_selectors">
<code class="sig-name descname">event_selectors</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail.event_selectors" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies an event selector for enabling data event logging. Fields documented below. Please note the <a class="reference external" href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/WhatIsCloudTrail-Limits.html">CloudTrail limits</a> when configuring these.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataResources</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Specifies logging data events. Fields documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The resource type in which you want to log data events. You can specify only the following value: “AWS::S3::Object”, “AWS::Lambda::Function”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of ARN for the specified S3 buckets and object prefixes..</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeManagementEvents</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specify if you want your event selector to include management events for your trail.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">readWriteType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specify if you want your trail to log read-only events, write-only events, or all. By default, the value is All. You can specify only the following value: “ReadOnly”, “WriteOnly”, “All”. Defaults to <code class="docutils literal notranslate"><span class="pre">All</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudtrail.Trail.home_region">
<code class="sig-name descname">home_region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail.home_region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which the trail was created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudtrail.Trail.include_global_service_events">
<code class="sig-name descname">include_global_service_events</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail.include_global_service_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the trail is publishing events
from global services such as IAM to the log files. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudtrail.Trail.is_multi_region_trail">
<code class="sig-name descname">is_multi_region_trail</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail.is_multi_region_trail" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the trail is created in the current
region or in all regions. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudtrail.Trail.is_organization_trail">
<code class="sig-name descname">is_organization_trail</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail.is_organization_trail" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the trail is an AWS Organizations trail. Organization trails log events for the master account and all member accounts. Can only be created in the organization master account. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudtrail.Trail.kms_key_id">
<code class="sig-name descname">kms_key_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail.kms_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the KMS key ARN to use to encrypt the logs delivered by CloudTrail.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudtrail.Trail.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the trail.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudtrail.Trail.s3_bucket_name">
<code class="sig-name descname">s3_bucket_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail.s3_bucket_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the S3 bucket designated for publishing log files.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudtrail.Trail.s3_key_prefix">
<code class="sig-name descname">s3_key_prefix</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail.s3_key_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the S3 key prefix that follows
the name of the bucket you have designated for log file delivery.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudtrail.Trail.sns_topic_name">
<code class="sig-name descname">sns_topic_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail.sns_topic_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Amazon SNS topic
defined for notification of log file delivery.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.cloudtrail.Trail.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the trail</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloudtrail.Trail.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_watch_logs_group_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_watch_logs_role_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_log_file_validation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_logging</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">event_selectors</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">home_region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">include_global_service_events</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_multi_region_trail</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_organization_trail</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">s3_bucket_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">s3_key_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sns_topic_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Trail resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name of the trail.</p></li>
<li><p><strong>cloud_watch_logs_group_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a log group name using an Amazon Resource Name (ARN),
that represents the log group to which CloudTrail logs will be delivered.</p></li>
<li><p><strong>cloud_watch_logs_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the role for the CloudWatch Logs
endpoint to assume to write to a user’s log group.</p></li>
<li><p><strong>enable_log_file_validation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether log file integrity validation is enabled.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>enable_logging</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enables logging for the trail. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.
Setting this to <code class="docutils literal notranslate"><span class="pre">false</span></code> will pause logging.</p></li>
<li><p><strong>event_selectors</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>Specifies an event selector for enabling data event logging. Fields documented below. Please note the <a class="reference external" href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/WhatIsCloudTrail-Limits.html">CloudTrail limits</a> when configuring these.</p>
</p></li>
<li><p><strong>home_region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which the trail was created.</p></li>
<li><p><strong>include_global_service_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the trail is publishing events
from global services such as IAM to the log files. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>is_multi_region_trail</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the trail is created in the current
region or in all regions. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>is_organization_trail</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the trail is an AWS Organizations trail. Organization trails log events for the master account and all member accounts. Can only be created in the organization master account. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>kms_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the KMS key ARN to use to encrypt the logs delivered by CloudTrail.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the trail.</p></li>
<li><p><strong>s3_bucket_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the S3 bucket designated for publishing log files.</p></li>
<li><p><strong>s3_key_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the S3 key prefix that follows
the name of the bucket you have designated for log file delivery.</p></li>
<li><p><strong>sns_topic_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Amazon SNS topic
defined for notification of log file delivery.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the trail</p></li>
</ul>
</dd>
</dl>
<p>The <strong>event_selectors</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dataResources</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies logging data events. Fields documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The resource type in which you want to log data events. You can specify only the following value: “AWS::S3::Object”, “AWS::Lambda::Function”</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of ARN for the specified S3 buckets and object prefixes..</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeManagementEvents</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specify if you want your event selector to include management events for your trail.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">readWriteType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specify if you want your trail to log read-only events, write-only events, or all. By default, the value is All. You can specify only the following value: “ReadOnly”, “WriteOnly”, “All”. Defaults to <code class="docutils literal notranslate"><span class="pre">All</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.cloudtrail.Trail.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cloudtrail.Trail.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudtrail.Trail.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py function">
<dt id="pulumi_aws.cloudtrail.get_service_account">
<code class="sig-prename descclassname">pulumi_aws.cloudtrail.</code><code class="sig-name descname">get_service_account</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cloudtrail.get_service_account" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the Account ID of the <a class="reference external" href="http://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-supported-regions.html">AWS CloudTrail Service Account</a>
in a given region for the purpose of allowing CloudTrail to store trail data in S3.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>region</strong> (<em>str</em>) – Name of the region whose AWS CloudTrail account ID is desired.
Defaults to the region from the AWS provider configuration.</p>
</dd>
</dl>
</dd></dl>

</div>
