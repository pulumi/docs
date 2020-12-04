---
title: Package pulumi_cloudamqp
title_tag: Package pulumi_cloudamqp | Python SDK
linktitle: pulumi_cloudamqp
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "cloudamqp" >}}

<div class="section" id="module-pulumi_cloudamqp">
<span id="pulumi-cloudamqp"></span><h1>Pulumi CloudAMQP<a class="headerlink" href="#module-pulumi_cloudamqp" title="Permalink to this headline">¶</a></h1>
<dl class="py class">
<dt id="pulumi_cloudamqp.Alarm">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">Alarm</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">queue_regex</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recipients</span><span class="p">:</span> <span class="n">Union[Sequence[Union[int, Awaitable[int], Output[T]]], Awaitable[Sequence[Union[int, Awaitable[int], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_threshold</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value_threshold</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vhost_regex</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.Alarm" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to create and manage alarms to trigger based on a set of conditions. Once triggerd a notification will be sent to the assigned recipients. When creating a new instance, there will also be a set of default alarms (cpu, memory and disk) created. All default alarms uses the default recipient for notifications.</p>
<p>By setting <code class="docutils literal notranslate"><span class="pre">no_default_alarms</span></code> to <em>true</em> in <code class="docutils literal notranslate"><span class="pre">Instance</span></code>. This will create the instance without default alarms and avoid the need to import them to get full control.</p>
<p>Available for all subscription plans, but <code class="docutils literal notranslate"><span class="pre">lemur</span></code>and <code class="docutils literal notranslate"><span class="pre">tiger</span></code>are limited to fewer alarm types. The limited types supported can be seen in the table below in Alarm Type Reference.</p>
<p>Valid options for notification type.</p>
<p>Required arguments for all alarms: <em>instance_id</em>, <em>type</em> and <em>enabled</em><span class="raw-html-m2r"><br></span>
Optional argument for all alarms: <em>tags</em>, <em>queue_regex</em>, <em>vhost_regex</em></p>
<p>This resource depends on CloudAMQP instance identifier, <code class="docutils literal notranslate"><span class="pre">cloudamqp_instance.instance.id</span></code>.</p>
<p><code class="docutils literal notranslate"><span class="pre">cloudamqp_alarm</span></code> can be imported using CloudAMQP internal identifier of the alarm together (CSV separated) with the instance identifier. To retrieve the alarm identifier, use <a class="reference external" href="https://docs.cloudamqp.com/cloudamqp_api.html#list-alarms">CloudAMQP API</a></p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import cloudamqp:index/alarm:Alarm alarm &lt;alarm_id&gt;,&lt;instance_id&gt;<span class="sb">`</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable or disable the alarm to trigger.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The CloudAMQP instance ID.</p></li>
<li><p><strong>message_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Message type <code class="docutils literal notranslate"><span class="pre">(total,</span> <span class="pre">unacked,</span> <span class="pre">ready)</span></code> used by queue alarm type.</p></li>
<li><p><strong>queue_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Regex for which queue to check.</p></li>
<li><p><strong>recipients</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>int</em><em>]</em><em>]</em><em>]</em>) – Identifier for recipient to be notified. Leave empty to notify all recipients.</p></li>
<li><p><strong>time_threshold</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The time interval (in seconds) the <code class="docutils literal notranslate"><span class="pre">value_threshold</span></code> should be active before triggering an alarm.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The alarm type, see valid options below.</p></li>
<li><p><strong>value_threshold</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The value to trigger the alarm for.</p></li>
<li><p><strong>vhost_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Regex for which vhost to check</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudamqp.Alarm.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">queue_regex</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recipients</span><span class="p">:</span> <span class="n">Union[Sequence[Union[int, Awaitable[int], Output[T]]], Awaitable[Sequence[Union[int, Awaitable[int], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_threshold</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value_threshold</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vhost_regex</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudamqp.alarm.Alarm<a class="headerlink" href="#pulumi_cloudamqp.Alarm.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Alarm resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable or disable the alarm to trigger.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The CloudAMQP instance ID.</p></li>
<li><p><strong>message_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Message type <code class="docutils literal notranslate"><span class="pre">(total,</span> <span class="pre">unacked,</span> <span class="pre">ready)</span></code> used by queue alarm type.</p></li>
<li><p><strong>queue_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Regex for which queue to check.</p></li>
<li><p><strong>recipients</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>int</em><em>]</em><em>]</em><em>]</em>) – Identifier for recipient to be notified. Leave empty to notify all recipients.</p></li>
<li><p><strong>time_threshold</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The time interval (in seconds) the <code class="docutils literal notranslate"><span class="pre">value_threshold</span></code> should be active before triggering an alarm.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The alarm type, see valid options below.</p></li>
<li><p><strong>value_threshold</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The value to trigger the alarm for.</p></li>
<li><p><strong>vhost_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Regex for which vhost to check</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.Alarm.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_cloudamqp.Alarm.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable or disable the alarm to trigger.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.Alarm.instance_id">
<em class="property">property </em><code class="sig-name descname">instance_id</code><a class="headerlink" href="#pulumi_cloudamqp.Alarm.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The CloudAMQP instance ID.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.Alarm.message_type">
<em class="property">property </em><code class="sig-name descname">message_type</code><a class="headerlink" href="#pulumi_cloudamqp.Alarm.message_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Message type <code class="docutils literal notranslate"><span class="pre">(total,</span> <span class="pre">unacked,</span> <span class="pre">ready)</span></code> used by queue alarm type.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.Alarm.queue_regex">
<em class="property">property </em><code class="sig-name descname">queue_regex</code><a class="headerlink" href="#pulumi_cloudamqp.Alarm.queue_regex" title="Permalink to this definition">¶</a></dt>
<dd><p>Regex for which queue to check.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.Alarm.recipients">
<em class="property">property </em><code class="sig-name descname">recipients</code><a class="headerlink" href="#pulumi_cloudamqp.Alarm.recipients" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier for recipient to be notified. Leave empty to notify all recipients.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.Alarm.time_threshold">
<em class="property">property </em><code class="sig-name descname">time_threshold</code><a class="headerlink" href="#pulumi_cloudamqp.Alarm.time_threshold" title="Permalink to this definition">¶</a></dt>
<dd><p>The time interval (in seconds) the <code class="docutils literal notranslate"><span class="pre">value_threshold</span></code> should be active before triggering an alarm.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.Alarm.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_cloudamqp.Alarm.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The alarm type, see valid options below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.Alarm.value_threshold">
<em class="property">property </em><code class="sig-name descname">value_threshold</code><a class="headerlink" href="#pulumi_cloudamqp.Alarm.value_threshold" title="Permalink to this definition">¶</a></dt>
<dd><p>The value to trigger the alarm for.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.Alarm.vhost_regex">
<em class="property">property </em><code class="sig-name descname">vhost_regex</code><a class="headerlink" href="#pulumi_cloudamqp.Alarm.vhost_regex" title="Permalink to this definition">¶</a></dt>
<dd><p>Regex for which vhost to check</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.Alarm.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.Alarm.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.Alarm.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.Alarm.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.AwaitableGetAlarmResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">AwaitableGetAlarmResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">alarm_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">queue_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recipients</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_threshold</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value_threshold</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vhost_regex</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.AwaitableGetAlarmResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_cloudamqp.AwaitableGetCredentialsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">AwaitableGetCredentialsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.AwaitableGetCredentialsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_cloudamqp.AwaitableGetInstanceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">AwaitableGetInstanceResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">apikey</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dedicated</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rmq_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vhost</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_subnet</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.AwaitableGetInstanceResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_cloudamqp.AwaitableGetNodesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">AwaitableGetNodesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nodes</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.AwaitableGetNodesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_cloudamqp.AwaitableGetNotificationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">AwaitableGetNotificationResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recipient_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.AwaitableGetNotificationResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_cloudamqp.AwaitableGetPluginsCommunityResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">AwaitableGetPluginsCommunityResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plugins</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.AwaitableGetPluginsCommunityResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_cloudamqp.AwaitableGetPluginsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">AwaitableGetPluginsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plugins</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.AwaitableGetPluginsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_cloudamqp.AwaitableGetVpcInfoResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">AwaitableGetVpcInfoResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_subnet</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.AwaitableGetVpcInfoResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_cloudamqp.GetAlarmResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">GetAlarmResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">alarm_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">queue_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recipients</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_threshold</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value_threshold</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vhost_regex</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.GetAlarmResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAlarm.</p>
<dl class="py method">
<dt id="pulumi_cloudamqp.GetAlarmResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_cloudamqp.GetAlarmResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_cloudamqp.GetCredentialsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">GetCredentialsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.GetCredentialsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCredentials.</p>
<dl class="py method">
<dt id="pulumi_cloudamqp.GetCredentialsResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_cloudamqp.GetCredentialsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_cloudamqp.GetInstanceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">GetInstanceResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">apikey</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dedicated</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nodes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rmq_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vhost</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_subnet</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.GetInstanceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getInstance.</p>
<dl class="py method">
<dt id="pulumi_cloudamqp.GetInstanceResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_cloudamqp.GetInstanceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_cloudamqp.GetNodesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">GetNodesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nodes</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.GetNodesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNodes.</p>
<dl class="py method">
<dt id="pulumi_cloudamqp.GetNodesResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_cloudamqp.GetNodesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_cloudamqp.GetNotificationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">GetNotificationResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recipient_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.GetNotificationResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNotification.</p>
<dl class="py method">
<dt id="pulumi_cloudamqp.GetNotificationResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_cloudamqp.GetNotificationResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_cloudamqp.GetPluginsCommunityResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">GetPluginsCommunityResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plugins</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.GetPluginsCommunityResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPluginsCommunity.</p>
<dl class="py method">
<dt id="pulumi_cloudamqp.GetPluginsCommunityResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_cloudamqp.GetPluginsCommunityResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_cloudamqp.GetPluginsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">GetPluginsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plugins</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.GetPluginsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPlugins.</p>
<dl class="py method">
<dt id="pulumi_cloudamqp.GetPluginsResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_cloudamqp.GetPluginsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_cloudamqp.GetVpcInfoResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">GetVpcInfoResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_subnet</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.GetVpcInfoResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVpcInfo.</p>
<dl class="py method">
<dt id="pulumi_cloudamqp.GetVpcInfoResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_cloudamqp.GetVpcInfoResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_cloudamqp.Instance">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">Instance</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">no_default_alarms</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nodes</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rmq_version</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_subnet</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to create and manage a CloudAMQP instance running Rabbit MQ and deploy to multiple cloud platforms provider and over multiple regions, see Instance regions for more information.</p>
<p>Once the instance is created it will be assigned a unique identifier. All other resource and data sources created for this instance needs to reference the instance identifier.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudamqp</span> <span class="k">as</span> <span class="nn">cloudamqp</span>

<span class="c1"># Minimum free lemur instance</span>
<span class="n">lemur_instance</span> <span class="o">=</span> <span class="n">cloudamqp</span><span class="o">.</span><span class="n">Instance</span><span class="p">(</span><span class="s2">&quot;lemurInstance&quot;</span><span class="p">,</span>
    <span class="n">plan</span><span class="o">=</span><span class="s2">&quot;lemur&quot;</span><span class="p">,</span>
    <span class="n">region</span><span class="o">=</span><span class="s2">&quot;amazon-web-services::us-west-1&quot;</span><span class="p">)</span>
<span class="c1"># New dedicated bunny instance</span>
<span class="n">instance</span> <span class="o">=</span> <span class="n">cloudamqp</span><span class="o">.</span><span class="n">Instance</span><span class="p">(</span><span class="s2">&quot;instance&quot;</span><span class="p">,</span>
    <span class="n">no_default_alarms</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">nodes</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">plan</span><span class="o">=</span><span class="s2">&quot;bunny&quot;</span><span class="p">,</span>
    <span class="n">region</span><span class="o">=</span><span class="s2">&quot;amazon-web-services::us-west-1&quot;</span><span class="p">,</span>
    <span class="n">rmq_version</span><span class="o">=</span><span class="s2">&quot;3.8.3&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;terraform&quot;</span><span class="p">])</span>
</pre></div>
</div>
<p><code class="docutils literal notranslate"><span class="pre">cloudamqp_instance</span></code>can be imported using CloudAMQP internal identifier. To retrieve the identifier for an instance, use <a class="reference external" href="https://docs.cloudamqp.com/#list-instances">CloudAMQP customer API</a>.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import cloudamqp:index/instance:Instance instance &lt;instance_id&gt;<span class="sb">`</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the CloudAMQP instance.</p></li>
<li><p><strong>no_default_alarms</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to true to discard creating default alarms when the instance is created.</p></li>
<li><p><strong>nodes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Number of nodes, 1 to 3, in the CloudAMQP instance, default set to 1. The plan chosen must support the number of nodes.</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The subscription plan. See available plans</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region to host the instance in. See Instance regions</p></li>
<li><p><strong>rmq_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Rabbit MQ version. Default set to current loaded default value in CloudAMQP API.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – One or more tags for the CloudAMQP instance, makes it possible to categories multiple instances in console view. Default there is no tags assigned.</p></li>
<li><p><strong>vpc_subnet</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a dedicated VPC subnet, shouldn’t overlap with other VPC subnet, default subnet used 10.56.72.0/24. <strong>NOTE: extra fee will be charged when using VPC, see `CloudAMQP &lt;https://cloudamqp.com&gt;`_ for more information.</strong></p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudamqp.Instance.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">apikey</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dedicated</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">no_default_alarms</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nodes</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plan</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ready</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rmq_version</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vhost</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_subnet</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudamqp.instance.Instance<a class="headerlink" href="#pulumi_cloudamqp.Instance.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Instance resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>apikey</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>(Computed) API key needed to communicate to CloudAMQP’s second API. The second API is used to manage alarms, integration and more, full description <a class="reference external" href="https://docs.cloudamqp.com/cloudamqp_api.html">CloudAMQP API</a>.</p>
</p></li>
<li><p><strong>dedicated</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is the instance hosted on a dedicated server</p></li>
<li><p><strong>host</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The host name for the CloudAMQP instance.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the CloudAMQP instance.</p></li>
<li><p><strong>no_default_alarms</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to true to discard creating default alarms when the instance is created.</p></li>
<li><p><strong>nodes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Number of nodes, 1 to 3, in the CloudAMQP instance, default set to 1. The plan chosen must support the number of nodes.</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The subscription plan. See available plans</p></li>
<li><p><strong>ready</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag describing if the resource is ready</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region to host the instance in. See Instance regions</p></li>
<li><p><strong>rmq_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Rabbit MQ version. Default set to current loaded default value in CloudAMQP API.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – One or more tags for the CloudAMQP instance, makes it possible to categories multiple instances in console view. Default there is no tags assigned.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) AMQP server endpoint. <code class="docutils literal notranslate"><span class="pre">amqps://{username}:{password}&#64;{hostname}/{vhost}</span></code></p></li>
<li><p><strong>vhost</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The virtual host used by Rabbit MQ.</p></li>
<li><p><strong>vpc_subnet</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Creates a dedicated VPC subnet, shouldn’t overlap with other VPC subnet, default subnet used 10.56.72.0/24. <strong>NOTE: extra fee will be charged when using VPC, see `CloudAMQP &lt;https://cloudamqp.com&gt;`_ for more information.</strong></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.Instance.apikey">
<em class="property">property </em><code class="sig-name descname">apikey</code><a class="headerlink" href="#pulumi_cloudamqp.Instance.apikey" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) API key needed to communicate to CloudAMQP’s second API. The second API is used to manage alarms, integration and more, full description <a class="reference external" href="https://docs.cloudamqp.com/cloudamqp_api.html">CloudAMQP API</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.Instance.dedicated">
<em class="property">property </em><code class="sig-name descname">dedicated</code><a class="headerlink" href="#pulumi_cloudamqp.Instance.dedicated" title="Permalink to this definition">¶</a></dt>
<dd><p>Is the instance hosted on a dedicated server</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.Instance.host">
<em class="property">property </em><code class="sig-name descname">host</code><a class="headerlink" href="#pulumi_cloudamqp.Instance.host" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The host name for the CloudAMQP instance.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.Instance.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_cloudamqp.Instance.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the CloudAMQP instance.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.Instance.no_default_alarms">
<em class="property">property </em><code class="sig-name descname">no_default_alarms</code><a class="headerlink" href="#pulumi_cloudamqp.Instance.no_default_alarms" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to true to discard creating default alarms when the instance is created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.Instance.nodes">
<em class="property">property </em><code class="sig-name descname">nodes</code><a class="headerlink" href="#pulumi_cloudamqp.Instance.nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of nodes, 1 to 3, in the CloudAMQP instance, default set to 1. The plan chosen must support the number of nodes.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.Instance.plan">
<em class="property">property </em><code class="sig-name descname">plan</code><a class="headerlink" href="#pulumi_cloudamqp.Instance.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>The subscription plan. See available plans</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.Instance.ready">
<em class="property">property </em><code class="sig-name descname">ready</code><a class="headerlink" href="#pulumi_cloudamqp.Instance.ready" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag describing if the resource is ready</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.Instance.region">
<em class="property">property </em><code class="sig-name descname">region</code><a class="headerlink" href="#pulumi_cloudamqp.Instance.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region to host the instance in. See Instance regions</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.Instance.rmq_version">
<em class="property">property </em><code class="sig-name descname">rmq_version</code><a class="headerlink" href="#pulumi_cloudamqp.Instance.rmq_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The Rabbit MQ version. Default set to current loaded default value in CloudAMQP API.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.Instance.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_cloudamqp.Instance.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more tags for the CloudAMQP instance, makes it possible to categories multiple instances in console view. Default there is no tags assigned.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.Instance.url">
<em class="property">property </em><code class="sig-name descname">url</code><a class="headerlink" href="#pulumi_cloudamqp.Instance.url" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) AMQP server endpoint. <code class="docutils literal notranslate"><span class="pre">amqps://{username}:{password}&#64;{hostname}/{vhost}</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.Instance.vhost">
<em class="property">property </em><code class="sig-name descname">vhost</code><a class="headerlink" href="#pulumi_cloudamqp.Instance.vhost" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The virtual host used by Rabbit MQ.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.Instance.vpc_subnet">
<em class="property">property </em><code class="sig-name descname">vpc_subnet</code><a class="headerlink" href="#pulumi_cloudamqp.Instance.vpc_subnet" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a dedicated VPC subnet, shouldn’t overlap with other VPC subnet, default subnet used 10.56.72.0/24. <strong>NOTE: extra fee will be charged when using VPC, see `CloudAMQP &lt;https://cloudamqp.com&gt;`_ for more information.</strong></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.Instance.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.Instance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.Instance.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.Instance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.IntegrationLog">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">IntegrationLog</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_key_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_email</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host_port</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret_access_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.IntegrationLog" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to create and manage third party log integrations for a CloudAMQP instance. Once configured, the logs produced will be forward to corresponding integration.</p>
<p>Only available for dedicated subscription plans.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudamqp</span> <span class="k">as</span> <span class="nn">cloudamqp</span>

<span class="n">cloudwatch</span> <span class="o">=</span> <span class="n">cloudamqp</span><span class="o">.</span><span class="n">IntegrationLog</span><span class="p">(</span><span class="s2">&quot;cloudwatch&quot;</span><span class="p">,</span>
    <span class="n">instance_id</span><span class="o">=</span><span class="n">cloudamqp_instance</span><span class="p">[</span><span class="s2">&quot;instance&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">access_key_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;aws_access_key_id&quot;</span><span class="p">],</span>
    <span class="n">secret_access_key</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;aws_secret_access_key&quot;</span><span class="p">],</span>
    <span class="n">region</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;aws_region&quot;</span><span class="p">])</span>
<span class="n">logentries</span> <span class="o">=</span> <span class="n">cloudamqp</span><span class="o">.</span><span class="n">IntegrationLog</span><span class="p">(</span><span class="s2">&quot;logentries&quot;</span><span class="p">,</span>
    <span class="n">instance_id</span><span class="o">=</span><span class="n">cloudamqp_instance</span><span class="p">[</span><span class="s2">&quot;instance&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">token</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;logentries_token&quot;</span><span class="p">])</span>
<span class="n">loggly</span> <span class="o">=</span> <span class="n">cloudamqp</span><span class="o">.</span><span class="n">IntegrationLog</span><span class="p">(</span><span class="s2">&quot;loggly&quot;</span><span class="p">,</span>
    <span class="n">instance_id</span><span class="o">=</span><span class="n">cloudamqp_instance</span><span class="p">[</span><span class="s2">&quot;instance&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">token</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;loggly_token&quot;</span><span class="p">])</span>
<span class="n">papertrail</span> <span class="o">=</span> <span class="n">cloudamqp</span><span class="o">.</span><span class="n">IntegrationLog</span><span class="p">(</span><span class="s2">&quot;papertrail&quot;</span><span class="p">,</span>
    <span class="n">instance_id</span><span class="o">=</span><span class="n">cloudamqp_instance</span><span class="p">[</span><span class="s2">&quot;instance&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">url</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;papertrail_url&quot;</span><span class="p">])</span>
<span class="n">splunk</span> <span class="o">=</span> <span class="n">cloudamqp</span><span class="o">.</span><span class="n">IntegrationLog</span><span class="p">(</span><span class="s2">&quot;splunk&quot;</span><span class="p">,</span>
    <span class="n">instance_id</span><span class="o">=</span><span class="n">cloudamqp_instance</span><span class="p">[</span><span class="s2">&quot;instance&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">token</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;splunk_token&quot;</span><span class="p">],</span>
    <span class="n">host_port</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;splunk_host_port&quot;</span><span class="p">])</span>
<span class="n">datadog</span> <span class="o">=</span> <span class="n">cloudamqp</span><span class="o">.</span><span class="n">IntegrationLog</span><span class="p">(</span><span class="s2">&quot;datadog&quot;</span><span class="p">,</span>
    <span class="n">instance_id</span><span class="o">=</span><span class="n">cloudamqp_instance</span><span class="p">[</span><span class="s2">&quot;instance&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">region</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;datadog_region&quot;</span><span class="p">],</span>
    <span class="n">api_key</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;datadog_api_key&quot;</span><span class="p">],</span>
    <span class="n">tags</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;datadog_tags&quot;</span><span class="p">])</span>
<span class="n">stackdriver</span> <span class="o">=</span> <span class="n">cloudamqp</span><span class="o">.</span><span class="n">IntegrationLog</span><span class="p">(</span><span class="s2">&quot;stackdriver&quot;</span><span class="p">,</span>
    <span class="n">instance_id</span><span class="o">=</span><span class="n">cloudamqp_instance</span><span class="p">[</span><span class="s2">&quot;instance&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;stackdriver_project_id&quot;</span><span class="p">],</span>
    <span class="n">private_key</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;stackdriver_private_key&quot;</span><span class="p">],</span>
    <span class="n">client_email</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;stackdriver_client_email&quot;</span><span class="p">])</span>
</pre></div>
</div>
<p>Cloudwatch argument reference and example. Create an IAM user with programmatic access and the following permissions:</p>
<ul class="simple">
<li><p>CreateLogGroup</p></li>
<li><p>CreateLogStream</p></li>
<li><p>DescribeLogGroups</p></li>
<li><p>DescribeLogStreams</p></li>
<li><p>PutLogEvents</p></li>
</ul>
<p>Valid names for third party log integration.</p>
<table class="docutils align-default">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Name</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>cloudwatchlog</p></td>
<td><p>Create a IAM with programmatic access.</p></td>
</tr>
<tr class="row-odd"><td><p>logentries</p></td>
<td><p>Create a Logentries token at <a class="reference external" href="https://logentries.com/app#/add-log/manual">https://logentries.com/app#/add-log/manual</a></p></td>
</tr>
<tr class="row-even"><td><p>loggly</p></td>
<td><p>Create a Loggly token at <a class="reference external" href="https:/">https:/</a>/{your-company}.loggly.com/tokens</p></td>
</tr>
<tr class="row-odd"><td><p>papertrail</p></td>
<td><p>Create a Papertrail endpoint <a class="reference external" href="https://papertrailapp.com/systems/setup">https://papertrailapp.com/systems/setup</a></p></td>
</tr>
<tr class="row-even"><td><p>splunk</p></td>
<td><p>Create a HTTP Event Collector token at <a class="reference external" href="https://.cloud.splunk.com/en-US/manager/search/http-eventcollector">https://.cloud.splunk.com/en-US/manager/search/http-eventcollector</a></p></td>
</tr>
<tr class="row-odd"><td><p>datadog</p></td>
<td><p>Create a Datadog API key at app.datadoghq.com</p></td>
</tr>
<tr class="row-even"><td><p>stackdriver</p></td>
<td><p>Create a service account and add ‘monitor metrics writer’ role, then download credentials.</p></td>
</tr>
</tbody>
</table>
<p>Valid arguments for third party log integrations.</p>
<p>Required arguments for all integrations: name</p>
<table class="docutils align-default">
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Name</p></th>
<th class="head"><p>Type</p></th>
<th class="head"><p>Required arguments</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>CloudWatch</p></td>
<td><p>cloudwatchlog</p></td>
<td><p>access_key_id, secret_access_key, region</p></td>
</tr>
<tr class="row-odd"><td><p>Log Entries</p></td>
<td><p>logentries</p></td>
<td><p>token</p></td>
</tr>
<tr class="row-even"><td><p>Loggly</p></td>
<td><p>loggly</p></td>
<td><p>token</p></td>
</tr>
<tr class="row-odd"><td><p>Papertrail</p></td>
<td><p>papertrail</p></td>
<td><p>url</p></td>
</tr>
<tr class="row-even"><td><p>Splunk</p></td>
<td><p>splunk</p></td>
<td><p>token, host_port</p></td>
</tr>
<tr class="row-odd"><td><p>Data Dog</p></td>
<td><p>datadog</p></td>
<td><p>region, api_keys, tags</p></td>
</tr>
<tr class="row-even"><td><p>Stackdriver</p></td>
<td><p>stackdriver</p></td>
<td><p>project_id, private_key, client_email</p></td>
</tr>
</tbody>
</table>
<p>This resource depends on CloudAMQP instance identifier, <code class="docutils literal notranslate"><span class="pre">cloudamqp_instance.instance.id</span></code>.</p>
<p><code class="docutils literal notranslate"><span class="pre">cloudamqp_integration_log</span></code>can be imported using the name argument of the resource together with CloudAMQP instance identifier. The name and identifier are CSV separated, see example below.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import cloudamqp:index/integrationLog:IntegrationLog &lt;resource_name&gt; &lt;name&gt;,&lt;instance_id&gt;<span class="sb">`</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS access key identifier.</p></li>
<li><p><strong>api_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API key.</p></li>
<li><p><strong>client_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The client email registered for the integration service.</p></li>
<li><p><strong>host_port</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Destination to send the logs.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Instance identifier used to make proxy calls</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the third party log integration. See</p></li>
<li><p><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private access key.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project identifier.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Region hosting the integration service.</p></li>
<li><p><strong>secret_access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS secret access key.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Tag the integration, e.g. env=prod, region=europe.</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Token used for authentication.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Endpoint to log integration.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudamqp.IntegrationLog.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_key_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_email</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host_port</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret_access_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudamqp.integration_log.IntegrationLog<a class="headerlink" href="#pulumi_cloudamqp.IntegrationLog.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IntegrationLog resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS access key identifier.</p></li>
<li><p><strong>api_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API key.</p></li>
<li><p><strong>client_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The client email registered for the integration service.</p></li>
<li><p><strong>host_port</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Destination to send the logs.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Instance identifier used to make proxy calls</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the third party log integration. See</p></li>
<li><p><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private access key.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project identifier.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Region hosting the integration service.</p></li>
<li><p><strong>secret_access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS secret access key.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Tag the integration, e.g. env=prod, region=europe.</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Token used for authentication.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Endpoint to log integration.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.IntegrationLog.access_key_id">
<em class="property">property </em><code class="sig-name descname">access_key_id</code><a class="headerlink" href="#pulumi_cloudamqp.IntegrationLog.access_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS access key identifier.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.IntegrationLog.api_key">
<em class="property">property </em><code class="sig-name descname">api_key</code><a class="headerlink" href="#pulumi_cloudamqp.IntegrationLog.api_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The API key.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.IntegrationLog.client_email">
<em class="property">property </em><code class="sig-name descname">client_email</code><a class="headerlink" href="#pulumi_cloudamqp.IntegrationLog.client_email" title="Permalink to this definition">¶</a></dt>
<dd><p>The client email registered for the integration service.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.IntegrationLog.host_port">
<em class="property">property </em><code class="sig-name descname">host_port</code><a class="headerlink" href="#pulumi_cloudamqp.IntegrationLog.host_port" title="Permalink to this definition">¶</a></dt>
<dd><p>Destination to send the logs.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.IntegrationLog.instance_id">
<em class="property">property </em><code class="sig-name descname">instance_id</code><a class="headerlink" href="#pulumi_cloudamqp.IntegrationLog.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance identifier used to make proxy calls</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.IntegrationLog.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_cloudamqp.IntegrationLog.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the third party log integration. See</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.IntegrationLog.private_key">
<em class="property">property </em><code class="sig-name descname">private_key</code><a class="headerlink" href="#pulumi_cloudamqp.IntegrationLog.private_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The private access key.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.IntegrationLog.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_cloudamqp.IntegrationLog.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The project identifier.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.IntegrationLog.region">
<em class="property">property </em><code class="sig-name descname">region</code><a class="headerlink" href="#pulumi_cloudamqp.IntegrationLog.region" title="Permalink to this definition">¶</a></dt>
<dd><p>Region hosting the integration service.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.IntegrationLog.secret_access_key">
<em class="property">property </em><code class="sig-name descname">secret_access_key</code><a class="headerlink" href="#pulumi_cloudamqp.IntegrationLog.secret_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS secret access key.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.IntegrationLog.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_cloudamqp.IntegrationLog.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Tag the integration, e.g. env=prod, region=europe.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.IntegrationLog.token">
<em class="property">property </em><code class="sig-name descname">token</code><a class="headerlink" href="#pulumi_cloudamqp.IntegrationLog.token" title="Permalink to this definition">¶</a></dt>
<dd><p>Token used for authentication.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.IntegrationLog.url">
<em class="property">property </em><code class="sig-name descname">url</code><a class="headerlink" href="#pulumi_cloudamqp.IntegrationLog.url" title="Permalink to this definition">¶</a></dt>
<dd><p>Endpoint to log integration.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.IntegrationLog.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.IntegrationLog.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.IntegrationLog.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.IntegrationLog.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.IntegrationMetric">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">IntegrationMetric</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_key_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_email</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">license_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">queue_allowlist</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">queue_whitelist</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret_access_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vhost_allowlist</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vhost_whitelist</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.IntegrationMetric" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a IntegrationMetric resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] access_key_id: AWS access key identifier. (Cloudwatch)
:param pulumi.Input[str] api_key: The API key for the integration service. (Librato)
:param pulumi.Input[str] client_email: The client email. (Stackdriver)
:param pulumi.Input[str] email: The email address registred for the integration service. (Librato)
:param pulumi.Input[int] instance_id: Instance identifier
:param pulumi.Input[str] license_key: The license key registred for the integration service. (New Relic)
:param pulumi.Input[str] name: The name of metrics integration
:param pulumi.Input[str] private_key: The private key. (Stackdriver)
:param pulumi.Input[str] project_id: Project ID. (Stackdriver)
:param pulumi.Input[str] queue_allowlist: (optional) allowlist using regular expression
:param pulumi.Input[str] queue_whitelist: <strong>Deprecated</strong>
:param pulumi.Input[str] region: AWS region for Cloudwatch and [US/EU] for Data dog/New relic. (Cloudwatch, Data Dog, New Relic)
:param pulumi.Input[str] secret_access_key: AWS secret key. (Cloudwatch)
:param pulumi.Input[str] tags: (optional) tags. E.g. env=prod,region=europe
:param pulumi.Input[str] vhost_allowlist: (optional) allowlist using regular expression
:param pulumi.Input[str] vhost_whitelist: <strong>Deprecated</strong></p>
<dl class="py method">
<dt id="pulumi_cloudamqp.IntegrationMetric.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_key_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_email</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">license_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">queue_allowlist</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">queue_whitelist</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret_access_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vhost_allowlist</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vhost_whitelist</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudamqp.integration_metric.IntegrationMetric<a class="headerlink" href="#pulumi_cloudamqp.IntegrationMetric.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IntegrationMetric resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS access key identifier. (Cloudwatch)</p></li>
<li><p><strong>api_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API key for the integration service. (Librato)</p></li>
<li><p><strong>client_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The client email. (Stackdriver)</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email address registred for the integration service. (Librato)</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Instance identifier</p></li>
<li><p><strong>license_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The license key registred for the integration service. (New Relic)</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of metrics integration</p></li>
<li><p><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private key. (Stackdriver)</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project ID. (Stackdriver)</p></li>
<li><p><strong>queue_allowlist</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (optional) allowlist using regular expression</p></li>
<li><p><strong>queue_whitelist</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <strong>Deprecated</strong></p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS region for Cloudwatch and [US/EU] for Data dog/New relic. (Cloudwatch, Data Dog, New Relic)</p></li>
<li><p><strong>secret_access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS secret key. (Cloudwatch)</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (optional) tags. E.g. env=prod,region=europe</p></li>
<li><p><strong>vhost_allowlist</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (optional) allowlist using regular expression</p></li>
<li><p><strong>vhost_whitelist</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <strong>Deprecated</strong></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.IntegrationMetric.access_key_id">
<em class="property">property </em><code class="sig-name descname">access_key_id</code><a class="headerlink" href="#pulumi_cloudamqp.IntegrationMetric.access_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS access key identifier. (Cloudwatch)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.IntegrationMetric.api_key">
<em class="property">property </em><code class="sig-name descname">api_key</code><a class="headerlink" href="#pulumi_cloudamqp.IntegrationMetric.api_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The API key for the integration service. (Librato)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.IntegrationMetric.client_email">
<em class="property">property </em><code class="sig-name descname">client_email</code><a class="headerlink" href="#pulumi_cloudamqp.IntegrationMetric.client_email" title="Permalink to this definition">¶</a></dt>
<dd><p>The client email. (Stackdriver)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.IntegrationMetric.email">
<em class="property">property </em><code class="sig-name descname">email</code><a class="headerlink" href="#pulumi_cloudamqp.IntegrationMetric.email" title="Permalink to this definition">¶</a></dt>
<dd><p>The email address registred for the integration service. (Librato)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.IntegrationMetric.instance_id">
<em class="property">property </em><code class="sig-name descname">instance_id</code><a class="headerlink" href="#pulumi_cloudamqp.IntegrationMetric.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance identifier</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.IntegrationMetric.license_key">
<em class="property">property </em><code class="sig-name descname">license_key</code><a class="headerlink" href="#pulumi_cloudamqp.IntegrationMetric.license_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The license key registred for the integration service. (New Relic)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.IntegrationMetric.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_cloudamqp.IntegrationMetric.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of metrics integration</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.IntegrationMetric.private_key">
<em class="property">property </em><code class="sig-name descname">private_key</code><a class="headerlink" href="#pulumi_cloudamqp.IntegrationMetric.private_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The private key. (Stackdriver)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.IntegrationMetric.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_cloudamqp.IntegrationMetric.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Project ID. (Stackdriver)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.IntegrationMetric.queue_allowlist">
<em class="property">property </em><code class="sig-name descname">queue_allowlist</code><a class="headerlink" href="#pulumi_cloudamqp.IntegrationMetric.queue_allowlist" title="Permalink to this definition">¶</a></dt>
<dd><p>(optional) allowlist using regular expression</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.IntegrationMetric.queue_whitelist">
<em class="property">property </em><code class="sig-name descname">queue_whitelist</code><a class="headerlink" href="#pulumi_cloudamqp.IntegrationMetric.queue_whitelist" title="Permalink to this definition">¶</a></dt>
<dd><p><strong>Deprecated</strong></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.IntegrationMetric.region">
<em class="property">property </em><code class="sig-name descname">region</code><a class="headerlink" href="#pulumi_cloudamqp.IntegrationMetric.region" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS region for Cloudwatch and [US/EU] for Data dog/New relic. (Cloudwatch, Data Dog, New Relic)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.IntegrationMetric.secret_access_key">
<em class="property">property </em><code class="sig-name descname">secret_access_key</code><a class="headerlink" href="#pulumi_cloudamqp.IntegrationMetric.secret_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS secret key. (Cloudwatch)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.IntegrationMetric.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_cloudamqp.IntegrationMetric.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>(optional) tags. E.g. env=prod,region=europe</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.IntegrationMetric.vhost_allowlist">
<em class="property">property </em><code class="sig-name descname">vhost_allowlist</code><a class="headerlink" href="#pulumi_cloudamqp.IntegrationMetric.vhost_allowlist" title="Permalink to this definition">¶</a></dt>
<dd><p>(optional) allowlist using regular expression</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.IntegrationMetric.vhost_whitelist">
<em class="property">property </em><code class="sig-name descname">vhost_whitelist</code><a class="headerlink" href="#pulumi_cloudamqp.IntegrationMetric.vhost_whitelist" title="Permalink to this definition">¶</a></dt>
<dd><p><strong>Deprecated</strong></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.IntegrationMetric.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.IntegrationMetric.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.IntegrationMetric.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.IntegrationMetric.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.Notification">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">Notification</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.Notification" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to create and manage recipients to receive alarm notifications. There will always be a default recipient created upon instance creation. This recipient will use team email and receive notifications from default alarms.</p>
<p>Available for all subscription plans.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudamqp</span> <span class="k">as</span> <span class="nn">cloudamqp</span>

<span class="c1"># New recipient to receieve notifications</span>
<span class="n">recipient01</span> <span class="o">=</span> <span class="n">cloudamqp</span><span class="o">.</span><span class="n">Notification</span><span class="p">(</span><span class="s2">&quot;recipient01&quot;</span><span class="p">,</span>
    <span class="n">instance_id</span><span class="o">=</span><span class="n">cloudamqp_instance</span><span class="p">[</span><span class="s2">&quot;instance&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;email&quot;</span><span class="p">,</span>
    <span class="n">value</span><span class="o">=</span><span class="s2">&quot;alarm@example.com&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Valid options for notification type.</p>
<ul class="simple">
<li><p>email</p></li>
<li><p>webhook</p></li>
<li><p>pagerduty</p></li>
<li><p>victorops</p></li>
<li><p>opsgenie</p></li>
<li><p>opsgenie-eu</p></li>
<li><p>slack</p></li>
</ul>
<p>This resource depends on CloudAMQP instance identifier, <code class="docutils literal notranslate"><span class="pre">cloudamqp_instance.instance.id</span></code>.</p>
<p><code class="docutils literal notranslate"><span class="pre">cloudamqp_notification</span></code> can be imported using CloudAMQP internal identifier of a recipient together (CSV separated) with the instance identifier. To retrieve the identifier of a recipient, use <a class="reference external" href="https://docs.cloudamqp.com/cloudamqp_api.html#list-notification-recipients">CloudAMQP API</a></p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import cloudamqp:index/notification:Notification recipient &lt;recpient_id&gt;,&lt;indstance_id&gt;<span class="sb">`</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The CloudAMQP instance ID.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Display name of the recipient.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the notification. See valid options below.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Endpoint to send the notification.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudamqp.Notification.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudamqp.notification.Notification<a class="headerlink" href="#pulumi_cloudamqp.Notification.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Notification resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The CloudAMQP instance ID.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Display name of the recipient.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the notification. See valid options below.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Endpoint to send the notification.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.Notification.instance_id">
<em class="property">property </em><code class="sig-name descname">instance_id</code><a class="headerlink" href="#pulumi_cloudamqp.Notification.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The CloudAMQP instance ID.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.Notification.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_cloudamqp.Notification.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Display name of the recipient.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.Notification.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_cloudamqp.Notification.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of the notification. See valid options below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.Notification.value">
<em class="property">property </em><code class="sig-name descname">value</code><a class="headerlink" href="#pulumi_cloudamqp.Notification.value" title="Permalink to this definition">¶</a></dt>
<dd><p>Endpoint to send the notification.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.Notification.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.Notification.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.Notification.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.Notification.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.Plugin">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">Plugin</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.Plugin" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to enable or disable Rabbit MQ plugins.</p>
<p>Only available for dedicated subscription plans.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudamqp</span> <span class="k">as</span> <span class="nn">cloudamqp</span>

<span class="n">plugin_rabbitmq_top</span> <span class="o">=</span> <span class="n">cloudamqp</span><span class="o">.</span><span class="n">Plugin</span><span class="p">(</span><span class="s2">&quot;pluginRabbitmqTop&quot;</span><span class="p">,</span>
    <span class="n">instance_id</span><span class="o">=</span><span class="n">cloudamqp_instance</span><span class="p">[</span><span class="s2">&quot;instance&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>
</div>
<p>This resource depends on CloudAMQP instance identifier, <code class="docutils literal notranslate"><span class="pre">cloudamqp_instance.instance.id</span></code>.</p>
<p><code class="docutils literal notranslate"><span class="pre">cloudamqp_plugin</span></code> can be imported using the name argument of the resource together with CloudAMQP instance identifier. The name and identifier are CSV separated, see example below.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import cloudamqp:index/plugin:Plugin rabbitmq_management rabbitmq_management,&lt;instance_id&gt;<span class="sb">`</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable or disable the plugins.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The CloudAMQP instance ID.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Rabbit MQ plugin.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudamqp.Plugin.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudamqp.plugin.Plugin<a class="headerlink" href="#pulumi_cloudamqp.Plugin.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Plugin resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable or disable the plugins.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The CloudAMQP instance ID.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Rabbit MQ plugin.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.Plugin.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_cloudamqp.Plugin.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable or disable the plugins.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.Plugin.instance_id">
<em class="property">property </em><code class="sig-name descname">instance_id</code><a class="headerlink" href="#pulumi_cloudamqp.Plugin.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The CloudAMQP instance ID.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.Plugin.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_cloudamqp.Plugin.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Rabbit MQ plugin.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.Plugin.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.Plugin.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.Plugin.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.Plugin.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.PluginCommunity">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">PluginCommunity</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.PluginCommunity" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to install or uninstall community plugins. Once installed the plugin will be available in <code class="docutils literal notranslate"><span class="pre">Plugin</span></code>.</p>
<p>Only available for dedicated subscription plans.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudamqp</span> <span class="k">as</span> <span class="nn">cloudamqp</span>

<span class="n">rabbitmq_delayed_message_exchange</span> <span class="o">=</span> <span class="n">cloudamqp</span><span class="o">.</span><span class="n">PluginCommunity</span><span class="p">(</span><span class="s2">&quot;rabbitmqDelayedMessageExchange&quot;</span><span class="p">,</span>
    <span class="n">instance_id</span><span class="o">=</span><span class="n">cloudamqp_instance</span><span class="p">[</span><span class="s2">&quot;instance_01&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>
</div>
<p>This resource depends on CloudAMQP instance identifier, <code class="docutils literal notranslate"><span class="pre">cloudamqp_instance.instance.id</span></code>.</p>
<p><code class="docutils literal notranslate"><span class="pre">cloudamqp_plugin</span></code> can be imported using the name argument of the resource together with CloudAMQP instance identifier. The name and identifier are CSV separated, see example below.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import cloudamqp:index/pluginCommunity:PluginCommunity &lt;resource_name&gt; &lt;plugin_name&gt;,&lt;instance_id&gt;<span class="sb">`</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable or disable the plugins.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The CloudAMQP instance ID.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Rabbit MQ plugin.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudamqp.PluginCommunity.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudamqp.plugin_community.PluginCommunity<a class="headerlink" href="#pulumi_cloudamqp.PluginCommunity.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PluginCommunity resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable or disable the plugins.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The CloudAMQP instance ID.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Rabbit MQ plugin.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.PluginCommunity.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_cloudamqp.PluginCommunity.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable or disable the plugins.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.PluginCommunity.instance_id">
<em class="property">property </em><code class="sig-name descname">instance_id</code><a class="headerlink" href="#pulumi_cloudamqp.PluginCommunity.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The CloudAMQP instance ID.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.PluginCommunity.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_cloudamqp.PluginCommunity.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Rabbit MQ plugin.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.PluginCommunity.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.PluginCommunity.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.PluginCommunity.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.PluginCommunity.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">apikey</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">baseurl</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.Provider" title="Permalink to this definition">¶</a></dt>
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
<dl class="py method">
<dt id="pulumi_cloudamqp.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.SecurityFirewall">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">SecurityFirewall</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="p">:</span> <span class="n">Union[Sequence[Union[SecurityFirewallRuleArgs, Mapping[str, Any], Awaitable[Union[SecurityFirewallRuleArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[SecurityFirewallRuleArgs, Mapping[str, Any], Awaitable[Union[SecurityFirewallRuleArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.SecurityFirewall" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to configure and manage firewall rules for the CloudAMQP instance. Beware that all rules need to be present, since all older configurations will be overwritten.</p>
<p>Only available for dedicated subscription plans.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudamqp</span> <span class="k">as</span> <span class="nn">cloudamqp</span>

<span class="n">firewall_settings</span> <span class="o">=</span> <span class="n">cloudamqp</span><span class="o">.</span><span class="n">SecurityFirewall</span><span class="p">(</span><span class="s2">&quot;firewallSettings&quot;</span><span class="p">,</span>
    <span class="n">instance_id</span><span class="o">=</span><span class="n">cloudamqp_instance</span><span class="p">[</span><span class="s2">&quot;instance&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">rules</span><span class="o">=</span><span class="p">[</span>
        <span class="n">cloudamqp</span><span class="o">.</span><span class="n">SecurityFirewallRuleArgs</span><span class="p">(</span>
            <span class="n">ip</span><span class="o">=</span><span class="s2">&quot;192.168.0.0/24&quot;</span><span class="p">,</span>
            <span class="n">ports</span><span class="o">=</span><span class="p">[</span>
                <span class="mi">4567</span><span class="p">,</span>
                <span class="mi">4568</span><span class="p">,</span>
            <span class="p">],</span>
            <span class="n">services</span><span class="o">=</span><span class="p">[</span>
                <span class="s2">&quot;AMQP&quot;</span><span class="p">,</span>
                <span class="s2">&quot;AMQPS&quot;</span><span class="p">,</span>
            <span class="p">],</span>
        <span class="p">),</span>
        <span class="n">cloudamqp</span><span class="o">.</span><span class="n">SecurityFirewallRuleArgs</span><span class="p">(</span>
            <span class="n">ip</span><span class="o">=</span><span class="s2">&quot;10.56.72.0/24&quot;</span><span class="p">,</span>
            <span class="n">ports</span><span class="o">=</span><span class="p">[],</span>
            <span class="n">services</span><span class="o">=</span><span class="p">[</span>
                <span class="s2">&quot;AMQP&quot;</span><span class="p">,</span>
                <span class="s2">&quot;AMQPS&quot;</span><span class="p">,</span>
            <span class="p">],</span>
        <span class="p">),</span>
    <span class="p">])</span>
</pre></div>
</div>
<p>This resource depends on CloudAMQP instance identifier, <code class="docutils literal notranslate"><span class="pre">cloudamqp_instance.instance.id</span></code>.</p>
<p><code class="docutils literal notranslate"><span class="pre">cloudamqp_security_firewall</span></code> can be imported using CloudAMQP instance identifier.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import cloudamqp:index/securityFirewall:SecurityFirewall firewall &lt;instance_id&gt;<span class="sb">`</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The CloudAMQP instance ID.</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SecurityFirewallRuleArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – An array of rules, minimum of 1 needs to be configured. Each <code class="docutils literal notranslate"><span class="pre">rules</span></code> block consists of the field documented below.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudamqp.SecurityFirewall.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="p">:</span> <span class="n">Union[Sequence[Union[SecurityFirewallRuleArgs, Mapping[str, Any], Awaitable[Union[SecurityFirewallRuleArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[SecurityFirewallRuleArgs, Mapping[str, Any], Awaitable[Union[SecurityFirewallRuleArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudamqp.security_firewall.SecurityFirewall<a class="headerlink" href="#pulumi_cloudamqp.SecurityFirewall.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecurityFirewall resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The CloudAMQP instance ID.</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SecurityFirewallRuleArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – An array of rules, minimum of 1 needs to be configured. Each <code class="docutils literal notranslate"><span class="pre">rules</span></code> block consists of the field documented below.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.SecurityFirewall.instance_id">
<em class="property">property </em><code class="sig-name descname">instance_id</code><a class="headerlink" href="#pulumi_cloudamqp.SecurityFirewall.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The CloudAMQP instance ID.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.SecurityFirewall.rules">
<em class="property">property </em><code class="sig-name descname">rules</code><a class="headerlink" href="#pulumi_cloudamqp.SecurityFirewall.rules" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of rules, minimum of 1 needs to be configured. Each <code class="docutils literal notranslate"><span class="pre">rules</span></code> block consists of the field documented below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.SecurityFirewall.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.SecurityFirewall.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.SecurityFirewall.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.SecurityFirewall.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.VpcPeering">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">VpcPeering</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peering_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.VpcPeering" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">cloudamqp_vpc_peering</span></code> can be imported using the CloudAMQP instance identifier.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import cloudamqp:index/vpcPeering:VpcPeering &lt;resource_name&gt; &lt;instance_id&gt;<span class="sb">`</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The CloudAMQP instance ID.</p></li>
<li><p><strong>peering_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Peering identifier created by AW peering request.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_cloudamqp.VpcPeering.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peering_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudamqp.vpc_peering.VpcPeering<a class="headerlink" href="#pulumi_cloudamqp.VpcPeering.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VpcPeering resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>instance_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The CloudAMQP instance ID.</p></li>
<li><p><strong>peering_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Peering identifier created by AW peering request.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – VPC peering status</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.VpcPeering.instance_id">
<em class="property">property </em><code class="sig-name descname">instance_id</code><a class="headerlink" href="#pulumi_cloudamqp.VpcPeering.instance_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The CloudAMQP instance ID.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.VpcPeering.peering_id">
<em class="property">property </em><code class="sig-name descname">peering_id</code><a class="headerlink" href="#pulumi_cloudamqp.VpcPeering.peering_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Peering identifier created by AW peering request.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.VpcPeering.status">
<em class="property">property </em><code class="sig-name descname">status</code><a class="headerlink" href="#pulumi_cloudamqp.VpcPeering.status" title="Permalink to this definition">¶</a></dt>
<dd><p>VPC peering status</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_cloudamqp.VpcPeering.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.VpcPeering.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.VpcPeering.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_cloudamqp.VpcPeering.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_cloudamqp.get_alarm">
<code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">get_alarm</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">alarm_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudamqp.get_alarm.AwaitableGetAlarmResult<a class="headerlink" href="#pulumi_cloudamqp.get_alarm" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve information about default or created alarms. Either use <code class="docutils literal notranslate"><span class="pre">alarm_id</span></code> or <code class="docutils literal notranslate"><span class="pre">type</span></code> to retrieve the alarm.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudamqp</span> <span class="k">as</span> <span class="nn">cloudamqp</span>

<span class="n">default_cpu_alarm</span> <span class="o">=</span> <span class="n">cloudamqp</span><span class="o">.</span><span class="n">get_alarm</span><span class="p">(</span><span class="n">instance_id</span><span class="o">=</span><span class="n">cloudamqp_instance</span><span class="p">[</span><span class="s2">&quot;instance&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;cpu&quot;</span><span class="p">)</span>
</pre></div>
</div>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instance_id</span></code> - (Required) The CloudAMQP instance identifier.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">alarm_id</span></code>    - (Optional) The alarm identifier. Either use this or <code class="docutils literal notranslate"><span class="pre">type</span></code> to give <code class="docutils literal notranslate"><span class="pre">Alarm</span></code> necessary information to retrieve the alarm.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code>        - (Optional) The alarm type. Either use this or <code class="docutils literal notranslate"><span class="pre">alarm_id</span></code> to give <code class="docutils literal notranslate"><span class="pre">Alarm</span></code> necessary information when retrieve the alarm.</p></li>
</ul>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code>         - (Computed) Enable/disable status of the alarm.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value_threshold</span></code> - (Computed) The value threshold that triggers the alarm.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">time_threshold</span></code>  - (Computed) The time interval (in seconds) the <code class="docutils literal notranslate"><span class="pre">value_threshold</span></code> should be active before trigger an alarm.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queue_regex</span></code>     - (Computed) Regular expression for which queue to check.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vhost_regex</span></code>     - (Computed) Regular expression for which vhost to check</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">recipients</span></code>      - (Computed) Identifier for recipient to be notified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">message_type</span></code>    - (Computed) Message type <code class="docutils literal notranslate"><span class="pre">(total,</span> <span class="pre">unacked,</span> <span class="pre">ready)</span></code> used by queue alarm type.</p></li>
</ul>
<p>This data source depends on CloudAMQP instance identifier, <code class="docutils literal notranslate"><span class="pre">cloudamqp_instance.instance.id</span></code>.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_cloudamqp.get_credentials">
<code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">get_credentials</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">instance_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudamqp.get_credentials.AwaitableGetCredentialsResult<a class="headerlink" href="#pulumi_cloudamqp.get_credentials" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve information about the credentials of the configured user in Rabbit MQ. Information is extracted from <code class="docutils literal notranslate"><span class="pre">cloudamqp_instance.instance.url</span></code>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudamqp</span> <span class="k">as</span> <span class="nn">cloudamqp</span>

<span class="n">credentials</span> <span class="o">=</span> <span class="n">cloudamqp</span><span class="o">.</span><span class="n">get_credentials</span><span class="p">(</span><span class="n">instance_id</span><span class="o">=</span><span class="n">cloudamqp_instance</span><span class="p">[</span><span class="s2">&quot;instance&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instance_id</span></code> - (Required) The CloudAMQP instance identifier.</p></li>
</ul>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code>    - (Computed/Sensitive) The username for the configured user in Rabbit MQ.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code>    - (Computed/Sensitive) The password used by the <code class="docutils literal notranslate"><span class="pre">username</span></code>.</p></li>
</ul>
<p>This data source depends on CloudAMQP instance identifier, <code class="docutils literal notranslate"><span class="pre">cloudamqp_instance.instance.id</span></code>.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_cloudamqp.get_instance">
<code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">get_instance</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">instance_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_subnet</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudamqp.get_instance.AwaitableGetInstanceResult<a class="headerlink" href="#pulumi_cloudamqp.get_instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve information about an already created CloudAMQP instance. In order to retrieve the correct information, the CoudAMQP instance identifier is needed.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instance_id</span></code> - (Required) The CloudAMQP instance identifier.</p></li>
</ul>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code>        - (Computed) The name of the CloudAMQP instance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">plan</span></code>        - (Computed) The subscription plan for the CloudAMQP instance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">region</span></code>      - (Computed) The cloud platform and region that host the CloudAMQP instance, <code class="docutils literal notranslate"><span class="pre">{platform}::{region}</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_subnet</span></code>  - (Computed) Dedicated VPC subnet configured for the CloudAMQP instance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodes</span></code>       - (Computed) Number of nodes in the cluster of the CloudAMQP instance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rmq_version</span></code> - (Computed) The version of installed Rabbit MQ.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code>         - (Computed/Sensitive) The AMQP url, used by clients to connect for pub/sub.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">apikey</span></code>      - (Computed/Sensitive) The API key to secondary API handing alarms, integration etc.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tags</span></code>        - (Computed) Tags the CloudAMQP instance with categories.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code>        - (Computed) The hostname for the CloudAMQP instance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vhost</span></code>       - (Computed) The virtual host configured in Rabbit MQ.</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_cloudamqp.get_nodes">
<code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">get_nodes</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">instance_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">nodes</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>GetNodesNodeArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudamqp.get_nodes.AwaitableGetNodesResult<a class="headerlink" href="#pulumi_cloudamqp.get_nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve information about the node(s) created by CloudAMQP instance.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudamqp</span> <span class="k">as</span> <span class="nn">cloudamqp</span>

<span class="n">nodes</span> <span class="o">=</span> <span class="n">cloudamqp</span><span class="o">.</span><span class="n">get_nodes</span><span class="p">(</span><span class="n">instance_id</span><span class="o">=</span><span class="n">cloudamqp_instance</span><span class="p">[</span><span class="s2">&quot;instance&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instance_id</span></code> - (Required) The CloudAMQP instance identifier.</p></li>
</ul>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">nodes</span></code> - (Computed) An array of node information. Each <code class="docutils literal notranslate"><span class="pre">nodes</span></code> block consists of the fields documented below.</p></li>
</ul>
<p>The <code class="docutils literal notranslate"><span class="pre">nodes</span></code> block consist of</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">hostname</span></code>          - (Computed) Hostname assigned to the node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code>              - (Computed) Name of the node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">running</span></code>           - (Computed) Is the node running?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rabbitmq_version</span></code>  - (Computed) Currently configured Rabbit MQ version on the node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">erlang_version</span></code>    - (Computed) Currently used Erlanbg version on the node.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hipe</span></code>              - (Computed) Enable or disable High-performance Erlang.</p></li>
</ul>
<p>This data source depends on CloudAMQP instance identifier, <code class="docutils literal notranslate"><span class="pre">cloudamqp_instance.instance.id</span></code>.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_cloudamqp.get_notification">
<code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">get_notification</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">instance_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recipient_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudamqp.get_notification.AwaitableGetNotificationResult<a class="headerlink" href="#pulumi_cloudamqp.get_notification" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve information about default or created recipients. The recipient will receive notifications assigned to an alarm that has triggered. To retrieve the recipient either use <code class="docutils literal notranslate"><span class="pre">recipient_id</span></code> or <code class="docutils literal notranslate"><span class="pre">name</span></code>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudamqp</span> <span class="k">as</span> <span class="nn">cloudamqp</span>

<span class="n">default_recipient</span> <span class="o">=</span> <span class="n">cloudamqp</span><span class="o">.</span><span class="n">get_notification</span><span class="p">(</span><span class="n">instance_id</span><span class="o">=</span><span class="n">cloudamqp_instance</span><span class="p">[</span><span class="s2">&quot;instance&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;default&quot;</span><span class="p">)</span>
</pre></div>
</div>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instance_id</span></code>   - (Required) The CloudAMQP instance identifier.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">recipient_id</span></code>  - (Optional) The recipient identifier.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code>          - (Optional) The name set for the recipient.</p></li>
</ul>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code>  - (Computed) The type of the recipient.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> - (Computed) The notification endpoint, where to send the notification.</p></li>
</ul>
<p>This data source depends on CloudAMQP instance identifier, <code class="docutils literal notranslate"><span class="pre">cloudamqp_instance.instance.id</span></code>.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_cloudamqp.get_plugins">
<code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">get_plugins</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">instance_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plugins</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>GetPluginsPluginArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudamqp.get_plugins.AwaitableGetPluginsResult<a class="headerlink" href="#pulumi_cloudamqp.get_plugins" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve information about installed and available plugins for the CloudAMQP instance.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudamqp</span> <span class="k">as</span> <span class="nn">cloudamqp</span>

<span class="n">plugins</span> <span class="o">=</span> <span class="n">cloudamqp</span><span class="o">.</span><span class="n">get_plugins</span><span class="p">(</span><span class="n">instance_id</span><span class="o">=</span><span class="n">cloudamqp_instance</span><span class="p">[</span><span class="s2">&quot;instance&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instance_id</span></code> - (Required) The CloudAMQP instance identifier.</p></li>
</ul>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">plugins</span></code> - (Computed) An array of plugins. Each <code class="docutils literal notranslate"><span class="pre">plugins</span></code> block consists of the fields documented below.</p></li>
</ul>
<p>The <code class="docutils literal notranslate"><span class="pre">plugins</span></code> block consist of</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code>        - (Computed) The type of the recipient.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code>     - (Computed) Rabbit MQ version that the plugins are shipped with.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> - (Computed) Description of what the plugin does.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code>     - (Computed) Enable or disable information for the plugin.</p></li>
</ul>
<p>This data source depends on CloudAMQP instance identifier, <code class="docutils literal notranslate"><span class="pre">cloudamqp_instance.instance.id</span></code>.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_cloudamqp.get_plugins_community">
<code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">get_plugins_community</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">instance_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plugins</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>GetPluginsCommunityPluginArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudamqp.get_plugins_community.AwaitableGetPluginsCommunityResult<a class="headerlink" href="#pulumi_cloudamqp.get_plugins_community" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve information about available community plugins for the CloudAMQP instance.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudamqp</span> <span class="k">as</span> <span class="nn">cloudamqp</span>

<span class="n">communit_plugins</span> <span class="o">=</span> <span class="n">cloudamqp</span><span class="o">.</span><span class="n">get_plugins_community</span><span class="p">(</span><span class="n">instance_id</span><span class="o">=</span><span class="n">cloudamqp_instance</span><span class="p">[</span><span class="s2">&quot;instance&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instance_id</span></code> - (Required) The CloudAMQP instance identifier.</p></li>
</ul>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">plugins</span></code> - (Computed) An array of community plugins. Each <code class="docutils literal notranslate"><span class="pre">plugins</span></code> block consists of the fields documented below.</p></li>
</ul>
<p>The <code class="docutils literal notranslate"><span class="pre">plugins</span></code> block consists of</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code>        - (Computed) The type of the recipient.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">require</span></code>     - (Computed) Min. required Rabbit MQ version to be used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> - (Computed) Description of what the plugin does.</p></li>
</ul>
<p>This data source depends on CloudAMQP instance identifier, <code class="docutils literal notranslate"><span class="pre">cloudamqp_instance.instance.id</span></code>.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_cloudamqp.get_vpc_info">
<code class="sig-prename descclassname">pulumi_cloudamqp.</code><code class="sig-name descname">get_vpc_info</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">instance_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_cloudamqp.get_vpc_info.AwaitableGetVpcInfoResult<a class="headerlink" href="#pulumi_cloudamqp.get_vpc_info" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve information about VPC for a CloudAMQP instance.</p>
<p>Only available for CloudAMQP instances hosted in AWS.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_cloudamqp</span> <span class="k">as</span> <span class="nn">cloudamqp</span>

<span class="n">vpc_info</span> <span class="o">=</span> <span class="n">cloudamqp</span><span class="o">.</span><span class="n">get_vpc_info</span><span class="p">(</span><span class="n">instance_id</span><span class="o">=</span><span class="n">cloudamqp_instance</span><span class="p">[</span><span class="s2">&quot;instance&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">instance_id</span></code> - (Required) The CloudAMQP instance identifier.</p></li>
</ul>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code>                - (Computed) The name of the CloudAMQP instance.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vpc_subnet</span></code>          - (Computed) Dedicated VPC subnet.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">owner_id</span></code>            - (Computed) AWS account identifier.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">security_group_id</span></code>   - (Computed) AWS security group identifier.</p></li>
</ul>
<p>This data source depends on CloudAMQP instance identifier, <code class="docutils literal notranslate"><span class="pre">cloudamqp_instance.instance.id</span></code>.</p>
</dd></dl>

</div>
