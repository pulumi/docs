---
title: Module mns
title_tag: Module mns | Package pulumi_alicloud | Python SDK
linktitle: mns
notitle: true
---

<div class="section" id="mns">
<h1>mns<a class="headerlink" href="#mns" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.mns"></span><dl class="class">
<dt id="pulumi_alicloud.mns.AwaitableGetQueuesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.mns.</code><code class="sig-name descname">AwaitableGetQueuesResult</code><span class="sig-paren">(</span><em class="sig-param">name_prefix=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">queues=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.mns.AwaitableGetQueuesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.mns.AwaitableGetTopicSubscriptionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.mns.</code><code class="sig-name descname">AwaitableGetTopicSubscriptionsResult</code><span class="sig-paren">(</span><em class="sig-param">name_prefix=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">subscriptions=None</em>, <em class="sig-param">topic_name=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.mns.AwaitableGetTopicSubscriptionsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.mns.AwaitableGetTopicsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.mns.</code><code class="sig-name descname">AwaitableGetTopicsResult</code><span class="sig-paren">(</span><em class="sig-param">name_prefix=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">topics=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.mns.AwaitableGetTopicsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.mns.GetQueuesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.mns.</code><code class="sig-name descname">GetQueuesResult</code><span class="sig-paren">(</span><em class="sig-param">name_prefix=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">queues=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.mns.GetQueuesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getQueues.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.mns.GetQueuesResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mns.GetQueuesResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of queue names.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mns.GetQueuesResult.queues">
<code class="sig-name descname">queues</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mns.GetQueuesResult.queues" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of queues. Each element contains the following attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mns.GetQueuesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mns.GetQueuesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.mns.GetTopicSubscriptionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.mns.</code><code class="sig-name descname">GetTopicSubscriptionsResult</code><span class="sig-paren">(</span><em class="sig-param">name_prefix=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">subscriptions=None</em>, <em class="sig-param">topic_name=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.mns.GetTopicSubscriptionsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getTopicSubscriptions.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.mns.GetTopicSubscriptionsResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mns.GetTopicSubscriptionsResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of subscription names.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mns.GetTopicSubscriptionsResult.subscriptions">
<code class="sig-name descname">subscriptions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mns.GetTopicSubscriptionsResult.subscriptions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of subscriptions. Each element contains the following attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mns.GetTopicSubscriptionsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mns.GetTopicSubscriptionsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.mns.GetTopicsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.mns.</code><code class="sig-name descname">GetTopicsResult</code><span class="sig-paren">(</span><em class="sig-param">name_prefix=None</em>, <em class="sig-param">names=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">topics=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.mns.GetTopicsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getTopics.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.mns.GetTopicsResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mns.GetTopicsResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of topic names.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mns.GetTopicsResult.topics">
<code class="sig-name descname">topics</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mns.GetTopicsResult.topics" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of topics. Each element contains the following attributes:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mns.GetTopicsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mns.GetTopicsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_alicloud.mns.Queue">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.mns.</code><code class="sig-name descname">Queue</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">delay_seconds=None</em>, <em class="sig-param">maximum_message_size=None</em>, <em class="sig-param">message_retention_period=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">polling_wait_seconds=None</em>, <em class="sig-param">visibility_timeout=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.mns.Queue" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Queue resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>delay_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – This attribute defines the length of time, in seconds, after which every message sent to the queue is dequeued. Valid value range: 0-604800 seconds, i.e., 0 to 7 days. Default value to 0.</p></li>
<li><p><strong>maximum_message_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – This indicates the maximum length, in bytes, of any message body sent to the queue. Valid value range: 1024-65536, i.e., 1K to 64K. Default value to 65536.</p></li>
<li><p><strong>message_retention_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Messages are deleted from the queue after a specified length of time, whether they have been activated or not. This attribute defines the viability period, in seconds, for every message in the queue. Valid value range: 60-604800 seconds, i.e., 1 minutes to 7 days. Default value to 345600.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Two queues on a single account in the same region cannot have the same name. A queue name must start with an English letter or a digit, and can contain English letters, digits, and hyphens, with the length not exceeding 256 characters .</p></li>
<li><p><strong>polling_wait_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Long polling is measured in seconds. When this attribute is set to 0, long polling is disabled. When it is not set to 0, long polling is enabled and message dequeue requests will be processed only when valid messages are received or when long polling times out. Valid value range: 0-30 seconds. Default value to 0.</p></li>
<li><p><strong>visibility_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The VisibilityTimeout attribute of the queue. A dequeued messages will change from active (visible) status to inactive (invisible) status, and this attribute defines the length of time, in seconds, that messages remain invisible. Messages return to active status after the set period. Valid value range: 1-43200 seconds, i.e., 1 seconds to 12 hours. Default value to 30.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/mns_queue.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/mns_queue.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_alicloud.mns.Queue.delay_seconds">
<code class="sig-name descname">delay_seconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mns.Queue.delay_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>This attribute defines the length of time, in seconds, after which every message sent to the queue is dequeued. Valid value range: 0-604800 seconds, i.e., 0 to 7 days. Default value to 0.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mns.Queue.maximum_message_size">
<code class="sig-name descname">maximum_message_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mns.Queue.maximum_message_size" title="Permalink to this definition">¶</a></dt>
<dd><p>This indicates the maximum length, in bytes, of any message body sent to the queue. Valid value range: 1024-65536, i.e., 1K to 64K. Default value to 65536.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mns.Queue.message_retention_period">
<code class="sig-name descname">message_retention_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mns.Queue.message_retention_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Messages are deleted from the queue after a specified length of time, whether they have been activated or not. This attribute defines the viability period, in seconds, for every message in the queue. Valid value range: 60-604800 seconds, i.e., 1 minutes to 7 days. Default value to 345600.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mns.Queue.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mns.Queue.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Two queues on a single account in the same region cannot have the same name. A queue name must start with an English letter or a digit, and can contain English letters, digits, and hyphens, with the length not exceeding 256 characters .</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mns.Queue.polling_wait_seconds">
<code class="sig-name descname">polling_wait_seconds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mns.Queue.polling_wait_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>Long polling is measured in seconds. When this attribute is set to 0, long polling is disabled. When it is not set to 0, long polling is enabled and message dequeue requests will be processed only when valid messages are received or when long polling times out. Valid value range: 0-30 seconds. Default value to 0.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mns.Queue.visibility_timeout">
<code class="sig-name descname">visibility_timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mns.Queue.visibility_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The VisibilityTimeout attribute of the queue. A dequeued messages will change from active (visible) status to inactive (invisible) status, and this attribute defines the length of time, in seconds, that messages remain invisible. Messages return to active status after the set period. Valid value range: 1-43200 seconds, i.e., 1 seconds to 12 hours. Default value to 30.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.mns.Queue.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">delay_seconds=None</em>, <em class="sig-param">maximum_message_size=None</em>, <em class="sig-param">message_retention_period=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">polling_wait_seconds=None</em>, <em class="sig-param">visibility_timeout=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.mns.Queue.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Queue resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>delay_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – This attribute defines the length of time, in seconds, after which every message sent to the queue is dequeued. Valid value range: 0-604800 seconds, i.e., 0 to 7 days. Default value to 0.</p></li>
<li><p><strong>maximum_message_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – This indicates the maximum length, in bytes, of any message body sent to the queue. Valid value range: 1024-65536, i.e., 1K to 64K. Default value to 65536.</p></li>
<li><p><strong>message_retention_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Messages are deleted from the queue after a specified length of time, whether they have been activated or not. This attribute defines the viability period, in seconds, for every message in the queue. Valid value range: 60-604800 seconds, i.e., 1 minutes to 7 days. Default value to 345600.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Two queues on a single account in the same region cannot have the same name. A queue name must start with an English letter or a digit, and can contain English letters, digits, and hyphens, with the length not exceeding 256 characters .</p></li>
<li><p><strong>polling_wait_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Long polling is measured in seconds. When this attribute is set to 0, long polling is disabled. When it is not set to 0, long polling is enabled and message dequeue requests will be processed only when valid messages are received or when long polling times out. Valid value range: 0-30 seconds. Default value to 0.</p></li>
<li><p><strong>visibility_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The VisibilityTimeout attribute of the queue. A dequeued messages will change from active (visible) status to inactive (invisible) status, and this attribute defines the length of time, in seconds, that messages remain invisible. Messages return to active status after the set period. Valid value range: 1-43200 seconds, i.e., 1 seconds to 12 hours. Default value to 30.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/mns_queue.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/mns_queue.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.mns.Queue.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.mns.Queue.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.mns.Queue.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.mns.Queue.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.mns.Topic">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.mns.</code><code class="sig-name descname">Topic</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">logging_enabled=None</em>, <em class="sig-param">maximum_message_size=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.mns.Topic" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Topic resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>logging_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is logging enabled? true or false. Default value to false.</p></li>
<li><p><strong>maximum_message_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – This indicates the maximum length, in bytes, of any message body sent to the topic. Valid value range: 1024-65536, i.e., 1K to 64K. Default value to 65536.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Two topics on a single account in the same region cannot have the same name. A topic name must start with an English letter or a digit, and can contain English letters, digits, and hyphens, with the length not exceeding 256 characters.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/mns_topic.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/mns_topic.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_alicloud.mns.Topic.logging_enabled">
<code class="sig-name descname">logging_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mns.Topic.logging_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Is logging enabled? true or false. Default value to false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mns.Topic.maximum_message_size">
<code class="sig-name descname">maximum_message_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mns.Topic.maximum_message_size" title="Permalink to this definition">¶</a></dt>
<dd><p>This indicates the maximum length, in bytes, of any message body sent to the topic. Valid value range: 1024-65536, i.e., 1K to 64K. Default value to 65536.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mns.Topic.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mns.Topic.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Two topics on a single account in the same region cannot have the same name. A topic name must start with an English letter or a digit, and can contain English letters, digits, and hyphens, with the length not exceeding 256 characters.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.mns.Topic.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">logging_enabled=None</em>, <em class="sig-param">maximum_message_size=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.mns.Topic.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Topic resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>logging_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is logging enabled? true or false. Default value to false.</p></li>
<li><p><strong>maximum_message_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – This indicates the maximum length, in bytes, of any message body sent to the topic. Valid value range: 1024-65536, i.e., 1K to 64K. Default value to 65536.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Two topics on a single account in the same region cannot have the same name. A topic name must start with an English letter or a digit, and can contain English letters, digits, and hyphens, with the length not exceeding 256 characters.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/mns_topic.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/mns_topic.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.mns.Topic.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.mns.Topic.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.mns.Topic.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.mns.Topic.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.mns.TopicSubscription">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.mns.</code><code class="sig-name descname">TopicSubscription</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">endpoint=None</em>, <em class="sig-param">filter_tag=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">notify_content_format=None</em>, <em class="sig-param">notify_strategy=None</em>, <em class="sig-param">topic_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.mns.TopicSubscription" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a TopicSubscription resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint has three format. Available values format:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">HTTP</span> <span class="n">Format</span><span class="p">:</span> <span class="n">http</span><span class="p">:</span><span class="o">//</span><span class="n">xxx</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">xxx</span>
<span class="o">-</span> <span class="n">Queue</span> <span class="n">Format</span><span class="p">:</span> <span class="n">acs</span><span class="p">:</span><span class="n">mns</span><span class="p">:{</span><span class="n">REGION</span><span class="p">}:{</span><span class="n">AccountID</span><span class="p">}:</span><span class="n">queues</span><span class="o">/</span><span class="p">{</span><span class="n">QueueName</span><span class="p">}</span>
<span class="o">-</span> <span class="n">Email</span> <span class="n">Format</span><span class="p">:</span> <span class="n">mail</span><span class="p">:</span><span class="n">directmail</span><span class="p">:{</span><span class="n">MailAddress</span><span class="p">}</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>filter_tag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The length should be shorter than 16.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Two topics subscription on a single account in the same topic cannot have the same name. A topic subscription name must start with an English letter or a digit, and can contain English letters, digits, and hyphens, with the length not exceeding 256 characters.</p></li>
<li><p><strong>notify_content_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The NotifyContentFormat attribute of Subscription. This attribute specifies the content format of the messages pushed to users. The valid values: ‘SIMPLIFIED’, ‘XML’ and ‘JSON’. Default to ‘SIMPLIFIED’.</p></li>
<li><p><strong>notify_strategy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The NotifyStrategy attribute of Subscription. This attribute specifies the retry strategy when message sending fails. the attribute has two value EXPONENTIAL_DECAY_RETR or BACKOFF_RETRY. Default value to BACKOFF_RETRY .</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/mns_topic_subscription.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/mns_topic_subscription.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_alicloud.mns.TopicSubscription.endpoint">
<code class="sig-name descname">endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mns.TopicSubscription.endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The endpoint has three format. Available values format:</p>
<ul class="simple">
<li><p>HTTP Format: <a class="reference external" href="http://xxx.com/xxx">http://xxx.com/xxx</a></p></li>
<li><p>Queue Format: acs:mns:{REGION}:{AccountID}:queues/{QueueName}</p></li>
<li><p>Email Format: mail:directmail:{MailAddress}</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mns.TopicSubscription.filter_tag">
<code class="sig-name descname">filter_tag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mns.TopicSubscription.filter_tag" title="Permalink to this definition">¶</a></dt>
<dd><p>The length should be shorter than 16.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mns.TopicSubscription.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mns.TopicSubscription.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Two topics subscription on a single account in the same topic cannot have the same name. A topic subscription name must start with an English letter or a digit, and can contain English letters, digits, and hyphens, with the length not exceeding 256 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mns.TopicSubscription.notify_content_format">
<code class="sig-name descname">notify_content_format</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mns.TopicSubscription.notify_content_format" title="Permalink to this definition">¶</a></dt>
<dd><p>The NotifyContentFormat attribute of Subscription. This attribute specifies the content format of the messages pushed to users. The valid values: ‘SIMPLIFIED’, ‘XML’ and ‘JSON’. Default to ‘SIMPLIFIED’.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.mns.TopicSubscription.notify_strategy">
<code class="sig-name descname">notify_strategy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.mns.TopicSubscription.notify_strategy" title="Permalink to this definition">¶</a></dt>
<dd><p>The NotifyStrategy attribute of Subscription. This attribute specifies the retry strategy when message sending fails. the attribute has two value EXPONENTIAL_DECAY_RETR or BACKOFF_RETRY. Default value to BACKOFF_RETRY .</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.mns.TopicSubscription.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">endpoint=None</em>, <em class="sig-param">filter_tag=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">notify_content_format=None</em>, <em class="sig-param">notify_strategy=None</em>, <em class="sig-param">topic_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.mns.TopicSubscription.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TopicSubscription resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The endpoint has three format. Available values format:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">HTTP</span> <span class="n">Format</span><span class="p">:</span> <span class="n">http</span><span class="p">:</span><span class="o">//</span><span class="n">xxx</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">xxx</span>
<span class="o">-</span> <span class="n">Queue</span> <span class="n">Format</span><span class="p">:</span> <span class="n">acs</span><span class="p">:</span><span class="n">mns</span><span class="p">:{</span><span class="n">REGION</span><span class="p">}:{</span><span class="n">AccountID</span><span class="p">}:</span><span class="n">queues</span><span class="o">/</span><span class="p">{</span><span class="n">QueueName</span><span class="p">}</span>
<span class="o">-</span> <span class="n">Email</span> <span class="n">Format</span><span class="p">:</span> <span class="n">mail</span><span class="p">:</span><span class="n">directmail</span><span class="p">:{</span><span class="n">MailAddress</span><span class="p">}</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>filter_tag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The length should be shorter than 16.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Two topics subscription on a single account in the same topic cannot have the same name. A topic subscription name must start with an English letter or a digit, and can contain English letters, digits, and hyphens, with the length not exceeding 256 characters.</p></li>
<li><p><strong>notify_content_format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The NotifyContentFormat attribute of Subscription. This attribute specifies the content format of the messages pushed to users. The valid values: ‘SIMPLIFIED’, ‘XML’ and ‘JSON’. Default to ‘SIMPLIFIED’.</p></li>
<li><p><strong>notify_strategy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The NotifyStrategy attribute of Subscription. This attribute specifies the retry strategy when message sending fails. the attribute has two value EXPONENTIAL_DECAY_RETR or BACKOFF_RETRY. Default value to BACKOFF_RETRY .</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/mns_topic_subscription.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/mns_topic_subscription.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.mns.TopicSubscription.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.mns.TopicSubscription.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.mns.TopicSubscription.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.mns.TopicSubscription.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.mns.get_queues">
<code class="sig-prename descclassname">pulumi_alicloud.mns.</code><code class="sig-name descname">get_queues</code><span class="sig-paren">(</span><em class="sig-param">name_prefix=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.mns.get_queues" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list of MNS queues in an Alibaba Cloud account according to the specified parameters.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name_prefix</strong> (<em>str</em>) – A string to filter resulting queues by their name prefixs.</p>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/mns_queues.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/mns_queues.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_alicloud.mns.get_topic_subscriptions">
<code class="sig-prename descclassname">pulumi_alicloud.mns.</code><code class="sig-name descname">get_topic_subscriptions</code><span class="sig-paren">(</span><em class="sig-param">name_prefix=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">topic_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.mns.get_topic_subscriptions" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list of MNS topic subscriptions in an Alibaba Cloud account according to the specified parameters.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name_prefix</strong> (<em>str</em>) – A string to filter resulting subscriptions of the topic by their name prefixs.</p></li>
<li><p><strong>topic_name</strong> (<em>str</em>) – Two topics on a single account in the same region cannot have the same name. A topic name must start with an English letter or a digit, and can contain English letters, digits, and hyphens, with the length not exceeding 256 characters.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/mns_topic_subscriptions.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/mns_topic_subscriptions.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_alicloud.mns.get_topics">
<code class="sig-prename descclassname">pulumi_alicloud.mns.</code><code class="sig-name descname">get_topics</code><span class="sig-paren">(</span><em class="sig-param">name_prefix=None</em>, <em class="sig-param">output_file=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.mns.get_topics" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a list of MNS topics in an Alibaba Cloud account according to the specified parameters.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name_prefix</strong> (<em>str</em>) – A string to filter resulting topics by their name prefixs.</p>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/mns_topics.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/mns_topics.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
