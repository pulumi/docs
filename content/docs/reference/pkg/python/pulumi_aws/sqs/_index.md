---
---

<div class="section" id="module-pulumi_aws.sqs">
<span id="sqs"></span><h1>sqs<a class="headerlink" href="#module-pulumi_aws.sqs" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_aws.sqs.GetQueueResult">
<em class="property">class </em><code class="descclassname">pulumi_aws.sqs.</code><code class="descname">GetQueueResult</code><span class="sig-paren">(</span><em>arn=None</em>, <em>name=None</em>, <em>url=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sqs.GetQueueResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getQueue.</p>
<dl class="attribute">
<dt id="pulumi_aws.sqs.GetQueueResult.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.GetQueueResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the queue.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sqs.GetQueueResult.url">
<code class="descname">url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.GetQueueResult.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the queue.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sqs.GetQueueResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.GetQueueResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_aws.sqs.Queue">
<em class="property">class </em><code class="descclassname">pulumi_aws.sqs.</code><code class="descname">Queue</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>content_based_deduplication=None</em>, <em>delay_seconds=None</em>, <em>fifo_queue=None</em>, <em>kms_data_key_reuse_period_seconds=None</em>, <em>kms_master_key_id=None</em>, <em>max_message_size=None</em>, <em>message_retention_seconds=None</em>, <em>name=None</em>, <em>name_prefix=None</em>, <em>policy=None</em>, <em>receive_wait_time_seconds=None</em>, <em>redrive_policy=None</em>, <em>tags=None</em>, <em>visibility_timeout_seconds=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sqs.Queue" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Queue resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>content_based_deduplication</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enables content-based deduplication for FIFO queues. For more information, see the <a class="reference external" href="http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html#FIFO-queues-exactly-once-processing">related documentation</a></li>
<li><strong>delay_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time in seconds that the delivery of all messages in the queue will be delayed. An integer from 0 to 900 (15 minutes). The default for this attribute is 0 seconds.</li>
<li><strong>fifo_queue</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean designating a FIFO queue. If not set, it defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code> making it standard.</li>
<li><strong>kms_data_key_reuse_period_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The length of time, in seconds, for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again. An integer representing seconds, between 60 seconds (1 minute) and 86,400 seconds (24 hours). The default is 300 (5 minutes).</li>
<li><strong>kms_master_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of an AWS-managed customer master key (CMK) for Amazon SQS or a custom CMK. For more information, see <a class="reference external" href="http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-sse-key-terms">Key Terms</a>.</li>
<li><strong>max_message_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The limit of how many bytes a message can contain before Amazon SQS rejects it. An integer from 1024 bytes (1 KiB) up to 262144 bytes (256 KiB). The default for this attribute is 262144 (256 KiB).</li>
<li><strong>message_retention_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of seconds Amazon SQS retains a message. Integer representing seconds, from 60 (1 minute) to 1209600 (14 days). The default for this attribute is 345600 (4 days).</li>
<li><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</li>
<li><strong>receive_wait_time_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time for which a ReceiveMessage call will wait for a message to arrive (long polling) before returning. An integer from 0 to 20 (seconds). The default for this attribute is 0, meaning that the call will return immediately.</li>
<li><strong>redrive_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The JSON policy to set up the Dead Letter Queue, see <a class="reference external" href="https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/SQSDeadLetterQueue.html">AWS docs</a>. <strong>Note:</strong> when specifying <code class="docutils literal notranslate"><span class="pre">maxReceiveCount</span></code>, you must specify it as an integer (<code class="docutils literal notranslate"><span class="pre">5</span></code>), and not a string (<code class="docutils literal notranslate"><span class="pre">&quot;5&quot;</span></code>).</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the queue.</li>
<li><strong>visibility_timeout_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>The visibility timeout for the queue. An integer from 0 to 43200 (12 hours). The default for this attribute is 30. For more information about visibility timeout, see <a class="reference external" href="https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/AboutVT.html">AWS docs</a>.</p>
</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sqs_queue.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sqs_queue.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.sqs.Queue.arn">
<code class="descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.Queue.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the SQS queue</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sqs.Queue.content_based_deduplication">
<code class="descname">content_based_deduplication</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.Queue.content_based_deduplication" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables content-based deduplication for FIFO queues. For more information, see the <a class="reference external" href="http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html#FIFO-queues-exactly-once-processing">related documentation</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sqs.Queue.delay_seconds">
<code class="descname">delay_seconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.Queue.delay_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>The time in seconds that the delivery of all messages in the queue will be delayed. An integer from 0 to 900 (15 minutes). The default for this attribute is 0 seconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sqs.Queue.fifo_queue">
<code class="descname">fifo_queue</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.Queue.fifo_queue" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean designating a FIFO queue. If not set, it defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code> making it standard.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sqs.Queue.kms_data_key_reuse_period_seconds">
<code class="descname">kms_data_key_reuse_period_seconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.Queue.kms_data_key_reuse_period_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>The length of time, in seconds, for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again. An integer representing seconds, between 60 seconds (1 minute) and 86,400 seconds (24 hours). The default is 300 (5 minutes).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sqs.Queue.kms_master_key_id">
<code class="descname">kms_master_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.Queue.kms_master_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of an AWS-managed customer master key (CMK) for Amazon SQS or a custom CMK. For more information, see <a class="reference external" href="http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-sse-key-terms">Key Terms</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sqs.Queue.max_message_size">
<code class="descname">max_message_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.Queue.max_message_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The limit of how many bytes a message can contain before Amazon SQS rejects it. An integer from 1024 bytes (1 KiB) up to 262144 bytes (256 KiB). The default for this attribute is 262144 (256 KiB).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sqs.Queue.message_retention_seconds">
<code class="descname">message_retention_seconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.Queue.message_retention_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of seconds Amazon SQS retains a message. Integer representing seconds, from 60 (1 minute) to 1209600 (14 days). The default for this attribute is 345600 (4 days).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sqs.Queue.name_prefix">
<code class="descname">name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.Queue.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sqs.Queue.receive_wait_time_seconds">
<code class="descname">receive_wait_time_seconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.Queue.receive_wait_time_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>The time for which a ReceiveMessage call will wait for a message to arrive (long polling) before returning. An integer from 0 to 20 (seconds). The default for this attribute is 0, meaning that the call will return immediately.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sqs.Queue.redrive_policy">
<code class="descname">redrive_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.Queue.redrive_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The JSON policy to set up the Dead Letter Queue, see <a class="reference external" href="https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/SQSDeadLetterQueue.html">AWS docs</a>. <strong>Note:</strong> when specifying <code class="docutils literal notranslate"><span class="pre">maxReceiveCount</span></code>, you must specify it as an integer (<code class="docutils literal notranslate"><span class="pre">5</span></code>), and not a string (<code class="docutils literal notranslate"><span class="pre">&quot;5&quot;</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sqs.Queue.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.Queue.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the queue.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_aws.sqs.Queue.visibility_timeout_seconds">
<code class="descname">visibility_timeout_seconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.Queue.visibility_timeout_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>The visibility timeout for the queue. An integer from 0 to 43200 (12 hours). The default for this attribute is 30. For more information about visibility timeout, see <a class="reference external" href="https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/AboutVT.html">AWS docs</a>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.sqs.Queue.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sqs.Queue.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sqs.Queue.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sqs.Queue.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sqs.QueuePolicy">
<em class="property">class </em><code class="descclassname">pulumi_aws.sqs.</code><code class="descname">QueuePolicy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>policy=None</em>, <em>queue_url=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sqs.QueuePolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows you to set a policy of an SQS Queue
while referencing ARN of the queue within the policy.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>queue_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the SQS Queue to which to attach the policy</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sqs_queue_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/sqs_queue_policy.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_aws.sqs.QueuePolicy.queue_url">
<code class="descname">queue_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.QueuePolicy.queue_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the SQS Queue to which to attach the policy</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_aws.sqs.QueuePolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sqs.QueuePolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sqs.QueuePolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sqs.QueuePolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sqs.get_queue">
<code class="descclassname">pulumi_aws.sqs.</code><code class="descname">get_queue</code><span class="sig-paren">(</span><em>name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sqs.get_queue" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ARN and URL of queue in AWS Simple Queue Service (SQS).
By using this data source, you can reference SQS queues without having to hardcode
the ARNs as input.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/sqs_queue.html.markdown">https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/sqs_queue.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
