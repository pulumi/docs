---
title: Package pulumi_signalfx
title_tag: Package pulumi_signalfx | Python SDK
linktitle: pulumi_signalfx
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "signalfx" >}}

<div class="section" id="pulumi-signalfx">
<h1>Pulumi SignalFX<a class="headerlink" href="#pulumi-signalfx" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-signalfx">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-signalfx/issues">pulumi/pulumi-signalfx repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-signalfx/issues">terraform-providers/terraform-provider-signalfx repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_signalfx"></span><dl class="py class">
<dt id="pulumi_signalfx.AlertMutingRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_signalfx.</code><code class="sig-name descname">AlertMutingRule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">detectors</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="p">:</span> <span class="n">Union[Sequence[Union[AlertMutingRuleFilterArgs, Mapping[str, Any], Awaitable[Union[AlertMutingRuleFilterArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[AlertMutingRuleFilterArgs, Mapping[str, Any], Awaitable[Union[AlertMutingRuleFilterArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_time</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stop_time</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.AlertMutingRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a SignalFx resource for managing alert muting rules. See <a class="reference external" href="https://docs.signalfx.com/en/latest/detect-alert/mute-notifications.html">Mute Notifications</a> for more information.</p>
<blockquote>
<div><p><strong>WARNING</strong> SignalFx does not allow the start time of a <strong>currently active</strong> muting rule to be modified. As such, attempting to modify a currently active rule will destroy the existing rule and create a new rule. This may result in the emission of notifications.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_signalfx</span> <span class="k">as</span> <span class="nn">signalfx</span>

<span class="n">rool_mooter_one</span> <span class="o">=</span> <span class="n">signalfx</span><span class="o">.</span><span class="n">AlertMutingRule</span><span class="p">(</span><span class="s2">&quot;roolMooterOne&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;mooted it NEW&quot;</span><span class="p">,</span>
    <span class="n">start_time</span><span class="o">=</span><span class="mi">1573063243</span><span class="p">,</span>
    <span class="n">stop_time</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
    <span class="n">detectors</span><span class="o">=</span><span class="p">[</span><span class="n">signalfx_detector</span><span class="p">[</span><span class="s2">&quot;some_detector_id&quot;</span><span class="p">]],</span>
    <span class="n">filters</span><span class="o">=</span><span class="p">[</span><span class="n">signalfx</span><span class="o">.</span><span class="n">AlertMutingRuleFilterArgs</span><span class="p">(</span>
        <span class="nb">property</span><span class="o">=</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
        <span class="n">property_value</span><span class="o">=</span><span class="s2">&quot;bar&quot;</span><span class="p">,</span>
    <span class="p">)])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description for this muting rule</p></li>
<li><p><strong>detectors</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A convenience attribute that associated this muting rule with specific detector ids.</p></li>
<li><p><strong>filters</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AlertMutingRuleFilterArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Filters for this rule. See <a class="reference external" href="https://docs.signalfx.com/en/latest/detect-alert/mute-notifications.html#rule-from-scratch">Creating muting rules from scratch</a> for more information.</p></li>
<li><p><strong>start_time</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Starting time of an alert muting rule as a Unit time stamp in seconds.</p></li>
<li><p><strong>stop_time</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Starting time of an alert muting rule as a Unix time stamp in seconds.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_signalfx.AlertMutingRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">detectors</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">effective_start_time</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="p">:</span> <span class="n">Union[Sequence[Union[AlertMutingRuleFilterArgs, Mapping[str, Any], Awaitable[Union[AlertMutingRuleFilterArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[AlertMutingRuleFilterArgs, Mapping[str, Any], Awaitable[Union[AlertMutingRuleFilterArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_time</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stop_time</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_signalfx.alert_muting_rule.AlertMutingRule<a class="headerlink" href="#pulumi_signalfx.AlertMutingRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AlertMutingRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description for this muting rule</p></li>
<li><p><strong>detectors</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A convenience attribute that associated this muting rule with specific detector ids.</p></li>
<li><p><strong>filters</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AlertMutingRuleFilterArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – <p>Filters for this rule. See <a class="reference external" href="https://docs.signalfx.com/en/latest/detect-alert/mute-notifications.html#rule-from-scratch">Creating muting rules from scratch</a> for more information.</p>
</p></li>
<li><p><strong>start_time</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Starting time of an alert muting rule as a Unit time stamp in seconds.</p></li>
<li><p><strong>stop_time</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Starting time of an alert muting rule as a Unix time stamp in seconds.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.AlertMutingRule.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_signalfx.AlertMutingRule.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description for this muting rule</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.AlertMutingRule.detectors">
<em class="property">property </em><code class="sig-name descname">detectors</code><a class="headerlink" href="#pulumi_signalfx.AlertMutingRule.detectors" title="Permalink to this definition">¶</a></dt>
<dd><p>A convenience attribute that associated this muting rule with specific detector ids.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.AlertMutingRule.filters">
<em class="property">property </em><code class="sig-name descname">filters</code><a class="headerlink" href="#pulumi_signalfx.AlertMutingRule.filters" title="Permalink to this definition">¶</a></dt>
<dd><p>Filters for this rule. See <a class="reference external" href="https://docs.signalfx.com/en/latest/detect-alert/mute-notifications.html#rule-from-scratch">Creating muting rules from scratch</a> for more information.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.AlertMutingRule.start_time">
<em class="property">property </em><code class="sig-name descname">start_time</code><a class="headerlink" href="#pulumi_signalfx.AlertMutingRule.start_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Starting time of an alert muting rule as a Unit time stamp in seconds.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.AlertMutingRule.stop_time">
<em class="property">property </em><code class="sig-name descname">stop_time</code><a class="headerlink" href="#pulumi_signalfx.AlertMutingRule.stop_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Starting time of an alert muting rule as a Unix time stamp in seconds.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.AlertMutingRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.AlertMutingRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.AlertMutingRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.AlertMutingRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.AwaitableGetAwsServicesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_signalfx.</code><code class="sig-name descname">AwaitableGetAwsServicesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">services</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.AwaitableGetAwsServicesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_signalfx.AwaitableGetAzureServicesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_signalfx.</code><code class="sig-name descname">AwaitableGetAzureServicesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">services</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.AwaitableGetAzureServicesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_signalfx.AwaitableGetDimensionValuesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_signalfx.</code><code class="sig-name descname">AwaitableGetDimensionValuesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">values</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.AwaitableGetDimensionValuesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_signalfx.Dashboard">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_signalfx.</code><code class="sig-name descname">Dashboard</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorized_writer_teams</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorized_writer_users</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">charts</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DashboardChartArgs, Mapping[str, Any], Awaitable[Union[DashboardChartArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DashboardChartArgs, Mapping[str, Any], Awaitable[Union[DashboardChartArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">charts_resolution</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">columns</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DashboardColumnArgs, Mapping[str, Any], Awaitable[Union[DashboardColumnArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DashboardColumnArgs, Mapping[str, Any], Awaitable[Union[DashboardColumnArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dashboard_group</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">discovery_options_query</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">discovery_options_selectors</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_time</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">event_overlays</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DashboardEventOverlayArgs, Mapping[str, Any], Awaitable[Union[DashboardEventOverlayArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DashboardEventOverlayArgs, Mapping[str, Any], Awaitable[Union[DashboardEventOverlayArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DashboardFilterArgs, Mapping[str, Any], Awaitable[Union[DashboardFilterArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DashboardFilterArgs, Mapping[str, Any], Awaitable[Union[DashboardFilterArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grids</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DashboardGridArgs, Mapping[str, Any], Awaitable[Union[DashboardGridArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DashboardGridArgs, Mapping[str, Any], Awaitable[Union[DashboardGridArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">selected_event_overlays</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DashboardSelectedEventOverlayArgs, Mapping[str, Any], Awaitable[Union[DashboardSelectedEventOverlayArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DashboardSelectedEventOverlayArgs, Mapping[str, Any], Awaitable[Union[DashboardSelectedEventOverlayArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_time</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_range</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">variables</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DashboardVariableArgs, Mapping[str, Any], Awaitable[Union[DashboardVariableArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DashboardVariableArgs, Mapping[str, Any], Awaitable[Union[DashboardVariableArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.Dashboard" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Dashboard resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[Sequence[pulumi.Input[str]]] authorized_writer_teams: Team IDs that have write access to this dashboard group. Remember to use an admin’s token if using this feature and to include that admin’s team (or user id in <code class="docutils literal notranslate"><span class="pre">authorized_writer_teams</span></code>).
:param pulumi.Input[Sequence[pulumi.Input[str]]] authorized_writer_users: User IDs that have write access to this dashboard group. Remember to use an admin’s token if using this feature and to include that admin’s user id (or team id in <code class="docutils literal notranslate"><span class="pre">authorized_writer_teams</span></code>).
:param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType[‘DashboardChartArgs’]]]] charts: Chart ID and layout information for the charts in the dashboard.
:param pulumi.Input[str] charts_resolution: Specifies the chart data display resolution for charts in this dashboard. Value can be one of <code class="docutils literal notranslate"><span class="pre">&quot;default&quot;</span></code>,  <code class="docutils literal notranslate"><span class="pre">&quot;low&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;high&quot;</span></code>, or  <code class="docutils literal notranslate"><span class="pre">&quot;highest&quot;</span></code>.
:param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType[‘DashboardColumnArgs’]]]] columns: Column number for the layout.
:param pulumi.Input[str] dashboard_group: The ID of the dashboard group that contains the dashboard.
:param pulumi.Input[str] description: Variable description.
:param pulumi.Input[int] end_time: Seconds since epoch. Used for visualization.
:param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType[‘DashboardEventOverlayArgs’]]]] event_overlays: Specify a list of event overlays to include in the dashboard. Note: These overlays correspond to the <em>suggested</em> event overlays specified in the web UI, and they’re not automatically applied as active overlays. To set default active event overlays, use the <code class="docutils literal notranslate"><span class="pre">selected_event_overlay</span></code> property instead.
:param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType[‘DashboardFilterArgs’]]]] filters: Filter to apply to the charts when displaying the dashboard.
:param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType[‘DashboardGridArgs’]]]] grids: Grid dashboard layout. Charts listed will be placed in a grid by row with the same width and height. If a chart cannot fit in a row, it will be placed automatically in the next row.
:param pulumi.Input[str] name: Name of the dashboard.
:param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType[‘DashboardSelectedEventOverlayArgs’]]]] selected_event_overlays: Defines event overlays which are enabled by <strong>default</strong>. Any overlay specified here should have an accompanying entry in <code class="docutils literal notranslate"><span class="pre">event_overlay</span></code>, which are similar to the properties here.
:param pulumi.Input[int] start_time: Seconds since epoch. Used for visualization.
:param pulumi.Input[str] time_range: The time range prior to now to visualize. SignalFx time syntax (e.g. <code class="docutils literal notranslate"><span class="pre">&quot;-5m&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;-1h&quot;</span></code>).
:param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType[‘DashboardVariableArgs’]]]] variables: Dashboard variable to apply to each chart in the dashboard.</p>
<dl class="py method">
<dt id="pulumi_signalfx.Dashboard.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorized_writer_teams</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorized_writer_users</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">charts</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DashboardChartArgs, Mapping[str, Any], Awaitable[Union[DashboardChartArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DashboardChartArgs, Mapping[str, Any], Awaitable[Union[DashboardChartArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">charts_resolution</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">columns</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DashboardColumnArgs, Mapping[str, Any], Awaitable[Union[DashboardColumnArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DashboardColumnArgs, Mapping[str, Any], Awaitable[Union[DashboardColumnArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dashboard_group</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">discovery_options_query</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">discovery_options_selectors</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_time</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">event_overlays</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DashboardEventOverlayArgs, Mapping[str, Any], Awaitable[Union[DashboardEventOverlayArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DashboardEventOverlayArgs, Mapping[str, Any], Awaitable[Union[DashboardEventOverlayArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DashboardFilterArgs, Mapping[str, Any], Awaitable[Union[DashboardFilterArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DashboardFilterArgs, Mapping[str, Any], Awaitable[Union[DashboardFilterArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">grids</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DashboardGridArgs, Mapping[str, Any], Awaitable[Union[DashboardGridArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DashboardGridArgs, Mapping[str, Any], Awaitable[Union[DashboardGridArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">selected_event_overlays</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DashboardSelectedEventOverlayArgs, Mapping[str, Any], Awaitable[Union[DashboardSelectedEventOverlayArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DashboardSelectedEventOverlayArgs, Mapping[str, Any], Awaitable[Union[DashboardSelectedEventOverlayArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_time</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_range</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">variables</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DashboardVariableArgs, Mapping[str, Any], Awaitable[Union[DashboardVariableArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DashboardVariableArgs, Mapping[str, Any], Awaitable[Union[DashboardVariableArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_signalfx.dashboard.Dashboard<a class="headerlink" href="#pulumi_signalfx.Dashboard.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Dashboard resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>authorized_writer_teams</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Team IDs that have write access to this dashboard group. Remember to use an admin’s token if using this feature and to include that admin’s team (or user id in <code class="docutils literal notranslate"><span class="pre">authorized_writer_teams</span></code>).</p></li>
<li><p><strong>authorized_writer_users</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – User IDs that have write access to this dashboard group. Remember to use an admin’s token if using this feature and to include that admin’s user id (or team id in <code class="docutils literal notranslate"><span class="pre">authorized_writer_teams</span></code>).</p></li>
<li><p><strong>charts</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DashboardChartArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Chart ID and layout information for the charts in the dashboard.</p></li>
<li><p><strong>charts_resolution</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the chart data display resolution for charts in this dashboard. Value can be one of <code class="docutils literal notranslate"><span class="pre">&quot;default&quot;</span></code>,  <code class="docutils literal notranslate"><span class="pre">&quot;low&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;high&quot;</span></code>, or  <code class="docutils literal notranslate"><span class="pre">&quot;highest&quot;</span></code>.</p></li>
<li><p><strong>columns</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DashboardColumnArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Column number for the layout.</p></li>
<li><p><strong>dashboard_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the dashboard group that contains the dashboard.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Variable description.</p></li>
<li><p><strong>end_time</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Seconds since epoch. Used for visualization.</p></li>
<li><p><strong>event_overlays</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DashboardEventOverlayArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Specify a list of event overlays to include in the dashboard. Note: These overlays correspond to the <em>suggested</em> event overlays specified in the web UI, and they’re not automatically applied as active overlays. To set default active event overlays, use the <code class="docutils literal notranslate"><span class="pre">selected_event_overlay</span></code> property instead.</p></li>
<li><p><strong>filters</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DashboardFilterArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Filter to apply to the charts when displaying the dashboard.</p></li>
<li><p><strong>grids</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DashboardGridArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Grid dashboard layout. Charts listed will be placed in a grid by row with the same width and height. If a chart cannot fit in a row, it will be placed automatically in the next row.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the dashboard.</p></li>
<li><p><strong>selected_event_overlays</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DashboardSelectedEventOverlayArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Defines event overlays which are enabled by <strong>default</strong>. Any overlay specified here should have an accompanying entry in <code class="docutils literal notranslate"><span class="pre">event_overlay</span></code>, which are similar to the properties here.</p></li>
<li><p><strong>start_time</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Seconds since epoch. Used for visualization.</p></li>
<li><p><strong>time_range</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time range prior to now to visualize. SignalFx time syntax (e.g. <code class="docutils literal notranslate"><span class="pre">&quot;-5m&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;-1h&quot;</span></code>).</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the dashboard.</p></li>
<li><p><strong>variables</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DashboardVariableArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Dashboard variable to apply to each chart in the dashboard.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Dashboard.authorized_writer_teams">
<em class="property">property </em><code class="sig-name descname">authorized_writer_teams</code><a class="headerlink" href="#pulumi_signalfx.Dashboard.authorized_writer_teams" title="Permalink to this definition">¶</a></dt>
<dd><p>Team IDs that have write access to this dashboard group. Remember to use an admin’s token if using this feature and to include that admin’s team (or user id in <code class="docutils literal notranslate"><span class="pre">authorized_writer_teams</span></code>).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Dashboard.authorized_writer_users">
<em class="property">property </em><code class="sig-name descname">authorized_writer_users</code><a class="headerlink" href="#pulumi_signalfx.Dashboard.authorized_writer_users" title="Permalink to this definition">¶</a></dt>
<dd><p>User IDs that have write access to this dashboard group. Remember to use an admin’s token if using this feature and to include that admin’s user id (or team id in <code class="docutils literal notranslate"><span class="pre">authorized_writer_teams</span></code>).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Dashboard.charts">
<em class="property">property </em><code class="sig-name descname">charts</code><a class="headerlink" href="#pulumi_signalfx.Dashboard.charts" title="Permalink to this definition">¶</a></dt>
<dd><p>Chart ID and layout information for the charts in the dashboard.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Dashboard.charts_resolution">
<em class="property">property </em><code class="sig-name descname">charts_resolution</code><a class="headerlink" href="#pulumi_signalfx.Dashboard.charts_resolution" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the chart data display resolution for charts in this dashboard. Value can be one of <code class="docutils literal notranslate"><span class="pre">&quot;default&quot;</span></code>,  <code class="docutils literal notranslate"><span class="pre">&quot;low&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;high&quot;</span></code>, or  <code class="docutils literal notranslate"><span class="pre">&quot;highest&quot;</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Dashboard.columns">
<em class="property">property </em><code class="sig-name descname">columns</code><a class="headerlink" href="#pulumi_signalfx.Dashboard.columns" title="Permalink to this definition">¶</a></dt>
<dd><p>Column number for the layout.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Dashboard.dashboard_group">
<em class="property">property </em><code class="sig-name descname">dashboard_group</code><a class="headerlink" href="#pulumi_signalfx.Dashboard.dashboard_group" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the dashboard group that contains the dashboard.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Dashboard.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_signalfx.Dashboard.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Variable description.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Dashboard.end_time">
<em class="property">property </em><code class="sig-name descname">end_time</code><a class="headerlink" href="#pulumi_signalfx.Dashboard.end_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Seconds since epoch. Used for visualization.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Dashboard.event_overlays">
<em class="property">property </em><code class="sig-name descname">event_overlays</code><a class="headerlink" href="#pulumi_signalfx.Dashboard.event_overlays" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify a list of event overlays to include in the dashboard. Note: These overlays correspond to the <em>suggested</em> event overlays specified in the web UI, and they’re not automatically applied as active overlays. To set default active event overlays, use the <code class="docutils literal notranslate"><span class="pre">selected_event_overlay</span></code> property instead.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Dashboard.filters">
<em class="property">property </em><code class="sig-name descname">filters</code><a class="headerlink" href="#pulumi_signalfx.Dashboard.filters" title="Permalink to this definition">¶</a></dt>
<dd><p>Filter to apply to the charts when displaying the dashboard.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Dashboard.grids">
<em class="property">property </em><code class="sig-name descname">grids</code><a class="headerlink" href="#pulumi_signalfx.Dashboard.grids" title="Permalink to this definition">¶</a></dt>
<dd><p>Grid dashboard layout. Charts listed will be placed in a grid by row with the same width and height. If a chart cannot fit in a row, it will be placed automatically in the next row.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Dashboard.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_signalfx.Dashboard.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the dashboard.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Dashboard.selected_event_overlays">
<em class="property">property </em><code class="sig-name descname">selected_event_overlays</code><a class="headerlink" href="#pulumi_signalfx.Dashboard.selected_event_overlays" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines event overlays which are enabled by <strong>default</strong>. Any overlay specified here should have an accompanying entry in <code class="docutils literal notranslate"><span class="pre">event_overlay</span></code>, which are similar to the properties here.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Dashboard.start_time">
<em class="property">property </em><code class="sig-name descname">start_time</code><a class="headerlink" href="#pulumi_signalfx.Dashboard.start_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Seconds since epoch. Used for visualization.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Dashboard.time_range">
<em class="property">property </em><code class="sig-name descname">time_range</code><a class="headerlink" href="#pulumi_signalfx.Dashboard.time_range" title="Permalink to this definition">¶</a></dt>
<dd><p>The time range prior to now to visualize. SignalFx time syntax (e.g. <code class="docutils literal notranslate"><span class="pre">&quot;-5m&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;-1h&quot;</span></code>).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Dashboard.url">
<em class="property">property </em><code class="sig-name descname">url</code><a class="headerlink" href="#pulumi_signalfx.Dashboard.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the dashboard.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Dashboard.variables">
<em class="property">property </em><code class="sig-name descname">variables</code><a class="headerlink" href="#pulumi_signalfx.Dashboard.variables" title="Permalink to this definition">¶</a></dt>
<dd><p>Dashboard variable to apply to each chart in the dashboard.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Dashboard.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.Dashboard.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.Dashboard.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.Dashboard.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.DashboardGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_signalfx.</code><code class="sig-name descname">DashboardGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorized_writer_teams</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorized_writer_users</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dashboards</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DashboardGroupDashboardArgs, Mapping[str, Any], Awaitable[Union[DashboardGroupDashboardArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DashboardGroupDashboardArgs, Mapping[str, Any], Awaitable[Union[DashboardGroupDashboardArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">import_qualifiers</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DashboardGroupImportQualifierArgs, Mapping[str, Any], Awaitable[Union[DashboardGroupImportQualifierArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DashboardGroupImportQualifierArgs, Mapping[str, Any], Awaitable[Union[DashboardGroupImportQualifierArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">teams</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.DashboardGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>In the SignalFx web UI, a <a class="reference external" href="https://developers.signalfx.com/dashboard_groups_reference.html">dashboard group</a> is a collection of dashboards.</p>
<blockquote>
<div><p><strong>NOTE</strong> Dashboard groups cannot be accessed directly, but just via a dashboard contained in them. This is the reason why make show won’t show any of yours dashboard groups.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_signalfx</span> <span class="k">as</span> <span class="nn">signalfx</span>

<span class="n">mydashboardgroup0</span> <span class="o">=</span> <span class="n">signalfx</span><span class="o">.</span><span class="n">DashboardGroup</span><span class="p">(</span><span class="s2">&quot;mydashboardgroup0&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Cool dashboard group&quot;</span><span class="p">,</span>
    <span class="n">authorized_writer_teams</span><span class="o">=</span><span class="p">[</span><span class="n">signalfx_team</span><span class="p">[</span><span class="s2">&quot;mycoolteam&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">]],</span>
    <span class="n">authorized_writer_users</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;abc123&quot;</span><span class="p">])</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_signalfx</span> <span class="k">as</span> <span class="nn">signalfx</span>

<span class="n">mydashboardgroup_withmirrors</span> <span class="o">=</span> <span class="n">signalfx</span><span class="o">.</span><span class="n">DashboardGroup</span><span class="p">(</span><span class="s2">&quot;mydashboardgroupWithmirrors&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Cool dashboard group&quot;</span><span class="p">,</span>
    <span class="n">dashboards</span><span class="o">=</span><span class="p">[</span><span class="n">signalfx</span><span class="o">.</span><span class="n">DashboardGroupDashboardArgs</span><span class="p">(</span>
        <span class="n">dashboard_id</span><span class="o">=</span><span class="n">signalfx_dashboard</span><span class="p">[</span><span class="s2">&quot;gc_dashboard&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
        <span class="n">name_override</span><span class="o">=</span><span class="s2">&quot;GC For My Service&quot;</span><span class="p">,</span>
        <span class="n">description_override</span><span class="o">=</span><span class="s2">&quot;Garbage Collection dashboard maintained by JVM team&quot;</span><span class="p">,</span>
        <span class="n">filter_overrides</span><span class="o">=</span><span class="p">[</span><span class="n">signalfx</span><span class="o">.</span><span class="n">DashboardGroupDashboardFilterOverrideArgs</span><span class="p">(</span>
            <span class="nb">property</span><span class="o">=</span><span class="s2">&quot;service&quot;</span><span class="p">,</span>
            <span class="n">values</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;myservice&quot;</span><span class="p">],</span>
            <span class="n">negated</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
        <span class="p">)],</span>
        <span class="n">variable_overrides</span><span class="o">=</span><span class="p">[</span><span class="n">signalfx</span><span class="o">.</span><span class="n">DashboardGroupDashboardVariableOverrideArgs</span><span class="p">(</span>
            <span class="nb">property</span><span class="o">=</span><span class="s2">&quot;region&quot;</span><span class="p">,</span>
            <span class="n">values</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;us-west1&quot;</span><span class="p">],</span>
            <span class="n">values_suggesteds</span><span class="o">=</span><span class="p">[</span>
                <span class="s2">&quot;us-west-1&quot;</span><span class="p">,</span>
                <span class="s2">&quot;us-east-1&quot;</span><span class="p">,</span>
            <span class="p">],</span>
        <span class="p">)],</span>
    <span class="p">)])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>authorized_writer_teams</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Team IDs that have write access to this dashboard group. Remember to use an admin’s token if using this feature and to include that admin’s team (or user id in <code class="docutils literal notranslate"><span class="pre">authorized_writer_teams</span></code>).</p></li>
<li><p><strong>authorized_writer_users</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – User IDs that have write access to this dashboard group. Remember to use an admin’s token if using this feature and to include that admin’s user id (or team id in <code class="docutils literal notranslate"><span class="pre">authorized_writer_teams</span></code>).</p></li>
<li><p><strong>dashboards</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DashboardGroupDashboardArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – <a class="reference external" href="https://docs.signalfx.com/en/latest/dashboards/dashboard-mirrors.html">Mirrored dashboards</a> in this dashboard group. <strong>Note:</strong> This feature is not present in all accounts. Please contact support if you are unsure.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the dashboard group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the dashboard group.</p></li>
<li><p><strong>teams</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Team IDs to associate the dashboard group to.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_signalfx.DashboardGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorized_writer_teams</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorized_writer_users</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dashboards</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DashboardGroupDashboardArgs, Mapping[str, Any], Awaitable[Union[DashboardGroupDashboardArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DashboardGroupDashboardArgs, Mapping[str, Any], Awaitable[Union[DashboardGroupDashboardArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">import_qualifiers</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DashboardGroupImportQualifierArgs, Mapping[str, Any], Awaitable[Union[DashboardGroupImportQualifierArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DashboardGroupImportQualifierArgs, Mapping[str, Any], Awaitable[Union[DashboardGroupImportQualifierArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">teams</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_signalfx.dashboard_group.DashboardGroup<a class="headerlink" href="#pulumi_signalfx.DashboardGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DashboardGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>authorized_writer_teams</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Team IDs that have write access to this dashboard group. Remember to use an admin’s token if using this feature and to include that admin’s team (or user id in <code class="docutils literal notranslate"><span class="pre">authorized_writer_teams</span></code>).</p></li>
<li><p><strong>authorized_writer_users</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – User IDs that have write access to this dashboard group. Remember to use an admin’s token if using this feature and to include that admin’s user id (or team id in <code class="docutils literal notranslate"><span class="pre">authorized_writer_teams</span></code>).</p></li>
<li><p><strong>dashboards</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DashboardGroupDashboardArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – <p><a class="reference external" href="https://docs.signalfx.com/en/latest/dashboards/dashboard-mirrors.html">Mirrored dashboards</a> in this dashboard group. <strong>Note:</strong> This feature is not present in all accounts. Please contact support if you are unsure.</p>
</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the dashboard group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the dashboard group.</p></li>
<li><p><strong>teams</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Team IDs to associate the dashboard group to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.DashboardGroup.authorized_writer_teams">
<em class="property">property </em><code class="sig-name descname">authorized_writer_teams</code><a class="headerlink" href="#pulumi_signalfx.DashboardGroup.authorized_writer_teams" title="Permalink to this definition">¶</a></dt>
<dd><p>Team IDs that have write access to this dashboard group. Remember to use an admin’s token if using this feature and to include that admin’s team (or user id in <code class="docutils literal notranslate"><span class="pre">authorized_writer_teams</span></code>).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.DashboardGroup.authorized_writer_users">
<em class="property">property </em><code class="sig-name descname">authorized_writer_users</code><a class="headerlink" href="#pulumi_signalfx.DashboardGroup.authorized_writer_users" title="Permalink to this definition">¶</a></dt>
<dd><p>User IDs that have write access to this dashboard group. Remember to use an admin’s token if using this feature and to include that admin’s user id (or team id in <code class="docutils literal notranslate"><span class="pre">authorized_writer_teams</span></code>).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.DashboardGroup.dashboards">
<em class="property">property </em><code class="sig-name descname">dashboards</code><a class="headerlink" href="#pulumi_signalfx.DashboardGroup.dashboards" title="Permalink to this definition">¶</a></dt>
<dd><p><a class="reference external" href="https://docs.signalfx.com/en/latest/dashboards/dashboard-mirrors.html">Mirrored dashboards</a> in this dashboard group. <strong>Note:</strong> This feature is not present in all accounts. Please contact support if you are unsure.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.DashboardGroup.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_signalfx.DashboardGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the dashboard group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.DashboardGroup.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_signalfx.DashboardGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the dashboard group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.DashboardGroup.teams">
<em class="property">property </em><code class="sig-name descname">teams</code><a class="headerlink" href="#pulumi_signalfx.DashboardGroup.teams" title="Permalink to this definition">¶</a></dt>
<dd><p>Team IDs to associate the dashboard group to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.DashboardGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.DashboardGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.DashboardGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.DashboardGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.DataLink">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_signalfx.</code><code class="sig-name descname">DataLink</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">context_dashboard_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">property_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">property_value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_external_urls</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DataLinkTargetExternalUrlArgs, Mapping[str, Any], Awaitable[Union[DataLinkTargetExternalUrlArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DataLinkTargetExternalUrlArgs, Mapping[str, Any], Awaitable[Union[DataLinkTargetExternalUrlArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_signalfx_dashboards</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DataLinkTargetSignalfxDashboardArgs, Mapping[str, Any], Awaitable[Union[DataLinkTargetSignalfxDashboardArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DataLinkTargetSignalfxDashboardArgs, Mapping[str, Any], Awaitable[Union[DataLinkTargetSignalfxDashboardArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_splunks</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DataLinkTargetSplunkArgs, Mapping[str, Any], Awaitable[Union[DataLinkTargetSplunkArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DataLinkTargetSplunkArgs, Mapping[str, Any], Awaitable[Union[DataLinkTargetSplunkArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.DataLink" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage SignalFx <a class="reference external" href="https://docs.signalfx.com/en/latest/managing/data-links.html">Data Links</a>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_signalfx</span> <span class="k">as</span> <span class="nn">signalfx</span>

<span class="c1"># A global link to SignalFx dashboard.</span>
<span class="n">my_data_link</span> <span class="o">=</span> <span class="n">signalfx</span><span class="o">.</span><span class="n">DataLink</span><span class="p">(</span><span class="s2">&quot;myDataLink&quot;</span><span class="p">,</span>
    <span class="n">property_name</span><span class="o">=</span><span class="s2">&quot;pname&quot;</span><span class="p">,</span>
    <span class="n">property_value</span><span class="o">=</span><span class="s2">&quot;pvalue&quot;</span><span class="p">,</span>
    <span class="n">target_signalfx_dashboards</span><span class="o">=</span><span class="p">[</span><span class="n">signalfx</span><span class="o">.</span><span class="n">DataLinkTargetSignalfxDashboardArgs</span><span class="p">(</span>
        <span class="n">is_default</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">name</span><span class="o">=</span><span class="s2">&quot;sfx_dash&quot;</span><span class="p">,</span>
        <span class="n">dashboard_group_id</span><span class="o">=</span><span class="n">signalfx_dashboard_group</span><span class="p">[</span><span class="s2">&quot;mydashboardgroup0&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
        <span class="n">dashboard_id</span><span class="o">=</span><span class="n">signalfx_dashboard</span><span class="p">[</span><span class="s2">&quot;mydashboard0&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="p">)])</span>
<span class="c1"># A dashboard-specific link to an external URL</span>
<span class="n">my_data_link_dash</span> <span class="o">=</span> <span class="n">signalfx</span><span class="o">.</span><span class="n">DataLink</span><span class="p">(</span><span class="s2">&quot;myDataLinkDash&quot;</span><span class="p">,</span>
    <span class="n">context_dashboard_id</span><span class="o">=</span><span class="n">signalfx_dashboard</span><span class="p">[</span><span class="s2">&quot;mydashboard0&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">property_name</span><span class="o">=</span><span class="s2">&quot;pname2&quot;</span><span class="p">,</span>
    <span class="n">property_value</span><span class="o">=</span><span class="s2">&quot;pvalue&quot;</span><span class="p">,</span>
    <span class="n">target_external_urls</span><span class="o">=</span><span class="p">[</span><span class="n">signalfx</span><span class="o">.</span><span class="n">DataLinkTargetExternalUrlArgs</span><span class="p">(</span>
        <span class="n">is_default</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
        <span class="n">name</span><span class="o">=</span><span class="s2">&quot;ex_url&quot;</span><span class="p">,</span>
        <span class="n">time_format</span><span class="o">=</span><span class="s2">&quot;ISO8601&quot;</span><span class="p">,</span>
        <span class="n">url</span><span class="o">=</span><span class="s2">&quot;https://www.example.com&quot;</span><span class="p">,</span>
        <span class="n">property_key_mapping</span><span class="o">=</span><span class="p">{</span>
            <span class="s2">&quot;foo&quot;</span><span class="p">:</span> <span class="s2">&quot;bar&quot;</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">)])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>context_dashboard_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If provided, scopes this data link to the supplied dashboard id. If omitted then the link will be global.</p></li>
<li><p><strong>property_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name (key) of the metadata that’s the trigger of a data link. If you specify <code class="docutils literal notranslate"><span class="pre">property_value</span></code>, you must specify <code class="docutils literal notranslate"><span class="pre">property_name</span></code>.</p></li>
<li><p><strong>property_value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Value of the metadata that’s the trigger of a data link. If you specify this property, you must also specify <code class="docutils literal notranslate"><span class="pre">property_name</span></code>.</p></li>
<li><p><strong>target_external_urls</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DataLinkTargetExternalUrlArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Link to an external URL</p></li>
<li><p><strong>target_signalfx_dashboards</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DataLinkTargetSignalfxDashboardArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Link to a SignalFx dashboard</p></li>
<li><p><strong>target_splunks</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DataLinkTargetSplunkArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Link to an external URL</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_signalfx.DataLink.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">context_dashboard_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">property_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">property_value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_external_urls</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DataLinkTargetExternalUrlArgs, Mapping[str, Any], Awaitable[Union[DataLinkTargetExternalUrlArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DataLinkTargetExternalUrlArgs, Mapping[str, Any], Awaitable[Union[DataLinkTargetExternalUrlArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_signalfx_dashboards</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DataLinkTargetSignalfxDashboardArgs, Mapping[str, Any], Awaitable[Union[DataLinkTargetSignalfxDashboardArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DataLinkTargetSignalfxDashboardArgs, Mapping[str, Any], Awaitable[Union[DataLinkTargetSignalfxDashboardArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_splunks</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DataLinkTargetSplunkArgs, Mapping[str, Any], Awaitable[Union[DataLinkTargetSplunkArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DataLinkTargetSplunkArgs, Mapping[str, Any], Awaitable[Union[DataLinkTargetSplunkArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_signalfx.data_link.DataLink<a class="headerlink" href="#pulumi_signalfx.DataLink.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DataLink resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>context_dashboard_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If provided, scopes this data link to the supplied dashboard id. If omitted then the link will be global.</p></li>
<li><p><strong>property_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name (key) of the metadata that’s the trigger of a data link. If you specify <code class="docutils literal notranslate"><span class="pre">property_value</span></code>, you must specify <code class="docutils literal notranslate"><span class="pre">property_name</span></code>.</p></li>
<li><p><strong>property_value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Value of the metadata that’s the trigger of a data link. If you specify this property, you must also specify <code class="docutils literal notranslate"><span class="pre">property_name</span></code>.</p></li>
<li><p><strong>target_external_urls</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DataLinkTargetExternalUrlArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Link to an external URL</p></li>
<li><p><strong>target_signalfx_dashboards</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DataLinkTargetSignalfxDashboardArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Link to a SignalFx dashboard</p></li>
<li><p><strong>target_splunks</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DataLinkTargetSplunkArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Link to an external URL</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.DataLink.context_dashboard_id">
<em class="property">property </em><code class="sig-name descname">context_dashboard_id</code><a class="headerlink" href="#pulumi_signalfx.DataLink.context_dashboard_id" title="Permalink to this definition">¶</a></dt>
<dd><p>If provided, scopes this data link to the supplied dashboard id. If omitted then the link will be global.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.DataLink.property_name">
<em class="property">property </em><code class="sig-name descname">property_name</code><a class="headerlink" href="#pulumi_signalfx.DataLink.property_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name (key) of the metadata that’s the trigger of a data link. If you specify <code class="docutils literal notranslate"><span class="pre">property_value</span></code>, you must specify <code class="docutils literal notranslate"><span class="pre">property_name</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.DataLink.property_value">
<em class="property">property </em><code class="sig-name descname">property_value</code><a class="headerlink" href="#pulumi_signalfx.DataLink.property_value" title="Permalink to this definition">¶</a></dt>
<dd><p>Value of the metadata that’s the trigger of a data link. If you specify this property, you must also specify <code class="docutils literal notranslate"><span class="pre">property_name</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.DataLink.target_external_urls">
<em class="property">property </em><code class="sig-name descname">target_external_urls</code><a class="headerlink" href="#pulumi_signalfx.DataLink.target_external_urls" title="Permalink to this definition">¶</a></dt>
<dd><p>Link to an external URL</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.DataLink.target_signalfx_dashboards">
<em class="property">property </em><code class="sig-name descname">target_signalfx_dashboards</code><a class="headerlink" href="#pulumi_signalfx.DataLink.target_signalfx_dashboards" title="Permalink to this definition">¶</a></dt>
<dd><p>Link to a SignalFx dashboard</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.DataLink.target_splunks">
<em class="property">property </em><code class="sig-name descname">target_splunks</code><a class="headerlink" href="#pulumi_signalfx.DataLink.target_splunks" title="Permalink to this definition">¶</a></dt>
<dd><p>Link to an external URL</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.DataLink.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.DataLink.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.DataLink.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.DataLink.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.Detector">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_signalfx.</code><code class="sig-name descname">Detector</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorized_writer_teams</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorized_writer_users</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disable_sampling</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_time</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_delay</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">program_text</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DetectorRuleArgs, Mapping[str, Any], Awaitable[Union[DetectorRuleArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DetectorRuleArgs, Mapping[str, Any], Awaitable[Union[DetectorRuleArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">show_data_markers</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">show_event_lines</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_time</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">teams</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_range</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">viz_options</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DetectorVizOptionArgs, Mapping[str, Any], Awaitable[Union[DetectorVizOptionArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DetectorVizOptionArgs, Mapping[str, Any], Awaitable[Union[DetectorVizOptionArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.Detector" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a SignalFx detector resource. This can be used to create and manage detectors.</p>
<blockquote>
<div><p><strong>NOTE</strong> If you’re interested in using SignalFx detector features such as Historical Anomaly, Resource Running Out, or others then consider building them in the UI first then using the “Show SignalFlow” feature to extract the value for <code class="docutils literal notranslate"><span class="pre">program_text</span></code>. You may also consult the <a class="reference external" href="https://github.com/signalfx/signalflow-library/tree/master/library/signalfx/detectors">documentation for detector functions in signalflow-library</a>.</p>
</div></blockquote>
<p>As SignalFx supports different notification mechanisms a comma-delimited string is used to provide inputs. If you’d like to specify multiple notifications, then each should be a member in the list, like so:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
<p>This will likely be changed in a future iteration of the provider. See <a class="reference external" href="https://developers.signalfx.com/detectors_reference.html#operation/Create%20Single%20Detector">SignalFx Docs</a> for more information. For now, here are some example of how to configure each notification type:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
<p>Note that the <code class="docutils literal notranslate"><span class="pre">credentialId</span></code> is the SignalFx-provided ID shown after setting up your Jira integration. (See also <code class="docutils literal notranslate"><span class="pre">jira.Integration</span></code>.)</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
<p>Note that the <code class="docutils literal notranslate"><span class="pre">credentialId</span></code> is the SignalFx-provided ID shown after setting up your Opsgenie integration. <code class="docutils literal notranslate"><span class="pre">Team</span></code> here is hardcoded as the <code class="docutils literal notranslate"><span class="pre">responderType</span></code> as that is the only acceptable type as per the API docs.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
<p>Exclude the <code class="docutils literal notranslate"><span class="pre">#</span></code> on the channel name!</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
<p>Sends <a class="reference external" href="https://docs.signalfx.com/en/latest/managing/teams/team-notifications.html">notifications to a team</a>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
<p>Sends an email to every member of a team.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
<blockquote>
<div><p><strong>NOTE</strong> You need to include all the commas even if you only use a credential id below.</p>
</div></blockquote>
<p>You can either configure a Webhook to use an existing integration’s credential id:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
<p>or configure one inline:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
<p>Detectors can be imported using their string ID (recoverable from URL<code class="docutils literal notranslate"><span class="pre">/#/detector/v2/abc123/edit</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import signalfx:index/detector:Detector application_delay abc123
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>authorized_writer_teams</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Team IDs that have write access to this detector. Remember to use an admin’s token if using this feature and to include that admin’s team id (or user id in <code class="docutils literal notranslate"><span class="pre">authorized_writer_users</span></code>).</p></li>
<li><p><strong>authorized_writer_users</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – User IDs that have write access to this detector. Remember to use an admin’s token if using this feature and to include that admin’s user id (or team id in <code class="docutils literal notranslate"><span class="pre">authorized_writer_teams</span></code>).</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description for the rule. Displays as the alert condition in the Alert Rules tab of the detector editor in the web UI.</p></li>
<li><p><strong>disable_sampling</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">false</span></code>, the visualization may sample the output timeseries rather than displaying them all. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default.</p></li>
<li><p><strong>end_time</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Seconds since epoch. Used for visualization. Conflicts with <code class="docutils literal notranslate"><span class="pre">time_range</span></code>.</p></li>
<li><p><strong>max_delay</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How long (in seconds) to wait for late datapoints. See <a class="reference external" href="https://signalfx-product-docs.readthedocs-hosted.com/en/latest/charts/chart-builder.html#delayed-datapoints">Delayed Datapoints</a> for more info. Max value is <code class="docutils literal notranslate"><span class="pre">900</span></code> seconds (15 minutes). <code class="docutils literal notranslate"><span class="pre">Auto</span></code> (as little as possible) by default.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the detector.</p></li>
<li><p><strong>program_text</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Signalflow program text for the detector. More info <a class="reference external" href="https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language">in the SignalFx docs</a>.</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DetectorRuleArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Set of rules used for alerting.</p></li>
<li><p><strong>show_data_markers</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">true</span></code>, markers will be drawn for each datapoint within the visualization. <code class="docutils literal notranslate"><span class="pre">true</span></code> by default.</p></li>
<li><p><strong>show_event_lines</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">true</span></code>, the visualization will display a vertical line for each event trigger. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default.</p></li>
<li><p><strong>start_time</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Seconds since epoch. Used for visualization. Conflicts with <code class="docutils literal notranslate"><span class="pre">time_range</span></code>.</p></li>
<li><p><strong>teams</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Team IDs to associate the detector to.</p></li>
<li><p><strong>time_range</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Seconds to display in the visualization. This is a rolling range from the current time. Example: <code class="docutils literal notranslate"><span class="pre">3600</span></code> corresponds to <code class="docutils literal notranslate"><span class="pre">-1h</span></code> in web UI. <code class="docutils literal notranslate"><span class="pre">3600</span></code> by default.</p></li>
<li><p><strong>viz_options</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DetectorVizOptionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Plot-level customization options, associated with a publish statement.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_signalfx.Detector.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorized_writer_teams</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorized_writer_users</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disable_sampling</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_time</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_delay</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">program_text</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DetectorRuleArgs, Mapping[str, Any], Awaitable[Union[DetectorRuleArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DetectorRuleArgs, Mapping[str, Any], Awaitable[Union[DetectorRuleArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">show_data_markers</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">show_event_lines</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_time</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">teams</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_range</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">viz_options</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DetectorVizOptionArgs, Mapping[str, Any], Awaitable[Union[DetectorVizOptionArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DetectorVizOptionArgs, Mapping[str, Any], Awaitable[Union[DetectorVizOptionArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_signalfx.detector.Detector<a class="headerlink" href="#pulumi_signalfx.Detector.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Detector resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>authorized_writer_teams</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Team IDs that have write access to this detector. Remember to use an admin’s token if using this feature and to include that admin’s team id (or user id in <code class="docutils literal notranslate"><span class="pre">authorized_writer_users</span></code>).</p></li>
<li><p><strong>authorized_writer_users</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – User IDs that have write access to this detector. Remember to use an admin’s token if using this feature and to include that admin’s user id (or team id in <code class="docutils literal notranslate"><span class="pre">authorized_writer_teams</span></code>).</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description for the rule. Displays as the alert condition in the Alert Rules tab of the detector editor in the web UI.</p></li>
<li><p><strong>disable_sampling</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">false</span></code>, the visualization may sample the output timeseries rather than displaying them all. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default.</p></li>
<li><p><strong>end_time</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Seconds since epoch. Used for visualization. Conflicts with <code class="docutils literal notranslate"><span class="pre">time_range</span></code>.</p></li>
<li><p><strong>max_delay</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – <p>How long (in seconds) to wait for late datapoints. See <a class="reference external" href="https://signalfx-product-docs.readthedocs-hosted.com/en/latest/charts/chart-builder.html#delayed-datapoints">Delayed Datapoints</a> for more info. Max value is <code class="docutils literal notranslate"><span class="pre">900</span></code> seconds (15 minutes). <code class="docutils literal notranslate"><span class="pre">Auto</span></code> (as little as possible) by default.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the detector.</p></li>
<li><p><strong>program_text</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Signalflow program text for the detector. More info <a class="reference external" href="https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language">in the SignalFx docs</a>.</p>
</p></li>
<li><p><strong>rules</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DetectorRuleArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Set of rules used for alerting.</p></li>
<li><p><strong>show_data_markers</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">true</span></code>, markers will be drawn for each datapoint within the visualization. <code class="docutils literal notranslate"><span class="pre">true</span></code> by default.</p></li>
<li><p><strong>show_event_lines</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">true</span></code>, the visualization will display a vertical line for each event trigger. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default.</p></li>
<li><p><strong>start_time</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Seconds since epoch. Used for visualization. Conflicts with <code class="docutils literal notranslate"><span class="pre">time_range</span></code>.</p></li>
<li><p><strong>teams</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Team IDs to associate the detector to.</p></li>
<li><p><strong>time_range</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Seconds to display in the visualization. This is a rolling range from the current time. Example: <code class="docutils literal notranslate"><span class="pre">3600</span></code> corresponds to <code class="docutils literal notranslate"><span class="pre">-1h</span></code> in web UI. <code class="docutils literal notranslate"><span class="pre">3600</span></code> by default.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the detector.</p></li>
<li><p><strong>viz_options</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DetectorVizOptionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Plot-level customization options, associated with a publish statement.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Detector.authorized_writer_teams">
<em class="property">property </em><code class="sig-name descname">authorized_writer_teams</code><a class="headerlink" href="#pulumi_signalfx.Detector.authorized_writer_teams" title="Permalink to this definition">¶</a></dt>
<dd><p>Team IDs that have write access to this detector. Remember to use an admin’s token if using this feature and to include that admin’s team id (or user id in <code class="docutils literal notranslate"><span class="pre">authorized_writer_users</span></code>).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Detector.authorized_writer_users">
<em class="property">property </em><code class="sig-name descname">authorized_writer_users</code><a class="headerlink" href="#pulumi_signalfx.Detector.authorized_writer_users" title="Permalink to this definition">¶</a></dt>
<dd><p>User IDs that have write access to this detector. Remember to use an admin’s token if using this feature and to include that admin’s user id (or team id in <code class="docutils literal notranslate"><span class="pre">authorized_writer_teams</span></code>).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Detector.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_signalfx.Detector.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description for the rule. Displays as the alert condition in the Alert Rules tab of the detector editor in the web UI.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Detector.disable_sampling">
<em class="property">property </em><code class="sig-name descname">disable_sampling</code><a class="headerlink" href="#pulumi_signalfx.Detector.disable_sampling" title="Permalink to this definition">¶</a></dt>
<dd><p>When <code class="docutils literal notranslate"><span class="pre">false</span></code>, the visualization may sample the output timeseries rather than displaying them all. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Detector.end_time">
<em class="property">property </em><code class="sig-name descname">end_time</code><a class="headerlink" href="#pulumi_signalfx.Detector.end_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Seconds since epoch. Used for visualization. Conflicts with <code class="docutils literal notranslate"><span class="pre">time_range</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Detector.max_delay">
<em class="property">property </em><code class="sig-name descname">max_delay</code><a class="headerlink" href="#pulumi_signalfx.Detector.max_delay" title="Permalink to this definition">¶</a></dt>
<dd><p>How long (in seconds) to wait for late datapoints. See <a class="reference external" href="https://signalfx-product-docs.readthedocs-hosted.com/en/latest/charts/chart-builder.html#delayed-datapoints">Delayed Datapoints</a> for more info. Max value is <code class="docutils literal notranslate"><span class="pre">900</span></code> seconds (15 minutes). <code class="docutils literal notranslate"><span class="pre">Auto</span></code> (as little as possible) by default.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Detector.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_signalfx.Detector.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the detector.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Detector.program_text">
<em class="property">property </em><code class="sig-name descname">program_text</code><a class="headerlink" href="#pulumi_signalfx.Detector.program_text" title="Permalink to this definition">¶</a></dt>
<dd><p>Signalflow program text for the detector. More info <a class="reference external" href="https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language">in the SignalFx docs</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Detector.rules">
<em class="property">property </em><code class="sig-name descname">rules</code><a class="headerlink" href="#pulumi_signalfx.Detector.rules" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of rules used for alerting.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Detector.show_data_markers">
<em class="property">property </em><code class="sig-name descname">show_data_markers</code><a class="headerlink" href="#pulumi_signalfx.Detector.show_data_markers" title="Permalink to this definition">¶</a></dt>
<dd><p>When <code class="docutils literal notranslate"><span class="pre">true</span></code>, markers will be drawn for each datapoint within the visualization. <code class="docutils literal notranslate"><span class="pre">true</span></code> by default.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Detector.show_event_lines">
<em class="property">property </em><code class="sig-name descname">show_event_lines</code><a class="headerlink" href="#pulumi_signalfx.Detector.show_event_lines" title="Permalink to this definition">¶</a></dt>
<dd><p>When <code class="docutils literal notranslate"><span class="pre">true</span></code>, the visualization will display a vertical line for each event trigger. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Detector.start_time">
<em class="property">property </em><code class="sig-name descname">start_time</code><a class="headerlink" href="#pulumi_signalfx.Detector.start_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Seconds since epoch. Used for visualization. Conflicts with <code class="docutils literal notranslate"><span class="pre">time_range</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Detector.teams">
<em class="property">property </em><code class="sig-name descname">teams</code><a class="headerlink" href="#pulumi_signalfx.Detector.teams" title="Permalink to this definition">¶</a></dt>
<dd><p>Team IDs to associate the detector to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Detector.time_range">
<em class="property">property </em><code class="sig-name descname">time_range</code><a class="headerlink" href="#pulumi_signalfx.Detector.time_range" title="Permalink to this definition">¶</a></dt>
<dd><p>Seconds to display in the visualization. This is a rolling range from the current time. Example: <code class="docutils literal notranslate"><span class="pre">3600</span></code> corresponds to <code class="docutils literal notranslate"><span class="pre">-1h</span></code> in web UI. <code class="docutils literal notranslate"><span class="pre">3600</span></code> by default.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Detector.url">
<em class="property">property </em><code class="sig-name descname">url</code><a class="headerlink" href="#pulumi_signalfx.Detector.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the detector.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Detector.viz_options">
<em class="property">property </em><code class="sig-name descname">viz_options</code><a class="headerlink" href="#pulumi_signalfx.Detector.viz_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Plot-level customization options, associated with a publish statement.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Detector.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.Detector.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.Detector.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.Detector.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.EventFeedChart">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_signalfx.</code><code class="sig-name descname">EventFeedChart</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_time</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">program_text</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_time</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_range</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.EventFeedChart" title="Permalink to this definition">¶</a></dt>
<dd><p>Displays a listing of events as a widget in a dashboard.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the text note.</p></li>
<li><p><strong>end_time</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Seconds since epoch. Used for visualization. Conflicts with <code class="docutils literal notranslate"><span class="pre">time_range</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the text note.</p></li>
<li><p><strong>program_text</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Signalflow program text for the chart. More info<a class="reference external" href="https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language">in the SignalFx docs</a>.</p>
</p></li>
<li><p><strong>start_time</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Seconds since epoch. Used for visualization. Conflicts with <code class="docutils literal notranslate"><span class="pre">time_range</span></code>.</p></li>
<li><p><strong>time_range</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – From when to display data. SignalFx time syntax (e.g. <code class="docutils literal notranslate"><span class="pre">&quot;-5m&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;-1h&quot;</span></code>). Conflicts with <code class="docutils literal notranslate"><span class="pre">start_time</span></code> and <code class="docutils literal notranslate"><span class="pre">end_time</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_signalfx.EventFeedChart.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_time</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">program_text</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_time</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_range</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_signalfx.event_feed_chart.EventFeedChart<a class="headerlink" href="#pulumi_signalfx.EventFeedChart.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EventFeedChart resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the text note.</p></li>
<li><p><strong>end_time</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Seconds since epoch. Used for visualization. Conflicts with <code class="docutils literal notranslate"><span class="pre">time_range</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the text note.</p></li>
<li><p><strong>program_text</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Signalflow program text for the chart. More info<a class="reference external" href="https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language">in the SignalFx docs</a>.</p>
</p></li>
<li><p><strong>start_time</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Seconds since epoch. Used for visualization. Conflicts with <code class="docutils literal notranslate"><span class="pre">time_range</span></code>.</p></li>
<li><p><strong>time_range</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – From when to display data. SignalFx time syntax (e.g. <code class="docutils literal notranslate"><span class="pre">&quot;-5m&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;-1h&quot;</span></code>). Conflicts with <code class="docutils literal notranslate"><span class="pre">start_time</span></code> and <code class="docutils literal notranslate"><span class="pre">end_time</span></code>.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the chart.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.EventFeedChart.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_signalfx.EventFeedChart.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the text note.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.EventFeedChart.end_time">
<em class="property">property </em><code class="sig-name descname">end_time</code><a class="headerlink" href="#pulumi_signalfx.EventFeedChart.end_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Seconds since epoch. Used for visualization. Conflicts with <code class="docutils literal notranslate"><span class="pre">time_range</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.EventFeedChart.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_signalfx.EventFeedChart.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the text note.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.EventFeedChart.program_text">
<em class="property">property </em><code class="sig-name descname">program_text</code><a class="headerlink" href="#pulumi_signalfx.EventFeedChart.program_text" title="Permalink to this definition">¶</a></dt>
<dd><p>Signalflow program text for the chart. More info<a class="reference external" href="https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language">in the SignalFx docs</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.EventFeedChart.start_time">
<em class="property">property </em><code class="sig-name descname">start_time</code><a class="headerlink" href="#pulumi_signalfx.EventFeedChart.start_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Seconds since epoch. Used for visualization. Conflicts with <code class="docutils literal notranslate"><span class="pre">time_range</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.EventFeedChart.time_range">
<em class="property">property </em><code class="sig-name descname">time_range</code><a class="headerlink" href="#pulumi_signalfx.EventFeedChart.time_range" title="Permalink to this definition">¶</a></dt>
<dd><p>From when to display data. SignalFx time syntax (e.g. <code class="docutils literal notranslate"><span class="pre">&quot;-5m&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;-1h&quot;</span></code>). Conflicts with <code class="docutils literal notranslate"><span class="pre">start_time</span></code> and <code class="docutils literal notranslate"><span class="pre">end_time</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.EventFeedChart.url">
<em class="property">property </em><code class="sig-name descname">url</code><a class="headerlink" href="#pulumi_signalfx.EventFeedChart.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the chart.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.EventFeedChart.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.EventFeedChart.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.EventFeedChart.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.EventFeedChart.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.GetAwsServicesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_signalfx.</code><code class="sig-name descname">GetAwsServicesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">services</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.GetAwsServicesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAwsServices.</p>
<dl class="py method">
<dt id="pulumi_signalfx.GetAwsServicesResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_signalfx.GetAwsServicesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_signalfx.GetAzureServicesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_signalfx.</code><code class="sig-name descname">GetAzureServicesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">services</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.GetAzureServicesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAzureServices.</p>
<dl class="py method">
<dt id="pulumi_signalfx.GetAzureServicesResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_signalfx.GetAzureServicesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_signalfx.GetDimensionValuesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_signalfx.</code><code class="sig-name descname">GetDimensionValuesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">values</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.GetDimensionValuesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDimensionValues.</p>
<dl class="py method">
<dt id="pulumi_signalfx.GetDimensionValuesResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_signalfx.GetDimensionValuesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_signalfx.HeatmapChart">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_signalfx.</code><code class="sig-name descname">HeatmapChart</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">color_range</span><span class="p">:</span> <span class="n">Union[HeatmapChartColorRangeArgs, Mapping[str, Any], Awaitable[Union[HeatmapChartColorRangeArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">color_scales</span><span class="p">:</span> <span class="n">Union[Sequence[Union[HeatmapChartColorScaleArgs, Mapping[str, Any], Awaitable[Union[HeatmapChartColorScaleArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[HeatmapChartColorScaleArgs, Mapping[str, Any], Awaitable[Union[HeatmapChartColorScaleArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disable_sampling</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_bies</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hide_timestamp</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_delay</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">minimum_resolution</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">program_text</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">refresh_interval</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sort_by</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">unit_prefix</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.HeatmapChart" title="Permalink to this definition">¶</a></dt>
<dd><p>This chart type displays the specified plot in a heatmap fashion. This format is similar to the <a class="reference external" href="https://signalfx-product-docs.readthedocs-hosted.com/en/latest/built-in-content/infra-nav.html#infra">Infrastructure Navigator</a>, with squares representing each source for the selected metric, and the color of each square representing the value range of the metric.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_signalfx</span> <span class="k">as</span> <span class="nn">signalfx</span>

<span class="n">myheatmapchart0</span> <span class="o">=</span> <span class="n">signalfx</span><span class="o">.</span><span class="n">HeatmapChart</span><span class="p">(</span><span class="s2">&quot;myheatmapchart0&quot;</span><span class="p">,</span>
    <span class="n">color_range</span><span class="o">=</span><span class="n">signalfx</span><span class="o">.</span><span class="n">HeatmapChartColorRangeArgs</span><span class="p">(</span>
        <span class="n">color</span><span class="o">=</span><span class="s2">&quot;#ff0000&quot;</span><span class="p">,</span>
        <span class="n">max_value</span><span class="o">=</span><span class="mi">100</span><span class="p">,</span>
        <span class="n">min_value</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">color_scales</span><span class="o">=</span><span class="p">[</span>
        <span class="n">signalfx</span><span class="o">.</span><span class="n">HeatmapChartColorScaleArgs</span><span class="p">(</span>
            <span class="n">color</span><span class="o">=</span><span class="s2">&quot;green&quot;</span><span class="p">,</span>
            <span class="n">gte</span><span class="o">=</span><span class="mi">99</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">signalfx</span><span class="o">.</span><span class="n">HeatmapChartColorScaleArgs</span><span class="p">(</span>
            <span class="n">color</span><span class="o">=</span><span class="s2">&quot;yellow&quot;</span><span class="p">,</span>
            <span class="n">gte</span><span class="o">=</span><span class="mi">95</span><span class="p">,</span>
            <span class="n">lt</span><span class="o">=</span><span class="mi">99</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">signalfx</span><span class="o">.</span><span class="n">HeatmapChartColorScaleArgs</span><span class="p">(</span>
            <span class="n">color</span><span class="o">=</span><span class="s2">&quot;red&quot;</span><span class="p">,</span>
            <span class="n">lt</span><span class="o">=</span><span class="mi">95</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">],</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Very cool Heatmap&quot;</span><span class="p">,</span>
    <span class="n">disable_sampling</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">group_bies</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;hostname&quot;</span><span class="p">,</span>
        <span class="s2">&quot;host&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">hide_timestamp</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">program_text</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;myfilters = filter(&quot;cluster_name&quot;, &quot;prod&quot;) and filter(&quot;role&quot;, &quot;search&quot;)</span>
<span class="s2">data(&quot;cpu.total.idle&quot;, filter=myfilters).publish()</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
    <span class="n">sort_by</span><span class="o">=</span><span class="s2">&quot;+host&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>color_range</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'HeatmapChartColorRangeArgs'</em><em>]</em><em>]</em>) – Values and color for the color range. Example: <code class="docutils literal notranslate"><span class="pre">color_range</span> <span class="pre">:</span> <span class="pre">{</span> <span class="pre">min</span> <span class="pre">:</span> <span class="pre">0,</span> <span class="pre">max</span> <span class="pre">:</span> <span class="pre">100,</span> <span class="pre">color</span> <span class="pre">:</span> <span class="pre">&quot;#0000ff&quot;</span> <span class="pre">}</span></code>. Look at this <a class="reference external" href="https://docs.signalfx.com/en/latest/charts/chart-options-tab.html">link</a>.</p></li>
<li><p><strong>color_scales</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'HeatmapChartColorScaleArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – <p>One to N blocks, each defining a single color range including both the color to display for that range and the borders of the range. Example: <code class="docutils literal notranslate"><span class="pre">color_scale</span> <span class="pre">{</span> <span class="pre">gt</span> <span class="pre">=</span> <span class="pre">60,</span> <span class="pre">color</span> <span class="pre">=</span> <span class="pre">&quot;blue&quot;</span> <span class="pre">}</span> <span class="pre">color_scale</span> <span class="pre">{</span> <span class="pre">lte</span> <span class="pre">=</span> <span class="pre">60,</span> <span class="pre">color</span> <span class="pre">=</span> <span class="pre">&quot;yellow&quot;</span> <span class="pre">}</span></code>. Look at this <a class="reference external" href="https://docs.signalfx.com/en/latest/charts/chart-options-tab.html">link</a>.</p>
</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the chart.</p></li>
<li><p><strong>disable_sampling</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">false</span></code>, samples a subset of the output MTS, which improves UI performance. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default.</p></li>
<li><p><strong>group_bies</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Properties to group by in the heatmap (in nesting order).</p></li>
<li><p><strong>hide_timestamp</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to show the timestamp in the chart. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default.</p></li>
<li><p><strong>max_delay</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How long (in seconds) to wait for late datapoints.</p></li>
<li><p><strong>minimum_resolution</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The minimum resolution (in seconds) to use for computing the underlying program.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the chart.</p></li>
<li><p><strong>program_text</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Signalflow program text for the chart. More info at <a class="reference external" href="https://developers.signalfx.com/docs/signalflow-overview">https://developers.signalfx.com/docs/signalflow-overview</a>.</p></li>
<li><p><strong>refresh_interval</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How often (in seconds) to refresh the values of the heatmap.</p></li>
<li><p><strong>sort_by</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The property to use when sorting the elements. Must be prepended with <code class="docutils literal notranslate"><span class="pre">+</span></code> for ascending or <code class="docutils literal notranslate"><span class="pre">-</span></code> for descending (e.g. <code class="docutils literal notranslate"><span class="pre">-foo</span></code>).</p></li>
<li><p><strong>unit_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Must be <code class="docutils literal notranslate"><span class="pre">&quot;Metric&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Binary</span></code>”. <code class="docutils literal notranslate"><span class="pre">&quot;Metric&quot;</span></code> by default.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_signalfx.HeatmapChart.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">color_range</span><span class="p">:</span> <span class="n">Union[HeatmapChartColorRangeArgs, Mapping[str, Any], Awaitable[Union[HeatmapChartColorRangeArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">color_scales</span><span class="p">:</span> <span class="n">Union[Sequence[Union[HeatmapChartColorScaleArgs, Mapping[str, Any], Awaitable[Union[HeatmapChartColorScaleArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[HeatmapChartColorScaleArgs, Mapping[str, Any], Awaitable[Union[HeatmapChartColorScaleArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disable_sampling</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_bies</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hide_timestamp</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_delay</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">minimum_resolution</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">program_text</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">refresh_interval</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sort_by</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">unit_prefix</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_signalfx.heatmap_chart.HeatmapChart<a class="headerlink" href="#pulumi_signalfx.HeatmapChart.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing HeatmapChart resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>color_range</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'HeatmapChartColorRangeArgs'</em><em>]</em><em>]</em>) – <p>Values and color for the color range. Example: <code class="docutils literal notranslate"><span class="pre">color_range</span> <span class="pre">:</span> <span class="pre">{</span> <span class="pre">min</span> <span class="pre">:</span> <span class="pre">0,</span> <span class="pre">max</span> <span class="pre">:</span> <span class="pre">100,</span> <span class="pre">color</span> <span class="pre">:</span> <span class="pre">&quot;#0000ff&quot;</span> <span class="pre">}</span></code>. Look at this <a class="reference external" href="https://docs.signalfx.com/en/latest/charts/chart-options-tab.html">link</a>.</p>
</p></li>
<li><p><strong>color_scales</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'HeatmapChartColorScaleArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – <p>One to N blocks, each defining a single color range including both the color to display for that range and the borders of the range. Example: <code class="docutils literal notranslate"><span class="pre">color_scale</span> <span class="pre">{</span> <span class="pre">gt</span> <span class="pre">=</span> <span class="pre">60,</span> <span class="pre">color</span> <span class="pre">=</span> <span class="pre">&quot;blue&quot;</span> <span class="pre">}</span> <span class="pre">color_scale</span> <span class="pre">{</span> <span class="pre">lte</span> <span class="pre">=</span> <span class="pre">60,</span> <span class="pre">color</span> <span class="pre">=</span> <span class="pre">&quot;yellow&quot;</span> <span class="pre">}</span></code>. Look at this <a class="reference external" href="https://docs.signalfx.com/en/latest/charts/chart-options-tab.html">link</a>.</p>
</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the chart.</p></li>
<li><p><strong>disable_sampling</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">false</span></code>, samples a subset of the output MTS, which improves UI performance. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default.</p></li>
<li><p><strong>group_bies</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Properties to group by in the heatmap (in nesting order).</p></li>
<li><p><strong>hide_timestamp</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to show the timestamp in the chart. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default.</p></li>
<li><p><strong>max_delay</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How long (in seconds) to wait for late datapoints.</p></li>
<li><p><strong>minimum_resolution</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The minimum resolution (in seconds) to use for computing the underlying program.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the chart.</p></li>
<li><p><strong>program_text</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Signalflow program text for the chart. More info at <a class="reference external" href="https://developers.signalfx.com/docs/signalflow-overview">https://developers.signalfx.com/docs/signalflow-overview</a>.</p></li>
<li><p><strong>refresh_interval</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How often (in seconds) to refresh the values of the heatmap.</p></li>
<li><p><strong>sort_by</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The property to use when sorting the elements. Must be prepended with <code class="docutils literal notranslate"><span class="pre">+</span></code> for ascending or <code class="docutils literal notranslate"><span class="pre">-</span></code> for descending (e.g. <code class="docutils literal notranslate"><span class="pre">-foo</span></code>).</p></li>
<li><p><strong>unit_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Must be <code class="docutils literal notranslate"><span class="pre">&quot;Metric&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Binary</span></code>”. <code class="docutils literal notranslate"><span class="pre">&quot;Metric&quot;</span></code> by default.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the chart.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.HeatmapChart.color_range">
<em class="property">property </em><code class="sig-name descname">color_range</code><a class="headerlink" href="#pulumi_signalfx.HeatmapChart.color_range" title="Permalink to this definition">¶</a></dt>
<dd><p>Values and color for the color range. Example: <code class="docutils literal notranslate"><span class="pre">color_range</span> <span class="pre">:</span> <span class="pre">{</span> <span class="pre">min</span> <span class="pre">:</span> <span class="pre">0,</span> <span class="pre">max</span> <span class="pre">:</span> <span class="pre">100,</span> <span class="pre">color</span> <span class="pre">:</span> <span class="pre">&quot;#0000ff&quot;</span> <span class="pre">}</span></code>. Look at this <a class="reference external" href="https://docs.signalfx.com/en/latest/charts/chart-options-tab.html">link</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.HeatmapChart.color_scales">
<em class="property">property </em><code class="sig-name descname">color_scales</code><a class="headerlink" href="#pulumi_signalfx.HeatmapChart.color_scales" title="Permalink to this definition">¶</a></dt>
<dd><p>One to N blocks, each defining a single color range including both the color to display for that range and the borders of the range. Example: <code class="docutils literal notranslate"><span class="pre">color_scale</span> <span class="pre">{</span> <span class="pre">gt</span> <span class="pre">=</span> <span class="pre">60,</span> <span class="pre">color</span> <span class="pre">=</span> <span class="pre">&quot;blue&quot;</span> <span class="pre">}</span> <span class="pre">color_scale</span> <span class="pre">{</span> <span class="pre">lte</span> <span class="pre">=</span> <span class="pre">60,</span> <span class="pre">color</span> <span class="pre">=</span> <span class="pre">&quot;yellow&quot;</span> <span class="pre">}</span></code>. Look at this <a class="reference external" href="https://docs.signalfx.com/en/latest/charts/chart-options-tab.html">link</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.HeatmapChart.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_signalfx.HeatmapChart.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the chart.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.HeatmapChart.disable_sampling">
<em class="property">property </em><code class="sig-name descname">disable_sampling</code><a class="headerlink" href="#pulumi_signalfx.HeatmapChart.disable_sampling" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">false</span></code>, samples a subset of the output MTS, which improves UI performance. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.HeatmapChart.group_bies">
<em class="property">property </em><code class="sig-name descname">group_bies</code><a class="headerlink" href="#pulumi_signalfx.HeatmapChart.group_bies" title="Permalink to this definition">¶</a></dt>
<dd><p>Properties to group by in the heatmap (in nesting order).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.HeatmapChart.hide_timestamp">
<em class="property">property </em><code class="sig-name descname">hide_timestamp</code><a class="headerlink" href="#pulumi_signalfx.HeatmapChart.hide_timestamp" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to show the timestamp in the chart. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.HeatmapChart.max_delay">
<em class="property">property </em><code class="sig-name descname">max_delay</code><a class="headerlink" href="#pulumi_signalfx.HeatmapChart.max_delay" title="Permalink to this definition">¶</a></dt>
<dd><p>How long (in seconds) to wait for late datapoints.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.HeatmapChart.minimum_resolution">
<em class="property">property </em><code class="sig-name descname">minimum_resolution</code><a class="headerlink" href="#pulumi_signalfx.HeatmapChart.minimum_resolution" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum resolution (in seconds) to use for computing the underlying program.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.HeatmapChart.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_signalfx.HeatmapChart.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the chart.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.HeatmapChart.program_text">
<em class="property">property </em><code class="sig-name descname">program_text</code><a class="headerlink" href="#pulumi_signalfx.HeatmapChart.program_text" title="Permalink to this definition">¶</a></dt>
<dd><p>Signalflow program text for the chart. More info at <a class="reference external" href="https://developers.signalfx.com/docs/signalflow-overview">https://developers.signalfx.com/docs/signalflow-overview</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.HeatmapChart.refresh_interval">
<em class="property">property </em><code class="sig-name descname">refresh_interval</code><a class="headerlink" href="#pulumi_signalfx.HeatmapChart.refresh_interval" title="Permalink to this definition">¶</a></dt>
<dd><p>How often (in seconds) to refresh the values of the heatmap.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.HeatmapChart.sort_by">
<em class="property">property </em><code class="sig-name descname">sort_by</code><a class="headerlink" href="#pulumi_signalfx.HeatmapChart.sort_by" title="Permalink to this definition">¶</a></dt>
<dd><p>The property to use when sorting the elements. Must be prepended with <code class="docutils literal notranslate"><span class="pre">+</span></code> for ascending or <code class="docutils literal notranslate"><span class="pre">-</span></code> for descending (e.g. <code class="docutils literal notranslate"><span class="pre">-foo</span></code>).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.HeatmapChart.unit_prefix">
<em class="property">property </em><code class="sig-name descname">unit_prefix</code><a class="headerlink" href="#pulumi_signalfx.HeatmapChart.unit_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Must be <code class="docutils literal notranslate"><span class="pre">&quot;Metric&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Binary</span></code>”. <code class="docutils literal notranslate"><span class="pre">&quot;Metric&quot;</span></code> by default.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.HeatmapChart.url">
<em class="property">property </em><code class="sig-name descname">url</code><a class="headerlink" href="#pulumi_signalfx.HeatmapChart.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the chart.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.HeatmapChart.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.HeatmapChart.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.HeatmapChart.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.HeatmapChart.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.ListChart">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_signalfx.</code><code class="sig-name descname">ListChart</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">color_by</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">color_scales</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ListChartColorScaleArgs, Mapping[str, Any], Awaitable[Union[ListChartColorScaleArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ListChartColorScaleArgs, Mapping[str, Any], Awaitable[Union[ListChartColorScaleArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disable_sampling</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_time</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hide_missing_values</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">legend_fields_to_hides</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">legend_options_fields</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ListChartLegendOptionsFieldArgs, Mapping[str, Any], Awaitable[Union[ListChartLegendOptionsFieldArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ListChartLegendOptionsFieldArgs, Mapping[str, Any], Awaitable[Union[ListChartLegendOptionsFieldArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_delay</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_precision</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">program_text</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">refresh_interval</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secondary_visualization</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sort_by</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_time</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_range</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">unit_prefix</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">viz_options</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ListChartVizOptionArgs, Mapping[str, Any], Awaitable[Union[ListChartVizOptionArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ListChartVizOptionArgs, Mapping[str, Any], Awaitable[Union[ListChartVizOptionArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.ListChart" title="Permalink to this definition">¶</a></dt>
<dd><p>This chart type displays current data values in a list format.</p>
<p>The name of each value in the chart reflects the name of the plot and any associated dimensions. We recommend you click the Pencil icon and give the plot a meaningful name, as in plot B below. Otherwise, just the raw metric name will be displayed on the chart, as in plot A below.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_signalfx</span> <span class="k">as</span> <span class="nn">signalfx</span>

<span class="n">mylistchart0</span> <span class="o">=</span> <span class="n">signalfx</span><span class="o">.</span><span class="n">ListChart</span><span class="p">(</span><span class="s2">&quot;mylistchart0&quot;</span><span class="p">,</span>
    <span class="n">color_by</span><span class="o">=</span><span class="s2">&quot;Metric&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Very cool List Chart&quot;</span><span class="p">,</span>
    <span class="n">disable_sampling</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">hide_missing_values</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">legend_options_fields</span><span class="o">=</span><span class="p">[</span>
        <span class="n">signalfx</span><span class="o">.</span><span class="n">ListChartLegendOptionsFieldArgs</span><span class="p">(</span>
            <span class="n">enabled</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
            <span class="nb">property</span><span class="o">=</span><span class="s2">&quot;collector&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">signalfx</span><span class="o">.</span><span class="n">ListChartLegendOptionsFieldArgs</span><span class="p">(</span>
            <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="nb">property</span><span class="o">=</span><span class="s2">&quot;cluster_name&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">signalfx</span><span class="o">.</span><span class="n">ListChartLegendOptionsFieldArgs</span><span class="p">(</span>
            <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="nb">property</span><span class="o">=</span><span class="s2">&quot;role&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">signalfx</span><span class="o">.</span><span class="n">ListChartLegendOptionsFieldArgs</span><span class="p">(</span>
            <span class="n">enabled</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
            <span class="nb">property</span><span class="o">=</span><span class="s2">&quot;collector&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">signalfx</span><span class="o">.</span><span class="n">ListChartLegendOptionsFieldArgs</span><span class="p">(</span>
            <span class="n">enabled</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
            <span class="nb">property</span><span class="o">=</span><span class="s2">&quot;host&quot;</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">],</span>
    <span class="n">max_delay</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
    <span class="n">max_precision</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
    <span class="n">program_text</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;myfilters = filter(&quot;cluster_name&quot;, &quot;prod&quot;) and filter(&quot;role&quot;, &quot;search&quot;)</span>
<span class="s2">data(&quot;cpu.total.idle&quot;, filter=myfilters).publish()</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
    <span class="n">refresh_interval</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">sort_by</span><span class="o">=</span><span class="s2">&quot;-value&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>color_by</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Must be one of <code class="docutils literal notranslate"><span class="pre">&quot;Scale&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;Dimension&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Metric&quot;</span></code>. <code class="docutils literal notranslate"><span class="pre">&quot;Dimension&quot;</span></code> by default.</p></li>
<li><p><strong>color_scales</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ListChartColorScaleArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – <p>Single color range including both the color to display for that range and the borders of the range. Example: <code class="docutils literal notranslate"><span class="pre">[{</span> <span class="pre">gt</span> <span class="pre">=</span> <span class="pre">60,</span> <span class="pre">color</span> <span class="pre">=</span> <span class="pre">&quot;blue&quot;</span> <span class="pre">},</span> <span class="pre">{</span> <span class="pre">lte</span> <span class="pre">=</span> <span class="pre">60,</span> <span class="pre">color</span> <span class="pre">=</span> <span class="pre">&quot;yellow&quot;</span> <span class="pre">}]</span></code>. Look at this <a class="reference external" href="https://docs.signalfx.com/en/latest/charts/chart-options-tab.html">link</a>.</p>
</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the chart.</p></li>
<li><p><strong>disable_sampling</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">false</span></code>, samples a subset of the output MTS, which improves UI performance. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default.</p></li>
<li><p><strong>end_time</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Seconds since epoch. Used for visualization. Conflicts with <code class="docutils literal notranslate"><span class="pre">time_range</span></code>.</p></li>
<li><p><strong>hide_missing_values</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines whether to hide missing data points in the chart. If <code class="docutils literal notranslate"><span class="pre">true</span></code>, missing data points in the chart would be hidden. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default.</p></li>
<li><p><strong>legend_fields_to_hides</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of properties that should not be displayed in the chart legend (i.e. dimension names). All the properties are visible by default. Deprecated, please use <code class="docutils literal notranslate"><span class="pre">legend_options_fields</span></code>.</p></li>
<li><p><strong>legend_options_fields</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ListChartLegendOptionsFieldArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – List of property names and enabled flags that should be displayed in the data table for the chart, in the order provided. This option cannot be used with <code class="docutils literal notranslate"><span class="pre">legend_fields_to_hide</span></code>.</p></li>
<li><p><strong>max_delay</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How long (in seconds) to wait for late datapoints.</p></li>
<li><p><strong>max_precision</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Maximum number of digits to display when rounding values up or down.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the chart.</p></li>
<li><p><strong>program_text</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Signalflow program text for the chart. More info<a class="reference external" href="https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language">in the SignalFx docs</a>.</p>
</p></li>
<li><p><strong>refresh_interval</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How often (in seconds) to refresh the values of the list.</p></li>
<li><p><strong>secondary_visualization</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of secondary visualization. Can be <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">Radial</span></code>, <code class="docutils literal notranslate"><span class="pre">Linear</span></code>, or <code class="docutils literal notranslate"><span class="pre">Sparkline</span></code>. If unset, the SignalFx default is used (<code class="docutils literal notranslate"><span class="pre">Sparkline</span></code>).</p></li>
<li><p><strong>sort_by</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The property to use when sorting the elements. Use <code class="docutils literal notranslate"><span class="pre">value</span></code> if you want to sort by value. Must be prepended with <code class="docutils literal notranslate"><span class="pre">+</span></code> for ascending or <code class="docutils literal notranslate"><span class="pre">-</span></code> for descending (e.g. <code class="docutils literal notranslate"><span class="pre">-foo</span></code>). Note there are some special values for some of the options provided in the UX: <code class="docutils literal notranslate"><span class="pre">&quot;value&quot;</span></code> for Value, <code class="docutils literal notranslate"><span class="pre">&quot;sf_originatingMetric&quot;</span></code> for Metric, and <code class="docutils literal notranslate"><span class="pre">&quot;sf_metric&quot;</span></code> for plot.</p></li>
<li><p><strong>start_time</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Seconds since epoch. Used for visualization. Conflicts with <code class="docutils literal notranslate"><span class="pre">time_range</span></code>.</p></li>
<li><p><strong>time_range</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How many seconds ago from which to display data. For example, the last hour would be <code class="docutils literal notranslate"><span class="pre">3600</span></code>, etc. Conflicts with <code class="docutils literal notranslate"><span class="pre">start_time</span></code> and <code class="docutils literal notranslate"><span class="pre">end_time</span></code>.</p></li>
<li><p><strong>unit_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Must be <code class="docutils literal notranslate"><span class="pre">&quot;Metric&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Binary</span></code>”. <code class="docutils literal notranslate"><span class="pre">&quot;Metric&quot;</span></code> by default.</p></li>
<li><p><strong>viz_options</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ListChartVizOptionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Plot-level customization options, associated with a publish statement.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_signalfx.ListChart.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">color_by</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">color_scales</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ListChartColorScaleArgs, Mapping[str, Any], Awaitable[Union[ListChartColorScaleArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ListChartColorScaleArgs, Mapping[str, Any], Awaitable[Union[ListChartColorScaleArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disable_sampling</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_time</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hide_missing_values</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">legend_fields_to_hides</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">legend_options_fields</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ListChartLegendOptionsFieldArgs, Mapping[str, Any], Awaitable[Union[ListChartLegendOptionsFieldArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ListChartLegendOptionsFieldArgs, Mapping[str, Any], Awaitable[Union[ListChartLegendOptionsFieldArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_delay</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_precision</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">program_text</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">refresh_interval</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secondary_visualization</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sort_by</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_time</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_range</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">unit_prefix</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">viz_options</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ListChartVizOptionArgs, Mapping[str, Any], Awaitable[Union[ListChartVizOptionArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ListChartVizOptionArgs, Mapping[str, Any], Awaitable[Union[ListChartVizOptionArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_signalfx.list_chart.ListChart<a class="headerlink" href="#pulumi_signalfx.ListChart.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ListChart resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>color_by</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Must be one of <code class="docutils literal notranslate"><span class="pre">&quot;Scale&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;Dimension&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Metric&quot;</span></code>. <code class="docutils literal notranslate"><span class="pre">&quot;Dimension&quot;</span></code> by default.</p></li>
<li><p><strong>color_scales</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ListChartColorScaleArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – <p>Single color range including both the color to display for that range and the borders of the range. Example: <code class="docutils literal notranslate"><span class="pre">[{</span> <span class="pre">gt</span> <span class="pre">=</span> <span class="pre">60,</span> <span class="pre">color</span> <span class="pre">=</span> <span class="pre">&quot;blue&quot;</span> <span class="pre">},</span> <span class="pre">{</span> <span class="pre">lte</span> <span class="pre">=</span> <span class="pre">60,</span> <span class="pre">color</span> <span class="pre">=</span> <span class="pre">&quot;yellow&quot;</span> <span class="pre">}]</span></code>. Look at this <a class="reference external" href="https://docs.signalfx.com/en/latest/charts/chart-options-tab.html">link</a>.</p>
</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the chart.</p></li>
<li><p><strong>disable_sampling</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">false</span></code>, samples a subset of the output MTS, which improves UI performance. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default.</p></li>
<li><p><strong>end_time</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Seconds since epoch. Used for visualization. Conflicts with <code class="docutils literal notranslate"><span class="pre">time_range</span></code>.</p></li>
<li><p><strong>hide_missing_values</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines whether to hide missing data points in the chart. If <code class="docutils literal notranslate"><span class="pre">true</span></code>, missing data points in the chart would be hidden. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default.</p></li>
<li><p><strong>legend_fields_to_hides</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of properties that should not be displayed in the chart legend (i.e. dimension names). All the properties are visible by default. Deprecated, please use <code class="docutils literal notranslate"><span class="pre">legend_options_fields</span></code>.</p></li>
<li><p><strong>legend_options_fields</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ListChartLegendOptionsFieldArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – List of property names and enabled flags that should be displayed in the data table for the chart, in the order provided. This option cannot be used with <code class="docutils literal notranslate"><span class="pre">legend_fields_to_hide</span></code>.</p></li>
<li><p><strong>max_delay</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How long (in seconds) to wait for late datapoints.</p></li>
<li><p><strong>max_precision</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Maximum number of digits to display when rounding values up or down.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the chart.</p></li>
<li><p><strong>program_text</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Signalflow program text for the chart. More info<a class="reference external" href="https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language">in the SignalFx docs</a>.</p>
</p></li>
<li><p><strong>refresh_interval</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How often (in seconds) to refresh the values of the list.</p></li>
<li><p><strong>secondary_visualization</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of secondary visualization. Can be <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">Radial</span></code>, <code class="docutils literal notranslate"><span class="pre">Linear</span></code>, or <code class="docutils literal notranslate"><span class="pre">Sparkline</span></code>. If unset, the SignalFx default is used (<code class="docutils literal notranslate"><span class="pre">Sparkline</span></code>).</p></li>
<li><p><strong>sort_by</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The property to use when sorting the elements. Use <code class="docutils literal notranslate"><span class="pre">value</span></code> if you want to sort by value. Must be prepended with <code class="docutils literal notranslate"><span class="pre">+</span></code> for ascending or <code class="docutils literal notranslate"><span class="pre">-</span></code> for descending (e.g. <code class="docutils literal notranslate"><span class="pre">-foo</span></code>). Note there are some special values for some of the options provided in the UX: <code class="docutils literal notranslate"><span class="pre">&quot;value&quot;</span></code> for Value, <code class="docutils literal notranslate"><span class="pre">&quot;sf_originatingMetric&quot;</span></code> for Metric, and <code class="docutils literal notranslate"><span class="pre">&quot;sf_metric&quot;</span></code> for plot.</p></li>
<li><p><strong>start_time</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Seconds since epoch. Used for visualization. Conflicts with <code class="docutils literal notranslate"><span class="pre">time_range</span></code>.</p></li>
<li><p><strong>time_range</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How many seconds ago from which to display data. For example, the last hour would be <code class="docutils literal notranslate"><span class="pre">3600</span></code>, etc. Conflicts with <code class="docutils literal notranslate"><span class="pre">start_time</span></code> and <code class="docutils literal notranslate"><span class="pre">end_time</span></code>.</p></li>
<li><p><strong>unit_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Must be <code class="docutils literal notranslate"><span class="pre">&quot;Metric&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Binary</span></code>”. <code class="docutils literal notranslate"><span class="pre">&quot;Metric&quot;</span></code> by default.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the chart.</p></li>
<li><p><strong>viz_options</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ListChartVizOptionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Plot-level customization options, associated with a publish statement.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.ListChart.color_by">
<em class="property">property </em><code class="sig-name descname">color_by</code><a class="headerlink" href="#pulumi_signalfx.ListChart.color_by" title="Permalink to this definition">¶</a></dt>
<dd><p>Must be one of <code class="docutils literal notranslate"><span class="pre">&quot;Scale&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;Dimension&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Metric&quot;</span></code>. <code class="docutils literal notranslate"><span class="pre">&quot;Dimension&quot;</span></code> by default.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.ListChart.color_scales">
<em class="property">property </em><code class="sig-name descname">color_scales</code><a class="headerlink" href="#pulumi_signalfx.ListChart.color_scales" title="Permalink to this definition">¶</a></dt>
<dd><p>Single color range including both the color to display for that range and the borders of the range. Example: <code class="docutils literal notranslate"><span class="pre">[{</span> <span class="pre">gt</span> <span class="pre">=</span> <span class="pre">60,</span> <span class="pre">color</span> <span class="pre">=</span> <span class="pre">&quot;blue&quot;</span> <span class="pre">},</span> <span class="pre">{</span> <span class="pre">lte</span> <span class="pre">=</span> <span class="pre">60,</span> <span class="pre">color</span> <span class="pre">=</span> <span class="pre">&quot;yellow&quot;</span> <span class="pre">}]</span></code>. Look at this <a class="reference external" href="https://docs.signalfx.com/en/latest/charts/chart-options-tab.html">link</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.ListChart.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_signalfx.ListChart.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the chart.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.ListChart.disable_sampling">
<em class="property">property </em><code class="sig-name descname">disable_sampling</code><a class="headerlink" href="#pulumi_signalfx.ListChart.disable_sampling" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">false</span></code>, samples a subset of the output MTS, which improves UI performance. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.ListChart.end_time">
<em class="property">property </em><code class="sig-name descname">end_time</code><a class="headerlink" href="#pulumi_signalfx.ListChart.end_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Seconds since epoch. Used for visualization. Conflicts with <code class="docutils literal notranslate"><span class="pre">time_range</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.ListChart.hide_missing_values">
<em class="property">property </em><code class="sig-name descname">hide_missing_values</code><a class="headerlink" href="#pulumi_signalfx.ListChart.hide_missing_values" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines whether to hide missing data points in the chart. If <code class="docutils literal notranslate"><span class="pre">true</span></code>, missing data points in the chart would be hidden. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.ListChart.legend_fields_to_hides">
<em class="property">property </em><code class="sig-name descname">legend_fields_to_hides</code><a class="headerlink" href="#pulumi_signalfx.ListChart.legend_fields_to_hides" title="Permalink to this definition">¶</a></dt>
<dd><p>List of properties that should not be displayed in the chart legend (i.e. dimension names). All the properties are visible by default. Deprecated, please use <code class="docutils literal notranslate"><span class="pre">legend_options_fields</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.ListChart.legend_options_fields">
<em class="property">property </em><code class="sig-name descname">legend_options_fields</code><a class="headerlink" href="#pulumi_signalfx.ListChart.legend_options_fields" title="Permalink to this definition">¶</a></dt>
<dd><p>List of property names and enabled flags that should be displayed in the data table for the chart, in the order provided. This option cannot be used with <code class="docutils literal notranslate"><span class="pre">legend_fields_to_hide</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.ListChart.max_delay">
<em class="property">property </em><code class="sig-name descname">max_delay</code><a class="headerlink" href="#pulumi_signalfx.ListChart.max_delay" title="Permalink to this definition">¶</a></dt>
<dd><p>How long (in seconds) to wait for late datapoints.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.ListChart.max_precision">
<em class="property">property </em><code class="sig-name descname">max_precision</code><a class="headerlink" href="#pulumi_signalfx.ListChart.max_precision" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum number of digits to display when rounding values up or down.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.ListChart.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_signalfx.ListChart.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the chart.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.ListChart.program_text">
<em class="property">property </em><code class="sig-name descname">program_text</code><a class="headerlink" href="#pulumi_signalfx.ListChart.program_text" title="Permalink to this definition">¶</a></dt>
<dd><p>Signalflow program text for the chart. More info<a class="reference external" href="https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language">in the SignalFx docs</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.ListChart.refresh_interval">
<em class="property">property </em><code class="sig-name descname">refresh_interval</code><a class="headerlink" href="#pulumi_signalfx.ListChart.refresh_interval" title="Permalink to this definition">¶</a></dt>
<dd><p>How often (in seconds) to refresh the values of the list.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.ListChart.secondary_visualization">
<em class="property">property </em><code class="sig-name descname">secondary_visualization</code><a class="headerlink" href="#pulumi_signalfx.ListChart.secondary_visualization" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of secondary visualization. Can be <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">Radial</span></code>, <code class="docutils literal notranslate"><span class="pre">Linear</span></code>, or <code class="docutils literal notranslate"><span class="pre">Sparkline</span></code>. If unset, the SignalFx default is used (<code class="docutils literal notranslate"><span class="pre">Sparkline</span></code>).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.ListChart.sort_by">
<em class="property">property </em><code class="sig-name descname">sort_by</code><a class="headerlink" href="#pulumi_signalfx.ListChart.sort_by" title="Permalink to this definition">¶</a></dt>
<dd><p>The property to use when sorting the elements. Use <code class="docutils literal notranslate"><span class="pre">value</span></code> if you want to sort by value. Must be prepended with <code class="docutils literal notranslate"><span class="pre">+</span></code> for ascending or <code class="docutils literal notranslate"><span class="pre">-</span></code> for descending (e.g. <code class="docutils literal notranslate"><span class="pre">-foo</span></code>). Note there are some special values for some of the options provided in the UX: <code class="docutils literal notranslate"><span class="pre">&quot;value&quot;</span></code> for Value, <code class="docutils literal notranslate"><span class="pre">&quot;sf_originatingMetric&quot;</span></code> for Metric, and <code class="docutils literal notranslate"><span class="pre">&quot;sf_metric&quot;</span></code> for plot.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.ListChart.start_time">
<em class="property">property </em><code class="sig-name descname">start_time</code><a class="headerlink" href="#pulumi_signalfx.ListChart.start_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Seconds since epoch. Used for visualization. Conflicts with <code class="docutils literal notranslate"><span class="pre">time_range</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.ListChart.time_range">
<em class="property">property </em><code class="sig-name descname">time_range</code><a class="headerlink" href="#pulumi_signalfx.ListChart.time_range" title="Permalink to this definition">¶</a></dt>
<dd><p>How many seconds ago from which to display data. For example, the last hour would be <code class="docutils literal notranslate"><span class="pre">3600</span></code>, etc. Conflicts with <code class="docutils literal notranslate"><span class="pre">start_time</span></code> and <code class="docutils literal notranslate"><span class="pre">end_time</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.ListChart.unit_prefix">
<em class="property">property </em><code class="sig-name descname">unit_prefix</code><a class="headerlink" href="#pulumi_signalfx.ListChart.unit_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Must be <code class="docutils literal notranslate"><span class="pre">&quot;Metric&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Binary</span></code>”. <code class="docutils literal notranslate"><span class="pre">&quot;Metric&quot;</span></code> by default.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.ListChart.url">
<em class="property">property </em><code class="sig-name descname">url</code><a class="headerlink" href="#pulumi_signalfx.ListChart.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the chart.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.ListChart.viz_options">
<em class="property">property </em><code class="sig-name descname">viz_options</code><a class="headerlink" href="#pulumi_signalfx.ListChart.viz_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Plot-level customization options, associated with a publish statement.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.ListChart.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.ListChart.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.ListChart.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.ListChart.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.OrgToken">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_signalfx.</code><code class="sig-name descname">OrgToken</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dpm_limits</span><span class="p">:</span> <span class="n">Union[OrgTokenDpmLimitsArgs, Mapping[str, Any], Awaitable[Union[OrgTokenDpmLimitsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host_or_usage_limits</span><span class="p">:</span> <span class="n">Union[OrgTokenHostOrUsageLimitsArgs, Mapping[str, Any], Awaitable[Union[OrgTokenHostOrUsageLimitsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notifications</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.OrgToken" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage SignalFx org tokens.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_signalfx</span> <span class="k">as</span> <span class="nn">signalfx</span>

<span class="n">myteamkey0</span> <span class="o">=</span> <span class="n">signalfx</span><span class="o">.</span><span class="n">OrgToken</span><span class="p">(</span><span class="s2">&quot;myteamkey0&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;My team&#39;s rad key&quot;</span><span class="p">,</span>
    <span class="n">host_or_usage_limits</span><span class="o">=</span><span class="n">signalfx</span><span class="o">.</span><span class="n">OrgTokenHostOrUsageLimitsArgs</span><span class="p">(</span>
        <span class="n">container_limit</span><span class="o">=</span><span class="mi">200</span><span class="p">,</span>
        <span class="n">container_notification_threshold</span><span class="o">=</span><span class="mi">180</span><span class="p">,</span>
        <span class="n">custom_metrics_limit</span><span class="o">=</span><span class="mi">1000</span><span class="p">,</span>
        <span class="n">custom_metrics_notification_threshold</span><span class="o">=</span><span class="mi">900</span><span class="p">,</span>
        <span class="n">high_res_metrics_limit</span><span class="o">=</span><span class="mi">1000</span><span class="p">,</span>
        <span class="n">high_res_metrics_notification_threshold</span><span class="o">=</span><span class="mi">900</span><span class="p">,</span>
        <span class="n">host_limit</span><span class="o">=</span><span class="mi">100</span><span class="p">,</span>
        <span class="n">host_notification_threshold</span><span class="o">=</span><span class="mi">90</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">notifications</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;Email,foo-alerts@bar.com&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the token.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag that controls enabling the token. If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the token is disabled, and you can’t use it for authentication. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>dpm_limits</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'OrgTokenDpmLimitsArgs'</em><em>]</em><em>]</em>) – Specify DPM-based limits for this token.</p></li>
<li><p><strong>host_or_usage_limits</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'OrgTokenHostOrUsageLimitsArgs'</em><em>]</em><em>]</em>) – Specify Usage-based limits for this token.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the token.</p></li>
<li><p><strong>notifications</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of strings specifying where notifications will be sent when an incident occurs. See
<a class="reference external" href="https://developers.signalfx.com/v2/docs/detector-model#notifications-models">https://developers.signalfx.com/v2/docs/detector-model#notifications-models</a> for more info</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_signalfx.OrgToken.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dpm_limits</span><span class="p">:</span> <span class="n">Union[OrgTokenDpmLimitsArgs, Mapping[str, Any], Awaitable[Union[OrgTokenDpmLimitsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">host_or_usage_limits</span><span class="p">:</span> <span class="n">Union[OrgTokenHostOrUsageLimitsArgs, Mapping[str, Any], Awaitable[Union[OrgTokenHostOrUsageLimitsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notifications</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_signalfx.org_token.OrgToken<a class="headerlink" href="#pulumi_signalfx.OrgToken.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OrgToken resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the token.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag that controls enabling the token. If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the token is disabled, and you can’t use it for authentication. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>dpm_limits</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'OrgTokenDpmLimitsArgs'</em><em>]</em><em>]</em>) – Specify DPM-based limits for this token.</p></li>
<li><p><strong>host_or_usage_limits</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'OrgTokenHostOrUsageLimitsArgs'</em><em>]</em><em>]</em>) – Specify Usage-based limits for this token.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the token.</p></li>
<li><p><strong>notifications</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of strings specifying where notifications will be sent when an incident occurs. See
<a class="reference external" href="https://developers.signalfx.com/v2/docs/detector-model#notifications-models">https://developers.signalfx.com/v2/docs/detector-model#notifications-models</a> for more info</p></li>
<li><p><strong>secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The secret token created by the API. You cannot set this value.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.OrgToken.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_signalfx.OrgToken.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the token.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.OrgToken.disabled">
<em class="property">property </em><code class="sig-name descname">disabled</code><a class="headerlink" href="#pulumi_signalfx.OrgToken.disabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag that controls enabling the token. If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the token is disabled, and you can’t use it for authentication. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.OrgToken.dpm_limits">
<em class="property">property </em><code class="sig-name descname">dpm_limits</code><a class="headerlink" href="#pulumi_signalfx.OrgToken.dpm_limits" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify DPM-based limits for this token.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.OrgToken.host_or_usage_limits">
<em class="property">property </em><code class="sig-name descname">host_or_usage_limits</code><a class="headerlink" href="#pulumi_signalfx.OrgToken.host_or_usage_limits" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify Usage-based limits for this token.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.OrgToken.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_signalfx.OrgToken.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the token.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.OrgToken.notifications">
<em class="property">property </em><code class="sig-name descname">notifications</code><a class="headerlink" href="#pulumi_signalfx.OrgToken.notifications" title="Permalink to this definition">¶</a></dt>
<dd><p>List of strings specifying where notifications will be sent when an incident occurs. See
<a class="reference external" href="https://developers.signalfx.com/v2/docs/detector-model#notifications-models">https://developers.signalfx.com/v2/docs/detector-model#notifications-models</a> for more info</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.OrgToken.secret">
<em class="property">property </em><code class="sig-name descname">secret</code><a class="headerlink" href="#pulumi_signalfx.OrgToken.secret" title="Permalink to this definition">¶</a></dt>
<dd><p>The secret token created by the API. You cannot set this value.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.OrgToken.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.OrgToken.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.OrgToken.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.OrgToken.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_signalfx.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth_token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_app_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout_seconds</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the signalfx package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – API URL for your SignalFx org, may include a realm</p></li>
<li><p><strong>auth_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – SignalFx auth token</p></li>
<li><p><strong>custom_app_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Application URL for your SignalFx org, often customzied for organizations using SSO</p></li>
<li><p><strong>timeout_seconds</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Timeout duration for a single HTTP call in seconds. Defaults to 120</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_signalfx.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.SingleValueChart">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_signalfx.</code><code class="sig-name descname">SingleValueChart</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">color_by</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">color_scales</span><span class="p">:</span> <span class="n">Union[Sequence[Union[SingleValueChartColorScaleArgs, Mapping[str, Any], Awaitable[Union[SingleValueChartColorScaleArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[SingleValueChartColorScaleArgs, Mapping[str, Any], Awaitable[Union[SingleValueChartColorScaleArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_timestamp_hidden</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_delay</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_precision</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">program_text</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">refresh_interval</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secondary_visualization</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">show_spark_line</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timezone</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">unit_prefix</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">viz_options</span><span class="p">:</span> <span class="n">Union[Sequence[Union[SingleValueChartVizOptionArgs, Mapping[str, Any], Awaitable[Union[SingleValueChartVizOptionArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[SingleValueChartVizOptionArgs, Mapping[str, Any], Awaitable[Union[SingleValueChartVizOptionArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.SingleValueChart" title="Permalink to this definition">¶</a></dt>
<dd><p>This chart type displays a single number in a large font, representing the current value of a single metric on a plot line.</p>
<p>If the time period is in the past, the number represents the value of the metric near the end of the time period.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_signalfx</span> <span class="k">as</span> <span class="nn">signalfx</span>

<span class="n">mysvchart0</span> <span class="o">=</span> <span class="n">signalfx</span><span class="o">.</span><span class="n">SingleValueChart</span><span class="p">(</span><span class="s2">&quot;mysvchart0&quot;</span><span class="p">,</span>
    <span class="n">color_by</span><span class="o">=</span><span class="s2">&quot;Dimension&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Very cool Single Value Chart&quot;</span><span class="p">,</span>
    <span class="n">is_timestamp_hidden</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">max_delay</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
    <span class="n">max_precision</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
    <span class="n">program_text</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;myfilters = filter(&quot;cluster_name&quot;, &quot;prod&quot;) and filter(&quot;role&quot;, &quot;search&quot;)</span>
<span class="s2">data(&quot;cpu.total.idle&quot;, filter=myfilters).publish()</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
    <span class="n">refresh_interval</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>color_by</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Must be <code class="docutils literal notranslate"><span class="pre">&quot;Dimension&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;Scale&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Metric&quot;</span></code>. <code class="docutils literal notranslate"><span class="pre">&quot;Dimension&quot;</span></code> by default.</p></li>
<li><p><strong>color_scales</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SingleValueChartColorScaleArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – <p>Single color range including both the color to display for that range and the borders of the range. Example: <code class="docutils literal notranslate"><span class="pre">[{</span> <span class="pre">gt</span> <span class="pre">=</span> <span class="pre">60,</span> <span class="pre">color</span> <span class="pre">=</span> <span class="pre">&quot;blue&quot;</span> <span class="pre">},</span> <span class="pre">{</span> <span class="pre">lte</span> <span class="pre">=</span> <span class="pre">60,</span> <span class="pre">color</span> <span class="pre">=</span> <span class="pre">&quot;yellow&quot;</span> <span class="pre">}]</span></code>. Look at this <a class="reference external" href="https://docs.signalfx.com/en/latest/charts/chart-options-tab.html">link</a>.</p>
</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the chart.</p></li>
<li><p><strong>is_timestamp_hidden</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to hide the timestamp in the chart. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default.</p></li>
<li><p><strong>max_delay</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How long (in seconds) to wait for late datapoints</p></li>
<li><p><strong>max_precision</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The maximum precision to for value displayed.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the chart.</p></li>
<li><p><strong>program_text</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Signalflow program text for the chart. More info <a class="reference external" href="https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language">in the SignalFx docs</a>.</p>
</p></li>
<li><p><strong>refresh_interval</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How often (in seconds) to refresh the value.</p></li>
<li><p><strong>secondary_visualization</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of secondary visualization. Can be <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">Radial</span></code>, <code class="docutils literal notranslate"><span class="pre">Linear</span></code>, or <code class="docutils literal notranslate"><span class="pre">Sparkline</span></code>. If unset, the SignalFx default is used (<code class="docutils literal notranslate"><span class="pre">None</span></code>).</p></li>
<li><p><strong>show_spark_line</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to show a trend line below the current value. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default.</p></li>
<li><p><strong>timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The property value is a string that denotes the geographic region associated with the time zone, (e.g. Australia/Sydney)</p></li>
<li><p><strong>unit_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Must be <code class="docutils literal notranslate"><span class="pre">&quot;Metric&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Binary&quot;</span></code>. <code class="docutils literal notranslate"><span class="pre">&quot;Metric&quot;</span></code> by default.</p></li>
<li><p><strong>viz_options</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SingleValueChartVizOptionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Plot-level customization options, associated with a publish statement.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_signalfx.SingleValueChart.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">color_by</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">color_scales</span><span class="p">:</span> <span class="n">Union[Sequence[Union[SingleValueChartColorScaleArgs, Mapping[str, Any], Awaitable[Union[SingleValueChartColorScaleArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[SingleValueChartColorScaleArgs, Mapping[str, Any], Awaitable[Union[SingleValueChartColorScaleArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_timestamp_hidden</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_delay</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_precision</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">program_text</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">refresh_interval</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secondary_visualization</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">show_spark_line</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timezone</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">unit_prefix</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">viz_options</span><span class="p">:</span> <span class="n">Union[Sequence[Union[SingleValueChartVizOptionArgs, Mapping[str, Any], Awaitable[Union[SingleValueChartVizOptionArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[SingleValueChartVizOptionArgs, Mapping[str, Any], Awaitable[Union[SingleValueChartVizOptionArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_signalfx.single_value_chart.SingleValueChart<a class="headerlink" href="#pulumi_signalfx.SingleValueChart.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SingleValueChart resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>color_by</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Must be <code class="docutils literal notranslate"><span class="pre">&quot;Dimension&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;Scale&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Metric&quot;</span></code>. <code class="docutils literal notranslate"><span class="pre">&quot;Dimension&quot;</span></code> by default.</p></li>
<li><p><strong>color_scales</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SingleValueChartColorScaleArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – <p>Single color range including both the color to display for that range and the borders of the range. Example: <code class="docutils literal notranslate"><span class="pre">[{</span> <span class="pre">gt</span> <span class="pre">=</span> <span class="pre">60,</span> <span class="pre">color</span> <span class="pre">=</span> <span class="pre">&quot;blue&quot;</span> <span class="pre">},</span> <span class="pre">{</span> <span class="pre">lte</span> <span class="pre">=</span> <span class="pre">60,</span> <span class="pre">color</span> <span class="pre">=</span> <span class="pre">&quot;yellow&quot;</span> <span class="pre">}]</span></code>. Look at this <a class="reference external" href="https://docs.signalfx.com/en/latest/charts/chart-options-tab.html">link</a>.</p>
</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the chart.</p></li>
<li><p><strong>is_timestamp_hidden</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to hide the timestamp in the chart. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default.</p></li>
<li><p><strong>max_delay</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How long (in seconds) to wait for late datapoints</p></li>
<li><p><strong>max_precision</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The maximum precision to for value displayed.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the chart.</p></li>
<li><p><strong>program_text</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Signalflow program text for the chart. More info <a class="reference external" href="https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language">in the SignalFx docs</a>.</p>
</p></li>
<li><p><strong>refresh_interval</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How often (in seconds) to refresh the value.</p></li>
<li><p><strong>secondary_visualization</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of secondary visualization. Can be <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">Radial</span></code>, <code class="docutils literal notranslate"><span class="pre">Linear</span></code>, or <code class="docutils literal notranslate"><span class="pre">Sparkline</span></code>. If unset, the SignalFx default is used (<code class="docutils literal notranslate"><span class="pre">None</span></code>).</p></li>
<li><p><strong>show_spark_line</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether to show a trend line below the current value. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default.</p></li>
<li><p><strong>timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The property value is a string that denotes the geographic region associated with the time zone, (e.g. Australia/Sydney)</p></li>
<li><p><strong>unit_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Must be <code class="docutils literal notranslate"><span class="pre">&quot;Metric&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Binary&quot;</span></code>. <code class="docutils literal notranslate"><span class="pre">&quot;Metric&quot;</span></code> by default.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the chart.</p></li>
<li><p><strong>viz_options</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SingleValueChartVizOptionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Plot-level customization options, associated with a publish statement.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.SingleValueChart.color_by">
<em class="property">property </em><code class="sig-name descname">color_by</code><a class="headerlink" href="#pulumi_signalfx.SingleValueChart.color_by" title="Permalink to this definition">¶</a></dt>
<dd><p>Must be <code class="docutils literal notranslate"><span class="pre">&quot;Dimension&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;Scale&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Metric&quot;</span></code>. <code class="docutils literal notranslate"><span class="pre">&quot;Dimension&quot;</span></code> by default.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.SingleValueChart.color_scales">
<em class="property">property </em><code class="sig-name descname">color_scales</code><a class="headerlink" href="#pulumi_signalfx.SingleValueChart.color_scales" title="Permalink to this definition">¶</a></dt>
<dd><p>Single color range including both the color to display for that range and the borders of the range. Example: <code class="docutils literal notranslate"><span class="pre">[{</span> <span class="pre">gt</span> <span class="pre">=</span> <span class="pre">60,</span> <span class="pre">color</span> <span class="pre">=</span> <span class="pre">&quot;blue&quot;</span> <span class="pre">},</span> <span class="pre">{</span> <span class="pre">lte</span> <span class="pre">=</span> <span class="pre">60,</span> <span class="pre">color</span> <span class="pre">=</span> <span class="pre">&quot;yellow&quot;</span> <span class="pre">}]</span></code>. Look at this <a class="reference external" href="https://docs.signalfx.com/en/latest/charts/chart-options-tab.html">link</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.SingleValueChart.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_signalfx.SingleValueChart.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the chart.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.SingleValueChart.is_timestamp_hidden">
<em class="property">property </em><code class="sig-name descname">is_timestamp_hidden</code><a class="headerlink" href="#pulumi_signalfx.SingleValueChart.is_timestamp_hidden" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to hide the timestamp in the chart. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.SingleValueChart.max_delay">
<em class="property">property </em><code class="sig-name descname">max_delay</code><a class="headerlink" href="#pulumi_signalfx.SingleValueChart.max_delay" title="Permalink to this definition">¶</a></dt>
<dd><p>How long (in seconds) to wait for late datapoints</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.SingleValueChart.max_precision">
<em class="property">property </em><code class="sig-name descname">max_precision</code><a class="headerlink" href="#pulumi_signalfx.SingleValueChart.max_precision" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum precision to for value displayed.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.SingleValueChart.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_signalfx.SingleValueChart.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the chart.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.SingleValueChart.program_text">
<em class="property">property </em><code class="sig-name descname">program_text</code><a class="headerlink" href="#pulumi_signalfx.SingleValueChart.program_text" title="Permalink to this definition">¶</a></dt>
<dd><p>Signalflow program text for the chart. More info <a class="reference external" href="https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language">in the SignalFx docs</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.SingleValueChart.refresh_interval">
<em class="property">property </em><code class="sig-name descname">refresh_interval</code><a class="headerlink" href="#pulumi_signalfx.SingleValueChart.refresh_interval" title="Permalink to this definition">¶</a></dt>
<dd><p>How often (in seconds) to refresh the value.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.SingleValueChart.secondary_visualization">
<em class="property">property </em><code class="sig-name descname">secondary_visualization</code><a class="headerlink" href="#pulumi_signalfx.SingleValueChart.secondary_visualization" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of secondary visualization. Can be <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">Radial</span></code>, <code class="docutils literal notranslate"><span class="pre">Linear</span></code>, or <code class="docutils literal notranslate"><span class="pre">Sparkline</span></code>. If unset, the SignalFx default is used (<code class="docutils literal notranslate"><span class="pre">None</span></code>).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.SingleValueChart.show_spark_line">
<em class="property">property </em><code class="sig-name descname">show_spark_line</code><a class="headerlink" href="#pulumi_signalfx.SingleValueChart.show_spark_line" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether to show a trend line below the current value. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.SingleValueChart.timezone">
<em class="property">property </em><code class="sig-name descname">timezone</code><a class="headerlink" href="#pulumi_signalfx.SingleValueChart.timezone" title="Permalink to this definition">¶</a></dt>
<dd><p>The property value is a string that denotes the geographic region associated with the time zone, (e.g. Australia/Sydney)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.SingleValueChart.unit_prefix">
<em class="property">property </em><code class="sig-name descname">unit_prefix</code><a class="headerlink" href="#pulumi_signalfx.SingleValueChart.unit_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Must be <code class="docutils literal notranslate"><span class="pre">&quot;Metric&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Binary&quot;</span></code>. <code class="docutils literal notranslate"><span class="pre">&quot;Metric&quot;</span></code> by default.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.SingleValueChart.url">
<em class="property">property </em><code class="sig-name descname">url</code><a class="headerlink" href="#pulumi_signalfx.SingleValueChart.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the chart.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.SingleValueChart.viz_options">
<em class="property">property </em><code class="sig-name descname">viz_options</code><a class="headerlink" href="#pulumi_signalfx.SingleValueChart.viz_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Plot-level customization options, associated with a publish statement.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.SingleValueChart.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.SingleValueChart.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.SingleValueChart.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.SingleValueChart.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.Team">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_signalfx.</code><code class="sig-name descname">Team</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notifications_criticals</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notifications_defaults</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notifications_infos</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notifications_majors</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notifications_minors</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notifications_warnings</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.Team" title="Permalink to this definition">¶</a></dt>
<dd><p>Handles management of SignalFx teams.</p>
<p>You can configure <a class="reference external" href="https://docs.signalfx.com/en/latest/managing/teams/team-notifications.html">team notification policies</a> using this resource and the various <code class="docutils literal notranslate"><span class="pre">notifications_*</span></code> properties.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_signalfx</span> <span class="k">as</span> <span class="nn">signalfx</span>

<span class="n">myteam0</span> <span class="o">=</span> <span class="n">signalfx</span><span class="o">.</span><span class="n">Team</span><span class="p">(</span><span class="s2">&quot;myteam0&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Super great team no jerks definitely&quot;</span><span class="p">,</span>
    <span class="n">members</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;userid1&quot;</span><span class="p">,</span>
        <span class="s2">&quot;userid2&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">notifications_criticals</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;PagerDuty,credentialId&quot;</span><span class="p">],</span>
    <span class="n">notifications_infos</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;Email,notify@example.com&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the team.</p></li>
<li><p><strong>members</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of user IDs to include in the team.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the team.</p></li>
<li><p><strong>notifications_criticals</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Where to send notifications for critical alerts</p></li>
<li><p><strong>notifications_defaults</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Where to send notifications for default alerts</p></li>
<li><p><strong>notifications_infos</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Where to send notifications for info alerts</p></li>
<li><p><strong>notifications_majors</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Where to send notifications for major alerts</p></li>
<li><p><strong>notifications_minors</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Where to send notifications for minor alerts</p></li>
<li><p><strong>notifications_warnings</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Where to send notifications for warning alerts</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_signalfx.Team.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notifications_criticals</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notifications_defaults</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notifications_infos</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notifications_majors</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notifications_minors</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notifications_warnings</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_signalfx.team.Team<a class="headerlink" href="#pulumi_signalfx.Team.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Team resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the team.</p></li>
<li><p><strong>members</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of user IDs to include in the team.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the team.</p></li>
<li><p><strong>notifications_criticals</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Where to send notifications for critical alerts</p></li>
<li><p><strong>notifications_defaults</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Where to send notifications for default alerts</p></li>
<li><p><strong>notifications_infos</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Where to send notifications for info alerts</p></li>
<li><p><strong>notifications_majors</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Where to send notifications for major alerts</p></li>
<li><p><strong>notifications_minors</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Where to send notifications for minor alerts</p></li>
<li><p><strong>notifications_warnings</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Where to send notifications for warning alerts</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the team.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Team.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_signalfx.Team.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the team.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Team.members">
<em class="property">property </em><code class="sig-name descname">members</code><a class="headerlink" href="#pulumi_signalfx.Team.members" title="Permalink to this definition">¶</a></dt>
<dd><p>List of user IDs to include in the team.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Team.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_signalfx.Team.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the team.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Team.notifications_criticals">
<em class="property">property </em><code class="sig-name descname">notifications_criticals</code><a class="headerlink" href="#pulumi_signalfx.Team.notifications_criticals" title="Permalink to this definition">¶</a></dt>
<dd><p>Where to send notifications for critical alerts</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Team.notifications_defaults">
<em class="property">property </em><code class="sig-name descname">notifications_defaults</code><a class="headerlink" href="#pulumi_signalfx.Team.notifications_defaults" title="Permalink to this definition">¶</a></dt>
<dd><p>Where to send notifications for default alerts</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Team.notifications_infos">
<em class="property">property </em><code class="sig-name descname">notifications_infos</code><a class="headerlink" href="#pulumi_signalfx.Team.notifications_infos" title="Permalink to this definition">¶</a></dt>
<dd><p>Where to send notifications for info alerts</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Team.notifications_majors">
<em class="property">property </em><code class="sig-name descname">notifications_majors</code><a class="headerlink" href="#pulumi_signalfx.Team.notifications_majors" title="Permalink to this definition">¶</a></dt>
<dd><p>Where to send notifications for major alerts</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Team.notifications_minors">
<em class="property">property </em><code class="sig-name descname">notifications_minors</code><a class="headerlink" href="#pulumi_signalfx.Team.notifications_minors" title="Permalink to this definition">¶</a></dt>
<dd><p>Where to send notifications for minor alerts</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Team.notifications_warnings">
<em class="property">property </em><code class="sig-name descname">notifications_warnings</code><a class="headerlink" href="#pulumi_signalfx.Team.notifications_warnings" title="Permalink to this definition">¶</a></dt>
<dd><p>Where to send notifications for warning alerts</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Team.url">
<em class="property">property </em><code class="sig-name descname">url</code><a class="headerlink" href="#pulumi_signalfx.Team.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the team.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.Team.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.Team.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.Team.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.Team.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.TextChart">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_signalfx.</code><code class="sig-name descname">TextChart</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">markdown</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.TextChart" title="Permalink to this definition">¶</a></dt>
<dd><p>This special type of chart doesn’t display any metric data. Rather, it lets you place a text note on the dashboard.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_signalfx</span> <span class="k">as</span> <span class="nn">signalfx</span>

<span class="n">mynote0</span> <span class="o">=</span> <span class="n">signalfx</span><span class="o">.</span><span class="n">TextChart</span><span class="p">(</span><span class="s2">&quot;mynote0&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Lorem ipsum dolor sit amet, laudem tibique iracundia at mea. Nam posse dolores ex, nec cu adhuc putent honestatis&quot;</span><span class="p">,</span>
    <span class="n">markdown</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;    1. First ordered list item</span>
<span class="s2">    2. Another item</span>
<span class="s2">      * Unordered sub-list.</span>
<span class="s2">    1. Actual numbers don&#39;t matter, just that it&#39;s a number</span>
<span class="s2">      1. Ordered sub-list</span>
<span class="s2">    4. And another item.</span>

<span class="s2">       You can have properly indented paragraphs within list items. Notice the blank line above, and the leading spaces (at least one, but we&#39;ll use three here to also align the raw Markdown).</span>

<span class="s2">       To have a line break without a paragraph, you will need to use two trailing spaces.⋅⋅</span>
<span class="s2">       Note that this line is separate, but within the same paragraph.⋅⋅</span>
<span class="s2">       (This is contrary to the typical GFM line break behaviour, where trailing spaces are not required.)</span>

<span class="s2">    * Unordered list can use asterisks</span>
<span class="s2">    - Or minuses</span>
<span class="s2">    + Or pluses</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the text note.</p></li>
<li><p><strong>markdown</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Markdown text to display.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the text note.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_signalfx.TextChart.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">markdown</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_signalfx.text_chart.TextChart<a class="headerlink" href="#pulumi_signalfx.TextChart.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TextChart resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the text note.</p></li>
<li><p><strong>markdown</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Markdown text to display.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the text note.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the chart.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.TextChart.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_signalfx.TextChart.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the text note.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.TextChart.markdown">
<em class="property">property </em><code class="sig-name descname">markdown</code><a class="headerlink" href="#pulumi_signalfx.TextChart.markdown" title="Permalink to this definition">¶</a></dt>
<dd><p>Markdown text to display.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.TextChart.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_signalfx.TextChart.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the text note.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.TextChart.url">
<em class="property">property </em><code class="sig-name descname">url</code><a class="headerlink" href="#pulumi_signalfx.TextChart.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the chart.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.TextChart.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.TextChart.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.TextChart.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.TextChart.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.TimeChart">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_signalfx.</code><code class="sig-name descname">TimeChart</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">axes_include_zero</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">axes_precision</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">axis_left</span><span class="p">:</span> <span class="n">Union[TimeChartAxisLeftArgs, Mapping[str, Any], Awaitable[Union[TimeChartAxisLeftArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">axis_right</span><span class="p">:</span> <span class="n">Union[TimeChartAxisRightArgs, Mapping[str, Any], Awaitable[Union[TimeChartAxisRightArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">color_by</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disable_sampling</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_time</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">event_options</span><span class="p">:</span> <span class="n">Union[Sequence[Union[TimeChartEventOptionArgs, Mapping[str, Any], Awaitable[Union[TimeChartEventOptionArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[TimeChartEventOptionArgs, Mapping[str, Any], Awaitable[Union[TimeChartEventOptionArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">histogram_options</span><span class="p">:</span> <span class="n">Union[Sequence[Union[TimeChartHistogramOptionArgs, Mapping[str, Any], Awaitable[Union[TimeChartHistogramOptionArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[TimeChartHistogramOptionArgs, Mapping[str, Any], Awaitable[Union[TimeChartHistogramOptionArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">legend_fields_to_hides</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">legend_options_fields</span><span class="p">:</span> <span class="n">Union[Sequence[Union[TimeChartLegendOptionsFieldArgs, Mapping[str, Any], Awaitable[Union[TimeChartLegendOptionsFieldArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[TimeChartLegendOptionsFieldArgs, Mapping[str, Any], Awaitable[Union[TimeChartLegendOptionsFieldArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_delay</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">minimum_resolution</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">on_chart_legend_dimension</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plot_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">program_text</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">show_data_markers</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">show_event_lines</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stacked</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_time</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_range</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timezone</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">unit_prefix</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">viz_options</span><span class="p">:</span> <span class="n">Union[Sequence[Union[TimeChartVizOptionArgs, Mapping[str, Any], Awaitable[Union[TimeChartVizOptionArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[TimeChartVizOptionArgs, Mapping[str, Any], Awaitable[Union[TimeChartVizOptionArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.TimeChart" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a SignalFx time chart resource. This can be used to create and manage the different types of time charts.</p>
<p>Time charts display data points over a period of time.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_signalfx</span> <span class="k">as</span> <span class="nn">signalfx</span>

<span class="n">mychart0</span> <span class="o">=</span> <span class="n">signalfx</span><span class="o">.</span><span class="n">TimeChart</span><span class="p">(</span><span class="s2">&quot;mychart0&quot;</span><span class="p">,</span>
    <span class="n">axis_left</span><span class="o">=</span><span class="n">signalfx</span><span class="o">.</span><span class="n">TimeChartAxisLeftArgs</span><span class="p">(</span>
        <span class="n">label</span><span class="o">=</span><span class="s2">&quot;CPU Total Idle&quot;</span><span class="p">,</span>
        <span class="n">low_watermark</span><span class="o">=</span><span class="mi">1000</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">legend_options_fields</span><span class="o">=</span><span class="p">[</span>
        <span class="n">signalfx</span><span class="o">.</span><span class="n">TimeChartLegendOptionsFieldArgs</span><span class="p">(</span>
            <span class="n">enabled</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
            <span class="nb">property</span><span class="o">=</span><span class="s2">&quot;collector&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">signalfx</span><span class="o">.</span><span class="n">TimeChartLegendOptionsFieldArgs</span><span class="p">(</span>
            <span class="n">enabled</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
            <span class="nb">property</span><span class="o">=</span><span class="s2">&quot;hostname&quot;</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">],</span>
    <span class="n">plot_type</span><span class="o">=</span><span class="s2">&quot;LineChart&quot;</span><span class="p">,</span>
    <span class="n">program_text</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;data(&quot;cpu.total.idle&quot;).publish(label=&quot;CPU Idle&quot;)</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
    <span class="n">show_data_markers</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">time_range</span><span class="o">=</span><span class="mi">3600</span><span class="p">,</span>
    <span class="n">viz_options</span><span class="o">=</span><span class="p">[</span><span class="n">signalfx</span><span class="o">.</span><span class="n">TimeChartVizOptionArgs</span><span class="p">(</span>
        <span class="n">axis</span><span class="o">=</span><span class="s2">&quot;left&quot;</span><span class="p">,</span>
        <span class="n">color</span><span class="o">=</span><span class="s2">&quot;orange&quot;</span><span class="p">,</span>
        <span class="n">label</span><span class="o">=</span><span class="s2">&quot;CPU Idle&quot;</span><span class="p">,</span>
    <span class="p">)])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>axes_include_zero</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Force the chart to display zero on the y-axes, even if none of the data is near zero.</p></li>
<li><p><strong>axes_precision</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Specifies the digits SignalFx displays for values plotted on the chart. Defaults to <code class="docutils literal notranslate"><span class="pre">3</span></code>.</p></li>
<li><p><strong>axis_left</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TimeChartAxisLeftArgs'</em><em>]</em><em>]</em>) – Set of axis options.</p></li>
<li><p><strong>axis_right</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TimeChartAxisRightArgs'</em><em>]</em><em>]</em>) – Set of axis options.</p></li>
<li><p><strong>color_by</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Must be <code class="docutils literal notranslate"><span class="pre">&quot;Dimension&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Metric&quot;</span></code>. <code class="docutils literal notranslate"><span class="pre">&quot;Dimension&quot;</span></code> by default.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the chart.</p></li>
<li><p><strong>disable_sampling</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">false</span></code>, samples a subset of the output MTS, which improves UI performance. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default</p></li>
<li><p><strong>end_time</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Seconds since epoch. Used for visualization. Conflicts with <code class="docutils literal notranslate"><span class="pre">time_range</span></code>.</p></li>
<li><p><strong>event_options</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TimeChartEventOptionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Event customization options, associated with a publish statement. You will need to use this to change settings for any <code class="docutils literal notranslate"><span class="pre">events(…)</span></code> statements you use.</p></li>
<li><p><strong>histogram_options</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TimeChartHistogramOptionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Only used when <code class="docutils literal notranslate"><span class="pre">plot_type</span></code> is <code class="docutils literal notranslate"><span class="pre">&quot;Histogram&quot;</span></code>. Histogram specific options.</p></li>
<li><p><strong>legend_fields_to_hides</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of properties that should not be displayed in the chart legend (i.e. dimension names). All the properties are visible by default. Deprecated, please use <code class="docutils literal notranslate"><span class="pre">legend_options_fields</span></code>.</p></li>
<li><p><strong>legend_options_fields</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TimeChartLegendOptionsFieldArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – List of property names and enabled flags that should be displayed in the data table for the chart, in the order provided. This option cannot be used with <code class="docutils literal notranslate"><span class="pre">legend_fields_to_hide</span></code>.</p></li>
<li><p><strong>max_delay</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How long (in seconds) to wait for late datapoints.</p></li>
<li><p><strong>minimum_resolution</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The minimum resolution (in seconds) to use for computing the underlying program.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the chart.</p></li>
<li><p><strong>on_chart_legend_dimension</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Dimensions to show in the on-chart legend. On-chart legend is off unless a dimension is specified. Allowed: <code class="docutils literal notranslate"><span class="pre">&quot;metric&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;plot_label&quot;</span></code> and any dimension.</p></li>
<li><p><strong>plot_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The visualization style to use. Must be <code class="docutils literal notranslate"><span class="pre">&quot;LineChart&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;AreaChart&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ColumnChart&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;Histogram&quot;</span></code>. Chart level <code class="docutils literal notranslate"><span class="pre">plot_type</span></code> by default.</p></li>
<li><p><strong>program_text</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Signalflow program text for the chart. More info <a class="reference external" href="https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language">in the SignalFx docs</a>.</p>
</p></li>
<li><p><strong>show_data_markers</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Show markers (circles) for each datapoint used to draw line or area charts. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default.</p></li>
<li><p><strong>show_event_lines</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether vertical highlight lines should be drawn in the visualizations at times when events occurred. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default.</p></li>
<li><p><strong>stacked</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether area and bar charts in the visualization should be stacked. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default.</p></li>
<li><p><strong>start_time</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Seconds since epoch. Used for visualization. Conflicts with <code class="docutils literal notranslate"><span class="pre">time_range</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Tags associated with the chart</p></li>
<li><p><strong>time_range</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How many seconds ago from which to display data. For example, the last hour would be <code class="docutils literal notranslate"><span class="pre">3600</span></code>, etc. Conflicts with <code class="docutils literal notranslate"><span class="pre">start_time</span></code> and <code class="docutils literal notranslate"><span class="pre">end_time</span></code>.</p></li>
<li><p><strong>timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Time zone that SignalFlow uses as the basis of calendar window transformation methods. For example, if you set “timezone”: “Europe/Paris” and then use the transformation sum(cycle=”week”, cycle_start=”Monday”) in your chart’s SignalFlow program, the calendar window starts on Monday, Paris time. See the <a class="reference external" href="https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_supported_signalflow_time_zones">full list of timezones for more</a>. <code class="docutils literal notranslate"><span class="pre">&quot;UTC&quot;</span></code> by default.</p></li>
<li><p><strong>unit_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Must be <code class="docutils literal notranslate"><span class="pre">&quot;Metric&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Binary</span></code>”. <code class="docutils literal notranslate"><span class="pre">&quot;Metric&quot;</span></code> by default.</p></li>
<li><p><strong>viz_options</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TimeChartVizOptionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Plot-level customization options, associated with a publish statement.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_signalfx.TimeChart.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">axes_include_zero</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">axes_precision</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">axis_left</span><span class="p">:</span> <span class="n">Union[TimeChartAxisLeftArgs, Mapping[str, Any], Awaitable[Union[TimeChartAxisLeftArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">axis_right</span><span class="p">:</span> <span class="n">Union[TimeChartAxisRightArgs, Mapping[str, Any], Awaitable[Union[TimeChartAxisRightArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">color_by</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disable_sampling</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_time</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">event_options</span><span class="p">:</span> <span class="n">Union[Sequence[Union[TimeChartEventOptionArgs, Mapping[str, Any], Awaitable[Union[TimeChartEventOptionArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[TimeChartEventOptionArgs, Mapping[str, Any], Awaitable[Union[TimeChartEventOptionArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">histogram_options</span><span class="p">:</span> <span class="n">Union[Sequence[Union[TimeChartHistogramOptionArgs, Mapping[str, Any], Awaitable[Union[TimeChartHistogramOptionArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[TimeChartHistogramOptionArgs, Mapping[str, Any], Awaitable[Union[TimeChartHistogramOptionArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">legend_fields_to_hides</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">legend_options_fields</span><span class="p">:</span> <span class="n">Union[Sequence[Union[TimeChartLegendOptionsFieldArgs, Mapping[str, Any], Awaitable[Union[TimeChartLegendOptionsFieldArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[TimeChartLegendOptionsFieldArgs, Mapping[str, Any], Awaitable[Union[TimeChartLegendOptionsFieldArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_delay</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">minimum_resolution</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">on_chart_legend_dimension</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plot_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">program_text</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">show_data_markers</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">show_event_lines</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">stacked</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_time</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">time_range</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timezone</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">unit_prefix</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">viz_options</span><span class="p">:</span> <span class="n">Union[Sequence[Union[TimeChartVizOptionArgs, Mapping[str, Any], Awaitable[Union[TimeChartVizOptionArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[TimeChartVizOptionArgs, Mapping[str, Any], Awaitable[Union[TimeChartVizOptionArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_signalfx.time_chart.TimeChart<a class="headerlink" href="#pulumi_signalfx.TimeChart.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TimeChart resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>axes_include_zero</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Force the chart to display zero on the y-axes, even if none of the data is near zero.</p></li>
<li><p><strong>axes_precision</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Specifies the digits SignalFx displays for values plotted on the chart. Defaults to <code class="docutils literal notranslate"><span class="pre">3</span></code>.</p></li>
<li><p><strong>axis_left</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TimeChartAxisLeftArgs'</em><em>]</em><em>]</em>) – Set of axis options.</p></li>
<li><p><strong>axis_right</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TimeChartAxisRightArgs'</em><em>]</em><em>]</em>) – Set of axis options.</p></li>
<li><p><strong>color_by</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Must be <code class="docutils literal notranslate"><span class="pre">&quot;Dimension&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Metric&quot;</span></code>. <code class="docutils literal notranslate"><span class="pre">&quot;Dimension&quot;</span></code> by default.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the chart.</p></li>
<li><p><strong>disable_sampling</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">false</span></code>, samples a subset of the output MTS, which improves UI performance. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default</p></li>
<li><p><strong>end_time</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Seconds since epoch. Used for visualization. Conflicts with <code class="docutils literal notranslate"><span class="pre">time_range</span></code>.</p></li>
<li><p><strong>event_options</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TimeChartEventOptionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Event customization options, associated with a publish statement. You will need to use this to change settings for any <code class="docutils literal notranslate"><span class="pre">events(…)</span></code> statements you use.</p></li>
<li><p><strong>histogram_options</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TimeChartHistogramOptionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Only used when <code class="docutils literal notranslate"><span class="pre">plot_type</span></code> is <code class="docutils literal notranslate"><span class="pre">&quot;Histogram&quot;</span></code>. Histogram specific options.</p></li>
<li><p><strong>legend_fields_to_hides</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of properties that should not be displayed in the chart legend (i.e. dimension names). All the properties are visible by default. Deprecated, please use <code class="docutils literal notranslate"><span class="pre">legend_options_fields</span></code>.</p></li>
<li><p><strong>legend_options_fields</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TimeChartLegendOptionsFieldArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – List of property names and enabled flags that should be displayed in the data table for the chart, in the order provided. This option cannot be used with <code class="docutils literal notranslate"><span class="pre">legend_fields_to_hide</span></code>.</p></li>
<li><p><strong>max_delay</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How long (in seconds) to wait for late datapoints.</p></li>
<li><p><strong>minimum_resolution</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The minimum resolution (in seconds) to use for computing the underlying program.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the chart.</p></li>
<li><p><strong>on_chart_legend_dimension</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Dimensions to show in the on-chart legend. On-chart legend is off unless a dimension is specified. Allowed: <code class="docutils literal notranslate"><span class="pre">&quot;metric&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;plot_label&quot;</span></code> and any dimension.</p></li>
<li><p><strong>plot_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The visualization style to use. Must be <code class="docutils literal notranslate"><span class="pre">&quot;LineChart&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;AreaChart&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ColumnChart&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;Histogram&quot;</span></code>. Chart level <code class="docutils literal notranslate"><span class="pre">plot_type</span></code> by default.</p></li>
<li><p><strong>program_text</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Signalflow program text for the chart. More info <a class="reference external" href="https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language">in the SignalFx docs</a>.</p>
</p></li>
<li><p><strong>show_data_markers</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Show markers (circles) for each datapoint used to draw line or area charts. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default.</p></li>
<li><p><strong>show_event_lines</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether vertical highlight lines should be drawn in the visualizations at times when events occurred. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default.</p></li>
<li><p><strong>stacked</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether area and bar charts in the visualization should be stacked. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default.</p></li>
<li><p><strong>start_time</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Seconds since epoch. Used for visualization. Conflicts with <code class="docutils literal notranslate"><span class="pre">time_range</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Tags associated with the chart</p></li>
<li><p><strong>time_range</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – How many seconds ago from which to display data. For example, the last hour would be <code class="docutils literal notranslate"><span class="pre">3600</span></code>, etc. Conflicts with <code class="docutils literal notranslate"><span class="pre">start_time</span></code> and <code class="docutils literal notranslate"><span class="pre">end_time</span></code>.</p></li>
<li><p><strong>timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Time zone that SignalFlow uses as the basis of calendar window transformation methods. For example, if you set “timezone”: “Europe/Paris” and then use the transformation sum(cycle=”week”, cycle_start=”Monday”) in your chart’s SignalFlow program, the calendar window starts on Monday, Paris time. See the <a class="reference external" href="https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_supported_signalflow_time_zones">full list of timezones for more</a>. <code class="docutils literal notranslate"><span class="pre">&quot;UTC&quot;</span></code> by default.</p>
</p></li>
<li><p><strong>unit_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Must be <code class="docutils literal notranslate"><span class="pre">&quot;Metric&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Binary</span></code>”. <code class="docutils literal notranslate"><span class="pre">&quot;Metric&quot;</span></code> by default.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the chart.</p></li>
<li><p><strong>viz_options</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TimeChartVizOptionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Plot-level customization options, associated with a publish statement.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.TimeChart.axes_include_zero">
<em class="property">property </em><code class="sig-name descname">axes_include_zero</code><a class="headerlink" href="#pulumi_signalfx.TimeChart.axes_include_zero" title="Permalink to this definition">¶</a></dt>
<dd><p>Force the chart to display zero on the y-axes, even if none of the data is near zero.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.TimeChart.axes_precision">
<em class="property">property </em><code class="sig-name descname">axes_precision</code><a class="headerlink" href="#pulumi_signalfx.TimeChart.axes_precision" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the digits SignalFx displays for values plotted on the chart. Defaults to <code class="docutils literal notranslate"><span class="pre">3</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.TimeChart.axis_left">
<em class="property">property </em><code class="sig-name descname">axis_left</code><a class="headerlink" href="#pulumi_signalfx.TimeChart.axis_left" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of axis options.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.TimeChart.axis_right">
<em class="property">property </em><code class="sig-name descname">axis_right</code><a class="headerlink" href="#pulumi_signalfx.TimeChart.axis_right" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of axis options.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.TimeChart.color_by">
<em class="property">property </em><code class="sig-name descname">color_by</code><a class="headerlink" href="#pulumi_signalfx.TimeChart.color_by" title="Permalink to this definition">¶</a></dt>
<dd><p>Must be <code class="docutils literal notranslate"><span class="pre">&quot;Dimension&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Metric&quot;</span></code>. <code class="docutils literal notranslate"><span class="pre">&quot;Dimension&quot;</span></code> by default.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.TimeChart.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_signalfx.TimeChart.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the chart.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.TimeChart.disable_sampling">
<em class="property">property </em><code class="sig-name descname">disable_sampling</code><a class="headerlink" href="#pulumi_signalfx.TimeChart.disable_sampling" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">false</span></code>, samples a subset of the output MTS, which improves UI performance. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.TimeChart.end_time">
<em class="property">property </em><code class="sig-name descname">end_time</code><a class="headerlink" href="#pulumi_signalfx.TimeChart.end_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Seconds since epoch. Used for visualization. Conflicts with <code class="docutils literal notranslate"><span class="pre">time_range</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.TimeChart.event_options">
<em class="property">property </em><code class="sig-name descname">event_options</code><a class="headerlink" href="#pulumi_signalfx.TimeChart.event_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Event customization options, associated with a publish statement. You will need to use this to change settings for any <code class="docutils literal notranslate"><span class="pre">events(…)</span></code> statements you use.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.TimeChart.histogram_options">
<em class="property">property </em><code class="sig-name descname">histogram_options</code><a class="headerlink" href="#pulumi_signalfx.TimeChart.histogram_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Only used when <code class="docutils literal notranslate"><span class="pre">plot_type</span></code> is <code class="docutils literal notranslate"><span class="pre">&quot;Histogram&quot;</span></code>. Histogram specific options.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.TimeChart.legend_fields_to_hides">
<em class="property">property </em><code class="sig-name descname">legend_fields_to_hides</code><a class="headerlink" href="#pulumi_signalfx.TimeChart.legend_fields_to_hides" title="Permalink to this definition">¶</a></dt>
<dd><p>List of properties that should not be displayed in the chart legend (i.e. dimension names). All the properties are visible by default. Deprecated, please use <code class="docutils literal notranslate"><span class="pre">legend_options_fields</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.TimeChart.legend_options_fields">
<em class="property">property </em><code class="sig-name descname">legend_options_fields</code><a class="headerlink" href="#pulumi_signalfx.TimeChart.legend_options_fields" title="Permalink to this definition">¶</a></dt>
<dd><p>List of property names and enabled flags that should be displayed in the data table for the chart, in the order provided. This option cannot be used with <code class="docutils literal notranslate"><span class="pre">legend_fields_to_hide</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.TimeChart.max_delay">
<em class="property">property </em><code class="sig-name descname">max_delay</code><a class="headerlink" href="#pulumi_signalfx.TimeChart.max_delay" title="Permalink to this definition">¶</a></dt>
<dd><p>How long (in seconds) to wait for late datapoints.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.TimeChart.minimum_resolution">
<em class="property">property </em><code class="sig-name descname">minimum_resolution</code><a class="headerlink" href="#pulumi_signalfx.TimeChart.minimum_resolution" title="Permalink to this definition">¶</a></dt>
<dd><p>The minimum resolution (in seconds) to use for computing the underlying program.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.TimeChart.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_signalfx.TimeChart.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the chart.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.TimeChart.on_chart_legend_dimension">
<em class="property">property </em><code class="sig-name descname">on_chart_legend_dimension</code><a class="headerlink" href="#pulumi_signalfx.TimeChart.on_chart_legend_dimension" title="Permalink to this definition">¶</a></dt>
<dd><p>Dimensions to show in the on-chart legend. On-chart legend is off unless a dimension is specified. Allowed: <code class="docutils literal notranslate"><span class="pre">&quot;metric&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;plot_label&quot;</span></code> and any dimension.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.TimeChart.plot_type">
<em class="property">property </em><code class="sig-name descname">plot_type</code><a class="headerlink" href="#pulumi_signalfx.TimeChart.plot_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The visualization style to use. Must be <code class="docutils literal notranslate"><span class="pre">&quot;LineChart&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;AreaChart&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;ColumnChart&quot;</span></code>, or <code class="docutils literal notranslate"><span class="pre">&quot;Histogram&quot;</span></code>. Chart level <code class="docutils literal notranslate"><span class="pre">plot_type</span></code> by default.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.TimeChart.program_text">
<em class="property">property </em><code class="sig-name descname">program_text</code><a class="headerlink" href="#pulumi_signalfx.TimeChart.program_text" title="Permalink to this definition">¶</a></dt>
<dd><p>Signalflow program text for the chart. More info <a class="reference external" href="https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language">in the SignalFx docs</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.TimeChart.show_data_markers">
<em class="property">property </em><code class="sig-name descname">show_data_markers</code><a class="headerlink" href="#pulumi_signalfx.TimeChart.show_data_markers" title="Permalink to this definition">¶</a></dt>
<dd><p>Show markers (circles) for each datapoint used to draw line or area charts. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.TimeChart.show_event_lines">
<em class="property">property </em><code class="sig-name descname">show_event_lines</code><a class="headerlink" href="#pulumi_signalfx.TimeChart.show_event_lines" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether vertical highlight lines should be drawn in the visualizations at times when events occurred. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.TimeChart.stacked">
<em class="property">property </em><code class="sig-name descname">stacked</code><a class="headerlink" href="#pulumi_signalfx.TimeChart.stacked" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether area and bar charts in the visualization should be stacked. <code class="docutils literal notranslate"><span class="pre">false</span></code> by default.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.TimeChart.start_time">
<em class="property">property </em><code class="sig-name descname">start_time</code><a class="headerlink" href="#pulumi_signalfx.TimeChart.start_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Seconds since epoch. Used for visualization. Conflicts with <code class="docutils literal notranslate"><span class="pre">time_range</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.TimeChart.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_signalfx.TimeChart.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Tags associated with the chart</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.TimeChart.time_range">
<em class="property">property </em><code class="sig-name descname">time_range</code><a class="headerlink" href="#pulumi_signalfx.TimeChart.time_range" title="Permalink to this definition">¶</a></dt>
<dd><p>How many seconds ago from which to display data. For example, the last hour would be <code class="docutils literal notranslate"><span class="pre">3600</span></code>, etc. Conflicts with <code class="docutils literal notranslate"><span class="pre">start_time</span></code> and <code class="docutils literal notranslate"><span class="pre">end_time</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.TimeChart.timezone">
<em class="property">property </em><code class="sig-name descname">timezone</code><a class="headerlink" href="#pulumi_signalfx.TimeChart.timezone" title="Permalink to this definition">¶</a></dt>
<dd><p>Time zone that SignalFlow uses as the basis of calendar window transformation methods. For example, if you set “timezone”: “Europe/Paris” and then use the transformation sum(cycle=”week”, cycle_start=”Monday”) in your chart’s SignalFlow program, the calendar window starts on Monday, Paris time. See the <a class="reference external" href="https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_supported_signalflow_time_zones">full list of timezones for more</a>. <code class="docutils literal notranslate"><span class="pre">&quot;UTC&quot;</span></code> by default.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.TimeChart.unit_prefix">
<em class="property">property </em><code class="sig-name descname">unit_prefix</code><a class="headerlink" href="#pulumi_signalfx.TimeChart.unit_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>Must be <code class="docutils literal notranslate"><span class="pre">&quot;Metric&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;Binary</span></code>”. <code class="docutils literal notranslate"><span class="pre">&quot;Metric&quot;</span></code> by default.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.TimeChart.url">
<em class="property">property </em><code class="sig-name descname">url</code><a class="headerlink" href="#pulumi_signalfx.TimeChart.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the chart.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.TimeChart.viz_options">
<em class="property">property </em><code class="sig-name descname">viz_options</code><a class="headerlink" href="#pulumi_signalfx.TimeChart.viz_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Plot-level customization options, associated with a publish statement.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.TimeChart.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.TimeChart.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.TimeChart.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.TimeChart.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.WebhookIntegration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_signalfx.</code><code class="sig-name descname">WebhookIntegration</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">headers</span><span class="p">:</span> <span class="n">Union[Sequence[Union[WebhookIntegrationHeaderArgs, Mapping[str, Any], Awaitable[Union[WebhookIntegrationHeaderArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[WebhookIntegrationHeaderArgs, Mapping[str, Any], Awaitable[Union[WebhookIntegrationHeaderArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shared_secret</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.WebhookIntegration" title="Permalink to this definition">¶</a></dt>
<dd><p>SignalFx Webhook integration.</p>
<blockquote>
<div><p><strong>NOTE</strong> When managing integrations you’ll need to use an admin token to authenticate the SignalFx provider. Otherwise you’ll receive a 4xx error.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the integration is enabled.</p></li>
<li><p><strong>headers</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'WebhookIntegrationHeaderArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A header to send with the request</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the integration.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL to request</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_signalfx.WebhookIntegration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">headers</span><span class="p">:</span> <span class="n">Union[Sequence[Union[WebhookIntegrationHeaderArgs, Mapping[str, Any], Awaitable[Union[WebhookIntegrationHeaderArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[WebhookIntegrationHeaderArgs, Mapping[str, Any], Awaitable[Union[WebhookIntegrationHeaderArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shared_secret</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_signalfx.webhook_integration.WebhookIntegration<a class="headerlink" href="#pulumi_signalfx.WebhookIntegration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing WebhookIntegration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the integration is enabled.</p></li>
<li><p><strong>headers</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'WebhookIntegrationHeaderArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A header to send with the request</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the integration.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL to request</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.WebhookIntegration.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_signalfx.WebhookIntegration.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the integration is enabled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.WebhookIntegration.headers">
<em class="property">property </em><code class="sig-name descname">headers</code><a class="headerlink" href="#pulumi_signalfx.WebhookIntegration.headers" title="Permalink to this definition">¶</a></dt>
<dd><p>A header to send with the request</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.WebhookIntegration.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_signalfx.WebhookIntegration.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the integration.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.WebhookIntegration.url">
<em class="property">property </em><code class="sig-name descname">url</code><a class="headerlink" href="#pulumi_signalfx.WebhookIntegration.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL to request</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_signalfx.WebhookIntegration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.WebhookIntegration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.WebhookIntegration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_signalfx.WebhookIntegration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_signalfx.get_aws_services">
<code class="sig-prename descclassname">pulumi_signalfx.</code><code class="sig-name descname">get_aws_services</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">services</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>GetAwsServicesServiceArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_signalfx.get_aws_services.AwaitableGetAwsServicesResult<a class="headerlink" href="#pulumi_signalfx.get_aws_services" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_signalfx.get_azure_services">
<code class="sig-prename descclassname">pulumi_signalfx.</code><code class="sig-name descname">get_azure_services</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">services</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>GetAzureServicesServiceArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_signalfx.get_azure_services.AwaitableGetAzureServicesResult<a class="headerlink" href="#pulumi_signalfx.get_azure_services" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_signalfx.get_dimension_values">
<code class="sig-prename descclassname">pulumi_signalfx.</code><code class="sig-name descname">get_dimension_values</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">query</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_signalfx.get_dimension_values.AwaitableGetDimensionValuesResult<a class="headerlink" href="#pulumi_signalfx.get_dimension_values" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to get a list of dimension values matching the provided query.</p>
<blockquote>
<div><p><strong>NOTE</strong> This data source only allows 1000 values, as it’s kinda nuts to make anything with <code class="docutils literal notranslate"><span class="pre">for_each</span></code> that big in SignalFx. This is negotiable.</p>
</div></blockquote>
</dd></dl>

</div>
