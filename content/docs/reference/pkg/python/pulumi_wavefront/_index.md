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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">Alert</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_information</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">can_modifies</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">can_views</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">conditions</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_expression</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">minutes</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_resend_frequency_minutes</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resolve_after_minutes</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">severity</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">threshold_targets</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.Alert" title="Permalink to this definition">¶</a></dt>
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
<p>Alerts can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import wavefront:index/alert:Alert alert_target <span class="m">1479868728473</span>
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
<li><p><strong>can_modifies</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of users or groups that can modify this resource.</p></li>
<li><p><strong>can_views</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of users or groups that can view this resource.</p></li>
<li><p><strong>condition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A Wavefront query that is evaluated at regular intervals (default 1m).
The alert fires and notifications are triggered when data series matching this query evaluates
to a non-zero value for a set number of consecutive minutes.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>conditions</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – a string-&gt;string map of <code class="docutils literal notranslate"><span class="pre">severity</span></code> to <code class="docutils literal notranslate"><span class="pre">condition</span></code> 
for which this alert will trigger.</p></li>
<li><p><strong>display_expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A second query whose results are displayed in the alert user
interface instead of the condition query.  This field is often used to display a version
of the condition query with Boolean operators removed so that numerical values are plotted.</p></li>
<li><p><strong>minutes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of consecutive minutes that a series matching the condition query must 
evaluate to “true” (non-zero value) before the alert fires.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the alert as it is displayed in Wavefront.</p></li>
<li><p><strong>notification_resend_frequency_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How often to re-trigger a continually failing alert. 
If absent or &lt;= 0, no re-triggering occur.</p></li>
<li><p><strong>resolve_after_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of consecutive minutes that a firing series matching the condition
query must evaluate to “false” (zero value) before the alert resolves.  When unset, this default sto
the same value as <code class="docutils literal notranslate"><span class="pre">minutes</span></code>.</p></li>
<li><p><strong>severity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <ul>
<li><p>Severity of the alert, valid values are <code class="docutils literal notranslate"><span class="pre">INFO</span></code>, <code class="docutils literal notranslate"><span class="pre">SMOKE</span></code>, <code class="docutils literal notranslate"><span class="pre">WARN</span></code>, <code class="docutils literal notranslate"><span class="pre">SEVERE</span></code>.</p></li>
</ul>
</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A set of tags to assign to this resource.</p></li>
<li><p><strong>target</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A comma-separated list of the email address or integration endpoint 
(such as PagerDuty or web hook) to notify when the alert status changes.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>threshold_targets</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Targets for severity</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_wavefront.Alert.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_information</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">can_modifies</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">can_views</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">condition</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">conditions</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_expression</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">minutes</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notification_resend_frequency_minutes</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resolve_after_minutes</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">severity</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">threshold_targets</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_wavefront.alert.Alert<a class="headerlink" href="#pulumi_wavefront.Alert.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Alert resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_information</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User-supplied additional explanatory information for this alert.
Useful for linking runbooks, migrations…etc</p></li>
<li><p><strong>alert_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of alert in Wavefront.  Either <code class="docutils literal notranslate"><span class="pre">CLASSIC</span></code> (default) 
or <code class="docutils literal notranslate"><span class="pre">THRESHOLD</span></code></p></li>
<li><p><strong>can_modifies</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of users or groups that can modify this resource.</p></li>
<li><p><strong>can_views</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of users or groups that can view this resource.</p></li>
<li><p><strong>condition</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A Wavefront query that is evaluated at regular intervals (default 1m).
The alert fires and notifications are triggered when data series matching this query evaluates
to a non-zero value for a set number of consecutive minutes.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>conditions</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – a string-&gt;string map of <code class="docutils literal notranslate"><span class="pre">severity</span></code> to <code class="docutils literal notranslate"><span class="pre">condition</span></code> 
for which this alert will trigger.</p></li>
<li><p><strong>display_expression</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A second query whose results are displayed in the alert user
interface instead of the condition query.  This field is often used to display a version
of the condition query with Boolean operators removed so that numerical values are plotted.</p></li>
<li><p><strong>minutes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of consecutive minutes that a series matching the condition query must 
evaluate to “true” (non-zero value) before the alert fires.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the alert as it is displayed in Wavefront.</p></li>
<li><p><strong>notification_resend_frequency_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How often to re-trigger a continually failing alert. 
If absent or &lt;= 0, no re-triggering occur.</p></li>
<li><p><strong>resolve_after_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of consecutive minutes that a firing series matching the condition
query must evaluate to “false” (zero value) before the alert resolves.  When unset, this default sto
the same value as <code class="docutils literal notranslate"><span class="pre">minutes</span></code>.</p></li>
<li><p><strong>severity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <ul>
<li><p>Severity of the alert, valid values are <code class="docutils literal notranslate"><span class="pre">INFO</span></code>, <code class="docutils literal notranslate"><span class="pre">SMOKE</span></code>, <code class="docutils literal notranslate"><span class="pre">WARN</span></code>, <code class="docutils literal notranslate"><span class="pre">SEVERE</span></code>.</p></li>
</ul>
</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A set of tags to assign to this resource.</p></li>
<li><p><strong>target</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A comma-separated list of the email address or integration endpoint 
(such as PagerDuty or web hook) to notify when the alert status changes.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>threshold_targets</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Targets for severity</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.Alert.additional_information">
<em class="property">property </em><code class="sig-name descname">additional_information</code><a class="headerlink" href="#pulumi_wavefront.Alert.additional_information" title="Permalink to this definition">¶</a></dt>
<dd><p>User-supplied additional explanatory information for this alert.
Useful for linking runbooks, migrations…etc</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.Alert.alert_type">
<em class="property">property </em><code class="sig-name descname">alert_type</code><a class="headerlink" href="#pulumi_wavefront.Alert.alert_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of alert in Wavefront.  Either <code class="docutils literal notranslate"><span class="pre">CLASSIC</span></code> (default) 
or <code class="docutils literal notranslate"><span class="pre">THRESHOLD</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.Alert.can_modifies">
<em class="property">property </em><code class="sig-name descname">can_modifies</code><a class="headerlink" href="#pulumi_wavefront.Alert.can_modifies" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of users or groups that can modify this resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.Alert.can_views">
<em class="property">property </em><code class="sig-name descname">can_views</code><a class="headerlink" href="#pulumi_wavefront.Alert.can_views" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of users or groups that can view this resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.Alert.condition">
<em class="property">property </em><code class="sig-name descname">condition</code><a class="headerlink" href="#pulumi_wavefront.Alert.condition" title="Permalink to this definition">¶</a></dt>
<dd><p>A Wavefront query that is evaluated at regular intervals (default 1m).
The alert fires and notifications are triggered when data series matching this query evaluates
to a non-zero value for a set number of consecutive minutes.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.Alert.conditions">
<em class="property">property </em><code class="sig-name descname">conditions</code><a class="headerlink" href="#pulumi_wavefront.Alert.conditions" title="Permalink to this definition">¶</a></dt>
<dd><p>a string-&gt;string map of <code class="docutils literal notranslate"><span class="pre">severity</span></code> to <code class="docutils literal notranslate"><span class="pre">condition</span></code> 
for which this alert will trigger.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.Alert.display_expression">
<em class="property">property </em><code class="sig-name descname">display_expression</code><a class="headerlink" href="#pulumi_wavefront.Alert.display_expression" title="Permalink to this definition">¶</a></dt>
<dd><p>A second query whose results are displayed in the alert user
interface instead of the condition query.  This field is often used to display a version
of the condition query with Boolean operators removed so that numerical values are plotted.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.Alert.minutes">
<em class="property">property </em><code class="sig-name descname">minutes</code><a class="headerlink" href="#pulumi_wavefront.Alert.minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of consecutive minutes that a series matching the condition query must 
evaluate to “true” (non-zero value) before the alert fires.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.Alert.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_wavefront.Alert.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the alert as it is displayed in Wavefront.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.Alert.notification_resend_frequency_minutes">
<em class="property">property </em><code class="sig-name descname">notification_resend_frequency_minutes</code><a class="headerlink" href="#pulumi_wavefront.Alert.notification_resend_frequency_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>How often to re-trigger a continually failing alert. 
If absent or &lt;= 0, no re-triggering occur.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.Alert.resolve_after_minutes">
<em class="property">property </em><code class="sig-name descname">resolve_after_minutes</code><a class="headerlink" href="#pulumi_wavefront.Alert.resolve_after_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of consecutive minutes that a firing series matching the condition
query must evaluate to “false” (zero value) before the alert resolves.  When unset, this default sto
the same value as <code class="docutils literal notranslate"><span class="pre">minutes</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.Alert.severity">
<em class="property">property </em><code class="sig-name descname">severity</code><a class="headerlink" href="#pulumi_wavefront.Alert.severity" title="Permalink to this definition">¶</a></dt>
<dd><ul class="simple">
<li><p>Severity of the alert, valid values are <code class="docutils literal notranslate"><span class="pre">INFO</span></code>, <code class="docutils literal notranslate"><span class="pre">SMOKE</span></code>, <code class="docutils literal notranslate"><span class="pre">WARN</span></code>, <code class="docutils literal notranslate"><span class="pre">SEVERE</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.Alert.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_wavefront.Alert.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of tags to assign to this resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.Alert.target">
<em class="property">property </em><code class="sig-name descname">target</code><a class="headerlink" href="#pulumi_wavefront.Alert.target" title="Permalink to this definition">¶</a></dt>
<dd><p>A comma-separated list of the email address or integration endpoint 
(such as PagerDuty or web hook) to notify when the alert status changes.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.Alert.threshold_targets">
<em class="property">property </em><code class="sig-name descname">threshold_targets</code><a class="headerlink" href="#pulumi_wavefront.Alert.threshold_targets" title="Permalink to this definition">¶</a></dt>
<dd><p>Targets for severity</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">AlertTarget</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_headers</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_subject</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_html_content</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">method</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recipient</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">routes</span><span class="p">:</span> <span class="n">Union[Sequence[Union[AlertTargetRouteArgs, Mapping[str, Any], Awaitable[Union[AlertTargetRouteArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[AlertTargetRouteArgs, Mapping[str, Any], Awaitable[Union[AlertTargetRouteArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">triggers</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.AlertTarget" title="Permalink to this definition">¶</a></dt>
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
        <span class="n">wavefront</span><span class="o">.</span><span class="n">AlertTargetRouteArgs</span><span class="p">(</span>
            <span class="nb">filter</span><span class="o">=</span><span class="p">{</span>
                <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;env&quot;</span><span class="p">,</span>
                <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;prod&quot;</span><span class="p">,</span>
            <span class="p">},</span>
            <span class="n">method</span><span class="o">=</span><span class="s2">&quot;WEBHOOK&quot;</span><span class="p">,</span>
            <span class="n">target</span><span class="o">=</span><span class="s2">&quot;https://hooks.slack.com/services/test/me/prod&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">wavefront</span><span class="o">.</span><span class="n">AlertTargetRouteArgs</span><span class="p">(</span>
            <span class="nb">filter</span><span class="o">=</span><span class="p">{</span>
                <span class="s2">&quot;key&quot;</span><span class="p">:</span> <span class="s2">&quot;env&quot;</span><span class="p">,</span>
                <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;dev&quot;</span><span class="p">,</span>
            <span class="p">},</span>
            <span class="n">method</span><span class="o">=</span><span class="s2">&quot;WEBHOOK&quot;</span><span class="p">,</span>
            <span class="n">target</span><span class="o">=</span><span class="s2">&quot;https://hooks.slack.com/services/test/me/dev&quot;</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">],</span>
    <span class="n">template</span><span class="o">=</span><span class="s2">&quot;</span><span class="si">{}</span><span class="s2">&quot;</span><span class="p">,</span>
    <span class="n">triggers</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;ALERT_OPENED&quot;</span><span class="p">,</span>
        <span class="s2">&quot;ALERT_RESOLVED&quot;</span><span class="p">,</span>
    <span class="p">])</span>
</pre></div>
</div>
<p>Alert Targets can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import wavefront:index/alertTarget:AlertTarget alert_target abcdEFGhijKLMNO
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>content_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of the <code class="docutils literal notranslate"><span class="pre">Content-Type</span></code> header of the webhook.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>custom_headers</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A <code class="docutils literal notranslate"><span class="pre">string-&gt;string</span></code> map specifying the custome HTTP header key/value pairs that will be 
sent in the requests with a method of <code class="docutils literal notranslate"><span class="pre">WEBHOOK</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description describing this alert target.</p></li>
<li><p><strong>email_subject</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The subject title of an email notification target.</p></li>
<li><p><strong>is_html_content</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determine whether the email alert content is sent as HTML or text.</p></li>
<li><p><strong>method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The notification method used for notification target. One of <code class="docutils literal notranslate"><span class="pre">WEBHOOK</span></code>, <code class="docutils literal notranslate"><span class="pre">EMAIL</span></code>, <code class="docutils literal notranslate"><span class="pre">PAGERDUTY</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the alert target as it is displayed in wavefront</p></li>
<li><p><strong>recipient</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The end point for the notification Target.  <cite>EMAIL</cite>: email address. <cite>PAGERDUTY</cite>: PagerDuty 
routing key. <code class="docutils literal notranslate"><span class="pre">WEBHOOK</span></code>: URL endpoint.</p></li>
<li><p><strong>routes</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AlertTargetRouteArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – List of routing targets that this alert target will notify. See Route</p></li>
<li><p><strong>template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A mustache template that will form the body of the POST request, email and summary of the PagerDuty.</p></li>
<li><p><strong>triggers</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of occurrences on which this webhook will be fired. Valid values are <code class="docutils literal notranslate"><span class="pre">ALERT_OPENED</span></code>,
<code class="docutils literal notranslate"><span class="pre">ALERT_UPDATED</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_RESOLVED</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_MAINTENANCE</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_SNOOZED</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_NO_DATA</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_NO_DATA_RESOLVED</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_NO_DATA_MAINTENANCE</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_wavefront.AlertTarget.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_headers</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email_subject</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_html_content</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">method</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recipient</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">routes</span><span class="p">:</span> <span class="n">Union[Sequence[Union[AlertTargetRouteArgs, Mapping[str, Any], Awaitable[Union[AlertTargetRouteArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[AlertTargetRouteArgs, Mapping[str, Any], Awaitable[Union[AlertTargetRouteArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">triggers</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_wavefront.alert_target.AlertTarget<a class="headerlink" href="#pulumi_wavefront.AlertTarget.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AlertTarget resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>content_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of the <code class="docutils literal notranslate"><span class="pre">Content-Type</span></code> header of the webhook.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>custom_headers</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A <code class="docutils literal notranslate"><span class="pre">string-&gt;string</span></code> map specifying the custome HTTP header key/value pairs that will be 
sent in the requests with a method of <code class="docutils literal notranslate"><span class="pre">WEBHOOK</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description describing this alert target.</p></li>
<li><p><strong>email_subject</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The subject title of an email notification target.</p></li>
<li><p><strong>is_html_content</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determine whether the email alert content is sent as HTML or text.</p></li>
<li><p><strong>method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The notification method used for notification target. One of <code class="docutils literal notranslate"><span class="pre">WEBHOOK</span></code>, <code class="docutils literal notranslate"><span class="pre">EMAIL</span></code>, <code class="docutils literal notranslate"><span class="pre">PAGERDUTY</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the alert target as it is displayed in wavefront</p></li>
<li><p><strong>recipient</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The end point for the notification Target.  <cite>EMAIL</cite>: email address. <cite>PAGERDUTY</cite>: PagerDuty 
routing key. <code class="docutils literal notranslate"><span class="pre">WEBHOOK</span></code>: URL endpoint.</p></li>
<li><p><strong>routes</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AlertTargetRouteArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – List of routing targets that this alert target will notify. See Route</p></li>
<li><p><strong>template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A mustache template that will form the body of the POST request, email and summary of the PagerDuty.</p></li>
<li><p><strong>triggers</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of occurrences on which this webhook will be fired. Valid values are <code class="docutils literal notranslate"><span class="pre">ALERT_OPENED</span></code>,
<code class="docutils literal notranslate"><span class="pre">ALERT_UPDATED</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_RESOLVED</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_MAINTENANCE</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_SNOOZED</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_NO_DATA</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_NO_DATA_RESOLVED</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_NO_DATA_MAINTENANCE</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.AlertTarget.content_type">
<em class="property">property </em><code class="sig-name descname">content_type</code><a class="headerlink" href="#pulumi_wavefront.AlertTarget.content_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the <code class="docutils literal notranslate"><span class="pre">Content-Type</span></code> header of the webhook.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.AlertTarget.custom_headers">
<em class="property">property </em><code class="sig-name descname">custom_headers</code><a class="headerlink" href="#pulumi_wavefront.AlertTarget.custom_headers" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">string-&gt;string</span></code> map specifying the custome HTTP header key/value pairs that will be 
sent in the requests with a method of <code class="docutils literal notranslate"><span class="pre">WEBHOOK</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.AlertTarget.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_wavefront.AlertTarget.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description describing this alert target.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.AlertTarget.email_subject">
<em class="property">property </em><code class="sig-name descname">email_subject</code><a class="headerlink" href="#pulumi_wavefront.AlertTarget.email_subject" title="Permalink to this definition">¶</a></dt>
<dd><p>The subject title of an email notification target.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.AlertTarget.is_html_content">
<em class="property">property </em><code class="sig-name descname">is_html_content</code><a class="headerlink" href="#pulumi_wavefront.AlertTarget.is_html_content" title="Permalink to this definition">¶</a></dt>
<dd><p>Determine whether the email alert content is sent as HTML or text.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.AlertTarget.method">
<em class="property">property </em><code class="sig-name descname">method</code><a class="headerlink" href="#pulumi_wavefront.AlertTarget.method" title="Permalink to this definition">¶</a></dt>
<dd><p>The notification method used for notification target. One of <code class="docutils literal notranslate"><span class="pre">WEBHOOK</span></code>, <code class="docutils literal notranslate"><span class="pre">EMAIL</span></code>, <code class="docutils literal notranslate"><span class="pre">PAGERDUTY</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.AlertTarget.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_wavefront.AlertTarget.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the alert target as it is displayed in wavefront</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.AlertTarget.recipient">
<em class="property">property </em><code class="sig-name descname">recipient</code><a class="headerlink" href="#pulumi_wavefront.AlertTarget.recipient" title="Permalink to this definition">¶</a></dt>
<dd><p>The end point for the notification Target.  <cite>EMAIL</cite>: email address. <cite>PAGERDUTY</cite>: PagerDuty 
routing key. <code class="docutils literal notranslate"><span class="pre">WEBHOOK</span></code>: URL endpoint.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.AlertTarget.routes">
<em class="property">property </em><code class="sig-name descname">routes</code><a class="headerlink" href="#pulumi_wavefront.AlertTarget.routes" title="Permalink to this definition">¶</a></dt>
<dd><p>List of routing targets that this alert target will notify. See Route</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.AlertTarget.template">
<em class="property">property </em><code class="sig-name descname">template</code><a class="headerlink" href="#pulumi_wavefront.AlertTarget.template" title="Permalink to this definition">¶</a></dt>
<dd><p>A mustache template that will form the body of the POST request, email and summary of the PagerDuty.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.AlertTarget.triggers">
<em class="property">property </em><code class="sig-name descname">triggers</code><a class="headerlink" href="#pulumi_wavefront.AlertTarget.triggers" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of occurrences on which this webhook will be fired. Valid values are <code class="docutils literal notranslate"><span class="pre">ALERT_OPENED</span></code>,
<code class="docutils literal notranslate"><span class="pre">ALERT_UPDATED</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_RESOLVED</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_MAINTENANCE</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_SNOOZED</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_NO_DATA</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_NO_DATA_RESOLVED</span></code>, <code class="docutils literal notranslate"><span class="pre">ALERT_NO_DATA_MAINTENANCE</span></code>.</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">CloudIntegrationAppDynamics</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_filter_regexes</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">controller_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_app_infra_metrics</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_backend_metrics</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_business_trx_metrics</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_error_metrics</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_individual_node_metrics</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_overall_perf_metrics</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_rollup</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_service_endpoint_metrics</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encrypted_password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics" title="Permalink to this definition">¶</a></dt>
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
<p>App Dynamic Cloud Integrations can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import wavefront:index/cloudIntegrationAppDynamics:CloudIntegrationAppDynamics app_dynamics a411c16b-3cf7-4f03-bf11-8ca05aab898d
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>app_filter_regexes</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of regular expressions that a application name must match (case-insensitively) 
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
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
<li><p><strong>user_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username is a combination of userName and the account name</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_filter_regexes</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">controller_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_app_infra_metrics</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_backend_metrics</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_business_trx_metrics</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_error_metrics</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_individual_node_metrics</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_overall_perf_metrics</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_rollup</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_service_endpoint_metrics</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encrypted_password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_wavefront.cloud_integration_app_dynamics.CloudIntegrationAppDynamics<a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CloudIntegrationAppDynamics resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>app_filter_regexes</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of regular expressions that a application name must match (case-insensitively) 
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
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
<li><p><strong>user_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username is a combination of userName and the account name</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.additional_tags">
<em class="property">property </em><code class="sig-name descname">additional_tags</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.additional_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of point tag key-values to add to every point ingested using this integration</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.app_filter_regexes">
<em class="property">property </em><code class="sig-name descname">app_filter_regexes</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.app_filter_regexes" title="Permalink to this definition">¶</a></dt>
<dd><p>List of regular expressions that a application name must match (case-insensitively) 
in order to be ingested</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.controller_name">
<em class="property">property </em><code class="sig-name descname">controller_name</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.controller_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the SaaS controller</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.enable_app_infra_metrics">
<em class="property">property </em><code class="sig-name descname">enable_app_infra_metrics</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.enable_app_infra_metrics" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag to control Application Infrastructure metric injection</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.enable_backend_metrics">
<em class="property">property </em><code class="sig-name descname">enable_backend_metrics</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.enable_backend_metrics" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag to control Backend metric injection</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.enable_business_trx_metrics">
<em class="property">property </em><code class="sig-name descname">enable_business_trx_metrics</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.enable_business_trx_metrics" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag to control Business Transaction metric injection</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.enable_error_metrics">
<em class="property">property </em><code class="sig-name descname">enable_error_metrics</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.enable_error_metrics" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag to control Error metric injection</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.enable_individual_node_metrics">
<em class="property">property </em><code class="sig-name descname">enable_individual_node_metrics</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.enable_individual_node_metrics" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag to control Individual Node metric injection</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.enable_overall_perf_metrics">
<em class="property">property </em><code class="sig-name descname">enable_overall_perf_metrics</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.enable_overall_perf_metrics" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag to control Overall Performance metric injection</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.enable_rollup">
<em class="property">property </em><code class="sig-name descname">enable_rollup</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.enable_rollup" title="Permalink to this definition">¶</a></dt>
<dd><p>Set this to <code class="docutils literal notranslate"><span class="pre">false</span></code> to get separate results for all values within the time range, 
by default it is <code class="docutils literal notranslate"><span class="pre">true</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.enable_service_endpoint_metrics">
<em class="property">property </em><code class="sig-name descname">enable_service_endpoint_metrics</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.enable_service_endpoint_metrics" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean flag to control Service End point metric injection</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.encrypted_password">
<em class="property">property </em><code class="sig-name descname">encrypted_password</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.encrypted_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Password for AppDynamics user</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.force_save">
<em class="property">property </em><code class="sig-name descname">force_save</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.force_save" title="Permalink to this definition">¶</a></dt>
<dd><p>Forces this resource to save, even if errors are present</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The human-readable name of this integration</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.service">
<em class="property">property </em><code class="sig-name descname">service</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.service" title="Permalink to this definition">¶</a></dt>
<dd><p>A value denoting which cloud service this service integrates with</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.service_refresh_rate_in_minutes">
<em class="property">property </em><code class="sig-name descname">service_refresh_rate_in_minutes</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.service_refresh_rate_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>How often, in minutes, to refresh the service</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAppDynamics.user_name">
<em class="property">property </em><code class="sig-name descname">user_name</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAppDynamics.user_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Username is a combination of userName and the account name</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">CloudIntegrationAwsExternalId</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAwsExternalId" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides an External ID for use in AWS IAM Roles.  This allows External IDs to be created and deleted.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_wavefront</span> <span class="k">as</span> <span class="nn">wavefront</span>

<span class="n">external_id</span> <span class="o">=</span> <span class="n">wavefront</span><span class="o">.</span><span class="n">CloudIntegrationAwsExternalId</span><span class="p">(</span><span class="s2">&quot;externalId&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>External IDs can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import wavefront:index/cloudIntegrationAwsExternalId:CloudIntegrationAwsExternalId external_id uGJdkH3k
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
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_wavefront.cloud_integration_aws_external_id.CloudIntegrationAwsExternalId<a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAwsExternalId.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CloudIntegrationAwsExternalId resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">CloudIntegrationAzure</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">category_filters</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_secret</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_filter_regex</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_filters</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzure" title="Permalink to this definition">¶</a></dt>
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
<p>Azure Cloud Integrations can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import wavefront:index/cloudIntegrationAzure:CloudIntegrationAzure azure a411c16b-3cf7-4f03-bf11-8ca05aab898d
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>category_filters</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of Azure Activity Log categories.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client id for an azure service account within your project</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client secret for an Azure service account within your project</p></li>
<li><p><strong>force_save</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Forces this resource to save, even if errors are present</p></li>
<li><p><strong>metric_filter_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A regular expression that a metric name must match (case-insensitively) in order to be ingested</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable name of this integration</p></li>
<li><p><strong>resource_group_filters</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of Azure resource groups from which to pull metrics</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value denoting which cloud service this service integrates with</p></li>
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
<li><p><strong>tenant</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Tenant Id for an Azure service account within your project</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAzure.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">category_filters</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_secret</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_filter_regex</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_filters</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_wavefront.cloud_integration_azure.CloudIntegrationAzure<a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzure.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CloudIntegrationAzure resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>category_filters</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of Azure Activity Log categories.</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client id for an azure service account within your project</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client secret for an Azure service account within your project</p></li>
<li><p><strong>force_save</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Forces this resource to save, even if errors are present</p></li>
<li><p><strong>metric_filter_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A regular expression that a metric name must match (case-insensitively) in order to be ingested</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable name of this integration</p></li>
<li><p><strong>resource_group_filters</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of Azure resource groups from which to pull metrics</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value denoting which cloud service this service integrates with</p></li>
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
<li><p><strong>tenant</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Tenant Id for an Azure service account within your project</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAzure.additional_tags">
<em class="property">property </em><code class="sig-name descname">additional_tags</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzure.additional_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of point tag key-values to add to every point ingested using this integration</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAzure.category_filters">
<em class="property">property </em><code class="sig-name descname">category_filters</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzure.category_filters" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Azure Activity Log categories.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAzure.client_id">
<em class="property">property </em><code class="sig-name descname">client_id</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzure.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Client id for an azure service account within your project</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAzure.client_secret">
<em class="property">property </em><code class="sig-name descname">client_secret</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzure.client_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>Client secret for an Azure service account within your project</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAzure.force_save">
<em class="property">property </em><code class="sig-name descname">force_save</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzure.force_save" title="Permalink to this definition">¶</a></dt>
<dd><p>Forces this resource to save, even if errors are present</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAzure.metric_filter_regex">
<em class="property">property </em><code class="sig-name descname">metric_filter_regex</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzure.metric_filter_regex" title="Permalink to this definition">¶</a></dt>
<dd><p>A regular expression that a metric name must match (case-insensitively) in order to be ingested</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAzure.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzure.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The human-readable name of this integration</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAzure.resource_group_filters">
<em class="property">property </em><code class="sig-name descname">resource_group_filters</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzure.resource_group_filters" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Azure resource groups from which to pull metrics</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAzure.service">
<em class="property">property </em><code class="sig-name descname">service</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzure.service" title="Permalink to this definition">¶</a></dt>
<dd><p>A value denoting which cloud service this service integrates with</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAzure.service_refresh_rate_in_minutes">
<em class="property">property </em><code class="sig-name descname">service_refresh_rate_in_minutes</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzure.service_refresh_rate_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>How often, in minutes, to refresh the service</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAzure.tenant">
<em class="property">property </em><code class="sig-name descname">tenant</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzure.tenant" title="Permalink to this definition">¶</a></dt>
<dd><p>Tenant Id for an Azure service account within your project</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">CloudIntegrationAzureActivityLog</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">category_filters</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_secret</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzureActivityLog" title="Permalink to this definition">¶</a></dt>
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
<p>Azure Activity Log Cloud Integrations can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import wavefront:index/cloudIntegrationAzureActivityLog:CloudIntegrationAzureActivityLog azure_al a411c16b-3cf7-4f03-bf11-8ca05aab898d
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>category_filters</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of Azure services (such as Microsoft.Compute/virtualMachines) from which to pull metrics</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client id for an azure service account within your project</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client secret for an Azure service account within your project</p></li>
<li><p><strong>force_save</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Forces this resource to save, even if errors are present</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable name of this integration</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value denoting which cloud service this service integrates with</p></li>
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
<li><p><strong>tenant</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Tenant Id for an Azure service account within your project</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAzureActivityLog.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">category_filters</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_secret</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tenant</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_wavefront.cloud_integration_azure_activity_log.CloudIntegrationAzureActivityLog<a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzureActivityLog.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CloudIntegrationAzureActivityLog resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>category_filters</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of Azure services (such as Microsoft.Compute/virtualMachines) from which to pull metrics</p></li>
<li><p><strong>client_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client id for an azure service account within your project</p></li>
<li><p><strong>client_secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Client secret for an Azure service account within your project</p></li>
<li><p><strong>force_save</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Forces this resource to save, even if errors are present</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable name of this integration</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value denoting which cloud service this service integrates with</p></li>
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
<li><p><strong>tenant</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Tenant Id for an Azure service account within your project</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAzureActivityLog.additional_tags">
<em class="property">property </em><code class="sig-name descname">additional_tags</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzureActivityLog.additional_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of point tag key-values to add to every point ingested using this integration</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAzureActivityLog.category_filters">
<em class="property">property </em><code class="sig-name descname">category_filters</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzureActivityLog.category_filters" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Azure services (such as Microsoft.Compute/virtualMachines) from which to pull metrics</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAzureActivityLog.client_id">
<em class="property">property </em><code class="sig-name descname">client_id</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzureActivityLog.client_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Client id for an azure service account within your project</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAzureActivityLog.client_secret">
<em class="property">property </em><code class="sig-name descname">client_secret</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzureActivityLog.client_secret" title="Permalink to this definition">¶</a></dt>
<dd><p>Client secret for an Azure service account within your project</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAzureActivityLog.force_save">
<em class="property">property </em><code class="sig-name descname">force_save</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzureActivityLog.force_save" title="Permalink to this definition">¶</a></dt>
<dd><p>Forces this resource to save, even if errors are present</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAzureActivityLog.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzureActivityLog.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The human-readable name of this integration</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAzureActivityLog.service">
<em class="property">property </em><code class="sig-name descname">service</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzureActivityLog.service" title="Permalink to this definition">¶</a></dt>
<dd><p>A value denoting which cloud service this service integrates with</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAzureActivityLog.service_refresh_rate_in_minutes">
<em class="property">property </em><code class="sig-name descname">service_refresh_rate_in_minutes</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzureActivityLog.service_refresh_rate_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>How often, in minutes, to refresh the service</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationAzureActivityLog.tenant">
<em class="property">property </em><code class="sig-name descname">tenant</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationAzureActivityLog.tenant" title="Permalink to this definition">¶</a></dt>
<dd><p>Tenant Id for an Azure service account within your project</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">CloudIntegrationCloudTrail</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bucket_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">external_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter_rule</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">prefix</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_arn</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudTrail" title="Permalink to this definition">¶</a></dt>
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
<p>CloudTrail Cloud Integrations can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import wavefront:index/cloudIntegrationCloudTrail:CloudIntegrationCloudTrail cloudtrail a411c16b-3cf7-4f03-bf11-8ca05aab898d
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>bucket_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the S3 bucket where CloudTrail logs are stored</p></li>
<li><p><strong>external_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Role ARN that the customer has created in AWS IAM to allow access to Wavefront</p></li>
<li><p><strong>filter_rule</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Rule to filter CloudTrail log event</p></li>
<li><p><strong>force_save</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Forces this resource to save, even if errors are present</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable name of this integration</p></li>
<li><p><strong>prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The common prefix, if any, appended to all CloudTrail log files.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS region of the S3 bucket where CloudTrail logs are stored</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The external id corresponding to the Role ARN</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value denoting which cloud service this service integrates with</p></li>
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationCloudTrail.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bucket_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">external_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter_rule</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">prefix</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_arn</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_wavefront.cloud_integration_cloud_trail.CloudIntegrationCloudTrail<a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudTrail.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CloudIntegrationCloudTrail resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>bucket_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the S3 bucket where CloudTrail logs are stored</p></li>
<li><p><strong>external_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Role ARN that the customer has created in AWS IAM to allow access to Wavefront</p></li>
<li><p><strong>filter_rule</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Rule to filter CloudTrail log event</p></li>
<li><p><strong>force_save</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Forces this resource to save, even if errors are present</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable name of this integration</p></li>
<li><p><strong>prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The common prefix, if any, appended to all CloudTrail log files.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS region of the S3 bucket where CloudTrail logs are stored</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The external id corresponding to the Role ARN</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value denoting which cloud service this service integrates with</p></li>
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationCloudTrail.additional_tags">
<em class="property">property </em><code class="sig-name descname">additional_tags</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudTrail.additional_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of point tag key-values to add to every point ingested using this integration</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationCloudTrail.bucket_name">
<em class="property">property </em><code class="sig-name descname">bucket_name</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudTrail.bucket_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the S3 bucket where CloudTrail logs are stored</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationCloudTrail.external_id">
<em class="property">property </em><code class="sig-name descname">external_id</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudTrail.external_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Role ARN that the customer has created in AWS IAM to allow access to Wavefront</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationCloudTrail.filter_rule">
<em class="property">property </em><code class="sig-name descname">filter_rule</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudTrail.filter_rule" title="Permalink to this definition">¶</a></dt>
<dd><p>Rule to filter CloudTrail log event</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationCloudTrail.force_save">
<em class="property">property </em><code class="sig-name descname">force_save</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudTrail.force_save" title="Permalink to this definition">¶</a></dt>
<dd><p>Forces this resource to save, even if errors are present</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationCloudTrail.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudTrail.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The human-readable name of this integration</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationCloudTrail.prefix">
<em class="property">property </em><code class="sig-name descname">prefix</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudTrail.prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The common prefix, if any, appended to all CloudTrail log files.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationCloudTrail.region">
<em class="property">property </em><code class="sig-name descname">region</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudTrail.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS region of the S3 bucket where CloudTrail logs are stored</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationCloudTrail.role_arn">
<em class="property">property </em><code class="sig-name descname">role_arn</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudTrail.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The external id corresponding to the Role ARN</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationCloudTrail.service">
<em class="property">property </em><code class="sig-name descname">service</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudTrail.service" title="Permalink to this definition">¶</a></dt>
<dd><p>A value denoting which cloud service this service integrates with</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationCloudTrail.service_refresh_rate_in_minutes">
<em class="property">property </em><code class="sig-name descname">service_refresh_rate_in_minutes</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudTrail.service_refresh_rate_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>How often, in minutes, to refresh the service</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">CloudIntegrationCloudWatch</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">external_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_selection_tags</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_filter_regex</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespaces</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">point_tag_filter_regex</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_arn</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">volume_selection_tags</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudWatch" title="Permalink to this definition">¶</a></dt>
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
<p>CloudWatch Cloud Integrations can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import wavefront:index/cloudIntegrationCloudWatch:CloudIntegrationCloudWatch cloudwatch a411c16b-3cf7-4f03-bf11-8ca05aab898d
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>external_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Role ARN that the customer has created in AWS IAM to allow access to Wavefront</p></li>
<li><p><strong>force_save</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Forces this resource to save, even if errors are present</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>instance_selection_tags</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A string-&gt;string map whitelist of instance tag-value pairs (in AWS).
If the instance’s AWS tags match this whitelist, CloudWatch data about this instance is ingested.
Multiple entries are OR’ed</p></li>
<li><p><strong>metric_filter_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A regular expression that a CloudWatch metric name must match (case-insensitively) in order to be ingested</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable name of this integration</p></li>
<li><p><strong>namespaces</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of namespaces that limit what we query from CloudWatch</p></li>
<li><p><strong>point_tag_filter_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A regular expression that AWS tag key name must match (case-insensitively)
in order to be ingested</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The external id corresponding to the Role ARN</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value denoting which cloud service this service integrates with</p></li>
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>volume_selection_tags</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A string-&gt;string map of whitelist of volume tag-value pairs (in AWS).
If the volume’s AWS tags match this whitelist, CloudWatch data about this volume is ingested.
Multiple entries are OR’ed</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationCloudWatch.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">external_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">instance_selection_tags</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_filter_regex</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespaces</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">point_tag_filter_regex</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_arn</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">volume_selection_tags</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_wavefront.cloud_integration_cloud_watch.CloudIntegrationCloudWatch<a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudWatch.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CloudIntegrationCloudWatch resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>external_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Role ARN that the customer has created in AWS IAM to allow access to Wavefront</p></li>
<li><p><strong>force_save</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Forces this resource to save, even if errors are present</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>instance_selection_tags</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A string-&gt;string map whitelist of instance tag-value pairs (in AWS).
If the instance’s AWS tags match this whitelist, CloudWatch data about this instance is ingested.
Multiple entries are OR’ed</p></li>
<li><p><strong>metric_filter_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A regular expression that a CloudWatch metric name must match (case-insensitively) in order to be ingested</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable name of this integration</p></li>
<li><p><strong>namespaces</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of namespaces that limit what we query from CloudWatch</p></li>
<li><p><strong>point_tag_filter_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A regular expression that AWS tag key name must match (case-insensitively)
in order to be ingested</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The external id corresponding to the Role ARN</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value denoting which cloud service this service integrates with</p></li>
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>volume_selection_tags</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A string-&gt;string map of whitelist of volume tag-value pairs (in AWS).
If the volume’s AWS tags match this whitelist, CloudWatch data about this volume is ingested.
Multiple entries are OR’ed</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationCloudWatch.additional_tags">
<em class="property">property </em><code class="sig-name descname">additional_tags</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudWatch.additional_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of point tag key-values to add to every point ingested using this integration</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationCloudWatch.external_id">
<em class="property">property </em><code class="sig-name descname">external_id</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudWatch.external_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Role ARN that the customer has created in AWS IAM to allow access to Wavefront</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationCloudWatch.force_save">
<em class="property">property </em><code class="sig-name descname">force_save</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudWatch.force_save" title="Permalink to this definition">¶</a></dt>
<dd><p>Forces this resource to save, even if errors are present</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationCloudWatch.instance_selection_tags">
<em class="property">property </em><code class="sig-name descname">instance_selection_tags</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudWatch.instance_selection_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A string-&gt;string map whitelist of instance tag-value pairs (in AWS).
If the instance’s AWS tags match this whitelist, CloudWatch data about this instance is ingested.
Multiple entries are OR’ed</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationCloudWatch.metric_filter_regex">
<em class="property">property </em><code class="sig-name descname">metric_filter_regex</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudWatch.metric_filter_regex" title="Permalink to this definition">¶</a></dt>
<dd><p>A regular expression that a CloudWatch metric name must match (case-insensitively) in order to be ingested</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationCloudWatch.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudWatch.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The human-readable name of this integration</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationCloudWatch.namespaces">
<em class="property">property </em><code class="sig-name descname">namespaces</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudWatch.namespaces" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of namespaces that limit what we query from CloudWatch</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationCloudWatch.point_tag_filter_regex">
<em class="property">property </em><code class="sig-name descname">point_tag_filter_regex</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudWatch.point_tag_filter_regex" title="Permalink to this definition">¶</a></dt>
<dd><p>A regular expression that AWS tag key name must match (case-insensitively)
in order to be ingested</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationCloudWatch.role_arn">
<em class="property">property </em><code class="sig-name descname">role_arn</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudWatch.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The external id corresponding to the Role ARN</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationCloudWatch.service">
<em class="property">property </em><code class="sig-name descname">service</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudWatch.service" title="Permalink to this definition">¶</a></dt>
<dd><p>A value denoting which cloud service this service integrates with</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationCloudWatch.service_refresh_rate_in_minutes">
<em class="property">property </em><code class="sig-name descname">service_refresh_rate_in_minutes</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudWatch.service_refresh_rate_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>How often, in minutes, to refresh the service</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationCloudWatch.volume_selection_tags">
<em class="property">property </em><code class="sig-name descname">volume_selection_tags</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationCloudWatch.volume_selection_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A string-&gt;string map of whitelist of volume tag-value pairs (in AWS).
If the volume’s AWS tags match this whitelist, CloudWatch data about this volume is ingested.
Multiple entries are OR’ed</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">CloudIntegrationEc2</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">external_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname_tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_arn</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationEc2" title="Permalink to this definition">¶</a></dt>
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
<p>EC2 Cloud Integrations can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import wavefront:index/cloudIntegrationEc2:CloudIntegrationEc2 ec2 a411c16b-3cf7-4f03-bf11-8ca05aab898d
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>external_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Role ARN that the customer has created in AWS IAM to allow access to Wavefront</p></li>
<li><p><strong>force_save</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Forces this resource to save, even if errors are present</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable name of this integration</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The external id corresponding to the Role ARN</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value denoting which cloud service this service integrates with</p></li>
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationEc2.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">external_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hostname_tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_arn</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_wavefront.cloud_integration_ec2.CloudIntegrationEc2<a class="headerlink" href="#pulumi_wavefront.CloudIntegrationEc2.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CloudIntegrationEc2 resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>external_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Role ARN that the customer has created in AWS IAM to allow access to Wavefront</p></li>
<li><p><strong>force_save</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Forces this resource to save, even if errors are present</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable name of this integration</p></li>
<li><p><strong>role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The external id corresponding to the Role ARN</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value denoting which cloud service this service integrates with</p></li>
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationEc2.additional_tags">
<em class="property">property </em><code class="sig-name descname">additional_tags</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationEc2.additional_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of point tag key-values to add to every point ingested using this integration</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationEc2.external_id">
<em class="property">property </em><code class="sig-name descname">external_id</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationEc2.external_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Role ARN that the customer has created in AWS IAM to allow access to Wavefront</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationEc2.force_save">
<em class="property">property </em><code class="sig-name descname">force_save</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationEc2.force_save" title="Permalink to this definition">¶</a></dt>
<dd><p>Forces this resource to save, even if errors are present</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationEc2.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationEc2.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The human-readable name of this integration</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationEc2.role_arn">
<em class="property">property </em><code class="sig-name descname">role_arn</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationEc2.role_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>The external id corresponding to the Role ARN</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationEc2.service">
<em class="property">property </em><code class="sig-name descname">service</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationEc2.service" title="Permalink to this definition">¶</a></dt>
<dd><p>A value denoting which cloud service this service integrates with</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationEc2.service_refresh_rate_in_minutes">
<em class="property">property </em><code class="sig-name descname">service_refresh_rate_in_minutes</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationEc2.service_refresh_rate_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>How often, in minutes, to refresh the service</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">CloudIntegrationGcp</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">categories</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">json_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_filter_regex</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcp" title="Permalink to this definition">¶</a></dt>
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
<p>GCP Cloud Integrations can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import wavefront:index/cloudIntegrationGcp:CloudIntegrationGcp gcp a411c16b-3cf7-4f03-bf11-8ca05aab898d
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>categories</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of Google Cloud Platform (GCP) services.  Valid values are <code class="docutils literal notranslate"><span class="pre">APPENGINE</span></code>, 
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
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationGcp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">categories</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">json_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_filter_regex</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_wavefront.cloud_integration_gcp.CloudIntegrationGcp<a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CloudIntegrationGcp resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>categories</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of Google Cloud Platform (GCP) services.  Valid values are <code class="docutils literal notranslate"><span class="pre">APPENGINE</span></code>, 
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
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationGcp.additional_tags">
<em class="property">property </em><code class="sig-name descname">additional_tags</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcp.additional_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of point tag key-values to add to every point ingested using this integration</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationGcp.categories">
<em class="property">property </em><code class="sig-name descname">categories</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcp.categories" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Google Cloud Platform (GCP) services.  Valid values are <code class="docutils literal notranslate"><span class="pre">APPENGINE</span></code>, 
<code class="docutils literal notranslate"><span class="pre">BIGQUERY</span></code>, <code class="docutils literal notranslate"><span class="pre">BIGTABLE</span></code>, <code class="docutils literal notranslate"><span class="pre">CLOUDFUNCTIONS</span></code>, <code class="docutils literal notranslate"><span class="pre">CLOUDIOT</span></code>, <code class="docutils literal notranslate"><span class="pre">CLOUDSQL</span></code>, <code class="docutils literal notranslate"><span class="pre">CLOUDTASKS</span></code>, <code class="docutils literal notranslate"><span class="pre">COMPUTE</span></code>, <code class="docutils literal notranslate"><span class="pre">CONTAINER</span></code>,
<code class="docutils literal notranslate"><span class="pre">DATAFLOW</span></code>, <code class="docutils literal notranslate"><span class="pre">DATAPROC</span></code>, <code class="docutils literal notranslate"><span class="pre">DATASTORE</span></code>, <code class="docutils literal notranslate"><span class="pre">FIREBASEDATABASE</span></code>, <code class="docutils literal notranslate"><span class="pre">FIREBASEHOSTING</span></code>, <code class="docutils literal notranslate"><span class="pre">FIRESTORE</span></code>, <code class="docutils literal notranslate"><span class="pre">INTERCONNECT</span></code>,
<code class="docutils literal notranslate"><span class="pre">LOADBALANCING</span></code>, <code class="docutils literal notranslate"><span class="pre">LOGGING</span></code>, <code class="docutils literal notranslate"><span class="pre">ML</span></code>, <code class="docutils literal notranslate"><span class="pre">MONITORING</span></code>, <code class="docutils literal notranslate"><span class="pre">PUBSUB</span></code>, <code class="docutils literal notranslate"><span class="pre">REDIS</span></code>, <code class="docutils literal notranslate"><span class="pre">ROUTER</span></code>, <code class="docutils literal notranslate"><span class="pre">SERVICERUNTIME</span></code>, <code class="docutils literal notranslate"><span class="pre">SPANNER</span></code>, <code class="docutils literal notranslate"><span class="pre">STORAGE</span></code>,
<code class="docutils literal notranslate"><span class="pre">TPU</span></code>, <code class="docutils literal notranslate"><span class="pre">VPN</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationGcp.force_save">
<em class="property">property </em><code class="sig-name descname">force_save</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcp.force_save" title="Permalink to this definition">¶</a></dt>
<dd><p>Forces this resource to save, even if errors are present</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationGcp.json_key">
<em class="property">property </em><code class="sig-name descname">json_key</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcp.json_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Private key for a Google Cloud Platform (GCP) service account within your project.
The account must be at least granted Monitoring Viewer permissions. This key must be in the JSON format generated by GCP.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationGcp.metric_filter_regex">
<em class="property">property </em><code class="sig-name descname">metric_filter_regex</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcp.metric_filter_regex" title="Permalink to this definition">¶</a></dt>
<dd><p>A regular expression that a metric name must match (case-insensitively) in order to be ingested</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationGcp.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcp.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The human-readable name of this integration</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationGcp.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcp.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Google Cloud Platform (GCP) Project Id</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationGcp.service">
<em class="property">property </em><code class="sig-name descname">service</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcp.service" title="Permalink to this definition">¶</a></dt>
<dd><p>A value denoting which cloud service this service integrates with</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationGcp.service_refresh_rate_in_minutes">
<em class="property">property </em><code class="sig-name descname">service_refresh_rate_in_minutes</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcp.service_refresh_rate_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>How often, in minutes, to refresh the service</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">CloudIntegrationGcpBilling</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">json_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcpBilling" title="Permalink to this definition">¶</a></dt>
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
<p>GCP Billing Cloud Integrations can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import wavefront:index/cloudIntegrationGcpBilling:CloudIntegrationGcpBilling gcp_billing a411c16b-3cf7-4f03-bf11-8ca05aab898d
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>api_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – API key for Google Cloud Platform (GCP)</p></li>
<li><p><strong>force_save</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Forces this resource to save, even if errors are present</p></li>
<li><p><strong>json_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Private key for a Google Cloud Platform (GCP) service account within your project.
The account must be at least granted Monitoring Viewer permissions. This key must be in the JSON format generated by GCP.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable name of this integration</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Google Cloud Platform (GCP) Project Id</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value denoting which cloud service this service integrates with</p></li>
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationGcpBilling.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">json_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_wavefront.cloud_integration_gcp_billing.CloudIntegrationGcpBilling<a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcpBilling.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CloudIntegrationGcpBilling resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>api_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – API key for Google Cloud Platform (GCP)</p></li>
<li><p><strong>force_save</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Forces this resource to save, even if errors are present</p></li>
<li><p><strong>json_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Private key for a Google Cloud Platform (GCP) service account within your project.
The account must be at least granted Monitoring Viewer permissions. This key must be in the JSON format generated by GCP.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable name of this integration</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Google Cloud Platform (GCP) Project Id</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value denoting which cloud service this service integrates with</p></li>
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationGcpBilling.additional_tags">
<em class="property">property </em><code class="sig-name descname">additional_tags</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcpBilling.additional_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of point tag key-values to add to every point ingested using this integration</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationGcpBilling.api_key">
<em class="property">property </em><code class="sig-name descname">api_key</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcpBilling.api_key" title="Permalink to this definition">¶</a></dt>
<dd><p>API key for Google Cloud Platform (GCP)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationGcpBilling.force_save">
<em class="property">property </em><code class="sig-name descname">force_save</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcpBilling.force_save" title="Permalink to this definition">¶</a></dt>
<dd><p>Forces this resource to save, even if errors are present</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationGcpBilling.json_key">
<em class="property">property </em><code class="sig-name descname">json_key</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcpBilling.json_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Private key for a Google Cloud Platform (GCP) service account within your project.
The account must be at least granted Monitoring Viewer permissions. This key must be in the JSON format generated by GCP.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationGcpBilling.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcpBilling.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The human-readable name of this integration</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationGcpBilling.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcpBilling.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Google Cloud Platform (GCP) Project Id</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationGcpBilling.service">
<em class="property">property </em><code class="sig-name descname">service</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcpBilling.service" title="Permalink to this definition">¶</a></dt>
<dd><p>A value denoting which cloud service this service integrates with</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationGcpBilling.service_refresh_rate_in_minutes">
<em class="property">property </em><code class="sig-name descname">service_refresh_rate_in_minutes</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationGcpBilling.service_refresh_rate_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>How often, in minutes, to refresh the service</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">CloudIntegrationNewRelic</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_filter_regex</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host_filter_regex</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_filters</span><span class="p">:</span> <span class="n">Union[Sequence[Union[CloudIntegrationNewRelicMetricFilterArgs, Mapping[str, Any], Awaitable[Union[CloudIntegrationNewRelicMetricFilterArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[CloudIntegrationNewRelicMetricFilterArgs, Mapping[str, Any], Awaitable[Union[CloudIntegrationNewRelicMetricFilterArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationNewRelic" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Wavefront Cloud Integration for NewRelic. This allows NewRelic cloud integrations to be created,
updated, and deleted.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_wavefront</span> <span class="k">as</span> <span class="nn">wavefront</span>

<span class="n">newrelic</span> <span class="o">=</span> <span class="n">wavefront</span><span class="o">.</span><span class="n">CloudIntegrationNewRelic</span><span class="p">(</span><span class="s2">&quot;newrelic&quot;</span><span class="p">,</span> <span class="n">api_key</span><span class="o">=</span><span class="s2">&quot;example-api-key&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>NewRelic Integrations can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import wavefront:index/cloudIntegrationNewRelic:CloudIntegrationNewRelic newrelic a411c16b-3cf7-4f03-bf11-8ca05aab898d
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>api_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – NewRelic REST api key</p></li>
<li><p><strong>app_filter_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A regular expression that an application name must match (case-insensitively) iun order to collect metrics</p></li>
<li><p><strong>force_save</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Forces this resource to save, even if errors are present</p></li>
<li><p><strong>host_filter_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A regular expression that a host name must match (case-insensitively) in order to collect metrics</p></li>
<li><p><strong>metric_filters</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'CloudIntegrationNewRelicMetricFilterArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – See Metric Filter</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable name of this integration</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value denoting which cloud service this service integrates with</p></li>
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationNewRelic.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_filter_regex</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host_filter_regex</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_filters</span><span class="p">:</span> <span class="n">Union[Sequence[Union[CloudIntegrationNewRelicMetricFilterArgs, Mapping[str, Any], Awaitable[Union[CloudIntegrationNewRelicMetricFilterArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[CloudIntegrationNewRelicMetricFilterArgs, Mapping[str, Any], Awaitable[Union[CloudIntegrationNewRelicMetricFilterArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_wavefront.cloud_integration_new_relic.CloudIntegrationNewRelic<a class="headerlink" href="#pulumi_wavefront.CloudIntegrationNewRelic.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CloudIntegrationNewRelic resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>api_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – NewRelic REST api key</p></li>
<li><p><strong>app_filter_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A regular expression that an application name must match (case-insensitively) iun order to collect metrics</p></li>
<li><p><strong>force_save</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Forces this resource to save, even if errors are present</p></li>
<li><p><strong>host_filter_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A regular expression that a host name must match (case-insensitively) in order to collect metrics</p></li>
<li><p><strong>metric_filters</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'CloudIntegrationNewRelicMetricFilterArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – See Metric Filter</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable name of this integration</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value denoting which cloud service this service integrates with</p></li>
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationNewRelic.additional_tags">
<em class="property">property </em><code class="sig-name descname">additional_tags</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationNewRelic.additional_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of point tag key-values to add to every point ingested using this integration</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationNewRelic.api_key">
<em class="property">property </em><code class="sig-name descname">api_key</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationNewRelic.api_key" title="Permalink to this definition">¶</a></dt>
<dd><p>NewRelic REST api key</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationNewRelic.app_filter_regex">
<em class="property">property </em><code class="sig-name descname">app_filter_regex</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationNewRelic.app_filter_regex" title="Permalink to this definition">¶</a></dt>
<dd><p>A regular expression that an application name must match (case-insensitively) iun order to collect metrics</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationNewRelic.force_save">
<em class="property">property </em><code class="sig-name descname">force_save</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationNewRelic.force_save" title="Permalink to this definition">¶</a></dt>
<dd><p>Forces this resource to save, even if errors are present</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationNewRelic.host_filter_regex">
<em class="property">property </em><code class="sig-name descname">host_filter_regex</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationNewRelic.host_filter_regex" title="Permalink to this definition">¶</a></dt>
<dd><p>A regular expression that a host name must match (case-insensitively) in order to collect metrics</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationNewRelic.metric_filters">
<em class="property">property </em><code class="sig-name descname">metric_filters</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationNewRelic.metric_filters" title="Permalink to this definition">¶</a></dt>
<dd><p>See Metric Filter</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationNewRelic.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationNewRelic.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The human-readable name of this integration</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationNewRelic.service">
<em class="property">property </em><code class="sig-name descname">service</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationNewRelic.service" title="Permalink to this definition">¶</a></dt>
<dd><p>A value denoting which cloud service this service integrates with</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationNewRelic.service_refresh_rate_in_minutes">
<em class="property">property </em><code class="sig-name descname">service_refresh_rate_in_minutes</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationNewRelic.service_refresh_rate_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>How often, in minutes, to refresh the service</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">CloudIntegrationTesla</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationTesla" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Wavefront Cloud Integration for Tesla. This allows NewRelic cloud integrations to be created,
updated, and deleted.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_wavefront</span> <span class="k">as</span> <span class="nn">wavefront</span>

<span class="n">tesla</span> <span class="o">=</span> <span class="n">wavefront</span><span class="o">.</span><span class="n">CloudIntegrationTesla</span><span class="p">(</span><span class="s2">&quot;tesla&quot;</span><span class="p">,</span>
    <span class="n">email</span><span class="o">=</span><span class="s2">&quot;email@example.com&quot;</span><span class="p">,</span>
    <span class="n">password</span><span class="o">=</span><span class="s2">&quot;password&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Tesla Integrations can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import wavefront:index/cloudIntegrationTesla:CloudIntegrationTesla tesla a411c16b-3cf7-4f03-bf11-8ca05aab898d
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Email address for the Tesla account login</p></li>
<li><p><strong>force_save</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Forces this resource to save, even if errors are present</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable name of this integration</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password for the Tesla account login</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value denoting which cloud service this service integrates with</p></li>
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationTesla.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_tags</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_save</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_refresh_rate_in_minutes</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_wavefront.cloud_integration_tesla.CloudIntegrationTesla<a class="headerlink" href="#pulumi_wavefront.CloudIntegrationTesla.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CloudIntegrationTesla resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>additional_tags</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A list of point tag key-values to add to every point ingested using this integration</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Email address for the Tesla account login</p></li>
<li><p><strong>force_save</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Forces this resource to save, even if errors are present</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The human-readable name of this integration</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Password for the Tesla account login</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value denoting which cloud service this service integrates with</p></li>
<li><p><strong>service_refresh_rate_in_minutes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How often, in minutes, to refresh the service</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationTesla.additional_tags">
<em class="property">property </em><code class="sig-name descname">additional_tags</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationTesla.additional_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of point tag key-values to add to every point ingested using this integration</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationTesla.email">
<em class="property">property </em><code class="sig-name descname">email</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationTesla.email" title="Permalink to this definition">¶</a></dt>
<dd><p>Email address for the Tesla account login</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationTesla.force_save">
<em class="property">property </em><code class="sig-name descname">force_save</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationTesla.force_save" title="Permalink to this definition">¶</a></dt>
<dd><p>Forces this resource to save, even if errors are present</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationTesla.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationTesla.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The human-readable name of this integration</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationTesla.password">
<em class="property">property </em><code class="sig-name descname">password</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationTesla.password" title="Permalink to this definition">¶</a></dt>
<dd><p>Password for the Tesla account login</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationTesla.service">
<em class="property">property </em><code class="sig-name descname">service</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationTesla.service" title="Permalink to this definition">¶</a></dt>
<dd><p>A value denoting which cloud service this service integrates with</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.CloudIntegrationTesla.service_refresh_rate_in_minutes">
<em class="property">property </em><code class="sig-name descname">service_refresh_rate_in_minutes</code><a class="headerlink" href="#pulumi_wavefront.CloudIntegrationTesla.service_refresh_rate_in_minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>How often, in minutes, to refresh the service</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">Dashboard</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">can_modifies</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">can_views</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_query_parameters</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_section_table_of_contents</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">event_filter_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameter_details</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DashboardParameterDetailArgs, Mapping[str, Any], Awaitable[Union[DashboardParameterDetailArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DashboardParameterDetailArgs, Mapping[str, Any], Awaitable[Union[DashboardParameterDetailArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sections</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DashboardSectionArgs, Mapping[str, Any], Awaitable[Union[DashboardSectionArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DashboardSectionArgs, Mapping[str, Any], Awaitable[Union[DashboardSectionArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.Dashboard" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Wavefront Dashboard resource.  This allows dashboards to be created, updated, and deleted.</p>
<p>Dashboards can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import wavefront:index/dashboard:Dashboard dashboard tftestimport
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>can_modifies</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of users that have modify ACL access to the dashboard</p></li>
<li><p><strong>can_views</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of users that have view ACL access to the dashboard</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description of the dashboard</p></li>
<li><p><strong>display_query_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the dashboard parameters section is opened by default when the dashboard
is shown</p></li>
<li><p><strong>display_section_table_of_contents</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the “pills” quick-linked the sections of the dashboard are 
displayed by default when the dashboard is shown</p></li>
<li><p><strong>event_filter_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – How charts belonging to this dashboard should display events. BYCHART is default if 
unspecified; Valid options are: <code class="docutils literal notranslate"><span class="pre">BYCHART</span></code>, <code class="docutils literal notranslate"><span class="pre">AUTOMATIC</span></code>, <code class="docutils literal notranslate"><span class="pre">ALL</span></code>, <code class="docutils literal notranslate"><span class="pre">NONE</span></code>, <code class="docutils literal notranslate"><span class="pre">BYDASHBOARD</span></code>, and <code class="docutils literal notranslate"><span class="pre">BYCHARTANDDASHBOARD</span></code></p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the dashboard</p></li>
<li><p><strong>parameter_details</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DashboardParameterDetailArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – The current JSON representation of dashboard parameters. See parameter details</p></li>
<li><p><strong>sections</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DashboardSectionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Dashboard chart sections. See dashboard sections</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A set of tags to assign to this resource.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier, also URL slug, of the dashboard</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_wavefront.Dashboard.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">can_modifies</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">can_views</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_query_parameters</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_section_table_of_contents</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">event_filter_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameter_details</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DashboardParameterDetailArgs, Mapping[str, Any], Awaitable[Union[DashboardParameterDetailArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DashboardParameterDetailArgs, Mapping[str, Any], Awaitable[Union[DashboardParameterDetailArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sections</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DashboardSectionArgs, Mapping[str, Any], Awaitable[Union[DashboardSectionArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DashboardSectionArgs, Mapping[str, Any], Awaitable[Union[DashboardSectionArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_wavefront.dashboard.Dashboard<a class="headerlink" href="#pulumi_wavefront.Dashboard.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Dashboard resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>can_modifies</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of users that have modify ACL access to the dashboard</p></li>
<li><p><strong>can_views</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of users that have view ACL access to the dashboard</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description of the dashboard</p></li>
<li><p><strong>display_query_parameters</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the dashboard parameters section is opened by default when the dashboard
is shown</p></li>
<li><p><strong>display_section_table_of_contents</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the “pills” quick-linked the sections of the dashboard are 
displayed by default when the dashboard is shown</p></li>
<li><p><strong>event_filter_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – How charts belonging to this dashboard should display events. BYCHART is default if 
unspecified; Valid options are: <code class="docutils literal notranslate"><span class="pre">BYCHART</span></code>, <code class="docutils literal notranslate"><span class="pre">AUTOMATIC</span></code>, <code class="docutils literal notranslate"><span class="pre">ALL</span></code>, <code class="docutils literal notranslate"><span class="pre">NONE</span></code>, <code class="docutils literal notranslate"><span class="pre">BYDASHBOARD</span></code>, and <code class="docutils literal notranslate"><span class="pre">BYCHARTANDDASHBOARD</span></code></p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the dashboard</p></li>
<li><p><strong>parameter_details</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DashboardParameterDetailArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – The current JSON representation of dashboard parameters. See parameter details</p></li>
<li><p><strong>sections</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DashboardSectionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Dashboard chart sections. See dashboard sections</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A set of tags to assign to this resource.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier, also URL slug, of the dashboard</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.Dashboard.can_modifies">
<em class="property">property </em><code class="sig-name descname">can_modifies</code><a class="headerlink" href="#pulumi_wavefront.Dashboard.can_modifies" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of users that have modify ACL access to the dashboard</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.Dashboard.can_views">
<em class="property">property </em><code class="sig-name descname">can_views</code><a class="headerlink" href="#pulumi_wavefront.Dashboard.can_views" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of users that have view ACL access to the dashboard</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.Dashboard.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_wavefront.Dashboard.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Human-readable description of the dashboard</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.Dashboard.display_query_parameters">
<em class="property">property </em><code class="sig-name descname">display_query_parameters</code><a class="headerlink" href="#pulumi_wavefront.Dashboard.display_query_parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the dashboard parameters section is opened by default when the dashboard
is shown</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.Dashboard.display_section_table_of_contents">
<em class="property">property </em><code class="sig-name descname">display_section_table_of_contents</code><a class="headerlink" href="#pulumi_wavefront.Dashboard.display_section_table_of_contents" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the “pills” quick-linked the sections of the dashboard are 
displayed by default when the dashboard is shown</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.Dashboard.event_filter_type">
<em class="property">property </em><code class="sig-name descname">event_filter_type</code><a class="headerlink" href="#pulumi_wavefront.Dashboard.event_filter_type" title="Permalink to this definition">¶</a></dt>
<dd><p>How charts belonging to this dashboard should display events. BYCHART is default if 
unspecified; Valid options are: <code class="docutils literal notranslate"><span class="pre">BYCHART</span></code>, <code class="docutils literal notranslate"><span class="pre">AUTOMATIC</span></code>, <code class="docutils literal notranslate"><span class="pre">ALL</span></code>, <code class="docutils literal notranslate"><span class="pre">NONE</span></code>, <code class="docutils literal notranslate"><span class="pre">BYDASHBOARD</span></code>, and <code class="docutils literal notranslate"><span class="pre">BYCHARTANDDASHBOARD</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.Dashboard.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_wavefront.Dashboard.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the dashboard</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.Dashboard.parameter_details">
<em class="property">property </em><code class="sig-name descname">parameter_details</code><a class="headerlink" href="#pulumi_wavefront.Dashboard.parameter_details" title="Permalink to this definition">¶</a></dt>
<dd><p>The current JSON representation of dashboard parameters. See parameter details</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.Dashboard.sections">
<em class="property">property </em><code class="sig-name descname">sections</code><a class="headerlink" href="#pulumi_wavefront.Dashboard.sections" title="Permalink to this definition">¶</a></dt>
<dd><p>Dashboard chart sections. See dashboard sections</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.Dashboard.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_wavefront.Dashboard.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of tags to assign to this resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.Dashboard.url">
<em class="property">property </em><code class="sig-name descname">url</code><a class="headerlink" href="#pulumi_wavefront.Dashboard.url" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier, also URL slug, of the dashboard</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">DashboardJson</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dashboard_json</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.DashboardJson" title="Permalink to this definition">¶</a></dt>
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
<p>Dashboard JSON can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import wavefront:index/dashboardJson:DashboardJson dashboard_json tftestimport
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
<dl class="py method">
<dt id="pulumi_wavefront.DashboardJson.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dashboard_json</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_wavefront.dashboard_json.DashboardJson<a class="headerlink" href="#pulumi_wavefront.DashboardJson.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DashboardJson resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dashboard_json</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>See <a class="reference external" href="https://docs.wavefront.com/wavefront_api.html#api-documentation-wavefront-instance">Wavefront API Documentation</a> 
for instructions on how to get to your API documentation for more details.</p>
</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.DashboardJson.dashboard_json">
<em class="property">property </em><code class="sig-name descname">dashboard_json</code><a class="headerlink" href="#pulumi_wavefront.DashboardJson.dashboard_json" title="Permalink to this definition">¶</a></dt>
<dd><p>See <a class="reference external" href="https://docs.wavefront.com/wavefront_api.html#api-documentation-wavefront-instance">Wavefront API Documentation</a> 
for instructions on how to get to your API documentation for more details.</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">DerivedMetric</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_information</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">minutes</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.DerivedMetric" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Wavefront Derived Metric Resource. This allows derived metrics to be created,
updated, and deleted.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_wavefront</span> <span class="k">as</span> <span class="nn">wavefront</span>

<span class="n">derived</span> <span class="o">=</span> <span class="n">wavefront</span><span class="o">.</span><span class="n">DerivedMetric</span><span class="p">(</span><span class="s2">&quot;derived&quot;</span><span class="p">,</span>
    <span class="n">minutes</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
    <span class="n">query</span><span class="o">=</span><span class="s2">&quot;aliasMetric(5, &quot;</span><span class="n">some</span><span class="o">.</span><span class="n">metric</span><span class="s2">&quot;)&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Derived Metrics can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import wavefront:index/derivedMetric:DerivedMetric derived_metric <span class="m">1577102900578</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_information</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User-supplied additional explanatory information for the derived metric</p></li>
<li><p><strong>minutes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How frequently the query generating the derived metric is run</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Derived Metric in Wavefront</p></li>
<li><p><strong>query</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A Wavefront query that is evaluated at regular intervals (default <code class="docutils literal notranslate"><span class="pre">1m</span></code>)</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A set of tags to assign to this resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_wavefront.DerivedMetric.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_information</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">minutes</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_wavefront.derived_metric.DerivedMetric<a class="headerlink" href="#pulumi_wavefront.DerivedMetric.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DerivedMetric resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_information</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – User-supplied additional explanatory information for the derived metric</p></li>
<li><p><strong>minutes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How frequently the query generating the derived metric is run</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Derived Metric in Wavefront</p></li>
<li><p><strong>query</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A Wavefront query that is evaluated at regular intervals (default <code class="docutils literal notranslate"><span class="pre">1m</span></code>)</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A set of tags to assign to this resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.DerivedMetric.additional_information">
<em class="property">property </em><code class="sig-name descname">additional_information</code><a class="headerlink" href="#pulumi_wavefront.DerivedMetric.additional_information" title="Permalink to this definition">¶</a></dt>
<dd><p>User-supplied additional explanatory information for the derived metric</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.DerivedMetric.minutes">
<em class="property">property </em><code class="sig-name descname">minutes</code><a class="headerlink" href="#pulumi_wavefront.DerivedMetric.minutes" title="Permalink to this definition">¶</a></dt>
<dd><p>How frequently the query generating the derived metric is run</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.DerivedMetric.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_wavefront.DerivedMetric.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Derived Metric in Wavefront</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.DerivedMetric.query">
<em class="property">property </em><code class="sig-name descname">query</code><a class="headerlink" href="#pulumi_wavefront.DerivedMetric.query" title="Permalink to this definition">¶</a></dt>
<dd><p>A Wavefront query that is evaluated at regular intervals (default <code class="docutils literal notranslate"><span class="pre">1m</span></code>)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.DerivedMetric.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_wavefront.DerivedMetric.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of tags to assign to this resource.</p>
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
<dt id="pulumi_wavefront.ExternalLink">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">ExternalLink</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_log_integration</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_filter_regex</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">point_tag_filter_regexes</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_filter_regex</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.ExternalLink" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Wavefront External Link Resource. This allows external links to be created, updated, and deleted.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_wavefront</span> <span class="k">as</span> <span class="nn">wavefront</span>

<span class="n">basic</span> <span class="o">=</span> <span class="n">wavefront</span><span class="o">.</span><span class="n">ExternalLink</span><span class="p">(</span><span class="s2">&quot;basic&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;An external link description&quot;</span><span class="p">,</span>
    <span class="n">template</span><span class="o">=</span><span class="s2">&quot;https://example.com/source=&#x7B;&#x7B;</span><span class="si">{source}</span><span class="s2">&#x7D;&#x7D;&amp;startTime={{startEpochMillis}}&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Maintenance windows can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import wavefront:index/externalLink:ExternalLink basic fVj6fz6zYC4aBkID
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description for this link</p></li>
<li><p><strong>is_log_integration</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this is a “Log Integration” subType of external link</p></li>
<li><p><strong>metric_filter_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Controls whether a link is displayed in the context menu of a highlighted series. If present, the metric name of the highlighted series must match this regular expression in order for the link to be displayed.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the external link</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>point_tag_filter_regexes</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Controls whether a link is displayed in the context menu of a highlighted series. This is a map from string to regular expression. The highlighted series must contain point tags whose keys are present in the keys of this map and whose values match the regular expressions associated with those keys in order for the link to be displayed</p></li>
<li><p><strong>source_filter_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Controls whether a link is displayed in the context menu of a highlighted series. If present, the source name of the highlighted series must match this regular expression in order for the link to be displayed.</p></li>
<li><p><strong>template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mustache template for this link. The template must expand to a full URL, including scheme, origin, etc.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_wavefront.ExternalLink.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_log_integration</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_filter_regex</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">point_tag_filter_regexes</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_filter_regex</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_wavefront.external_link.ExternalLink<a class="headerlink" href="#pulumi_wavefront.ExternalLink.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ExternalLink resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Human-readable description for this link</p></li>
<li><p><strong>is_log_integration</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this is a “Log Integration” subType of external link</p></li>
<li><p><strong>metric_filter_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Controls whether a link is displayed in the context menu of a highlighted series. If present, the metric name of the highlighted series must match this regular expression in order for the link to be displayed.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the external link</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>point_tag_filter_regexes</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Controls whether a link is displayed in the context menu of a highlighted series. This is a map from string to regular expression. The highlighted series must contain point tags whose keys are present in the keys of this map and whose values match the regular expressions associated with those keys in order for the link to be displayed</p></li>
<li><p><strong>source_filter_regex</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Controls whether a link is displayed in the context menu of a highlighted series. If present, the source name of the highlighted series must match this regular expression in order for the link to be displayed.</p></li>
<li><p><strong>template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mustache template for this link. The template must expand to a full URL, including scheme, origin, etc.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.ExternalLink.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_wavefront.ExternalLink.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Human-readable description for this link</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.ExternalLink.is_log_integration">
<em class="property">property </em><code class="sig-name descname">is_log_integration</code><a class="headerlink" href="#pulumi_wavefront.ExternalLink.is_log_integration" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this is a “Log Integration” subType of external link</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.ExternalLink.metric_filter_regex">
<em class="property">property </em><code class="sig-name descname">metric_filter_regex</code><a class="headerlink" href="#pulumi_wavefront.ExternalLink.metric_filter_regex" title="Permalink to this definition">¶</a></dt>
<dd><p>Controls whether a link is displayed in the context menu of a highlighted series. If present, the metric name of the highlighted series must match this regular expression in order for the link to be displayed.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.ExternalLink.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_wavefront.ExternalLink.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the external link</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.ExternalLink.point_tag_filter_regexes">
<em class="property">property </em><code class="sig-name descname">point_tag_filter_regexes</code><a class="headerlink" href="#pulumi_wavefront.ExternalLink.point_tag_filter_regexes" title="Permalink to this definition">¶</a></dt>
<dd><p>Controls whether a link is displayed in the context menu of a highlighted series. This is a map from string to regular expression. The highlighted series must contain point tags whose keys are present in the keys of this map and whose values match the regular expressions associated with those keys in order for the link to be displayed</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.ExternalLink.source_filter_regex">
<em class="property">property </em><code class="sig-name descname">source_filter_regex</code><a class="headerlink" href="#pulumi_wavefront.ExternalLink.source_filter_regex" title="Permalink to this definition">¶</a></dt>
<dd><p>Controls whether a link is displayed in the context menu of a highlighted series. If present, the source name of the highlighted series must match this regular expression in order for the link to be displayed.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.ExternalLink.template">
<em class="property">property </em><code class="sig-name descname">template</code><a class="headerlink" href="#pulumi_wavefront.ExternalLink.template" title="Permalink to this definition">¶</a></dt>
<dd><p>The mustache template for this link. The template must expand to a full URL, including scheme, origin, etc.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.ExternalLink.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.ExternalLink.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.ExternalLink.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.ExternalLink.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dl class="py method">
<dt id="pulumi_wavefront.GetDefaultUserGroupResult.group_id">
<em class="property">property </em><code class="sig-name descname">group_id</code><a class="headerlink" href="#pulumi_wavefront.GetDefaultUserGroupResult.group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to the Group ID of the <code class="docutils literal notranslate"><span class="pre">Everyone</span></code> group, suitable for referencing
in other resources that support group memberships. s</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.GetDefaultUserGroupResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_wavefront.GetDefaultUserGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_wavefront.MaintenanceWindow">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">MaintenanceWindow</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_time_in_seconds</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host_tag_group_host_names_group_anded</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reason</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">relevant_customer_tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">relevant_host_names</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">relevant_host_tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">relevant_host_tags_anded</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_time_in_seconds</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">title</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.MaintenanceWindow" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Wavefront Maintenance Window Resource. This allows maintenance windows to be created, updated, and deleted.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_wavefront</span> <span class="k">as</span> <span class="nn">wavefront</span>

<span class="n">basic</span> <span class="o">=</span> <span class="n">wavefront</span><span class="o">.</span><span class="n">MaintenanceWindow</span><span class="p">(</span><span class="s2">&quot;basic&quot;</span><span class="p">,</span>
    <span class="n">end_time_in_seconds</span><span class="o">=</span><span class="mi">1601123456</span><span class="p">,</span>
    <span class="n">reason</span><span class="o">=</span><span class="s2">&quot;Routine maintenance for 2020&quot;</span><span class="p">,</span>
    <span class="n">relevant_host_names</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;my_hostname&quot;</span><span class="p">,</span>
        <span class="s2">&quot;my_other_hostname&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">start_time_in_seconds</span><span class="o">=</span><span class="mi">1600123456</span><span class="p">,</span>
    <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Routine maintenance&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Maintenance windows can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import wavefront:index/maintenanceWindow:MaintenanceWindow basic <span class="m">1600383357095</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>end_time_in_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – end time in seconds after 1 Jan 1970 GMT.</p></li>
<li><p><strong>host_tag_group_host_names_group_anded</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, a source/host must be in ‘relevantHostNames’ and have tags matching the specification formed by ‘relevantHostTags’ and ‘relevantHostTagsAnded’ in order for this maintenance window to apply. If false, a source/host must either be in ‘relevantHostNames’ or match ‘relevantHostTags’ and ‘relevantHostTagsAnded’. Default: false</p></li>
<li><p><strong>reason</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The reason for the maintenance window</p></li>
<li><p><strong>relevant_customer_tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of alert tags whose matching alerts will be put into maintenance because of this maintenance window. At least one of relevant_customer_tags, relevant_host_tags, or relevant_host_names is required.</p></li>
<li><p><strong>relevant_host_names</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of source/host names that will be put into maintenance because of this maintenance window. At least one of relevant_customer_tags, relevant_host_tags, or relevant_host_names is required.</p></li>
<li><p><strong>relevant_host_tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of source/host tags whose matching sources/hosts will be put into maintenance because of this maintenance window. At least one of relevant_customer_tags, relevant_host_tags, or relevant_host_names is required.</p></li>
<li><p><strong>relevant_host_tags_anded</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to AND source/host tags listed in relevantHostTags. If true, a source/host must contain all tags in order for the maintenance window to apply. If false, the tags are OR’ed, and a source/host must contain one of the tags. Default: false</p></li>
<li><p><strong>start_time_in_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – start time in seconds after 1 Jan 1970 GMT.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The title of the maintenance window</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_wavefront.MaintenanceWindow.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_time_in_seconds</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host_tag_group_host_names_group_anded</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reason</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">relevant_customer_tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">relevant_host_names</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">relevant_host_tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">relevant_host_tags_anded</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_time_in_seconds</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">title</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_wavefront.maintenance_window.MaintenanceWindow<a class="headerlink" href="#pulumi_wavefront.MaintenanceWindow.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MaintenanceWindow resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>end_time_in_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – end time in seconds after 1 Jan 1970 GMT.</p></li>
<li><p><strong>host_tag_group_host_names_group_anded</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If true, a source/host must be in ‘relevantHostNames’ and have tags matching the specification formed by ‘relevantHostTags’ and ‘relevantHostTagsAnded’ in order for this maintenance window to apply. If false, a source/host must either be in ‘relevantHostNames’ or match ‘relevantHostTags’ and ‘relevantHostTagsAnded’. Default: false</p></li>
<li><p><strong>reason</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The reason for the maintenance window</p></li>
<li><p><strong>relevant_customer_tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of alert tags whose matching alerts will be put into maintenance because of this maintenance window. At least one of relevant_customer_tags, relevant_host_tags, or relevant_host_names is required.</p></li>
<li><p><strong>relevant_host_names</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of source/host names that will be put into maintenance because of this maintenance window. At least one of relevant_customer_tags, relevant_host_tags, or relevant_host_names is required.</p></li>
<li><p><strong>relevant_host_tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of source/host tags whose matching sources/hosts will be put into maintenance because of this maintenance window. At least one of relevant_customer_tags, relevant_host_tags, or relevant_host_names is required.</p></li>
<li><p><strong>relevant_host_tags_anded</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to AND source/host tags listed in relevantHostTags. If true, a source/host must contain all tags in order for the maintenance window to apply. If false, the tags are OR’ed, and a source/host must contain one of the tags. Default: false</p></li>
<li><p><strong>start_time_in_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – start time in seconds after 1 Jan 1970 GMT.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The title of the maintenance window</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.MaintenanceWindow.end_time_in_seconds">
<em class="property">property </em><code class="sig-name descname">end_time_in_seconds</code><a class="headerlink" href="#pulumi_wavefront.MaintenanceWindow.end_time_in_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>end time in seconds after 1 Jan 1970 GMT.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.MaintenanceWindow.host_tag_group_host_names_group_anded">
<em class="property">property </em><code class="sig-name descname">host_tag_group_host_names_group_anded</code><a class="headerlink" href="#pulumi_wavefront.MaintenanceWindow.host_tag_group_host_names_group_anded" title="Permalink to this definition">¶</a></dt>
<dd><p>If true, a source/host must be in ‘relevantHostNames’ and have tags matching the specification formed by ‘relevantHostTags’ and ‘relevantHostTagsAnded’ in order for this maintenance window to apply. If false, a source/host must either be in ‘relevantHostNames’ or match ‘relevantHostTags’ and ‘relevantHostTagsAnded’. Default: false</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.MaintenanceWindow.reason">
<em class="property">property </em><code class="sig-name descname">reason</code><a class="headerlink" href="#pulumi_wavefront.MaintenanceWindow.reason" title="Permalink to this definition">¶</a></dt>
<dd><p>The reason for the maintenance window</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.MaintenanceWindow.relevant_customer_tags">
<em class="property">property </em><code class="sig-name descname">relevant_customer_tags</code><a class="headerlink" href="#pulumi_wavefront.MaintenanceWindow.relevant_customer_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>List of alert tags whose matching alerts will be put into maintenance because of this maintenance window. At least one of relevant_customer_tags, relevant_host_tags, or relevant_host_names is required.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.MaintenanceWindow.relevant_host_names">
<em class="property">property </em><code class="sig-name descname">relevant_host_names</code><a class="headerlink" href="#pulumi_wavefront.MaintenanceWindow.relevant_host_names" title="Permalink to this definition">¶</a></dt>
<dd><p>List of source/host names that will be put into maintenance because of this maintenance window. At least one of relevant_customer_tags, relevant_host_tags, or relevant_host_names is required.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.MaintenanceWindow.relevant_host_tags">
<em class="property">property </em><code class="sig-name descname">relevant_host_tags</code><a class="headerlink" href="#pulumi_wavefront.MaintenanceWindow.relevant_host_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>List of source/host tags whose matching sources/hosts will be put into maintenance because of this maintenance window. At least one of relevant_customer_tags, relevant_host_tags, or relevant_host_names is required.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.MaintenanceWindow.relevant_host_tags_anded">
<em class="property">property </em><code class="sig-name descname">relevant_host_tags_anded</code><a class="headerlink" href="#pulumi_wavefront.MaintenanceWindow.relevant_host_tags_anded" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to AND source/host tags listed in relevantHostTags. If true, a source/host must contain all tags in order for the maintenance window to apply. If false, the tags are OR’ed, and a source/host must contain one of the tags. Default: false</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.MaintenanceWindow.start_time_in_seconds">
<em class="property">property </em><code class="sig-name descname">start_time_in_seconds</code><a class="headerlink" href="#pulumi_wavefront.MaintenanceWindow.start_time_in_seconds" title="Permalink to this definition">¶</a></dt>
<dd><p>start time in seconds after 1 Jan 1970 GMT.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.MaintenanceWindow.title">
<em class="property">property </em><code class="sig-name descname">title</code><a class="headerlink" href="#pulumi_wavefront.MaintenanceWindow.title" title="Permalink to this definition">¶</a></dt>
<dd><p>The title of the maintenance window</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.MaintenanceWindow.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.MaintenanceWindow.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.MaintenanceWindow.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.MaintenanceWindow.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">http_proxy</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.Provider" title="Permalink to this definition">¶</a></dt>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">Role</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">assignees</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.Role" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Wavefront Role Resource. This allows user groups to be created, updated, and deleted.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_wavefront</span> <span class="k">as</span> <span class="nn">wavefront</span>

<span class="n">role</span> <span class="o">=</span> <span class="n">wavefront</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;role&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>User Groups can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import wavefront:index/role:Role some_group a411c16b-3cf7-4f03-bf11-8ca05aab898d
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>assignees</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of user groups or accounts to assign to this role.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A short description of the user group</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user group</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of permissions to assign to this role. Valid options are 
<code class="docutils literal notranslate"><span class="pre">agent_management</span></code>, <code class="docutils literal notranslate"><span class="pre">alerts_management</span></code>, <code class="docutils literal notranslate"><span class="pre">dashboard_management</span></code>, <code class="docutils literal notranslate"><span class="pre">embedded_charts</span></code>, <code class="docutils literal notranslate"><span class="pre">events_management</span></code>, <code class="docutils literal notranslate"><span class="pre">external_links_management</span></code>,
<code class="docutils literal notranslate"><span class="pre">host_tag_management</span></code>, <code class="docutils literal notranslate"><span class="pre">metrics_management</span></code>, <code class="docutils literal notranslate"><span class="pre">user_management</span></code></p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_wavefront.Role.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">assignees</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_wavefront.role.Role<a class="headerlink" href="#pulumi_wavefront.Role.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Role resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>assignees</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of user groups or accounts to assign to this role.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A short description of the user group</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user group</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of permissions to assign to this role. Valid options are 
<code class="docutils literal notranslate"><span class="pre">agent_management</span></code>, <code class="docutils literal notranslate"><span class="pre">alerts_management</span></code>, <code class="docutils literal notranslate"><span class="pre">dashboard_management</span></code>, <code class="docutils literal notranslate"><span class="pre">embedded_charts</span></code>, <code class="docutils literal notranslate"><span class="pre">events_management</span></code>, <code class="docutils literal notranslate"><span class="pre">external_links_management</span></code>,
<code class="docutils literal notranslate"><span class="pre">host_tag_management</span></code>, <code class="docutils literal notranslate"><span class="pre">metrics_management</span></code>, <code class="docutils literal notranslate"><span class="pre">user_management</span></code></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.Role.assignees">
<em class="property">property </em><code class="sig-name descname">assignees</code><a class="headerlink" href="#pulumi_wavefront.Role.assignees" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of user groups or accounts to assign to this role.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.Role.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_wavefront.Role.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A short description of the user group</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.Role.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_wavefront.Role.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the user group</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.Role.permissions">
<em class="property">property </em><code class="sig-name descname">permissions</code><a class="headerlink" href="#pulumi_wavefront.Role.permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of permissions to assign to this role. Valid options are 
<code class="docutils literal notranslate"><span class="pre">agent_management</span></code>, <code class="docutils literal notranslate"><span class="pre">alerts_management</span></code>, <code class="docutils literal notranslate"><span class="pre">dashboard_management</span></code>, <code class="docutils literal notranslate"><span class="pre">embedded_charts</span></code>, <code class="docutils literal notranslate"><span class="pre">events_management</span></code>, <code class="docutils literal notranslate"><span class="pre">external_links_management</span></code>,
<code class="docutils literal notranslate"><span class="pre">host_tag_management</span></code>, <code class="docutils literal notranslate"><span class="pre">metrics_management</span></code>, <code class="docutils literal notranslate"><span class="pre">user_management</span></code></p>
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
<dt id="pulumi_wavefront.ServiceAccount">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">ServiceAccount</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">active</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identifier</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_groups</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.ServiceAccount" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Wavefront Service Account Resource. This allows service accounts to be created, updated, and deleted.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_wavefront</span> <span class="k">as</span> <span class="nn">wavefront</span>

<span class="n">basic</span> <span class="o">=</span> <span class="n">wavefront</span><span class="o">.</span><span class="n">ServiceAccount</span><span class="p">(</span><span class="s2">&quot;basic&quot;</span><span class="p">,</span>
    <span class="n">active</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">identifier</span><span class="o">=</span><span class="s2">&quot;sa::tftesting&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Service accounts can be imported using <code class="docutils literal notranslate"><span class="pre">identifier</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import wavefront:index/serviceAccount:ServiceAccount basic sa::tftesting
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>active</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not the service account is active</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the service account</p></li>
<li><p><strong>identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The (unique) identifier of the service account to create. Must start with sa:</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of permission to grant to this service account.  Valid options are
<code class="docutils literal notranslate"><span class="pre">agent_management</span></code>, <code class="docutils literal notranslate"><span class="pre">alerts_management</span></code>, <code class="docutils literal notranslate"><span class="pre">dashboard_management</span></code>, <code class="docutils literal notranslate"><span class="pre">embedded_charts</span></code>, <code class="docutils literal notranslate"><span class="pre">events_management</span></code>, <code class="docutils literal notranslate"><span class="pre">external_links_management</span></code>,
<code class="docutils literal notranslate"><span class="pre">host_tag_management</span></code>, <code class="docutils literal notranslate"><span class="pre">metrics_management</span></code>, <code class="docutils literal notranslate"><span class="pre">user_management</span></code></p></li>
<li><p><strong>user_groups</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of user groups for this service account</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_wavefront.ServiceAccount.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">active</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">identifier</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_groups</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_wavefront.service_account.ServiceAccount<a class="headerlink" href="#pulumi_wavefront.ServiceAccount.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceAccount resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>active</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not the service account is active</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the service account</p></li>
<li><p><strong>identifier</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The (unique) identifier of the service account to create. Must start with sa:</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of permission to grant to this service account.  Valid options are
<code class="docutils literal notranslate"><span class="pre">agent_management</span></code>, <code class="docutils literal notranslate"><span class="pre">alerts_management</span></code>, <code class="docutils literal notranslate"><span class="pre">dashboard_management</span></code>, <code class="docutils literal notranslate"><span class="pre">embedded_charts</span></code>, <code class="docutils literal notranslate"><span class="pre">events_management</span></code>, <code class="docutils literal notranslate"><span class="pre">external_links_management</span></code>,
<code class="docutils literal notranslate"><span class="pre">host_tag_management</span></code>, <code class="docutils literal notranslate"><span class="pre">metrics_management</span></code>, <code class="docutils literal notranslate"><span class="pre">user_management</span></code></p></li>
<li><p><strong>user_groups</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of user groups for this service account</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.ServiceAccount.active">
<em class="property">property </em><code class="sig-name descname">active</code><a class="headerlink" href="#pulumi_wavefront.ServiceAccount.active" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not the service account is active</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.ServiceAccount.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_wavefront.ServiceAccount.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the service account</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.ServiceAccount.identifier">
<em class="property">property </em><code class="sig-name descname">identifier</code><a class="headerlink" href="#pulumi_wavefront.ServiceAccount.identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The (unique) identifier of the service account to create. Must start with sa:</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.ServiceAccount.permissions">
<em class="property">property </em><code class="sig-name descname">permissions</code><a class="headerlink" href="#pulumi_wavefront.ServiceAccount.permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>List of permission to grant to this service account.  Valid options are
<code class="docutils literal notranslate"><span class="pre">agent_management</span></code>, <code class="docutils literal notranslate"><span class="pre">alerts_management</span></code>, <code class="docutils literal notranslate"><span class="pre">dashboard_management</span></code>, <code class="docutils literal notranslate"><span class="pre">embedded_charts</span></code>, <code class="docutils literal notranslate"><span class="pre">events_management</span></code>, <code class="docutils literal notranslate"><span class="pre">external_links_management</span></code>,
<code class="docutils literal notranslate"><span class="pre">host_tag_management</span></code>, <code class="docutils literal notranslate"><span class="pre">metrics_management</span></code>, <code class="docutils literal notranslate"><span class="pre">user_management</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.ServiceAccount.user_groups">
<em class="property">property </em><code class="sig-name descname">user_groups</code><a class="headerlink" href="#pulumi_wavefront.ServiceAccount.user_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>List of user groups for this service account</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.ServiceAccount.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.ServiceAccount.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_wavefront.ServiceAccount.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.ServiceAccount.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">User</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">customer</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_groups</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.User" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Wavefront User Resource. This allows users to be created, updated, and deleted.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_wavefront</span> <span class="k">as</span> <span class="nn">wavefront</span>

<span class="n">basic</span> <span class="o">=</span> <span class="n">wavefront</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;basic&quot;</span><span class="p">,</span> <span class="n">email</span><span class="o">=</span><span class="s2">&quot;test+tftesting@example.com&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Users can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import wavefront:index/user:User some_user test@example.com
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The (unique) identifier of the user to create. Must be a valid email address</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of permission to grant to this user.  Valid options are
<code class="docutils literal notranslate"><span class="pre">agent_management</span></code>, <code class="docutils literal notranslate"><span class="pre">alerts_management</span></code>, <code class="docutils literal notranslate"><span class="pre">dashboard_management</span></code>, <code class="docutils literal notranslate"><span class="pre">embedded_charts</span></code>, <code class="docutils literal notranslate"><span class="pre">events_management</span></code>, <code class="docutils literal notranslate"><span class="pre">external_links_management</span></code>,
<code class="docutils literal notranslate"><span class="pre">host_tag_management</span></code>, <code class="docutils literal notranslate"><span class="pre">metrics_management</span></code>, <code class="docutils literal notranslate"><span class="pre">user_management</span></code></p></li>
<li><p><strong>user_groups</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of user groups to this user</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_wavefront.User.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">customer</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_groups</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_wavefront.user.User<a class="headerlink" href="#pulumi_wavefront.User.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing User resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The (unique) identifier of the user to create. Must be a valid email address</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of permission to grant to this user.  Valid options are
<code class="docutils literal notranslate"><span class="pre">agent_management</span></code>, <code class="docutils literal notranslate"><span class="pre">alerts_management</span></code>, <code class="docutils literal notranslate"><span class="pre">dashboard_management</span></code>, <code class="docutils literal notranslate"><span class="pre">embedded_charts</span></code>, <code class="docutils literal notranslate"><span class="pre">events_management</span></code>, <code class="docutils literal notranslate"><span class="pre">external_links_management</span></code>,
<code class="docutils literal notranslate"><span class="pre">host_tag_management</span></code>, <code class="docutils literal notranslate"><span class="pre">metrics_management</span></code>, <code class="docutils literal notranslate"><span class="pre">user_management</span></code></p></li>
<li><p><strong>user_groups</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of user groups to this user</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.User.email">
<em class="property">property </em><code class="sig-name descname">email</code><a class="headerlink" href="#pulumi_wavefront.User.email" title="Permalink to this definition">¶</a></dt>
<dd><p>The (unique) identifier of the user to create. Must be a valid email address</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.User.permissions">
<em class="property">property </em><code class="sig-name descname">permissions</code><a class="headerlink" href="#pulumi_wavefront.User.permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>List of permission to grant to this user.  Valid options are
<code class="docutils literal notranslate"><span class="pre">agent_management</span></code>, <code class="docutils literal notranslate"><span class="pre">alerts_management</span></code>, <code class="docutils literal notranslate"><span class="pre">dashboard_management</span></code>, <code class="docutils literal notranslate"><span class="pre">embedded_charts</span></code>, <code class="docutils literal notranslate"><span class="pre">events_management</span></code>, <code class="docutils literal notranslate"><span class="pre">external_links_management</span></code>,
<code class="docutils literal notranslate"><span class="pre">host_tag_management</span></code>, <code class="docutils literal notranslate"><span class="pre">metrics_management</span></code>, <code class="docutils literal notranslate"><span class="pre">user_management</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.User.user_groups">
<em class="property">property </em><code class="sig-name descname">user_groups</code><a class="headerlink" href="#pulumi_wavefront.User.user_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>List of user groups to this user</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">UserGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_wavefront.UserGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Wavefront User Group Resource. This allows user groups to be created, updated, and deleted.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_wavefront</span> <span class="k">as</span> <span class="nn">wavefront</span>

<span class="n">basic</span> <span class="o">=</span> <span class="n">wavefront</span><span class="o">.</span><span class="n">UserGroup</span><span class="p">(</span><span class="s2">&quot;basic&quot;</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Basic User Group for Unit Tests&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>User Groups can be imported using the <code class="docutils literal notranslate"><span class="pre">id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import wavefront:index/userGroup:UserGroup some_group a411c16b-3cf7-4f03-bf11-8ca05aab898d
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
<dl class="py method">
<dt id="pulumi_wavefront.UserGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_wavefront.user_group.UserGroup<a class="headerlink" href="#pulumi_wavefront.UserGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UserGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A short description of the user group</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user group</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.UserGroup.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_wavefront.UserGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A short description of the user group</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_wavefront.UserGroup.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_wavefront.UserGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the user group</p>
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
<code class="sig-prename descclassname">pulumi_wavefront.</code><code class="sig-name descname">get_default_user_group</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_wavefront.get_default_user_group.AwaitableGetDefaultUserGroupResult<a class="headerlink" href="#pulumi_wavefront.get_default_user_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get the Group ID of the <code class="docutils literal notranslate"><span class="pre">Everyone</span></code> group in Wavefront.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_wavefront</span> <span class="k">as</span> <span class="nn">wavefront</span>

<span class="n">everyone_group</span> <span class="o">=</span> <span class="n">wavefront</span><span class="o">.</span><span class="n">get_default_user_group</span><span class="p">()</span>
</pre></div>
</div>
</dd></dl>

</div>
