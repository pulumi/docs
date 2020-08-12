---
title: Package pulumi_wavefront
title_tag: Package pulumi_wavefront | Python SDK
linktitle: pulumi_wavefront
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "wavefront" >}}

<div class="section" id="pulumi-wavefront">
<h1>Pulumi Wavefront<a class="headerlink" href="#pulumi-wavefront" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-wavefront">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-wavefront/issues">pulumi/pulumi-wavefront repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-wavefront/issues">terraform-providers/terraform-provider-wavefront repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_wavefront"></span><dl class="py class">
<dt id="pulumi_wavefront.Alert">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">Alert</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_information</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">can_modifies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">can_views</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">conditions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_expression</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">minutes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_resend_frequency_minutes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resolve_after_minutes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">severity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">threshold_targets</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.Alert" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Wavefront Alert resource.  This allows alerts to be created, updated, and deleted.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_wavefront</span> <span class="k">as</span> <span class="nn">wavefront</span>

<span class="n">foobar</span> <span class="o">=</span> <span class="n">wavefront</span><span class="o">.</span><span class="n">Alert</span><span class="p">(</span><span class="s2">&quot;foobar&quot;</span><span class="p">,</span>
    <span class="n">condition</span><span class="o">=</span><span class="s2">&quot;100-ts(&quot;</span><span class="n">cpu</span><span class="o">.</span><span class="n">usage_idle</span><span class="s2">&quot;, environment=preprod and cpu=cpu-total ) &gt; 80&quot;</span><span class="p">,</span>
    <span class="n">display_expression</span><span class="o">=</span><span class="s2">&quot;100-ts(&quot;</span><span class="n">cpu</span><span class="o">.</span><span class="n">usage_idle</span><span class="s2">&quot;, environment=preprod and cpu=cpu-total )&quot;</span><span class="p">,</span>
    <span class="n">minutes</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
    <span class="n">resolve_after_minutes</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
    <span class="n">severity</span><span class="o">=</span><span class="s2">&quot;WARN&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;terraform&quot;</span><span class="p">,</span>
        <span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">target</span><span class="o">=</span><span class="s2">&quot;test@example.com&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_information</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User-supplied additional explanatory information for this alert.
Useful for linking runbooks, migrations…etc</p></li>
<li><p><strong>alert_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of alert in Wavefront.  Either <code class="docutils literal notranslate"><span class="pre">CLASSIC</span></code> (default) 
or <code class="docutils literal notranslate"><span class="pre">THRESHOLD</span></code></p></li>
<li><p><strong>can_modifies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of users or groups that can modify this resource.</p></li>
<li><p><strong>can_views</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of users or groups that can view this resource.</p></li>
<li><p><strong>condition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A Wavefront query that is evaluated at regular intervals (default 1m).
The alert fires and notifications are triggered when data series matching this query evaluates
to a non-zero value for a set number of consecutive minutes.</p></li>
<li><p><strong>conditions</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – a string-&gt;string map of <code class="docutils literal notranslate"><span class="pre">severity</span></code> to <code class="docutils literal notranslate"><span class="pre">condition</span></code> 
for which this alert will trigger.</p></li>
<li><p><strong>display_expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A second query whose results are displayed in the alert user
interface instead of the condition query.  This field is often used to display a version
of the condition query with Boolean operators removed so that numerical values are plotted.</p></li>
<li><p><strong>minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of consecutive minutes that a series matching the condition query must 
evaluate to “true” (non-zero value) before the alert fires.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the alert as it is displayed in Wavefront.</p></li>
<li><p><strong>notification_resend_frequency_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How often to re-trigger a continually failing alert. 
If absent or &lt;= 0, no re-triggering occur.</p></li>
<li><p><strong>resolve_after_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of consecutive minutes that a firing series matching the condition
query must evaluate to “false” (zero value) before the alert resolves.  When unset, this default sto
the same value as <code class="docutils literal notranslate"><span class="pre">minutes</span></code>.</p></li>
<li><p><strong>severity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <ul>
<li><p>Severity of the alert, valid values are <code class="docutils literal notranslate"><span class="pre">INFO</span></code>, <code class="docutils literal notranslate"><span class="pre">SMOKE</span></code>, <code class="docutils literal notranslate"><span class="pre">WARN</span></code>, <code class="docutils literal notranslate"><span class="pre">SEVERE</span></code>.</p></li>
</ul>
</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of tags to assign to this resource.</p></li>
<li><p><strong>target</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A comma-separated list of the email address or integration endpoint 
(such as PagerDuty or web hook) to notify when the alert status changes.</p></li>
<li><p><strong>threshold_targets</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Targets for severity</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_wavefront.Alert.additional_information">
<code class="sig-name descname">additional_information</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.Alert.additional_information" title="Permalink to this definition">¶</a></dt>
<dd><p>User-supplied additional explanatory information for this alert.
Useful for linking runbooks, migrations…etc</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.Alert.alert_type">
<code class="sig-name descname">alert_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.Alert.alert_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of alert in Wavefront.  Either <code class="docutils literal notranslate"><span class="pre">CLASSIC</span></code> (default) 
or <code class="docutils literal notranslate"><span class="pre">THRESHOLD</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.Alert.can_modifies">
<code class="sig-name descname">can_modifies</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.Alert.can_modifies" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of users or groups that can modify this resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.Alert.can_views">
<code class="sig-name descname">can_views</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.Alert.can_views" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of users or groups that can view this resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.Alert.condition">
<code class="sig-name descname">condition</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.Alert.condition" title="Permalink to this definition">¶</a></dt>
<dd><p>A Wavefront query that is evaluated at regular intervals (default 1m).
The alert fires and notifications are triggered when data series matching this query evaluates
to a non-zero value for a set number of consecutive minutes.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.Alert.conditions">
<code class="sig-name descname">conditions</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.Alert.conditions" title="Permalink to this definition">¶</a></dt>
<dd><p>a string-&gt;string map of <code class="docutils literal notranslate"><span class="pre">severity</span></code> to <code class="docutils literal notranslate"><span class="pre">condition</span></code> 
for which this alert will trigger.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.Alert.display_expression">
<code class="sig-name descname">display_expression</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.Alert.display_expression" title="Permalink to this definition">¶</a></dt>
<dd><p>A second query whose results are displayed in the alert user
interface instead of the condition query.  This field is often used to display a version
of the condition query with Boolean operators removed so that numerical values are plotted.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.Alert.minutes">
<code class="sig-name descname">minutes</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.Alert.minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of consecutive minutes that a series matching the condition query must 
evaluate to “true” (non-zero value) before the alert fires.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.Alert.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.Alert.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the alert as it is displayed in Wavefront.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.Alert.notification_resend_frequency_minutes">
<code class="sig-name descname">notification_resend_frequency_minutes</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.Alert.notification_resend_frequency_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>How often to re-trigger a continually failing alert. 
If absent or &lt;= 0, no re-triggering occur.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.Alert.resolve_after_minutes">
<code class="sig-name descname">resolve_after_minutes</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.Alert.resolve_after_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of consecutive minutes that a firing series matching the condition
query must evaluate to “false” (zero value) before the alert resolves.  When unset, this default sto
the same value as <code class="docutils literal notranslate"><span class="pre">minutes</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.Alert.severity">
<code class="sig-name descname">severity</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.Alert.severity" title="Permalink to this definition">¶</a></dt>
<dd><ul class="simple">
<li><p>Severity of the alert, valid values are <code class="docutils literal notranslate"><span class="pre">INFO</span></code>, <code class="docutils literal notranslate"><span class="pre">SMOKE</span></code>, <code class="docutils literal notranslate"><span class="pre">WARN</span></code>, <code class="docutils literal notranslate"><span class="pre">SEVERE</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.Alert.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.Alert.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of tags to assign to this resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.Alert.target">
<code class="sig-name descname">target</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.Alert.target" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma-separated list of the email address or integration endpoint 
(such as PagerDuty or web hook) to notify when the alert status changes.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.Alert.threshold_targets">
<code class="sig-name descname">threshold_targets</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.Alert.threshold_targets" title="Permalink to this definition">¶</a></dt>
<dd><p>Targets for severity</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.Alert.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_information</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">can_modifies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">can_views</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">conditions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_expression</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">minutes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_resend_frequency_minutes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resolve_after_minutes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">severity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">threshold_targets</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.Alert.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Alert resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_information</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User-supplied additional explanatory information for this alert.
Useful for linking runbooks, migrations…etc</p></li>
<li><p><strong>alert_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of alert in Wavefront.  Either <code class="docutils literal notranslate"><span class="pre">CLASSIC</span></code> (default) 
or <code class="docutils literal notranslate"><span class="pre">THRESHOLD</span></code></p></li>
<li><p><strong>can_modifies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of users or groups that can modify this resource.</p></li>
<li><p><strong>can_views</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of users or groups that can view this resource.</p></li>
<li><p><strong>condition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A Wavefront query that is evaluated at regular intervals (default 1m).
The alert fires and notifications are triggered when data series matching this query evaluates
to a non-zero value for a set number of consecutive minutes.</p></li>
<li><p><strong>conditions</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – a string-&gt;string map of <code class="docutils literal notranslate"><span class="pre">severity</span></code> to <code class="docutils literal notranslate"><span class="pre">condition</span></code> 
for which this alert will trigger.</p></li>
<li><p><strong>display_expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A second query whose results are displayed in the alert user
interface instead of the condition query.  This field is often used to display a version
of the condition query with Boolean operators removed so that numerical values are plotted.</p></li>
<li><p><strong>minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of consecutive minutes that a series matching the condition query must 
evaluate to “true” (non-zero value) before the alert fires.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the alert as it is displayed in Wavefront.</p></li>
<li><p><strong>notification_resend_frequency_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How often to re-trigger a continually failing alert. 
If absent or &lt;= 0, no re-triggering occur.</p></li>
<li><p><strong>resolve_after_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of consecutive minutes that a firing series matching the condition
query must evaluate to “false” (zero value) before the alert resolves.  When unset, this default sto
the same value as <code class="docutils literal notranslate"><span class="pre">minutes</span></code>.</p></li>
<li><p><strong>severity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <ul>
<li><p>Severity of the alert, valid values are <code class="docutils literal notranslate"><span class="pre">INFO</span></code>, <code class="docutils literal notranslate"><span class="pre">SMOKE</span></code>, <code class="docutils literal notranslate"><span class="pre">WARN</span></code>, <code class="docutils literal notranslate"><span class="pre">SEVERE</span></code>.</p></li>
</ul>
</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of tags to assign to this resource.</p></li>
<li><p><strong>target</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A comma-separated list of the email address or integration endpoint 
(such as PagerDuty or web hook) to notify when the alert status changes.</p></li>
<li><p><strong>threshold_targets</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Targets for severity</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.Alert.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.Alert.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.Alert.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.Alert.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.AlertTarget">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">AlertTarget</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_headers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_subject</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_html_content</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recipient</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">routes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">triggers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.AlertTarget" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a wavefront Alert Target resource. This allows alert targets to created, updated, and deleted.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_wavefront</span> <span class="k">as</span> <span class="nn">wavefront</span>

<span class="n">test_target</span> <span class="o">=</span> <span class="n">wavefront</span><span class="o">.</span><span class="n">AlertTarget</span><span class="p">(</span><span class="s2">&quot;testTarget&quot;</span><span class="p">,</span>
    <span class="n">content_type</span><span class="o">=</span><span class="s2">&quot;application/json&quot;</span><span class="p">,</span>
    <span class="n">custom_headers</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;Testing&quot;</span><span class="p">:</span> <span class="s2">&quot;true&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Test target&quot;</span><span class="p">,</span>
    <span class="n">method</span><span class="o">=</span><span class="s2">&quot;WEBHOOK&quot;</span><span class="p">,</span>
    <span class="n">recipient</span><span class="o">=</span><span class="s2">&quot;https://hooks.slack.com/services/test/me&quot;</span><span class="p">,</span>
    <span class="n">template</span><span class="o">=</span><span class="s2">&quot;</span><span class="si">{}</span><span class="s2">&quot;</span><span class="p">,</span>
    <span class="n">triggers</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;ALERT_OPENED&quot;</span><span class="p">,</span>
        <span class="s2">&quot;ALERT_RESOLVED&quot;</span><span class="p">,</span>
    <span class="p">])</span>
</pre></div>
</div>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">target_id</span></code> - The target ID prefixed with <code class="docutils literal notranslate"><span class="pre">target:</span></code> for interpolating into a Wavefront Alert.</p></li>
</ul>
<p>The <code class="docutils literal notranslate"><span class="pre">route</span></code> mapping supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> - (Required)  The notification method used for notification target. One of <code class="docutils literal notranslate"><span class="pre">WEBHOOK</span></code>, <code class="docutils literal notranslate"><span class="pre">EMAIL</span></code>, <code class="docutils literal notranslate"><span class="pre">PAGERDUTY</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> - (Required) The endpoint for the alert route. <cite>EMAIL</cite>: email address. <cite>PAGERDUTY</cite>: PagerDuty routing
key. <code class="docutils literal notranslate"><span class="pre">WEBHOOK</span></code>: URL endpoint.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">filter</span></code> - (Required) String that filters the route. Space delimited.  Currently only allows a single key value pair.
(e.g. <code class="docutils literal notranslate"><span class="pre">env</span> <span class="pre">prod</span></code>)</p></li>
</ul>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_wavefront</span> <span class="k">as</span> <span class="nn">wavefront</span>

<span class="n">test_target</span> <span class="o">=</span> <span class="n">wavefront</span><span class="o">.</span><span class="n">AlertTarget</span><span class="p">(</span><span class="s2">&quot;testTarget&quot;</span><span class="p">,</span>
    <span class="n">content_type</span><span class="o">=</span><span class="s2">&quot;application/json&quot;</span><span class="p">,</span>
    <span class="n">custom_headers</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;Testing&quot;</span><span class="p">:</span> <span class="s2">&quot;true&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Test target&quot;</span><span class="p">,</span>
    <span class="n">method</span><span class="o">=</span><span class="s2">&quot;WEBHOOK&quot;</span><span class="p">,</span>
    <span class="n">recipient</span><span class="o">=</span><span class="s2">&quot;https://hooks.slack.com/services/test/me&quot;</span><span class="p">,</span>
    <span class="n">routes</span><span class="o">=</span><span class="p">[</span>
        <span class="p">{</span>
            <span class="s2">&quot;filter&quot;</span><span class="p">:</span> <span class="p">{</span>
                <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;env&quot;</span><span class="p">,</span>
                <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;prod&quot;</span><span class="p">,</span>
            <span class="p">},</span>
            <span class="s2">&quot;method&quot;</span><span class="p">:</span> <span class="s2">&quot;WEBHOOK&quot;</span><span class="p">,</span>
            <span class="s2">&quot;target&quot;</span><span class="p">:</span> <span class="s2">&quot;https://hooks.slack.com/services/test/me/prod&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;filter&quot;</span><span class="p">:</span> <span class="p">{</span>
                <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;env&quot;</span><span class="p">,</span>
                <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;dev&quot;</span><span class="p">,</span>
            <span class="p">},</span>
            <span class="s2">&quot;method&quot;</span><span class="p">:</span> <span class="s2">&quot;WEBHOOK&quot;</span><span class="p">,</span>
            <span class="s2">&quot;target&quot;</span><span class="p">:</span> <span class="s2">&quot;https://hooks.slack.com/services/test/me/dev&quot;</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">],</span>
    <span class="n">template</span><span class="o">=</span><span class="s2">&quot;</span><span class="si">{}</span><span class="s2">&quot;</span><span class="p">,</span>
    <span class="n">triggers</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;ALERT_OPENED&quot;</span><span class="p">,</span>
        <span class="s2">&quot;ALERT_RESOLVED&quot;</span><span class="p">,</span>
    <span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>content_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of the <code class="docutils literal notranslate"><span class="pre">Content-Type</span></code> header of the webhook.</p></li>
<li><p><strong>custom_headers</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">string-&gt;string</span></code> map specifying the custome HTTP header key/value pairs that will be 
sent in the requests with a method of <code class="docutils literal notranslate"><span class="pre">WEBHOOK</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description describing this alert target.</p></li>
<li><p><strong>email_subject</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The subject title of an email notification target.</p></li>
<li><p><strong>is_html_content</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determine whether the email alert content is sent as HTML or text.</p></li>
<li><p><strong>method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The notification method used for notification target. One of <code class="docutils literal notranslate"><span class="pre">WEBHOOK</span></code>, <code class="docutils literal notranslate"><span class="pre">EMAIL</span></code>, <code class="docutils literal notranslate"><span class="pre">PAGERDUTY</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the alert target as it is displayed in wavefront</p></li>
<li><p><strong>recipient</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The end point for the notification Target.  <cite>EMAIL</cite>: email address. <cite>PAGERDUTY</cite>: PagerDuty 
routing key. <code class="docutils literal notranslate"><span class="pre">WEBHOOK</span></code>: URL endpoint.</p></li>
<li><p><strong>routes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of routing targets that this alert target will notify. See Route</p></li>
<li><p><strong>template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A mustache template that will form the body of the POST request, email and summary of the PagerDuty.</p></li>
<li><p><strong>triggers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of occurrences on which this webhook will be fired. Valid values are <code class="docutils literal notranslate"><span class="pre">ALERT_OPENED</span></code>,
<code class="docutils literal notranslate"><span class="pre">ALERT_UPDATED</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_RESOLVED</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_MAINTENANCE</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_SNOOZED</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_INVALID</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_NO_LONGER_INVALID</span></code>,
<code class="docutils literal notranslate"><span class="pre">ALERT_RETRIGGERED</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_NO_DATA</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_NO_DATA_RESOLVED</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_NO_DATA_MAINTENANCE</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_SEVERITY_UPDATE</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>routes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The notification method used for notification target. One of <code class="docutils literal notranslate"><span class="pre">WEBHOOK</span></code>, <code class="docutils literal notranslate"><span class="pre">EMAIL</span></code>, <code class="docutils literal notranslate"><span class="pre">PAGERDUTY</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_wavefront.AlertTarget.content_type">
<code class="sig-name descname">content_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.AlertTarget.content_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the <code class="docutils literal notranslate"><span class="pre">Content-Type</span></code> header of the webhook.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.AlertTarget.custom_headers">
<code class="sig-name descname">custom_headers</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.AlertTarget.custom_headers" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">string-&gt;string</span></code> map specifying the custome HTTP header key/value pairs that will be 
sent in the requests with a method of <code class="docutils literal notranslate"><span class="pre">WEBHOOK</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.AlertTarget.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.AlertTarget.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description describing this alert target.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.AlertTarget.email_subject">
<code class="sig-name descname">email_subject</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.AlertTarget.email_subject" title="Permalink to this definition">¶</a></dt>
<dd><p>The subject title of an email notification target.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.AlertTarget.is_html_content">
<code class="sig-name descname">is_html_content</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.AlertTarget.is_html_content" title="Permalink to this definition">¶</a></dt>
<dd><p>Determine whether the email alert content is sent as HTML or text.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.AlertTarget.method">
<code class="sig-name descname">method</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.AlertTarget.method" title="Permalink to this definition">¶</a></dt>
<dd><p>The notification method used for notification target. One of <code class="docutils literal notranslate"><span class="pre">WEBHOOK</span></code>, <code class="docutils literal notranslate"><span class="pre">EMAIL</span></code>, <code class="docutils literal notranslate"><span class="pre">PAGERDUTY</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.AlertTarget.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.AlertTarget.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the alert target as it is displayed in wavefront</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.AlertTarget.recipient">
<code class="sig-name descname">recipient</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.AlertTarget.recipient" title="Permalink to this definition">¶</a></dt>
<dd><p>The end point for the notification Target.  <cite>EMAIL</cite>: email address. <cite>PAGERDUTY</cite>: PagerDuty 
routing key. <code class="docutils literal notranslate"><span class="pre">WEBHOOK</span></code>: URL endpoint.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.AlertTarget.routes">
<code class="sig-name descname">routes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.AlertTarget.routes" title="Permalink to this definition">¶</a></dt>
<dd><p>List of routing targets that this alert target will notify. See Route</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filter</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The notification method used for notification target. One of <code class="docutils literal notranslate"><span class="pre">WEBHOOK</span></code>, <code class="docutils literal notranslate"><span class="pre">EMAIL</span></code>, <code class="docutils literal notranslate"><span class="pre">PAGERDUTY</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.AlertTarget.template">
<code class="sig-name descname">template</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.AlertTarget.template" title="Permalink to this definition">¶</a></dt>
<dd><p>A mustache template that will form the body of the POST request, email and summary of the PagerDuty.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.AlertTarget.triggers">
<code class="sig-name descname">triggers</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.AlertTarget.triggers" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of occurrences on which this webhook will be fired. Valid values are <code class="docutils literal notranslate"><span class="pre">ALERT_OPENED</span></code>,
<code class="docutils literal notranslate"><span class="pre">ALERT_UPDATED</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_RESOLVED</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_MAINTENANCE</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_SNOOZED</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_INVALID</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_NO_LONGER_INVALID</span></code>,
<code class="docutils literal notranslate"><span class="pre">ALERT_RETRIGGERED</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_NO_DATA</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_NO_DATA_RESOLVED</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_NO_DATA_MAINTENANCE</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_SEVERITY_UPDATE</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.AlertTarget.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_headers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_subject</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_html_content</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recipient</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">routes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">triggers</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.AlertTarget.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AlertTarget resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>content_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of the <code class="docutils literal notranslate"><span class="pre">Content-Type</span></code> header of the webhook.</p></li>
<li><p><strong>custom_headers</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">string-&gt;string</span></code> map specifying the custome HTTP header key/value pairs that will be 
sent in the requests with a method of <code class="docutils literal notranslate"><span class="pre">WEBHOOK</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description describing this alert target.</p></li>
<li><p><strong>email_subject</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The subject title of an email notification target.</p></li>
<li><p><strong>is_html_content</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determine whether the email alert content is sent as HTML or text.</p></li>
<li><p><strong>method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The notification method used for notification target. One of <code class="docutils literal notranslate"><span class="pre">WEBHOOK</span></code>, <code class="docutils literal notranslate"><span class="pre">EMAIL</span></code>, <code class="docutils literal notranslate"><span class="pre">PAGERDUTY</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the alert target as it is displayed in wavefront</p></li>
<li><p><strong>recipient</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The end point for the notification Target.  <cite>EMAIL</cite>: email address. <cite>PAGERDUTY</cite>: PagerDuty 
routing key. <code class="docutils literal notranslate"><span class="pre">WEBHOOK</span></code>: URL endpoint.</p></li>
<li><p><strong>routes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of routing targets that this alert target will notify. See Route</p></li>
<li><p><strong>template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A mustache template that will form the body of the POST request, email and summary of the PagerDuty.</p></li>
<li><p><strong>triggers</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of occurrences on which this webhook will be fired. Valid values are <code class="docutils literal notranslate"><span class="pre">ALERT_OPENED</span></code>,
<code class="docutils literal notranslate"><span class="pre">ALERT_UPDATED</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_RESOLVED</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_MAINTENANCE</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_SNOOZED</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_INVALID</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_NO_LONGER_INVALID</span></code>,
<code class="docutils literal notranslate"><span class="pre">ALERT_RETRIGGERED</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_NO_DATA</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_NO_DATA_RESOLVED</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_NO_DATA_MAINTENANCE</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_SEVERITY_UPDATE</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>routes</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">filter</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">method</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The notification method used for notification target. One of <code class="docutils literal notranslate"><span class="pre">WEBHOOK</span></code>, <code class="docutils literal notranslate"><span class="pre">EMAIL</span></code>, <code class="docutils literal notranslate"><span class="pre">PAGERDUTY</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">target</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.AlertTarget.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.AlertTarget.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.AlertTarget.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.AlertTarget.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.AwaitableGetDefaultUserGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">AwaitableGetDefaultUserGroupResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.AwaitableGetDefaultUserGroupResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">CloudIntegrationAppDynamics</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_filter_regexes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">controller_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_app_infra_metrics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_backend_metrics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_business_trx_metrics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_error_metrics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_individual_node_metrics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_overall_perf_metrics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_rollup</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_service_endpoint_metrics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encrypted_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Wavefront Cloud Integration for App Dynamics. This allows app dynamics cloud integrations to be created,
updated, and deleted.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_wavefront</span> <span class="k">as</span> <span class="nn">wavefront</span>

<span class="n">app_dynamics</span> <span class="o">=</span> <span class="n">wavefront</span><span class="o">.</span><span class="n">CloudIntegrationAppDynamics</span><span class="p">(</span><span class="s2">&quot;appDynamics&quot;</span><span class="p">,</span>
    <span class="n">controller_name</span><span class="o">=</span><span class="s2">&quot;exampleController&quot;</span><span class="p">,</span>
    <span class="n">encrypted_password</span><span class="o">=</span><span class="s2">&quot;encryptedPassword&quot;</span><span class="p">,</span>
    <span class="n">user_name</span><span class="o">=</span><span class="s2">&quot;example&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>app_filter_regexes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of regular expressions that a application name must match (case-insensitively) 
in order to be ingested</p></li>
<li><p><strong>controller_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the SaaS controller</p></li>
<li><p><strong>enable_app_infra_metrics</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag to control Application Infrastructure metric injection</p></li>
<li><p><strong>enable_backend_metrics</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag to control Backend metric injection</p></li>
<li><p><strong>enable_business_trx_metrics</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag to control Business Transaction metric injection</p></li>
<li><p><strong>enable_error_metrics</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag to control Error metric injection</p></li>
<li><p><strong>enable_individual_node_metrics</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag to control Individual Node metric injection</p></li>
<li><p><strong>enable_overall_perf_metrics</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag to control Overall Performance metric injection</p></li>
<li><p><strong>enable_rollup</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set this to <code class="docutils literal notranslate"><span class="pre">false</span></code> to get separate results for all values within the time range, 
by default it is <code class="docutils literal notranslate"><span class="pre">true</span></code></p></li>
<li><p><strong>enable_service_endpoint_metrics</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag to control Service End point metric injection</p></li>
<li><p><strong>encrypted_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password for AppDynamics user</p></li>
<li><p><strong>force_save</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Forces this resource to save, even if errors are present</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable name of this integration</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value denoting which cloud service this service integrates with</p></li>
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
<li><p><strong>user_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username is a combination of userName and the account name</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.additional_tags">
<code class="sig-name descname">additional_tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.additional_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of point tag key-values to add to every point ingested using this integration</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.app_filter_regexes">
<code class="sig-name descname">app_filter_regexes</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.app_filter_regexes" title="Permalink to this definition">¶</a></dt>
<dd><p>List of regular expressions that a application name must match (case-insensitively) 
in order to be ingested</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.controller_name">
<code class="sig-name descname">controller_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.controller_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the SaaS controller</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.enable_app_infra_metrics">
<code class="sig-name descname">enable_app_infra_metrics</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.enable_app_infra_metrics" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag to control Application Infrastructure metric injection</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.enable_backend_metrics">
<code class="sig-name descname">enable_backend_metrics</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.enable_backend_metrics" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag to control Backend metric injection</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.enable_business_trx_metrics">
<code class="sig-name descname">enable_business_trx_metrics</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.enable_business_trx_metrics" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag to control Business Transaction metric injection</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.enable_error_metrics">
<code class="sig-name descname">enable_error_metrics</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.enable_error_metrics" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag to control Error metric injection</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.enable_individual_node_metrics">
<code class="sig-name descname">enable_individual_node_metrics</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.enable_individual_node_metrics" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag to control Individual Node metric injection</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.enable_overall_perf_metrics">
<code class="sig-name descname">enable_overall_perf_metrics</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.enable_overall_perf_metrics" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag to control Overall Performance metric injection</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.enable_rollup">
<code class="sig-name descname">enable_rollup</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.enable_rollup" title="Permalink to this definition">¶</a></dt>
<dd><p>Set this to <code class="docutils literal notranslate"><span class="pre">false</span></code> to get separate results for all values within the time range, 
by default it is <code class="docutils literal notranslate"><span class="pre">true</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.enable_service_endpoint_metrics">
<code class="sig-name descname">enable_service_endpoint_metrics</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.enable_service_endpoint_metrics" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag to control Service End point metric injection</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.encrypted_password">
<code class="sig-name descname">encrypted_password</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.encrypted_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Password for AppDynamics user</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.force_save">
<code class="sig-name descname">force_save</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.force_save" title="Permalink to this definition">¶</a></dt>
<dd><p>Forces this resource to save, even if errors are present</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The human-readable name of this integration</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.service">
<code class="sig-name descname">service</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.service" title="Permalink to this definition">¶</a></dt>
<dd><p>A value denoting which cloud service this service integrates with</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.service_refresh_rate_in_minutes">
<code class="sig-name descname">service_refresh_rate_in_minutes</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.service_refresh_rate_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>How often, in minutes, to refresh the service</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.user_name">
<code class="sig-name descname">user_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.user_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Username is a combination of userName and the account name</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_filter_regexes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">controller_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_app_infra_metrics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_backend_metrics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_business_trx_metrics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_error_metrics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_individual_node_metrics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_overall_perf_metrics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_rollup</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_service_endpoint_metrics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encrypted_password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CloudIntegrationAppDynamics resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>app_filter_regexes</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of regular expressions that a application name must match (case-insensitively) 
in order to be ingested</p></li>
<li><p><strong>controller_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the SaaS controller</p></li>
<li><p><strong>enable_app_infra_metrics</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag to control Application Infrastructure metric injection</p></li>
<li><p><strong>enable_backend_metrics</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag to control Backend metric injection</p></li>
<li><p><strong>enable_business_trx_metrics</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag to control Business Transaction metric injection</p></li>
<li><p><strong>enable_error_metrics</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag to control Error metric injection</p></li>
<li><p><strong>enable_individual_node_metrics</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag to control Individual Node metric injection</p></li>
<li><p><strong>enable_overall_perf_metrics</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag to control Overall Performance metric injection</p></li>
<li><p><strong>enable_rollup</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set this to <code class="docutils literal notranslate"><span class="pre">false</span></code> to get separate results for all values within the time range, 
by default it is <code class="docutils literal notranslate"><span class="pre">true</span></code></p></li>
<li><p><strong>enable_service_endpoint_metrics</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean flag to control Service End point metric injection</p></li>
<li><p><strong>encrypted_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password for AppDynamics user</p></li>
<li><p><strong>force_save</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Forces this resource to save, even if errors are present</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable name of this integration</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value denoting which cloud service this service integrates with</p></li>
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
<li><p><strong>user_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username is a combination of userName and the account name</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.CloudIntegrationAwsExternalId">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">CloudIntegrationAwsExternalId</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAwsExternalId" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an External ID for use in AWS IAM Roles.  This allows External IDs to be created and deleted.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_wavefront</span> <span class="k">as</span> <span class="nn">wavefront</span>

<span class="n">external_id</span> <span class="o">=</span> <span class="n">wavefront</span><span class="o">.</span><span class="n">CloudIntegrationAwsExternalId</span><span class="p">(</span><span class="s2">&quot;externalId&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAwsExternalId.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAwsExternalId.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CloudIntegrationAwsExternalId resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAwsExternalId.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAwsExternalId.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.CloudIntegrationAwsExternalId.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAwsExternalId.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.CloudIntegrationAzure">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">CloudIntegrationAzure</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">category_filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_secret</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_filter_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzure" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Wavefront Cloud Integration for Azure. This allows azure cloud integrations to be created,
updated, and deleted.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_wavefront</span> <span class="k">as</span> <span class="nn">wavefront</span>

<span class="n">azure_activity_log</span> <span class="o">=</span> <span class="n">wavefront</span><span class="o">.</span><span class="n">CloudIntegrationAzureActivityLog</span><span class="p">(</span><span class="s2">&quot;azureActivityLog&quot;</span><span class="p">,</span>
    <span class="n">client_id</span><span class="o">=</span><span class="s2">&quot;client-id2&quot;</span><span class="p">,</span>
    <span class="n">client_secret</span><span class="o">=</span><span class="s2">&quot;client-secret2&quot;</span><span class="p">,</span>
    <span class="n">tenant</span><span class="o">=</span><span class="s2">&quot;my-tenant2&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>category_filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Azure Activity Log categories.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client id for an azure service account within your project</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client secret for an Azure service account within your project</p></li>
<li><p><strong>force_save</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Forces this resource to save, even if errors are present</p></li>
<li><p><strong>metric_filter_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A regular expression that a metric name must match (case-insensitively) in order to be ingested</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable name of this integration</p></li>
<li><p><strong>resource_group_filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Azure resource groups from which to pull metrics</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value denoting which cloud service this service integrates with</p></li>
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
<li><p><strong>tenant</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Tenant Id for an Azure service account within your project</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationAzure.additional_tags">
<code class="sig-name descname">additional_tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzure.additional_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of point tag key-values to add to every point ingested using this integration</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationAzure.category_filters">
<code class="sig-name descname">category_filters</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzure.category_filters" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Azure Activity Log categories.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationAzure.client_id">
<code class="sig-name descname">client_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzure.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Client id for an azure service account within your project</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationAzure.client_secret">
<code class="sig-name descname">client_secret</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzure.client_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>Client secret for an Azure service account within your project</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationAzure.force_save">
<code class="sig-name descname">force_save</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzure.force_save" title="Permalink to this definition">¶</a></dt>
<dd><p>Forces this resource to save, even if errors are present</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationAzure.metric_filter_regex">
<code class="sig-name descname">metric_filter_regex</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzure.metric_filter_regex" title="Permalink to this definition">¶</a></dt>
<dd><p>A regular expression that a metric name must match (case-insensitively) in order to be ingested</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationAzure.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzure.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The human-readable name of this integration</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationAzure.resource_group_filters">
<code class="sig-name descname">resource_group_filters</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzure.resource_group_filters" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Azure resource groups from which to pull metrics</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationAzure.service">
<code class="sig-name descname">service</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzure.service" title="Permalink to this definition">¶</a></dt>
<dd><p>A value denoting which cloud service this service integrates with</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationAzure.service_refresh_rate_in_minutes">
<code class="sig-name descname">service_refresh_rate_in_minutes</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzure.service_refresh_rate_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>How often, in minutes, to refresh the service</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationAzure.tenant">
<code class="sig-name descname">tenant</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzure.tenant" title="Permalink to this definition">¶</a></dt>
<dd><p>Tenant Id for an Azure service account within your project</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAzure.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">category_filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_secret</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_filter_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzure.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CloudIntegrationAzure resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>category_filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Azure Activity Log categories.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client id for an azure service account within your project</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client secret for an Azure service account within your project</p></li>
<li><p><strong>force_save</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Forces this resource to save, even if errors are present</p></li>
<li><p><strong>metric_filter_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A regular expression that a metric name must match (case-insensitively) in order to be ingested</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable name of this integration</p></li>
<li><p><strong>resource_group_filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Azure resource groups from which to pull metrics</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value denoting which cloud service this service integrates with</p></li>
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
<li><p><strong>tenant</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Tenant Id for an Azure service account within your project</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAzure.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzure.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.CloudIntegrationAzure.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzure.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.CloudIntegrationAzureActivityLog">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">CloudIntegrationAzureActivityLog</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">category_filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_secret</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzureActivityLog" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Wavefront Cloud Integration for Azure Activity Logs. This allows azure activity log cloud integrations to be created,
updated, and deleted.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_wavefront</span> <span class="k">as</span> <span class="nn">wavefront</span>

<span class="n">azure_activity_log</span> <span class="o">=</span> <span class="n">wavefront</span><span class="o">.</span><span class="n">CloudIntegrationAzureActivityLog</span><span class="p">(</span><span class="s2">&quot;azureActivityLog&quot;</span><span class="p">,</span>
    <span class="n">category_filters</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;ADMINISTRATIVE&quot;</span><span class="p">],</span>
    <span class="n">client_id</span><span class="o">=</span><span class="s2">&quot;client-id2&quot;</span><span class="p">,</span>
    <span class="n">client_secret</span><span class="o">=</span><span class="s2">&quot;client-secret2&quot;</span><span class="p">,</span>
    <span class="n">tenant</span><span class="o">=</span><span class="s2">&quot;my-tenant2&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>category_filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Azure services (such as Microsoft.Compute/virtualMachines) from which to pull metrics</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client id for an azure service account within your project</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client secret for an Azure service account within your project</p></li>
<li><p><strong>force_save</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Forces this resource to save, even if errors are present</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable name of this integration</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value denoting which cloud service this service integrates with</p></li>
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
<li><p><strong>tenant</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Tenant Id for an Azure service account within your project</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationAzureActivityLog.additional_tags">
<code class="sig-name descname">additional_tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzureActivityLog.additional_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of point tag key-values to add to every point ingested using this integration</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationAzureActivityLog.category_filters">
<code class="sig-name descname">category_filters</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzureActivityLog.category_filters" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Azure services (such as Microsoft.Compute/virtualMachines) from which to pull metrics</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationAzureActivityLog.client_id">
<code class="sig-name descname">client_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzureActivityLog.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Client id for an azure service account within your project</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationAzureActivityLog.client_secret">
<code class="sig-name descname">client_secret</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzureActivityLog.client_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>Client secret for an Azure service account within your project</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationAzureActivityLog.force_save">
<code class="sig-name descname">force_save</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzureActivityLog.force_save" title="Permalink to this definition">¶</a></dt>
<dd><p>Forces this resource to save, even if errors are present</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationAzureActivityLog.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzureActivityLog.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The human-readable name of this integration</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationAzureActivityLog.service">
<code class="sig-name descname">service</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzureActivityLog.service" title="Permalink to this definition">¶</a></dt>
<dd><p>A value denoting which cloud service this service integrates with</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationAzureActivityLog.service_refresh_rate_in_minutes">
<code class="sig-name descname">service_refresh_rate_in_minutes</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzureActivityLog.service_refresh_rate_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>How often, in minutes, to refresh the service</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationAzureActivityLog.tenant">
<code class="sig-name descname">tenant</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzureActivityLog.tenant" title="Permalink to this definition">¶</a></dt>
<dd><p>Tenant Id for an Azure service account within your project</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAzureActivityLog.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">category_filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_secret</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzureActivityLog.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CloudIntegrationAzureActivityLog resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>category_filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Azure services (such as Microsoft.Compute/virtualMachines) from which to pull metrics</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client id for an azure service account within your project</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client secret for an Azure service account within your project</p></li>
<li><p><strong>force_save</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Forces this resource to save, even if errors are present</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable name of this integration</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value denoting which cloud service this service integrates with</p></li>
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
<li><p><strong>tenant</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Tenant Id for an Azure service account within your project</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAzureActivityLog.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzureActivityLog.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.CloudIntegrationAzureActivityLog.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzureActivityLog.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.CloudIntegrationCloudTrail">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">CloudIntegrationCloudTrail</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bucket_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">external_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter_rule</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudTrail" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Wavefront Cloud Integration for CloudTrail. This allows CloudTrail cloud integrations to be created,
updated, and deleted.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_wavefront</span> <span class="k">as</span> <span class="nn">wavefront</span>

<span class="n">ext_id</span> <span class="o">=</span> <span class="n">wavefront</span><span class="o">.</span><span class="n">CloudIntegrationAwsExternalId</span><span class="p">(</span><span class="s2">&quot;extId&quot;</span><span class="p">)</span>
<span class="n">cloudtrail</span> <span class="o">=</span> <span class="n">wavefront</span><span class="o">.</span><span class="n">CloudIntegrationCloudTrail</span><span class="p">(</span><span class="s2">&quot;cloudtrail&quot;</span><span class="p">,</span>
    <span class="n">role_arn</span><span class="o">=</span><span class="s2">&quot;arn:aws::1234567:role/example-arn&quot;</span><span class="p">,</span>
    <span class="n">external_id</span><span class="o">=</span><span class="n">ext_id</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">region</span><span class="o">=</span><span class="s2">&quot;us-west-2&quot;</span><span class="p">,</span>
    <span class="n">bucket_name</span><span class="o">=</span><span class="s2">&quot;example-s3-bucket&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>bucket_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the S3 bucket where CloudTrail logs are stored</p></li>
<li><p><strong>external_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Role ARN that the customer has created in AWS IAM to allow access to Wavefront</p></li>
<li><p><strong>filter_rule</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Rule to filter CloudTrail log event</p></li>
<li><p><strong>force_save</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Forces this resource to save, even if errors are present</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable name of this integration</p></li>
<li><p><strong>prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The common prefix, if any, appended to all CloudTrail log files.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS region of the S3 bucket where CloudTrail logs are stored</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The external id corresponding to the Role ARN</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value denoting which cloud service this service integrates with</p></li>
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationCloudTrail.additional_tags">
<code class="sig-name descname">additional_tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudTrail.additional_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of point tag key-values to add to every point ingested using this integration</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationCloudTrail.bucket_name">
<code class="sig-name descname">bucket_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudTrail.bucket_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the S3 bucket where CloudTrail logs are stored</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationCloudTrail.external_id">
<code class="sig-name descname">external_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudTrail.external_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Role ARN that the customer has created in AWS IAM to allow access to Wavefront</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationCloudTrail.filter_rule">
<code class="sig-name descname">filter_rule</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudTrail.filter_rule" title="Permalink to this definition">¶</a></dt>
<dd><p>Rule to filter CloudTrail log event</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationCloudTrail.force_save">
<code class="sig-name descname">force_save</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudTrail.force_save" title="Permalink to this definition">¶</a></dt>
<dd><p>Forces this resource to save, even if errors are present</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationCloudTrail.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudTrail.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The human-readable name of this integration</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationCloudTrail.prefix">
<code class="sig-name descname">prefix</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudTrail.prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The common prefix, if any, appended to all CloudTrail log files.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationCloudTrail.region">
<code class="sig-name descname">region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudTrail.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS region of the S3 bucket where CloudTrail logs are stored</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationCloudTrail.role_arn">
<code class="sig-name descname">role_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudTrail.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The external id corresponding to the Role ARN</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationCloudTrail.service">
<code class="sig-name descname">service</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudTrail.service" title="Permalink to this definition">¶</a></dt>
<dd><p>A value denoting which cloud service this service integrates with</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationCloudTrail.service_refresh_rate_in_minutes">
<code class="sig-name descname">service_refresh_rate_in_minutes</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudTrail.service_refresh_rate_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>How often, in minutes, to refresh the service</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationCloudTrail.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bucket_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">external_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter_rule</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">prefix</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudTrail.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CloudIntegrationCloudTrail resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>bucket_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the S3 bucket where CloudTrail logs are stored</p></li>
<li><p><strong>external_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Role ARN that the customer has created in AWS IAM to allow access to Wavefront</p></li>
<li><p><strong>filter_rule</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Rule to filter CloudTrail log event</p></li>
<li><p><strong>force_save</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Forces this resource to save, even if errors are present</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable name of this integration</p></li>
<li><p><strong>prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The common prefix, if any, appended to all CloudTrail log files.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS region of the S3 bucket where CloudTrail logs are stored</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The external id corresponding to the Role ARN</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value denoting which cloud service this service integrates with</p></li>
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationCloudTrail.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudTrail.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.CloudIntegrationCloudTrail.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudTrail.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.CloudIntegrationCloudWatch">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">CloudIntegrationCloudWatch</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">external_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_selection_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_filter_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespaces</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">point_tag_filter_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">volume_selection_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudWatch" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Wavefront Cloud Integration for CloudTrail. This allows CloudTrail cloud integrations to be created,
updated, and delete</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_wavefront</span> <span class="k">as</span> <span class="nn">wavefront</span>

<span class="n">ext_id</span> <span class="o">=</span> <span class="n">wavefront</span><span class="o">.</span><span class="n">CloudIntegrationAwsExternalId</span><span class="p">(</span><span class="s2">&quot;extId&quot;</span><span class="p">)</span>
<span class="n">cloudwatch</span> <span class="o">=</span> <span class="n">wavefront</span><span class="o">.</span><span class="n">CloudIntegrationCloudWatch</span><span class="p">(</span><span class="s2">&quot;cloudwatch&quot;</span><span class="p">,</span>
    <span class="n">force_save</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">role_arn</span><span class="o">=</span><span class="s2">&quot;arn:aws::1234567:role/example-arn&quot;</span><span class="p">,</span>
    <span class="n">external_id</span><span class="o">=</span><span class="n">ext_id</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>external_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Role ARN that the customer has created in AWS IAM to allow access to Wavefront</p></li>
<li><p><strong>force_save</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Forces this resource to save, even if errors are present</p></li>
<li><p><strong>instance_selection_tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A string-&gt;string map whitelist of instance tag-value pairs (in AWS).
If the instance’s AWS tags match this whitelist, CloudWatch data about this instance is ingested.
Multiple entries are OR’ed</p></li>
<li><p><strong>metric_filter_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A regular expression that a CloudWatch metric name must match (case-insensitively) in order to be ingested</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable name of this integration</p></li>
<li><p><strong>namespaces</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of namespaces that limit what we query from CloudWatch</p></li>
<li><p><strong>point_tag_filter_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A regular expression that AWS tag key name must match (case-insensitively)
in order to be ingested</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The external id corresponding to the Role ARN</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value denoting which cloud service this service integrates with</p></li>
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
<li><p><strong>volume_selection_tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A string-&gt;string map of whitelist of volume tag-value pairs (in AWS).
If the volume’s AWS tags match this whitelist, CloudWatch data about this volume is ingested.
Multiple entries are OR’ed</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationCloudWatch.additional_tags">
<code class="sig-name descname">additional_tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudWatch.additional_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of point tag key-values to add to every point ingested using this integration</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationCloudWatch.external_id">
<code class="sig-name descname">external_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudWatch.external_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Role ARN that the customer has created in AWS IAM to allow access to Wavefront</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationCloudWatch.force_save">
<code class="sig-name descname">force_save</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudWatch.force_save" title="Permalink to this definition">¶</a></dt>
<dd><p>Forces this resource to save, even if errors are present</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationCloudWatch.instance_selection_tags">
<code class="sig-name descname">instance_selection_tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudWatch.instance_selection_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A string-&gt;string map whitelist of instance tag-value pairs (in AWS).
If the instance’s AWS tags match this whitelist, CloudWatch data about this instance is ingested.
Multiple entries are OR’ed</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationCloudWatch.metric_filter_regex">
<code class="sig-name descname">metric_filter_regex</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudWatch.metric_filter_regex" title="Permalink to this definition">¶</a></dt>
<dd><p>A regular expression that a CloudWatch metric name must match (case-insensitively) in order to be ingested</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationCloudWatch.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudWatch.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The human-readable name of this integration</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationCloudWatch.namespaces">
<code class="sig-name descname">namespaces</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudWatch.namespaces" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of namespaces that limit what we query from CloudWatch</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationCloudWatch.point_tag_filter_regex">
<code class="sig-name descname">point_tag_filter_regex</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudWatch.point_tag_filter_regex" title="Permalink to this definition">¶</a></dt>
<dd><p>A regular expression that AWS tag key name must match (case-insensitively)
in order to be ingested</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationCloudWatch.role_arn">
<code class="sig-name descname">role_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudWatch.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The external id corresponding to the Role ARN</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationCloudWatch.service">
<code class="sig-name descname">service</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudWatch.service" title="Permalink to this definition">¶</a></dt>
<dd><p>A value denoting which cloud service this service integrates with</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationCloudWatch.service_refresh_rate_in_minutes">
<code class="sig-name descname">service_refresh_rate_in_minutes</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudWatch.service_refresh_rate_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>How often, in minutes, to refresh the service</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationCloudWatch.volume_selection_tags">
<code class="sig-name descname">volume_selection_tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudWatch.volume_selection_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A string-&gt;string map of whitelist of volume tag-value pairs (in AWS).
If the volume’s AWS tags match this whitelist, CloudWatch data about this volume is ingested.
Multiple entries are OR’ed</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationCloudWatch.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">external_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_selection_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_filter_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespaces</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">point_tag_filter_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">volume_selection_tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudWatch.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CloudIntegrationCloudWatch resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>external_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Role ARN that the customer has created in AWS IAM to allow access to Wavefront</p></li>
<li><p><strong>force_save</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Forces this resource to save, even if errors are present</p></li>
<li><p><strong>instance_selection_tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A string-&gt;string map whitelist of instance tag-value pairs (in AWS).
If the instance’s AWS tags match this whitelist, CloudWatch data about this instance is ingested.
Multiple entries are OR’ed</p></li>
<li><p><strong>metric_filter_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A regular expression that a CloudWatch metric name must match (case-insensitively) in order to be ingested</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable name of this integration</p></li>
<li><p><strong>namespaces</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of namespaces that limit what we query from CloudWatch</p></li>
<li><p><strong>point_tag_filter_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A regular expression that AWS tag key name must match (case-insensitively)
in order to be ingested</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The external id corresponding to the Role ARN</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value denoting which cloud service this service integrates with</p></li>
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
<li><p><strong>volume_selection_tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A string-&gt;string map of whitelist of volume tag-value pairs (in AWS).
If the volume’s AWS tags match this whitelist, CloudWatch data about this volume is ingested.
Multiple entries are OR’ed</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationCloudWatch.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudWatch.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.CloudIntegrationCloudWatch.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudWatch.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.CloudIntegrationEc2">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">CloudIntegrationEc2</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">external_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationEc2" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Wavefront Cloud Integration for EC2. This allows EC2 cloud integrations to be created,
updated, and delete</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_wavefront</span> <span class="k">as</span> <span class="nn">wavefront</span>

<span class="n">ext_id</span> <span class="o">=</span> <span class="n">wavefront</span><span class="o">.</span><span class="n">CloudIntegrationAwsExternalId</span><span class="p">(</span><span class="s2">&quot;extId&quot;</span><span class="p">)</span>
<span class="n">ec2</span> <span class="o">=</span> <span class="n">wavefront</span><span class="o">.</span><span class="n">CloudIntegrationEc2</span><span class="p">(</span><span class="s2">&quot;ec2&quot;</span><span class="p">,</span>
    <span class="n">role_arn</span><span class="o">=</span><span class="s2">&quot;arn:aws::1234567:role/example-arn&quot;</span><span class="p">,</span>
    <span class="n">external_id</span><span class="o">=</span><span class="n">ext_id</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>external_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Role ARN that the customer has created in AWS IAM to allow access to Wavefront</p></li>
<li><p><strong>force_save</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Forces this resource to save, even if errors are present</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable name of this integration</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The external id corresponding to the Role ARN</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value denoting which cloud service this service integrates with</p></li>
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationEc2.additional_tags">
<code class="sig-name descname">additional_tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationEc2.additional_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of point tag key-values to add to every point ingested using this integration</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationEc2.external_id">
<code class="sig-name descname">external_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationEc2.external_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Role ARN that the customer has created in AWS IAM to allow access to Wavefront</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationEc2.force_save">
<code class="sig-name descname">force_save</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationEc2.force_save" title="Permalink to this definition">¶</a></dt>
<dd><p>Forces this resource to save, even if errors are present</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationEc2.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationEc2.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The human-readable name of this integration</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationEc2.role_arn">
<code class="sig-name descname">role_arn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationEc2.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The external id corresponding to the Role ARN</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationEc2.service">
<code class="sig-name descname">service</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationEc2.service" title="Permalink to this definition">¶</a></dt>
<dd><p>A value denoting which cloud service this service integrates with</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationEc2.service_refresh_rate_in_minutes">
<code class="sig-name descname">service_refresh_rate_in_minutes</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationEc2.service_refresh_rate_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>How often, in minutes, to refresh the service</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationEc2.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">external_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_arn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationEc2.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CloudIntegrationEc2 resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>external_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Role ARN that the customer has created in AWS IAM to allow access to Wavefront</p></li>
<li><p><strong>force_save</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Forces this resource to save, even if errors are present</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable name of this integration</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The external id corresponding to the Role ARN</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value denoting which cloud service this service integrates with</p></li>
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationEc2.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationEc2.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.CloudIntegrationEc2.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationEc2.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.CloudIntegrationGcp">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">CloudIntegrationGcp</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">categories</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">json_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_filter_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcp" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Wavefront Cloud Integration for GCP. This allows GCP cloud integrations to be created,
updated, and deleted.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_wavefront</span> <span class="k">as</span> <span class="nn">wavefront</span>

<span class="n">gcp</span> <span class="o">=</span> <span class="n">wavefront</span><span class="o">.</span><span class="n">CloudIntegrationGcp</span><span class="p">(</span><span class="s2">&quot;gcp&quot;</span><span class="p">,</span>
    <span class="n">json_key</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;{...your gcp key ...}</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;example-gcp-project&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>categories</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Google Cloud Platform (GCP) services.  Valid values are <code class="docutils literal notranslate"><span class="pre">APPENGINE</span></code>, 
<code class="docutils literal notranslate"><span class="pre">BIGQUERY</span></code>, <code class="docutils literal notranslate"><span class="pre">BIGTABLE</span></code>, <code class="docutils literal notranslate"><span class="pre">CLOUDFUNCTIONS</span></code>, <code class="docutils literal notranslate"><span class="pre">CLOUDIOT</span></code>, <code class="docutils literal notranslate"><span class="pre">CLOUDSQL</span></code>, <code class="docutils literal notranslate"><span class="pre">CLOUDTASKS</span></code>, <code class="docutils literal notranslate"><span class="pre">COMPUTE</span></code>, <code class="docutils literal notranslate"><span class="pre">CONTAINER</span></code>,
<code class="docutils literal notranslate"><span class="pre">DATAFLOW</span></code>, <code class="docutils literal notranslate"><span class="pre">DATAPROC</span></code>, <code class="docutils literal notranslate"><span class="pre">DATASTORE</span></code>, <code class="docutils literal notranslate"><span class="pre">FIREBASEDATABASE</span></code>, <code class="docutils literal notranslate"><span class="pre">FIREBASEHOSTING</span></code>, <code class="docutils literal notranslate"><span class="pre">FIRESTORE</span></code>, <code class="docutils literal notranslate"><span class="pre">INTERCONNECT</span></code>,
<code class="docutils literal notranslate"><span class="pre">LOADBALANCING</span></code>, <code class="docutils literal notranslate"><span class="pre">LOGGING</span></code>, <code class="docutils literal notranslate"><span class="pre">ML</span></code>, <code class="docutils literal notranslate"><span class="pre">MONITORING</span></code>, <code class="docutils literal notranslate"><span class="pre">PUBSUB</span></code>, <code class="docutils literal notranslate"><span class="pre">REDIS</span></code>, <code class="docutils literal notranslate"><span class="pre">ROUTER</span></code>, <code class="docutils literal notranslate"><span class="pre">SERVICERUNTIME</span></code>, <code class="docutils literal notranslate"><span class="pre">SPANNER</span></code>, <code class="docutils literal notranslate"><span class="pre">STORAGE</span></code>,
<code class="docutils literal notranslate"><span class="pre">TPU</span></code>, <code class="docutils literal notranslate"><span class="pre">VPN</span></code></p></li>
<li><p><strong>force_save</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Forces this resource to save, even if errors are present</p></li>
<li><p><strong>json_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Private key for a Google Cloud Platform (GCP) service account within your project.
The account must be at least granted Monitoring Viewer permissions. This key must be in the JSON format generated by GCP.</p></li>
<li><p><strong>metric_filter_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A regular expression that a metric name must match (case-insensitively) in order to be ingested</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable name of this integration</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Google Cloud Platform (GCP) Project Id</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value denoting which cloud service this service integrates with</p></li>
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationGcp.additional_tags">
<code class="sig-name descname">additional_tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcp.additional_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of point tag key-values to add to every point ingested using this integration</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationGcp.categories">
<code class="sig-name descname">categories</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcp.categories" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Google Cloud Platform (GCP) services.  Valid values are <code class="docutils literal notranslate"><span class="pre">APPENGINE</span></code>, 
<code class="docutils literal notranslate"><span class="pre">BIGQUERY</span></code>, <code class="docutils literal notranslate"><span class="pre">BIGTABLE</span></code>, <code class="docutils literal notranslate"><span class="pre">CLOUDFUNCTIONS</span></code>, <code class="docutils literal notranslate"><span class="pre">CLOUDIOT</span></code>, <code class="docutils literal notranslate"><span class="pre">CLOUDSQL</span></code>, <code class="docutils literal notranslate"><span class="pre">CLOUDTASKS</span></code>, <code class="docutils literal notranslate"><span class="pre">COMPUTE</span></code>, <code class="docutils literal notranslate"><span class="pre">CONTAINER</span></code>,
<code class="docutils literal notranslate"><span class="pre">DATAFLOW</span></code>, <code class="docutils literal notranslate"><span class="pre">DATAPROC</span></code>, <code class="docutils literal notranslate"><span class="pre">DATASTORE</span></code>, <code class="docutils literal notranslate"><span class="pre">FIREBASEDATABASE</span></code>, <code class="docutils literal notranslate"><span class="pre">FIREBASEHOSTING</span></code>, <code class="docutils literal notranslate"><span class="pre">FIRESTORE</span></code>, <code class="docutils literal notranslate"><span class="pre">INTERCONNECT</span></code>,
<code class="docutils literal notranslate"><span class="pre">LOADBALANCING</span></code>, <code class="docutils literal notranslate"><span class="pre">LOGGING</span></code>, <code class="docutils literal notranslate"><span class="pre">ML</span></code>, <code class="docutils literal notranslate"><span class="pre">MONITORING</span></code>, <code class="docutils literal notranslate"><span class="pre">PUBSUB</span></code>, <code class="docutils literal notranslate"><span class="pre">REDIS</span></code>, <code class="docutils literal notranslate"><span class="pre">ROUTER</span></code>, <code class="docutils literal notranslate"><span class="pre">SERVICERUNTIME</span></code>, <code class="docutils literal notranslate"><span class="pre">SPANNER</span></code>, <code class="docutils literal notranslate"><span class="pre">STORAGE</span></code>,
<code class="docutils literal notranslate"><span class="pre">TPU</span></code>, <code class="docutils literal notranslate"><span class="pre">VPN</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationGcp.force_save">
<code class="sig-name descname">force_save</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcp.force_save" title="Permalink to this definition">¶</a></dt>
<dd><p>Forces this resource to save, even if errors are present</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationGcp.json_key">
<code class="sig-name descname">json_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcp.json_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Private key for a Google Cloud Platform (GCP) service account within your project.
The account must be at least granted Monitoring Viewer permissions. This key must be in the JSON format generated by GCP.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationGcp.metric_filter_regex">
<code class="sig-name descname">metric_filter_regex</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcp.metric_filter_regex" title="Permalink to this definition">¶</a></dt>
<dd><p>A regular expression that a metric name must match (case-insensitively) in order to be ingested</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationGcp.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcp.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The human-readable name of this integration</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationGcp.project_id">
<code class="sig-name descname">project_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcp.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Google Cloud Platform (GCP) Project Id</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationGcp.service">
<code class="sig-name descname">service</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcp.service" title="Permalink to this definition">¶</a></dt>
<dd><p>A value denoting which cloud service this service integrates with</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationGcp.service_refresh_rate_in_minutes">
<code class="sig-name descname">service_refresh_rate_in_minutes</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcp.service_refresh_rate_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>How often, in minutes, to refresh the service</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationGcp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">categories</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">json_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_filter_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CloudIntegrationGcp resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>categories</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Google Cloud Platform (GCP) services.  Valid values are <code class="docutils literal notranslate"><span class="pre">APPENGINE</span></code>, 
<code class="docutils literal notranslate"><span class="pre">BIGQUERY</span></code>, <code class="docutils literal notranslate"><span class="pre">BIGTABLE</span></code>, <code class="docutils literal notranslate"><span class="pre">CLOUDFUNCTIONS</span></code>, <code class="docutils literal notranslate"><span class="pre">CLOUDIOT</span></code>, <code class="docutils literal notranslate"><span class="pre">CLOUDSQL</span></code>, <code class="docutils literal notranslate"><span class="pre">CLOUDTASKS</span></code>, <code class="docutils literal notranslate"><span class="pre">COMPUTE</span></code>, <code class="docutils literal notranslate"><span class="pre">CONTAINER</span></code>,
<code class="docutils literal notranslate"><span class="pre">DATAFLOW</span></code>, <code class="docutils literal notranslate"><span class="pre">DATAPROC</span></code>, <code class="docutils literal notranslate"><span class="pre">DATASTORE</span></code>, <code class="docutils literal notranslate"><span class="pre">FIREBASEDATABASE</span></code>, <code class="docutils literal notranslate"><span class="pre">FIREBASEHOSTING</span></code>, <code class="docutils literal notranslate"><span class="pre">FIRESTORE</span></code>, <code class="docutils literal notranslate"><span class="pre">INTERCONNECT</span></code>,
<code class="docutils literal notranslate"><span class="pre">LOADBALANCING</span></code>, <code class="docutils literal notranslate"><span class="pre">LOGGING</span></code>, <code class="docutils literal notranslate"><span class="pre">ML</span></code>, <code class="docutils literal notranslate"><span class="pre">MONITORING</span></code>, <code class="docutils literal notranslate"><span class="pre">PUBSUB</span></code>, <code class="docutils literal notranslate"><span class="pre">REDIS</span></code>, <code class="docutils literal notranslate"><span class="pre">ROUTER</span></code>, <code class="docutils literal notranslate"><span class="pre">SERVICERUNTIME</span></code>, <code class="docutils literal notranslate"><span class="pre">SPANNER</span></code>, <code class="docutils literal notranslate"><span class="pre">STORAGE</span></code>,
<code class="docutils literal notranslate"><span class="pre">TPU</span></code>, <code class="docutils literal notranslate"><span class="pre">VPN</span></code></p></li>
<li><p><strong>force_save</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Forces this resource to save, even if errors are present</p></li>
<li><p><strong>json_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Private key for a Google Cloud Platform (GCP) service account within your project.
The account must be at least granted Monitoring Viewer permissions. This key must be in the JSON format generated by GCP.</p></li>
<li><p><strong>metric_filter_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A regular expression that a metric name must match (case-insensitively) in order to be ingested</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable name of this integration</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Google Cloud Platform (GCP) Project Id</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value denoting which cloud service this service integrates with</p></li>
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationGcp.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.CloudIntegrationGcp.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.CloudIntegrationGcpBilling">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">CloudIntegrationGcpBilling</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">json_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcpBilling" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Wavefront Cloud Integration for GCP Billing. This allows GCP Billing cloud integrations to be created,
updated, and deleted.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_wavefront</span> <span class="k">as</span> <span class="nn">wavefront</span>

<span class="n">gcp_billing</span> <span class="o">=</span> <span class="n">wavefront</span><span class="o">.</span><span class="n">CloudIntegrationGcpBilling</span><span class="p">(</span><span class="s2">&quot;gcpBilling&quot;</span><span class="p">,</span>
    <span class="n">api_key</span><span class="o">=</span><span class="s2">&quot;example-api-key&quot;</span><span class="p">,</span>
    <span class="n">json_key</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;{...your gcp key ...}</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;example-gcp-project&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>api_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – API key for Google Cloud Platform (GCP)</p></li>
<li><p><strong>force_save</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Forces this resource to save, even if errors are present</p></li>
<li><p><strong>json_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Private key for a Google Cloud Platform (GCP) service account within your project.
The account must be at least granted Monitoring Viewer permissions. This key must be in the JSON format generated by GCP.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable name of this integration</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Google Cloud Platform (GCP) Project Id</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value denoting which cloud service this service integrates with</p></li>
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationGcpBilling.additional_tags">
<code class="sig-name descname">additional_tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcpBilling.additional_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of point tag key-values to add to every point ingested using this integration</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationGcpBilling.api_key">
<code class="sig-name descname">api_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcpBilling.api_key" title="Permalink to this definition">¶</a></dt>
<dd><p>API key for Google Cloud Platform (GCP)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationGcpBilling.force_save">
<code class="sig-name descname">force_save</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcpBilling.force_save" title="Permalink to this definition">¶</a></dt>
<dd><p>Forces this resource to save, even if errors are present</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationGcpBilling.json_key">
<code class="sig-name descname">json_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcpBilling.json_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Private key for a Google Cloud Platform (GCP) service account within your project.
The account must be at least granted Monitoring Viewer permissions. This key must be in the JSON format generated by GCP.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationGcpBilling.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcpBilling.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The human-readable name of this integration</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationGcpBilling.project_id">
<code class="sig-name descname">project_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcpBilling.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Google Cloud Platform (GCP) Project Id</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationGcpBilling.service">
<code class="sig-name descname">service</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcpBilling.service" title="Permalink to this definition">¶</a></dt>
<dd><p>A value denoting which cloud service this service integrates with</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationGcpBilling.service_refresh_rate_in_minutes">
<code class="sig-name descname">service_refresh_rate_in_minutes</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcpBilling.service_refresh_rate_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>How often, in minutes, to refresh the service</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationGcpBilling.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">json_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcpBilling.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CloudIntegrationGcpBilling resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>api_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – API key for Google Cloud Platform (GCP)</p></li>
<li><p><strong>force_save</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Forces this resource to save, even if errors are present</p></li>
<li><p><strong>json_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Private key for a Google Cloud Platform (GCP) service account within your project.
The account must be at least granted Monitoring Viewer permissions. This key must be in the JSON format generated by GCP.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable name of this integration</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Google Cloud Platform (GCP) Project Id</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value denoting which cloud service this service integrates with</p></li>
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationGcpBilling.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcpBilling.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.CloudIntegrationGcpBilling.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcpBilling.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.CloudIntegrationNewRelic">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">CloudIntegrationNewRelic</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_filter_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host_filter_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationNewRelic" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Wavefront Cloud Integration for NewRelic. This allows NewRelic cloud integrations to be created,
updated, and deleted.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_wavefront</span> <span class="k">as</span> <span class="nn">wavefront</span>

<span class="n">newrelic</span> <span class="o">=</span> <span class="n">wavefront</span><span class="o">.</span><span class="n">CloudIntegrationNewRelic</span><span class="p">(</span><span class="s2">&quot;newrelic&quot;</span><span class="p">,</span> <span class="n">api_key</span><span class="o">=</span><span class="s2">&quot;example-api-key&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>api_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – NewRelic REST api key</p></li>
<li><p><strong>app_filter_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A regular expression that an application name must match (case-insensitively) iun order to collect metrics</p></li>
<li><p><strong>force_save</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Forces this resource to save, even if errors are present</p></li>
<li><p><strong>host_filter_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A regular expression that a host name must match (case-insensitively) in order to collect metrics</p></li>
<li><p><strong>metric_filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – See Metric Filter</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable name of this integration</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value denoting which cloud service this service integrates with</p></li>
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
</ul>
</dd>
</dl>
<p>The <strong>metric_filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">appName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of a NewRelic App</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metric_filter_regex</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A regular expression that a metric name must match (case-insensitively) in order to be ingested</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationNewRelic.additional_tags">
<code class="sig-name descname">additional_tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationNewRelic.additional_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of point tag key-values to add to every point ingested using this integration</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationNewRelic.api_key">
<code class="sig-name descname">api_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationNewRelic.api_key" title="Permalink to this definition">¶</a></dt>
<dd><p>NewRelic REST api key</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationNewRelic.app_filter_regex">
<code class="sig-name descname">app_filter_regex</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationNewRelic.app_filter_regex" title="Permalink to this definition">¶</a></dt>
<dd><p>A regular expression that an application name must match (case-insensitively) iun order to collect metrics</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationNewRelic.force_save">
<code class="sig-name descname">force_save</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationNewRelic.force_save" title="Permalink to this definition">¶</a></dt>
<dd><p>Forces this resource to save, even if errors are present</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationNewRelic.host_filter_regex">
<code class="sig-name descname">host_filter_regex</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationNewRelic.host_filter_regex" title="Permalink to this definition">¶</a></dt>
<dd><p>A regular expression that a host name must match (case-insensitively) in order to collect metrics</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationNewRelic.metric_filters">
<code class="sig-name descname">metric_filters</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationNewRelic.metric_filters" title="Permalink to this definition">¶</a></dt>
<dd><p>See Metric Filter</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">appName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of a NewRelic App</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metric_filter_regex</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A regular expression that a metric name must match (case-insensitively) in order to be ingested</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationNewRelic.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationNewRelic.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The human-readable name of this integration</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationNewRelic.service">
<code class="sig-name descname">service</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationNewRelic.service" title="Permalink to this definition">¶</a></dt>
<dd><p>A value denoting which cloud service this service integrates with</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationNewRelic.service_refresh_rate_in_minutes">
<code class="sig-name descname">service_refresh_rate_in_minutes</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationNewRelic.service_refresh_rate_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>How often, in minutes, to refresh the service</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationNewRelic.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_filter_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host_filter_regex</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationNewRelic.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CloudIntegrationNewRelic resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>api_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – NewRelic REST api key</p></li>
<li><p><strong>app_filter_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A regular expression that an application name must match (case-insensitively) iun order to collect metrics</p></li>
<li><p><strong>force_save</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Forces this resource to save, even if errors are present</p></li>
<li><p><strong>host_filter_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A regular expression that a host name must match (case-insensitively) in order to collect metrics</p></li>
<li><p><strong>metric_filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – See Metric Filter</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable name of this integration</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value denoting which cloud service this service integrates with</p></li>
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
</ul>
</dd>
</dl>
<p>The <strong>metric_filters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">appName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of a NewRelic App</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">metric_filter_regex</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A regular expression that a metric name must match (case-insensitively) in order to be ingested</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationNewRelic.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationNewRelic.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.CloudIntegrationNewRelic.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationNewRelic.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.CloudIntegrationTesla">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">CloudIntegrationTesla</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationTesla" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Wavefront Cloud Integration for Tesla. This allows NewRelic cloud integrations to be created,
updated, and deleted.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_wavefront</span> <span class="k">as</span> <span class="nn">wavefront</span>

<span class="n">tesla</span> <span class="o">=</span> <span class="n">wavefront</span><span class="o">.</span><span class="n">CloudIntegrationTesla</span><span class="p">(</span><span class="s2">&quot;tesla&quot;</span><span class="p">,</span>
    <span class="n">email</span><span class="o">=</span><span class="s2">&quot;email@example.com&quot;</span><span class="p">,</span>
    <span class="n">password</span><span class="o">=</span><span class="s2">&quot;password&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Email address for the Tesla account login</p></li>
<li><p><strong>force_save</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Forces this resource to save, even if errors are present</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable name of this integration</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password for the Tesla account login</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value denoting which cloud service this service integrates with</p></li>
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationTesla.additional_tags">
<code class="sig-name descname">additional_tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationTesla.additional_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of point tag key-values to add to every point ingested using this integration</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationTesla.email">
<code class="sig-name descname">email</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationTesla.email" title="Permalink to this definition">¶</a></dt>
<dd><p>Email address for the Tesla account login</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationTesla.force_save">
<code class="sig-name descname">force_save</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationTesla.force_save" title="Permalink to this definition">¶</a></dt>
<dd><p>Forces this resource to save, even if errors are present</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationTesla.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationTesla.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The human-readable name of this integration</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationTesla.password">
<code class="sig-name descname">password</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationTesla.password" title="Permalink to this definition">¶</a></dt>
<dd><p>Password for the Tesla account login</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationTesla.service">
<code class="sig-name descname">service</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationTesla.service" title="Permalink to this definition">¶</a></dt>
<dd><p>A value denoting which cloud service this service integrates with</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.CloudIntegrationTesla.service_refresh_rate_in_minutes">
<code class="sig-name descname">service_refresh_rate_in_minutes</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationTesla.service_refresh_rate_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>How often, in minutes, to refresh the service</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationTesla.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationTesla.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CloudIntegrationTesla resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Email address for the Tesla account login</p></li>
<li><p><strong>force_save</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Forces this resource to save, even if errors are present</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable name of this integration</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password for the Tesla account login</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value denoting which cloud service this service integrates with</p></li>
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationTesla.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationTesla.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.CloudIntegrationTesla.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationTesla.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.Dashboard">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">Dashboard</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">can_modifies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">can_views</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_query_parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_section_table_of_contents</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">event_filter_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameter_details</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sections</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.Dashboard" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Wavefront Dashboard resource.  This allows dashboards to be created, updated, and deleted.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_wavefront</span> <span class="k">as</span> <span class="nn">wavefront</span>

<span class="n">basic</span> <span class="o">=</span> <span class="n">wavefront</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;basic&quot;</span><span class="p">,</span>
    <span class="n">email</span><span class="o">=</span><span class="s2">&quot;test+tftesting@example.com&quot;</span><span class="p">,</span>
    <span class="n">groups</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;agent_management&quot;</span><span class="p">,</span>
        <span class="s2">&quot;alerts_management&quot;</span><span class="p">,</span>
    <span class="p">])</span>
<span class="n">test_dashboard</span> <span class="o">=</span> <span class="n">wavefront</span><span class="o">.</span><span class="n">Dashboard</span><span class="p">(</span><span class="s2">&quot;testDashboard&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;testing, testing&quot;</span><span class="p">,</span>
    <span class="n">url</span><span class="o">=</span><span class="s2">&quot;tftestcreate&quot;</span><span class="p">,</span>
    <span class="n">display_section_table_of_contents</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">display_query_parameters</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">can_views</span><span class="o">=</span><span class="p">[</span><span class="n">basic</span><span class="o">.</span><span class="n">id</span><span class="p">],</span>
    <span class="n">sections</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;section 1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;rows&quot;</span><span class="p">:</span> <span class="p">[{</span>
            <span class="s2">&quot;charts&quot;</span><span class="p">:</span> <span class="p">[{</span>
                <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;chart 1&quot;</span><span class="p">,</span>
                <span class="s2">&quot;description&quot;</span><span class="p">:</span> <span class="s2">&quot;chart number 1&quot;</span><span class="p">,</span>
                <span class="s2">&quot;units&quot;</span><span class="p">:</span> <span class="s2">&quot;something per unit&quot;</span><span class="p">,</span>
                <span class="s2">&quot;sources&quot;</span><span class="p">:</span> <span class="p">[{</span>
                    <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;source name&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;query&quot;</span><span class="p">:</span> <span class="s2">&quot;ts()&quot;</span><span class="p">,</span>
                <span class="p">}],</span>
                <span class="s2">&quot;chartSetting&quot;</span><span class="p">:</span> <span class="p">{</span>
                    <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;linear&quot;</span><span class="p">,</span>
                <span class="p">},</span>
                <span class="s2">&quot;summarization&quot;</span><span class="p">:</span> <span class="s2">&quot;MEAN&quot;</span><span class="p">,</span>
            <span class="p">}],</span>
        <span class="p">}],</span>
    <span class="p">}],</span>
    <span class="n">parameter_details</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;param1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;label&quot;</span><span class="p">:</span> <span class="s2">&quot;param1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;defaultValue&quot;</span><span class="p">:</span> <span class="s2">&quot;Label&quot;</span><span class="p">,</span>
        <span class="s2">&quot;hideFromView&quot;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
        <span class="s2">&quot;parameterType&quot;</span><span class="p">:</span> <span class="s2">&quot;SIMPLE&quot;</span><span class="p">,</span>
        <span class="s2">&quot;valuesToReadableStrings&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;Label&quot;</span><span class="p">:</span> <span class="s2">&quot;test&quot;</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">}],</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;b&quot;</span><span class="p">,</span>
        <span class="s2">&quot;terraform&quot;</span><span class="p">,</span>
        <span class="s2">&quot;a&quot;</span><span class="p">,</span>
        <span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>can_modifies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of users that have modify ACL access to the dashboard</p></li>
<li><p><strong>can_views</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of users that have view ACL access to the dashboard</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description of the dashboard</p></li>
<li><p><strong>display_query_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the dashboard parameters section is opened by default when the dashboard
is shown</p></li>
<li><p><strong>display_section_table_of_contents</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the “pills” quick-linked the sections of the dashboard are 
displayed by default when the dashboard is shown</p></li>
<li><p><strong>event_filter_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – How charts belonging to this dashboard should display events. BYCHART is default if 
unspecified; Valid options are: <code class="docutils literal notranslate"><span class="pre">BYCHART</span></code>, <code class="docutils literal notranslate"><span class="pre">AUTOMATIC</span></code>, <code class="docutils literal notranslate"><span class="pre">ALL</span></code>, <code class="docutils literal notranslate"><span class="pre">NONE</span></code>, <code class="docutils literal notranslate"><span class="pre">BYDASHBOARD</span></code>, and <code class="docutils literal notranslate"><span class="pre">BYCHARTANDDASHBOARD</span></code></p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the dashboard</p></li>
<li><p><strong>parameter_details</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The current JSON representation of dashboard parameters. See parameter details</p></li>
<li><p><strong>sections</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Dashboard chart sections. See dashboard sections</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of tags to assign to this resource.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier, also URL slug, of the dashboard</p></li>
</ul>
</dd>
</dl>
<p>The <strong>parameter_details</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">defaultValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The default value of the parameter</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dynamicFieldType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For <code class="docutils literal notranslate"><span class="pre">DYNAMIC</span></code> parameter types, the type of the field. Valid options are <code class="docutils literal notranslate"><span class="pre">SOURCE</span></code>,
<code class="docutils literal notranslate"><span class="pre">SOURCE_TAG</span></code>, <code class="docutils literal notranslate"><span class="pre">METRIC_NAME</span></code>, <code class="docutils literal notranslate"><span class="pre">TAG_KEY</span></code>, <code class="docutils literal notranslate"><span class="pre">MATCHING_SOURCE_TAG</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hideFromView</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If <code class="docutils literal notranslate"><span class="pre">true</span></code> the parameter will only be shown on the edit view of the dashboard</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The label for the parameter</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the parameters</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameterType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of the parameter. <code class="docutils literal notranslate"><span class="pre">SIMPLE</span></code>, <code class="docutils literal notranslate"><span class="pre">LIST</span></code>, or <code class="docutils literal notranslate"><span class="pre">DYNAMIC</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For <code class="docutils literal notranslate"><span class="pre">DYNAMIC</span></code> parameter types, the query to execute to return values</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tagKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - for <code class="docutils literal notranslate"><span class="pre">TAG_KEY</span></code> dynamic field types, the tag key to return</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">valuesToReadableStrings</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A string-&gt;string map.  At least one of the keys must match the value of
<code class="docutils literal notranslate"><span class="pre">default_value</span></code></p></li>
</ul>
<p>The <strong>sections</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of this section</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rows</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - See dashboard section rows</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">charts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Charts in this section. See dashboard chart</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">chartSetting</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Chart settings. See chart settings</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">autoColumnTags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - deprecated</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">columnTags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - deprecated</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customTags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - For the tabular view, a list of point tags to display when using the <code class="docutils literal notranslate"><span class="pre">custom</span></code> tag display mode</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expectedDataSpacing</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Threshold (in seconds) for time delta between consecutive points in a series
above which a dotted line will replace a solid in in line plots. Default 60</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedLegendDisplayStats</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - For a chart with a fixed legend, a list of statistics to display in the legend</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedLegendEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to enable a fixed tabular legend adjacent to the chart</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedLegendFilterField</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Statistic to use for determining whether a series is displayed on the fixed legend.
Valid options are <code class="docutils literal notranslate"><span class="pre">CURRENT</span></code>, <code class="docutils literal notranslate"><span class="pre">MEAN</span></code>, <code class="docutils literal notranslate"><span class="pre">MEDIAN</span></code>, <code class="docutils literal notranslate"><span class="pre">SUM</span></code>, <code class="docutils literal notranslate"><span class="pre">MIN</span></code>, <code class="docutils literal notranslate"><span class="pre">MAX</span></code>, <code class="docutils literal notranslate"><span class="pre">COUNT</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedLegendFilterLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of series to include in the fixed legend</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedLegendFilterSort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether to display <code class="docutils literal notranslate"><span class="pre">TOP</span></code> or <code class="docutils literal notranslate"><span class="pre">BOTTOM</span></code> ranked series in a fixed legend. Valid options
are <code class="docutils literal notranslate"><span class="pre">TOP</span></code>, and <code class="docutils literal notranslate"><span class="pre">BOTTOM</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedLegendHideLabel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - deprecated</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedLegendPosition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where the fixed legend should be displayed with respect ot the chart.
Valid options are <code class="docutils literal notranslate"><span class="pre">RIGHt</span></code>, <code class="docutils literal notranslate"><span class="pre">TOP</span></code>, <code class="docutils literal notranslate"><span class="pre">LEFT</span></code>, <code class="docutils literal notranslate"><span class="pre">BOTTOM</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedLegendUseRawStats</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If <code class="docutils literal notranslate"><span class="pre">true</span></code>, the legend uses non-summarized stats instead of summarized</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupBySource</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - For the tabular view, whether to group multi metrics into a single row by a common source.
If <code class="docutils literal notranslate"><span class="pre">false</span></code>, each source is displayed in its own row.  if <code class="docutils literal notranslate"><span class="pre">true</span></code>, multiple metrics for the same host will be displayed as different
columns in the same row</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">invertDynamicLegendHoverControl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to disable the display of the floating legend (but
reenable it when the ctrl-key is pressed)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lineType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Plot interpolation type.  <code class="docutils literal notranslate"><span class="pre">linear</span></code> is default. Valid options are <code class="docutils literal notranslate"><span class="pre">linear</span></code>, <code class="docutils literal notranslate"><span class="pre">step-before</span></code>, 
<code class="docutils literal notranslate"><span class="pre">step-after</span></code>, <code class="docutils literal notranslate"><span class="pre">basis</span></code>, <code class="docutils literal notranslate"><span class="pre">cardinal</span></code>, <code class="docutils literal notranslate"><span class="pre">monotone</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Max value of the Y-axis. Set to null or leave blank for auto</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Min value of the Y-axis. Set to null or leave blank for auto</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numTags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - For the tabular view, how many point tags to display</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">plainMarkdownContent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The markdown content for a Markdown display, in plain text.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">showHosts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - For the tabular view, whether to display sources. Default is <code class="docutils literal notranslate"><span class="pre">true</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">showLabels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - For the tabular view, whether to display labels. Default is <code class="docutils literal notranslate"><span class="pre">true</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">showRawValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - For the tabular view, whether to display raw values. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sortValuesDescending</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - For the tabular view, whether to display display values in descending order. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineDecimalPrecision</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - For the single stat view, the decimal precision of the displayed number</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineDisplayColor</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For the single stat view, the color of the displayed text (when not dynamically determined). 
Values should be in <code class="docutils literal notranslate"><span class="pre">rgba(,,,,)</span></code> format</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineDisplayFontSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For the single stat view, the font size of the displayed text, in percent</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineDisplayHorizontalPosition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For the single stat view, the horizontal position of the displayed text.
Valid options are <code class="docutils literal notranslate"><span class="pre">MIDDLE</span></code>, <code class="docutils literal notranslate"><span class="pre">LEFT</span></code>, <code class="docutils literal notranslate"><span class="pre">RIGHT</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineDisplayPostfix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For the single stat view, a string to append to the displayed text</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineDisplayPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For the single stat view, a string to add before the displayed text</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineDisplayValueType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For the single stat view, where to display the name of the query or the value of the query.
Valid options are <code class="docutils literal notranslate"><span class="pre">VALUE</span></code> or <code class="docutils literal notranslate"><span class="pre">LABEL</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineDisplayVerticalPosition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - deprecated</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineFillColor</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For the single stat view, the color of the background fill.  Values should be
in <code class="docutils literal notranslate"><span class="pre">rgba(,,,,)</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineLineColor</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For the single stat view, the color of the line.  Values should be in <code class="docutils literal notranslate"><span class="pre">rgba(,,,,)</span></code> format</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For the single stat view, This determines whether the sparkline of the statistic is displayed in the chart <code class="docutils literal notranslate"><span class="pre">BACKGROUND</span></code>, <code class="docutils literal notranslate"><span class="pre">BOTTOM</span></code>, or <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.
Valid options are <code class="docutils literal notranslate"><span class="pre">BACKGROUND</span></code>, <code class="docutils literal notranslate"><span class="pre">BOTTOM</span></code>, <code class="docutils literal notranslate"><span class="pre">NONE</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineValueColorMapApplyTo</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For the single stat view, whether to apply dyunamic color settings to 
the displayed <code class="docutils literal notranslate"><span class="pre">TEXT</span></code> or <code class="docutils literal notranslate"><span class="pre">BACKGROUND</span></code>. Valid options are <code class="docutils literal notranslate"><span class="pre">TEXT</span></code> or <code class="docutils literal notranslate"><span class="pre">BACKGROUND</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineValueColorMapColors</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - For the single stat view, A list of colors that differing query values map to. 
Must contain one more element than <code class="docutils literal notranslate"><span class="pre">sparkline_value_color_map_values_v2</span></code>. Values should be in <code class="docutils literal notranslate"><span class="pre">rgba(,,,,)</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineValueColorMapValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - deprecated</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineValueColorMapValuesV2s</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - For the single stat view, a list of boundaries for mapping different
query values to colors.  Must contain one less element than <code class="docutils literal notranslate"><span class="pre">sparkline_value_color_map_colors</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineValueTextMapTexts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - For the single stat view, a list of display text values that different query
values map to.  Must contain one more element than <code class="docutils literal notranslate"><span class="pre">sparkline_value_text_map_thresholds</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineValueTextMapThresholds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - For the single stat view, a list of threshold boundaries for 
mapping different query values to display text.  Must contain one less element than <code class="docutils literal notranslate"><span class="pre">sparkline_value_text_map_text</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stackType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Type of stacked chart (applicable only if chart type is <code class="docutils literal notranslate"><span class="pre">stacked</span></code>). <code class="docutils literal notranslate"><span class="pre">zero</span></code> (default) means
stacked from y=0. <code class="docutils literal notranslate"><span class="pre">expand</span></code> means normalized from 0 to 1.  <code class="docutils literal notranslate"><span class="pre">wiggle</span></code> means minimize weighted changes. <code class="docutils literal notranslate"><span class="pre">silhouette</span></code> means to
center the stream. Valid options are <code class="docutils literal notranslate"><span class="pre">zero</span></code>, <code class="docutils literal notranslate"><span class="pre">expand</span></code>, <code class="docutils literal notranslate"><span class="pre">wiggle</span></code>, <code class="docutils literal notranslate"><span class="pre">silhouette</span></code>, <code class="docutils literal notranslate"><span class="pre">bars</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tagMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For the tabular view, which mode to use to determine which point tags to display.
Valid options are <code class="docutils literal notranslate"><span class="pre">all</span></code>, <code class="docutils literal notranslate"><span class="pre">top</span></code>, or <code class="docutils literal notranslate"><span class="pre">custom</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeBasedColoring</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - For x-y scatterplots, whether to color more recent points as darker than older points</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Chart Type. <code class="docutils literal notranslate"><span class="pre">line</span></code> refers to the Line Plot, <code class="docutils literal notranslate"><span class="pre">scatter</span></code> to the Point Plot, <code class="docutils literal notranslate"><span class="pre">stacked-area</span></code> to 
the Stacked Area plot, <code class="docutils literal notranslate"><span class="pre">table</span></code> to the Tabular View, <code class="docutils literal notranslate"><span class="pre">scatterploy-xy</span></code> to Scatter Plot, <code class="docutils literal notranslate"><span class="pre">markdown-widget</span></code> to the
Markdown display, and <code class="docutils literal notranslate"><span class="pre">sparkline</span></code> to the Single Stat view. Valid options are <code class="docutils literal notranslate"><span class="pre">line</span></code>, <code class="docutils literal notranslate"><span class="pre">scatterplot</span></code>,
<code class="docutils literal notranslate"><span class="pre">stacked-area</span></code>, <code class="docutils literal notranslate"><span class="pre">stacked-column</span></code>, <code class="docutils literal notranslate"><span class="pre">table</span></code>, <code class="docutils literal notranslate"><span class="pre">scatterplot-xy</span></code>, <code class="docutils literal notranslate"><span class="pre">markdown-widget</span></code>, <code class="docutils literal notranslate"><span class="pre">sparkline</span></code>, <code class="docutils literal notranslate"><span class="pre">globe</span></code>, <code class="docutils literal notranslate"><span class="pre">nodemap</span></code>,
<code class="docutils literal notranslate"><span class="pre">top-k</span></code>, <code class="docutils literal notranslate"><span class="pre">status-list</span></code>, <code class="docutils literal notranslate"><span class="pre">histogram</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">windowSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Width, in minutes, of the time window to use for <code class="docutils literal notranslate"><span class="pre">last</span></code> windowing</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">windowing</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For the tabular view, whether to use the full time window for the query or the last X minutes.
Valid options are <code class="docutils literal notranslate"><span class="pre">full</span></code> or <code class="docutils literal notranslate"><span class="pre">last</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">xmax</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - For x-y scatterplots, max value for the X-axis. Set to null for auto</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">xmin</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - For x-y scatterplots, min value for the X-axis. Set to null for auto</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">y0ScaleSiBy1024</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to scale numerical magnitude labels for left Y-axis by 1024 in the IEC/Binary manner (instead of by 1000 like SI)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">y0UnitAutoscaling</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to automatically adjust magnitude labels and units for the left Y-axis to favor smaller magnitudes and larger units</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">y1ScaleSiBy1024</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to scale numerical magnitude labels for right Y-axis by 1024 in the IEC/Binary manner (instead of by 1000 like SI)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">y1UnitAutoscaling</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to automatically adjust magnitude labels and units for the right Y-axis to favor smaller magnitudes and larger units</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">y1Units</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For plots with multiple Y-axes, units for right side Y-axis</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">y1max</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - For plots with multiple Y-axes, max value for the right side Y-axis. Set null for auto</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">y1min</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - For plots with multiple Y-axes, min value for the right side Y-axis. Set null for auto</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ymax</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - For x-y scatterplots, max value for the Y-axis. Set to null for auto</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ymin</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - For x-y scatterplots, min value for the Y-axis. Set to null for auto</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Description of the chart</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the source</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sources</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Query expression to plot on the chart. See chart source queries</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether the source is disabled</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the source</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">query</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Query expression to plot on the chart</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryBuilderEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether oir not this source line should have the query builder enabled</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scatterPlotSource</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For scatter plots, does this query source the X-axis or the Y-axis, <code class="docutils literal notranslate"><span class="pre">X</span></code>, or <code class="docutils literal notranslate"><span class="pre">Y</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceDescription</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A description for the purpose of this source</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">summarization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Summarization strategy for the chart. MEAN is default. Valid options are, <code class="docutils literal notranslate"><span class="pre">MEAN</span></code>, 
<code class="docutils literal notranslate"><span class="pre">MEDIAN</span></code>, <code class="docutils literal notranslate"><span class="pre">MIN</span></code>, <code class="docutils literal notranslate"><span class="pre">MAX</span></code>, <code class="docutils literal notranslate"><span class="pre">SUM</span></code>, <code class="docutils literal notranslate"><span class="pre">COUNT</span></code>, <code class="docutils literal notranslate"><span class="pre">LAST</span></code>, <code class="docutils literal notranslate"><span class="pre">FIRST</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">units</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String to label the units of the chart on the Y-Axis</p></li>
</ul>
</li>
</ul>
</li>
</ul>
<dl class="py attribute">
<dt id="pulumi_wavefront.Dashboard.can_modifies">
<code class="sig-name descname">can_modifies</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.Dashboard.can_modifies" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of users that have modify ACL access to the dashboard</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.Dashboard.can_views">
<code class="sig-name descname">can_views</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.Dashboard.can_views" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of users that have view ACL access to the dashboard</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.Dashboard.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.Dashboard.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Human-readable description of the dashboard</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.Dashboard.display_query_parameters">
<code class="sig-name descname">display_query_parameters</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.Dashboard.display_query_parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the dashboard parameters section is opened by default when the dashboard
is shown</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.Dashboard.display_section_table_of_contents">
<code class="sig-name descname">display_section_table_of_contents</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.Dashboard.display_section_table_of_contents" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the “pills” quick-linked the sections of the dashboard are 
displayed by default when the dashboard is shown</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.Dashboard.event_filter_type">
<code class="sig-name descname">event_filter_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.Dashboard.event_filter_type" title="Permalink to this definition">¶</a></dt>
<dd><p>How charts belonging to this dashboard should display events. BYCHART is default if 
unspecified; Valid options are: <code class="docutils literal notranslate"><span class="pre">BYCHART</span></code>, <code class="docutils literal notranslate"><span class="pre">AUTOMATIC</span></code>, <code class="docutils literal notranslate"><span class="pre">ALL</span></code>, <code class="docutils literal notranslate"><span class="pre">NONE</span></code>, <code class="docutils literal notranslate"><span class="pre">BYDASHBOARD</span></code>, and <code class="docutils literal notranslate"><span class="pre">BYCHARTANDDASHBOARD</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.Dashboard.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.Dashboard.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the dashboard</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.Dashboard.parameter_details">
<code class="sig-name descname">parameter_details</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.Dashboard.parameter_details" title="Permalink to this definition">¶</a></dt>
<dd><p>The current JSON representation of dashboard parameters. See parameter details</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">defaultValue</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The default value of the parameter</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dynamicFieldType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - For <code class="docutils literal notranslate"><span class="pre">DYNAMIC</span></code> parameter types, the type of the field. Valid options are <code class="docutils literal notranslate"><span class="pre">SOURCE</span></code>,
<code class="docutils literal notranslate"><span class="pre">SOURCE_TAG</span></code>, <code class="docutils literal notranslate"><span class="pre">METRIC_NAME</span></code>, <code class="docutils literal notranslate"><span class="pre">TAG_KEY</span></code>, <code class="docutils literal notranslate"><span class="pre">MATCHING_SOURCE_TAG</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hideFromView</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - If <code class="docutils literal notranslate"><span class="pre">true</span></code> the parameter will only be shown on the edit view of the dashboard</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The label for the parameter</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the parameters</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameterType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of the parameter. <code class="docutils literal notranslate"><span class="pre">SIMPLE</span></code>, <code class="docutils literal notranslate"><span class="pre">LIST</span></code>, or <code class="docutils literal notranslate"><span class="pre">DYNAMIC</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryValue</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - For <code class="docutils literal notranslate"><span class="pre">DYNAMIC</span></code> parameter types, the query to execute to return values</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tagKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - for <code class="docutils literal notranslate"><span class="pre">TAG_KEY</span></code> dynamic field types, the tag key to return</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">valuesToReadableStrings</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A string-&gt;string map.  At least one of the keys must match the value of
<code class="docutils literal notranslate"><span class="pre">default_value</span></code></p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.Dashboard.sections">
<code class="sig-name descname">sections</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.Dashboard.sections" title="Permalink to this definition">¶</a></dt>
<dd><p>Dashboard chart sections. See dashboard sections</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of this section</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rows</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - See dashboard section rows</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">charts</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Charts in this section. See dashboard chart</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">chartSetting</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Chart settings. See chart settings</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">autoColumnTags</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - deprecated</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">columnTags</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - deprecated</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customTags</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - For the tabular view, a list of point tags to display when using the <code class="docutils literal notranslate"><span class="pre">custom</span></code> tag display mode</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expectedDataSpacing</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Threshold (in seconds) for time delta between consecutive points in a series
above which a dotted line will replace a solid in in line plots. Default 60</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedLegendDisplayStats</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - For a chart with a fixed legend, a list of statistics to display in the legend</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedLegendEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to enable a fixed tabular legend adjacent to the chart</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedLegendFilterField</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Statistic to use for determining whether a series is displayed on the fixed legend.
Valid options are <code class="docutils literal notranslate"><span class="pre">CURRENT</span></code>, <code class="docutils literal notranslate"><span class="pre">MEAN</span></code>, <code class="docutils literal notranslate"><span class="pre">MEDIAN</span></code>, <code class="docutils literal notranslate"><span class="pre">SUM</span></code>, <code class="docutils literal notranslate"><span class="pre">MIN</span></code>, <code class="docutils literal notranslate"><span class="pre">MAX</span></code>, <code class="docutils literal notranslate"><span class="pre">COUNT</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedLegendFilterLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Number of series to include in the fixed legend</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedLegendFilterSort</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Whether to display <code class="docutils literal notranslate"><span class="pre">TOP</span></code> or <code class="docutils literal notranslate"><span class="pre">BOTTOM</span></code> ranked series in a fixed legend. Valid options
are <code class="docutils literal notranslate"><span class="pre">TOP</span></code>, and <code class="docutils literal notranslate"><span class="pre">BOTTOM</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedLegendHideLabel</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - deprecated</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedLegendPosition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Where the fixed legend should be displayed with respect ot the chart.
Valid options are <code class="docutils literal notranslate"><span class="pre">RIGHt</span></code>, <code class="docutils literal notranslate"><span class="pre">TOP</span></code>, <code class="docutils literal notranslate"><span class="pre">LEFT</span></code>, <code class="docutils literal notranslate"><span class="pre">BOTTOM</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedLegendUseRawStats</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - If <code class="docutils literal notranslate"><span class="pre">true</span></code>, the legend uses non-summarized stats instead of summarized</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupBySource</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - For the tabular view, whether to group multi metrics into a single row by a common source.
If <code class="docutils literal notranslate"><span class="pre">false</span></code>, each source is displayed in its own row.  if <code class="docutils literal notranslate"><span class="pre">true</span></code>, multiple metrics for the same host will be displayed as different
columns in the same row</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">invertDynamicLegendHoverControl</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to disable the display of the floating legend (but
reenable it when the ctrl-key is pressed)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lineType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Plot interpolation type.  <code class="docutils literal notranslate"><span class="pre">linear</span></code> is default. Valid options are <code class="docutils literal notranslate"><span class="pre">linear</span></code>, <code class="docutils literal notranslate"><span class="pre">step-before</span></code>, 
<code class="docutils literal notranslate"><span class="pre">step-after</span></code>, <code class="docutils literal notranslate"><span class="pre">basis</span></code>, <code class="docutils literal notranslate"><span class="pre">cardinal</span></code>, <code class="docutils literal notranslate"><span class="pre">monotone</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Max value of the Y-axis. Set to null or leave blank for auto</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Min value of the Y-axis. Set to null or leave blank for auto</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numTags</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - For the tabular view, how many point tags to display</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">plainMarkdownContent</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The markdown content for a Markdown display, in plain text.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">showHosts</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - For the tabular view, whether to display sources. Default is <code class="docutils literal notranslate"><span class="pre">true</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">showLabels</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - For the tabular view, whether to display labels. Default is <code class="docutils literal notranslate"><span class="pre">true</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">showRawValues</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - For the tabular view, whether to display raw values. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sortValuesDescending</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - For the tabular view, whether to display display values in descending order. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineDecimalPrecision</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - For the single stat view, the decimal precision of the displayed number</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineDisplayColor</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - For the single stat view, the color of the displayed text (when not dynamically determined). 
Values should be in <code class="docutils literal notranslate"><span class="pre">rgba(,,,,)</span></code> format</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineDisplayFontSize</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - For the single stat view, the font size of the displayed text, in percent</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineDisplayHorizontalPosition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - For the single stat view, the horizontal position of the displayed text.
Valid options are <code class="docutils literal notranslate"><span class="pre">MIDDLE</span></code>, <code class="docutils literal notranslate"><span class="pre">LEFT</span></code>, <code class="docutils literal notranslate"><span class="pre">RIGHT</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineDisplayPostfix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - For the single stat view, a string to append to the displayed text</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineDisplayPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - For the single stat view, a string to add before the displayed text</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineDisplayValueType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - For the single stat view, where to display the name of the query or the value of the query.
Valid options are <code class="docutils literal notranslate"><span class="pre">VALUE</span></code> or <code class="docutils literal notranslate"><span class="pre">LABEL</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineDisplayVerticalPosition</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - deprecated</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineFillColor</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - For the single stat view, the color of the background fill.  Values should be
in <code class="docutils literal notranslate"><span class="pre">rgba(,,,,)</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineLineColor</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - For the single stat view, the color of the line.  Values should be in <code class="docutils literal notranslate"><span class="pre">rgba(,,,,)</span></code> format</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineSize</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - For the single stat view, This determines whether the sparkline of the statistic is displayed in the chart <code class="docutils literal notranslate"><span class="pre">BACKGROUND</span></code>, <code class="docutils literal notranslate"><span class="pre">BOTTOM</span></code>, or <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.
Valid options are <code class="docutils literal notranslate"><span class="pre">BACKGROUND</span></code>, <code class="docutils literal notranslate"><span class="pre">BOTTOM</span></code>, <code class="docutils literal notranslate"><span class="pre">NONE</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineValueColorMapApplyTo</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - For the single stat view, whether to apply dyunamic color settings to 
the displayed <code class="docutils literal notranslate"><span class="pre">TEXT</span></code> or <code class="docutils literal notranslate"><span class="pre">BACKGROUND</span></code>. Valid options are <code class="docutils literal notranslate"><span class="pre">TEXT</span></code> or <code class="docutils literal notranslate"><span class="pre">BACKGROUND</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineValueColorMapColors</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - For the single stat view, A list of colors that differing query values map to. 
Must contain one more element than <code class="docutils literal notranslate"><span class="pre">sparkline_value_color_map_values_v2</span></code>. Values should be in <code class="docutils literal notranslate"><span class="pre">rgba(,,,,)</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineValueColorMapValues</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - deprecated</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineValueColorMapValuesV2s</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - For the single stat view, a list of boundaries for mapping different
query values to colors.  Must contain one less element than <code class="docutils literal notranslate"><span class="pre">sparkline_value_color_map_colors</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineValueTextMapTexts</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - For the single stat view, a list of display text values that different query
values map to.  Must contain one more element than <code class="docutils literal notranslate"><span class="pre">sparkline_value_text_map_thresholds</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineValueTextMapThresholds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - For the single stat view, a list of threshold boundaries for 
mapping different query values to display text.  Must contain one less element than <code class="docutils literal notranslate"><span class="pre">sparkline_value_text_map_text</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stackType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Type of stacked chart (applicable only if chart type is <code class="docutils literal notranslate"><span class="pre">stacked</span></code>). <code class="docutils literal notranslate"><span class="pre">zero</span></code> (default) means
stacked from y=0. <code class="docutils literal notranslate"><span class="pre">expand</span></code> means normalized from 0 to 1.  <code class="docutils literal notranslate"><span class="pre">wiggle</span></code> means minimize weighted changes. <code class="docutils literal notranslate"><span class="pre">silhouette</span></code> means to
center the stream. Valid options are <code class="docutils literal notranslate"><span class="pre">zero</span></code>, <code class="docutils literal notranslate"><span class="pre">expand</span></code>, <code class="docutils literal notranslate"><span class="pre">wiggle</span></code>, <code class="docutils literal notranslate"><span class="pre">silhouette</span></code>, <code class="docutils literal notranslate"><span class="pre">bars</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tagMode</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - For the tabular view, which mode to use to determine which point tags to display.
Valid options are <code class="docutils literal notranslate"><span class="pre">all</span></code>, <code class="docutils literal notranslate"><span class="pre">top</span></code>, or <code class="docutils literal notranslate"><span class="pre">custom</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeBasedColoring</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - For x-y scatterplots, whether to color more recent points as darker than older points</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Chart Type. <code class="docutils literal notranslate"><span class="pre">line</span></code> refers to the Line Plot, <code class="docutils literal notranslate"><span class="pre">scatter</span></code> to the Point Plot, <code class="docutils literal notranslate"><span class="pre">stacked-area</span></code> to 
the Stacked Area plot, <code class="docutils literal notranslate"><span class="pre">table</span></code> to the Tabular View, <code class="docutils literal notranslate"><span class="pre">scatterploy-xy</span></code> to Scatter Plot, <code class="docutils literal notranslate"><span class="pre">markdown-widget</span></code> to the
Markdown display, and <code class="docutils literal notranslate"><span class="pre">sparkline</span></code> to the Single Stat view. Valid options are <code class="docutils literal notranslate"><span class="pre">line</span></code>, <code class="docutils literal notranslate"><span class="pre">scatterplot</span></code>,
<code class="docutils literal notranslate"><span class="pre">stacked-area</span></code>, <code class="docutils literal notranslate"><span class="pre">stacked-column</span></code>, <code class="docutils literal notranslate"><span class="pre">table</span></code>, <code class="docutils literal notranslate"><span class="pre">scatterplot-xy</span></code>, <code class="docutils literal notranslate"><span class="pre">markdown-widget</span></code>, <code class="docutils literal notranslate"><span class="pre">sparkline</span></code>, <code class="docutils literal notranslate"><span class="pre">globe</span></code>, <code class="docutils literal notranslate"><span class="pre">nodemap</span></code>,
<code class="docutils literal notranslate"><span class="pre">top-k</span></code>, <code class="docutils literal notranslate"><span class="pre">status-list</span></code>, <code class="docutils literal notranslate"><span class="pre">histogram</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">windowSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Width, in minutes, of the time window to use for <code class="docutils literal notranslate"><span class="pre">last</span></code> windowing</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">windowing</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - For the tabular view, whether to use the full time window for the query or the last X minutes.
Valid options are <code class="docutils literal notranslate"><span class="pre">full</span></code> or <code class="docutils literal notranslate"><span class="pre">last</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">xmax</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - For x-y scatterplots, max value for the X-axis. Set to null for auto</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">xmin</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - For x-y scatterplots, min value for the X-axis. Set to null for auto</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">y0ScaleSiBy1024</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to scale numerical magnitude labels for left Y-axis by 1024 in the IEC/Binary manner (instead of by 1000 like SI)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">y0UnitAutoscaling</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to automatically adjust magnitude labels and units for the left Y-axis to favor smaller magnitudes and larger units</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">y1ScaleSiBy1024</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to scale numerical magnitude labels for right Y-axis by 1024 in the IEC/Binary manner (instead of by 1000 like SI)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">y1UnitAutoscaling</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether to automatically adjust magnitude labels and units for the right Y-axis to favor smaller magnitudes and larger units</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">y1Units</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - For plots with multiple Y-axes, units for right side Y-axis</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">y1max</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - For plots with multiple Y-axes, max value for the right side Y-axis. Set null for auto</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">y1min</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - For plots with multiple Y-axes, min value for the right side Y-axis. Set null for auto</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ymax</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - For x-y scatterplots, max value for the Y-axis. Set to null for auto</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ymin</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - For x-y scatterplots, min value for the Y-axis. Set to null for auto</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Description of the chart</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the source</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sources</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Query expression to plot on the chart. See chart source queries</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether the source is disabled</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Name of the source</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">query</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Query expression to plot on the chart</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryBuilderEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether oir not this source line should have the query builder enabled</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scatterPlotSource</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - For scatter plots, does this query source the X-axis or the Y-axis, <code class="docutils literal notranslate"><span class="pre">X</span></code>, or <code class="docutils literal notranslate"><span class="pre">Y</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceDescription</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A description for the purpose of this source</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">summarization</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Summarization strategy for the chart. MEAN is default. Valid options are, <code class="docutils literal notranslate"><span class="pre">MEAN</span></code>, 
<code class="docutils literal notranslate"><span class="pre">MEDIAN</span></code>, <code class="docutils literal notranslate"><span class="pre">MIN</span></code>, <code class="docutils literal notranslate"><span class="pre">MAX</span></code>, <code class="docutils literal notranslate"><span class="pre">SUM</span></code>, <code class="docutils literal notranslate"><span class="pre">COUNT</span></code>, <code class="docutils literal notranslate"><span class="pre">LAST</span></code>, <code class="docutils literal notranslate"><span class="pre">FIRST</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">units</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - String to label the units of the chart on the Y-Axis</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.Dashboard.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.Dashboard.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of tags to assign to this resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.Dashboard.url">
<code class="sig-name descname">url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.Dashboard.url" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier, also URL slug, of the dashboard</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.Dashboard.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">can_modifies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">can_views</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_query_parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_section_table_of_contents</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">event_filter_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameter_details</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sections</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.Dashboard.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Dashboard resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>can_modifies</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of users that have modify ACL access to the dashboard</p></li>
<li><p><strong>can_views</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of users that have view ACL access to the dashboard</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description of the dashboard</p></li>
<li><p><strong>display_query_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the dashboard parameters section is opened by default when the dashboard
is shown</p></li>
<li><p><strong>display_section_table_of_contents</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the “pills” quick-linked the sections of the dashboard are 
displayed by default when the dashboard is shown</p></li>
<li><p><strong>event_filter_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – How charts belonging to this dashboard should display events. BYCHART is default if 
unspecified; Valid options are: <code class="docutils literal notranslate"><span class="pre">BYCHART</span></code>, <code class="docutils literal notranslate"><span class="pre">AUTOMATIC</span></code>, <code class="docutils literal notranslate"><span class="pre">ALL</span></code>, <code class="docutils literal notranslate"><span class="pre">NONE</span></code>, <code class="docutils literal notranslate"><span class="pre">BYDASHBOARD</span></code>, and <code class="docutils literal notranslate"><span class="pre">BYCHARTANDDASHBOARD</span></code></p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the dashboard</p></li>
<li><p><strong>parameter_details</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The current JSON representation of dashboard parameters. See parameter details</p></li>
<li><p><strong>sections</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Dashboard chart sections. See dashboard sections</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of tags to assign to this resource.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier, also URL slug, of the dashboard</p></li>
</ul>
</dd>
</dl>
<p>The <strong>parameter_details</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">defaultValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The default value of the parameter</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dynamicFieldType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For <code class="docutils literal notranslate"><span class="pre">DYNAMIC</span></code> parameter types, the type of the field. Valid options are <code class="docutils literal notranslate"><span class="pre">SOURCE</span></code>,
<code class="docutils literal notranslate"><span class="pre">SOURCE_TAG</span></code>, <code class="docutils literal notranslate"><span class="pre">METRIC_NAME</span></code>, <code class="docutils literal notranslate"><span class="pre">TAG_KEY</span></code>, <code class="docutils literal notranslate"><span class="pre">MATCHING_SOURCE_TAG</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">hideFromView</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If <code class="docutils literal notranslate"><span class="pre">true</span></code> the parameter will only be shown on the edit view of the dashboard</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The label for the parameter</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the parameters</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">parameterType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of the parameter. <code class="docutils literal notranslate"><span class="pre">SIMPLE</span></code>, <code class="docutils literal notranslate"><span class="pre">LIST</span></code>, or <code class="docutils literal notranslate"><span class="pre">DYNAMIC</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For <code class="docutils literal notranslate"><span class="pre">DYNAMIC</span></code> parameter types, the query to execute to return values</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tagKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - for <code class="docutils literal notranslate"><span class="pre">TAG_KEY</span></code> dynamic field types, the tag key to return</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">valuesToReadableStrings</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A string-&gt;string map.  At least one of the keys must match the value of
<code class="docutils literal notranslate"><span class="pre">default_value</span></code></p></li>
</ul>
<p>The <strong>sections</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of this section</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">rows</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - See dashboard section rows</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">charts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Charts in this section. See dashboard chart</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">chartSetting</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Chart settings. See chart settings</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">autoColumnTags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - deprecated</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">columnTags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - deprecated</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">customTags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - For the tabular view, a list of point tags to display when using the <code class="docutils literal notranslate"><span class="pre">custom</span></code> tag display mode</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expectedDataSpacing</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Threshold (in seconds) for time delta between consecutive points in a series
above which a dotted line will replace a solid in in line plots. Default 60</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedLegendDisplayStats</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - For a chart with a fixed legend, a list of statistics to display in the legend</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedLegendEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to enable a fixed tabular legend adjacent to the chart</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedLegendFilterField</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Statistic to use for determining whether a series is displayed on the fixed legend.
Valid options are <code class="docutils literal notranslate"><span class="pre">CURRENT</span></code>, <code class="docutils literal notranslate"><span class="pre">MEAN</span></code>, <code class="docutils literal notranslate"><span class="pre">MEDIAN</span></code>, <code class="docutils literal notranslate"><span class="pre">SUM</span></code>, <code class="docutils literal notranslate"><span class="pre">MIN</span></code>, <code class="docutils literal notranslate"><span class="pre">MAX</span></code>, <code class="docutils literal notranslate"><span class="pre">COUNT</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedLegendFilterLimit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of series to include in the fixed legend</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedLegendFilterSort</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Whether to display <code class="docutils literal notranslate"><span class="pre">TOP</span></code> or <code class="docutils literal notranslate"><span class="pre">BOTTOM</span></code> ranked series in a fixed legend. Valid options
are <code class="docutils literal notranslate"><span class="pre">TOP</span></code>, and <code class="docutils literal notranslate"><span class="pre">BOTTOM</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedLegendHideLabel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - deprecated</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedLegendPosition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Where the fixed legend should be displayed with respect ot the chart.
Valid options are <code class="docutils literal notranslate"><span class="pre">RIGHt</span></code>, <code class="docutils literal notranslate"><span class="pre">TOP</span></code>, <code class="docutils literal notranslate"><span class="pre">LEFT</span></code>, <code class="docutils literal notranslate"><span class="pre">BOTTOM</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">fixedLegendUseRawStats</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If <code class="docutils literal notranslate"><span class="pre">true</span></code>, the legend uses non-summarized stats instead of summarized</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupBySource</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - For the tabular view, whether to group multi metrics into a single row by a common source.
If <code class="docutils literal notranslate"><span class="pre">false</span></code>, each source is displayed in its own row.  if <code class="docutils literal notranslate"><span class="pre">true</span></code>, multiple metrics for the same host will be displayed as different
columns in the same row</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">invertDynamicLegendHoverControl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to disable the display of the floating legend (but
reenable it when the ctrl-key is pressed)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lineType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Plot interpolation type.  <code class="docutils literal notranslate"><span class="pre">linear</span></code> is default. Valid options are <code class="docutils literal notranslate"><span class="pre">linear</span></code>, <code class="docutils literal notranslate"><span class="pre">step-before</span></code>, 
<code class="docutils literal notranslate"><span class="pre">step-after</span></code>, <code class="docutils literal notranslate"><span class="pre">basis</span></code>, <code class="docutils literal notranslate"><span class="pre">cardinal</span></code>, <code class="docutils literal notranslate"><span class="pre">monotone</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">max</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Max value of the Y-axis. Set to null or leave blank for auto</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">min</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Min value of the Y-axis. Set to null or leave blank for auto</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">numTags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - For the tabular view, how many point tags to display</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">plainMarkdownContent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The markdown content for a Markdown display, in plain text.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">showHosts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - For the tabular view, whether to display sources. Default is <code class="docutils literal notranslate"><span class="pre">true</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">showLabels</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - For the tabular view, whether to display labels. Default is <code class="docutils literal notranslate"><span class="pre">true</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">showRawValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - For the tabular view, whether to display raw values. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sortValuesDescending</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - For the tabular view, whether to display display values in descending order. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineDecimalPrecision</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - For the single stat view, the decimal precision of the displayed number</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineDisplayColor</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For the single stat view, the color of the displayed text (when not dynamically determined). 
Values should be in <code class="docutils literal notranslate"><span class="pre">rgba(,,,,)</span></code> format</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineDisplayFontSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For the single stat view, the font size of the displayed text, in percent</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineDisplayHorizontalPosition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For the single stat view, the horizontal position of the displayed text.
Valid options are <code class="docutils literal notranslate"><span class="pre">MIDDLE</span></code>, <code class="docutils literal notranslate"><span class="pre">LEFT</span></code>, <code class="docutils literal notranslate"><span class="pre">RIGHT</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineDisplayPostfix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For the single stat view, a string to append to the displayed text</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineDisplayPrefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For the single stat view, a string to add before the displayed text</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineDisplayValueType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For the single stat view, where to display the name of the query or the value of the query.
Valid options are <code class="docutils literal notranslate"><span class="pre">VALUE</span></code> or <code class="docutils literal notranslate"><span class="pre">LABEL</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineDisplayVerticalPosition</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - deprecated</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineFillColor</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For the single stat view, the color of the background fill.  Values should be
in <code class="docutils literal notranslate"><span class="pre">rgba(,,,,)</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineLineColor</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For the single stat view, the color of the line.  Values should be in <code class="docutils literal notranslate"><span class="pre">rgba(,,,,)</span></code> format</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For the single stat view, This determines whether the sparkline of the statistic is displayed in the chart <code class="docutils literal notranslate"><span class="pre">BACKGROUND</span></code>, <code class="docutils literal notranslate"><span class="pre">BOTTOM</span></code>, or <code class="docutils literal notranslate"><span class="pre">NONE</span></code>.
Valid options are <code class="docutils literal notranslate"><span class="pre">BACKGROUND</span></code>, <code class="docutils literal notranslate"><span class="pre">BOTTOM</span></code>, <code class="docutils literal notranslate"><span class="pre">NONE</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineValueColorMapApplyTo</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For the single stat view, whether to apply dyunamic color settings to 
the displayed <code class="docutils literal notranslate"><span class="pre">TEXT</span></code> or <code class="docutils literal notranslate"><span class="pre">BACKGROUND</span></code>. Valid options are <code class="docutils literal notranslate"><span class="pre">TEXT</span></code> or <code class="docutils literal notranslate"><span class="pre">BACKGROUND</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineValueColorMapColors</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - For the single stat view, A list of colors that differing query values map to. 
Must contain one more element than <code class="docutils literal notranslate"><span class="pre">sparkline_value_color_map_values_v2</span></code>. Values should be in <code class="docutils literal notranslate"><span class="pre">rgba(,,,,)</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineValueColorMapValues</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - deprecated</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineValueColorMapValuesV2s</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - For the single stat view, a list of boundaries for mapping different
query values to colors.  Must contain one less element than <code class="docutils literal notranslate"><span class="pre">sparkline_value_color_map_colors</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineValueTextMapTexts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - For the single stat view, a list of display text values that different query
values map to.  Must contain one more element than <code class="docutils literal notranslate"><span class="pre">sparkline_value_text_map_thresholds</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sparklineValueTextMapThresholds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - For the single stat view, a list of threshold boundaries for 
mapping different query values to display text.  Must contain one less element than <code class="docutils literal notranslate"><span class="pre">sparkline_value_text_map_text</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">stackType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Type of stacked chart (applicable only if chart type is <code class="docutils literal notranslate"><span class="pre">stacked</span></code>). <code class="docutils literal notranslate"><span class="pre">zero</span></code> (default) means
stacked from y=0. <code class="docutils literal notranslate"><span class="pre">expand</span></code> means normalized from 0 to 1.  <code class="docutils literal notranslate"><span class="pre">wiggle</span></code> means minimize weighted changes. <code class="docutils literal notranslate"><span class="pre">silhouette</span></code> means to
center the stream. Valid options are <code class="docutils literal notranslate"><span class="pre">zero</span></code>, <code class="docutils literal notranslate"><span class="pre">expand</span></code>, <code class="docutils literal notranslate"><span class="pre">wiggle</span></code>, <code class="docutils literal notranslate"><span class="pre">silhouette</span></code>, <code class="docutils literal notranslate"><span class="pre">bars</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tagMode</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For the tabular view, which mode to use to determine which point tags to display.
Valid options are <code class="docutils literal notranslate"><span class="pre">all</span></code>, <code class="docutils literal notranslate"><span class="pre">top</span></code>, or <code class="docutils literal notranslate"><span class="pre">custom</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeBasedColoring</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - For x-y scatterplots, whether to color more recent points as darker than older points</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Chart Type. <code class="docutils literal notranslate"><span class="pre">line</span></code> refers to the Line Plot, <code class="docutils literal notranslate"><span class="pre">scatter</span></code> to the Point Plot, <code class="docutils literal notranslate"><span class="pre">stacked-area</span></code> to 
the Stacked Area plot, <code class="docutils literal notranslate"><span class="pre">table</span></code> to the Tabular View, <code class="docutils literal notranslate"><span class="pre">scatterploy-xy</span></code> to Scatter Plot, <code class="docutils literal notranslate"><span class="pre">markdown-widget</span></code> to the
Markdown display, and <code class="docutils literal notranslate"><span class="pre">sparkline</span></code> to the Single Stat view. Valid options are <code class="docutils literal notranslate"><span class="pre">line</span></code>, <code class="docutils literal notranslate"><span class="pre">scatterplot</span></code>,
<code class="docutils literal notranslate"><span class="pre">stacked-area</span></code>, <code class="docutils literal notranslate"><span class="pre">stacked-column</span></code>, <code class="docutils literal notranslate"><span class="pre">table</span></code>, <code class="docutils literal notranslate"><span class="pre">scatterplot-xy</span></code>, <code class="docutils literal notranslate"><span class="pre">markdown-widget</span></code>, <code class="docutils literal notranslate"><span class="pre">sparkline</span></code>, <code class="docutils literal notranslate"><span class="pre">globe</span></code>, <code class="docutils literal notranslate"><span class="pre">nodemap</span></code>,
<code class="docutils literal notranslate"><span class="pre">top-k</span></code>, <code class="docutils literal notranslate"><span class="pre">status-list</span></code>, <code class="docutils literal notranslate"><span class="pre">histogram</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">windowSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Width, in minutes, of the time window to use for <code class="docutils literal notranslate"><span class="pre">last</span></code> windowing</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">windowing</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For the tabular view, whether to use the full time window for the query or the last X minutes.
Valid options are <code class="docutils literal notranslate"><span class="pre">full</span></code> or <code class="docutils literal notranslate"><span class="pre">last</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">xmax</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - For x-y scatterplots, max value for the X-axis. Set to null for auto</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">xmin</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - For x-y scatterplots, min value for the X-axis. Set to null for auto</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">y0ScaleSiBy1024</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to scale numerical magnitude labels for left Y-axis by 1024 in the IEC/Binary manner (instead of by 1000 like SI)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">y0UnitAutoscaling</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to automatically adjust magnitude labels and units for the left Y-axis to favor smaller magnitudes and larger units</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">y1ScaleSiBy1024</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to scale numerical magnitude labels for right Y-axis by 1024 in the IEC/Binary manner (instead of by 1000 like SI)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">y1UnitAutoscaling</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether to automatically adjust magnitude labels and units for the right Y-axis to favor smaller magnitudes and larger units</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">y1Units</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For plots with multiple Y-axes, units for right side Y-axis</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">y1max</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - For plots with multiple Y-axes, max value for the right side Y-axis. Set null for auto</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">y1min</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - For plots with multiple Y-axes, min value for the right side Y-axis. Set null for auto</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ymax</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - For x-y scatterplots, max value for the Y-axis. Set to null for auto</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ymin</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - For x-y scatterplots, min value for the Y-axis. Set to null for auto</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Description of the chart</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the source</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sources</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Query expression to plot on the chart. See chart source queries</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">disabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether the source is disabled</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Name of the source</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">query</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Query expression to plot on the chart</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queryBuilderEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether oir not this source line should have the query builder enabled</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scatterPlotSource</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - For scatter plots, does this query source the X-axis or the Y-axis, <code class="docutils literal notranslate"><span class="pre">X</span></code>, or <code class="docutils literal notranslate"><span class="pre">Y</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceDescription</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A description for the purpose of this source</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">summarization</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Summarization strategy for the chart. MEAN is default. Valid options are, <code class="docutils literal notranslate"><span class="pre">MEAN</span></code>, 
<code class="docutils literal notranslate"><span class="pre">MEDIAN</span></code>, <code class="docutils literal notranslate"><span class="pre">MIN</span></code>, <code class="docutils literal notranslate"><span class="pre">MAX</span></code>, <code class="docutils literal notranslate"><span class="pre">SUM</span></code>, <code class="docutils literal notranslate"><span class="pre">COUNT</span></code>, <code class="docutils literal notranslate"><span class="pre">LAST</span></code>, <code class="docutils literal notranslate"><span class="pre">FIRST</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">units</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - String to label the units of the chart on the Y-Axis</p></li>
</ul>
</li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.Dashboard.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.Dashboard.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.Dashboard.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.Dashboard.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.DashboardJson">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">DashboardJson</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dashboard_json</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.DashboardJson" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Wavefront Dashboard JSON resource.  This allows dashboards to be created, updated, and deleted.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_wavefront</span> <span class="k">as</span> <span class="nn">wavefront</span>

<span class="n">test_dashboard_json</span> <span class="o">=</span> <span class="n">wavefront</span><span class="o">.</span><span class="n">DashboardJson</span><span class="p">(</span><span class="s2">&quot;testDashboardJson&quot;</span><span class="p">,</span> <span class="n">dashboard_json</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;{</span>
<span class="s2">  &quot;name&quot;: &quot;Terraform Test Dashboard Json&quot;,</span>
<span class="s2">  &quot;description&quot;: &quot;a&quot;,</span>
<span class="s2">  &quot;eventFilterType&quot;: &quot;BYCHART&quot;,</span>
<span class="s2">  &quot;eventQuery&quot;: &quot;&quot;,</span>
<span class="s2">  &quot;defaultTimeWindow&quot;: &quot;&quot;,</span>
<span class="s2">  &quot;url&quot;: &quot;tftestimport&quot;,</span>
<span class="s2">  &quot;displayDescription&quot;: false,</span>
<span class="s2">  &quot;displaySectionTableOfContents&quot;: true,</span>
<span class="s2">  &quot;displayQueryParameters&quot;: false,</span>
<span class="s2">  &quot;sections&quot;: [</span>
<span class="s2">    {</span>
<span class="s2">      &quot;name&quot;: &quot;section 1&quot;,</span>
<span class="s2">      &quot;rows&quot;: [</span>
<span class="s2">        {</span>
<span class="s2">          &quot;charts&quot;: [</span>
<span class="s2">            {</span>
<span class="s2">              &quot;name&quot;: &quot;chart 1&quot;,</span>
<span class="s2">              &quot;sources&quot;: [</span>
<span class="s2">                {</span>
<span class="s2">                  &quot;name&quot;: &quot;source 1&quot;,</span>
<span class="s2">                  &quot;query&quot;: &quot;ts()&quot;,</span>
<span class="s2">                  &quot;scatterPlotSource&quot;: &quot;Y&quot;,</span>
<span class="s2">                  &quot;querybuilderEnabled&quot;: false,</span>
<span class="s2">                  &quot;sourceDescription&quot;: &quot;&quot;</span>
<span class="s2">                }</span>
<span class="s2">              ],</span>
<span class="s2">              &quot;units&quot;: &quot;someunit&quot;,</span>
<span class="s2">              &quot;base&quot;: 0,</span>
<span class="s2">              &quot;noDefaultEvents&quot;: false,</span>
<span class="s2">              &quot;interpolatePoints&quot;: false,</span>
<span class="s2">              &quot;includeObsoleteMetrics&quot;: false,</span>
<span class="s2">              &quot;description&quot;: &quot;This is chart 1, showing something&quot;,</span>
<span class="s2">              &quot;chartSettings&quot;: {</span>
<span class="s2">                &quot;type&quot;: &quot;markdown-widget&quot;,</span>
<span class="s2">                &quot;max&quot;: 100,</span>
<span class="s2">                &quot;expectedDataSpacing&quot;: 120,</span>
<span class="s2">                &quot;windowing&quot;: &quot;full&quot;,</span>
<span class="s2">                &quot;windowSize&quot;: 10,</span>
<span class="s2">                &quot;autoColumnTags&quot;: false,</span>
<span class="s2">                &quot;columnTags&quot;: &quot;deprecated&quot;,</span>
<span class="s2">                &quot;tagMode&quot;: &quot;all&quot;,</span>
<span class="s2">                &quot;numTags&quot;: 2,</span>
<span class="s2">                &quot;customTags&quot;: [</span>
<span class="s2">                  &quot;tag1&quot;,</span>
<span class="s2">                  &quot;tag2&quot;</span>
<span class="s2">                ],</span>
<span class="s2">                &quot;groupBySource&quot;: true,</span>
<span class="s2">                &quot;y1Max&quot;: 100,</span>
<span class="s2">                &quot;y1Units&quot;: &quot;units&quot;,</span>
<span class="s2">                &quot;y0ScaleSIBy1024&quot;: true,</span>
<span class="s2">                &quot;y1ScaleSIBy1024&quot;: true,</span>
<span class="s2">                &quot;y0UnitAutoscaling&quot;: true,</span>
<span class="s2">                &quot;y1UnitAutoscaling&quot;: true,</span>
<span class="s2">                &quot;fixedLegendEnabled&quot;: true,</span>
<span class="s2">                &quot;fixedLegendUseRawStats&quot;: true,</span>
<span class="s2">                &quot;fixedLegendPosition&quot;: &quot;RIGHT&quot;,</span>
<span class="s2">                &quot;fixedLegendDisplayStats&quot;: [</span>
<span class="s2">                  &quot;stat1&quot;,</span>
<span class="s2">                  &quot;stat2&quot;</span>
<span class="s2">                ],</span>
<span class="s2">                &quot;fixedLegendFilterSort&quot;: &quot;TOP&quot;,</span>
<span class="s2">                &quot;fixedLegendFilterLimit&quot;: 1,</span>
<span class="s2">                &quot;fixedLegendFilterField&quot;: &quot;CURRENT&quot;,</span>
<span class="s2">                &quot;plainMarkdownContent&quot;: &quot;markdown content&quot;</span>
<span class="s2">              },</span>
<span class="s2">              &quot;summarization&quot;: &quot;MEAN&quot;</span>
<span class="s2">            }</span>
<span class="s2">          ],</span>
<span class="s2">          &quot;heightFactor&quot;: 50</span>
<span class="s2">        }</span>
<span class="s2">      ]</span>
<span class="s2">    }</span>
<span class="s2">  ],</span>
<span class="s2">  &quot;parameterDetails&quot;: {</span>
<span class="s2">    &quot;param&quot;: {</span>
<span class="s2">      &quot;hideFromView&quot;: false,</span>
<span class="s2">      &quot;description&quot;: null,</span>
<span class="s2">      &quot;allowAll&quot;: null,</span>
<span class="s2">      &quot;tagKey&quot;: null,</span>
<span class="s2">      &quot;queryValue&quot;: null,</span>
<span class="s2">      &quot;dynamicFieldType&quot;: null,</span>
<span class="s2">      &quot;reverseDynSort&quot;: null,</span>
<span class="s2">      &quot;parameterType&quot;: &quot;SIMPLE&quot;,</span>
<span class="s2">      &quot;label&quot;: &quot;test&quot;,</span>
<span class="s2">      &quot;defaultValue&quot;: &quot;Label&quot;,</span>
<span class="s2">      &quot;valuesToReadableStrings&quot;: {</span>
<span class="s2">        &quot;Label&quot;: &quot;test&quot;</span>
<span class="s2">      },</span>
<span class="s2">      &quot;selectedLabel&quot;: &quot;Label&quot;,</span>
<span class="s2">      &quot;value&quot;: &quot;test&quot;</span>
<span class="s2">    }</span>
<span class="s2">  },</span>
<span class="s2">  &quot;tags&quot; :{</span>
<span class="s2">    &quot;customerTags&quot;:  [&quot;terraform&quot;]</span>
<span class="s2">  }</span>
<span class="s2">}</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dashboard_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – See <a class="reference external" href="https://docs.wavefront.com/wavefront_api.html#api-documentation-wavefront-instance">Wavefront API Documentation</a> 
for instructions on how to get to your API documentation for more details.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_wavefront.DashboardJson.dashboard_json">
<code class="sig-name descname">dashboard_json</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.DashboardJson.dashboard_json" title="Permalink to this definition">¶</a></dt>
<dd><p>See <a class="reference external" href="https://docs.wavefront.com/wavefront_api.html#api-documentation-wavefront-instance">Wavefront API Documentation</a> 
for instructions on how to get to your API documentation for more details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.DashboardJson.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dashboard_json</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.DashboardJson.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DashboardJson resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dashboard_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>See <a class="reference external" href="https://docs.wavefront.com/wavefront_api.html#api-documentation-wavefront-instance">Wavefront API Documentation</a> 
for instructions on how to get to your API documentation for more details.</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.DashboardJson.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.DashboardJson.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.DashboardJson.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.DashboardJson.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.DerivedMetric">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">DerivedMetric</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_information</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">minutes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.DerivedMetric" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Wavefront Derived Metric Resource. This allows derived metrics to be created,
updated, and deleted.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_wavefront</span> <span class="k">as</span> <span class="nn">wavefront</span>

<span class="n">derived</span> <span class="o">=</span> <span class="n">wavefront</span><span class="o">.</span><span class="n">DerivedMetric</span><span class="p">(</span><span class="s2">&quot;derived&quot;</span><span class="p">,</span>
    <span class="n">minutes</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
    <span class="n">query</span><span class="o">=</span><span class="s2">&quot;aliasMetric(5, &quot;</span><span class="n">some</span><span class="o">.</span><span class="n">metric</span><span class="s2">&quot;)&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_information</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User-supplied additional explanatory information for the derived metric</p></li>
<li><p><strong>minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How frequently the query generating the derived metric is run</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Derived Metric in Wavefront</p></li>
<li><p><strong>query</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A Wavefront query that is evaluated at regular intervals (default <code class="docutils literal notranslate"><span class="pre">1m</span></code>)</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of tags to assign to this resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_wavefront.DerivedMetric.additional_information">
<code class="sig-name descname">additional_information</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.DerivedMetric.additional_information" title="Permalink to this definition">¶</a></dt>
<dd><p>User-supplied additional explanatory information for the derived metric</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.DerivedMetric.minutes">
<code class="sig-name descname">minutes</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.DerivedMetric.minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>How frequently the query generating the derived metric is run</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.DerivedMetric.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.DerivedMetric.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Derived Metric in Wavefront</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.DerivedMetric.query">
<code class="sig-name descname">query</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.DerivedMetric.query" title="Permalink to this definition">¶</a></dt>
<dd><p>A Wavefront query that is evaluated at regular intervals (default <code class="docutils literal notranslate"><span class="pre">1m</span></code>)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.DerivedMetric.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.DerivedMetric.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of tags to assign to this resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.DerivedMetric.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_information</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">minutes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.DerivedMetric.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DerivedMetric resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_information</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User-supplied additional explanatory information for the derived metric</p></li>
<li><p><strong>minutes</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – How frequently the query generating the derived metric is run</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Derived Metric in Wavefront</p></li>
<li><p><strong>query</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A Wavefront query that is evaluated at regular intervals (default <code class="docutils literal notranslate"><span class="pre">1m</span></code>)</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A set of tags to assign to this resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.DerivedMetric.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.DerivedMetric.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.DerivedMetric.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.DerivedMetric.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.GetDefaultUserGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">GetDefaultUserGroupResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.GetDefaultUserGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDefaultUserGroup.</p>
<dl class="py attribute">
<dt id="pulumi_wavefront.GetDefaultUserGroupResult.group_id">
<code class="sig-name descname">group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.GetDefaultUserGroupResult.group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to the Group ID of the <code class="docutils literal notranslate"><span class="pre">Everyone</span></code> group, suitable for referencing
in other resources that support group memberships. s</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.GetDefaultUserGroupResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.GetDefaultUserGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_wavefront.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">http_proxy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the wavefront package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_wavefront.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.Role">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">Role</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">assignees</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.Role" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Wavefront Role Resource. This allows user groups to be created, updated, and deleted.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_wavefront</span> <span class="k">as</span> <span class="nn">wavefront</span>

<span class="n">role</span> <span class="o">=</span> <span class="n">wavefront</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;role&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>assignees</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of user groups or accounts to assign to this role.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A short description of the user group</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user group</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of permissions to assign to this role. Valid options are 
<code class="docutils literal notranslate"><span class="pre">agent_management</span></code>, <code class="docutils literal notranslate"><span class="pre">alerts_management</span></code>, <code class="docutils literal notranslate"><span class="pre">dashboard_management</span></code>, <code class="docutils literal notranslate"><span class="pre">embedded_charts</span></code>, <code class="docutils literal notranslate"><span class="pre">events_management</span></code>, <code class="docutils literal notranslate"><span class="pre">external_links_management</span></code>,
<code class="docutils literal notranslate"><span class="pre">host_tag_management</span></code>, <code class="docutils literal notranslate"><span class="pre">metrics_management</span></code>, <code class="docutils literal notranslate"><span class="pre">user_management</span></code></p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_wavefront.Role.assignees">
<code class="sig-name descname">assignees</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.Role.assignees" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of user groups or accounts to assign to this role.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.Role.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.Role.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A short description of the user group</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.Role.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.Role.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the user group</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.Role.permissions">
<code class="sig-name descname">permissions</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.Role.permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of permissions to assign to this role. Valid options are 
<code class="docutils literal notranslate"><span class="pre">agent_management</span></code>, <code class="docutils literal notranslate"><span class="pre">alerts_management</span></code>, <code class="docutils literal notranslate"><span class="pre">dashboard_management</span></code>, <code class="docutils literal notranslate"><span class="pre">embedded_charts</span></code>, <code class="docutils literal notranslate"><span class="pre">events_management</span></code>, <code class="docutils literal notranslate"><span class="pre">external_links_management</span></code>,
<code class="docutils literal notranslate"><span class="pre">host_tag_management</span></code>, <code class="docutils literal notranslate"><span class="pre">metrics_management</span></code>, <code class="docutils literal notranslate"><span class="pre">user_management</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.Role.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">assignees</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.Role.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Role resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>assignees</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of user groups or accounts to assign to this role.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A short description of the user group</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user group</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of permissions to assign to this role. Valid options are 
<code class="docutils literal notranslate"><span class="pre">agent_management</span></code>, <code class="docutils literal notranslate"><span class="pre">alerts_management</span></code>, <code class="docutils literal notranslate"><span class="pre">dashboard_management</span></code>, <code class="docutils literal notranslate"><span class="pre">embedded_charts</span></code>, <code class="docutils literal notranslate"><span class="pre">events_management</span></code>, <code class="docutils literal notranslate"><span class="pre">external_links_management</span></code>,
<code class="docutils literal notranslate"><span class="pre">host_tag_management</span></code>, <code class="docutils literal notranslate"><span class="pre">metrics_management</span></code>, <code class="docutils literal notranslate"><span class="pre">user_management</span></code></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.Role.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.Role.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.Role.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.Role.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.User">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">User</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">customer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.User" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Wavefront User Resource. This allows users to be created, updated, and deleted.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_wavefront</span> <span class="k">as</span> <span class="nn">wavefront</span>

<span class="n">basic</span> <span class="o">=</span> <span class="n">wavefront</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;basic&quot;</span><span class="p">,</span> <span class="n">email</span><span class="o">=</span><span class="s2">&quot;test+tftesting@example.com&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The (unique) identifier of the user to create. Must be a valid email address</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of permission to grant to this user.  Valid options are
<code class="docutils literal notranslate"><span class="pre">agent_management</span></code>, <code class="docutils literal notranslate"><span class="pre">alerts_management</span></code>, <code class="docutils literal notranslate"><span class="pre">dashboard_management</span></code>, <code class="docutils literal notranslate"><span class="pre">embedded_charts</span></code>, <code class="docutils literal notranslate"><span class="pre">events_management</span></code>, <code class="docutils literal notranslate"><span class="pre">external_links_management</span></code>,
<code class="docutils literal notranslate"><span class="pre">host_tag_management</span></code>, <code class="docutils literal notranslate"><span class="pre">metrics_management</span></code>, <code class="docutils literal notranslate"><span class="pre">user_management</span></code></p></li>
<li><p><strong>user_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of user groups to this user</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_wavefront.User.email">
<code class="sig-name descname">email</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.User.email" title="Permalink to this definition">¶</a></dt>
<dd><p>The (unique) identifier of the user to create. Must be a valid email address</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.User.permissions">
<code class="sig-name descname">permissions</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.User.permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>List of permission to grant to this user.  Valid options are
<code class="docutils literal notranslate"><span class="pre">agent_management</span></code>, <code class="docutils literal notranslate"><span class="pre">alerts_management</span></code>, <code class="docutils literal notranslate"><span class="pre">dashboard_management</span></code>, <code class="docutils literal notranslate"><span class="pre">embedded_charts</span></code>, <code class="docutils literal notranslate"><span class="pre">events_management</span></code>, <code class="docutils literal notranslate"><span class="pre">external_links_management</span></code>,
<code class="docutils literal notranslate"><span class="pre">host_tag_management</span></code>, <code class="docutils literal notranslate"><span class="pre">metrics_management</span></code>, <code class="docutils literal notranslate"><span class="pre">user_management</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.User.user_groups">
<code class="sig-name descname">user_groups</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.User.user_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>List of user groups to this user</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.User.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">customer</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_groups</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.User.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing User resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The (unique) identifier of the user to create. Must be a valid email address</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of permission to grant to this user.  Valid options are
<code class="docutils literal notranslate"><span class="pre">agent_management</span></code>, <code class="docutils literal notranslate"><span class="pre">alerts_management</span></code>, <code class="docutils literal notranslate"><span class="pre">dashboard_management</span></code>, <code class="docutils literal notranslate"><span class="pre">embedded_charts</span></code>, <code class="docutils literal notranslate"><span class="pre">events_management</span></code>, <code class="docutils literal notranslate"><span class="pre">external_links_management</span></code>,
<code class="docutils literal notranslate"><span class="pre">host_tag_management</span></code>, <code class="docutils literal notranslate"><span class="pre">metrics_management</span></code>, <code class="docutils literal notranslate"><span class="pre">user_management</span></code></p></li>
<li><p><strong>user_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of user groups to this user</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.User.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.User.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.User.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.User.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.UserGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">UserGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.UserGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Wavefront User Group Resource. This allows user groups to be created, updated, and deleted.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_wavefront</span> <span class="k">as</span> <span class="nn">wavefront</span>

<span class="n">basic</span> <span class="o">=</span> <span class="n">wavefront</span><span class="o">.</span><span class="n">UserGroup</span><span class="p">(</span><span class="s2">&quot;basic&quot;</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Basic User Group for Unit Tests&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A short description of the user group</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user group</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_wavefront.UserGroup.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.UserGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A short description of the user group</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_wavefront.UserGroup.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_wavefront.UserGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the user group</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.UserGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.UserGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UserGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A short description of the user group</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user group</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.UserGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.UserGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.UserGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.UserGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.get_default_user_group">
<code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">get_default_user_group</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.get_default_user_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the Group ID of the <code class="docutils literal notranslate"><span class="pre">Everyone</span></code> group in Wavefront.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_wavefront</span> <span class="k">as</span> <span class="nn">wavefront</span>

<span class="n">everyone_group</span> <span class="o">=</span> <span class="n">wavefront</span><span class="o">.</span><span class="n">get_default_user_group</span><span class="p">()</span>
</pre></div>
</div>
</dd></dl>

</div>
