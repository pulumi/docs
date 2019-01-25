<div class="section" id="module-pulumi_azure.monitoring">
<span id="monitoring"></span><h1>monitoring<a class="headerlink" href="#module-pulumi_azure.monitoring" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.monitoring.ActionGroup">
<em class="property">class </em><code class="descclassname">pulumi_azure.monitoring.</code><code class="descname">ActionGroup</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>email_receivers=None</em>, <em>enabled=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>short_name=None</em>, <em>sms_receivers=None</em>, <em>tags=None</em>, <em>webhook_receivers=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Action Group within Azure Monitor.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>email_receivers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <cite>email_receiver</cite> blocks as defined below.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this action group is enabled. If an action group is not enabled, then none of its receivers will receive communications. Defaults to <cite>true</cite>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Action Group instance.</li>
<li><strong>short_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The short name of the action group. This will be used in SMS messages.</li>
<li><strong>sms_receivers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <a href="#id1"><span class="problematic" id="id2">`</span></a>sms_receiver ` blocks as defined below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>webhook_receivers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <a href="#id3"><span class="problematic" id="id4">`</span></a>webhook_receiver ` blocks as defined below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.email_receivers">
<code class="descname">email_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.email_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <cite>email_receiver</cite> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this action group is enabled. If an action group is not enabled, then none of its receivers will receive communications. Defaults to <cite>true</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Action Group instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.short_name">
<code class="descname">short_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.short_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The short name of the action group. This will be used in SMS messages.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.sms_receivers">
<code class="descname">sms_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.sms_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <a href="#id5"><span class="problematic" id="id6">`</span></a>sms_receiver ` blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.webhook_receivers">
<code class="descname">webhook_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.webhook_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <a href="#id7"><span class="problematic" id="id8">`</span></a>webhook_receiver ` blocks as defined below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.monitoring.ActionGroup.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.ActionGroup.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.ActivityLogAlert">
<em class="property">class </em><code class="descclassname">pulumi_azure.monitoring.</code><code class="descname">ActivityLogAlert</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>actions=None</em>, <em>criteria=None</em>, <em>description=None</em>, <em>enabled=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>scopes=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.ActivityLogAlert" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ActivityLogAlert resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[list] actions
:param pulumi.Input[dict] criteria
:param pulumi.Input[str] description
:param pulumi.Input[bool] enabled
:param pulumi.Input[str] name
:param pulumi.Input[str] resource_group_name
:param pulumi.Input[list] scopes
:param pulumi.Input[dict] tags</p>
<dl class="method">
<dt id="pulumi_azure.monitoring.ActivityLogAlert.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.ActivityLogAlert.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.ActivityLogAlert.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.ActivityLogAlert.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.AlertRule">
<em class="property">class </em><code class="descclassname">pulumi_azure.monitoring.</code><code class="descname">AlertRule</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>aggregation=None</em>, <em>description=None</em>, <em>email_action=None</em>, <em>enabled=None</em>, <em>location=None</em>, <em>metric_name=None</em>, <em>name=None</em>, <em>operator=None</em>, <em>period=None</em>, <em>resource_group_name=None</em>, <em>resource_id=None</em>, <em>tags=None</em>, <em>threshold=None</em>, <em>webhook_action=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a [metric-based alert rule](<a class="reference external" href="https://docs.microsoft.com/en-us/azure/monitoring-and-diagnostics/monitor-quick-resource-metric-alert-portal">https://docs.microsoft.com/en-us/azure/monitoring-and-diagnostics/monitor-quick-resource-metric-alert-portal</a>) in Azure Monitor.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>aggregation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines how the metric data is combined over time. Possible values are <cite>Average</cite>, <cite>Minimum</cite>, <cite>Maximum</cite>, <cite>Total</cite>, and <cite>Last</cite>.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A verbose description of the alert rule that will be included in the alert email.</li>
<li><strong>email_action</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <cite>email_action</cite> block as defined below.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <cite>true</cite>, the alert rule is enabled. Defaults to <cite>true</cite>.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>metric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The metric that defines what the rule monitors.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the alert rule. Changing this forces a new resource to be created.</li>
<li><strong>operator</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The operator used to compare the metric data and the threshold. Possible values are <cite>GreaterThan</cite>, <cite>GreaterThanOrEqual</cite>, <cite>LessThan</cite>, and <cite>LessThanOrEqual</cite>.</li>
<li><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The period of time formatted in [ISO 8601 duration format](<a class="reference external" href="https://en.wikipedia.org/wiki/ISO_8601#Durations">https://en.wikipedia.org/wiki/ISO_8601#Durations</a>) that is used to monitor the alert activity based on the threshold. The period must be between 5 minutes and 1 day.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the alert rule. Changing this forces a new resource to be created.</li>
<li><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the resource monitored by the alert rule.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource. Changing this forces a new resource to be created.</li>
<li><strong>threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The threshold value that activates the alert.</li>
<li><strong>webhook_action</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <cite>webhook_action</cite> block as defined below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.monitoring.AlertRule.aggregation">
<code class="descname">aggregation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.aggregation" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines how the metric data is combined over time. Possible values are <cite>Average</cite>, <cite>Minimum</cite>, <cite>Maximum</cite>, <cite>Total</cite>, and <cite>Last</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AlertRule.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A verbose description of the alert rule that will be included in the alert email.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AlertRule.email_action">
<code class="descname">email_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.email_action" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>email_action</cite> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AlertRule.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>If <cite>true</cite>, the alert rule is enabled. Defaults to <cite>true</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AlertRule.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AlertRule.metric_name">
<code class="descname">metric_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.metric_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The metric that defines what the rule monitors.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AlertRule.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the alert rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AlertRule.operator">
<code class="descname">operator</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.operator" title="Permalink to this definition">¶</a></dt>
<dd><p>The operator used to compare the metric data and the threshold. Possible values are <cite>GreaterThan</cite>, <cite>GreaterThanOrEqual</cite>, <cite>LessThan</cite>, and <cite>LessThanOrEqual</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AlertRule.period">
<code class="descname">period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.period" title="Permalink to this definition">¶</a></dt>
<dd><p>The period of time formatted in [ISO 8601 duration format](<a class="reference external" href="https://en.wikipedia.org/wiki/ISO_8601#Durations">https://en.wikipedia.org/wiki/ISO_8601#Durations</a>) that is used to monitor the alert activity based on the threshold. The period must be between 5 minutes and 1 day.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AlertRule.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the alert rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AlertRule.resource_id">
<code class="descname">resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the resource monitored by the alert rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AlertRule.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AlertRule.threshold">
<code class="descname">threshold</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.threshold" title="Permalink to this definition">¶</a></dt>
<dd><p>The threshold value that activates the alert.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AlertRule.webhook_action">
<code class="descname">webhook_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.webhook_action" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>webhook_action</cite> block as defined below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.monitoring.AlertRule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.AlertRule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.DiagnosticSetting">
<em class="property">class </em><code class="descclassname">pulumi_azure.monitoring.</code><code class="descname">DiagnosticSetting</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>eventhub_authorization_rule_id=None</em>, <em>eventhub_name=None</em>, <em>logs=None</em>, <em>log_analytics_workspace_id=None</em>, <em>metrics=None</em>, <em>name=None</em>, <em>storage_account_id=None</em>, <em>target_resource_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Diagnostic Setting for an existing Resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>eventhub_authorization_rule_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of an Event Hub Namespace Authorization Rule used to send Diagnostics Data. Changing this forces a new resource to be created.</li>
<li><strong>eventhub_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Event Hub where Diagnostics Data should be sent. Changing this forces a new resource to be created.</li>
<li><strong>logs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <cite>log</cite> blocks as defined below.</li>
<li><strong>log_analytics_workspace_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of a Log Analytics Workspace where Diagnostics Data should be sent. Changing this forces a new resource to be created.</li>
<li><strong>metrics</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <cite>metric</cite> blocks as defined below.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Diagnostic Setting. Changing this forces a new resource to be created.</li>
<li><strong>storage_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – With this parameter you can specify a storage account which should be used to send the logs to. Parameter must be a valid Azure Resource ID. Changing this forces a new resource to be created.</li>
<li><strong>target_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of an existing Resource on which to configure Diagnostic Settings. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.monitoring.DiagnosticSetting.eventhub_authorization_rule_id">
<code class="descname">eventhub_authorization_rule_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting.eventhub_authorization_rule_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the ID of an Event Hub Namespace Authorization Rule used to send Diagnostics Data. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.DiagnosticSetting.eventhub_name">
<code class="descname">eventhub_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting.eventhub_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Event Hub where Diagnostics Data should be sent. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.DiagnosticSetting.logs">
<code class="descname">logs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting.logs" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <cite>log</cite> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.DiagnosticSetting.log_analytics_workspace_id">
<code class="descname">log_analytics_workspace_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting.log_analytics_workspace_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the ID of a Log Analytics Workspace where Diagnostics Data should be sent. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.DiagnosticSetting.metrics">
<code class="descname">metrics</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting.metrics" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <cite>metric</cite> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.DiagnosticSetting.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Diagnostic Setting. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.DiagnosticSetting.storage_account_id">
<code class="descname">storage_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting.storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>With this parameter you can specify a storage account which should be used to send the logs to. Parameter must be a valid Azure Resource ID. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.DiagnosticSetting.target_resource_id">
<code class="descname">target_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting.target_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of an existing Resource on which to configure Diagnostic Settings. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.monitoring.DiagnosticSetting.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.DiagnosticSetting.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.GetActionGroupResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.monitoring.</code><code class="descname">GetActionGroupResult</code><span class="sig-paren">(</span><em>email_receivers=None</em>, <em>enabled=None</em>, <em>short_name=None</em>, <em>sms_receivers=None</em>, <em>webhook_receivers=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getActionGroup.</p>
<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetActionGroupResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.monitoring.GetDiagnosticCategoriesResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.monitoring.</code><code class="descname">GetDiagnosticCategoriesResult</code><span class="sig-paren">(</span><em>logs=None</em>, <em>metrics=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.GetDiagnosticCategoriesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDiagnosticCategories.</p>
<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetDiagnosticCategoriesResult.logs">
<code class="descname">logs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetDiagnosticCategoriesResult.logs" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the Log Categories supported for this Resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetDiagnosticCategoriesResult.metrics">
<code class="descname">metrics</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetDiagnosticCategoriesResult.metrics" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the Metric Categories supported for this Resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetDiagnosticCategoriesResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetDiagnosticCategoriesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.monitoring.GetLogProfileResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.monitoring.</code><code class="descname">GetLogProfileResult</code><span class="sig-paren">(</span><em>categories=None</em>, <em>locations=None</em>, <em>retention_policy=None</em>, <em>servicebus_rule_id=None</em>, <em>storage_account_id=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.GetLogProfileResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getLogProfile.</p>
<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetLogProfileResult.categories">
<code class="descname">categories</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetLogProfileResult.categories" title="Permalink to this definition">¶</a></dt>
<dd><p>List of categories of the logs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetLogProfileResult.locations">
<code class="descname">locations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetLogProfileResult.locations" title="Permalink to this definition">¶</a></dt>
<dd><p>List of regions for which Activity Log events are stored or streamed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetLogProfileResult.servicebus_rule_id">
<code class="descname">servicebus_rule_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetLogProfileResult.servicebus_rule_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The service bus (or event hub) rule ID of the service bus (or event hub) namespace in which the Activity Log is streamed to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetLogProfileResult.storage_account_id">
<code class="descname">storage_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetLogProfileResult.storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource id of the storage account in which the Activity Log is stored.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetLogProfileResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetLogProfileResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.monitoring.LogProfile">
<em class="property">class </em><code class="descclassname">pulumi_azure.monitoring.</code><code class="descname">LogProfile</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>categories=None</em>, <em>locations=None</em>, <em>name=None</em>, <em>retention_policy=None</em>, <em>servicebus_rule_id=None</em>, <em>storage_account_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.LogProfile" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a [Log Profile](<a class="reference external" href="https://docs.microsoft.com/en-us/azure/monitoring-and-diagnostics/monitoring-overview-activity-logs#export-the-activity-log-with-a-log-profile">https://docs.microsoft.com/en-us/azure/monitoring-and-diagnostics/monitoring-overview-activity-logs#export-the-activity-log-with-a-log-profile</a>). A Log Profile configures how Activity Logs are exported.</p>
<p>-&gt; <strong>NOTE:</strong> It’s only possible to configure one Log Profile per Subscription. If you are trying to create more than one Log Profile, an error with <cite>StatusCode=409</cite> will occur.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>categories</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of categories of the logs.</li>
<li><strong>locations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of regions for which Activity Log events are stored or streamed.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Log Profile. Changing this forces a
new resource to be created.</li>
<li><strong>retention_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <cite>retention_policy</cite> block as documented below. A retention policy for how long Activity Logs are retained in the storage account.</li>
<li><strong>servicebus_rule_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service bus (or event hub) rule ID of the service bus (or event hub) namespace in which the Activity Log is streamed to. At least one of <cite>storage_account_id</cite> or <cite>servicebus_rule_id</cite> must be set.</li>
<li><strong>storage_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource ID of the storage account in which the Activity Log is stored. At least one of <cite>storage_account_id</cite> or <cite>servicebus_rule_id</cite> must be set.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.monitoring.LogProfile.categories">
<code class="descname">categories</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.LogProfile.categories" title="Permalink to this definition">¶</a></dt>
<dd><p>List of categories of the logs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.LogProfile.locations">
<code class="descname">locations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.LogProfile.locations" title="Permalink to this definition">¶</a></dt>
<dd><p>List of regions for which Activity Log events are stored or streamed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.LogProfile.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.LogProfile.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Log Profile. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.LogProfile.retention_policy">
<code class="descname">retention_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.LogProfile.retention_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A <cite>retention_policy</cite> block as documented below. A retention policy for how long Activity Logs are retained in the storage account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.LogProfile.servicebus_rule_id">
<code class="descname">servicebus_rule_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.LogProfile.servicebus_rule_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The service bus (or event hub) rule ID of the service bus (or event hub) namespace in which the Activity Log is streamed to. At least one of <cite>storage_account_id</cite> or <cite>servicebus_rule_id</cite> must be set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.LogProfile.storage_account_id">
<code class="descname">storage_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.LogProfile.storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource ID of the storage account in which the Activity Log is stored. At least one of <cite>storage_account_id</cite> or <cite>servicebus_rule_id</cite> must be set.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.monitoring.LogProfile.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.LogProfile.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.LogProfile.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.LogProfile.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.MetricAlert">
<em class="property">class </em><code class="descclassname">pulumi_azure.monitoring.</code><code class="descname">MetricAlert</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>actions=None</em>, <em>auto_mitigate=None</em>, <em>criterias=None</em>, <em>description=None</em>, <em>enabled=None</em>, <em>frequency=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>scopes=None</em>, <em>severity=None</em>, <em>tags=None</em>, <em>window_size=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a MetricAlert resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[list] actions
:param pulumi.Input[bool] auto_mitigate
:param pulumi.Input[list] criterias
:param pulumi.Input[str] description
:param pulumi.Input[bool] enabled
:param pulumi.Input[str] frequency
:param pulumi.Input[str] name
:param pulumi.Input[str] resource_group_name
:param pulumi.Input[str] scopes
:param pulumi.Input[int] severity
:param pulumi.Input[dict] tags
:param pulumi.Input[str] window_size</p>
<dl class="method">
<dt id="pulumi_azure.monitoring.MetricAlert.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.MetricAlert.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.get_diagnostic_categories">
<code class="descclassname">pulumi_azure.monitoring.</code><code class="descname">get_diagnostic_categories</code><span class="sig-paren">(</span><em>resource_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.get_diagnostic_categories" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about the Monitor Diagnostics Categories supported by an existing Resource.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.monitoring.get_log_profile">
<code class="descclassname">pulumi_azure.monitoring.</code><code class="descname">get_log_profile</code><span class="sig-paren">(</span><em>name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.get_log_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access the properties of a Log Profile.</p>
</dd></dl>

</div>
