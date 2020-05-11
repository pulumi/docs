---
title: Module sqs
title_tag: Module sqs | Package pulumi_aws | Python SDK
linktitle: sqs
notitle: true
---

<div class="section" id="sqs">
<h1>sqs<a class="headerlink" href="#sqs" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-aws/issues">pulumi/pulumi-aws repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-aws/issues">terraform-providers/terraform-provider-aws repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_aws.sqs"></span><dl class="py class">
<dt id="pulumi_aws.sqs.AwaitableGetQueueResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.sqs.</code><code class="sig-name descname">AwaitableGetQueueResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sqs.AwaitableGetQueueResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_aws.sqs.GetQueueResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.sqs.</code><code class="sig-name descname">GetQueueResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sqs.GetQueueResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getQueue.</p>
<dl class="py attribute">
<dt id="pulumi_aws.sqs.GetQueueResult.arn">
<code class="sig-name descname">arn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.GetQueueResult.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the queue.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.sqs.GetQueueResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.GetQueueResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.sqs.GetQueueResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.GetQueueResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags for the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.sqs.GetQueueResult.url">
<code class="sig-name descname">url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.GetQueueResult.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the queue.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_aws.sqs.Queue">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.sqs.</code><code class="sig-name descname">Queue</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content_based_deduplication</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delay_seconds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fifo_queue</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_data_key_reuse_period_seconds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_master_key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_message_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message_retention_seconds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">receive_wait_time_seconds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redrive_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">visibility_timeout_seconds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sqs.Queue" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">json</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">queue</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">sqs</span><span class="o">.</span><span class="n">Queue</span><span class="p">(</span><span class="s2">&quot;queue&quot;</span><span class="p">,</span>
    <span class="n">delay_seconds</span><span class="o">=</span><span class="mi">90</span><span class="p">,</span>
    <span class="n">max_message_size</span><span class="o">=</span><span class="mi">2048</span><span class="p">,</span>
    <span class="n">message_retention_seconds</span><span class="o">=</span><span class="mi">86400</span><span class="p">,</span>
    <span class="n">receive_wait_time_seconds</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span>
    <span class="n">redrive_policy</span><span class="o">=</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">({</span>
        <span class="s2">&quot;deadLetterTargetArn&quot;</span><span class="p">:</span> <span class="n">aws_sqs_queue</span><span class="p">[</span><span class="s2">&quot;queue_deadletter&quot;</span><span class="p">][</span><span class="s2">&quot;arn&quot;</span><span class="p">],</span>
        <span class="s2">&quot;maxReceiveCount&quot;</span><span class="p">:</span> <span class="mi">4</span><span class="p">,</span>
    <span class="p">}),</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;Environment&quot;</span><span class="p">:</span> <span class="s2">&quot;production&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">queue</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">sqs</span><span class="o">.</span><span class="n">Queue</span><span class="p">(</span><span class="s2">&quot;queue&quot;</span><span class="p">,</span>
    <span class="n">content_based_deduplication</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">fifo_queue</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">queue</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">sqs</span><span class="o">.</span><span class="n">Queue</span><span class="p">(</span><span class="s2">&quot;queue&quot;</span><span class="p">,</span>
    <span class="n">kms_data_key_reuse_period_seconds</span><span class="o">=</span><span class="mi">300</span><span class="p">,</span>
    <span class="n">kms_master_key_id</span><span class="o">=</span><span class="s2">&quot;alias/aws/sqs&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>content_based_deduplication</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enables content-based deduplication for FIFO queues. For more information, see the <a class="reference external" href="http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html#FIFO-queues-exactly-once-processing">related documentation</a></p></li>
<li><p><strong>delay_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time in seconds that the delivery of all messages in the queue will be delayed. An integer from 0 to 900 (15 minutes). The default for this attribute is 0 seconds.</p></li>
<li><p><strong>fifo_queue</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean designating a FIFO queue. If not set, it defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code> making it standard.</p></li>
<li><p><strong>kms_data_key_reuse_period_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The length of time, in seconds, for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again. An integer representing seconds, between 60 seconds (1 minute) and 86,400 seconds (24 hours). The default is 300 (5 minutes).</p></li>
<li><p><strong>kms_master_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of an AWS-managed customer master key (CMK) for Amazon SQS or a custom CMK. For more information, see <a class="reference external" href="http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-sse-key-terms">Key Terms</a>.</p></li>
<li><p><strong>max_message_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The limit of how many bytes a message can contain before Amazon SQS rejects it. An integer from 1024 bytes (1 KiB) up to 262144 bytes (256 KiB). The default for this attribute is 262144 (256 KiB).</p></li>
<li><p><strong>message_retention_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of seconds Amazon SQS retains a message. Integer representing seconds, from 60 (1 minute) to 1209600 (14 days). The default for this attribute is 345600 (4 days).</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is the human-readable name of the queue. If omitted, this provider will assign a random name.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The JSON policy for the SQS queue.</p></li>
<li><p><strong>receive_wait_time_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time for which a ReceiveMessage call will wait for a message to arrive (long polling) before returning. An integer from 0 to 20 (seconds). The default for this attribute is 0, meaning that the call will return immediately.</p></li>
<li><p><strong>redrive_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The JSON policy to set up the Dead Letter Queue, see <a class="reference external" href="https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/SQSDeadLetterQueue.html">AWS docs</a>. <strong>Note:</strong> when specifying <code class="docutils literal notranslate"><span class="pre">maxReceiveCount</span></code>, you must specify it as an integer (<code class="docutils literal notranslate"><span class="pre">5</span></code>), and not a string (<code class="docutils literal notranslate"><span class="pre">&quot;5&quot;</span></code>).</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the queue.</p></li>
<li><p><strong>visibility_timeout_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>The visibility timeout for the queue. An integer from 0 to 43200 (12 hours). The default for this attribute is 30. For more information about visibility timeout, see <a class="reference external" href="https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/AboutVT.html">AWS docs</a>.</p>
</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.sqs.Queue.arn">
<code class="sig-name descname">arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.Queue.arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The ARN of the SQS queue</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.sqs.Queue.content_based_deduplication">
<code class="sig-name descname">content_based_deduplication</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.Queue.content_based_deduplication" title="Permalink to this definition">¶</a></dt>
<dd><p>Enables content-based deduplication for FIFO queues. For more information, see the <a class="reference external" href="http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html#FIFO-queues-exactly-once-processing">related documentation</a></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.sqs.Queue.delay_seconds">
<code class="sig-name descname">delay_seconds</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.Queue.delay_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>The time in seconds that the delivery of all messages in the queue will be delayed. An integer from 0 to 900 (15 minutes). The default for this attribute is 0 seconds.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.sqs.Queue.fifo_queue">
<code class="sig-name descname">fifo_queue</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.Queue.fifo_queue" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean designating a FIFO queue. If not set, it defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code> making it standard.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.sqs.Queue.kms_data_key_reuse_period_seconds">
<code class="sig-name descname">kms_data_key_reuse_period_seconds</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.Queue.kms_data_key_reuse_period_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>The length of time, in seconds, for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again. An integer representing seconds, between 60 seconds (1 minute) and 86,400 seconds (24 hours). The default is 300 (5 minutes).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.sqs.Queue.kms_master_key_id">
<code class="sig-name descname">kms_master_key_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.Queue.kms_master_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of an AWS-managed customer master key (CMK) for Amazon SQS or a custom CMK. For more information, see <a class="reference external" href="http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-sse-key-terms">Key Terms</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.sqs.Queue.max_message_size">
<code class="sig-name descname">max_message_size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.Queue.max_message_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The limit of how many bytes a message can contain before Amazon SQS rejects it. An integer from 1024 bytes (1 KiB) up to 262144 bytes (256 KiB). The default for this attribute is 262144 (256 KiB).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.sqs.Queue.message_retention_seconds">
<code class="sig-name descname">message_retention_seconds</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.Queue.message_retention_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of seconds Amazon SQS retains a message. Integer representing seconds, from 60 (1 minute) to 1209600 (14 days). The default for this attribute is 345600 (4 days).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.sqs.Queue.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.Queue.name" title="Permalink to this definition">¶</a></dt>
<dd><p>This is the human-readable name of the queue. If omitted, this provider will assign a random name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.sqs.Queue.name_prefix">
<code class="sig-name descname">name_prefix</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.Queue.name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.sqs.Queue.policy">
<code class="sig-name descname">policy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.Queue.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The JSON policy for the SQS queue.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.sqs.Queue.receive_wait_time_seconds">
<code class="sig-name descname">receive_wait_time_seconds</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.Queue.receive_wait_time_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>The time for which a ReceiveMessage call will wait for a message to arrive (long polling) before returning. An integer from 0 to 20 (seconds). The default for this attribute is 0, meaning that the call will return immediately.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.sqs.Queue.redrive_policy">
<code class="sig-name descname">redrive_policy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.Queue.redrive_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The JSON policy to set up the Dead Letter Queue, see <a class="reference external" href="https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/SQSDeadLetterQueue.html">AWS docs</a>. <strong>Note:</strong> when specifying <code class="docutils literal notranslate"><span class="pre">maxReceiveCount</span></code>, you must specify it as an integer (<code class="docutils literal notranslate"><span class="pre">5</span></code>), and not a string (<code class="docutils literal notranslate"><span class="pre">&quot;5&quot;</span></code>).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.sqs.Queue.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.Queue.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags to assign to the queue.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.sqs.Queue.visibility_timeout_seconds">
<code class="sig-name descname">visibility_timeout_seconds</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.Queue.visibility_timeout_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>The visibility timeout for the queue. An integer from 0 to 43200 (12 hours). The default for this attribute is 30. For more information about visibility timeout, see <a class="reference external" href="https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/AboutVT.html">AWS docs</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.sqs.Queue.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content_based_deduplication</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delay_seconds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fifo_queue</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_data_key_reuse_period_seconds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_master_key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_message_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message_retention_seconds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">receive_wait_time_seconds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">redrive_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">visibility_timeout_seconds</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sqs.Queue.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Queue resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ARN of the SQS queue</p></li>
<li><p><strong>content_based_deduplication</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>Enables content-based deduplication for FIFO queues. For more information, see the <a class="reference external" href="http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/FIFO-queues.html#FIFO-queues-exactly-once-processing">related documentation</a></p>
</p></li>
<li><p><strong>delay_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time in seconds that the delivery of all messages in the queue will be delayed. An integer from 0 to 900 (15 minutes). The default for this attribute is 0 seconds.</p></li>
<li><p><strong>fifo_queue</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean designating a FIFO queue. If not set, it defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code> making it standard.</p></li>
<li><p><strong>kms_data_key_reuse_period_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The length of time, in seconds, for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling AWS KMS again. An integer representing seconds, between 60 seconds (1 minute) and 86,400 seconds (24 hours). The default is 300 (5 minutes).</p></li>
<li><p><strong>kms_master_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The ID of an AWS-managed customer master key (CMK) for Amazon SQS or a custom CMK. For more information, see <a class="reference external" href="http://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-server-side-encryption.html#sqs-sse-key-terms">Key Terms</a>.</p>
</p></li>
<li><p><strong>max_message_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The limit of how many bytes a message can contain before Amazon SQS rejects it. An integer from 1024 bytes (1 KiB) up to 262144 bytes (256 KiB). The default for this attribute is 262144 (256 KiB).</p></li>
<li><p><strong>message_retention_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of seconds Amazon SQS retains a message. Integer representing seconds, from 60 (1 minute) to 1209600 (14 days). The default for this attribute is 345600 (4 days).</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is the human-readable name of the queue. If omitted, this provider will assign a random name.</p></li>
<li><p><strong>name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a unique name beginning with the specified prefix. Conflicts with <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The JSON policy for the SQS queue.</p></li>
<li><p><strong>receive_wait_time_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time for which a ReceiveMessage call will wait for a message to arrive (long polling) before returning. An integer from 0 to 20 (seconds). The default for this attribute is 0, meaning that the call will return immediately.</p></li>
<li><p><strong>redrive_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The JSON policy to set up the Dead Letter Queue, see <a class="reference external" href="https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/SQSDeadLetterQueue.html">AWS docs</a>. <strong>Note:</strong> when specifying <code class="docutils literal notranslate"><span class="pre">maxReceiveCount</span></code>, you must specify it as an integer (<code class="docutils literal notranslate"><span class="pre">5</span></code>), and not a string (<code class="docutils literal notranslate"><span class="pre">&quot;5&quot;</span></code>).</p>
</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of tags to assign to the queue.</p></li>
<li><p><strong>visibility_timeout_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>The visibility timeout for the queue. An integer from 0 to 43200 (12 hours). The default for this attribute is 30. For more information about visibility timeout, see <a class="reference external" href="https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/AboutVT.html">AWS docs</a>.</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.sqs.Queue.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sqs.Queue.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sqs.Queue.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sqs.Queue.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_aws.sqs.QueuePolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_aws.sqs.</code><code class="sig-name descname">QueuePolicy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">queue_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sqs.QueuePolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows you to set a policy of an SQS Queue
while referencing ARN of the queue within the policy.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">queue</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">sqs</span><span class="o">.</span><span class="n">Queue</span><span class="p">(</span><span class="s2">&quot;queue&quot;</span><span class="p">)</span>
<span class="n">test</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">sqs</span><span class="o">.</span><span class="n">QueuePolicy</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">policy</span><span class="o">=</span><span class="n">queue</span><span class="o">.</span><span class="n">arn</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">arn</span><span class="p">:</span> <span class="sa">f</span><span class="s2">&quot;&quot;&quot;</span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">  &quot;Version&quot;: &quot;2012-10-17&quot;,</span>
<span class="s2">  &quot;Id&quot;: &quot;sqspolicy&quot;,</span>
<span class="s2">  &quot;Statement&quot;: [</span>
<span class="s2">    </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">      &quot;Sid&quot;: &quot;First&quot;,</span>
<span class="s2">      &quot;Effect&quot;: &quot;Allow&quot;,</span>
<span class="s2">      &quot;Principal&quot;: &quot;*&quot;,</span>
<span class="s2">      &quot;Action&quot;: &quot;sqs:SendMessage&quot;,</span>
<span class="s2">      &quot;Resource&quot;: &quot;</span><span class="si">{</span><span class="n">arn</span><span class="si">}</span><span class="s2">&quot;,</span>
<span class="s2">      &quot;Condition&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">        &quot;ArnEquals&quot;: </span><span class="se">&#x7B;&#x7B;</span><span class="s2"></span>
<span class="s2">          &quot;aws:SourceArn&quot;: &quot;</span><span class="si">{</span><span class="n">aws_sns_topic</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;arn&quot;</span><span class="p">]</span><span class="si">}</span><span class="s2">&quot;</span>
<span class="s2">        </span><span class="se">&#x7D;&#x7D;</span><span class="s2"></span>
<span class="s2">      </span><span class="se">&#x7D;&#x7D;</span><span class="s2"></span>
<span class="s2">    </span><span class="se">&#x7D;&#x7D;</span><span class="s2"></span>
<span class="s2">  ]</span>
<span class="se">&#x7D;&#x7D;</span><span class="s2"></span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">),</span>
    <span class="n">queue_url</span><span class="o">=</span><span class="n">queue</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The JSON policy for the SQS queue.</p></li>
<li><p><strong>queue_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the SQS Queue to which to attach the policy</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_aws.sqs.QueuePolicy.policy">
<code class="sig-name descname">policy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.QueuePolicy.policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The JSON policy for the SQS queue.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_aws.sqs.QueuePolicy.queue_url">
<code class="sig-name descname">queue_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_aws.sqs.QueuePolicy.queue_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the SQS Queue to which to attach the policy</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.sqs.QueuePolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">queue_url</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sqs.QueuePolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing QueuePolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The JSON policy for the SQS queue.</p></li>
<li><p><strong>queue_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the SQS Queue to which to attach the policy</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_aws.sqs.QueuePolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sqs.QueuePolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sqs.QueuePolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sqs.QueuePolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_aws.sqs.get_queue">
<code class="sig-prename descclassname">pulumi_aws.sqs.</code><code class="sig-name descname">get_queue</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_aws.sqs.get_queue" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the ARN and URL of queue in AWS Simple Queue Service (SQS).
By using this data source, you can reference SQS queues without having to hardcode
the ARNs as input.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">sqs</span><span class="o">.</span><span class="n">get_queue</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;queue&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the queue to match.</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – A map of tags for the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
