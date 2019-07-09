---
---

<div class="section" id="monitoring">
<h1>monitoring<a class="headerlink" href="#monitoring" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azure">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azure/issues">terraform-providers/terraform-provider-azure repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_azure.monitoring"></span><dl class="class">
<dt id="pulumi_azure.monitoring.ActionGroup">
<em class="property">class </em><code class="descclassname">pulumi_azure.monitoring.</code><code class="descname">ActionGroup</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>email_receivers=None</em>, <em>enabled=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>short_name=None</em>, <em>sms_receivers=None</em>, <em>tags=None</em>, <em>webhook_receivers=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Action Group within Azure Monitor.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>email_receivers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">email_receiver</span></code> blocks as defined below.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this action group is enabled. If an action group is not enabled, then none of its receivers will receive communications. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the webhook receiver. Names must be unique (case-insensitive) across all receivers within an action group.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Action Group instance.</li>
<li><strong>short_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The short name of the action group. This will be used in SMS messages.</li>
<li><strong>sms_receivers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">sms_receiver</span></code> blocks as defined below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>webhook_receivers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">webhook_receiver</span></code> blocks as defined below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_action_group.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_action_group.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.email_receivers">
<code class="descname">email_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.email_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">email_receiver</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this action group is enabled. If an action group is not enabled, then none of its receivers will receive communications. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
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
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">sms_receiver</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActionGroup.webhook_receivers">
<code class="descname">webhook_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActionGroup.webhook_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">webhook_receiver</span></code> blocks as defined below.</p>
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
<em class="property">class </em><code class="descclassname">pulumi_azure.monitoring.</code><code class="descname">ActivityLogAlert</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>actions=None</em>, <em>criteria=None</em>, <em>description=None</em>, <em>enabled=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>scopes=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.ActivityLogAlert" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Activity Log Alert within Azure Monitor.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">action</span></code> blocks as defined below.</li>
<li><strong>criteria</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">criteria</span></code> block as defined below.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of this activity log alert.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should this Activity Log Alert be enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the activity log alert. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the activity log alert instance.</li>
<li><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The Scope at which the Activity Log should be applied, for example a the Resource ID of a Subscription or a Resource (such as a Storage Account).</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_activity_log_alert.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_activity_log_alert.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActivityLogAlert.actions">
<code class="descname">actions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActivityLogAlert.actions" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">action</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActivityLogAlert.criteria">
<code class="descname">criteria</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActivityLogAlert.criteria" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">criteria</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActivityLogAlert.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActivityLogAlert.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of this activity log alert.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActivityLogAlert.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActivityLogAlert.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Should this Activity Log Alert be enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActivityLogAlert.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActivityLogAlert.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the activity log alert. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActivityLogAlert.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActivityLogAlert.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the activity log alert instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActivityLogAlert.scopes">
<code class="descname">scopes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActivityLogAlert.scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>The Scope at which the Activity Log should be applied, for example a the Resource ID of a Subscription or a Resource (such as a Storage Account).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.ActivityLogAlert.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.ActivityLogAlert.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

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
<em class="property">class </em><code class="descclassname">pulumi_azure.monitoring.</code><code class="descname">AlertRule</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>aggregation=None</em>, <em>description=None</em>, <em>email_action=None</em>, <em>enabled=None</em>, <em>location=None</em>, <em>metric_name=None</em>, <em>name=None</em>, <em>operator=None</em>, <em>period=None</em>, <em>resource_group_name=None</em>, <em>resource_id=None</em>, <em>tags=None</em>, <em>threshold=None</em>, <em>webhook_action=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a <a class="reference external" href="https://docs.microsoft.com/en-us/azure/monitoring-and-diagnostics/monitor-quick-resource-metric-alert-portal">metric-based alert rule</a> in Azure Monitor.</p>
<blockquote>
<div><strong>NOTE:</strong> This resource has been deprecated in favour of the <code class="docutils literal notranslate"><span class="pre">azurerm_monitor_metric_alertrule</span></code> resource and will be removed in the next major version of the AzureRM Provider. The new resource shares the same fields as this one, and information on migrating across can be found in this guide.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>aggregation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines how the metric data is combined over time. Possible values are <code class="docutils literal notranslate"><span class="pre">Average</span></code>, <code class="docutils literal notranslate"><span class="pre">Minimum</span></code>, <code class="docutils literal notranslate"><span class="pre">Maximum</span></code>, <code class="docutils literal notranslate"><span class="pre">Total</span></code>, and <code class="docutils literal notranslate"><span class="pre">Last</span></code>.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A verbose description of the alert rule that will be included in the alert email.</li>
<li><strong>email_action</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">email_action</span></code> block as defined below.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, the alert rule is enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>metric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The metric that defines what the rule monitors.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the alert rule. Changing this forces a new resource to be created.</li>
<li><strong>operator</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The operator used to compare the metric data and the threshold. Possible values are <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code>, and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</li>
<li><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The period of time formatted in <a class="reference external" href="https://en.wikipedia.org/wiki/ISO_8601#Durations">ISO 8601 duration format</a> that is used to monitor the alert activity based on the threshold. The period must be between 5 minutes and 1 day.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the alert rule. Changing this forces a new resource to be created.</li>
<li><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the resource monitored by the alert rule.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource. Changing this forces a new resource to be created.</li>
<li><strong>threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The threshold value that activates the alert.</li>
<li><strong>webhook_action</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">webhook_action</span></code> block as defined below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/metric_alertrule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/metric_alertrule.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.monitoring.AlertRule.aggregation">
<code class="descname">aggregation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.aggregation" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines how the metric data is combined over time. Possible values are <code class="docutils literal notranslate"><span class="pre">Average</span></code>, <code class="docutils literal notranslate"><span class="pre">Minimum</span></code>, <code class="docutils literal notranslate"><span class="pre">Maximum</span></code>, <code class="docutils literal notranslate"><span class="pre">Total</span></code>, and <code class="docutils literal notranslate"><span class="pre">Last</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AlertRule.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A verbose description of the alert rule that will be included in the alert email.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AlertRule.email_action">
<code class="descname">email_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.email_action" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">email_action</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AlertRule.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">true</span></code>, the alert rule is enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
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
<dd><p>The operator used to compare the metric data and the threshold. Possible values are <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code>, and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AlertRule.period">
<code class="descname">period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AlertRule.period" title="Permalink to this definition">¶</a></dt>
<dd><p>The period of time formatted in <a class="reference external" href="https://en.wikipedia.org/wiki/ISO_8601#Durations">ISO 8601 duration format</a> that is used to monitor the alert activity based on the threshold. The period must be between 5 minutes and 1 day.</p>
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
<dd><p>A <code class="docutils literal notranslate"><span class="pre">webhook_action</span></code> block as defined below.</p>
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
<dt id="pulumi_azure.monitoring.AutoscaleSetting">
<em class="property">class </em><code class="descclassname">pulumi_azure.monitoring.</code><code class="descname">AutoscaleSetting</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>enabled=None</em>, <em>location=None</em>, <em>name=None</em>, <em>notification=None</em>, <em>profiles=None</em>, <em>resource_group_name=None</em>, <em>tags=None</em>, <em>target_resource_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.AutoscaleSetting" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a AutoScale Setting which can be applied to Virtual Machine Scale Sets, App Services and other scalable resources.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether automatic scaling is enabled for the target resource. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the AutoScale Setting should exist. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the AutoScale Setting. Changing this forces a new resource to be created.</li>
<li><strong>notification</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies a <code class="docutils literal notranslate"><span class="pre">notification</span></code> block as defined below.</li>
<li><strong>profiles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies one or more (up to 20) <code class="docutils literal notranslate"><span class="pre">profile</span></code> blocks as defined below.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in the AutoScale Setting should be created. Changing this forces a new resource to be created.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>target_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the resource ID of the resource that the autoscale setting should be added to.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_autoscale_setting.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_autoscale_setting.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.monitoring.AutoscaleSetting.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AutoscaleSetting.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether automatic scaling is enabled for the target resource. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AutoscaleSetting.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AutoscaleSetting.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the AutoScale Setting should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AutoscaleSetting.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AutoscaleSetting.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the AutoScale Setting. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AutoscaleSetting.notification">
<code class="descname">notification</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AutoscaleSetting.notification" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a <code class="docutils literal notranslate"><span class="pre">notification</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AutoscaleSetting.profiles">
<code class="descname">profiles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AutoscaleSetting.profiles" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies one or more (up to 20) <code class="docutils literal notranslate"><span class="pre">profile</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AutoscaleSetting.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AutoscaleSetting.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in the AutoScale Setting should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AutoscaleSetting.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AutoscaleSetting.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.AutoscaleSetting.target_resource_id">
<code class="descname">target_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.AutoscaleSetting.target_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the resource ID of the resource that the autoscale setting should be added to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.monitoring.AutoscaleSetting.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.AutoscaleSetting.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.AutoscaleSetting.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.AutoscaleSetting.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<em class="property">class </em><code class="descclassname">pulumi_azure.monitoring.</code><code class="descname">DiagnosticSetting</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>eventhub_authorization_rule_id=None</em>, <em>eventhub_name=None</em>, <em>logs=None</em>, <em>log_analytics_workspace_id=None</em>, <em>metrics=None</em>, <em>name=None</em>, <em>storage_account_id=None</em>, <em>target_resource_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Diagnostic Setting for an existing Resource.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>eventhub_authorization_rule_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of an Event Hub Namespace Authorization Rule used to send Diagnostics Data. Changing this forces a new resource to be created.</li>
<li><strong>eventhub_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Event Hub where Diagnostics Data should be sent. Changing this forces a new resource to be created.</li>
<li><strong>logs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">log</span></code> blocks as defined below.</li>
<li><strong>log_analytics_workspace_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of a Log Analytics Workspace where Diagnostics Data should be sent. Changing this forces a new resource to be created.</li>
<li><strong>metrics</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">metric</span></code> blocks as defined below.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Diagnostic Setting. Changing this forces a new resource to be created.</li>
<li><strong>storage_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – With this parameter you can specify a storage account which should be used to send the logs to. Parameter must be a valid Azure Resource ID. Changing this forces a new resource to be created.</li>
<li><strong>target_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of an existing Resource on which to configure Diagnostic Settings. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_diagnostic_setting.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_diagnostic_setting.html.markdown</a>.</div></blockquote>
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
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">log</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.DiagnosticSetting.log_analytics_workspace_id">
<code class="descname">log_analytics_workspace_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting.log_analytics_workspace_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the ID of a Log Analytics Workspace where Diagnostics Data should be sent. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.DiagnosticSetting.metrics">
<code class="descname">metrics</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.DiagnosticSetting.metrics" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">metric</span></code> blocks as defined below.</p>
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
<em class="property">class </em><code class="descclassname">pulumi_azure.monitoring.</code><code class="descname">GetActionGroupResult</code><span class="sig-paren">(</span><em>email_receivers=None</em>, <em>enabled=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>short_name=None</em>, <em>sms_receivers=None</em>, <em>webhook_receivers=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getActionGroup.</p>
<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetActionGroupResult.email_receivers">
<code class="descname">email_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult.email_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">email_receiver</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetActionGroupResult.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this action group is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetActionGroupResult.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the webhook receiver.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetActionGroupResult.short_name">
<code class="descname">short_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult.short_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The short name of the action group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetActionGroupResult.sms_receivers">
<code class="descname">sms_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult.sms_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">sms_receiver</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetActionGroupResult.webhook_receivers">
<code class="descname">webhook_receivers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult.webhook_receivers" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">webhook_receiver</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.GetActionGroupResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.GetActionGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.monitoring.GetDiagnosticCategoriesResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.monitoring.</code><code class="descname">GetDiagnosticCategoriesResult</code><span class="sig-paren">(</span><em>logs=None</em>, <em>metrics=None</em>, <em>resource_id=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.GetDiagnosticCategoriesResult" title="Permalink to this definition">¶</a></dt>
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
<em class="property">class </em><code class="descclassname">pulumi_azure.monitoring.</code><code class="descname">GetLogProfileResult</code><span class="sig-paren">(</span><em>categories=None</em>, <em>locations=None</em>, <em>name=None</em>, <em>retention_policy=None</em>, <em>servicebus_rule_id=None</em>, <em>storage_account_id=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.GetLogProfileResult" title="Permalink to this definition">¶</a></dt>
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
<em class="property">class </em><code class="descclassname">pulumi_azure.monitoring.</code><code class="descname">LogProfile</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>categories=None</em>, <em>locations=None</em>, <em>name=None</em>, <em>retention_policy=None</em>, <em>servicebus_rule_id=None</em>, <em>storage_account_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.LogProfile" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a <a class="reference external" href="https://docs.microsoft.com/en-us/azure/monitoring-and-diagnostics/monitoring-overview-activity-logs#export-the-activity-log-with-a-log-profile">Log Profile</a>. A Log Profile configures how Activity Logs are exported.</p>
<blockquote>
<div><strong>NOTE:</strong> It’s only possible to configure one Log Profile per Subscription. If you are trying to create more than one Log Profile, an error with <code class="docutils literal notranslate"><span class="pre">StatusCode=409</span></code> will occur.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>categories</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of categories of the logs.</li>
<li><strong>locations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of regions for which Activity Log events are stored or streamed.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Log Profile. Changing this forces a
new resource to be created.</li>
<li><strong>retention_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">retention_policy</span></code> block as documented below. A retention policy for how long Activity Logs are retained in the storage account.</li>
<li><strong>servicebus_rule_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service bus (or event hub) rule ID of the service bus (or event hub) namespace in which the Activity Log is streamed to. At least one of <code class="docutils literal notranslate"><span class="pre">storage_account_id</span></code> or <code class="docutils literal notranslate"><span class="pre">servicebus_rule_id</span></code> must be set.</li>
<li><strong>storage_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource ID of the storage account in which the Activity Log is stored. At least one of <code class="docutils literal notranslate"><span class="pre">storage_account_id</span></code> or <code class="docutils literal notranslate"><span class="pre">servicebus_rule_id</span></code> must be set.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_log_profile.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_log_profile.html.markdown</a>.</div></blockquote>
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
<dd><p>A <code class="docutils literal notranslate"><span class="pre">retention_policy</span></code> block as documented below. A retention policy for how long Activity Logs are retained in the storage account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.LogProfile.servicebus_rule_id">
<code class="descname">servicebus_rule_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.LogProfile.servicebus_rule_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The service bus (or event hub) rule ID of the service bus (or event hub) namespace in which the Activity Log is streamed to. At least one of <code class="docutils literal notranslate"><span class="pre">storage_account_id</span></code> or <code class="docutils literal notranslate"><span class="pre">servicebus_rule_id</span></code> must be set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.LogProfile.storage_account_id">
<code class="descname">storage_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.LogProfile.storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource ID of the storage account in which the Activity Log is stored. At least one of <code class="docutils literal notranslate"><span class="pre">storage_account_id</span></code> or <code class="docutils literal notranslate"><span class="pre">servicebus_rule_id</span></code> must be set.</p>
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
<em class="property">class </em><code class="descclassname">pulumi_azure.monitoring.</code><code class="descname">MetricAlert</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>actions=None</em>, <em>auto_mitigate=None</em>, <em>criterias=None</em>, <em>description=None</em>, <em>enabled=None</em>, <em>frequency=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>scopes=None</em>, <em>severity=None</em>, <em>tags=None</em>, <em>window_size=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Metric Alert within Azure Monitor.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>actions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">action</span></code> blocks as defined below.</li>
<li><strong>auto_mitigate</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the alerts in this Metric Alert be auto resolved? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>criterias</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">criteria</span></code> blocks as defined below.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of this Metric Alert.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should this Metric Alert be enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
<li><strong>frequency</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The evaluation frequency of this Metric Alert, represented in ISO 8601 duration format. Possible values are <code class="docutils literal notranslate"><span class="pre">PT1M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT5M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT15M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT30M</span></code> and <code class="docutils literal notranslate"><span class="pre">PT1H</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">PT1M</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Metric Alert. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Metric Alert instance.</li>
<li><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource ID at which the metric criteria should be applied.</li>
<li><strong>severity</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The severity of this Metric Alert. Possible values are <code class="docutils literal notranslate"><span class="pre">0</span></code>, <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">2</span></code>, <code class="docutils literal notranslate"><span class="pre">3</span></code> and <code class="docutils literal notranslate"><span class="pre">4</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">3</span></code>.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>window_size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The period of time that is used to monitor alert activity, represented in ISO 8601 duration format. This value must be greater than <code class="docutils literal notranslate"><span class="pre">frequency</span></code>. Possible values are <code class="docutils literal notranslate"><span class="pre">PT1M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT5M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT15M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT30M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT1H</span></code>, <code class="docutils literal notranslate"><span class="pre">PT6H</span></code>, <code class="docutils literal notranslate"><span class="pre">PT12H</span></code> and <code class="docutils literal notranslate"><span class="pre">P1D</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">PT5M</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_metric_alert.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_metric_alert.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlert.actions">
<code class="descname">actions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.actions" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">action</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlert.auto_mitigate">
<code class="descname">auto_mitigate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.auto_mitigate" title="Permalink to this definition">¶</a></dt>
<dd><p>Should the alerts in this Metric Alert be auto resolved? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlert.criterias">
<code class="descname">criterias</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.criterias" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">criteria</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlert.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of this Metric Alert.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlert.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Should this Metric Alert be enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlert.frequency">
<code class="descname">frequency</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.frequency" title="Permalink to this definition">¶</a></dt>
<dd><p>The evaluation frequency of this Metric Alert, represented in ISO 8601 duration format. Possible values are <code class="docutils literal notranslate"><span class="pre">PT1M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT5M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT15M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT30M</span></code> and <code class="docutils literal notranslate"><span class="pre">PT1H</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">PT1M</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlert.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Metric Alert. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlert.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Metric Alert instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlert.scopes">
<code class="descname">scopes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource ID at which the metric criteria should be applied.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlert.severity">
<code class="descname">severity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.severity" title="Permalink to this definition">¶</a></dt>
<dd><p>The severity of this Metric Alert. Possible values are <code class="docutils literal notranslate"><span class="pre">0</span></code>, <code class="docutils literal notranslate"><span class="pre">1</span></code>, <code class="docutils literal notranslate"><span class="pre">2</span></code>, <code class="docutils literal notranslate"><span class="pre">3</span></code> and <code class="docutils literal notranslate"><span class="pre">4</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">3</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlert.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlert.window_size">
<code class="descname">window_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlert.window_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The period of time that is used to monitor alert activity, represented in ISO 8601 duration format. This value must be greater than <code class="docutils literal notranslate"><span class="pre">frequency</span></code>. Possible values are <code class="docutils literal notranslate"><span class="pre">PT1M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT5M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT15M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT30M</span></code>, <code class="docutils literal notranslate"><span class="pre">PT1H</span></code>, <code class="docutils literal notranslate"><span class="pre">PT6H</span></code>, <code class="docutils literal notranslate"><span class="pre">PT12H</span></code> and <code class="docutils literal notranslate"><span class="pre">P1D</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">PT5M</span></code>.</p>
</dd></dl>

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

<dl class="class">
<dt id="pulumi_azure.monitoring.MetricAlertRule">
<em class="property">class </em><code class="descclassname">pulumi_azure.monitoring.</code><code class="descname">MetricAlertRule</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>aggregation=None</em>, <em>description=None</em>, <em>email_action=None</em>, <em>enabled=None</em>, <em>location=None</em>, <em>metric_name=None</em>, <em>name=None</em>, <em>operator=None</em>, <em>period=None</em>, <em>resource_group_name=None</em>, <em>resource_id=None</em>, <em>tags=None</em>, <em>threshold=None</em>, <em>webhook_action=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlertRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a <a class="reference external" href="https://docs.microsoft.com/en-us/azure/monitoring-and-diagnostics/monitor-quick-resource-metric-alert-portal">metric-based alert rule</a> in Azure Monitor.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>aggregation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Defines how the metric data is combined over time. Possible values are <code class="docutils literal notranslate"><span class="pre">Average</span></code>, <code class="docutils literal notranslate"><span class="pre">Minimum</span></code>, <code class="docutils literal notranslate"><span class="pre">Maximum</span></code>, <code class="docutils literal notranslate"><span class="pre">Total</span></code>, and <code class="docutils literal notranslate"><span class="pre">Last</span></code>.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A verbose description of the alert rule that will be included in the alert email.</li>
<li><strong>email_action</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">email_action</span></code> block as defined below.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, the alert rule is enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>metric_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The metric that defines what the rule monitors.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the alert rule. Changing this forces a new resource to be created.</li>
<li><strong>operator</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The operator used to compare the metric data and the threshold. Possible values are <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code>, and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</li>
<li><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The period of time formatted in <a class="reference external" href="https://en.wikipedia.org/wiki/ISO_8601#Durations">ISO 8601 duration format</a> that is used to monitor the alert activity based on the threshold. The period must be between 5 minutes and 1 day.</p>
</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the alert rule. Changing this forces a new resource to be created.</li>
<li><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the resource monitored by the alert rule.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource. Changing this forces a new resource to be created.</li>
<li><strong>threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The threshold value that activates the alert.</li>
<li><strong>webhook_action</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">webhook_action</span></code> block as defined below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_metric_alertrule.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/monitor_metric_alertrule.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlertRule.aggregation">
<code class="descname">aggregation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlertRule.aggregation" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines how the metric data is combined over time. Possible values are <code class="docutils literal notranslate"><span class="pre">Average</span></code>, <code class="docutils literal notranslate"><span class="pre">Minimum</span></code>, <code class="docutils literal notranslate"><span class="pre">Maximum</span></code>, <code class="docutils literal notranslate"><span class="pre">Total</span></code>, and <code class="docutils literal notranslate"><span class="pre">Last</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlertRule.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlertRule.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A verbose description of the alert rule that will be included in the alert email.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlertRule.email_action">
<code class="descname">email_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlertRule.email_action" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">email_action</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlertRule.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlertRule.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">true</span></code>, the alert rule is enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlertRule.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlertRule.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlertRule.metric_name">
<code class="descname">metric_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlertRule.metric_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The metric that defines what the rule monitors.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlertRule.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlertRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the alert rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlertRule.operator">
<code class="descname">operator</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlertRule.operator" title="Permalink to this definition">¶</a></dt>
<dd><p>The operator used to compare the metric data and the threshold. Possible values are <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThanOrEqual</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code>, and <code class="docutils literal notranslate"><span class="pre">LessThanOrEqual</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlertRule.period">
<code class="descname">period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlertRule.period" title="Permalink to this definition">¶</a></dt>
<dd><p>The period of time formatted in <a class="reference external" href="https://en.wikipedia.org/wiki/ISO_8601#Durations">ISO 8601 duration format</a> that is used to monitor the alert activity based on the threshold. The period must be between 5 minutes and 1 day.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlertRule.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlertRule.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the alert rule. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlertRule.resource_id">
<code class="descname">resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlertRule.resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the resource monitored by the alert rule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlertRule.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlertRule.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlertRule.threshold">
<code class="descname">threshold</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlertRule.threshold" title="Permalink to this definition">¶</a></dt>
<dd><p>The threshold value that activates the alert.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.monitoring.MetricAlertRule.webhook_action">
<code class="descname">webhook_action</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlertRule.webhook_action" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">webhook_action</span></code> block as defined below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.monitoring.MetricAlertRule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlertRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.MetricAlertRule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.MetricAlertRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.monitoring.get_action_group">
<code class="descclassname">pulumi_azure.monitoring.</code><code class="descname">get_action_group</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.get_action_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access the properties of an Action Group.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/monitor_action_group.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/monitor_action_group.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.monitoring.get_diagnostic_categories">
<code class="descclassname">pulumi_azure.monitoring.</code><code class="descname">get_diagnostic_categories</code><span class="sig-paren">(</span><em>resource_id=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.get_diagnostic_categories" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about the Monitor Diagnostics Categories supported by an existing Resource.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/monitor_diagnostic_categories.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/monitor_diagnostic_categories.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.monitoring.get_log_profile">
<code class="descclassname">pulumi_azure.monitoring.</code><code class="descname">get_log_profile</code><span class="sig-paren">(</span><em>name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.monitoring.get_log_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access the properties of a Log Profile.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/monitor_log_profile.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/monitor_log_profile.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
