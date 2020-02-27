---
title: Module cms
title_tag: Module cms | Package pulumi_alicloud | Python SDK
linktitle: cms
notitle: true
---

<div class="section" id="cms">
<h1>cms<a class="headerlink" href="#cms" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.cms"></span><dl class="class">
<dt id="pulumi_alicloud.cms.Alarm">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.cms.</code><code class="sig-name descname">Alarm</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">contact_groups=None</em>, <em class="sig-param">dimensions=None</em>, <em class="sig-param">effective_interval=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">end_time=None</em>, <em class="sig-param">metric=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">operator=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">silence_time=None</em>, <em class="sig-param">start_time=None</em>, <em class="sig-param">statistics=None</em>, <em class="sig-param">threshold=None</em>, <em class="sig-param">triggered_count=None</em>, <em class="sig-param">webhook=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cms.Alarm" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource provides a alarm rule resource and it can be used to monitor several cloud services according different metrics.
Details for <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/28608.htm">alarm rule</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>contact_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List contact groups of the alarm rule, which must have been created on the console.</p></li>
<li><p><strong>dimensions</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Map of the resources associated with the alarm rule, such as “instanceId”, “device” and “port”. Each key’s value is a string and it uses comma to split multiple items. For more information, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/28619.htm">Metrics Reference</a>.</p></li>
<li><p><strong>effective_interval</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The interval of effecting alarm rule. It foramt as “hh:mm-hh:mm”, like “0:00-4:00”. Default to “0:00-24:00”.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable alarm rule. Default to true.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `webhook`- (Optional, Available in 1.46.0+) The webhook that should be called when the alarm is triggered. Currently, only http protocol is supported. Default is empty string.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>end_time</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – It has been deprecated from provider version 1.50.0 and ‘effective_interval’ instead.</p></li>
<li><p><strong>metric</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Name of the monitoring metrics corresponding to a project, such as “CPUUtilization” and “networkin_rate”. For more information, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/28619.htm">Metrics Reference</a>.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The alarm rule name.</p></li>
<li><p><strong>operator</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Alarm comparison operator. Valid values: [“&lt;=”, “&lt;”, “&gt;”, “&gt;=”, “==”, “!=”]. Default to “==”.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Index query cycle, which must be consistent with that defined for metrics. Default to 300, in seconds.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Monitor project name, such as “acs_ecs_dashboard” and “acs_rds_dashboard”. For more information, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/28619.htm">Metrics Reference</a>.</p>
</p></li>
<li><p><strong>silence_time</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Notification silence period in the alarm state, in seconds. Valid value range: [300, 86400]. Default to 86400</p></li>
<li><p><strong>start_time</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – It has been deprecated from provider version 1.50.0 and ‘effective_interval’ instead.</p></li>
<li><p><strong>statistics</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Statistical method. It must be consistent with that defined for metrics. Valid values: [“Average”, “Minimum”, “Maximum”]. Default to “Average”.</p></li>
<li><p><strong>threshold</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Alarm threshold value, which must be a numeric value currently.</p></li>
<li><p><strong>triggered_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of consecutive times it has been detected that the values exceed the threshold. Default to 3.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/cms_alarm.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/cms_alarm.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_alicloud.cms.Alarm.contact_groups">
<code class="sig-name descname">contact_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cms.Alarm.contact_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>List contact groups of the alarm rule, which must have been created on the console.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cms.Alarm.dimensions">
<code class="sig-name descname">dimensions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cms.Alarm.dimensions" title="Permalink to this definition">¶</a></dt>
<dd><p>Map of the resources associated with the alarm rule, such as “instanceId”, “device” and “port”. Each key’s value is a string and it uses comma to split multiple items. For more information, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/28619.htm">Metrics Reference</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cms.Alarm.effective_interval">
<code class="sig-name descname">effective_interval</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cms.Alarm.effective_interval" title="Permalink to this definition">¶</a></dt>
<dd><p>The interval of effecting alarm rule. It foramt as “hh:mm-hh:mm”, like “0:00-4:00”. Default to “0:00-24:00”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cms.Alarm.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cms.Alarm.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable alarm rule. Default to true.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">webhook</span></code>- (Optional, Available in 1.46.0+) The webhook that should be called when the alarm is triggered. Currently, only http protocol is supported. Default is empty string.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cms.Alarm.end_time">
<code class="sig-name descname">end_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cms.Alarm.end_time" title="Permalink to this definition">¶</a></dt>
<dd><p>It has been deprecated from provider version 1.50.0 and ‘effective_interval’ instead.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cms.Alarm.metric">
<code class="sig-name descname">metric</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cms.Alarm.metric" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the monitoring metrics corresponding to a project, such as “CPUUtilization” and “networkin_rate”. For more information, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/28619.htm">Metrics Reference</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cms.Alarm.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cms.Alarm.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The alarm rule name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cms.Alarm.operator">
<code class="sig-name descname">operator</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cms.Alarm.operator" title="Permalink to this definition">¶</a></dt>
<dd><p>Alarm comparison operator. Valid values: [“&lt;=”, “&lt;”, “&gt;”, “&gt;=”, “==”, “!=”]. Default to “==”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cms.Alarm.period">
<code class="sig-name descname">period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cms.Alarm.period" title="Permalink to this definition">¶</a></dt>
<dd><p>Index query cycle, which must be consistent with that defined for metrics. Default to 300, in seconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cms.Alarm.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cms.Alarm.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Monitor project name, such as “acs_ecs_dashboard” and “acs_rds_dashboard”. For more information, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/28619.htm">Metrics Reference</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cms.Alarm.silence_time">
<code class="sig-name descname">silence_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cms.Alarm.silence_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Notification silence period in the alarm state, in seconds. Valid value range: [300, 86400]. Default to 86400</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cms.Alarm.start_time">
<code class="sig-name descname">start_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cms.Alarm.start_time" title="Permalink to this definition">¶</a></dt>
<dd><p>It has been deprecated from provider version 1.50.0 and ‘effective_interval’ instead.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cms.Alarm.statistics">
<code class="sig-name descname">statistics</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cms.Alarm.statistics" title="Permalink to this definition">¶</a></dt>
<dd><p>Statistical method. It must be consistent with that defined for metrics. Valid values: [“Average”, “Minimum”, “Maximum”]. Default to “Average”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cms.Alarm.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cms.Alarm.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The current alarm rule status.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cms.Alarm.threshold">
<code class="sig-name descname">threshold</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cms.Alarm.threshold" title="Permalink to this definition">¶</a></dt>
<dd><p>Alarm threshold value, which must be a numeric value currently.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_alicloud.cms.Alarm.triggered_count">
<code class="sig-name descname">triggered_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.cms.Alarm.triggered_count" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of consecutive times it has been detected that the values exceed the threshold. Default to 3.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.cms.Alarm.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">contact_groups=None</em>, <em class="sig-param">dimensions=None</em>, <em class="sig-param">effective_interval=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">end_time=None</em>, <em class="sig-param">metric=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">operator=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">silence_time=None</em>, <em class="sig-param">start_time=None</em>, <em class="sig-param">statistics=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">threshold=None</em>, <em class="sig-param">triggered_count=None</em>, <em class="sig-param">webhook=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cms.Alarm.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Alarm resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>contact_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List contact groups of the alarm rule, which must have been created on the console.</p></li>
<li><p><strong>dimensions</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>Map of the resources associated with the alarm rule, such as “instanceId”, “device” and “port”. Each key’s value is a string and it uses comma to split multiple items. For more information, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/28619.htm">Metrics Reference</a>.</p>
</p></li>
<li><p><strong>effective_interval</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The interval of effecting alarm rule. It foramt as “hh:mm-hh:mm”, like “0:00-4:00”. Default to “0:00-24:00”.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable alarm rule. Default to true.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `webhook`- (Optional, Available in 1.46.0+) The webhook that should be called when the alarm is triggered. Currently, only http protocol is supported. Default is empty string.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>end_time</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – It has been deprecated from provider version 1.50.0 and ‘effective_interval’ instead.</p></li>
<li><p><strong>metric</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Name of the monitoring metrics corresponding to a project, such as “CPUUtilization” and “networkin_rate”. For more information, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/28619.htm">Metrics Reference</a>.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The alarm rule name.</p></li>
<li><p><strong>operator</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Alarm comparison operator. Valid values: [“&lt;=”, “&lt;”, “&gt;”, “&gt;=”, “==”, “!=”]. Default to “==”.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Index query cycle, which must be consistent with that defined for metrics. Default to 300, in seconds.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Monitor project name, such as “acs_ecs_dashboard” and “acs_rds_dashboard”. For more information, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/28619.htm">Metrics Reference</a>.</p>
</p></li>
<li><p><strong>silence_time</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Notification silence period in the alarm state, in seconds. Valid value range: [300, 86400]. Default to 86400</p></li>
<li><p><strong>start_time</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – It has been deprecated from provider version 1.50.0 and ‘effective_interval’ instead.</p></li>
<li><p><strong>statistics</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Statistical method. It must be consistent with that defined for metrics. Valid values: [“Average”, “Minimum”, “Maximum”]. Default to “Average”.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The current alarm rule status.</p></li>
<li><p><strong>threshold</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Alarm threshold value, which must be a numeric value currently.</p></li>
<li><p><strong>triggered_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of consecutive times it has been detected that the values exceed the threshold. Default to 3.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/cms_alarm.html.markdown">https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/cms_alarm.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_alicloud.cms.Alarm.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cms.Alarm.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.cms.Alarm.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.cms.Alarm.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
