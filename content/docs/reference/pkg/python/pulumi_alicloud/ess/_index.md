---
title: Module ess
title_tag: Module ess | Package pulumi_alicloud | Python SDK
linktitle: ess
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "alicloud" >}}

<div class="section" id="ess">
<h1>ess<a class="headerlink" href="#ess" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-alicloud/issues">pulumi/pulumi-alicloud repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-alicloud/issues">terraform-providers/terraform-provider-alicloud repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_alicloud.ess"></span><dl class="py class">
<dt id="pulumi_alicloud.ess.Alarm">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ess.</code><code class="sig-name descname">Alarm</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alarm_actions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_monitor_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comparison_operator</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dimensions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">evaluation_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">statistics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">threshold</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.Alarm" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Alarm resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[list] alarm_actions: The list of actions to execute when this alarm transition into an ALARM state. Each action is specified as ess scaling rule ari.
:param pulumi.Input[float] cloud_monitor_group_id: Defines the application group id defined by CMS which is assigned when you upload custom metric to CMS, only available for custom metirc.
:param pulumi.Input[str] comparison_operator: The arithmetic operation to use when comparing the specified Statistic and Threshold. The specified Statistic value is used as the first operand. Supported value: &gt;=, &lt;=, &gt;, &lt;. Defaults to &gt;=.
:param pulumi.Input[str] description: The description for the alarm.
:param pulumi.Input[dict] dimensions: The dimension map for the alarm’s associated metric (documented below). For all metrics, you can not set the dimension key as “scaling_group” or “userId”, which is set by default, the second dimension for metric, such as “device” for “PackagesNetIn”, need to be set by users.
:param pulumi.Input[bool] enable: Whether to enable specific ess alarm. Default to true.
:param pulumi.Input[float] evaluation_count: The number of times that needs to satisfies comparison condition before transition into ALARM state. Defaults to 3.
:param pulumi.Input[str] metric_name: The name for the alarm’s associated metric. See Block_metricNames_and_dimensions below for details.
:param pulumi.Input[str] metric_type: The type for the alarm’s associated metric. Supported value: system, custom. “system” means the metric data is collected by Aliyun Cloud Monitor Service(CMS), “custom” means the metric data is upload to CMS by users. Defaults to system. 
:param pulumi.Input[str] name: The name for ess alarm.
:param pulumi.Input[float] period: The period in seconds over which the specified statistic is applied. Supported value: 60, 120, 300, 900. Defaults to 300.
:param pulumi.Input[str] scaling_group_id: The scaling group associated with this alarm, the ‘ForceNew’ attribute is available in 1.56.0+.
:param pulumi.Input[str] statistics: The statistic to apply to the alarm’s associated metric. Supported value: Average, Minimum, Maximum. Defaults to Average.
:param pulumi.Input[str] threshold: The value against which the specified statistics is compared.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.ess.Alarm.alarm_actions">
<code class="sig-name descname">alarm_actions</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.Alarm.alarm_actions" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of actions to execute when this alarm transition into an ALARM state. Each action is specified as ess scaling rule ari.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.Alarm.cloud_monitor_group_id">
<code class="sig-name descname">cloud_monitor_group_id</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.Alarm.cloud_monitor_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines the application group id defined by CMS which is assigned when you upload custom metric to CMS, only available for custom metirc.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.Alarm.comparison_operator">
<code class="sig-name descname">comparison_operator</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.Alarm.comparison_operator" title="Permalink to this definition">¶</a></dt>
<dd><p>The arithmetic operation to use when comparing the specified Statistic and Threshold. The specified Statistic value is used as the first operand. Supported value: &gt;=, &lt;=, &gt;, &lt;. Defaults to &gt;=.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.Alarm.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.Alarm.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description for the alarm.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.Alarm.dimensions">
<code class="sig-name descname">dimensions</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.Alarm.dimensions" title="Permalink to this definition">¶</a></dt>
<dd><p>The dimension map for the alarm’s associated metric (documented below). For all metrics, you can not set the dimension key as “scaling_group” or “userId”, which is set by default, the second dimension for metric, such as “device” for “PackagesNetIn”, need to be set by users.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.Alarm.enable">
<code class="sig-name descname">enable</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.Alarm.enable" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to enable specific ess alarm. Default to true.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.Alarm.evaluation_count">
<code class="sig-name descname">evaluation_count</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.Alarm.evaluation_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of times that needs to satisfies comparison condition before transition into ALARM state. Defaults to 3.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.Alarm.metric_name">
<code class="sig-name descname">metric_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.Alarm.metric_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for the alarm’s associated metric. See Block_metricNames_and_dimensions below for details.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.Alarm.metric_type">
<code class="sig-name descname">metric_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.Alarm.metric_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type for the alarm’s associated metric. Supported value: system, custom. “system” means the metric data is collected by Aliyun Cloud Monitor Service(CMS), “custom” means the metric data is upload to CMS by users. Defaults to system.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.Alarm.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.Alarm.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for ess alarm.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.Alarm.period">
<code class="sig-name descname">period</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.Alarm.period" title="Permalink to this definition">¶</a></dt>
<dd><p>The period in seconds over which the specified statistic is applied. Supported value: 60, 120, 300, 900. Defaults to 300.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.Alarm.scaling_group_id">
<code class="sig-name descname">scaling_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.Alarm.scaling_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The scaling group associated with this alarm, the ‘ForceNew’ attribute is available in 1.56.0+.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.Alarm.state">
<code class="sig-name descname">state</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.Alarm.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The state of specified alarm.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.Alarm.statistics">
<code class="sig-name descname">statistics</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.Alarm.statistics" title="Permalink to this definition">¶</a></dt>
<dd><p>The statistic to apply to the alarm’s associated metric. Supported value: Average, Minimum, Maximum. Defaults to Average.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.Alarm.threshold">
<code class="sig-name descname">threshold</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.Alarm.threshold" title="Permalink to this definition">¶</a></dt>
<dd><p>The value against which the specified statistics is compared.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ess.Alarm.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alarm_actions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cloud_monitor_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comparison_operator</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dimensions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">evaluation_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">statistics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">threshold</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.Alarm.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Alarm resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alarm_actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of actions to execute when this alarm transition into an ALARM state. Each action is specified as ess scaling rule ari.</p></li>
<li><p><strong>cloud_monitor_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Defines the application group id defined by CMS which is assigned when you upload custom metric to CMS, only available for custom metirc.</p></li>
<li><p><strong>comparison_operator</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The arithmetic operation to use when comparing the specified Statistic and Threshold. The specified Statistic value is used as the first operand. Supported value: &gt;=, &lt;=, &gt;, &lt;. Defaults to &gt;=.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description for the alarm.</p></li>
<li><p><strong>dimensions</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The dimension map for the alarm’s associated metric (documented below). For all metrics, you can not set the dimension key as “scaling_group” or “userId”, which is set by default, the second dimension for metric, such as “device” for “PackagesNetIn”, need to be set by users.</p></li>
<li><p><strong>enable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to enable specific ess alarm. Default to true.</p></li>
<li><p><strong>evaluation_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of times that needs to satisfies comparison condition before transition into ALARM state. Defaults to 3.</p></li>
<li><p><strong>metric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the alarm’s associated metric. See Block_metricNames_and_dimensions below for details.</p></li>
<li><p><strong>metric_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type for the alarm’s associated metric. Supported value: system, custom. “system” means the metric data is collected by Aliyun Cloud Monitor Service(CMS), “custom” means the metric data is upload to CMS by users. Defaults to system.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for ess alarm.</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The period in seconds over which the specified statistic is applied. Supported value: 60, 120, 300, 900. Defaults to 300.</p></li>
<li><p><strong>scaling_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The scaling group associated with this alarm, the ‘ForceNew’ attribute is available in 1.56.0+.</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The state of specified alarm.<span class="raw-html-m2r"><br></span></p></li>
<li><p><strong>statistics</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The statistic to apply to the alarm’s associated metric. Supported value: Average, Minimum, Maximum. Defaults to Average.</p></li>
<li><p><strong>threshold</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value against which the specified statistics is compared.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ess.Alarm.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.Alarm.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ess.Alarm.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.Alarm.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ess.Attachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ess.</code><code class="sig-name descname">Attachment</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.Attachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Attaches several ECS instances to a specified scaling group or remove them from it.</p>
<blockquote>
<div><p><strong>NOTE:</strong> ECS instances can be attached or remove only when the scaling group is active and it has no scaling activity in progress.</p>
<p><strong>NOTE:</strong> There are two types ECS instances in a scaling group: “AutoCreated” and “Attached”. The total number of them can not larger than the scaling group “MaxSize”.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">config</span> <span class="o">=</span> <span class="n">pulumi</span><span class="o">.</span><span class="n">Config</span><span class="p">()</span>
<span class="n">name</span> <span class="o">=</span> <span class="n">config</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">&quot;name&quot;</span><span class="p">)</span>
<span class="k">if</span> <span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
    <span class="n">name</span> <span class="o">=</span> <span class="s2">&quot;essattachmentconfig&quot;</span>
<span class="n">default_zones</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">get_zones</span><span class="p">(</span><span class="n">available_disk_category</span><span class="o">=</span><span class="s2">&quot;cloud_efficiency&quot;</span><span class="p">,</span>
    <span class="n">available_resource_creation</span><span class="o">=</span><span class="s2">&quot;VSwitch&quot;</span><span class="p">)</span>
<span class="n">default_instance_types</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">get_instance_types</span><span class="p">(</span><span class="n">availability_zone</span><span class="o">=</span><span class="n">default_zones</span><span class="o">.</span><span class="n">zones</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">cpu_core_count</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
    <span class="n">memory_size</span><span class="o">=</span><span class="mi">4</span><span class="p">)</span>
<span class="n">default_images</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">get_images</span><span class="p">(</span><span class="n">most_recent</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">name_regex</span><span class="o">=</span><span class="s2">&quot;^ubuntu_18.*64&quot;</span><span class="p">,</span>
    <span class="n">owners</span><span class="o">=</span><span class="s2">&quot;system&quot;</span><span class="p">)</span>
<span class="n">default_network</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">vpc</span><span class="o">.</span><span class="n">Network</span><span class="p">(</span><span class="s2">&quot;defaultNetwork&quot;</span><span class="p">,</span> <span class="n">cidr_block</span><span class="o">=</span><span class="s2">&quot;172.16.0.0/16&quot;</span><span class="p">)</span>
<span class="n">default_switch</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">vpc</span><span class="o">.</span><span class="n">Switch</span><span class="p">(</span><span class="s2">&quot;defaultSwitch&quot;</span><span class="p">,</span>
    <span class="n">availability_zone</span><span class="o">=</span><span class="n">default_zones</span><span class="o">.</span><span class="n">zones</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">cidr_block</span><span class="o">=</span><span class="s2">&quot;172.16.0.0/24&quot;</span><span class="p">,</span>
    <span class="n">vpc_id</span><span class="o">=</span><span class="n">default_network</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">default_security_group</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">SecurityGroup</span><span class="p">(</span><span class="s2">&quot;defaultSecurityGroup&quot;</span><span class="p">,</span> <span class="n">vpc_id</span><span class="o">=</span><span class="n">default_network</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">default_security_group_rule</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">SecurityGroupRule</span><span class="p">(</span><span class="s2">&quot;defaultSecurityGroupRule&quot;</span><span class="p">,</span>
    <span class="n">cidr_ip</span><span class="o">=</span><span class="s2">&quot;172.16.0.0/24&quot;</span><span class="p">,</span>
    <span class="n">ip_protocol</span><span class="o">=</span><span class="s2">&quot;tcp&quot;</span><span class="p">,</span>
    <span class="n">nic_type</span><span class="o">=</span><span class="s2">&quot;intranet&quot;</span><span class="p">,</span>
    <span class="n">policy</span><span class="o">=</span><span class="s2">&quot;accept&quot;</span><span class="p">,</span>
    <span class="n">port_range</span><span class="o">=</span><span class="s2">&quot;22/22&quot;</span><span class="p">,</span>
    <span class="n">priority</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">security_group_id</span><span class="o">=</span><span class="n">default_security_group</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;ingress&quot;</span><span class="p">)</span>
<span class="n">default_scaling_group</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ess</span><span class="o">.</span><span class="n">ScalingGroup</span><span class="p">(</span><span class="s2">&quot;defaultScalingGroup&quot;</span><span class="p">,</span>
    <span class="n">max_size</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
    <span class="n">min_size</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
    <span class="n">removal_policies</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;OldestInstance&quot;</span><span class="p">,</span>
        <span class="s2">&quot;NewestInstance&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">scaling_group_name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span>
    <span class="n">vswitch_ids</span><span class="o">=</span><span class="p">[</span><span class="n">default_switch</span><span class="o">.</span><span class="n">id</span><span class="p">])</span>
<span class="n">default_scaling_configuration</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ess</span><span class="o">.</span><span class="n">ScalingConfiguration</span><span class="p">(</span><span class="s2">&quot;defaultScalingConfiguration&quot;</span><span class="p">,</span>
    <span class="n">active</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">enable</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">force_delete</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">image_id</span><span class="o">=</span><span class="n">default_images</span><span class="o">.</span><span class="n">images</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">instance_type</span><span class="o">=</span><span class="n">default_instance_types</span><span class="o">.</span><span class="n">instance_types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">scaling_group_id</span><span class="o">=</span><span class="n">default_scaling_group</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">security_group_id</span><span class="o">=</span><span class="n">default_security_group</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">default_instance</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="nb">range</span> <span class="ow">in</span> <span class="p">[{</span><span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="n">i</span><span class="p">}</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">2</span><span class="p">)]:</span>
    <span class="n">default_instance</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">alicloud</span><span class="o">.</span><span class="n">ecs</span><span class="o">.</span><span class="n">Instance</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;defaultInstance-</span><span class="si">{</span><span class="nb">range</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">,</span>
        <span class="n">image_id</span><span class="o">=</span><span class="n">default_images</span><span class="o">.</span><span class="n">images</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
        <span class="n">instance_charge_type</span><span class="o">=</span><span class="s2">&quot;PostPaid&quot;</span><span class="p">,</span>
        <span class="n">instance_name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span>
        <span class="n">instance_type</span><span class="o">=</span><span class="n">default_instance_types</span><span class="o">.</span><span class="n">instance_types</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
        <span class="n">internet_charge_type</span><span class="o">=</span><span class="s2">&quot;PayByTraffic&quot;</span><span class="p">,</span>
        <span class="n">internet_max_bandwidth_out</span><span class="o">=</span><span class="s2">&quot;10&quot;</span><span class="p">,</span>
        <span class="n">security_groups</span><span class="o">=</span><span class="p">[</span><span class="n">default_security_group</span><span class="o">.</span><span class="n">id</span><span class="p">],</span>
        <span class="n">system_disk_category</span><span class="o">=</span><span class="s2">&quot;cloud_efficiency&quot;</span><span class="p">,</span>
        <span class="n">vswitch_id</span><span class="o">=</span><span class="n">default_switch</span><span class="o">.</span><span class="n">id</span><span class="p">))</span>
<span class="n">default_attachment</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ess</span><span class="o">.</span><span class="n">Attachment</span><span class="p">(</span><span class="s2">&quot;defaultAttachment&quot;</span><span class="p">,</span>
    <span class="n">force</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">instance_ids</span><span class="o">=</span><span class="p">[</span>
        <span class="n">default_instance</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
        <span class="n">default_instance</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">scaling_group_id</span><span class="o">=</span><span class="n">default_scaling_group</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>force</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to remove forcibly “AutoCreated” ECS instances in order to release scaling group capacity “MaxSize” for attaching ECS instances. Default to false.</p></li>
<li><p><strong>instance_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – ID of the ECS instance to be attached to the scaling group. You can input up to 20 IDs.</p></li>
<li><p><strong>scaling_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the scaling group of a scaling configuration.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.ess.Attachment.force">
<code class="sig-name descname">force</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.Attachment.force" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to remove forcibly “AutoCreated” ECS instances in order to release scaling group capacity “MaxSize” for attaching ECS instances. Default to false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.Attachment.instance_ids">
<code class="sig-name descname">instance_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.Attachment.instance_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the ECS instance to be attached to the scaling group. You can input up to 20 IDs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.Attachment.scaling_group_id">
<code class="sig-name descname">scaling_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.Attachment.scaling_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the scaling group of a scaling configuration.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ess.Attachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_group_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.Attachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Attachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>force</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to remove forcibly “AutoCreated” ECS instances in order to release scaling group capacity “MaxSize” for attaching ECS instances. Default to false.</p></li>
<li><p><strong>instance_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – ID of the ECS instance to be attached to the scaling group. You can input up to 20 IDs.</p></li>
<li><p><strong>scaling_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the scaling group of a scaling configuration.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ess.Attachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.Attachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ess.Attachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.Attachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ess.AwaitableGetAlarmsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ess.</code><code class="sig-name descname">AwaitableGetAlarmsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">alarms</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_group_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.AwaitableGetAlarmsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ess.AwaitableGetLifecycleHooksResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ess.</code><code class="sig-name descname">AwaitableGetLifecycleHooksResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">hooks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_group_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.AwaitableGetLifecycleHooksResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ess.AwaitableGetNotificationsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ess.</code><code class="sig-name descname">AwaitableGetNotificationsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notifications</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_group_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.AwaitableGetNotificationsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ess.AwaitableGetScalingConfigurationsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ess.</code><code class="sig-name descname">AwaitableGetScalingConfigurationsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">configurations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_group_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.AwaitableGetScalingConfigurationsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ess.AwaitableGetScalingGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ess.</code><code class="sig-name descname">AwaitableGetScalingGroupsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.AwaitableGetScalingGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ess.AwaitableGetScalingRulesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ess.</code><code class="sig-name descname">AwaitableGetScalingRulesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.AwaitableGetScalingRulesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ess.AwaitableGetScheduledTasksResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ess.</code><code class="sig-name descname">AwaitableGetScheduledTasksResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheduled_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheduled_task_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tasks</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.AwaitableGetScheduledTasksResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ess.GetAlarmsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ess.</code><code class="sig-name descname">GetAlarmsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">alarms</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_group_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.GetAlarmsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAlarms.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.ess.GetAlarmsResult.alarms">
<code class="sig-name descname">alarms</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.GetAlarmsResult.alarms" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of alarms. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.GetAlarmsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.GetAlarmsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.GetAlarmsResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.GetAlarmsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of alarm ids.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.GetAlarmsResult.metric_type">
<code class="sig-name descname">metric_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.GetAlarmsResult.metric_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type for the alarm’s associated metric.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.GetAlarmsResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.GetAlarmsResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of alarm names.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.GetAlarmsResult.scaling_group_id">
<code class="sig-name descname">scaling_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.GetAlarmsResult.scaling_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The scaling group associated with this alarm.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ess.GetLifecycleHooksResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ess.</code><code class="sig-name descname">GetLifecycleHooksResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">hooks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_group_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.GetLifecycleHooksResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getLifecycleHooks.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.ess.GetLifecycleHooksResult.hooks">
<code class="sig-name descname">hooks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.GetLifecycleHooksResult.hooks" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of lifecycle hooks. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.GetLifecycleHooksResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.GetLifecycleHooksResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.GetLifecycleHooksResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.GetLifecycleHooksResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of lifecycle hook ids.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.GetLifecycleHooksResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.GetLifecycleHooksResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of lifecycle hook names.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.GetLifecycleHooksResult.scaling_group_id">
<code class="sig-name descname">scaling_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.GetLifecycleHooksResult.scaling_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the scaling group.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ess.GetNotificationsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ess.</code><code class="sig-name descname">GetNotificationsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notifications</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_group_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.GetNotificationsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNotifications.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.ess.GetNotificationsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.GetNotificationsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.GetNotificationsResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.GetNotificationsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of notification ids.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.GetNotificationsResult.notifications">
<code class="sig-name descname">notifications</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.GetNotificationsResult.notifications" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of notifications. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.GetNotificationsResult.scaling_group_id">
<code class="sig-name descname">scaling_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.GetNotificationsResult.scaling_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the scaling group.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ess.GetScalingConfigurationsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ess.</code><code class="sig-name descname">GetScalingConfigurationsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">configurations</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_group_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.GetScalingConfigurationsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getScalingConfigurations.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.ess.GetScalingConfigurationsResult.configurations">
<code class="sig-name descname">configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.GetScalingConfigurationsResult.configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of scaling rules. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.GetScalingConfigurationsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.GetScalingConfigurationsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.GetScalingConfigurationsResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.GetScalingConfigurationsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of scaling configuration ids.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.GetScalingConfigurationsResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.GetScalingConfigurationsResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of scaling configuration names.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.GetScalingConfigurationsResult.scaling_group_id">
<code class="sig-name descname">scaling_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.GetScalingConfigurationsResult.scaling_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the scaling group.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ess.GetScalingGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ess.</code><code class="sig-name descname">GetScalingGroupsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.GetScalingGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getScalingGroups.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.ess.GetScalingGroupsResult.groups">
<code class="sig-name descname">groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.GetScalingGroupsResult.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of scaling groups. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.GetScalingGroupsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.GetScalingGroupsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.GetScalingGroupsResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.GetScalingGroupsResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of scaling group ids.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.GetScalingGroupsResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.GetScalingGroupsResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of scaling group names.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ess.GetScalingRulesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ess.</code><code class="sig-name descname">GetScalingRulesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.GetScalingRulesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getScalingRules.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.ess.GetScalingRulesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.GetScalingRulesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.GetScalingRulesResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.GetScalingRulesResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of scaling rule ids.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.GetScalingRulesResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.GetScalingRulesResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of scaling rule names.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.GetScalingRulesResult.rules">
<code class="sig-name descname">rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.GetScalingRulesResult.rules" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of scaling rules. Each element contains the following attributes:</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.GetScalingRulesResult.scaling_group_id">
<code class="sig-name descname">scaling_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.GetScalingRulesResult.scaling_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the scaling group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.GetScalingRulesResult.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.GetScalingRulesResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of the scaling rule.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ess.GetScheduledTasksResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ess.</code><code class="sig-name descname">GetScheduledTasksResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheduled_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheduled_task_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tasks</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.GetScheduledTasksResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getScheduledTasks.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.ess.GetScheduledTasksResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.GetScheduledTasksResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.GetScheduledTasksResult.ids">
<code class="sig-name descname">ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.GetScheduledTasksResult.ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of scheduled task ids.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.GetScheduledTasksResult.names">
<code class="sig-name descname">names</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.GetScheduledTasksResult.names" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of scheduled task names.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.GetScheduledTasksResult.scheduled_action">
<code class="sig-name descname">scheduled_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.GetScheduledTasksResult.scheduled_action" title="Permalink to this definition">¶</a></dt>
<dd><p>The operation to be performed when a scheduled task is triggered.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.GetScheduledTasksResult.tasks">
<code class="sig-name descname">tasks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.GetScheduledTasksResult.tasks" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of scheduled tasks. Each element contains the following attributes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_alicloud.ess.LifecycleHook">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ess.</code><code class="sig-name descname">LifecycleHook</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_result</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">heartbeat_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lifecycle_transition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_metadata</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.LifecycleHook" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a LifecycleHook resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] default_result: Defines the action the Auto Scaling group should take when the lifecycle hook timeout elapses. Applicable value: CONTINUE, ABANDON, default value: CONTINUE.
:param pulumi.Input[float] heartbeat_timeout: Defines the amount of time, in seconds, that can elapse before the lifecycle hook times out. When the lifecycle hook times out, Auto Scaling performs the action defined in the default_result parameter. Default value: 600.
:param pulumi.Input[str] lifecycle_transition: Type of Scaling activity attached to lifecycle hook. Supported value: SCALE_OUT, SCALE<em>IN.
:param pulumi.Input[str] name: The name of the lifecycle hook, which must contain 2-64 characters (English or Chinese), starting with numbers, English letters or Chinese characters, and can contain number, underscores `</em><code class="docutils literal notranslate"><span class="pre">,</span> <span class="pre">hypens</span></code>-<code class="docutils literal notranslate"><span class="pre">,</span> <span class="pre">and</span> <span class="pre">decimal</span> <span class="pre">point</span></code>.`. If this parameter value is not specified, the default value is lifecycle hook id.
:param pulumi.Input[str] notification_arn: The Arn of notification target.
:param pulumi.Input[str] notification_metadata: Additional information that you want to include when Auto Scaling sends a message to the notification target.
:param pulumi.Input[str] scaling_group_id: The ID of the Auto Scaling group to which you want to assign the lifecycle hook.</p>
<dl class="py attribute">
<dt id="pulumi_alicloud.ess.LifecycleHook.default_result">
<code class="sig-name descname">default_result</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.LifecycleHook.default_result" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines the action the Auto Scaling group should take when the lifecycle hook timeout elapses. Applicable value: CONTINUE, ABANDON, default value: CONTINUE.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.LifecycleHook.heartbeat_timeout">
<code class="sig-name descname">heartbeat_timeout</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.LifecycleHook.heartbeat_timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines the amount of time, in seconds, that can elapse before the lifecycle hook times out. When the lifecycle hook times out, Auto Scaling performs the action defined in the default_result parameter. Default value: 600.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.LifecycleHook.lifecycle_transition">
<code class="sig-name descname">lifecycle_transition</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.LifecycleHook.lifecycle_transition" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of Scaling activity attached to lifecycle hook. Supported value: SCALE_OUT, SCALE_IN.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.LifecycleHook.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.LifecycleHook.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the lifecycle hook, which must contain 2-64 characters (English or Chinese), starting with numbers, English letters or Chinese characters, and can contain number, underscores <code class="docutils literal notranslate"><span class="pre">_</span></code>, hypens <code class="docutils literal notranslate"><span class="pre">-</span></code>, and decimal point <code class="docutils literal notranslate"><span class="pre">.</span></code>. If this parameter value is not specified, the default value is lifecycle hook id.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.LifecycleHook.notification_arn">
<code class="sig-name descname">notification_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.LifecycleHook.notification_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Arn of notification target.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.LifecycleHook.notification_metadata">
<code class="sig-name descname">notification_metadata</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.LifecycleHook.notification_metadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Additional information that you want to include when Auto Scaling sends a message to the notification target.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.LifecycleHook.scaling_group_id">
<code class="sig-name descname">scaling_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.LifecycleHook.scaling_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Auto Scaling group to which you want to assign the lifecycle hook.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ess.LifecycleHook.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_result</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">heartbeat_timeout</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lifecycle_transition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_metadata</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_group_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.LifecycleHook.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LifecycleHook resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_result</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines the action the Auto Scaling group should take when the lifecycle hook timeout elapses. Applicable value: CONTINUE, ABANDON, default value: CONTINUE.</p></li>
<li><p><strong>heartbeat_timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Defines the amount of time, in seconds, that can elapse before the lifecycle hook times out. When the lifecycle hook times out, Auto Scaling performs the action defined in the default_result parameter. Default value: 600.</p></li>
<li><p><strong>lifecycle_transition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of Scaling activity attached to lifecycle hook. Supported value: SCALE_OUT, SCALE<a href="#id1"><span class="problematic" id="id2">*</span></a>IN.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the lifecycle hook, which must contain 2-64 characters (English or Chinese), starting with numbers, English letters or Chinese characters, and can contain number, underscores <cite>*`</cite>, hypens``-<code class="docutils literal notranslate"><span class="pre">,</span> <span class="pre">and</span> <span class="pre">decimal</span> <span class="pre">point</span></code>.`. If this parameter value is not specified, the default value is lifecycle hook id.</p></li>
<li><p><strong>notification_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Arn of notification target.</p></li>
<li><p><strong>notification_metadata</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Additional information that you want to include when Auto Scaling sends a message to the notification target.</p></li>
<li><p><strong>scaling_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Auto Scaling group to which you want to assign the lifecycle hook.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ess.LifecycleHook.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.LifecycleHook.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ess.LifecycleHook.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.LifecycleHook.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ess.Notification">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ess.</code><code class="sig-name descname">Notification</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.Notification" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a ESS notification resource. More about Ess notification, see <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/71114.htm">Autoscaling Notification</a>.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.55.0+</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">config</span> <span class="o">=</span> <span class="n">pulumi</span><span class="o">.</span><span class="n">Config</span><span class="p">()</span>
<span class="n">name</span> <span class="o">=</span> <span class="n">config</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">&quot;name&quot;</span><span class="p">)</span>
<span class="k">if</span> <span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
    <span class="n">name</span> <span class="o">=</span> <span class="s2">&quot;tf-testAccEssNotification-</span><span class="si">%d</span><span class="s2">&quot;</span>
<span class="n">default_regions</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">get_regions</span><span class="p">(</span><span class="n">current</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">default_account</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">get_account</span><span class="p">()</span>
<span class="n">default_zones</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">get_zones</span><span class="p">(</span><span class="n">available_disk_category</span><span class="o">=</span><span class="s2">&quot;cloud_efficiency&quot;</span><span class="p">,</span>
    <span class="n">available_resource_creation</span><span class="o">=</span><span class="s2">&quot;VSwitch&quot;</span><span class="p">)</span>
<span class="n">default_network</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">vpc</span><span class="o">.</span><span class="n">Network</span><span class="p">(</span><span class="s2">&quot;defaultNetwork&quot;</span><span class="p">,</span> <span class="n">cidr_block</span><span class="o">=</span><span class="s2">&quot;172.16.0.0/16&quot;</span><span class="p">)</span>
<span class="n">default_switch</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">vpc</span><span class="o">.</span><span class="n">Switch</span><span class="p">(</span><span class="s2">&quot;defaultSwitch&quot;</span><span class="p">,</span>
    <span class="n">availability_zone</span><span class="o">=</span><span class="n">default_zones</span><span class="o">.</span><span class="n">zones</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">cidr_block</span><span class="o">=</span><span class="s2">&quot;172.16.0.0/24&quot;</span><span class="p">,</span>
    <span class="n">vpc_id</span><span class="o">=</span><span class="n">default_network</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">default_scaling_group</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ess</span><span class="o">.</span><span class="n">ScalingGroup</span><span class="p">(</span><span class="s2">&quot;defaultScalingGroup&quot;</span><span class="p">,</span>
    <span class="n">max_size</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">min_size</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">removal_policies</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;OldestInstance&quot;</span><span class="p">,</span>
        <span class="s2">&quot;NewestInstance&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">scaling_group_name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span>
    <span class="n">vswitch_ids</span><span class="o">=</span><span class="p">[</span><span class="n">default_switch</span><span class="o">.</span><span class="n">id</span><span class="p">])</span>
<span class="n">default_queue</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">mns</span><span class="o">.</span><span class="n">Queue</span><span class="p">(</span><span class="s2">&quot;defaultQueue&quot;</span><span class="p">)</span>
<span class="n">default_notification</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ess</span><span class="o">.</span><span class="n">Notification</span><span class="p">(</span><span class="s2">&quot;defaultNotification&quot;</span><span class="p">,</span>
    <span class="n">notification_arn</span><span class="o">=</span><span class="n">default_queue</span><span class="o">.</span><span class="n">name</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">name</span><span class="p">:</span> <span class="sa">f</span><span class="s2">&quot;acs:ess:</span><span class="si">{</span><span class="n">default_regions</span><span class="o">.</span><span class="n">regions</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s1">&#39;id&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">:</span><span class="si">{</span><span class="n">default_account</span><span class="o">.</span><span class="n">id</span><span class="si">}</span><span class="s2">:queue/</span><span class="si">{</span><span class="n">name</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">),</span>
    <span class="n">notification_types</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;AUTOSCALING:SCALE_OUT_SUCCESS&quot;</span><span class="p">,</span>
        <span class="s2">&quot;AUTOSCALING:SCALE_OUT_ERROR&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">scaling_group_id</span><span class="o">=</span><span class="n">default_scaling_group</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>notification_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Alibaba Cloud Resource Name (ARN) of the notification object, The value must be in <code class="docutils literal notranslate"><span class="pre">acs:ess:{region}:{account-id}:{resource-relative-id}</span></code> format.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* region: the region ID of the scaling group. For more information, see `Regions and zones`
* account-id: the ID of your account.
* resource-relative-id: the notification method. Valid values : `cloudmonitor`, MNS queue: `queue/{queuename}`, Replace the queuename with the specific MNS queue name, MNS topic: `topic/{topicname}`, Replace the topicname with the specific MNS topic name.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>notification_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The notification types of Auto Scaling events and resource changes. Supported notification types: ‘AUTOSCALING:SCALE_OUT_SUCCESS’, ‘AUTOSCALING:SCALE_IN_SUCCESS’, ‘AUTOSCALING:SCALE_OUT_ERROR’, ‘AUTOSCALING:SCALE_IN_ERROR’, ‘AUTOSCALING:SCALE_REJECT’, ‘AUTOSCALING:SCALE_OUT_START’, ‘AUTOSCALING:SCALE_IN_START’, ‘AUTOSCALING:SCHEDULE_TASK_EXPIRING’.</p></li>
<li><p><strong>scaling_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Auto Scaling group.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.ess.Notification.notification_arn">
<code class="sig-name descname">notification_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.Notification.notification_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The Alibaba Cloud Resource Name (ARN) of the notification object, The value must be in <code class="docutils literal notranslate"><span class="pre">acs:ess:{region}:{account-id}:{resource-relative-id}</span></code> format.</p>
<ul class="simple">
<li><p>region: the region ID of the scaling group. For more information, see <code class="docutils literal notranslate"><span class="pre">Regions</span> <span class="pre">and</span> <span class="pre">zones</span></code></p></li>
<li><p>account-id: the ID of your account.</p></li>
<li><p>resource-relative-id: the notification method. Valid values : <code class="docutils literal notranslate"><span class="pre">cloudmonitor</span></code>, MNS queue: <code class="docutils literal notranslate"><span class="pre">queue/{queuename}</span></code>, Replace the queuename with the specific MNS queue name, MNS topic: <code class="docutils literal notranslate"><span class="pre">topic/{topicname}</span></code>, Replace the topicname with the specific MNS topic name.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.Notification.notification_types">
<code class="sig-name descname">notification_types</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.Notification.notification_types" title="Permalink to this definition">¶</a></dt>
<dd><p>The notification types of Auto Scaling events and resource changes. Supported notification types: ‘AUTOSCALING:SCALE_OUT_SUCCESS’, ‘AUTOSCALING:SCALE_IN_SUCCESS’, ‘AUTOSCALING:SCALE_OUT_ERROR’, ‘AUTOSCALING:SCALE_IN_ERROR’, ‘AUTOSCALING:SCALE_REJECT’, ‘AUTOSCALING:SCALE_OUT_START’, ‘AUTOSCALING:SCALE_IN_START’, ‘AUTOSCALING:SCHEDULE_TASK_EXPIRING’.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.Notification.scaling_group_id">
<code class="sig-name descname">scaling_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.Notification.scaling_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Auto Scaling group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ess.Notification.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_group_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.Notification.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Notification resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>notification_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Alibaba Cloud Resource Name (ARN) of the notification object, The value must be in <code class="docutils literal notranslate"><span class="pre">acs:ess:{region}:{account-id}:{resource-relative-id}</span></code> format.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* region: the region ID of the scaling group. For more information, see `Regions and zones`
* account-id: the ID of your account.
* resource-relative-id: the notification method. Valid values : `cloudmonitor`, MNS queue: `queue/{queuename}`, Replace the queuename with the specific MNS queue name, MNS topic: `topic/{topicname}`, Replace the topicname with the specific MNS topic name.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>notification_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The notification types of Auto Scaling events and resource changes. Supported notification types: ‘AUTOSCALING:SCALE_OUT_SUCCESS’, ‘AUTOSCALING:SCALE_IN_SUCCESS’, ‘AUTOSCALING:SCALE_OUT_ERROR’, ‘AUTOSCALING:SCALE_IN_ERROR’, ‘AUTOSCALING:SCALE_REJECT’, ‘AUTOSCALING:SCALE_OUT_START’, ‘AUTOSCALING:SCALE_IN_START’, ‘AUTOSCALING:SCHEDULE_TASK_EXPIRING’.</p></li>
<li><p><strong>scaling_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Auto Scaling group.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ess.Notification.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.Notification.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ess.Notification.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.Notification.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ess.ScalingConfiguration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ess.</code><code class="sig-name descname">ScalingConfiguration</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">active</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_disks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_delete</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internet_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internet_max_bandwidth_in</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internet_max_bandwidth_out</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">io_optimized</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_outdated</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_encrypted_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_encryption_context</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">override</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_inherit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_configuration_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">substitute</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_disk_auto_snapshot_policy_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_disk_category</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_disk_description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_disk_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_disk_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ScalingConfiguration resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] active: Whether active current scaling configuration in the specified scaling group. Default to <code class="docutils literal notranslate"><span class="pre">false</span></code>.
:param pulumi.Input[list] data_disks: DataDisk mappings to attach to ecs instance. See Block datadisk below for details.
:param pulumi.Input[bool] enable: Whether enable the specified scaling group(make it active) to which the current scaling configuration belongs.
:param pulumi.Input[bool] force_delete: The last scaling configuration will be deleted forcibly with deleting its scaling group. Default to false.
:param pulumi.Input[str] image_id: ID of an image file, indicating the image resource selected when an instance is enabled.
:param pulumi.Input[str] image_name: Name of an image file, indicating the image resource selected when an instance is enabled.
:param pulumi.Input[list] instance_ids: It has been deprecated from version 1.6.0. New resource <code class="docutils literal notranslate"><span class="pre">ess.Attachment</span></code> replaces it.
:param pulumi.Input[str] instance_name: Name of an ECS instance. Default to “ESS-Instance”. It is valid from version 1.7.1.
:param pulumi.Input[str] instance_type: Resource type of an ECS instance.
:param pulumi.Input[list] instance_types: Resource types of an ECS instance.
:param pulumi.Input[str] internet_charge_type: Network billing type, Values: PayByBandwidth or PayByTraffic. Default to <code class="docutils literal notranslate"><span class="pre">PayByBandwidth</span></code>.
:param pulumi.Input[float] internet_max_bandwidth_in: Maximum incoming bandwidth from the public network, measured in Mbps (Mega bit per second). The value range is [1,200].
:param pulumi.Input[float] internet_max_bandwidth_out: Maximum outgoing bandwidth from the public network, measured in Mbps (Mega bit per second). The value range for PayByBandwidth is [0,100].
:param pulumi.Input[str] io_optimized: It has been deprecated on instance resource. All the launched alicloud instances will be I/O optimized.
:param pulumi.Input[bool] is_outdated: Whether to use outdated instance type. Default to false.
:param pulumi.Input[str] key_name: The name of key pair that can login ECS instance successfully without password. If it is specified, the password would be invalid.
:param pulumi.Input[str] kms_encrypted_password: An KMS encrypts password used to a db account. If the <code class="docutils literal notranslate"><span class="pre">password</span></code> is filled in, this field will be ignored.
:param pulumi.Input[dict] kms_encryption_context: An KMS encryption context used to decrypt <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> before creating or updating a db account with <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code>. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>. It is valid when <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> is set.
:param pulumi.Input[bool] override: Indicates whether to overwrite the existing data. Default to false.
:param pulumi.Input[str] password: The password of the ECS instance. The password must be 8 to 30 characters in length. It must contains at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include <code class="docutils literal notranslate"><span class="pre">()</span> <span class="pre">~!&#64;#$%^&amp;*-_+=\|{}[]:;'&lt;&gt;,.?/</span></code>, The password of Windows-based instances cannot start with a forward slash (/).
:param pulumi.Input[bool] password_inherit: Specifies whether to use the password that is predefined in the image. If the PasswordInherit parameter is set to true, the <code class="docutils literal notranslate"><span class="pre">password</span></code> and <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> will be ignored. You must ensure that the selected image has a password configured.
:param pulumi.Input[str] role_name: Instance RAM role name. The name is provided and maintained by RAM. You can use <code class="docutils literal notranslate"><span class="pre">ram.Role</span></code> to create a new one.
:param pulumi.Input[str] scaling_configuration<em>name: Name shown for the scheduled task. which must contain 2-64 characters (English or Chinese), starting with numbers, English letters or Chinese characters, and can contain number, underscores `</em><code class="docutils literal notranslate"><span class="pre">,</span> <span class="pre">hypens</span></code>-<code class="docutils literal notranslate"><span class="pre">,</span> <span class="pre">and</span> <span class="pre">decimal</span> <span class="pre">point</span></code>.<code class="docutils literal notranslate"><span class="pre">.</span> <span class="pre">If</span> <span class="pre">this</span> <span class="pre">parameter</span> <span class="pre">value</span> <span class="pre">is</span> <span class="pre">not</span> <span class="pre">specified,</span> <span class="pre">the</span> <span class="pre">default</span> <span class="pre">value</span> <span class="pre">is</span> <span class="pre">ScalingConfigurationId.</span>
<span class="pre">:param</span> <span class="pre">pulumi.Input[str]</span> <span class="pre">scaling_group_id:</span> <span class="pre">ID</span> <span class="pre">of</span> <span class="pre">the</span> <span class="pre">scaling</span> <span class="pre">group</span> <span class="pre">of</span> <span class="pre">a</span> <span class="pre">scaling</span> <span class="pre">configuration.</span>
<span class="pre">:param</span> <span class="pre">pulumi.Input[str]</span> <span class="pre">security_group_id:</span> <span class="pre">ID</span> <span class="pre">of</span> <span class="pre">the</span> <span class="pre">security</span> <span class="pre">group</span> <span class="pre">used</span> <span class="pre">to</span> <span class="pre">create</span> <span class="pre">new</span> <span class="pre">instance.</span> <span class="pre">It</span> <span class="pre">is</span> <span class="pre">conflict</span> <span class="pre">with</span></code>security_group_ids<code class="docutils literal notranslate"><span class="pre">.</span>
<span class="pre">:param</span> <span class="pre">pulumi.Input[list]</span> <span class="pre">security_group_ids:</span> <span class="pre">List</span> <span class="pre">IDs</span> <span class="pre">of</span> <span class="pre">the</span> <span class="pre">security</span> <span class="pre">group</span> <span class="pre">used</span> <span class="pre">to</span> <span class="pre">create</span> <span class="pre">new</span> <span class="pre">instances.</span> <span class="pre">It</span> <span class="pre">is</span> <span class="pre">conflict</span> <span class="pre">with</span></code>security_group_id<code class="docutils literal notranslate"><span class="pre">.</span>
<span class="pre">:param</span> <span class="pre">pulumi.Input[str]</span> <span class="pre">substitute:</span> <span class="pre">The</span> <span class="pre">another</span> <span class="pre">scaling</span> <span class="pre">configuration</span> <span class="pre">which</span> <span class="pre">will</span> <span class="pre">be</span> <span class="pre">active</span> <span class="pre">automatically</span> <span class="pre">and</span> <span class="pre">replace</span> <span class="pre">current</span> <span class="pre">configuration</span> <span class="pre">when</span> <span class="pre">setting</span></code>active<code class="docutils literal notranslate"><span class="pre">to</span> <span class="pre">'false'.</span> <span class="pre">It</span> <span class="pre">is</span> <span class="pre">invalid</span> <span class="pre">when</span></code>active<code class="docutils literal notranslate"><span class="pre">is</span> <span class="pre">'true'.</span>
<span class="pre">:param</span> <span class="pre">pulumi.Input[str]</span> <span class="pre">system_disk_auto_snapshot_policy_id:</span> <span class="pre">The</span> <span class="pre">id</span> <span class="pre">of</span> <span class="pre">auto</span> <span class="pre">snapshot</span> <span class="pre">policy</span> <span class="pre">for</span> <span class="pre">system</span> <span class="pre">disk.</span>
<span class="pre">:param</span> <span class="pre">pulumi.Input[str]</span> <span class="pre">system_disk_category:</span> <span class="pre">Category</span> <span class="pre">of</span> <span class="pre">the</span> <span class="pre">system</span> <span class="pre">disk.</span> <span class="pre">The</span> <span class="pre">parameter</span> <span class="pre">value</span> <span class="pre">options</span> <span class="pre">are</span></code>ephemeral_ssd<code class="docutils literal notranslate"><span class="pre">,</span></code>cloud_efficiency<code class="docutils literal notranslate"><span class="pre">,</span></code>cloud_ssd<code class="docutils literal notranslate"><span class="pre">,</span></code>cloud_essd<code class="docutils literal notranslate"><span class="pre">and</span></code>cloud<code class="docutils literal notranslate"><span class="pre">.</span></code>cloud<code class="docutils literal notranslate"><span class="pre">only</span> <span class="pre">is</span> <span class="pre">used</span> <span class="pre">to</span> <span class="pre">some</span> <span class="pre">no</span> <span class="pre">I/O</span> <span class="pre">optimized</span> <span class="pre">instance.</span> <span class="pre">Default</span> <span class="pre">to</span></code>cloud_efficiency`.
:param pulumi.Input[str] system_disk_description: The description of the system disk. The description must be 2 to 256 characters in length and cannot start with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>.
:param pulumi.Input[str] system_disk<em>name: The name of the system disk. It must be 2 to 128 characters in length. It must start with a letter and cannot start with http:// or https://. It can contain letters, digits, colons (:), underscores (</em>), and hyphens (-). Default value: null.
:param pulumi.Input[float] system_disk_size: Size of system disk, in GiB. Optional values: cloud: 20-500, cloud_efficiency: 20-500, cloud_ssd: 20-500, ephemeral_ssd: 20-500 The default value is max{40, ImageSize}. If this parameter is set, the system disk size must be greater than or equal to max{40, ImageSize}.
:param pulumi.Input[dict] tags: A mapping of tags to assign to the resource. It will be applied for ECS instances finally.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">Key</span><span class="p">:</span> <span class="n">It</span> <span class="n">can</span> <span class="n">be</span> <span class="n">up</span> <span class="n">to</span> <span class="mi">64</span> <span class="n">characters</span> <span class="ow">in</span> <span class="n">length</span><span class="o">.</span> <span class="n">It</span> <span class="n">cannot</span> <span class="n">begin</span> <span class="k">with</span> <span class="s2">&quot;aliyun&quot;</span><span class="p">,</span> <span class="s2">&quot;http://&quot;</span><span class="p">,</span> <span class="ow">or</span> <span class="s2">&quot;https://&quot;</span><span class="o">.</span> <span class="n">It</span> <span class="n">cannot</span> <span class="n">be</span> <span class="n">a</span> <span class="n">null</span> <span class="n">string</span><span class="o">.</span>
<span class="o">-</span> <span class="n">Value</span><span class="p">:</span> <span class="n">It</span> <span class="n">can</span> <span class="n">be</span> <span class="n">up</span> <span class="n">to</span> <span class="mi">128</span> <span class="n">characters</span> <span class="ow">in</span> <span class="n">length</span><span class="o">.</span> <span class="n">It</span> <span class="n">cannot</span> <span class="n">begin</span> <span class="k">with</span> <span class="s2">&quot;aliyun&quot;</span><span class="p">,</span> <span class="s2">&quot;http://&quot;</span><span class="p">,</span> <span class="ow">or</span> <span class="s2">&quot;https://&quot;</span> <span class="n">It</span> <span class="n">can</span> <span class="n">be</span> <span class="n">a</span> <span class="n">null</span> <span class="n">string</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User-defined data to customize the startup behaviors of the ECS instance and to pass data into the ECS instance.</p>
</dd>
</dl>
<p>The <strong>data_disks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoSnapshotPolicyId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">delete_with_instance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">device</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snapshot_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingConfiguration.active">
<code class="sig-name descname">active</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration.active" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether active current scaling configuration in the specified scaling group. Default to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingConfiguration.data_disks">
<code class="sig-name descname">data_disks</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration.data_disks" title="Permalink to this definition">¶</a></dt>
<dd><p>DataDisk mappings to attach to ecs instance. See Block datadisk below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoSnapshotPolicyId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">delete_with_instance</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">device</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snapshot_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingConfiguration.enable">
<code class="sig-name descname">enable</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration.enable" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether enable the specified scaling group(make it active) to which the current scaling configuration belongs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingConfiguration.force_delete">
<code class="sig-name descname">force_delete</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration.force_delete" title="Permalink to this definition">¶</a></dt>
<dd><p>The last scaling configuration will be deleted forcibly with deleting its scaling group. Default to false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingConfiguration.image_id">
<code class="sig-name descname">image_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration.image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of an image file, indicating the image resource selected when an instance is enabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingConfiguration.image_name">
<code class="sig-name descname">image_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration.image_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of an image file, indicating the image resource selected when an instance is enabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingConfiguration.instance_ids">
<code class="sig-name descname">instance_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration.instance_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>It has been deprecated from version 1.6.0. New resource <code class="docutils literal notranslate"><span class="pre">ess.Attachment</span></code> replaces it.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingConfiguration.instance_name">
<code class="sig-name descname">instance_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration.instance_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of an ECS instance. Default to “ESS-Instance”. It is valid from version 1.7.1.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingConfiguration.instance_type">
<code class="sig-name descname">instance_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration.instance_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource type of an ECS instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingConfiguration.instance_types">
<code class="sig-name descname">instance_types</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration.instance_types" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource types of an ECS instance.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingConfiguration.internet_charge_type">
<code class="sig-name descname">internet_charge_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration.internet_charge_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Network billing type, Values: PayByBandwidth or PayByTraffic. Default to <code class="docutils literal notranslate"><span class="pre">PayByBandwidth</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingConfiguration.internet_max_bandwidth_in">
<code class="sig-name descname">internet_max_bandwidth_in</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration.internet_max_bandwidth_in" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum incoming bandwidth from the public network, measured in Mbps (Mega bit per second). The value range is [1,200].</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingConfiguration.internet_max_bandwidth_out">
<code class="sig-name descname">internet_max_bandwidth_out</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration.internet_max_bandwidth_out" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum outgoing bandwidth from the public network, measured in Mbps (Mega bit per second). The value range for PayByBandwidth is [0,100].</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingConfiguration.io_optimized">
<code class="sig-name descname">io_optimized</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration.io_optimized" title="Permalink to this definition">¶</a></dt>
<dd><p>It has been deprecated on instance resource. All the launched alicloud instances will be I/O optimized.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingConfiguration.is_outdated">
<code class="sig-name descname">is_outdated</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration.is_outdated" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to use outdated instance type. Default to false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingConfiguration.key_name">
<code class="sig-name descname">key_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration.key_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of key pair that can login ECS instance successfully without password. If it is specified, the password would be invalid.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingConfiguration.kms_encrypted_password">
<code class="sig-name descname">kms_encrypted_password</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration.kms_encrypted_password" title="Permalink to this definition">¶</a></dt>
<dd><p>An KMS encrypts password used to a db account. If the <code class="docutils literal notranslate"><span class="pre">password</span></code> is filled in, this field will be ignored.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingConfiguration.kms_encryption_context">
<code class="sig-name descname">kms_encryption_context</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration.kms_encryption_context" title="Permalink to this definition">¶</a></dt>
<dd><p>An KMS encryption context used to decrypt <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> before creating or updating a db account with <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code>. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>. It is valid when <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> is set.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingConfiguration.override">
<code class="sig-name descname">override</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration.override" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether to overwrite the existing data. Default to false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingConfiguration.password">
<code class="sig-name descname">password</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password of the ECS instance. The password must be 8 to 30 characters in length. It must contains at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include <code class="docutils literal notranslate"><span class="pre">()</span> <span class="pre">~!&#64;#$%^&amp;*-_+=\|{}[]:;'&lt;&gt;,.?/</span></code>, The password of Windows-based instances cannot start with a forward slash (/).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingConfiguration.password_inherit">
<code class="sig-name descname">password_inherit</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration.password_inherit" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether to use the password that is predefined in the image. If the PasswordInherit parameter is set to true, the <code class="docutils literal notranslate"><span class="pre">password</span></code> and <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> will be ignored. You must ensure that the selected image has a password configured.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingConfiguration.role_name">
<code class="sig-name descname">role_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration.role_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Instance RAM role name. The name is provided and maintained by RAM. You can use <code class="docutils literal notranslate"><span class="pre">ram.Role</span></code> to create a new one.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingConfiguration.scaling_configuration_name">
<code class="sig-name descname">scaling_configuration_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration.scaling_configuration_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name shown for the scheduled task. which must contain 2-64 characters (English or Chinese), starting with numbers, English letters or Chinese characters, and can contain number, underscores <code class="docutils literal notranslate"><span class="pre">_</span></code>, hypens <code class="docutils literal notranslate"><span class="pre">-</span></code>, and decimal point <code class="docutils literal notranslate"><span class="pre">.</span></code>. If this parameter value is not specified, the default value is ScalingConfigurationId.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingConfiguration.scaling_group_id">
<code class="sig-name descname">scaling_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration.scaling_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the scaling group of a scaling configuration.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingConfiguration.security_group_id">
<code class="sig-name descname">security_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration.security_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the security group used to create new instance. It is conflict with <code class="docutils literal notranslate"><span class="pre">security_group_ids</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingConfiguration.security_group_ids">
<code class="sig-name descname">security_group_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration.security_group_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>List IDs of the security group used to create new instances. It is conflict with <code class="docutils literal notranslate"><span class="pre">security_group_id</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingConfiguration.substitute">
<code class="sig-name descname">substitute</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration.substitute" title="Permalink to this definition">¶</a></dt>
<dd><p>The another scaling configuration which will be active automatically and replace current configuration when setting <code class="docutils literal notranslate"><span class="pre">active</span></code> to ‘false’. It is invalid when <code class="docutils literal notranslate"><span class="pre">active</span></code> is ‘true’.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingConfiguration.system_disk_auto_snapshot_policy_id">
<code class="sig-name descname">system_disk_auto_snapshot_policy_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration.system_disk_auto_snapshot_policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of auto snapshot policy for system disk.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingConfiguration.system_disk_category">
<code class="sig-name descname">system_disk_category</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration.system_disk_category" title="Permalink to this definition">¶</a></dt>
<dd><p>Category of the system disk. The parameter value options are <code class="docutils literal notranslate"><span class="pre">ephemeral_ssd</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_ssd</span></code>, <code class="docutils literal notranslate"><span class="pre">cloud_essd</span></code> and <code class="docutils literal notranslate"><span class="pre">cloud</span></code>. <code class="docutils literal notranslate"><span class="pre">cloud</span></code> only is used to some no I/O optimized instance. Default to <code class="docutils literal notranslate"><span class="pre">cloud_efficiency</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingConfiguration.system_disk_description">
<code class="sig-name descname">system_disk_description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration.system_disk_description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the system disk. The description must be 2 to 256 characters in length and cannot start with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingConfiguration.system_disk_name">
<code class="sig-name descname">system_disk_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration.system_disk_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the system disk. It must be 2 to 128 characters in length. It must start with a letter and cannot start with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>. It can contain letters, digits, colons (:), underscores (_), and hyphens (-). Default value: null.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingConfiguration.system_disk_size">
<code class="sig-name descname">system_disk_size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration.system_disk_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Size of system disk, in GiB. Optional values: cloud: 20-500, cloud_efficiency: 20-500, cloud_ssd: 20-500, ephemeral_ssd: 20-500 The default value is max{40, ImageSize}. If this parameter is set, the system disk size must be greater than or equal to max{40, ImageSize}.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingConfiguration.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource. It will be applied for ECS instances finally.</p>
<ul class="simple">
<li><p>Key: It can be up to 64 characters in length. It cannot begin with “aliyun”, “<a class="reference external" href="http://">http://</a>”, or “<a class="reference external" href="https://">https://</a>”. It cannot be a null string.</p></li>
<li><p>Value: It can be up to 128 characters in length. It cannot begin with “aliyun”, “<a class="reference external" href="http://">http://</a>”, or “<a class="reference external" href="https://">https://</a>” It can be a null string.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingConfiguration.user_data">
<code class="sig-name descname">user_data</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration.user_data" title="Permalink to this definition">¶</a></dt>
<dd><p>User-defined data to customize the startup behaviors of the ECS instance and to pass data into the ECS instance.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ess.ScalingConfiguration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">active</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">data_disks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_delete</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">image_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internet_charge_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internet_max_bandwidth_in</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">internet_max_bandwidth_out</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">io_optimized</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_outdated</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_encrypted_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kms_encryption_context</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">override</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_inherit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_configuration_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">security_group_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">substitute</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_disk_auto_snapshot_policy_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_disk_category</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_disk_description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_disk_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">system_disk_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_data</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ScalingConfiguration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>active</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether active current scaling configuration in the specified scaling group. Default to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>data_disks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – DataDisk mappings to attach to ecs instance. See Block datadisk below for details.</p></li>
<li><p><strong>enable</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether enable the specified scaling group(make it active) to which the current scaling configuration belongs.</p></li>
<li><p><strong>force_delete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The last scaling configuration will be deleted forcibly with deleting its scaling group. Default to false.</p></li>
<li><p><strong>image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of an image file, indicating the image resource selected when an instance is enabled.</p></li>
<li><p><strong>image_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an image file, indicating the image resource selected when an instance is enabled.</p></li>
<li><p><strong>instance_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – It has been deprecated from version 1.6.0. New resource <code class="docutils literal notranslate"><span class="pre">ess.Attachment</span></code> replaces it.</p></li>
<li><p><strong>instance_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of an ECS instance. Default to “ESS-Instance”. It is valid from version 1.7.1.</p></li>
<li><p><strong>instance_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource type of an ECS instance.</p></li>
<li><p><strong>instance_types</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Resource types of an ECS instance.</p></li>
<li><p><strong>internet_charge_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Network billing type, Values: PayByBandwidth or PayByTraffic. Default to <code class="docutils literal notranslate"><span class="pre">PayByBandwidth</span></code>.</p></li>
<li><p><strong>internet_max_bandwidth_in</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum incoming bandwidth from the public network, measured in Mbps (Mega bit per second). The value range is [1,200].</p></li>
<li><p><strong>internet_max_bandwidth_out</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum outgoing bandwidth from the public network, measured in Mbps (Mega bit per second). The value range for PayByBandwidth is [0,100].</p></li>
<li><p><strong>io_optimized</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – It has been deprecated on instance resource. All the launched alicloud instances will be I/O optimized.</p></li>
<li><p><strong>is_outdated</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to use outdated instance type. Default to false.</p></li>
<li><p><strong>key_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of key pair that can login ECS instance successfully without password. If it is specified, the password would be invalid.</p></li>
<li><p><strong>kms_encrypted_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An KMS encrypts password used to a db account. If the <code class="docutils literal notranslate"><span class="pre">password</span></code> is filled in, this field will be ignored.</p></li>
<li><p><strong>kms_encryption_context</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>An KMS encryption context used to decrypt <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> before creating or updating a db account with <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code>. See <a class="reference external" href="https://www.alibabacloud.com/help/doc-detail/42975.htm">Encryption Context</a>. It is valid when <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> is set.</p>
</p></li>
<li><p><strong>override</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether to overwrite the existing data. Default to false.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password of the ECS instance. The password must be 8 to 30 characters in length. It must contains at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include <code class="docutils literal notranslate"><span class="pre">()</span> <span class="pre">~!&#64;#$%^&amp;*-_+=\|{}[]:;'&lt;&gt;,.?/</span></code>, The password of Windows-based instances cannot start with a forward slash (/).</p></li>
<li><p><strong>password_inherit</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether to use the password that is predefined in the image. If the PasswordInherit parameter is set to true, the <code class="docutils literal notranslate"><span class="pre">password</span></code> and <code class="docutils literal notranslate"><span class="pre">kms_encrypted_password</span></code> will be ignored. You must ensure that the selected image has a password configured.</p></li>
<li><p><strong>role_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Instance RAM role name. The name is provided and maintained by RAM. You can use <code class="docutils literal notranslate"><span class="pre">ram.Role</span></code> to create a new one.</p></li>
<li><p><strong>scaling_configuration*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Name shown for the scheduled task. which must contain 2-64 characters (English or Chinese), starting with numbers, English letters or Chinese characters, and can contain number, underscores <cite>*`</cite>, hypens``-<code class="docutils literal notranslate"><span class="pre">,</span> <span class="pre">and</span> <span class="pre">decimal</span> <span class="pre">point</span></code>.<a href="#id7"><span class="problematic" id="id8">``</span></a>. If this parameter value is not specified, the default value is ScalingConfigurationId.</p>
</p></li>
<li><p><strong>scaling_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the scaling group of a scaling configuration.</p></li>
<li><p><strong>security_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the security group used to create new instance. It is conflict with``security_group_ids<a href="#id9"><span class="problematic" id="id10">``</span></a>.</p></li>
<li><p><strong>security_group_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List IDs of the security group used to create new instances. It is conflict with``security_group_id<a href="#id11"><span class="problematic" id="id12">``</span></a>.</p></li>
<li><p><strong>substitute</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The another scaling configuration which will be active automatically and replace current configuration when setting``active<code class="docutils literal notranslate"><span class="pre">to</span> <span class="pre">'false'.</span> <span class="pre">It</span> <span class="pre">is</span> <span class="pre">invalid</span> <span class="pre">when</span></code>active<a href="#id13"><span class="problematic" id="id14">``</span></a>is ‘true’.</p></li>
<li><p><strong>system_disk_auto_snapshot_policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of auto snapshot policy for system disk.</p></li>
<li><p><strong>system_disk_category</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Category of the system disk. The parameter value options are``ephemeral_ssd<code class="docutils literal notranslate"><span class="pre">,</span></code>cloud_efficiency<code class="docutils literal notranslate"><span class="pre">,</span></code>cloud_ssd<code class="docutils literal notranslate"><span class="pre">,</span></code>cloud_essd<code class="docutils literal notranslate"><span class="pre">and</span></code>cloud<code class="docutils literal notranslate"><span class="pre">.</span></code>cloud<code class="docutils literal notranslate"><span class="pre">only</span> <span class="pre">is</span> <span class="pre">used</span> <span class="pre">to</span> <span class="pre">some</span> <span class="pre">no</span> <span class="pre">I/O</span> <span class="pre">optimized</span> <span class="pre">instance.</span> <span class="pre">Default</span> <span class="pre">to</span></code>cloud_efficiency`.</p></li>
<li><p><strong>system_disk_description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the system disk. The description must be 2 to 256 characters in length and cannot start with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>.</p></li>
<li><p><strong>system_disk*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name of the system disk. It must be 2 to 128 characters in length. It must start with a letter and cannot start with <a class="reference external" href="http://">http://</a> or <a class="reference external" href="https://">https://</a>. It can contain letters, digits, colons (:), underscores (<a href="#id17"><span class="problematic" id="id18">*</span></a>), and hyphens (-). Default value: null.</p>
</p></li>
<li><p><strong>system_disk_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Size of system disk, in GiB. Optional values: cloud: 20-500, cloud_efficiency: 20-500, cloud_ssd: 20-500, ephemeral_ssd: 20-500 The default value is max{40, ImageSize}. If this parameter is set, the system disk size must be greater than or equal to max{40, ImageSize}.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource. It will be applied for ECS instances finally.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">Key</span><span class="p">:</span> <span class="n">It</span> <span class="n">can</span> <span class="n">be</span> <span class="n">up</span> <span class="n">to</span> <span class="mi">64</span> <span class="n">characters</span> <span class="ow">in</span> <span class="n">length</span><span class="o">.</span> <span class="n">It</span> <span class="n">cannot</span> <span class="n">begin</span> <span class="k">with</span> <span class="s2">&quot;aliyun&quot;</span><span class="p">,</span> <span class="s2">&quot;http://&quot;</span><span class="p">,</span> <span class="ow">or</span> <span class="s2">&quot;https://&quot;</span><span class="o">.</span> <span class="n">It</span> <span class="n">cannot</span> <span class="n">be</span> <span class="n">a</span> <span class="n">null</span> <span class="n">string</span><span class="o">.</span>
<span class="o">-</span> <span class="n">Value</span><span class="p">:</span> <span class="n">It</span> <span class="n">can</span> <span class="n">be</span> <span class="n">up</span> <span class="n">to</span> <span class="mi">128</span> <span class="n">characters</span> <span class="ow">in</span> <span class="n">length</span><span class="o">.</span> <span class="n">It</span> <span class="n">cannot</span> <span class="n">begin</span> <span class="k">with</span> <span class="s2">&quot;aliyun&quot;</span><span class="p">,</span> <span class="s2">&quot;http://&quot;</span><span class="p">,</span> <span class="ow">or</span> <span class="s2">&quot;https://&quot;</span> <span class="n">It</span> <span class="n">can</span> <span class="n">be</span> <span class="n">a</span> <span class="n">null</span> <span class="n">string</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>user_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User-defined data to customize the startup behaviors of the ECS instance and to pass data into the ECS instance.</p>
</dd>
</dl>
<p>The <strong>data_disks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">autoSnapshotPolicyId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">category</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">delete_with_instance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">device</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">encrypted</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">kms_key_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">size</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">snapshot_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ess.ScalingConfiguration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ess.ScalingConfiguration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.ScalingConfiguration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ess.ScalingGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ess.</code><code class="sig-name descname">ScalingGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">db_instance_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_cooldown</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">desired_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">loadbalancer_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">multi_az_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">on_demand_base_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">on_demand_percentage_above_base_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">removal_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spot_instance_pools</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spot_instance_remedy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.ScalingGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ScalingGroup resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[list] db_instance_ids: If an RDS instance is specified in the scaling group, the scaling group automatically attaches the Intranet IP addresses of its ECS instances to the RDS access whitelist.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- The specified RDS instance must be in running status.
- The specified RDS instance’s whitelist must have room for more IP addresses.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>default_cooldown</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Default cool-down time (in seconds) of the scaling group. Value range: [0, 86400]. The default value is 300s.</p></li>
<li><p><strong>desired_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Expected number of ECS instances in the scaling group. Value range: [min_size, max_size].</p></li>
<li><p><strong>loadbalancer_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If a Server Load Balancer instance is specified in the scaling group, the scaling group automatically attaches its ECS instances to the Server Load Balancer instance.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- The Server Load Balancer instance must be enabled.
- At least one listener must be configured for each Server Load Balancer and it HealthCheck must be on. Otherwise, creation will fail (it may be useful to add a `depends_on` argument
targeting your `slb.Listener` in order to make sure the listener with its HealthCheck configuration is ready before creating your scaling group).
- The Server Load Balancer instance attached with VPC-type ECS instances cannot be attached to the scaling group.
- The default weight of an ECS instance attached to the Server Load Balancer instance is 50.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>max_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum number of ECS instances in the scaling group. Value range: [0, 1000].</p></li>
<li><p><strong>min_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum number of ECS instances in the scaling group. Value range: [0, 1000].</p></li>
<li><p><strong>multi_az_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Multi-AZ scaling group ECS instance expansion and contraction strategy. PRIORITY, BALANCE or COST_OPTIMIZED(Available in 1.54.0+).</p></li>
<li><p><strong>on_demand_base_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum amount of the Auto Scaling group’s capacity that must be fulfilled by On-Demand Instances. This base portion is provisioned first as your group scales.</p></li>
<li><p><strong>on_demand_percentage_above_base_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Controls the percentages of On-Demand Instances and Spot Instances for your additional capacity beyond OnDemandBaseCapacity.<span class="raw-html-m2r"><br></span></p></li>
<li><p><strong>removal_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – RemovalPolicy is used to select the ECS instances you want to remove from the scaling group when multiple candidates for removal exist. Optional values:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">OldestInstance</span><span class="p">:</span> <span class="n">removes</span> <span class="n">the</span> <span class="n">ECS</span> <span class="n">instance</span> <span class="n">that</span> <span class="ow">is</span> <span class="n">added</span> <span class="n">to</span> <span class="n">the</span> <span class="n">scaling</span> <span class="n">group</span> <span class="n">at</span> <span class="n">the</span> <span class="n">earliest</span> <span class="n">point</span> <span class="ow">in</span> <span class="n">time</span><span class="o">.</span>
<span class="o">-</span> <span class="n">NewestInstance</span><span class="p">:</span> <span class="n">removes</span> <span class="n">the</span> <span class="n">ECS</span> <span class="n">instance</span> <span class="n">that</span> <span class="ow">is</span> <span class="n">added</span> <span class="n">to</span> <span class="n">the</span> <span class="n">scaling</span> <span class="n">group</span> <span class="n">at</span> <span class="n">the</span> <span class="n">latest</span> <span class="n">point</span> <span class="ow">in</span> <span class="n">time</span><span class="o">.</span>
<span class="o">-</span> <span class="n">OldestScalingConfiguration</span><span class="p">:</span> <span class="n">removes</span> <span class="n">the</span> <span class="n">ECS</span> <span class="n">instance</span> <span class="n">that</span> <span class="ow">is</span> <span class="n">created</span> <span class="n">based</span> <span class="n">on</span> <span class="n">the</span> <span class="n">earliest</span> <span class="n">scaling</span> <span class="n">configuration</span><span class="o">.</span>
<span class="o">-</span> <span class="n">Default</span> <span class="n">values</span><span class="p">:</span> <span class="n">Default</span> <span class="n">value</span> <span class="n">of</span> <span class="n">RemovalPolicy</span><span class="o">.</span><span class="mi">1</span><span class="p">:</span> <span class="n">OldestScalingConfiguration</span><span class="o">.</span> <span class="n">Default</span> <span class="n">value</span> <span class="n">of</span> <span class="n">RemovalPolicy</span><span class="o">.</span><span class="mi">2</span><span class="p">:</span> <span class="n">OldestInstance</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>scaling_group*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Name shown for the scaling group, which must contain 2-64 characters (English or Chinese), starting with numbers, English letters or Chinese characters, and can contain numbers, underscores <cite>*`</cite>, hyphens``-<code class="docutils literal notranslate"><span class="pre">,</span> <span class="pre">and</span> <span class="pre">decimal</span> <span class="pre">points</span></code>.`. If this parameter is not specified, the default value is ScalingGroupId.</p>
</p></li>
<li><p><strong>spot_instance_pools</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of Spot pools to use to allocate your Spot capacity. The Spot pools is composed of instance types of lowest price.</p></li>
<li><p><strong>spot_instance_remedy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to replace spot instances with newly created spot/onDemand instance when receive a spot recycling message.<span class="raw-html-m2r"><br></span></p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – It has been deprecated from version 1.7.1 and new field ‘vswitch_ids’ replaces it.</p></li>
<li><p><strong>vswitch_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of virtual switch IDs in which the ecs instances to be launched.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingGroup.db_instance_ids">
<code class="sig-name descname">db_instance_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingGroup.db_instance_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>If an RDS instance is specified in the scaling group, the scaling group automatically attaches the Intranet IP addresses of its ECS instances to the RDS access whitelist.</p>
<ul class="simple">
<li><p>The specified RDS instance must be in running status.</p></li>
<li><p>The specified RDS instance’s whitelist must have room for more IP addresses.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingGroup.default_cooldown">
<code class="sig-name descname">default_cooldown</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingGroup.default_cooldown" title="Permalink to this definition">¶</a></dt>
<dd><p>Default cool-down time (in seconds) of the scaling group. Value range: [0, 86400]. The default value is 300s.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingGroup.desired_capacity">
<code class="sig-name descname">desired_capacity</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingGroup.desired_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>Expected number of ECS instances in the scaling group. Value range: [min_size, max_size].</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingGroup.loadbalancer_ids">
<code class="sig-name descname">loadbalancer_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingGroup.loadbalancer_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>If a Server Load Balancer instance is specified in the scaling group, the scaling group automatically attaches its ECS instances to the Server Load Balancer instance.</p>
<ul class="simple">
<li><p>The Server Load Balancer instance must be enabled.</p></li>
<li><p>At least one listener must be configured for each Server Load Balancer and it HealthCheck must be on. Otherwise, creation will fail (it may be useful to add a <code class="docutils literal notranslate"><span class="pre">depends_on</span></code> argument
targeting your <code class="docutils literal notranslate"><span class="pre">slb.Listener</span></code> in order to make sure the listener with its HealthCheck configuration is ready before creating your scaling group).</p></li>
<li><p>The Server Load Balancer instance attached with VPC-type ECS instances cannot be attached to the scaling group.</p></li>
<li><p>The default weight of an ECS instance attached to the Server Load Balancer instance is 50.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingGroup.max_size">
<code class="sig-name descname">max_size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingGroup.max_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum number of ECS instances in the scaling group. Value range: [0, 1000].</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingGroup.min_size">
<code class="sig-name descname">min_size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingGroup.min_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Minimum number of ECS instances in the scaling group. Value range: [0, 1000].</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingGroup.multi_az_policy">
<code class="sig-name descname">multi_az_policy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingGroup.multi_az_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Multi-AZ scaling group ECS instance expansion and contraction strategy. PRIORITY, BALANCE or COST_OPTIMIZED(Available in 1.54.0+).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingGroup.on_demand_base_capacity">
<code class="sig-name descname">on_demand_base_capacity</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingGroup.on_demand_base_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum amount of the Auto Scaling group’s capacity that must be fulfilled by On-Demand Instances. This base portion is provisioned first as your group scales.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingGroup.on_demand_percentage_above_base_capacity">
<code class="sig-name descname">on_demand_percentage_above_base_capacity</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingGroup.on_demand_percentage_above_base_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>Controls the percentages of On-Demand Instances and Spot Instances for your additional capacity beyond OnDemandBaseCapacity.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingGroup.removal_policies">
<code class="sig-name descname">removal_policies</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingGroup.removal_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>RemovalPolicy is used to select the ECS instances you want to remove from the scaling group when multiple candidates for removal exist. Optional values:</p>
<ul class="simple">
<li><p>OldestInstance: removes the ECS instance that is added to the scaling group at the earliest point in time.</p></li>
<li><p>NewestInstance: removes the ECS instance that is added to the scaling group at the latest point in time.</p></li>
<li><p>OldestScalingConfiguration: removes the ECS instance that is created based on the earliest scaling configuration.</p></li>
<li><p>Default values: Default value of RemovalPolicy.1: OldestScalingConfiguration. Default value of RemovalPolicy.2: OldestInstance.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingGroup.scaling_group_name">
<code class="sig-name descname">scaling_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingGroup.scaling_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name shown for the scaling group, which must contain 2-64 characters (English or Chinese), starting with numbers, English letters or Chinese characters, and can contain numbers, underscores <code class="docutils literal notranslate"><span class="pre">_</span></code>, hyphens <code class="docutils literal notranslate"><span class="pre">-</span></code>, and decimal points <code class="docutils literal notranslate"><span class="pre">.</span></code>. If this parameter is not specified, the default value is ScalingGroupId.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingGroup.spot_instance_pools">
<code class="sig-name descname">spot_instance_pools</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingGroup.spot_instance_pools" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of Spot pools to use to allocate your Spot capacity. The Spot pools is composed of instance types of lowest price.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingGroup.spot_instance_remedy">
<code class="sig-name descname">spot_instance_remedy</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingGroup.spot_instance_remedy" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to replace spot instances with newly created spot/onDemand instance when receive a spot recycling message.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingGroup.vswitch_id">
<code class="sig-name descname">vswitch_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingGroup.vswitch_id" title="Permalink to this definition">¶</a></dt>
<dd><p>It has been deprecated from version 1.7.1 and new field ‘vswitch_ids’ replaces it.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingGroup.vswitch_ids">
<code class="sig-name descname">vswitch_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingGroup.vswitch_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>List of virtual switch IDs in which the ecs instances to be launched.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ess.ScalingGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">db_instance_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_cooldown</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">desired_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">loadbalancer_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">multi_az_policy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">on_demand_base_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">on_demand_percentage_above_base_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">removal_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spot_instance_pools</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">spot_instance_remedy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vswitch_ids</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.ScalingGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ScalingGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>db_instance_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If an RDS instance is specified in the scaling group, the scaling group automatically attaches the Intranet IP addresses of its ECS instances to the RDS access whitelist.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- The specified RDS instance must be in running status.
- The specified RDS instance’s whitelist must have room for more IP addresses.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>default_cooldown</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Default cool-down time (in seconds) of the scaling group. Value range: [0, 86400]. The default value is 300s.</p></li>
<li><p><strong>desired_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Expected number of ECS instances in the scaling group. Value range: [min_size, max_size].</p></li>
<li><p><strong>loadbalancer_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – If a Server Load Balancer instance is specified in the scaling group, the scaling group automatically attaches its ECS instances to the Server Load Balancer instance.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- The Server Load Balancer instance must be enabled.
- At least one listener must be configured for each Server Load Balancer and it HealthCheck must be on. Otherwise, creation will fail (it may be useful to add a `depends_on` argument
targeting your `slb.Listener` in order to make sure the listener with its HealthCheck configuration is ready before creating your scaling group).
- The Server Load Balancer instance attached with VPC-type ECS instances cannot be attached to the scaling group.
- The default weight of an ECS instance attached to the Server Load Balancer instance is 50.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>max_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Maximum number of ECS instances in the scaling group. Value range: [0, 1000].</p></li>
<li><p><strong>min_size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Minimum number of ECS instances in the scaling group. Value range: [0, 1000].</p></li>
<li><p><strong>multi_az_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Multi-AZ scaling group ECS instance expansion and contraction strategy. PRIORITY, BALANCE or COST_OPTIMIZED(Available in 1.54.0+).</p></li>
<li><p><strong>on_demand_base_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum amount of the Auto Scaling group’s capacity that must be fulfilled by On-Demand Instances. This base portion is provisioned first as your group scales.</p></li>
<li><p><strong>on_demand_percentage_above_base_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Controls the percentages of On-Demand Instances and Spot Instances for your additional capacity beyond OnDemandBaseCapacity.<span class="raw-html-m2r"><br></span></p></li>
<li><p><strong>removal_policies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – RemovalPolicy is used to select the ECS instances you want to remove from the scaling group when multiple candidates for removal exist. Optional values:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">OldestInstance</span><span class="p">:</span> <span class="n">removes</span> <span class="n">the</span> <span class="n">ECS</span> <span class="n">instance</span> <span class="n">that</span> <span class="ow">is</span> <span class="n">added</span> <span class="n">to</span> <span class="n">the</span> <span class="n">scaling</span> <span class="n">group</span> <span class="n">at</span> <span class="n">the</span> <span class="n">earliest</span> <span class="n">point</span> <span class="ow">in</span> <span class="n">time</span><span class="o">.</span>
<span class="o">-</span> <span class="n">NewestInstance</span><span class="p">:</span> <span class="n">removes</span> <span class="n">the</span> <span class="n">ECS</span> <span class="n">instance</span> <span class="n">that</span> <span class="ow">is</span> <span class="n">added</span> <span class="n">to</span> <span class="n">the</span> <span class="n">scaling</span> <span class="n">group</span> <span class="n">at</span> <span class="n">the</span> <span class="n">latest</span> <span class="n">point</span> <span class="ow">in</span> <span class="n">time</span><span class="o">.</span>
<span class="o">-</span> <span class="n">OldestScalingConfiguration</span><span class="p">:</span> <span class="n">removes</span> <span class="n">the</span> <span class="n">ECS</span> <span class="n">instance</span> <span class="n">that</span> <span class="ow">is</span> <span class="n">created</span> <span class="n">based</span> <span class="n">on</span> <span class="n">the</span> <span class="n">earliest</span> <span class="n">scaling</span> <span class="n">configuration</span><span class="o">.</span>
<span class="o">-</span> <span class="n">Default</span> <span class="n">values</span><span class="p">:</span> <span class="n">Default</span> <span class="n">value</span> <span class="n">of</span> <span class="n">RemovalPolicy</span><span class="o">.</span><span class="mi">1</span><span class="p">:</span> <span class="n">OldestScalingConfiguration</span><span class="o">.</span> <span class="n">Default</span> <span class="n">value</span> <span class="n">of</span> <span class="n">RemovalPolicy</span><span class="o">.</span><span class="mi">2</span><span class="p">:</span> <span class="n">OldestInstance</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>scaling_group*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Name shown for the scaling group, which must contain 2-64 characters (English or Chinese), starting with numbers, English letters or Chinese characters, and can contain numbers, underscores <cite>*`</cite>, hyphens``-<code class="docutils literal notranslate"><span class="pre">,</span> <span class="pre">and</span> <span class="pre">decimal</span> <span class="pre">points</span></code>.`. If this parameter is not specified, the default value is ScalingGroupId.</p>
</p></li>
<li><p><strong>spot_instance_pools</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of Spot pools to use to allocate your Spot capacity. The Spot pools is composed of instance types of lowest price.</p></li>
<li><p><strong>spot_instance_remedy</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to replace spot instances with newly created spot/onDemand instance when receive a spot recycling message.<span class="raw-html-m2r"><br></span></p></li>
<li><p><strong>vswitch_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – It has been deprecated from version 1.7.1 and new field ‘vswitch_ids’ replaces it.</p></li>
<li><p><strong>vswitch_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of virtual switch IDs in which the ecs instances to be launched.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ess.ScalingGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.ScalingGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ess.ScalingGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.ScalingGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ess.ScalingGroupVServerGroups">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ess.</code><code class="sig-name descname">ScalingGroupVServerGroups</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vserver_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.ScalingGroupVServerGroups" title="Permalink to this definition">¶</a></dt>
<dd><p>Attaches/Detaches vserver groups to a specified scaling group.</p>
<blockquote>
<div><p><strong>NOTE:</strong> The load balancer of which vserver groups belongs to must be in <code class="docutils literal notranslate"><span class="pre">active</span></code> status.</p>
<p><strong>NOTE:</strong> If scaling group’s network type is <code class="docutils literal notranslate"><span class="pre">VPC</span></code>, the vserver groups must be in the same <code class="docutils literal notranslate"><span class="pre">VPC</span></code>.</p>
<p><strong>NOTE:</strong> A scaling group can have at most 5 vserver groups attached by default.</p>
<p><strong>NOTE:</strong> Vserver groups and the default group of loadbalancer share the same backend server quota.</p>
<p><strong>NOTE:</strong> When attach vserver groups to scaling group, existing ECS instances will be added to vserver groups; Instead, ECS instances will be removed from vserver group when detach.</p>
<p><strong>NOTE:</strong> Detach action will be executed before attach action.</p>
<p><strong>NOTE:</strong> Vserver group is defined uniquely by <code class="docutils literal notranslate"><span class="pre">loadbalancer_id</span></code>, <code class="docutils literal notranslate"><span class="pre">vserver_group_id</span></code>, <code class="docutils literal notranslate"><span class="pre">port</span></code>.</p>
<p><strong>NOTE:</strong> Modifing <code class="docutils literal notranslate"><span class="pre">weight</span></code> attribute means detach vserver group first and then, attach with new weight parameter.</p>
<p><strong>NOTE:</strong> Resource <code class="docutils literal notranslate"><span class="pre">ess.ScalingGroupVServerGroups</span></code> is available in 1.53.0+.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">config</span> <span class="o">=</span> <span class="n">pulumi</span><span class="o">.</span><span class="n">Config</span><span class="p">()</span>
<span class="n">name</span> <span class="o">=</span> <span class="n">config</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s2">&quot;name&quot;</span><span class="p">)</span>
<span class="k">if</span> <span class="n">name</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
    <span class="n">name</span> <span class="o">=</span> <span class="s2">&quot;testAccEssVserverGroupsAttachment&quot;</span>
<span class="n">default_zones</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">get_zones</span><span class="p">(</span><span class="n">available_disk_category</span><span class="o">=</span><span class="s2">&quot;cloud_efficiency&quot;</span><span class="p">,</span>
    <span class="n">available_resource_creation</span><span class="o">=</span><span class="s2">&quot;VSwitch&quot;</span><span class="p">)</span>
<span class="n">default_network</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">vpc</span><span class="o">.</span><span class="n">Network</span><span class="p">(</span><span class="s2">&quot;defaultNetwork&quot;</span><span class="p">,</span> <span class="n">cidr_block</span><span class="o">=</span><span class="s2">&quot;172.16.0.0/16&quot;</span><span class="p">)</span>
<span class="n">default_switch</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">vpc</span><span class="o">.</span><span class="n">Switch</span><span class="p">(</span><span class="s2">&quot;defaultSwitch&quot;</span><span class="p">,</span>
    <span class="n">availability_zone</span><span class="o">=</span><span class="n">default_zones</span><span class="o">.</span><span class="n">zones</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">cidr_block</span><span class="o">=</span><span class="s2">&quot;172.16.0.0/24&quot;</span><span class="p">,</span>
    <span class="n">vpc_id</span><span class="o">=</span><span class="n">default_network</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">default_load_balancer</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">slb</span><span class="o">.</span><span class="n">LoadBalancer</span><span class="p">(</span><span class="s2">&quot;defaultLoadBalancer&quot;</span><span class="p">,</span> <span class="n">vswitch_id</span><span class="o">=</span><span class="n">default_switch</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">default_server_group</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">slb</span><span class="o">.</span><span class="n">ServerGroup</span><span class="p">(</span><span class="s2">&quot;defaultServerGroup&quot;</span><span class="p">,</span> <span class="n">load_balancer_id</span><span class="o">=</span><span class="n">default_load_balancer</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">default_listener</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="nb">range</span> <span class="ow">in</span> <span class="p">[{</span><span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="n">i</span><span class="p">}</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">2</span><span class="p">)]:</span>
    <span class="n">default_listener</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">alicloud</span><span class="o">.</span><span class="n">slb</span><span class="o">.</span><span class="n">Listener</span><span class="p">(</span><span class="sa">f</span><span class="s2">&quot;defaultListener-</span><span class="si">{</span><span class="nb">range</span><span class="p">[</span><span class="s1">&#39;value&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">,</span>
        <span class="n">backend_port</span><span class="o">=</span><span class="s2">&quot;22&quot;</span><span class="p">,</span>
        <span class="n">bandwidth</span><span class="o">=</span><span class="s2">&quot;10&quot;</span><span class="p">,</span>
        <span class="n">frontend_port</span><span class="o">=</span><span class="s2">&quot;22&quot;</span><span class="p">,</span>
        <span class="n">health_check_type</span><span class="o">=</span><span class="s2">&quot;tcp&quot;</span><span class="p">,</span>
        <span class="n">load_balancer_id</span><span class="o">=</span><span class="p">[</span><span class="n">__item</span><span class="o">.</span><span class="n">id</span> <span class="k">for</span> <span class="n">__item</span> <span class="ow">in</span> <span class="p">[</span><span class="n">default_load_balancer</span><span class="p">]][</span><span class="nb">range</span><span class="p">[</span><span class="s2">&quot;value&quot;</span><span class="p">]],</span>
        <span class="n">protocol</span><span class="o">=</span><span class="s2">&quot;tcp&quot;</span><span class="p">))</span>
<span class="n">default_scaling_group</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ess</span><span class="o">.</span><span class="n">ScalingGroup</span><span class="p">(</span><span class="s2">&quot;defaultScalingGroup&quot;</span><span class="p">,</span>
    <span class="n">max_size</span><span class="o">=</span><span class="s2">&quot;2&quot;</span><span class="p">,</span>
    <span class="n">min_size</span><span class="o">=</span><span class="s2">&quot;2&quot;</span><span class="p">,</span>
    <span class="n">scaling_group_name</span><span class="o">=</span><span class="n">name</span><span class="p">,</span>
    <span class="n">vswitch_ids</span><span class="o">=</span><span class="p">[</span><span class="n">default_switch</span><span class="o">.</span><span class="n">id</span><span class="p">])</span>
<span class="n">default_scaling_group_v_server_groups</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ess</span><span class="o">.</span><span class="n">ScalingGroupVServerGroups</span><span class="p">(</span><span class="s2">&quot;defaultScalingGroupVServerGroups&quot;</span><span class="p">,</span>
    <span class="n">scaling_group_id</span><span class="o">=</span><span class="n">default_scaling_group</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">vserver_groups</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;loadbalancerId&quot;</span><span class="p">:</span> <span class="n">default_load_balancer</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
        <span class="s2">&quot;vserverAttributes&quot;</span><span class="p">:</span> <span class="p">[{</span>
            <span class="s2">&quot;port&quot;</span><span class="p">:</span> <span class="s2">&quot;100&quot;</span><span class="p">,</span>
            <span class="s2">&quot;vserver_group_id&quot;</span><span class="p">:</span> <span class="n">default_server_group</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
            <span class="s2">&quot;weight&quot;</span><span class="p">:</span> <span class="s2">&quot;60&quot;</span><span class="p">,</span>
        <span class="p">}],</span>
    <span class="p">}])</span>
</pre></div>
</div>
<p>the vserver_group supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">loadbalancer_id</span></code> - (Required) Loadbalancer server ID of VServer Group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vserver_attributes</span></code> - (Required) A list of VServer Group attributes. See Block vserver_attribute below for details.</p></li>
</ul>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">vserver_group_id</span></code> - (Required) ID of VServer Group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> - (Required) - The port will be used for VServer Group backend server.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> - (Required) The weight of an ECS instance attached to the VServer Group.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>force</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If instances of scaling group are attached/removed from slb backend server when attach/detach vserver group from scaling group. Default to true.</p></li>
<li><p><strong>scaling_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the scaling group.</p></li>
<li><p><strong>vserver_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of vserver groups attached on scaling group. See Block vserver_group below for details.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>vserver_groups</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">loadbalancerId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vserverAttributes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vserver_group_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
</ul>
<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingGroupVServerGroups.force">
<code class="sig-name descname">force</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingGroupVServerGroups.force" title="Permalink to this definition">¶</a></dt>
<dd><p>If instances of scaling group are attached/removed from slb backend server when attach/detach vserver group from scaling group. Default to true.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingGroupVServerGroups.scaling_group_id">
<code class="sig-name descname">scaling_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingGroupVServerGroups.scaling_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the scaling group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingGroupVServerGroups.vserver_groups">
<code class="sig-name descname">vserver_groups</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingGroupVServerGroups.vserver_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of vserver groups attached on scaling group. See Block vserver_group below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">loadbalancerId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vserverAttributes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vserver_group_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ess.ScalingGroupVServerGroups.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vserver_groups</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.ScalingGroupVServerGroups.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ScalingGroupVServerGroups resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>force</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If instances of scaling group are attached/removed from slb backend server when attach/detach vserver group from scaling group. Default to true.</p></li>
<li><p><strong>scaling_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the scaling group.</p></li>
<li><p><strong>vserver_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of vserver groups attached on scaling group. See Block vserver_group below for details.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>vserver_groups</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">loadbalancerId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vserverAttributes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vserver_group_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">weight</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ess.ScalingGroupVServerGroups.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.ScalingGroupVServerGroups.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ess.ScalingGroupVServerGroups.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.ScalingGroupVServerGroups.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ess.ScalingRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ess.</code><code class="sig-name descname">ScalingRule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">adjustment_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">adjustment_value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cooldown</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disable_scale_in</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">estimated_instance_warmup</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_rule_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_rule_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">step_adjustments</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.ScalingRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ScalingRule resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] adjustment_type: Adjustment mode of a scaling rule. Optional values:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">QuantityChangeInCapacity</span><span class="p">:</span> <span class="n">It</span> <span class="ow">is</span> <span class="n">used</span> <span class="n">to</span> <span class="n">increase</span> <span class="ow">or</span> <span class="n">decrease</span> <span class="n">a</span> <span class="n">specified</span> <span class="n">number</span> <span class="n">of</span> <span class="n">ECS</span> <span class="n">instances</span><span class="o">.</span>
<span class="o">-</span> <span class="n">PercentChangeInCapacity</span><span class="p">:</span> <span class="n">It</span> <span class="ow">is</span> <span class="n">used</span> <span class="n">to</span> <span class="n">increase</span> <span class="ow">or</span> <span class="n">decrease</span> <span class="n">a</span> <span class="n">specified</span> <span class="n">proportion</span> <span class="n">of</span> <span class="n">ECS</span> <span class="n">instances</span><span class="o">.</span>
<span class="o">-</span> <span class="n">TotalCapacity</span><span class="p">:</span> <span class="n">It</span> <span class="ow">is</span> <span class="n">used</span> <span class="n">to</span> <span class="n">adjust</span> <span class="n">the</span> <span class="n">quantity</span> <span class="n">of</span> <span class="n">ECS</span> <span class="n">instances</span> <span class="ow">in</span> <span class="n">the</span> <span class="n">current</span> <span class="n">scaling</span> <span class="n">group</span> <span class="n">to</span> <span class="n">a</span> <span class="n">specified</span> <span class="n">value</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>adjustment_value</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Adjusted value of a scaling rule. Value range:</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- QuantityChangeInCapacity：(0, 500] U (-500, 0]
- PercentChangeInCapacity：[0, 10000] U [-100, 0]
- TotalCapacity：[0, 1000]
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>cooldown</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Cool-down time of a scaling rule. Value range: [0, 86,400], in seconds. The default value is empty，if not set, the return value will be 0, which is the default value of integer.</p></li>
<li><p><strong>disable_scale_in</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether scale in by the target tracking policy is disabled. Default to false.</p></li>
<li><p><strong>estimated_instance_warmup</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The estimated time, in seconds, until a newly launched instance will contribute CloudMonitor metrics. Default to 300.</p></li>
<li><p><strong>metric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A CloudMonitor metric name.</p></li>
<li><p><strong>scaling_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the scaling group of a scaling rule.</p></li>
<li><p><strong>scaling_rule*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Name shown for the scaling rule, which must contain 2-64 characters (English or Chinese), starting with numbers, English letters or Chinese characters, and can contain number, underscores <cite>*`</cite>, hypens``-<code class="docutils literal notranslate"><span class="pre">,</span> <span class="pre">and</span> <span class="pre">decimal</span> <span class="pre">point</span></code>.`. If this parameter value is not specified, the default value is scaling rule id.</p>
</p></li>
<li><p><strong>scaling_rule_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The scaling rule type, either “SimpleScalingRule”, “TargetTrackingScalingRule”, “StepScalingRule”. Default to “SimpleScalingRule”.</p></li>
<li><p><strong>step_adjustments</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Steps for StepScalingRule. See Block stepAdjustment below for details.</p></li>
<li><p><strong>target_value</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The target value for the metric.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>step_adjustments</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">metricIntervalLowerBound</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricIntervalUpperBound</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scalingAdjustment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingRule.adjustment_type">
<code class="sig-name descname">adjustment_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingRule.adjustment_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Adjustment mode of a scaling rule. Optional values:</p>
<ul class="simple">
<li><p>QuantityChangeInCapacity: It is used to increase or decrease a specified number of ECS instances.</p></li>
<li><p>PercentChangeInCapacity: It is used to increase or decrease a specified proportion of ECS instances.</p></li>
<li><p>TotalCapacity: It is used to adjust the quantity of ECS instances in the current scaling group to a specified value.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingRule.adjustment_value">
<code class="sig-name descname">adjustment_value</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingRule.adjustment_value" title="Permalink to this definition">¶</a></dt>
<dd><p>Adjusted value of a scaling rule. Value range:</p>
<ul class="simple">
<li><p>QuantityChangeInCapacity：(0, 500] U (-500, 0]</p></li>
<li><p>PercentChangeInCapacity：[0, 10000] U [-100, 0]</p></li>
<li><p>TotalCapacity：[0, 1000]</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingRule.cooldown">
<code class="sig-name descname">cooldown</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingRule.cooldown" title="Permalink to this definition">¶</a></dt>
<dd><p>Cool-down time of a scaling rule. Value range: [0, 86,400], in seconds. The default value is empty，if not set, the return value will be 0, which is the default value of integer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingRule.disable_scale_in">
<code class="sig-name descname">disable_scale_in</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingRule.disable_scale_in" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether scale in by the target tracking policy is disabled. Default to false.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingRule.estimated_instance_warmup">
<code class="sig-name descname">estimated_instance_warmup</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingRule.estimated_instance_warmup" title="Permalink to this definition">¶</a></dt>
<dd><p>The estimated time, in seconds, until a newly launched instance will contribute CloudMonitor metrics. Default to 300.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingRule.metric_name">
<code class="sig-name descname">metric_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingRule.metric_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A CloudMonitor metric name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingRule.scaling_group_id">
<code class="sig-name descname">scaling_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingRule.scaling_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the scaling group of a scaling rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingRule.scaling_rule_name">
<code class="sig-name descname">scaling_rule_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingRule.scaling_rule_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name shown for the scaling rule, which must contain 2-64 characters (English or Chinese), starting with numbers, English letters or Chinese characters, and can contain number, underscores <code class="docutils literal notranslate"><span class="pre">_</span></code>, hypens <code class="docutils literal notranslate"><span class="pre">-</span></code>, and decimal point <code class="docutils literal notranslate"><span class="pre">.</span></code>. If this parameter value is not specified, the default value is scaling rule id.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingRule.scaling_rule_type">
<code class="sig-name descname">scaling_rule_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingRule.scaling_rule_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The scaling rule type, either “SimpleScalingRule”, “TargetTrackingScalingRule”, “StepScalingRule”. Default to “SimpleScalingRule”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingRule.step_adjustments">
<code class="sig-name descname">step_adjustments</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingRule.step_adjustments" title="Permalink to this definition">¶</a></dt>
<dd><p>Steps for StepScalingRule. See Block stepAdjustment below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">metricIntervalLowerBound</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricIntervalUpperBound</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scalingAdjustment</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScalingRule.target_value">
<code class="sig-name descname">target_value</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScalingRule.target_value" title="Permalink to this definition">¶</a></dt>
<dd><p>The target value for the metric.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ess.ScalingRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">adjustment_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">adjustment_value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ari</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cooldown</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disable_scale_in</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">estimated_instance_warmup</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_rule_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_rule_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">step_adjustments</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_value</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.ScalingRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ScalingRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>adjustment_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Adjustment mode of a scaling rule. Optional values:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">QuantityChangeInCapacity</span><span class="p">:</span> <span class="n">It</span> <span class="ow">is</span> <span class="n">used</span> <span class="n">to</span> <span class="n">increase</span> <span class="ow">or</span> <span class="n">decrease</span> <span class="n">a</span> <span class="n">specified</span> <span class="n">number</span> <span class="n">of</span> <span class="n">ECS</span> <span class="n">instances</span><span class="o">.</span>
<span class="o">-</span> <span class="n">PercentChangeInCapacity</span><span class="p">:</span> <span class="n">It</span> <span class="ow">is</span> <span class="n">used</span> <span class="n">to</span> <span class="n">increase</span> <span class="ow">or</span> <span class="n">decrease</span> <span class="n">a</span> <span class="n">specified</span> <span class="n">proportion</span> <span class="n">of</span> <span class="n">ECS</span> <span class="n">instances</span><span class="o">.</span>
<span class="o">-</span> <span class="n">TotalCapacity</span><span class="p">:</span> <span class="n">It</span> <span class="ow">is</span> <span class="n">used</span> <span class="n">to</span> <span class="n">adjust</span> <span class="n">the</span> <span class="n">quantity</span> <span class="n">of</span> <span class="n">ECS</span> <span class="n">instances</span> <span class="ow">in</span> <span class="n">the</span> <span class="n">current</span> <span class="n">scaling</span> <span class="n">group</span> <span class="n">to</span> <span class="n">a</span> <span class="n">specified</span> <span class="n">value</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>adjustment_value</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Adjusted value of a scaling rule. Value range:</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- QuantityChangeInCapacity：(0, 500] U (-500, 0]
- PercentChangeInCapacity：[0, 10000] U [-100, 0]
- TotalCapacity：[0, 1000]
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>cooldown</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Cool-down time of a scaling rule. Value range: [0, 86,400], in seconds. The default value is empty，if not set, the return value will be 0, which is the default value of integer.</p></li>
<li><p><strong>disable_scale_in</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether scale in by the target tracking policy is disabled. Default to false.</p></li>
<li><p><strong>estimated_instance_warmup</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The estimated time, in seconds, until a newly launched instance will contribute CloudMonitor metrics. Default to 300.</p></li>
<li><p><strong>metric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A CloudMonitor metric name.</p></li>
<li><p><strong>scaling_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the scaling group of a scaling rule.</p></li>
<li><p><strong>scaling_rule*name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Name shown for the scaling rule, which must contain 2-64 characters (English or Chinese), starting with numbers, English letters or Chinese characters, and can contain number, underscores <cite>*`</cite>, hypens``-<code class="docutils literal notranslate"><span class="pre">,</span> <span class="pre">and</span> <span class="pre">decimal</span> <span class="pre">point</span></code>.`. If this parameter value is not specified, the default value is scaling rule id.</p>
</p></li>
<li><p><strong>scaling_rule_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The scaling rule type, either “SimpleScalingRule”, “TargetTrackingScalingRule”, “StepScalingRule”. Default to “SimpleScalingRule”.</p></li>
<li><p><strong>step_adjustments</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Steps for StepScalingRule. See Block stepAdjustment below for details.</p></li>
<li><p><strong>target_value</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The target value for the metric.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>step_adjustments</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">metricIntervalLowerBound</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metricIntervalUpperBound</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scalingAdjustment</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ess.ScalingRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.ScalingRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ess.ScalingRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.ScalingRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ess.Schedule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ess.</code><code class="sig-name descname">Schedule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">desired_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">launch_expiration_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">launch_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recurrence_end_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recurrence_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recurrence_value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheduled_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheduled_task_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">task_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.Schedule" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Schedule resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.</p>
<dl class="py method">
<dt id="pulumi_alicloud.ess.Schedule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">desired_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">launch_expiration_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">launch_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recurrence_end_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recurrence_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recurrence_value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheduled_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheduled_task_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">task_enabled</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.Schedule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Schedule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ess.Schedule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.Schedule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ess.Schedule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.Schedule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ess.ScheduledTask">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_alicloud.ess.</code><code class="sig-name descname">ScheduledTask</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">desired_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">launch_expiration_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">launch_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recurrence_end_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recurrence_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recurrence_value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheduled_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheduled_task_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">task_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.ScheduledTask" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ScheduledTask resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] description: Description of the scheduled task, which is 2-200 characters (English or Chinese) long.
:param pulumi.Input[float] desired_capacity: The expected number of instances in a scaling group when the scaling method of the scheduled task is to specify the number of instances in a scaling group. <strong>NOTE:</strong> You must specify the <code class="docutils literal notranslate"><span class="pre">DesiredCapacity</span></code> parameter when you create the scaling group.
:param pulumi.Input[float] launch_expiration_time: The time period during which a failed scheduled task is retried. Unit: seconds. Valid values: 0 to 21600. Default value: 600
:param pulumi.Input[str] launch_time: The time at which the scheduled task is triggered. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mmZ format.</p>
<blockquote>
<div><p>The time must be in UTC. You cannot enter a time point later than 90 days from the date of scheduled task creation.
If the <code class="docutils literal notranslate"><span class="pre">recurrence_type</span></code> parameter is specified, the task is executed repeatedly at the time specified by LaunchTime.
Otherwise, the task is only executed once at the date and time specified by LaunchTime.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>max_value</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of instances in a scaling group when the scaling method of the scheduled task is to specify the number of instances in a scaling group.</p></li>
<li><p><strong>min_value</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum number of instances in a scaling group when the scaling method of the scheduled task is to specify the number of instances in a scaling group.</p></li>
<li><p><strong>recurrence_end_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the end time after which the scheduled task is no longer repeated. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. 
The time must be in UTC. You cannot enter a time point later than 365 days from the date of scheduled task creation. <strong>NOTE:</strong> You must specify <code class="docutils literal notranslate"><span class="pre">RecurrenceType</span></code>, <code class="docutils literal notranslate"><span class="pre">RecurrenceValue</span></code>, and <code class="docutils literal notranslate"><span class="pre">RecurrenceEndTime</span></code> at the same time.</p></li>
<li><p><strong>recurrence_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the recurrence type of the scheduled task. <strong>NOTE:</strong> You must specify <code class="docutils literal notranslate"><span class="pre">RecurrenceType</span></code>, <code class="docutils literal notranslate"><span class="pre">RecurrenceValue</span></code>, and <code class="docutils literal notranslate"><span class="pre">RecurrenceEndTime</span></code> at the same time. Valid values:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">Daily</span><span class="p">:</span> <span class="n">The</span> <span class="n">scheduled</span> <span class="n">task</span> <span class="ow">is</span> <span class="n">executed</span> <span class="n">once</span> <span class="n">every</span> <span class="n">specified</span> <span class="n">number</span> <span class="n">of</span> <span class="n">days</span><span class="o">.</span>
<span class="o">-</span> <span class="n">Weekly</span><span class="p">:</span> <span class="n">The</span> <span class="n">scheduled</span> <span class="n">task</span> <span class="ow">is</span> <span class="n">executed</span> <span class="n">on</span> <span class="n">each</span> <span class="n">specified</span> <span class="n">day</span> <span class="n">of</span> <span class="n">a</span> <span class="n">week</span><span class="o">.</span>
<span class="o">-</span> <span class="n">Monthly</span><span class="p">:</span> <span class="n">The</span> <span class="n">scheduled</span> <span class="n">task</span> <span class="ow">is</span> <span class="n">executed</span> <span class="n">on</span> <span class="n">each</span> <span class="n">specified</span> <span class="n">day</span> <span class="n">of</span> <span class="n">a</span> <span class="n">month</span><span class="o">.</span>
<span class="o">-</span> <span class="n">Cron</span><span class="p">:</span> <span class="p">(</span><span class="n">Available</span> <span class="ow">in</span> <span class="mf">1.60</span><span class="o">.</span><span class="mi">0</span><span class="o">+</span><span class="p">)</span> <span class="n">The</span> <span class="n">scheduled</span> <span class="n">task</span> <span class="ow">is</span> <span class="n">executed</span> <span class="n">based</span> <span class="n">on</span> <span class="n">the</span> <span class="n">specified</span> <span class="n">cron</span> <span class="n">expression</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>recurrence_value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies how often a scheduled task recurs. <strong>NOTE:</strong> You must specify <code class="docutils literal notranslate"><span class="pre">RecurrenceType</span></code>, <code class="docutils literal notranslate"><span class="pre">RecurrenceValue</span></code>, and <code class="docutils literal notranslate"><span class="pre">RecurrenceEndTime</span></code> at the same time. The valid value depends on <code class="docutils literal notranslate"><span class="pre">recurrence_type</span></code></p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- Daily: You can enter one value. Valid values: 1 to 31.
- Weekly: You can enter multiple values and separate them with commas (,). For example, the values 0 to 6 correspond to the days of the week in sequence from Sunday to Saturday.
- Monthly: You can enter two values in A-B format. Valid values of A and B: 1 to 31. The value of B must be greater than or equal to the value of A.
- Cron: You can enter a cron expression which is written in UTC and consists of five fields: minute, hour, day of month (date), month, and day of week. The expression can contain wildcard characters including commas (,), question marks (?), hyphens (-), asterisks (*), number signs (#), forward slashes (/), and the L and W letters.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>scaling_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the scaling group where the number of instances is modified when the scheduled task is triggered. After the <code class="docutils literal notranslate"><span class="pre">ScalingGroupId</span></code> parameter is specified, the scaling method of the scheduled task is to specify the number of instances in a scaling group. You must specify at least one of the following parameters: <code class="docutils literal notranslate"><span class="pre">MinValue</span></code>, <code class="docutils literal notranslate"><span class="pre">MaxValue</span></code>, and <code class="docutils literal notranslate"><span class="pre">DesiredCapacity</span></code>. <strong>NOTE:</strong> You cannot specify <code class="docutils literal notranslate"><span class="pre">scheduled_action</span></code> and <code class="docutils literal notranslate"><span class="pre">scaling_group_id</span></code> at the same time.</p></li>
<li><p><strong>scheduled_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The operation to be performed when a scheduled task is triggered. Enter the unique identifier of a scaling rule. <strong>NOTE:</strong> You cannot specify <code class="docutils literal notranslate"><span class="pre">scheduled_action</span></code> and <code class="docutils literal notranslate"><span class="pre">scaling_group_id</span></code> at the same time.</p></li>
<li><p><strong>scheduled_task_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Display name of the scheduled task, which must be 2-40 characters (English or Chinese) long.</p></li>
<li><p><strong>task_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether to start the scheduled task. Default to true.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScheduledTask.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScheduledTask.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the scheduled task, which is 2-200 characters (English or Chinese) long.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScheduledTask.desired_capacity">
<code class="sig-name descname">desired_capacity</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScheduledTask.desired_capacity" title="Permalink to this definition">¶</a></dt>
<dd><p>The expected number of instances in a scaling group when the scaling method of the scheduled task is to specify the number of instances in a scaling group. <strong>NOTE:</strong> You must specify the <code class="docutils literal notranslate"><span class="pre">DesiredCapacity</span></code> parameter when you create the scaling group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScheduledTask.launch_expiration_time">
<code class="sig-name descname">launch_expiration_time</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScheduledTask.launch_expiration_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time period during which a failed scheduled task is retried. Unit: seconds. Valid values: 0 to 21600. Default value: 600</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScheduledTask.launch_time">
<code class="sig-name descname">launch_time</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScheduledTask.launch_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time at which the scheduled task is triggered. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mmZ format. 
The time must be in UTC. You cannot enter a time point later than 90 days from the date of scheduled task creation.
If the <code class="docutils literal notranslate"><span class="pre">recurrence_type</span></code> parameter is specified, the task is executed repeatedly at the time specified by LaunchTime.
Otherwise, the task is only executed once at the date and time specified by LaunchTime.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScheduledTask.max_value">
<code class="sig-name descname">max_value</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScheduledTask.max_value" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of instances in a scaling group when the scaling method of the scheduled task is to specify the number of instances in a scaling group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScheduledTask.min_value">
<code class="sig-name descname">min_value</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScheduledTask.min_value" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum number of instances in a scaling group when the scaling method of the scheduled task is to specify the number of instances in a scaling group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScheduledTask.recurrence_end_time">
<code class="sig-name descname">recurrence_end_time</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScheduledTask.recurrence_end_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the end time after which the scheduled task is no longer repeated. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. 
The time must be in UTC. You cannot enter a time point later than 365 days from the date of scheduled task creation. <strong>NOTE:</strong> You must specify <code class="docutils literal notranslate"><span class="pre">RecurrenceType</span></code>, <code class="docutils literal notranslate"><span class="pre">RecurrenceValue</span></code>, and <code class="docutils literal notranslate"><span class="pre">RecurrenceEndTime</span></code> at the same time.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScheduledTask.recurrence_type">
<code class="sig-name descname">recurrence_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScheduledTask.recurrence_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the recurrence type of the scheduled task. <strong>NOTE:</strong> You must specify <code class="docutils literal notranslate"><span class="pre">RecurrenceType</span></code>, <code class="docutils literal notranslate"><span class="pre">RecurrenceValue</span></code>, and <code class="docutils literal notranslate"><span class="pre">RecurrenceEndTime</span></code> at the same time. Valid values:</p>
<ul class="simple">
<li><p>Daily: The scheduled task is executed once every specified number of days.</p></li>
<li><p>Weekly: The scheduled task is executed on each specified day of a week.</p></li>
<li><p>Monthly: The scheduled task is executed on each specified day of a month.</p></li>
<li><p>Cron: (Available in 1.60.0+) The scheduled task is executed based on the specified cron expression.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScheduledTask.recurrence_value">
<code class="sig-name descname">recurrence_value</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScheduledTask.recurrence_value" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies how often a scheduled task recurs. <strong>NOTE:</strong> You must specify <code class="docutils literal notranslate"><span class="pre">RecurrenceType</span></code>, <code class="docutils literal notranslate"><span class="pre">RecurrenceValue</span></code>, and <code class="docutils literal notranslate"><span class="pre">RecurrenceEndTime</span></code> at the same time. The valid value depends on <code class="docutils literal notranslate"><span class="pre">recurrence_type</span></code></p>
<ul class="simple">
<li><p>Daily: You can enter one value. Valid values: 1 to 31.</p></li>
<li><p>Weekly: You can enter multiple values and separate them with commas (,). For example, the values 0 to 6 correspond to the days of the week in sequence from Sunday to Saturday.</p></li>
<li><p>Monthly: You can enter two values in A-B format. Valid values of A and B: 1 to 31. The value of B must be greater than or equal to the value of A.</p></li>
<li><p>Cron: You can enter a cron expression which is written in UTC and consists of five fields: minute, hour, day of month (date), month, and day of week. The expression can contain wildcard characters including commas (,), question marks (?), hyphens (-), asterisks (*), number signs (#), forward slashes (/), and the L and W letters.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScheduledTask.scaling_group_id">
<code class="sig-name descname">scaling_group_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScheduledTask.scaling_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the scaling group where the number of instances is modified when the scheduled task is triggered. After the <code class="docutils literal notranslate"><span class="pre">ScalingGroupId</span></code> parameter is specified, the scaling method of the scheduled task is to specify the number of instances in a scaling group. You must specify at least one of the following parameters: <code class="docutils literal notranslate"><span class="pre">MinValue</span></code>, <code class="docutils literal notranslate"><span class="pre">MaxValue</span></code>, and <code class="docutils literal notranslate"><span class="pre">DesiredCapacity</span></code>. <strong>NOTE:</strong> You cannot specify <code class="docutils literal notranslate"><span class="pre">scheduled_action</span></code> and <code class="docutils literal notranslate"><span class="pre">scaling_group_id</span></code> at the same time.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScheduledTask.scheduled_action">
<code class="sig-name descname">scheduled_action</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScheduledTask.scheduled_action" title="Permalink to this definition">¶</a></dt>
<dd><p>The operation to be performed when a scheduled task is triggered. Enter the unique identifier of a scaling rule. <strong>NOTE:</strong> You cannot specify <code class="docutils literal notranslate"><span class="pre">scheduled_action</span></code> and <code class="docutils literal notranslate"><span class="pre">scaling_group_id</span></code> at the same time.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScheduledTask.scheduled_task_name">
<code class="sig-name descname">scheduled_task_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScheduledTask.scheduled_task_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Display name of the scheduled task, which must be 2-40 characters (English or Chinese) long.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_alicloud.ess.ScheduledTask.task_enabled">
<code class="sig-name descname">task_enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_alicloud.ess.ScheduledTask.task_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether to start the scheduled task. Default to true.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ess.ScheduledTask.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">desired_capacity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">launch_expiration_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">launch_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recurrence_end_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recurrence_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recurrence_value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheduled_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheduled_task_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">task_enabled</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.ScheduledTask.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ScheduledTask resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the scheduled task, which is 2-200 characters (English or Chinese) long.</p></li>
<li><p><strong>desired_capacity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The expected number of instances in a scaling group when the scaling method of the scheduled task is to specify the number of instances in a scaling group. <strong>NOTE:</strong> You must specify the <code class="docutils literal notranslate"><span class="pre">DesiredCapacity</span></code> parameter when you create the scaling group.</p></li>
<li><p><strong>launch_expiration_time</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The time period during which a failed scheduled task is retried. Unit: seconds. Valid values: 0 to 21600. Default value: 600</p></li>
<li><p><strong>launch_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time at which the scheduled task is triggered. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mmZ format. 
The time must be in UTC. You cannot enter a time point later than 90 days from the date of scheduled task creation.
If the <code class="docutils literal notranslate"><span class="pre">recurrence_type</span></code> parameter is specified, the task is executed repeatedly at the time specified by LaunchTime.
Otherwise, the task is only executed once at the date and time specified by LaunchTime.</p></li>
<li><p><strong>max_value</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum number of instances in a scaling group when the scaling method of the scheduled task is to specify the number of instances in a scaling group.</p></li>
<li><p><strong>min_value</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The minimum number of instances in a scaling group when the scaling method of the scheduled task is to specify the number of instances in a scaling group.</p></li>
<li><p><strong>recurrence_end_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the end time after which the scheduled task is no longer repeated. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. 
The time must be in UTC. You cannot enter a time point later than 365 days from the date of scheduled task creation. <strong>NOTE:</strong> You must specify <code class="docutils literal notranslate"><span class="pre">RecurrenceType</span></code>, <code class="docutils literal notranslate"><span class="pre">RecurrenceValue</span></code>, and <code class="docutils literal notranslate"><span class="pre">RecurrenceEndTime</span></code> at the same time.</p></li>
<li><p><strong>recurrence_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the recurrence type of the scheduled task. <strong>NOTE:</strong> You must specify <code class="docutils literal notranslate"><span class="pre">RecurrenceType</span></code>, <code class="docutils literal notranslate"><span class="pre">RecurrenceValue</span></code>, and <code class="docutils literal notranslate"><span class="pre">RecurrenceEndTime</span></code> at the same time. Valid values:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">Daily</span><span class="p">:</span> <span class="n">The</span> <span class="n">scheduled</span> <span class="n">task</span> <span class="ow">is</span> <span class="n">executed</span> <span class="n">once</span> <span class="n">every</span> <span class="n">specified</span> <span class="n">number</span> <span class="n">of</span> <span class="n">days</span><span class="o">.</span>
<span class="o">-</span> <span class="n">Weekly</span><span class="p">:</span> <span class="n">The</span> <span class="n">scheduled</span> <span class="n">task</span> <span class="ow">is</span> <span class="n">executed</span> <span class="n">on</span> <span class="n">each</span> <span class="n">specified</span> <span class="n">day</span> <span class="n">of</span> <span class="n">a</span> <span class="n">week</span><span class="o">.</span>
<span class="o">-</span> <span class="n">Monthly</span><span class="p">:</span> <span class="n">The</span> <span class="n">scheduled</span> <span class="n">task</span> <span class="ow">is</span> <span class="n">executed</span> <span class="n">on</span> <span class="n">each</span> <span class="n">specified</span> <span class="n">day</span> <span class="n">of</span> <span class="n">a</span> <span class="n">month</span><span class="o">.</span>
<span class="o">-</span> <span class="n">Cron</span><span class="p">:</span> <span class="p">(</span><span class="n">Available</span> <span class="ow">in</span> <span class="mf">1.60</span><span class="o">.</span><span class="mi">0</span><span class="o">+</span><span class="p">)</span> <span class="n">The</span> <span class="n">scheduled</span> <span class="n">task</span> <span class="ow">is</span> <span class="n">executed</span> <span class="n">based</span> <span class="n">on</span> <span class="n">the</span> <span class="n">specified</span> <span class="n">cron</span> <span class="n">expression</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>recurrence_value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies how often a scheduled task recurs. <strong>NOTE:</strong> You must specify <code class="docutils literal notranslate"><span class="pre">RecurrenceType</span></code>, <code class="docutils literal notranslate"><span class="pre">RecurrenceValue</span></code>, and <code class="docutils literal notranslate"><span class="pre">RecurrenceEndTime</span></code> at the same time. The valid value depends on <code class="docutils literal notranslate"><span class="pre">recurrence_type</span></code></p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- Daily: You can enter one value. Valid values: 1 to 31.
- Weekly: You can enter multiple values and separate them with commas (,). For example, the values 0 to 6 correspond to the days of the week in sequence from Sunday to Saturday.
- Monthly: You can enter two values in A-B format. Valid values of A and B: 1 to 31. The value of B must be greater than or equal to the value of A.
- Cron: You can enter a cron expression which is written in UTC and consists of five fields: minute, hour, day of month (date), month, and day of week. The expression can contain wildcard characters including commas (,), question marks (?), hyphens (-), asterisks (*), number signs (#), forward slashes (/), and the L and W letters.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>scaling_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the scaling group where the number of instances is modified when the scheduled task is triggered. After the <code class="docutils literal notranslate"><span class="pre">ScalingGroupId</span></code> parameter is specified, the scaling method of the scheduled task is to specify the number of instances in a scaling group. You must specify at least one of the following parameters: <code class="docutils literal notranslate"><span class="pre">MinValue</span></code>, <code class="docutils literal notranslate"><span class="pre">MaxValue</span></code>, and <code class="docutils literal notranslate"><span class="pre">DesiredCapacity</span></code>. <strong>NOTE:</strong> You cannot specify <code class="docutils literal notranslate"><span class="pre">scheduled_action</span></code> and <code class="docutils literal notranslate"><span class="pre">scaling_group_id</span></code> at the same time.</p></li>
<li><p><strong>scheduled_action</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The operation to be performed when a scheduled task is triggered. Enter the unique identifier of a scaling rule. <strong>NOTE:</strong> You cannot specify <code class="docutils literal notranslate"><span class="pre">scheduled_action</span></code> and <code class="docutils literal notranslate"><span class="pre">scaling_group_id</span></code> at the same time.</p></li>
<li><p><strong>scheduled_task_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Display name of the scheduled task, which must be 2-40 characters (English or Chinese) long.</p></li>
<li><p><strong>task_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether to start the scheduled task. Default to true.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_alicloud.ess.ScheduledTask.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.ScheduledTask.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ess.ScheduledTask.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.ScheduledTask.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_alicloud.ess.get_alarms">
<code class="sig-prename descclassname">pulumi_alicloud.ess.</code><code class="sig-name descname">get_alarms</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.get_alarms" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides available alarm resources.</p>
<blockquote>
<div><p><strong>NOTE</strong> Available in 1.72.0+</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of alarm IDs.</p></li>
<li><p><strong>metric_type</strong> (<em>str</em>) – The type for the alarm’s associated metric. Supported value: system, custom. “system” means the metric data is collected by Aliyun Cloud Monitor Service(CMS), “custom” means the metric data is upload to CMS by users. Defaults to system.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter resulting alarms by name.</p></li>
<li><p><strong>scaling_group_id</strong> (<em>str</em>) – Scaling group id the alarms belong to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.ess.get_lifecycle_hooks">
<code class="sig-prename descclassname">pulumi_alicloud.ess.</code><code class="sig-name descname">get_lifecycle_hooks</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.get_lifecycle_hooks" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides available lifecycle hook resources.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.72.0+</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">ds</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ess</span><span class="o">.</span><span class="n">get_lifecycle_hooks</span><span class="p">(</span><span class="n">name_regex</span><span class="o">=</span><span class="s2">&quot;lifecyclehook_name&quot;</span><span class="p">,</span>
    <span class="n">scaling_group_id</span><span class="o">=</span><span class="s2">&quot;scaling_group_id&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;firstLifecycleHook&quot;</span><span class="p">,</span> <span class="n">ds</span><span class="o">.</span><span class="n">hooks</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of lifecycle hook IDs.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter resulting lifecycle hook by name.</p></li>
<li><p><strong>scaling_group_id</strong> (<em>str</em>) – Scaling group id the lifecycle hooks belong to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.ess.get_notifications">
<code class="sig-prename descclassname">pulumi_alicloud.ess.</code><code class="sig-name descname">get_notifications</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.get_notifications" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides available notification resources.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.72.0+</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">ds</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ess</span><span class="o">.</span><span class="n">get_notifications</span><span class="p">(</span><span class="n">scaling_group_id</span><span class="o">=</span><span class="s2">&quot;scaling_group_id&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;firstNotification&quot;</span><span class="p">,</span> <span class="n">ds</span><span class="o">.</span><span class="n">notifications</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of notification ids.</p></li>
<li><p><strong>scaling_group_id</strong> (<em>str</em>) – Scaling group id the notifications belong to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.ess.get_scaling_configurations">
<code class="sig-prename descclassname">pulumi_alicloud.ess.</code><code class="sig-name descname">get_scaling_configurations</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.get_scaling_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides available scaling configuration resources.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">scalingconfigurations_ds</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ess</span><span class="o">.</span><span class="n">get_scaling_configurations</span><span class="p">(</span><span class="n">ids</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;scaling_configuration_id1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;scaling_configuration_id2&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">name_regex</span><span class="o">=</span><span class="s2">&quot;scaling_configuration_name&quot;</span><span class="p">,</span>
    <span class="n">scaling_group_id</span><span class="o">=</span><span class="s2">&quot;scaling_group_id&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;firstScalingRule&quot;</span><span class="p">,</span> <span class="n">scalingconfigurations_ds</span><span class="o">.</span><span class="n">configurations</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of scaling configuration IDs.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter resulting scaling configurations by name.</p></li>
<li><p><strong>scaling_group_id</strong> (<em>str</em>) – Scaling group id the scaling configurations belong to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.ess.get_scaling_groups">
<code class="sig-prename descclassname">pulumi_alicloud.ess.</code><code class="sig-name descname">get_scaling_groups</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.get_scaling_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides available scaling group resources.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">scalinggroups_ds</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ess</span><span class="o">.</span><span class="n">get_scaling_groups</span><span class="p">(</span><span class="n">ids</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;scaling_group_id1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;scaling_group_id2&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">name_regex</span><span class="o">=</span><span class="s2">&quot;scaling_group_name&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;firstScalingGroup&quot;</span><span class="p">,</span> <span class="n">scalinggroups_ds</span><span class="o">.</span><span class="n">groups</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of scaling group IDs.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter resulting scaling groups by name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.ess.get_scaling_rules">
<code class="sig-prename descclassname">pulumi_alicloud.ess.</code><code class="sig-name descname">get_scaling_rules</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scaling_group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.get_scaling_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides available scaling rule resources.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">scalingrules_ds</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ess</span><span class="o">.</span><span class="n">get_scaling_rules</span><span class="p">(</span><span class="n">ids</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;scaling_rule_id1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;scaling_rule_id2&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">name_regex</span><span class="o">=</span><span class="s2">&quot;scaling_rule_name&quot;</span><span class="p">,</span>
    <span class="n">scaling_group_id</span><span class="o">=</span><span class="s2">&quot;scaling_group_id&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;firstScalingRule&quot;</span><span class="p">,</span> <span class="n">scalingrules_ds</span><span class="o">.</span><span class="n">rules</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of scaling rule IDs.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter resulting scaling rules by name.</p></li>
<li><p><strong>scaling_group_id</strong> (<em>str</em>) – Scaling group id the scaling rules belong to.</p></li>
<li><p><strong>type</strong> (<em>str</em>) – Type of scaling rule.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_alicloud.ess.get_scheduled_tasks">
<code class="sig-prename descclassname">pulumi_alicloud.ess.</code><code class="sig-name descname">get_scheduled_tasks</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">output_file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheduled_action</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scheduled_task_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_alicloud.ess.get_scheduled_tasks" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides available scheduled task resources.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Available in 1.72.0+</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_alicloud</span> <span class="k">as</span> <span class="nn">alicloud</span>

<span class="n">ds</span> <span class="o">=</span> <span class="n">alicloud</span><span class="o">.</span><span class="n">ess</span><span class="o">.</span><span class="n">get_scheduled_tasks</span><span class="p">(</span><span class="n">name_regex</span><span class="o">=</span><span class="s2">&quot;scheduled_task_name&quot;</span><span class="p">,</span>
    <span class="n">scheduled_task_id</span><span class="o">=</span><span class="s2">&quot;scheduled_task_id&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;firstScheduledTask&quot;</span><span class="p">,</span> <span class="n">ds</span><span class="o">.</span><span class="n">tasks</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>ids</strong> (<em>list</em>) – A list of scheduled task IDs.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – A regex string to filter resulting scheduled tasks by name.</p></li>
<li><p><strong>scheduled_action</strong> (<em>str</em>) – The operation to be performed when a scheduled task is triggered.</p></li>
<li><p><strong>scheduled_task_id</strong> (<em>str</em>) – The id of the scheduled task.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
