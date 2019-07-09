---
---

<div class="section" id="synthetics">
<h1>synthetics<a class="headerlink" href="#synthetics" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-newrelic">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-newrelic/issues">pulumi/pulumi-newrelic repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-newrelic/issues">terraform-providers/terraform-provider-newrelic repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_newrelic.synthetics"></span><dl class="class">
<dt id="pulumi_newrelic.synthetics.AlertCondition">
<em class="property">class </em><code class="descclassname">pulumi_newrelic.synthetics.</code><code class="descname">AlertCondition</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>enabled=None</em>, <em>monitor_id=None</em>, <em>name=None</em>, <em>policy_id=None</em>, <em>runbook_url=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.synthetics.AlertCondition" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a AlertCondition resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set whether to enable the alert condition. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
<li><strong>monitor_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Synthetics monitor to be referenced in the alert condition.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The title of this condition.</li>
<li><strong>policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of the policy where this condition should be used.</li>
<li><strong>runbook_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Runbook URL to display in notifications.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-newrelic/blob/master/website/docs/r/synthetics_alert_condition.html.markdown">https://github.com/terraform-providers/terraform-provider-newrelic/blob/master/website/docs/r/synthetics_alert_condition.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.AlertCondition.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.AlertCondition.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Set whether to enable the alert condition. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.AlertCondition.monitor_id">
<code class="descname">monitor_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.AlertCondition.monitor_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Synthetics monitor to be referenced in the alert condition.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.AlertCondition.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.AlertCondition.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The title of this condition.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.AlertCondition.policy_id">
<code class="descname">policy_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.AlertCondition.policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the policy where this condition should be used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.AlertCondition.runbook_url">
<code class="descname">runbook_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.AlertCondition.runbook_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Runbook URL to display in notifications.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_newrelic.synthetics.AlertCondition.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.synthetics.AlertCondition.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.synthetics.AlertCondition.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.synthetics.AlertCondition.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.synthetics.GetMonitorResult">
<em class="property">class </em><code class="descclassname">pulumi_newrelic.synthetics.</code><code class="descname">GetMonitorResult</code><span class="sig-paren">(</span><em>monitor_id=None</em>, <em>name=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.synthetics.GetMonitorResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getMonitor.</p>
<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.GetMonitorResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.GetMonitorResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_newrelic.synthetics.Monitor">
<em class="property">class </em><code class="descclassname">pulumi_newrelic.synthetics.</code><code class="descname">Monitor</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>bypass_head_request=None</em>, <em>frequency=None</em>, <em>locations=None</em>, <em>name=None</em>, <em>sla_threshold=None</em>, <em>status=None</em>, <em>treat_redirect_as_failure=None</em>, <em>type=None</em>, <em>uri=None</em>, <em>validation_string=None</em>, <em>verify_ssl=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.synthetics.Monitor" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this resource to create, update, and delete a synthetics monitor in New Relic.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>bypass_head_request</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Bypass HEAD request.</li>
<li><strong>frequency</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The interval (in minutes) at which this monitor should run.</li>
<li><strong>locations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The locations in which this monitor should be run.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The title of this monitor.</li>
<li><strong>sla_threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The base threshold for the SLA report.</li>
<li><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The monitor status (i.e. ENABLED, MUTED, DISABLED)</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The monitor type.</li>
<li><strong>uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI for the monitor to hit.</li>
<li><strong>validation_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The string to validate against in the response.</li>
<li><strong>verify_ssl</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Verify SSL.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-newrelic/blob/master/website/docs/r/synthetics_monitor.html.markdown">https://github.com/terraform-providers/terraform-provider-newrelic/blob/master/website/docs/r/synthetics_monitor.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.Monitor.bypass_head_request">
<code class="descname">bypass_head_request</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.Monitor.bypass_head_request" title="Permalink to this definition">¶</a></dt>
<dd><p>Bypass HEAD request.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.Monitor.frequency">
<code class="descname">frequency</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.Monitor.frequency" title="Permalink to this definition">¶</a></dt>
<dd><p>The interval (in minutes) at which this monitor should run.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.Monitor.locations">
<code class="descname">locations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.Monitor.locations" title="Permalink to this definition">¶</a></dt>
<dd><p>The locations in which this monitor should be run.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.Monitor.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.Monitor.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The title of this monitor.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.Monitor.sla_threshold">
<code class="descname">sla_threshold</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.Monitor.sla_threshold" title="Permalink to this definition">¶</a></dt>
<dd><p>The base threshold for the SLA report.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.Monitor.status">
<code class="descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.Monitor.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The monitor status (i.e. ENABLED, MUTED, DISABLED)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.Monitor.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.Monitor.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The monitor type.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.Monitor.uri">
<code class="descname">uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.Monitor.uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI for the monitor to hit.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.Monitor.validation_string">
<code class="descname">validation_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.Monitor.validation_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The string to validate against in the response.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.Monitor.verify_ssl">
<code class="descname">verify_ssl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.Monitor.verify_ssl" title="Permalink to this definition">¶</a></dt>
<dd><p>Verify SSL.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_newrelic.synthetics.Monitor.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.synthetics.Monitor.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.synthetics.Monitor.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.synthetics.Monitor.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.synthetics.MonitorScript">
<em class="property">class </em><code class="descclassname">pulumi_newrelic.synthetics.</code><code class="descname">MonitorScript</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>monitor_id=None</em>, <em>text=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.synthetics.MonitorScript" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this resource to update a synthetics monitor script in New Relic.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>monitor_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the monitor to attach the script to.</li>
<li><strong>text</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – plaintext of the monitor script.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-newrelic/blob/master/website/docs/r/synthetics_monitor_script.html.markdown">https://github.com/terraform-providers/terraform-provider-newrelic/blob/master/website/docs/r/synthetics_monitor_script.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.MonitorScript.monitor_id">
<code class="descname">monitor_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.MonitorScript.monitor_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the monitor to attach the script to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.MonitorScript.text">
<code class="descname">text</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.MonitorScript.text" title="Permalink to this definition">¶</a></dt>
<dd><p>plaintext of the monitor script.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_newrelic.synthetics.MonitorScript.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.synthetics.MonitorScript.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.synthetics.MonitorScript.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.synthetics.MonitorScript.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.synthetics.get_monitor">
<code class="descclassname">pulumi_newrelic.synthetics.</code><code class="descname">get_monitor</code><span class="sig-paren">(</span><em>name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.synthetics.get_monitor" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a specific synthetics monitor in New Relic. This can then be used to set up a synthetics alert condition.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-newrelic/blob/master/website/docs/d/synthetics_monitor.html.markdown">https://github.com/terraform-providers/terraform-provider-newrelic/blob/master/website/docs/d/synthetics_monitor.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
