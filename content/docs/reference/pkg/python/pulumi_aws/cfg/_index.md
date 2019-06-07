---
---

<div class="section" id="module-pulumi_aws.cfg">
<span id="cfg"></span><h1>cfg<a class="headerlink" href="#module-pulumi_aws.cfg" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.cfg.AggregateAuthorization">
<em class="property">class </em><code class="descclassname">pulumi_aws.cfg.</code><code class="descname">AggregateAuthorization</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>account_id=None</em>, <em>region=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.AggregateAuthorization" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an AWS Config Aggregate Authorization</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Account ID</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Region</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.cfg.AggregateAuthorization.account_id">
<code class="descname">account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.AggregateAuthorization.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Account ID</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.AggregateAuthorization.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.AggregateAuthorization.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the authorization</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.AggregateAuthorization.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.AggregateAuthorization.region" title="Permalink to this definition">¶</a></dt>
<dd><p>Region</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cfg.AggregateAuthorization.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.AggregateAuthorization.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cfg.AggregateAuthorization.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.AggregateAuthorization.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cfg.ConfigurationAggregator">
<em class="property">class </em><code class="descclassname">pulumi_aws.cfg.</code><code class="descname">ConfigurationAggregator</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>account_aggregation_source=None</em>, <em>name=None</em>, <em>organization_aggregation_source=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.ConfigurationAggregator" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an AWS Config Configuration Aggregator</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>account_aggregation_source</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The account(s) to aggregate config data from as documented below.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the configuration aggregator.</li>
<li><strong>organization_aggregation_source</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The organization to aggregate config data from as documented below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.cfg.ConfigurationAggregator.account_aggregation_source">
<code class="descname">account_aggregation_source</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.ConfigurationAggregator.account_aggregation_source" title="Permalink to this definition">¶</a></dt>
<dd><p>The account(s) to aggregate config data from as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.ConfigurationAggregator.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.ConfigurationAggregator.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the aggregator</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.ConfigurationAggregator.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.ConfigurationAggregator.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the configuration aggregator.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.ConfigurationAggregator.organization_aggregation_source">
<code class="descname">organization_aggregation_source</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.ConfigurationAggregator.organization_aggregation_source" title="Permalink to this definition">¶</a></dt>
<dd><p>The organization to aggregate config data from as documented below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cfg.ConfigurationAggregator.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.ConfigurationAggregator.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cfg.ConfigurationAggregator.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.ConfigurationAggregator.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cfg.DeliveryChannel">
<em class="property">class </em><code class="descclassname">pulumi_aws.cfg.</code><code class="descname">DeliveryChannel</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>s3_bucket_name=None</em>, <em>s3_key_prefix=None</em>, <em>snapshot_delivery_properties=None</em>, <em>sns_topic_arn=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.DeliveryChannel" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AWS Config Delivery Channel.</p>
<blockquote>
<div><strong>Note:</strong> Delivery Channel requires a <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/config_configuration_recorder.html">Configuration Recorder</a> to be present. Use of <code class="docutils literal notranslate"><span class="pre">depends_on</span></code> (as shown below) is recommended to avoid race conditions.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the delivery channel. Defaults to <code class="docutils literal notranslate"><span class="pre">default</span></code>. Changing it recreates the resource.</li>
<li><strong>s3_bucket_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the S3 bucket used to store the configuration history.</li>
<li><strong>s3_key_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The prefix for the specified S3 bucket.</li>
<li><strong>snapshot_delivery_properties</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Options for how AWS Config delivers configuration snapshots. See below</li>
<li><strong>sns_topic_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the SNS topic that AWS Config delivers notifications to.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.cfg.DeliveryChannel.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.DeliveryChannel.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the delivery channel. Defaults to <code class="docutils literal notranslate"><span class="pre">default</span></code>. Changing it recreates the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.DeliveryChannel.s3_bucket_name">
<code class="descname">s3_bucket_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.DeliveryChannel.s3_bucket_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the S3 bucket used to store the configuration history.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.DeliveryChannel.s3_key_prefix">
<code class="descname">s3_key_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.DeliveryChannel.s3_key_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The prefix for the specified S3 bucket.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.DeliveryChannel.snapshot_delivery_properties">
<code class="descname">snapshot_delivery_properties</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.DeliveryChannel.snapshot_delivery_properties" title="Permalink to this definition">¶</a></dt>
<dd><p>Options for how AWS Config delivers configuration snapshots. See below</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.DeliveryChannel.sns_topic_arn">
<code class="descname">sns_topic_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.DeliveryChannel.sns_topic_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the SNS topic that AWS Config delivers notifications to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cfg.DeliveryChannel.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.DeliveryChannel.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cfg.DeliveryChannel.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.DeliveryChannel.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cfg.Recorder">
<em class="property">class </em><code class="descclassname">pulumi_aws.cfg.</code><code class="descname">Recorder</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>name=None</em>, <em>recording_group=None</em>, <em>role_arn=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.Recorder" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AWS Config Configuration Recorder. Please note that this resource <strong>does not start</strong> the created recorder automatically.</p>
<blockquote>
<div><strong>Note:</strong> <em>Starting</em> the Configuration Recorder requires a <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/config_delivery_channel.html">delivery channel</a> (while delivery channel creation requires Configuration Recorder). This is why <cite>``aws_config_configuration_recorder_status`</cite> &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/config_configuration_recorder_status.html">https://www.terraform.io/docs/providers/aws/r/config_configuration_recorder_status.html</a>&gt;`_ is a separate resource.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the recorder. Defaults to <code class="docutils literal notranslate"><span class="pre">default</span></code>. Changing it recreates the resource.</li>
<li><strong>recording_group</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Recording group - see below.</li>
<li><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Amazon Resource Name (ARN) of the IAM role.
used to make read or write requests to the delivery channel and to describe the AWS resources associated with the account.
See <a class="reference external" href="http://docs.aws.amazon.com/config/latest/developerguide/iamrole-permissions.html">AWS Docs</a> for more details.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.cfg.Recorder.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.Recorder.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the recorder. Defaults to <code class="docutils literal notranslate"><span class="pre">default</span></code>. Changing it recreates the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.Recorder.recording_group">
<code class="descname">recording_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.Recorder.recording_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Recording group - see below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.Recorder.role_arn">
<code class="descname">role_arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.Recorder.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>Amazon Resource Name (ARN) of the IAM role.
used to make read or write requests to the delivery channel and to describe the AWS resources associated with the account.
See <a class="reference external" href="http://docs.aws.amazon.com/config/latest/developerguide/iamrole-permissions.html">AWS Docs</a> for more details.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cfg.Recorder.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.Recorder.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cfg.Recorder.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.Recorder.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cfg.RecorderStatus">
<em class="property">class </em><code class="descclassname">pulumi_aws.cfg.</code><code class="descname">RecorderStatus</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>is_enabled=None</em>, <em>name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.RecorderStatus" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages status (recording / stopped) of an AWS Config Configuration Recorder.</p>
<blockquote>
<div><strong>Note:</strong> Starting Configuration Recorder requires a <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/config_delivery_channel.html">Delivery Channel</a> to be present. Use of <code class="docutils literal notranslate"><span class="pre">depends_on</span></code> (as shown below) is recommended to avoid race conditions.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>is_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the configuration recorder should be enabled or disabled.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the recorder</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.cfg.RecorderStatus.is_enabled">
<code class="descname">is_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.RecorderStatus.is_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the configuration recorder should be enabled or disabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.RecorderStatus.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.RecorderStatus.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the recorder</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cfg.RecorderStatus.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.RecorderStatus.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cfg.RecorderStatus.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.RecorderStatus.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cfg.Rule">
<em class="property">class </em><code class="descclassname">pulumi_aws.cfg.</code><code class="descname">Rule</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>input_parameters=None</em>, <em>maximum_execution_frequency=None</em>, <em>name=None</em>, <em>scope=None</em>, <em>source=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.Rule" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an AWS Config Rule.</p>
<blockquote>
<div><strong>Note:</strong> Config Rule requires an existing <a class="reference external" href="https://www.terraform.io/docs/providers/aws/r/config_configuration_recorder.html">Configuration Recorder</a> to be present. Use of <code class="docutils literal notranslate"><span class="pre">depends_on</span></code> is recommended (as shown below) to avoid race conditions.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the rule</li>
<li><strong>input_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string in JSON format that is passed to the AWS Config rule Lambda function.</li>
<li><strong>maximum_execution_frequency</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The frequency that you want AWS Config to run evaluations for a rule that
is triggered periodically. If specified, requires <code class="docutils literal notranslate"><span class="pre">message_type</span></code> to be <code class="docutils literal notranslate"><span class="pre">ScheduledNotification</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the rule</li>
<li><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Scope defines which resources can trigger an evaluation for the rule as documented below.</li>
<li><strong>source</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Source specifies the rule owner, the rule identifier, and the notifications that cause
the function to evaluate your AWS resources as documented below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_aws.cfg.Rule.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.Rule.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the config rule</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.Rule.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.Rule.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the rule</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.Rule.input_parameters">
<code class="descname">input_parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.Rule.input_parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A string in JSON format that is passed to the AWS Config rule Lambda function.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.Rule.maximum_execution_frequency">
<code class="descname">maximum_execution_frequency</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.Rule.maximum_execution_frequency" title="Permalink to this definition">¶</a></dt>
<dd><p>The frequency that you want AWS Config to run evaluations for a rule that
is triggered periodically. If specified, requires <code class="docutils literal notranslate"><span class="pre">message_type</span></code> to be <code class="docutils literal notranslate"><span class="pre">ScheduledNotification</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.Rule.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.Rule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the rule</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.Rule.rule_id">
<code class="descname">rule_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.Rule.rule_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the config rule</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.Rule.scope">
<code class="descname">scope</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.Rule.scope" title="Permalink to this definition">¶</a></dt>
<dd><p>Scope defines which resources can trigger an evaluation for the rule as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.cfg.Rule.source">
<code class="descname">source</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.cfg.Rule.source" title="Permalink to this definition">¶</a></dt>
<dd><p>Source specifies the rule owner, the rule identifier, and the notifications that cause
the function to evaluate your AWS resources as documented below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.cfg.Rule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.Rule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.cfg.Rule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.cfg.Rule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
