---
title: Module log
title_tag: Module log | Package pulumi_alicloud | Python SDK
linktitle: log
notitle: true
---

<div class="section" id="log">
<h1>log<a class="headerlink" href="#log" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.log"></span><dl class="class">
<dt id="pulumi_alicloud.log.Alert">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.log.</code><code class="sig-name descname">Alert</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">alert_description=None</em>, <em class="sig-param">alert_displayname=None</em>, <em class="sig-param">alert_name=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">dashboard=None</em>, <em class="sig-param">mute_until=None</em>, <em class="sig-param">notification_lists=None</em>, <em class="sig-param">notify_threshold=None</em>, <em class="sig-param">project_name=None</em>, <em class="sig-param">query_lists=None</em>, <em class="sig-param">schedule_interval=None</em>, <em class="sig-param">schedule_type=None</em>, <em class="sig-param">throttling=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.log.Alert" title="Permalink to this definition">¶</a></dt>
<dd><p>Log alert is a unit of log service, which is used to monitor and alert the user’s logstore status information. 
Log Service enables you to configure alerts based on the charts in a dashboard to monitor the service status in real time.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.78.0</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alert_description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Alert description.</p></li>
<li><p><strong>alert_displayname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Alert displayname.</p></li>
<li><p><strong>alert_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of logstore for configuring alarm service.</p></li>
<li><p><strong>condition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Conditional expression, such as: count&gt; 100.</p></li>
<li><p><strong>mute_until</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Timestamp, notifications before closing again.</p></li>
<li><p><strong>notification_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Alarm information notification list.</p></li>
<li><p><strong>notify_threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Notification threshold, which is not notified until the number of triggers is reached. The default is 1.</p></li>
<li><p><strong>project_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project name.</p></li>
<li><p><strong>query_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Multiple conditions for configured alarm query.</p></li>
<li><p><strong>schedule_interval</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Execution interval. 60 seconds minimum, such as 60s, 1h.</p></li>
<li><p><strong>schedule_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Default FixedRate. No need to configure this parameter.</p></li>
<li><p><strong>throttling</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Notification interval, default is no interval. Support number + unit type, for example 60s, 1h.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>notification_lists</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Notice content of alarm.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailLists</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Email address list.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mobileLists</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - SMS sending mobile number.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Request address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Notification type. support Email, SMS, DingTalk.</p></li>
</ul>
<p>The <strong>query_lists</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">chartTitle</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - chart title</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">end</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - end time. example: 20s.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logstore</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Query logstore</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">query</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - query corresponding to chart. example: * AND aliyun.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - begin time. example: -60s.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeSpanType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - default Custom. No need to configure this parameter.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_alicloud.log.Alert.alert_description">
<code class="sig-name descname">alert_description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.Alert.alert_description" title="Permalink to this definition">¶</a></dt>
<dd><p>Alert description.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.log.Alert.alert_displayname">
<code class="sig-name descname">alert_displayname</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.Alert.alert_displayname" title="Permalink to this definition">¶</a></dt>
<dd><p>Alert displayname.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.log.Alert.alert_name">
<code class="sig-name descname">alert_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.Alert.alert_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of logstore for configuring alarm service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.log.Alert.condition">
<code class="sig-name descname">condition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.Alert.condition" title="Permalink to this definition">¶</a></dt>
<dd><p>Conditional expression, such as: count&gt; 100.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.log.Alert.mute_until">
<code class="sig-name descname">mute_until</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.Alert.mute_until" title="Permalink to this definition">¶</a></dt>
<dd><p>Timestamp, notifications before closing again.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.log.Alert.notification_lists">
<code class="sig-name descname">notification_lists</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.Alert.notification_lists" title="Permalink to this definition">¶</a></dt>
<dd><p>Alarm information notification list.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Notice content of alarm.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailLists</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Email address list.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mobileLists</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - SMS sending mobile number.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Request address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Notification type. support Email, SMS, DingTalk.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.log.Alert.notify_threshold">
<code class="sig-name descname">notify_threshold</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.Alert.notify_threshold" title="Permalink to this definition">¶</a></dt>
<dd><p>Notification threshold, which is not notified until the number of triggers is reached. The default is 1.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.log.Alert.project_name">
<code class="sig-name descname">project_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.Alert.project_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The project name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.log.Alert.query_lists">
<code class="sig-name descname">query_lists</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.Alert.query_lists" title="Permalink to this definition">¶</a></dt>
<dd><p>Multiple conditions for configured alarm query.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">chartTitle</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - chart title</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">end</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - end time. example: 20s.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logstore</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Query logstore</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">query</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - query corresponding to chart. example: * AND aliyun.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - begin time. example: -60s.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeSpanType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - default Custom. No need to configure this parameter.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.log.Alert.schedule_interval">
<code class="sig-name descname">schedule_interval</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.Alert.schedule_interval" title="Permalink to this definition">¶</a></dt>
<dd><p>Execution interval. 60 seconds minimum, such as 60s, 1h.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.log.Alert.schedule_type">
<code class="sig-name descname">schedule_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.Alert.schedule_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Default FixedRate. No need to configure this parameter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.log.Alert.throttling">
<code class="sig-name descname">throttling</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.Alert.throttling" title="Permalink to this definition">¶</a></dt>
<dd><p>Notification interval, default is no interval. Support number + unit type, for example 60s, 1h.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.log.Alert.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">alert_description=None</em>, <em class="sig-param">alert_displayname=None</em>, <em class="sig-param">alert_name=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">dashboard=None</em>, <em class="sig-param">mute_until=None</em>, <em class="sig-param">notification_lists=None</em>, <em class="sig-param">notify_threshold=None</em>, <em class="sig-param">project_name=None</em>, <em class="sig-param">query_lists=None</em>, <em class="sig-param">schedule_interval=None</em>, <em class="sig-param">schedule_type=None</em>, <em class="sig-param">throttling=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.log.Alert.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Alert resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alert_description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Alert description.</p></li>
<li><p><strong>alert_displayname</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Alert displayname.</p></li>
<li><p><strong>alert_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of logstore for configuring alarm service.</p></li>
<li><p><strong>condition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Conditional expression, such as: count&gt; 100.</p></li>
<li><p><strong>mute_until</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Timestamp, notifications before closing again.</p></li>
<li><p><strong>notification_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Alarm information notification list.</p></li>
<li><p><strong>notify_threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Notification threshold, which is not notified until the number of triggers is reached. The default is 1.</p></li>
<li><p><strong>project_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project name.</p></li>
<li><p><strong>query_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Multiple conditions for configured alarm query.</p></li>
<li><p><strong>schedule_interval</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Execution interval. 60 seconds minimum, such as 60s, 1h.</p></li>
<li><p><strong>schedule_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Default FixedRate. No need to configure this parameter.</p></li>
<li><p><strong>throttling</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Notification interval, default is no interval. Support number + unit type, for example 60s, 1h.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>notification_lists</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Notice content of alarm.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">emailLists</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Email address list.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mobileLists</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - SMS sending mobile number.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Request address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Notification type. support Email, SMS, DingTalk.</p></li>
</ul>
<p>The <strong>query_lists</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">chartTitle</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - chart title</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">end</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - end time. example: 20s.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logstore</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Query logstore</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">query</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - query corresponding to chart. example: * AND aliyun.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">start</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - begin time. example: -60s.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeSpanType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - default Custom. No need to configure this parameter.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.log.Alert.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.log.Alert.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.log.Alert.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.log.Alert.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.log.LogTailAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.log.</code><code class="sig-name descname">LogTailAttachment</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">logtail_config_name=None</em>, <em class="sig-param">machine_group_name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.log.LogTailAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>The Logtail access service is a log collection agent provided by Log Service.
You can use Logtail to collect logs from servers such as Alibaba Cloud Elastic
Compute Service (ECS) instances in real time in the Log Service console. <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/29058.htm">Refer to details</a></p>
<p>This resource amis to attach one logtail configure to a machine group.</p>
<blockquote>
<div><p><strong>NOTE:</strong> One logtail configure can be attached to multiple machine groups and one machine group can attach several logtail configures.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>logtail_config_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Logtail configuration name, which is unique in the same project.</p></li>
<li><p><strong>machine_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The machine group name, which is unique in the same project.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project name to the log store belongs.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.log.LogTailAttachment.logtail_config_name">
<code class="sig-name descname">logtail_config_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.LogTailAttachment.logtail_config_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Logtail configuration name, which is unique in the same project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.log.LogTailAttachment.machine_group_name">
<code class="sig-name descname">machine_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.LogTailAttachment.machine_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The machine group name, which is unique in the same project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.log.LogTailAttachment.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.LogTailAttachment.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project name to the log store belongs.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.log.LogTailAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">logtail_config_name=None</em>, <em class="sig-param">machine_group_name=None</em>, <em class="sig-param">project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.log.LogTailAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LogTailAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>logtail_config_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Logtail configuration name, which is unique in the same project.</p></li>
<li><p><strong>machine_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The machine group name, which is unique in the same project.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project name to the log store belongs.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.log.LogTailAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.log.LogTailAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.log.LogTailAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.log.LogTailAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.log.LogTailConfig">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.log.</code><code class="sig-name descname">LogTailConfig</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">input_detail=None</em>, <em class="sig-param">input_type=None</em>, <em class="sig-param">log_sample=None</em>, <em class="sig-param">logstore=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">output_type=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.log.LogTailConfig" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a LogTailConfig resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] input_detail: The logtail configure the required JSON files. (<a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/29058.htm">Refer to details</a>)
:param pulumi.Input[str] input_type: The input type. Currently only two types of files and plugin are supported.
:param pulumi.Input[str] log_sample: （Optional）The log sample of the Logtail configuration. The log size cannot exceed 1,000 bytes.
:param pulumi.Input[str] logstore: The log store name to the query index belongs.
:param pulumi.Input[str] name: The Logtail configuration name, which is unique in the same project.
:param pulumi.Input[str] output_type: The output type. Currently, only LogService is supported.
:param pulumi.Input[str] project: The project name to the log store belongs.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.log.LogTailConfig.input_detail">
<code class="sig-name descname">input_detail</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.LogTailConfig.input_detail" title="Permalink to this definition">¶</a></dt>
<dd><p>The logtail configure the required JSON files. (<a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/29058.htm">Refer to details</a>)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.log.LogTailConfig.input_type">
<code class="sig-name descname">input_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.LogTailConfig.input_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The input type. Currently only two types of files and plugin are supported.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.log.LogTailConfig.log_sample">
<code class="sig-name descname">log_sample</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.LogTailConfig.log_sample" title="Permalink to this definition">¶</a></dt>
<dd><p>（Optional）The log sample of the Logtail configuration. The log size cannot exceed 1,000 bytes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.log.LogTailConfig.logstore">
<code class="sig-name descname">logstore</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.LogTailConfig.logstore" title="Permalink to this definition">¶</a></dt>
<dd><p>The log store name to the query index belongs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.log.LogTailConfig.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.LogTailConfig.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Logtail configuration name, which is unique in the same project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.log.LogTailConfig.output_type">
<code class="sig-name descname">output_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.LogTailConfig.output_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The output type. Currently, only LogService is supported.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.log.LogTailConfig.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.LogTailConfig.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project name to the log store belongs.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.log.LogTailConfig.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">input_detail=None</em>, <em class="sig-param">input_type=None</em>, <em class="sig-param">log_sample=None</em>, <em class="sig-param">logstore=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">output_type=None</em>, <em class="sig-param">project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.log.LogTailConfig.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LogTailConfig resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>input_detail</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The logtail configure the required JSON files. (<a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/29058.htm">Refer to details</a>)</p>
</p></li>
<li><p><strong>input_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The input type. Currently only two types of files and plugin are supported.</p></li>
<li><p><strong>log_sample</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – （Optional）The log sample of the Logtail configuration. The log size cannot exceed 1,000 bytes.</p></li>
<li><p><strong>logstore</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The log store name to the query index belongs.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Logtail configuration name, which is unique in the same project.</p></li>
<li><p><strong>output_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The output type. Currently, only LogService is supported.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project name to the log store belongs.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.log.LogTailConfig.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.log.LogTailConfig.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.log.LogTailConfig.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.log.LogTailConfig.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.log.MachineGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.log.</code><code class="sig-name descname">MachineGroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">identify_lists=None</em>, <em class="sig-param">identify_type=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">topic=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.log.MachineGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a MachineGroup resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[list] identify_lists: The machine identification.
:param pulumi.Input[str] identify_type: The machine identification type, including IP and user-defined identity. Valid values are “ip” and “userdefined”. Default to “ip”.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `identify_list`- (Required) The specific machine identification, which can be an IP address or user-defined identity.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The machine group name, which is unique in the same project.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project name to the machine group belongs.</p></li>
<li><p><strong>topic</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The topic of a machine group.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_alicloud.log.MachineGroup.identify_lists">
<code class="sig-name descname">identify_lists</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.MachineGroup.identify_lists" title="Permalink to this definition">¶</a></dt>
<dd><p>The machine identification.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.log.MachineGroup.identify_type">
<code class="sig-name descname">identify_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.MachineGroup.identify_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The machine identification type, including IP and user-defined identity. Valid values are “ip” and “userdefined”. Default to “ip”.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identify_list</span></code>- (Required) The specific machine identification, which can be an IP address or user-defined identity.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.log.MachineGroup.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.MachineGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The machine group name, which is unique in the same project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.log.MachineGroup.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.MachineGroup.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project name to the machine group belongs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.log.MachineGroup.topic">
<code class="sig-name descname">topic</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.MachineGroup.topic" title="Permalink to this definition">¶</a></dt>
<dd><p>The topic of a machine group.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.log.MachineGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">identify_lists=None</em>, <em class="sig-param">identify_type=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">topic=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.log.MachineGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MachineGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>identify_lists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The machine identification.</p></li>
<li><p><strong>identify_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The machine identification type, including IP and user-defined identity. Valid values are “ip” and “userdefined”. Default to “ip”.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `identify_list`- (Required) The specific machine identification, which can be an IP address or user-defined identity.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The machine group name, which is unique in the same project.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project name to the machine group belongs.</p></li>
<li><p><strong>topic</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The topic of a machine group.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.log.MachineGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.log.MachineGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.log.MachineGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.log.MachineGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.log.Project">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.log.</code><code class="sig-name descname">Project</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.log.Project" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Project resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] description: Description of the log project.
:param pulumi.Input[str] name: The name of the log project. It is the only in one Alicloud account.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.log.Project.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.Project.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the log project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.log.Project.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.Project.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the log project. It is the only in one Alicloud account.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.log.Project.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.log.Project.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Project resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the log project.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the log project. It is the only in one Alicloud account.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.log.Project.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.log.Project.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.log.Project.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.log.Project.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.log.Store">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.log.</code><code class="sig-name descname">Store</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">append_meta=None</em>, <em class="sig-param">auto_split=None</em>, <em class="sig-param">enable_web_tracking=None</em>, <em class="sig-param">max_split_shard_count=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">retention_period=None</em>, <em class="sig-param">shard_count=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.log.Store" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Store resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] append_meta: Determines whether to append log meta automatically. The meta includes log receive time and client IP address. Default to true.
:param pulumi.Input[bool] auto_split: Determines whether to automatically split a shard. Default to true.
:param pulumi.Input[bool] enable_web_tracking: Determines whether to enable Web Tracking. Default false.
:param pulumi.Input[float] max_split_shard_count: The maximum number of shards for automatic split, which is in the range of 1 to 64. You must specify this parameter when autoSplit is true.
:param pulumi.Input[str] name: The log store, which is unique in the same project.
:param pulumi.Input[str] project: The project name to the log store belongs.
:param pulumi.Input[float] retention_period: The data retention time (in days). Valid values: [1-3650]. Default to 30. Log store data will be stored permanently when the value is “3650”.
:param pulumi.Input[float] shard_count: The number of shards in this log store. Default to 2. You can modify it by “Split” or “Merge” operations. <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/28976.htm">Refer to details</a></p>
<dl class="attribute">
<dt id="pulumi_alicloud.log.Store.append_meta">
<code class="sig-name descname">append_meta</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.Store.append_meta" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines whether to append log meta automatically. The meta includes log receive time and client IP address. Default to true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.log.Store.auto_split">
<code class="sig-name descname">auto_split</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.Store.auto_split" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines whether to automatically split a shard. Default to true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.log.Store.enable_web_tracking">
<code class="sig-name descname">enable_web_tracking</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.Store.enable_web_tracking" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines whether to enable Web Tracking. Default false.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.log.Store.max_split_shard_count">
<code class="sig-name descname">max_split_shard_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.Store.max_split_shard_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of shards for automatic split, which is in the range of 1 to 64. You must specify this parameter when autoSplit is true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.log.Store.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.Store.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The log store, which is unique in the same project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.log.Store.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.Store.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project name to the log store belongs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.log.Store.retention_period">
<code class="sig-name descname">retention_period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.Store.retention_period" title="Permalink to this definition">¶</a></dt>
<dd><p>The data retention time (in days). Valid values: [1-3650]. Default to 30. Log store data will be stored permanently when the value is “3650”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.log.Store.shard_count">
<code class="sig-name descname">shard_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.Store.shard_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of shards in this log store. Default to 2. You can modify it by “Split” or “Merge” operations. <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/28976.htm">Refer to details</a></p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.log.Store.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">append_meta=None</em>, <em class="sig-param">auto_split=None</em>, <em class="sig-param">enable_web_tracking=None</em>, <em class="sig-param">max_split_shard_count=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">retention_period=None</em>, <em class="sig-param">shard_count=None</em>, <em class="sig-param">shards=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.log.Store.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Store resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>append_meta</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines whether to append log meta automatically. The meta includes log receive time and client IP address. Default to true.</p></li>
<li><p><strong>auto_split</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines whether to automatically split a shard. Default to true.</p></li>
<li><p><strong>enable_web_tracking</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines whether to enable Web Tracking. Default false.</p></li>
<li><p><strong>max_split_shard_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of shards for automatic split, which is in the range of 1 to 64. You must specify this parameter when autoSplit is true.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The log store, which is unique in the same project.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project name to the log store belongs.</p></li>
<li><p><strong>retention_period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The data retention time (in days). Valid values: [1-3650]. Default to 30. Log store data will be stored permanently when the value is “3650”.</p></li>
<li><p><strong>shard_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – <p>The number of shards in this log store. Default to 2. You can modify it by “Split” or “Merge” operations. <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/28976.htm">Refer to details</a></p>
</p></li>
</ul>
</dd>
</dl>
<p>The <strong>shards</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">beginKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">endKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The ID of the log project. It formats of <code class="docutils literal notranslate"><span class="pre">&lt;project&gt;:&lt;name&gt;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">status</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.log.Store.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.log.Store.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.log.Store.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.log.Store.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.log.StoreIndex">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.log.</code><code class="sig-name descname">StoreIndex</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">field_searches=None</em>, <em class="sig-param">full_text=None</em>, <em class="sig-param">logstore=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.log.StoreIndex" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-default notranslate"><div class="highlight"><pre><span></span>Create a StoreIndex resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[list] field_searches: List configurations of field search index. Valid item as follows:
:param pulumi.Input[dict] full_text: The configuration of full text index. Valid item as follows:
:param pulumi.Input[str] logstore: The log store name to the query index belongs.
:param pulumi.Input[str] project: The project name to the log store belongs.

The **field_searches** object supports the following:

  * `alias` (`pulumi.Input[str]`) - The alias of one field.
  * `caseSensitive` (`pulumi.Input[bool]`) - Whether the case sensitive for the field. Default to false. It is valid when &quot;type&quot; is &quot;text&quot; or &quot;json&quot;.
  * `enableAnalytics` (`pulumi.Input[bool]`) - Whether to enable field analytics. Default to true.
  * `includeChinese` (`pulumi.Input[bool]`) - Whether includes the chinese for the field. Default to false. It is valid when &quot;type&quot; is &quot;text&quot; or &quot;json&quot;.
  * `jsonKeys` (`pulumi.Input[list]`) - Use nested index when type is json
    * `alias` (`pulumi.Input[str]`) - The alias of one field.
    * `docValue` (`pulumi.Input[bool]`) - Whether to enable statistics. default to true.
    * `name` (`pulumi.Input[str]`) - When using the json_keys field, this field is required.
    * `type` (`pulumi.Input[str]`) - The type of one field. Valid values: [&quot;long&quot;, &quot;text&quot;, &quot;double&quot;]. Default to &quot;long&quot;

  * `name` (`pulumi.Input[str]`) - When using the json_keys field, this field is required.
  * `token` (`pulumi.Input[str]`) - The string of several split words, like &quot;
</pre></div>
</div>
<p>“, “#”. It is valid when “type” is “text” or “json”.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>  * `type` (`pulumi.Input[str]`) - The type of one field. Valid values: [&quot;long&quot;, &quot;text&quot;, &quot;double&quot;]. Default to &quot;long&quot;

The **full_text** object supports the following:

  * `caseSensitive` (`pulumi.Input[bool]`) - Whether the case sensitive for the field. Default to false. It is valid when &quot;type&quot; is &quot;text&quot; or &quot;json&quot;.
  * `includeChinese` (`pulumi.Input[bool]`) - Whether includes the chinese for the field. Default to false. It is valid when &quot;type&quot; is &quot;text&quot; or &quot;json&quot;.
  * `token` (`pulumi.Input[str]`) - The string of several split words, like &quot;
</pre></div>
</div>
<p>“, “#”. It is valid when “type” is “text” or “json”.</p>
<dl class="attribute">
<dt id="pulumi_alicloud.log.StoreIndex.field_searches">
<code class="sig-name descname">field_searches</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.StoreIndex.field_searches" title="Permalink to this definition">¶</a></dt>
<dd><p>List configurations of field search index. Valid item as follows:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">alias</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The alias of one field.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">caseSensitive</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether the case sensitive for the field. Default to false. It is valid when “type” is “text” or “json”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableAnalytics</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to enable field analytics. Default to true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeChinese</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether includes the chinese for the field. Default to false. It is valid when “type” is “text” or “json”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">jsonKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Use nested index when type is json</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">alias</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The alias of one field.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">docValue</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to enable statistics. default to true.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - When using the json_keys field, this field is required.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of one field. Valid values: [“long”, “text”, “double”]. Default to “long”</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - When using the json_keys field, this field is required.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The string of several split words, like ”
“, “#”. It is valid when “type” is “text” or “json”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of one field. Valid values: [“long”, “text”, “double”]. Default to “long”</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.log.StoreIndex.full_text">
<code class="sig-name descname">full_text</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.StoreIndex.full_text" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration of full text index. Valid item as follows:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caseSensitive</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether the case sensitive for the field. Default to false. It is valid when “type” is “text” or “json”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeChinese</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether includes the chinese for the field. Default to false. It is valid when “type” is “text” or “json”.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">token</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The string of several split words, like ”
“, “#”. It is valid when “type” is “text” or “json”.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.log.StoreIndex.logstore">
<code class="sig-name descname">logstore</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.StoreIndex.logstore" title="Permalink to this definition">¶</a></dt>
<dd><p>The log store name to the query index belongs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.log.StoreIndex.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.log.StoreIndex.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project name to the log store belongs.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.log.StoreIndex.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">field_searches=None</em>, <em class="sig-param">full_text=None</em>, <em class="sig-param">logstore=None</em>, <em class="sig-param">project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.log.StoreIndex.get" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-default notranslate"><div class="highlight"><pre><span></span>Get an existing StoreIndex resource&#39;s state with the given name, id, and optional extra
properties used to qualify the lookup.

:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[list] field_searches: List configurations of field search index. Valid item as follows:
:param pulumi.Input[dict] full_text: The configuration of full text index. Valid item as follows:
:param pulumi.Input[str] logstore: The log store name to the query index belongs.
:param pulumi.Input[str] project: The project name to the log store belongs.

The **field_searches** object supports the following:

  * `alias` (`pulumi.Input[str]`) - The alias of one field.
  * `caseSensitive` (`pulumi.Input[bool]`) - Whether the case sensitive for the field. Default to false. It is valid when &quot;type&quot; is &quot;text&quot; or &quot;json&quot;.
  * `enableAnalytics` (`pulumi.Input[bool]`) - Whether to enable field analytics. Default to true.
  * `includeChinese` (`pulumi.Input[bool]`) - Whether includes the chinese for the field. Default to false. It is valid when &quot;type&quot; is &quot;text&quot; or &quot;json&quot;.
  * `jsonKeys` (`pulumi.Input[list]`) - Use nested index when type is json
    * `alias` (`pulumi.Input[str]`) - The alias of one field.
    * `docValue` (`pulumi.Input[bool]`) - Whether to enable statistics. default to true.
    * `name` (`pulumi.Input[str]`) - When using the json_keys field, this field is required.
    * `type` (`pulumi.Input[str]`) - The type of one field. Valid values: [&quot;long&quot;, &quot;text&quot;, &quot;double&quot;]. Default to &quot;long&quot;

  * `name` (`pulumi.Input[str]`) - When using the json_keys field, this field is required.
  * `token` (`pulumi.Input[str]`) - The string of several split words, like &quot;
</pre></div>
</div>
<p>“, “#”. It is valid when “type” is “text” or “json”.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>  * `type` (`pulumi.Input[str]`) - The type of one field. Valid values: [&quot;long&quot;, &quot;text&quot;, &quot;double&quot;]. Default to &quot;long&quot;

The **full_text** object supports the following:

  * `caseSensitive` (`pulumi.Input[bool]`) - Whether the case sensitive for the field. Default to false. It is valid when &quot;type&quot; is &quot;text&quot; or &quot;json&quot;.
  * `includeChinese` (`pulumi.Input[bool]`) - Whether includes the chinese for the field. Default to false. It is valid when &quot;type&quot; is &quot;text&quot; or &quot;json&quot;.
  * `token` (`pulumi.Input[str]`) - The string of several split words, like &quot;
</pre></div>
</div>
<p>“, “#”. It is valid when “type” is “text” or “json”.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.log.StoreIndex.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.log.StoreIndex.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.log.StoreIndex.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.log.StoreIndex.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

</div>
