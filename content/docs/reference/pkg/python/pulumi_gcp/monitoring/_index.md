---
title: Module monitoring
title_tag: Module monitoring | Package pulumi_gcp | Python SDK
linktitle: monitoring
notitle: true
---

<div class="section" id="monitoring">
<h1>monitoring<a class="headerlink" href="#monitoring" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.monitoring"></span><dl class="class">
<dt id="pulumi_gcp.monitoring.AlertPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">AlertPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">combiner=None</em>, <em class="sig-param">conditions=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">documentation=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">notification_channels=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">user_labels=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a AlertPolicy resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] combiner: How to combine the results of multiple conditions to determine if an incident should be opened.
:param pulumi.Input[list] conditions: A list of conditions for the policy. The conditions are combined by AND or OR according to the combiner field. If the</p>
<blockquote>
<div><p>combined conditions evaluate to true, then an incident is created. A policy can have from one to six conditions.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion,
don’t use the same display name for multiple policies in the same project. The name is limited to 512 Unicode
characters.</p></li>
<li><p><strong>documentation</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion,
don’t use the same display name for multiple policies in the same project. The name is limited to 512 Unicode
characters.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not the policy is enabled. The default is true.</p></li>
<li><p><strong>notification_channels</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Identifies the notification channels to which notifications should be sent when incidents are opened or closed or when
new violations occur on an already opened incident. Each element of this array corresponds to the name field in each of
the NotificationChannel objects that are returned from the notificationChannels.list method. The syntax of the entries
in this field is ‘projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID]’</p></li>
<li><p><strong>user_labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – This field is intended to be used for organizing and identifying the AlertPolicy objects.The field can contain up to 64
entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values
can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>conditions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">conditionAbsent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">aggregations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">alignmentPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crossSeriesReducer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupByFields</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">perSeriesAligner</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trigger</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">percent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">conditionThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">aggregations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">alignmentPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crossSeriesReducer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupByFields</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">perSeriesAligner</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">comparison</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">denominatorAggregations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">alignmentPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crossSeriesReducer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupByFields</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">perSeriesAligner</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">denominatorFilter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thresholdValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trigger</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">percent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">display_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>documentation</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mimeType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.monitoring.AlertPolicy.combiner">
<code class="sig-name descname">combiner</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.combiner" title="Permalink to this definition">¶</a></dt>
<dd><p>How to combine the results of multiple conditions to determine if an incident should be opened.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.AlertPolicy.conditions">
<code class="sig-name descname">conditions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.conditions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of conditions for the policy. The conditions are combined by AND or OR according to the combiner field. If the
combined conditions evaluate to true, then an incident is created. A policy can have from one to six conditions.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">conditionAbsent</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">aggregations</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">alignmentPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crossSeriesReducer</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupByFields</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">perSeriesAligner</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filter</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trigger</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">percent</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">conditionThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">aggregations</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">alignmentPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crossSeriesReducer</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupByFields</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">perSeriesAligner</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">comparison</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">denominatorAggregations</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">alignmentPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crossSeriesReducer</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupByFields</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">perSeriesAligner</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">denominatorFilter</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filter</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thresholdValue</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trigger</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">percent</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">display_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.AlertPolicy.creation_record">
<code class="sig-name descname">creation_record</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.creation_record" title="Permalink to this definition">¶</a></dt>
<dd><p>A read-only record of the creation of the alerting policy. If provided in a call to create or update, this field will be
ignored.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mutateTime</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mutatedBy</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.AlertPolicy.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion,
don’t use the same display name for multiple policies in the same project. The name is limited to 512 Unicode
characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.AlertPolicy.documentation">
<code class="sig-name descname">documentation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.documentation" title="Permalink to this definition">¶</a></dt>
<dd><p>A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion,
don’t use the same display name for multiple policies in the same project. The name is limited to 512 Unicode
characters.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mimeType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.AlertPolicy.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not the policy is enabled. The default is true.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.AlertPolicy.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique resource name for this policy. Its syntax is: projects/[PROJECT_ID]/alertPolicies/[ALERT_POLICY_ID]</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.AlertPolicy.notification_channels">
<code class="sig-name descname">notification_channels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.notification_channels" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifies the notification channels to which notifications should be sent when incidents are opened or closed or when
new violations occur on an already opened incident. Each element of this array corresponds to the name field in each of
the NotificationChannel objects that are returned from the notificationChannels.list method. The syntax of the entries
in this field is ‘projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID]’</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.AlertPolicy.user_labels">
<code class="sig-name descname">user_labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.user_labels" title="Permalink to this definition">¶</a></dt>
<dd><p>This field is intended to be used for organizing and identifying the AlertPolicy objects.The field can contain up to 64
entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values
can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.monitoring.AlertPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">combiner=None</em>, <em class="sig-param">conditions=None</em>, <em class="sig-param">creation_record=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">documentation=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">notification_channels=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">user_labels=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AlertPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>combiner</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – How to combine the results of multiple conditions to determine if an incident should be opened.</p></li>
<li><p><strong>conditions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of conditions for the policy. The conditions are combined by AND or OR according to the combiner field. If the
combined conditions evaluate to true, then an incident is created. A policy can have from one to six conditions.</p></li>
<li><p><strong>creation_record</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A read-only record of the creation of the alerting policy. If provided in a call to create or update, this field will be
ignored.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion,
don’t use the same display name for multiple policies in the same project. The name is limited to 512 Unicode
characters.</p></li>
<li><p><strong>documentation</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion,
don’t use the same display name for multiple policies in the same project. The name is limited to 512 Unicode
characters.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not the policy is enabled. The default is true.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique resource name for this policy. Its syntax is: projects/[PROJECT_ID]/alertPolicies/[ALERT_POLICY_ID]</p></li>
<li><p><strong>notification_channels</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Identifies the notification channels to which notifications should be sent when incidents are opened or closed or when
new violations occur on an already opened incident. Each element of this array corresponds to the name field in each of
the NotificationChannel objects that are returned from the notificationChannels.list method. The syntax of the entries
in this field is ‘projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID]’</p></li>
<li><p><strong>user_labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – This field is intended to be used for organizing and identifying the AlertPolicy objects.The field can contain up to 64
entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values
can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>conditions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">conditionAbsent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">aggregations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">alignmentPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crossSeriesReducer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupByFields</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">perSeriesAligner</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trigger</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">percent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">conditionThreshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">aggregations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">alignmentPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crossSeriesReducer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupByFields</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">perSeriesAligner</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">comparison</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">denominatorAggregations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">alignmentPeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">crossSeriesReducer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupByFields</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">perSeriesAligner</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">denominatorFilter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">thresholdValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">trigger</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">count</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">percent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">display_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>creation_record</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mutateTime</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mutatedBy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>documentation</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mimeType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.monitoring.AlertPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.monitoring.AlertPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.AlertPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.monitoring.AwaitableGetNotificationChannelResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">AwaitableGetNotificationChannelResult</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">user_labels=None</em>, <em class="sig-param">verification_status=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.AwaitableGetNotificationChannelResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.monitoring.AwaitableGetSecretVersionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">AwaitableGetSecretVersionResult</code><span class="sig-paren">(</span><em class="sig-param">create_time=None</em>, <em class="sig-param">destroy_time=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">secret=None</em>, <em class="sig-param">secret_data=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.AwaitableGetSecretVersionResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.monitoring.GetNotificationChannelResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">GetNotificationChannelResult</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">user_labels=None</em>, <em class="sig-param">verification_status=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.GetNotificationChannelResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNotificationChannel.</p>
<dl class="attribute">
<dt id="pulumi_gcp.monitoring.GetNotificationChannelResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.GetNotificationChannelResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.monitoring.GetSecretVersionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">GetSecretVersionResult</code><span class="sig-paren">(</span><em class="sig-param">create_time=None</em>, <em class="sig-param">destroy_time=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">secret=None</em>, <em class="sig-param">secret_data=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.GetSecretVersionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSecretVersion.</p>
<dl class="attribute">
<dt id="pulumi_gcp.monitoring.GetSecretVersionResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.GetSecretVersionResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.monitoring.Group">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">Group</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">filter=None</em>, <em class="sig-param">is_cluster=None</em>, <em class="sig-param">parent_name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.Group" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Group resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] display_name: A user-assigned name for this group, used only for display purposes.
:param pulumi.Input[str] filter: The filter used to determine which monitored resources belong to this group.
:param pulumi.Input[bool] is_cluster: If true, the members of this group are considered to be a cluster. The system can perform additional analysis on groups</p>
<blockquote>
<div><p>that are clusters.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>parent_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the group’s parent, if it has one. The format is “projects/{project_id_or_number}/groups/{group_id}”. For
groups with no parent, parentName is the empty string, “”.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_gcp.monitoring.Group.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.Group.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A user-assigned name for this group, used only for display purposes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.Group.filter">
<code class="sig-name descname">filter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.Group.filter" title="Permalink to this definition">¶</a></dt>
<dd><p>The filter used to determine which monitored resources belong to this group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.Group.is_cluster">
<code class="sig-name descname">is_cluster</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.Group.is_cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, the members of this group are considered to be a cluster. The system can perform additional analysis on groups
that are clusters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.Group.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.Group.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique identifier for this group. The format is “projects/{project_id_or_number}/groups/{group_id}”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.Group.parent_name">
<code class="sig-name descname">parent_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.Group.parent_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the group’s parent, if it has one. The format is “projects/{project_id_or_number}/groups/{group_id}”. For
groups with no parent, parentName is the empty string, “”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.Group.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.Group.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.monitoring.Group.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">filter=None</em>, <em class="sig-param">is_cluster=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">parent_name=None</em>, <em class="sig-param">project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.Group.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Group resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A user-assigned name for this group, used only for display purposes.</p></li>
<li><p><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The filter used to determine which monitored resources belong to this group.</p></li>
<li><p><strong>is_cluster</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, the members of this group are considered to be a cluster. The system can perform additional analysis on groups
that are clusters.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique identifier for this group. The format is “projects/{project_id_or_number}/groups/{group_id}”.</p></li>
<li><p><strong>parent_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the group’s parent, if it has one. The format is “projects/{project_id_or_number}/groups/{group_id}”. For
groups with no parent, parentName is the empty string, “”.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.monitoring.Group.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.Group.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.monitoring.Group.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.Group.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.monitoring.NotificationChannel">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">NotificationChannel</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">user_labels=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a NotificationChannel resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] description: An optional human-readable description of this notification channel. This description may provide additional details,</p>
<blockquote>
<div><p>beyond the display name, for the channel. This may not exceed 1024 Unicode characters.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional human-readable name for this notification channel. It is recommended that you specify a non-empty and unique
name in order to make it easier to identify the channels in your project, though this is not enforced. The display name
is limited to 512 Unicode characters.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether notifications are forwarded to the described channel. This makes it possible to disable delivery of
notifications to a particular channel without removing the channel from all alerting policies that reference the
channel. This is a more convenient approach when the change is temporary and you want to receive notifications from the
same set of alerting policies on the channel at some point in the future.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration fields that define the channel and its behavior. The permissible and required labels are specified in the
NotificationChannelDescriptor corresponding to the type field. <strong>Note</strong>: Some NotificationChannelDescriptor labels are
sensitive and the API will return an partially-obfuscated value. For example, for ‘“type”: “slack”’ channels, an
‘auth_token’ label with value “SECRET” will be obfuscated as “<a href="#id1"><span class="problematic" id="id2">**</span></a>CRET”. In order to avoid a diff, Terraform will use the
state value if it appears that the obfuscated value matches the state value in length/unobfuscated characters. However,
Terraform will not detect a diff if the obfuscated portion of the value was changed outside of Terraform.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the notification channel. This field matches the value of the NotificationChannelDescriptor.type field. See
<a class="reference external" href="https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/list">https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/list</a> to get the list of
valid values such as “email”, “slack”, etc…</p></li>
<li><p><strong>user_labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – User-supplied key/value data that does not need to conform to the corresponding NotificationChannelDescriptor’s schema,
unlike the labels field. This field is intended to be used for organizing and identifying the NotificationChannel
objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes,
whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must
begin with a letter.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_gcp.monitoring.NotificationChannel.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.description" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional human-readable description of this notification channel. This description may provide additional details,
beyond the display name, for the channel. This may not exceed 1024 Unicode characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.NotificationChannel.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional human-readable name for this notification channel. It is recommended that you specify a non-empty and unique
name in order to make it easier to identify the channels in your project, though this is not enforced. The display name
is limited to 512 Unicode characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.NotificationChannel.enabled">
<code class="sig-name descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether notifications are forwarded to the described channel. This makes it possible to disable delivery of
notifications to a particular channel without removing the channel from all alerting policies that reference the
channel. This is a more convenient approach when the change is temporary and you want to receive notifications from the
same set of alerting policies on the channel at some point in the future.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.NotificationChannel.labels">
<code class="sig-name descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration fields that define the channel and its behavior. The permissible and required labels are specified in the
NotificationChannelDescriptor corresponding to the type field. <strong>Note</strong>: Some NotificationChannelDescriptor labels are
sensitive and the API will return an partially-obfuscated value. For example, for ‘“type”: “slack”’ channels, an
‘auth_token’ label with value “SECRET” will be obfuscated as “<a href="#id3"><span class="problematic" id="id4">**</span></a>CRET”. In order to avoid a diff, Terraform will use the
state value if it appears that the obfuscated value matches the state value in length/unobfuscated characters. However,
Terraform will not detect a diff if the obfuscated portion of the value was changed outside of Terraform.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.NotificationChannel.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The full REST resource name for this channel. The syntax is: projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID] The
[CHANNEL_ID] is automatically assigned by the server on creation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.NotificationChannel.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.NotificationChannel.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the notification channel. This field matches the value of the NotificationChannelDescriptor.type field. See
<a class="reference external" href="https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/list">https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/list</a> to get the list of
valid values such as “email”, “slack”, etc…</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.NotificationChannel.user_labels">
<code class="sig-name descname">user_labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.user_labels" title="Permalink to this definition">¶</a></dt>
<dd><p>User-supplied key/value data that does not need to conform to the corresponding NotificationChannelDescriptor’s schema,
unlike the labels field. This field is intended to be used for organizing and identifying the NotificationChannel
objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes,
whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must
begin with a letter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.NotificationChannel.verification_status">
<code class="sig-name descname">verification_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.verification_status" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether this channel has been verified or not. On a ListNotificationChannels or GetNotificationChannel
operation, this field is expected to be populated.If the value is UNVERIFIED, then it indicates that the channel is
non-functioning (it both requires verification and lacks verification); otherwise, it is assumed that the channel
works.If the channel is neither VERIFIED nor UNVERIFIED, it implies that the channel is of a type that does not require
verification or that this specific channel has been exempted from verification because it was created prior to
verification being required for channels of this type.This field cannot be modified using a standard
UpdateNotificationChannel operation. To change the value of this field, you must call VerifyNotificationChannel.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.monitoring.NotificationChannel.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">enabled=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">user_labels=None</em>, <em class="sig-param">verification_status=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NotificationChannel resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional human-readable description of this notification channel. This description may provide additional details,
beyond the display name, for the channel. This may not exceed 1024 Unicode characters.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional human-readable name for this notification channel. It is recommended that you specify a non-empty and unique
name in order to make it easier to identify the channels in your project, though this is not enforced. The display name
is limited to 512 Unicode characters.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether notifications are forwarded to the described channel. This makes it possible to disable delivery of
notifications to a particular channel without removing the channel from all alerting policies that reference the
channel. This is a more convenient approach when the change is temporary and you want to receive notifications from the
same set of alerting policies on the channel at some point in the future.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration fields that define the channel and its behavior. The permissible and required labels are specified in the
NotificationChannelDescriptor corresponding to the type field. <strong>Note</strong>: Some NotificationChannelDescriptor labels are
sensitive and the API will return an partially-obfuscated value. For example, for ‘“type”: “slack”’ channels, an
‘auth_token’ label with value “SECRET” will be obfuscated as “<a href="#id5"><span class="problematic" id="id6">**</span></a>CRET”. In order to avoid a diff, Terraform will use the
state value if it appears that the obfuscated value matches the state value in length/unobfuscated characters. However,
Terraform will not detect a diff if the obfuscated portion of the value was changed outside of Terraform.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The full REST resource name for this channel. The syntax is: projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID] The
[CHANNEL_ID] is automatically assigned by the server on creation.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the notification channel. This field matches the value of the NotificationChannelDescriptor.type field. See
<a class="reference external" href="https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/list">https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/list</a> to get the list of
valid values such as “email”, “slack”, etc…</p></li>
<li><p><strong>user_labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – User-supplied key/value data that does not need to conform to the corresponding NotificationChannelDescriptor’s schema,
unlike the labels field. This field is intended to be used for organizing and identifying the NotificationChannel
objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes,
whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must
begin with a letter.</p></li>
<li><p><strong>verification_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates whether this channel has been verified or not. On a ListNotificationChannels or GetNotificationChannel
operation, this field is expected to be populated.If the value is UNVERIFIED, then it indicates that the channel is
non-functioning (it both requires verification and lacks verification); otherwise, it is assumed that the channel
works.If the channel is neither VERIFIED nor UNVERIFIED, it implies that the channel is of a type that does not require
verification or that this specific channel has been exempted from verification because it was created prior to
verification being required for channels of this type.This field cannot be modified using a standard
UpdateNotificationChannel operation. To change the value of this field, you must call VerifyNotificationChannel.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.monitoring.NotificationChannel.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.monitoring.NotificationChannel.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.NotificationChannel.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">UptimeCheckConfig</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">content_matchers=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">http_check=None</em>, <em class="sig-param">monitored_resource=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">resource_group=None</em>, <em class="sig-param">selected_regions=None</em>, <em class="sig-param">tcp_check=None</em>, <em class="sig-param">timeout=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a UptimeCheckConfig resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[list] content_matchers: The expected content on the page the check is run against. Currently, only the first entry in the list is supported, and</p>
<blockquote>
<div><p>other entries will be ignored. The server will look for an exact match of the string in the page response’s content.
This field is optional and should only be specified if a content match is required.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-friendly name for the uptime check configuration. The display name should be unique within a Stackdriver
Workspace in order to make it easier to identify; however, uniqueness is not enforced.</p></li>
<li><p><strong>http_check</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Contains information needed to make an HTTP or HTTPS check.</p></li>
<li><p><strong>monitored_resource</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The monitored resource (<a class="reference external" href="https://cloud.google.com/monitoring/api/resources">https://cloud.google.com/monitoring/api/resources</a>) associated with the configuration. The
following monitored resource types are supported for uptime checks: uptime_url gce_instance gae_app aws_ec2_instance
aws_elb_load_balancer</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – How often, in seconds, the uptime check is performed. Currently, the only supported values are 60s (1 minute), 300s (5
minutes), 600s (10 minutes), and 900s (15 minutes). Optional, defaults to 300s.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>resource_group</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The group resource associated with the configuration.</p></li>
<li><p><strong>selected_regions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of regions from which the check will be run. Some regions contain one location, and others contain more than
one. If this field is specified, enough regions to include a minimum of 3 locations must be provided, or an error
message is returned. Not specifying this field will result in uptime checks running from all regions.</p></li>
<li><p><strong>tcp_check</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Contains information needed to make a TCP check.</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum amount of time to wait for the request to complete (must be between 1 and 60 seconds). Accepted formats
<a class="reference external" href="https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration">https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration</a></p></li>
</ul>
</dd>
</dl>
<p>The <strong>content_matchers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>http_check</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authInfo</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maskHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">validateSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>monitored_resource</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>resource_group</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">groupId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>tcp_check</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.content_matchers">
<code class="sig-name descname">content_matchers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.content_matchers" title="Permalink to this definition">¶</a></dt>
<dd><p>The expected content on the page the check is run against. Currently, only the first entry in the list is supported, and
other entries will be ignored. The server will look for an exact match of the string in the page response’s content.
This field is optional and should only be specified if a content match is required.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-friendly name for the uptime check configuration. The display name should be unique within a Stackdriver
Workspace in order to make it easier to identify; however, uniqueness is not enforced.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.http_check">
<code class="sig-name descname">http_check</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.http_check" title="Permalink to this definition">¶</a></dt>
<dd><p>Contains information needed to make an HTTP or HTTPS check.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authInfo</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maskHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">validateSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.monitored_resource">
<code class="sig-name descname">monitored_resource</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.monitored_resource" title="Permalink to this definition">¶</a></dt>
<dd><p>The monitored resource (<a class="reference external" href="https://cloud.google.com/monitoring/api/resources">https://cloud.google.com/monitoring/api/resources</a>) associated with the configuration. The
following monitored resource types are supported for uptime checks: uptime_url gce_instance gae_app aws_ec2_instance
aws_elb_load_balancer</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique resource name for this UptimeCheckConfig. The format is
projects/[PROJECT_ID]/uptimeCheckConfigs/[UPTIME_CHECK_ID].</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.period">
<code class="sig-name descname">period</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.period" title="Permalink to this definition">¶</a></dt>
<dd><p>How often, in seconds, the uptime check is performed. Currently, the only supported values are 60s (1 minute), 300s (5
minutes), 600s (10 minutes), and 900s (15 minutes). Optional, defaults to 300s.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.resource_group">
<code class="sig-name descname">resource_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.resource_group" title="Permalink to this definition">¶</a></dt>
<dd><p>The group resource associated with the configuration.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">groupId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.selected_regions">
<code class="sig-name descname">selected_regions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.selected_regions" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of regions from which the check will be run. Some regions contain one location, and others contain more than
one. If this field is specified, enough regions to include a minimum of 3 locations must be provided, or an error
message is returned. Not specifying this field will result in uptime checks running from all regions.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.tcp_check">
<code class="sig-name descname">tcp_check</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.tcp_check" title="Permalink to this definition">¶</a></dt>
<dd><p>Contains information needed to make a TCP check.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.timeout">
<code class="sig-name descname">timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum amount of time to wait for the request to complete (must be between 1 and 60 seconds). Accepted formats
<a class="reference external" href="https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration">https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.uptime_check_id">
<code class="sig-name descname">uptime_check_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.uptime_check_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the uptime check</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">content_matchers=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">http_check=None</em>, <em class="sig-param">monitored_resource=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">period=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">resource_group=None</em>, <em class="sig-param">selected_regions=None</em>, <em class="sig-param">tcp_check=None</em>, <em class="sig-param">timeout=None</em>, <em class="sig-param">uptime_check_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UptimeCheckConfig resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>content_matchers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The expected content on the page the check is run against. Currently, only the first entry in the list is supported, and
other entries will be ignored. The server will look for an exact match of the string in the page response’s content.
This field is optional and should only be specified if a content match is required.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-friendly name for the uptime check configuration. The display name should be unique within a Stackdriver
Workspace in order to make it easier to identify; however, uniqueness is not enforced.</p></li>
<li><p><strong>http_check</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Contains information needed to make an HTTP or HTTPS check.</p></li>
<li><p><strong>monitored_resource</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The monitored resource (<a class="reference external" href="https://cloud.google.com/monitoring/api/resources">https://cloud.google.com/monitoring/api/resources</a>) associated with the configuration. The
following monitored resource types are supported for uptime checks: uptime_url gce_instance gae_app aws_ec2_instance
aws_elb_load_balancer</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique resource name for this UptimeCheckConfig. The format is
projects/[PROJECT_ID]/uptimeCheckConfigs/[UPTIME_CHECK_ID].</p></li>
<li><p><strong>period</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – How often, in seconds, the uptime check is performed. Currently, the only supported values are 60s (1 minute), 300s (5
minutes), 600s (10 minutes), and 900s (15 minutes). Optional, defaults to 300s.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>resource_group</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The group resource associated with the configuration.</p></li>
<li><p><strong>selected_regions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of regions from which the check will be run. Some regions contain one location, and others contain more than
one. If this field is specified, enough regions to include a minimum of 3 locations must be provided, or an error
message is returned. Not specifying this field will result in uptime checks running from all regions.</p></li>
<li><p><strong>tcp_check</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Contains information needed to make a TCP check.</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The maximum amount of time to wait for the request to complete (must be between 1 and 60 seconds). Accepted formats
<a class="reference external" href="https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration">https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#google.protobuf.Duration</a></p></li>
<li><p><strong>uptime_check_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the uptime check</p></li>
</ul>
</dd>
</dl>
<p>The <strong>content_matchers</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>http_check</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">authInfo</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maskHeaders</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">useSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">validateSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>monitored_resource</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">labels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>resource_group</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">groupId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">resourceType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>tcp_check</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">port</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.monitoring.UptimeCheckConfig.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.UptimeCheckConfig.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.monitoring.get_notification_channel">
<code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">get_notification_channel</code><span class="sig-paren">(</span><em class="sig-param">display_name=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">user_labels=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.get_notification_channel" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.monitoring.get_secret_version">
<code class="sig-prename descclassname">pulumi_gcp.monitoring.</code><code class="sig-name descname">get_secret_version</code><span class="sig-paren">(</span><em class="sig-param">project=None</em>, <em class="sig-param">secret=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.monitoring.get_secret_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

</div>
