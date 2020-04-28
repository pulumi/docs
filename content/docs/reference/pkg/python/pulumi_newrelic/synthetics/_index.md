---
title: Module synthetics
title_tag: Module synthetics | Package pulumi_newrelic | Python SDK
linktitle: synthetics
notitle: true
---

<div class="section" id="synthetics">
<h1>synthetics<a class="headerlink" href="#synthetics" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-newrelic">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-newrelic/issues">pulumi/pulumi-newrelic repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-newrelic/issues">terraform-providers/terraform-provider-newrelic repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_newrelic.synthetics"></span><dl class="class">
<dt id="pulumi_newrelic.synthetics.AlertCondition">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.synthetics.</code><code class="sig-name descname">AlertCondition</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">monitor_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">policy_id=None</em>, <em class="sig-param">runbook_url=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.synthetics.AlertCondition" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this resource to create and manage synthetics alert conditions in New Relic.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set whether to enable the alert condition. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>monitor_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Synthetics monitor to be referenced in the alert condition.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The title of this condition.</p></li>
<li><p><strong>policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of the policy where this condition should be used.</p></li>
<li><p><strong>runbook_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Runbook URL to display in notifications.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.AlertCondition.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.AlertCondition.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Set whether to enable the alert condition. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.AlertCondition.monitor_id">
<code class="sig-name descname">monitor_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.AlertCondition.monitor_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Synthetics monitor to be referenced in the alert condition.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.AlertCondition.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.AlertCondition.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The title of this condition.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.AlertCondition.policy_id">
<code class="sig-name descname">policy_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.AlertCondition.policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the policy where this condition should be used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.AlertCondition.runbook_url">
<code class="sig-name descname">runbook_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.AlertCondition.runbook_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Runbook URL to display in notifications.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_newrelic.synthetics.AlertCondition.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">monitor_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">policy_id=None</em>, <em class="sig-param">runbook_url=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.synthetics.AlertCondition.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AlertCondition resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set whether to enable the alert condition. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>monitor_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Synthetics monitor to be referenced in the alert condition.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The title of this condition.</p></li>
<li><p><strong>policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of the policy where this condition should be used.</p></li>
<li><p><strong>runbook_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Runbook URL to display in notifications.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_newrelic.synthetics.AlertCondition.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.synthetics.AlertCondition.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.synthetics.AlertCondition.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.synthetics.AlertCondition.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.synthetics.AwaitableGetMonitorResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.synthetics.</code><code class="sig-name descname">AwaitableGetMonitorResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">monitor_id=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.synthetics.AwaitableGetMonitorResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_newrelic.synthetics.AwaitableGetSecureCredentialResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.synthetics.</code><code class="sig-name descname">AwaitableGetSecureCredentialResult</code><span class="sig-paren">(</span><em class="sig-param">created_at=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">key=None</em>, <em class="sig-param">last_updated=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.synthetics.AwaitableGetSecureCredentialResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_newrelic.synthetics.GetMonitorResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.synthetics.</code><code class="sig-name descname">GetMonitorResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">monitor_id=None</em>, <em class="sig-param">name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.synthetics.GetMonitorResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getMonitor.</p>
<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.GetMonitorResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.GetMonitorResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.GetMonitorResult.monitor_id">
<code class="sig-name descname">monitor_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.GetMonitorResult.monitor_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the synthetics monitor.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_newrelic.synthetics.GetSecureCredentialResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.synthetics.</code><code class="sig-name descname">GetSecureCredentialResult</code><span class="sig-paren">(</span><em class="sig-param">created_at=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">key=None</em>, <em class="sig-param">last_updated=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.synthetics.GetSecureCredentialResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSecureCredential.</p>
<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.GetSecureCredentialResult.created_at">
<code class="sig-name descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.GetSecureCredentialResult.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The time the secure credential was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.GetSecureCredentialResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.GetSecureCredentialResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The secure credential’s description.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.GetSecureCredentialResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.GetSecureCredentialResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.GetSecureCredentialResult.last_updated">
<code class="sig-name descname">last_updated</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.GetSecureCredentialResult.last_updated" title="Permalink to this definition">¶</a></dt>
<dd><p>The time the secure credential was last updated.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_newrelic.synthetics.Label">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.synthetics.</code><code class="sig-name descname">Label</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">monitor_id=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">value=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.synthetics.Label" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this resource to create, update, and delete a Synthetics label in New Relic.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>monitor_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the monitor that will be assigned the label.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string representing the label key/category.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string representing the label value.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.Label.href">
<code class="sig-name descname">href</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.Label.href" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the Synthetics label.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.Label.monitor_id">
<code class="sig-name descname">monitor_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.Label.monitor_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the monitor that will be assigned the label.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.Label.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.Label.type" title="Permalink to this definition">¶</a></dt>
<dd><p>A string representing the label key/category.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.Label.value">
<code class="sig-name descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.Label.value" title="Permalink to this definition">¶</a></dt>
<dd><p>A string representing the label value.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_newrelic.synthetics.Label.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">href=None</em>, <em class="sig-param">monitor_id=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.synthetics.Label.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Label resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>href</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the Synthetics label.</p></li>
<li><p><strong>monitor_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the monitor that will be assigned the label.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string representing the label key/category.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string representing the label value.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_newrelic.synthetics.Label.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.synthetics.Label.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.synthetics.Label.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.synthetics.Label.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.synthetics.Monitor">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.synthetics.</code><code class="sig-name descname">Monitor</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">bypass_head_request=None</em>, <em class="sig-param">frequency=None</em>, <em class="sig-param">locations=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">sla_threshold=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">treat_redirect_as_failure=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">uri=None</em>, <em class="sig-param">validation_string=None</em>, <em class="sig-param">verify_ssl=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.synthetics.Monitor" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this resource to create, update, and delete a synthetics monitor in New Relic.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bypass_head_request</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Bypass HEAD request.</p></li>
<li><p><strong>frequency</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The interval (in minutes) at which this monitor should run.</p></li>
<li><p><strong>locations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The locations in which this monitor should be run.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The title of this monitor.</p></li>
<li><p><strong>sla_threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The base threshold for the SLA report.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The monitor status (i.e. <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>, <code class="docutils literal notranslate"><span class="pre">MUTED</span></code>, <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>).</p></li>
<li><p><strong>treat_redirect_as_failure</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Fail the monitor check if redirected.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The monitor type. Valid values are <code class="docutils literal notranslate"><span class="pre">SIMPLE</span></code>, <code class="docutils literal notranslate"><span class="pre">BROWSER</span></code>, <code class="docutils literal notranslate"><span class="pre">SCRIPT_BROWSER</span></code>, and <code class="docutils literal notranslate"><span class="pre">SCRIPT_API</span></code>.</p></li>
<li><p><strong>uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI for the monitor to hit.</p></li>
<li><p><strong>validation_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The string to validate against in the response.</p></li>
<li><p><strong>verify_ssl</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Verify SSL.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.Monitor.bypass_head_request">
<code class="sig-name descname">bypass_head_request</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.Monitor.bypass_head_request" title="Permalink to this definition">¶</a></dt>
<dd><p>Bypass HEAD request.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.Monitor.frequency">
<code class="sig-name descname">frequency</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.Monitor.frequency" title="Permalink to this definition">¶</a></dt>
<dd><p>The interval (in minutes) at which this monitor should run.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.Monitor.locations">
<code class="sig-name descname">locations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.Monitor.locations" title="Permalink to this definition">¶</a></dt>
<dd><p>The locations in which this monitor should be run.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.Monitor.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.Monitor.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The title of this monitor.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.Monitor.sla_threshold">
<code class="sig-name descname">sla_threshold</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.Monitor.sla_threshold" title="Permalink to this definition">¶</a></dt>
<dd><p>The base threshold for the SLA report.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.Monitor.status">
<code class="sig-name descname">status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.Monitor.status" title="Permalink to this definition">¶</a></dt>
<dd><p>The monitor status (i.e. <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>, <code class="docutils literal notranslate"><span class="pre">MUTED</span></code>, <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.Monitor.treat_redirect_as_failure">
<code class="sig-name descname">treat_redirect_as_failure</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.Monitor.treat_redirect_as_failure" title="Permalink to this definition">¶</a></dt>
<dd><p>Fail the monitor check if redirected.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.Monitor.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.Monitor.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The monitor type. Valid values are <code class="docutils literal notranslate"><span class="pre">SIMPLE</span></code>, <code class="docutils literal notranslate"><span class="pre">BROWSER</span></code>, <code class="docutils literal notranslate"><span class="pre">SCRIPT_BROWSER</span></code>, and <code class="docutils literal notranslate"><span class="pre">SCRIPT_API</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.Monitor.uri">
<code class="sig-name descname">uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.Monitor.uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI for the monitor to hit.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.Monitor.validation_string">
<code class="sig-name descname">validation_string</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.Monitor.validation_string" title="Permalink to this definition">¶</a></dt>
<dd><p>The string to validate against in the response.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.Monitor.verify_ssl">
<code class="sig-name descname">verify_ssl</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.Monitor.verify_ssl" title="Permalink to this definition">¶</a></dt>
<dd><p>Verify SSL.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_newrelic.synthetics.Monitor.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">bypass_head_request=None</em>, <em class="sig-param">frequency=None</em>, <em class="sig-param">locations=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">sla_threshold=None</em>, <em class="sig-param">status=None</em>, <em class="sig-param">treat_redirect_as_failure=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">uri=None</em>, <em class="sig-param">validation_string=None</em>, <em class="sig-param">verify_ssl=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.synthetics.Monitor.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Monitor resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>bypass_head_request</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Bypass HEAD request.</p></li>
<li><p><strong>frequency</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The interval (in minutes) at which this monitor should run.</p></li>
<li><p><strong>locations</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The locations in which this monitor should be run.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The title of this monitor.</p></li>
<li><p><strong>sla_threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The base threshold for the SLA report.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The monitor status (i.e. <code class="docutils literal notranslate"><span class="pre">ENABLED</span></code>, <code class="docutils literal notranslate"><span class="pre">MUTED</span></code>, <code class="docutils literal notranslate"><span class="pre">DISABLED</span></code>).</p></li>
<li><p><strong>treat_redirect_as_failure</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Fail the monitor check if redirected.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The monitor type. Valid values are <code class="docutils literal notranslate"><span class="pre">SIMPLE</span></code>, <code class="docutils literal notranslate"><span class="pre">BROWSER</span></code>, <code class="docutils literal notranslate"><span class="pre">SCRIPT_BROWSER</span></code>, and <code class="docutils literal notranslate"><span class="pre">SCRIPT_API</span></code>.</p></li>
<li><p><strong>uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI for the monitor to hit.</p></li>
<li><p><strong>validation_string</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The string to validate against in the response.</p></li>
<li><p><strong>verify_ssl</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Verify SSL.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_newrelic.synthetics.Monitor.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.synthetics.Monitor.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.synthetics.Monitor.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.synthetics.Monitor.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.synthetics.MonitorScript">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.synthetics.</code><code class="sig-name descname">MonitorScript</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">monitor_id=None</em>, <em class="sig-param">text=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.synthetics.MonitorScript" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this resource to update a synthetics monitor script in New Relic.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>monitor_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the monitor to attach the script to.</p></li>
<li><p><strong>text</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The plaintext representing the monitor script.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.MonitorScript.monitor_id">
<code class="sig-name descname">monitor_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.MonitorScript.monitor_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the monitor to attach the script to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.MonitorScript.text">
<code class="sig-name descname">text</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.MonitorScript.text" title="Permalink to this definition">¶</a></dt>
<dd><p>The plaintext representing the monitor script.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_newrelic.synthetics.MonitorScript.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">monitor_id=None</em>, <em class="sig-param">text=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.synthetics.MonitorScript.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MonitorScript resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>monitor_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the monitor to attach the script to.</p></li>
<li><p><strong>text</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The plaintext representing the monitor script.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_newrelic.synthetics.MonitorScript.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.synthetics.MonitorScript.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.synthetics.MonitorScript.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.synthetics.MonitorScript.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.synthetics.SecureCredential">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.synthetics.</code><code class="sig-name descname">SecureCredential</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">created_at=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">key=None</em>, <em class="sig-param">last_updated=None</em>, <em class="sig-param">value=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.synthetics.SecureCredential" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this resource to create and manage New Relic Synthetic secure credentials.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>created_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time the secure credential was created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The secure credential’s description.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The secure credential’s key name.  Regardless of the case used in the configuration, the provider will provide an upcased key to the underlying API.</p></li>
<li><p><strong>last_updated</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time the secure credential was last updated.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The secure credential’s value.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.SecureCredential.created_at">
<code class="sig-name descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.SecureCredential.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>The time the secure credential was created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.SecureCredential.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.SecureCredential.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The secure credential’s description.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.SecureCredential.key">
<code class="sig-name descname">key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.SecureCredential.key" title="Permalink to this definition">¶</a></dt>
<dd><p>The secure credential’s key name.  Regardless of the case used in the configuration, the provider will provide an upcased key to the underlying API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.SecureCredential.last_updated">
<code class="sig-name descname">last_updated</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.SecureCredential.last_updated" title="Permalink to this definition">¶</a></dt>
<dd><p>The time the secure credential was last updated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_newrelic.synthetics.SecureCredential.value">
<code class="sig-name descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.synthetics.SecureCredential.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The secure credential’s value.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_newrelic.synthetics.SecureCredential.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">created_at=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">key=None</em>, <em class="sig-param">last_updated=None</em>, <em class="sig-param">value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.synthetics.SecureCredential.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecureCredential resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>created_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time the secure credential was created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The secure credential’s description.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The secure credential’s key name.  Regardless of the case used in the configuration, the provider will provide an upcased key to the underlying API.</p></li>
<li><p><strong>last_updated</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time the secure credential was last updated.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The secure credential’s value.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_newrelic.synthetics.SecureCredential.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.synthetics.SecureCredential.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.synthetics.SecureCredential.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.synthetics.SecureCredential.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.synthetics.get_monitor">
<code class="sig-prename descclassname">pulumi_newrelic.synthetics.</code><code class="sig-name descname">get_monitor</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.synthetics.get_monitor" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a specific synthetics monitor in New Relic that already exists. This can be used to set up a Synthetics alert condition.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – The name of the synthetics monitor in New Relic.</p>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_newrelic.synthetics.get_secure_credential">
<code class="sig-prename descclassname">pulumi_newrelic.synthetics.</code><code class="sig-name descname">get_secure_credential</code><span class="sig-paren">(</span><em class="sig-param">key=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.synthetics.get_secure_credential" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get information about a specific Synthetics secure credential in New Relic that already exists.</p>
<p>Note that the secure credential’s value is not returned as an attribute for security reasons.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>key</strong> (<em>str</em>) – The secure credential’s key name.  Regardless of the case used in the configuration, the provider will provide an upcased key to the underlying API.</p>
</dd>
</dl>
</dd></dl>

</div>
