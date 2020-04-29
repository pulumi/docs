---
title: Package pulumi_cloudamqp
title_tag: Package pulumi_cloudamqp | Python SDK
linktitle: pulumi_cloudamqp
notitle: true
---

<div class="section" id="module-pulumi_cloudamqp">
<span id="pulumi-cloudamqp"></span><h1>Pulumi CloudAMQP<a class="headerlink" href="#module-pulumi_cloudamqp" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_cloudamqp.Alarm">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">Alarm</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">message_type=None</em>, <em class="sig-param">queue_regex=None</em>, <em class="sig-param">recipients=None</em>, <em class="sig-param">time_threshold=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">value_threshold=None</em>, <em class="sig-param">vhost_regex=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.Alarm" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Alarm resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] enabled: Enable or disable an alarm
:param pulumi.Input[float] instance_id: Instance identifier
:param pulumi.Input[str] message_type: Message types (total, unacked, ready) of the queue to trigger the alarm
:param pulumi.Input[str] queue_regex: Regex for which queues to check
:param pulumi.Input[list] recipients: Identifiers for recipients to be notified.
:param pulumi.Input[float] time_threshold: For how long (in seconds) the value_threshold should be active before trigger alarm
:param pulumi.Input[str] type: Type of the alarm, valid options are: cpu, memory, disk_usage, queue_length, connection_count, consumers_count,</p>
<blockquote>
<div><p>net_split</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>value_threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – What value to trigger the alarm for</p></li>
<li><p><strong>vhost_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Regex for which vhost the queues are in</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_cloudamqp.Alarm.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.Alarm.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable or disable an alarm</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.Alarm.instance_id">
<code class="sig-name descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.Alarm.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance identifier</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.Alarm.message_type">
<code class="sig-name descname">message_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.Alarm.message_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Message types (total, unacked, ready) of the queue to trigger the alarm</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.Alarm.queue_regex">
<code class="sig-name descname">queue_regex</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.Alarm.queue_regex" title="Permalink to this definition">¶</a></dt>
<dd><p>Regex for which queues to check</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.Alarm.recipients">
<code class="sig-name descname">recipients</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.Alarm.recipients" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifiers for recipients to be notified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.Alarm.time_threshold">
<code class="sig-name descname">time_threshold</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.Alarm.time_threshold" title="Permalink to this definition">¶</a></dt>
<dd><p>For how long (in seconds) the value_threshold should be active before trigger alarm</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.Alarm.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.Alarm.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of the alarm, valid options are: cpu, memory, disk_usage, queue_length, connection_count, consumers_count,
net_split</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.Alarm.value_threshold">
<code class="sig-name descname">value_threshold</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.Alarm.value_threshold" title="Permalink to this definition">¶</a></dt>
<dd><p>What value to trigger the alarm for</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.Alarm.vhost_regex">
<code class="sig-name descname">vhost_regex</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.Alarm.vhost_regex" title="Permalink to this definition">¶</a></dt>
<dd><p>Regex for which vhost the queues are in</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudamqp.Alarm.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">message_type=None</em>, <em class="sig-param">queue_regex=None</em>, <em class="sig-param">recipients=None</em>, <em class="sig-param">time_threshold=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">value_threshold=None</em>, <em class="sig-param">vhost_regex=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.Alarm.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Alarm resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable or disable an alarm</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Instance identifier</p></li>
<li><p><strong>message_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Message types (total, unacked, ready) of the queue to trigger the alarm</p></li>
<li><p><strong>queue_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Regex for which queues to check</p></li>
<li><p><strong>recipients</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Identifiers for recipients to be notified.</p></li>
<li><p><strong>time_threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – For how long (in seconds) the value_threshold should be active before trigger alarm</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the alarm, valid options are: cpu, memory, disk_usage, queue_length, connection_count, consumers_count,
net_split</p></li>
<li><p><strong>value_threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – What value to trigger the alarm for</p></li>
<li><p><strong>vhost_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Regex for which vhost the queues are in</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudamqp.Alarm.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.Alarm.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.Alarm.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.Alarm.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.AwaitableGetAlarmResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">AwaitableGetAlarmResult</code><span class="sig-paren">(</span><em class="sig-param">alarm_id=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">message_type=None</em>, <em class="sig-param">queue_regex=None</em>, <em class="sig-param">recipients=None</em>, <em class="sig-param">time_threshold=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">value_threshold=None</em>, <em class="sig-param">vhost_regex=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.AwaitableGetAlarmResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_cloudamqp.AwaitableGetCredentialsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">AwaitableGetCredentialsResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">username=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.AwaitableGetCredentialsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_cloudamqp.AwaitableGetInstanceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">AwaitableGetInstanceResult</code><span class="sig-paren">(</span><em class="sig-param">apikey=None</em>, <em class="sig-param">host=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">nodes=None</em>, <em class="sig-param">plan=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">rmq_version=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">url=None</em>, <em class="sig-param">vhost=None</em>, <em class="sig-param">vpc_subnet=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.AwaitableGetInstanceResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_cloudamqp.AwaitableGetNotificationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">AwaitableGetNotificationResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">recipient_id=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.AwaitableGetNotificationResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_cloudamqp.AwaitableGetPluginsCommunityResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">AwaitableGetPluginsCommunityResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">plugins=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.AwaitableGetPluginsCommunityResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_cloudamqp.AwaitableGetPluginsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">AwaitableGetPluginsResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">plugins=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.AwaitableGetPluginsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_cloudamqp.AwaitableGetVpcInfoResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">AwaitableGetVpcInfoResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">owner_id=None</em>, <em class="sig-param">security_group_id=None</em>, <em class="sig-param">vpc_subnet=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.AwaitableGetVpcInfoResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_cloudamqp.GetAlarmResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">GetAlarmResult</code><span class="sig-paren">(</span><em class="sig-param">alarm_id=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">message_type=None</em>, <em class="sig-param">queue_regex=None</em>, <em class="sig-param">recipients=None</em>, <em class="sig-param">time_threshold=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">value_threshold=None</em>, <em class="sig-param">vhost_regex=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.GetAlarmResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAlarm.</p>
<dl class="attribute">
<dt id="pulumi_cloudamqp.GetAlarmResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.GetAlarmResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_cloudamqp.GetCredentialsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">GetCredentialsResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">username=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.GetCredentialsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCredentials.</p>
<dl class="attribute">
<dt id="pulumi_cloudamqp.GetCredentialsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.GetCredentialsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_cloudamqp.GetInstanceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">GetInstanceResult</code><span class="sig-paren">(</span><em class="sig-param">apikey=None</em>, <em class="sig-param">host=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">nodes=None</em>, <em class="sig-param">plan=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">rmq_version=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">url=None</em>, <em class="sig-param">vhost=None</em>, <em class="sig-param">vpc_subnet=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.GetInstanceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getInstance.</p>
<dl class="attribute">
<dt id="pulumi_cloudamqp.GetInstanceResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.GetInstanceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_cloudamqp.GetNotificationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">GetNotificationResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">recipient_id=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.GetNotificationResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNotification.</p>
<dl class="attribute">
<dt id="pulumi_cloudamqp.GetNotificationResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.GetNotificationResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_cloudamqp.GetPluginsCommunityResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">GetPluginsCommunityResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">plugins=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.GetPluginsCommunityResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPluginsCommunity.</p>
<dl class="attribute">
<dt id="pulumi_cloudamqp.GetPluginsCommunityResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.GetPluginsCommunityResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_cloudamqp.GetPluginsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">GetPluginsResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">plugins=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.GetPluginsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPlugins.</p>
<dl class="attribute">
<dt id="pulumi_cloudamqp.GetPluginsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.GetPluginsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_cloudamqp.GetVpcInfoResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">GetVpcInfoResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">owner_id=None</em>, <em class="sig-param">security_group_id=None</em>, <em class="sig-param">vpc_subnet=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.GetVpcInfoResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVpcInfo.</p>
<dl class="attribute">
<dt id="pulumi_cloudamqp.GetVpcInfoResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.GetVpcInfoResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_cloudamqp.Instance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">Instance</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">nodes=None</em>, <em class="sig-param">plan=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">rmq_version=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vpc_subnet=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Instance resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] name: Name of the instance
:param pulumi.Input[float] nodes: Number of nodes in cluster (plan must support it)
:param pulumi.Input[str] plan: Name of the plan, valid options are: lemur, tiger, bunny, rabbit, panda, ape, hippo, lion
:param pulumi.Input[str] region: Name of the region you want to create your instance in
:param pulumi.Input[str] rmq_version: RabbitMQ version
:param pulumi.Input[list] tags: Tag the instances with optional tags
:param pulumi.Input[str] vpc_subnet: Dedicated VPC subnet, shouldn’t overlap with your current VPC’s subnet</p>
<dl class="attribute">
<dt id="pulumi_cloudamqp.Instance.apikey">
<code class="sig-name descname">apikey</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.Instance.apikey" title="Permalink to this definition">¶</a></dt>
<dd><p>API key for the CloudAMQP instance</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.Instance.host">
<code class="sig-name descname">host</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.Instance.host" title="Permalink to this definition">¶</a></dt>
<dd><p>Host name for the CloudAMQP instance</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.Instance.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.Instance.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the instance</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.Instance.nodes">
<code class="sig-name descname">nodes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.Instance.nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of nodes in cluster (plan must support it)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.Instance.plan">
<code class="sig-name descname">plan</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.Instance.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the plan, valid options are: lemur, tiger, bunny, rabbit, panda, ape, hippo, lion</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.Instance.ready">
<code class="sig-name descname">ready</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.Instance.ready" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag describing if the resource is ready</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.Instance.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.Instance.region" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the region you want to create your instance in</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.Instance.rmq_version">
<code class="sig-name descname">rmq_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.Instance.rmq_version" title="Permalink to this definition">¶</a></dt>
<dd><p>RabbitMQ version</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.Instance.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.Instance.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Tag the instances with optional tags</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.Instance.url">
<code class="sig-name descname">url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.Instance.url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL of the CloudAMQP instance</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.Instance.vhost">
<code class="sig-name descname">vhost</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.Instance.vhost" title="Permalink to this definition">¶</a></dt>
<dd><p>The virtual host</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.Instance.vpc_subnet">
<code class="sig-name descname">vpc_subnet</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.Instance.vpc_subnet" title="Permalink to this definition">¶</a></dt>
<dd><p>Dedicated VPC subnet, shouldn’t overlap with your current VPC’s subnet</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudamqp.Instance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">apikey=None</em>, <em class="sig-param">host=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">nodes=None</em>, <em class="sig-param">plan=None</em>, <em class="sig-param">ready=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">rmq_version=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">url=None</em>, <em class="sig-param">vhost=None</em>, <em class="sig-param">vpc_subnet=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.Instance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Instance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>apikey</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – API key for the CloudAMQP instance</p></li>
<li><p><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Host name for the CloudAMQP instance</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the instance</p></li>
<li><p><strong>nodes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of nodes in cluster (plan must support it)</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the plan, valid options are: lemur, tiger, bunny, rabbit, panda, ape, hippo, lion</p></li>
<li><p><strong>ready</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag describing if the resource is ready</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the region you want to create your instance in</p></li>
<li><p><strong>rmq_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – RabbitMQ version</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Tag the instances with optional tags</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL of the CloudAMQP instance</p></li>
<li><p><strong>vhost</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The virtual host</p></li>
<li><p><strong>vpc_subnet</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Dedicated VPC subnet, shouldn’t overlap with your current VPC’s subnet</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudamqp.Instance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.Instance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.Instance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.Instance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.IntegrationLog">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">IntegrationLog</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access_key_id=None</em>, <em class="sig-param">host_port=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">secret_access_key=None</em>, <em class="sig-param">token=None</em>, <em class="sig-param">url=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.IntegrationLog" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a IntegrationLog resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] access_key_id: AWS access key identifier. (Cloudwatch)
:param pulumi.Input[str] host_port: Destination to send the logs. (Splunk)
:param pulumi.Input[float] instance_id: Instance identifier used to make proxy calls
:param pulumi.Input[str] name: The name of log integration
:param pulumi.Input[str] region: The region hosting integration service. (Cloudwatch)
:param pulumi.Input[str] secret_access_key: AWS secret access key. (Cloudwatch)
:param pulumi.Input[str] token: The token used for authentication. (Loggly, Logentries, Splunk)
:param pulumi.Input[str] url: The URL to push the logs to. (Papertrail)</p>
<dl class="attribute">
<dt id="pulumi_cloudamqp.IntegrationLog.access_key_id">
<code class="sig-name descname">access_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.IntegrationLog.access_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS access key identifier. (Cloudwatch)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.IntegrationLog.host_port">
<code class="sig-name descname">host_port</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.IntegrationLog.host_port" title="Permalink to this definition">¶</a></dt>
<dd><p>Destination to send the logs. (Splunk)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.IntegrationLog.instance_id">
<code class="sig-name descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.IntegrationLog.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance identifier used to make proxy calls</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.IntegrationLog.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.IntegrationLog.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of log integration</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.IntegrationLog.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.IntegrationLog.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region hosting integration service. (Cloudwatch)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.IntegrationLog.secret_access_key">
<code class="sig-name descname">secret_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.IntegrationLog.secret_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS secret access key. (Cloudwatch)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.IntegrationLog.token">
<code class="sig-name descname">token</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.IntegrationLog.token" title="Permalink to this definition">¶</a></dt>
<dd><p>The token used for authentication. (Loggly, Logentries, Splunk)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.IntegrationLog.url">
<code class="sig-name descname">url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.IntegrationLog.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL to push the logs to. (Papertrail)</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudamqp.IntegrationLog.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access_key_id=None</em>, <em class="sig-param">host_port=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">secret_access_key=None</em>, <em class="sig-param">token=None</em>, <em class="sig-param">url=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.IntegrationLog.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IntegrationLog resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS access key identifier. (Cloudwatch)</p></li>
<li><p><strong>host_port</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Destination to send the logs. (Splunk)</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Instance identifier used to make proxy calls</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of log integration</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region hosting integration service. (Cloudwatch)</p></li>
<li><p><strong>secret_access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS secret access key. (Cloudwatch)</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The token used for authentication. (Loggly, Logentries, Splunk)</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL to push the logs to. (Papertrail)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudamqp.IntegrationLog.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.IntegrationLog.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.IntegrationLog.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.IntegrationLog.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.IntegrationMetric">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">IntegrationMetric</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access_key_id=None</em>, <em class="sig-param">api_key=None</em>, <em class="sig-param">email=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">license_key=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">queue_whitelist=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">secret_access_key=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vhost_whitelist=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.IntegrationMetric" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a IntegrationMetric resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] access_key_id: AWS access key identifier. (Cloudwatch)
:param pulumi.Input[str] api_key: The API key for the integration service. (Librato)
:param pulumi.Input[str] email: The email address registred for the integration service. (Librato)
:param pulumi.Input[float] instance_id: Instance identifier
:param pulumi.Input[str] license_key: The license key registred for the integration service. (New Relic)
:param pulumi.Input[str] name: The name of metrics integration
:param pulumi.Input[str] queue_whitelist: (optional) whitelist using regular expression
:param pulumi.Input[str] region: AWS region for Cloudwatch and [US/EU] for Data dog/New relic. (Cloudwatch, Data Dog, New Relic)
:param pulumi.Input[str] secret_access_key: AWS secret key. (Cloudwatch)
:param pulumi.Input[str] tags: (optional) tags. E.g. env=prod,region=europe
:param pulumi.Input[str] vhost_whitelist: (optional) whitelist using regular expression</p>
<dl class="attribute">
<dt id="pulumi_cloudamqp.IntegrationMetric.access_key_id">
<code class="sig-name descname">access_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.IntegrationMetric.access_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS access key identifier. (Cloudwatch)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.IntegrationMetric.api_key">
<code class="sig-name descname">api_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.IntegrationMetric.api_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The API key for the integration service. (Librato)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.IntegrationMetric.email">
<code class="sig-name descname">email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.IntegrationMetric.email" title="Permalink to this definition">¶</a></dt>
<dd><p>The email address registred for the integration service. (Librato)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.IntegrationMetric.instance_id">
<code class="sig-name descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.IntegrationMetric.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance identifier</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.IntegrationMetric.license_key">
<code class="sig-name descname">license_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.IntegrationMetric.license_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The license key registred for the integration service. (New Relic)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.IntegrationMetric.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.IntegrationMetric.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of metrics integration</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.IntegrationMetric.queue_whitelist">
<code class="sig-name descname">queue_whitelist</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.IntegrationMetric.queue_whitelist" title="Permalink to this definition">¶</a></dt>
<dd><p>(optional) whitelist using regular expression</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.IntegrationMetric.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.IntegrationMetric.region" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS region for Cloudwatch and [US/EU] for Data dog/New relic. (Cloudwatch, Data Dog, New Relic)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.IntegrationMetric.secret_access_key">
<code class="sig-name descname">secret_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.IntegrationMetric.secret_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS secret key. (Cloudwatch)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.IntegrationMetric.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.IntegrationMetric.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>(optional) tags. E.g. env=prod,region=europe</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.IntegrationMetric.vhost_whitelist">
<code class="sig-name descname">vhost_whitelist</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.IntegrationMetric.vhost_whitelist" title="Permalink to this definition">¶</a></dt>
<dd><p>(optional) whitelist using regular expression</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudamqp.IntegrationMetric.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">access_key_id=None</em>, <em class="sig-param">api_key=None</em>, <em class="sig-param">email=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">license_key=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">queue_whitelist=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">secret_access_key=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vhost_whitelist=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.IntegrationMetric.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IntegrationMetric resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS access key identifier. (Cloudwatch)</p></li>
<li><p><strong>api_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API key for the integration service. (Librato)</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address registred for the integration service. (Librato)</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Instance identifier</p></li>
<li><p><strong>license_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The license key registred for the integration service. (New Relic)</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of metrics integration</p></li>
<li><p><strong>queue_whitelist</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (optional) whitelist using regular expression</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS region for Cloudwatch and [US/EU] for Data dog/New relic. (Cloudwatch, Data Dog, New Relic)</p></li>
<li><p><strong>secret_access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS secret key. (Cloudwatch)</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (optional) tags. E.g. env=prod,region=europe</p></li>
<li><p><strong>vhost_whitelist</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (optional) whitelist using regular expression</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudamqp.IntegrationMetric.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.IntegrationMetric.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.IntegrationMetric.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.IntegrationMetric.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.Notification">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">Notification</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">value=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.Notification" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Notification resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[float] instance_id: Instance identifier
:param pulumi.Input[str] name: Optional display name of the recipient
:param pulumi.Input[str] type: Type of the notification, valid options are: email, webhook, pagerduty, victorops, opsgenie, opsgenie-eu, slack
:param pulumi.Input[str] value: Notification endpoint, where to send the notifcation</p>
<dl class="attribute">
<dt id="pulumi_cloudamqp.Notification.instance_id">
<code class="sig-name descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.Notification.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance identifier</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.Notification.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.Notification.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Optional display name of the recipient</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.Notification.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.Notification.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of the notification, valid options are: email, webhook, pagerduty, victorops, opsgenie, opsgenie-eu, slack</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.Notification.value">
<code class="sig-name descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.Notification.value" title="Permalink to this definition">¶</a></dt>
<dd><p>Notification endpoint, where to send the notifcation</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudamqp.Notification.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.Notification.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Notification resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Instance identifier</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Optional display name of the recipient</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the notification, valid options are: email, webhook, pagerduty, victorops, opsgenie, opsgenie-eu, slack</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Notification endpoint, where to send the notifcation</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudamqp.Notification.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.Notification.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.Notification.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.Notification.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.Plugin">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">Plugin</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.Plugin" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Plugin resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] enabled: If the plugin is enabled
:param pulumi.Input[float] instance_id: Instance identifier
:param pulumi.Input[str] name: The name of the plugin</p>
<dl class="attribute">
<dt id="pulumi_cloudamqp.Plugin.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.Plugin.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>If the plugin is enabled</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.Plugin.instance_id">
<code class="sig-name descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.Plugin.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance identifier</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.Plugin.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.Plugin.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the plugin</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudamqp.Plugin.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.Plugin.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Plugin resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If the plugin is enabled</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Instance identifier</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the plugin</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudamqp.Plugin.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.Plugin.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.Plugin.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.Plugin.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.PluginCommunity">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">PluginCommunity</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.PluginCommunity" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a PluginCommunity resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] enabled: If the plugin is enabled
:param pulumi.Input[float] instance_id: Instance identifier
:param pulumi.Input[str] name: The name of the plugin</p>
<dl class="attribute">
<dt id="pulumi_cloudamqp.PluginCommunity.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.PluginCommunity.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>If the plugin is enabled</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.PluginCommunity.instance_id">
<code class="sig-name descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.PluginCommunity.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance identifier</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.PluginCommunity.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.PluginCommunity.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the plugin</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudamqp.PluginCommunity.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.PluginCommunity.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PluginCommunity resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If the plugin is enabled</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Instance identifier</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the plugin</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudamqp.PluginCommunity.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.PluginCommunity.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.PluginCommunity.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.PluginCommunity.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">apikey=None</em>, <em class="sig-param">baseurl=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the cloudamqp package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>apikey</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Key used to authentication to the CloudAMQP Customer API</p></li>
<li><p><strong>baseurl</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Base URL to CloudAMQP Customer website</p></li>
</ul>
</dd>
</dl>
<dl class="method">
<dt id="pulumi_cloudamqp.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.SecurityFirewall">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">SecurityFirewall</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">rules=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.SecurityFirewall" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a SecurityFirewall resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[float] instance_id: Instance identifier</p>
<p>The <strong>rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ports</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">services</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_cloudamqp.SecurityFirewall.instance_id">
<code class="sig-name descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.SecurityFirewall.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance identifier</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudamqp.SecurityFirewall.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">rules=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.SecurityFirewall.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecurityFirewall resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Instance identifier</p></li>
</ul>
</dd>
</dl>
<p>The <strong>rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ip</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ports</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">services</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudamqp.SecurityFirewall.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.SecurityFirewall.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.SecurityFirewall.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.SecurityFirewall.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.VpcPeering">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">VpcPeering</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">peering_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.VpcPeering" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a VpcPeering resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[float] instance_id: Instance identifier
:param pulumi.Input[str] peering_id: VPC peering identifier</p>
<dl class="attribute">
<dt id="pulumi_cloudamqp.VpcPeering.instance_id">
<code class="sig-name descname">instance_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.VpcPeering.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance identifier</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.VpcPeering.peering_id">
<code class="sig-name descname">peering_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.VpcPeering.peering_id" title="Permalink to this definition">¶</a></dt>
<dd><p>VPC peering identifier</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_cloudamqp.VpcPeering.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_cloudamqp.VpcPeering.status" title="Permalink to this definition">¶</a></dt>
<dd><p>VPC peering status</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudamqp.VpcPeering.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">peering_id=None</em>, <em class="sig-param">status=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.VpcPeering.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VpcPeering resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Instance identifier</p></li>
<li><p><strong>peering_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – VPC peering identifier</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – VPC peering status</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_cloudamqp.VpcPeering.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.VpcPeering.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.VpcPeering.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.VpcPeering.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.get_alarm">
<code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">get_alarm</code><span class="sig-paren">(</span><em class="sig-param">alarm_id=None</em>, <em class="sig-param">instance_id=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.get_alarm" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_cloudamqp.get_credentials">
<code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">get_credentials</code><span class="sig-paren">(</span><em class="sig-param">instance_id=None</em>, <em class="sig-param">password=None</em>, <em class="sig-param">username=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.get_credentials" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_cloudamqp.get_instance">
<code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">get_instance</code><span class="sig-paren">(</span><em class="sig-param">instance_id=None</em>, <em class="sig-param">vpc_subnet=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.get_instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_cloudamqp.get_notification">
<code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">get_notification</code><span class="sig-paren">(</span><em class="sig-param">instance_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">recipient_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.get_notification" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_cloudamqp.get_plugins">
<code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">get_plugins</code><span class="sig-paren">(</span><em class="sig-param">instance_id=None</em>, <em class="sig-param">plugins=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.get_plugins" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<p>The <strong>plugins</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="function">
<dt id="pulumi_cloudamqp.get_plugins_community">
<code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">get_plugins_community</code><span class="sig-paren">(</span><em class="sig-param">instance_id=None</em>, <em class="sig-param">plugins=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.get_plugins_community" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<p>The <strong>plugins</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">require</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="function">
<dt id="pulumi_cloudamqp.get_vpc_info">
<code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">get_vpc_info</code><span class="sig-paren">(</span><em class="sig-param">instance_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.get_vpc_info" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

</div>
