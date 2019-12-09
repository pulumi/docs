---
title: Module plugins
title_tag: Module plugins | Package pulumi_newrelic | Python SDK
linktitle: plugins
notitle: true
---

<div class="section" id="plugins">
<h1>plugins<a class="headerlink" href="#plugins" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-newrelic">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-newrelic/issues">pulumi/pulumi-newrelic repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-newrelic/issues">terraform-providers/terraform-provider-newrelic repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_newrelic.plugins"></span><dl class="class">
<dt id="pulumi_newrelic.plugins.AlertCondition">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.plugins.</code><code class="sig-name descname">AlertCondition</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">entities=None</em>, <em class="sig-param">metric=None</em>, <em class="sig-param">metric_description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">plugin_guid=None</em>, <em class="sig-param">plugin_id=None</em>, <em class="sig-param">policy_id=None</em>, <em class="sig-param">runbook_url=None</em>, <em class="sig-param">terms=None</em>, <em class="sig-param">value_function=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.plugins.AlertCondition" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">term</span></code> mapping supports the following arguments:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> - (Required) In minutes, must be in the range of <code class="docutils literal notranslate"><span class="pre">5</span></code> to <code class="docutils literal notranslate"><span class="pre">120</span></code>, inclusive.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> - (Optional) <code class="docutils literal notranslate"><span class="pre">above</span></code>, <code class="docutils literal notranslate"><span class="pre">below</span></code>, or <code class="docutils literal notranslate"><span class="pre">equal</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">equal</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> - (Optional) <code class="docutils literal notranslate"><span class="pre">critical</span></code> or <code class="docutils literal notranslate"><span class="pre">warning</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">critical</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> - (Required) Must be 0 or greater.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">time_function</span></code> - (Required) <code class="docutils literal notranslate"><span class="pre">all</span></code> or <code class="docutils literal notranslate"><span class="pre">any</span></code>.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>metric</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The metric field accepts parameters based on the <code class="docutils literal notranslate"><span class="pre">type</span></code> set.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The title of the condition. Must be between 1 and 64 characters, inclusive.</p></li>
<li><p><strong>plugin_guid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GUID of the plugin which produces the metric.</p></li>
<li><p><strong>plugin_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the installed plugin instance which produces the metric.</p></li>
<li><p><strong>policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of the policy where this condition should be used.</p></li>
<li><p><strong>runbook_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Runbook URL to display in notifications.</p></li>
<li><p><strong>terms</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of terms for this condition. See Terms below for details.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>terms</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeFunction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-newrelic/blob/master/website/docs/r/plugins_alert_condition.html.markdown">https://github.com/terraform-providers/terraform-provider-newrelic/blob/master/website/docs/r/plugins_alert_condition.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_newrelic.plugins.AlertCondition.metric">
<code class="sig-name descname">metric</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.plugins.AlertCondition.metric" title="Permalink to this definition">¶</a></dt>
<dd><p>The metric field accepts parameters based on the <code class="docutils literal notranslate"><span class="pre">type</span></code> set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.plugins.AlertCondition.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.plugins.AlertCondition.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The title of the condition. Must be between 1 and 64 characters, inclusive.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.plugins.AlertCondition.plugin_guid">
<code class="sig-name descname">plugin_guid</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.plugins.AlertCondition.plugin_guid" title="Permalink to this definition">¶</a></dt>
<dd><p>The GUID of the plugin which produces the metric.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.plugins.AlertCondition.plugin_id">
<code class="sig-name descname">plugin_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.plugins.AlertCondition.plugin_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the installed plugin instance which produces the metric.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.plugins.AlertCondition.policy_id">
<code class="sig-name descname">policy_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.plugins.AlertCondition.policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the policy where this condition should be used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.plugins.AlertCondition.runbook_url">
<code class="sig-name descname">runbook_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.plugins.AlertCondition.runbook_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Runbook URL to display in notifications.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.plugins.AlertCondition.terms">
<code class="sig-name descname">terms</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.plugins.AlertCondition.terms" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of terms for this condition. See Terms below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeFunction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_newrelic.plugins.AlertCondition.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">entities=None</em>, <em class="sig-param">metric=None</em>, <em class="sig-param">metric_description=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">plugin_guid=None</em>, <em class="sig-param">plugin_id=None</em>, <em class="sig-param">policy_id=None</em>, <em class="sig-param">runbook_url=None</em>, <em class="sig-param">terms=None</em>, <em class="sig-param">value_function=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.plugins.AlertCondition.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AlertCondition resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>metric</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The metric field accepts parameters based on the <code class="docutils literal notranslate"><span class="pre">type</span></code> set.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The title of the condition. Must be between 1 and 64 characters, inclusive.</p></li>
<li><p><strong>plugin_guid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GUID of the plugin which produces the metric.</p></li>
<li><p><strong>plugin_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the installed plugin instance which produces the metric.</p></li>
<li><p><strong>policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of the policy where this condition should be used.</p></li>
<li><p><strong>runbook_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Runbook URL to display in notifications.</p></li>
<li><p><strong>terms</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of terms for this condition. See Terms below for details.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>terms</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeFunction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-newrelic/blob/master/website/docs/r/plugins_alert_condition.html.markdown">https://github.com/terraform-providers/terraform-provider-newrelic/blob/master/website/docs/r/plugins_alert_condition.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_newrelic.plugins.AlertCondition.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.plugins.AlertCondition.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.plugins.AlertCondition.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.plugins.AlertCondition.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.plugins.AwaitableGetPluginComponentResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.plugins.</code><code class="sig-name descname">AwaitableGetPluginComponentResult</code><span class="sig-paren">(</span><em class="sig-param">health_status=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">plugin_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.plugins.AwaitableGetPluginComponentResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_newrelic.plugins.AwaitableGetPluginResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.plugins.</code><code class="sig-name descname">AwaitableGetPluginResult</code><span class="sig-paren">(</span><em class="sig-param">guid=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.plugins.AwaitableGetPluginResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_newrelic.plugins.GetPluginComponentResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.plugins.</code><code class="sig-name descname">GetPluginComponentResult</code><span class="sig-paren">(</span><em class="sig-param">health_status=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">plugin_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.plugins.GetPluginComponentResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPluginComponent.</p>
<dl class="attribute">
<dt id="pulumi_newrelic.plugins.GetPluginComponentResult.health_status">
<code class="sig-name descname">health_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.plugins.GetPluginComponentResult.health_status" title="Permalink to this definition">¶</a></dt>
<dd><p>The health status of the plugin component.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.plugins.GetPluginComponentResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.plugins.GetPluginComponentResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the plugin component.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_newrelic.plugins.GetPluginResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.plugins.</code><code class="sig-name descname">GetPluginResult</code><span class="sig-paren">(</span><em class="sig-param">guid=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.plugins.GetPluginResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPlugin.</p>
<dl class="attribute">
<dt id="pulumi_newrelic.plugins.GetPluginResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.plugins.GetPluginResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the installed plugin instance.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_newrelic.plugins.get_plugin">
<code class="sig-prename descclassname">pulumi_newrelic.plugins.</code><code class="sig-name descname">get_plugin</code><span class="sig-paren">(</span><em class="sig-param">guid=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.plugins.get_plugin" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a specific installed plugin in New Relic.</p>
<p>Each plugin published to New Relic’s Plugin Central is assigned a <a class="reference external" href="https://docs.newrelic.com/docs/plugins/plugin-developer-resources/planning-your-plugin/parts-plugin#guid">GUID</a>. Once you have installed a plugin into your account it is assigned an ID. This account-specific ID is required when creating Plugins Alert Conditions.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>guid</strong> (<em>str</em>) – The GUID of the plugin in New Relic.</p>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-newrelic/blob/master/website/docs/d/plugin.html.markdown">https://github.com/terraform-providers/terraform-provider-newrelic/blob/master/website/docs/d/plugin.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_newrelic.plugins.get_plugin_component">
<code class="sig-prename descclassname">pulumi_newrelic.plugins.</code><code class="sig-name descname">get_plugin_component</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">plugin_id=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.plugins.get_plugin_component" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a single plugin component in New Relic.</p>
<p>Each plugin component reporting into to New Relic is assigned a unique ID. Once you have a plugin component reporting data into your account, its component ID can be used to create Plugins Alert Conditions.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the plugin component.</p></li>
<li><p><strong>plugin_id</strong> (<em>float</em>) – The ID of the plugin instance this component belongs to.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-newrelic/blob/master/website/docs/d/plugin_component.html.markdown">https://github.com/terraform-providers/terraform-provider-newrelic/blob/master/website/docs/d/plugin_component.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
