---
title: Package pulumi_datadog
title_tag: Package pulumi_datadog | Python SDK
linktitle: pulumi_datadog
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "datadog" >}}

<div class="section" id="pulumi-datadog">
<h1>Pulumi Datadog<a class="headerlink" href="#pulumi-datadog" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-datadog">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-datadog/issues">pulumi/pulumi-datadog repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-datadog/issues">terraform-providers/terraform-provider-datadog repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_datadog"></span><dl class="py class">
<dt id="pulumi_datadog.AwaitableGetDashboardListResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">AwaitableGetDashboardListResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.AwaitableGetDashboardListResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_datadog.AwaitableGetDashboardResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">AwaitableGetDashboardResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">title</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.AwaitableGetDashboardResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_datadog.AwaitableGetIpRangesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">AwaitableGetIpRangesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">agents_ipv4s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">agents_ipv6s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_ipv4s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_ipv6s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">apm_ipv4s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">apm_ipv6s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logs_ipv4s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logs_ipv6s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">process_ipv4s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">process_ipv6s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">synthetics_ipv4s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">synthetics_ipv6s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">webhooks_ipv4s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">webhooks_ipv6s</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.AwaitableGetIpRangesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_datadog.AwaitableGetMonitorResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">AwaitableGetMonitorResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">enable_logs_sample</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">escalation_message</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">evaluation_delay</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">include_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locked</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitor_tags_filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitor_threshold_windows</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitor_thresholds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">new_host_delay</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">no_data_timeframe</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_audit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_no_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">renotify_interval</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">require_full_window</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags_filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">threshold_windows</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">thresholds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout_h</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.AwaitableGetMonitorResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_datadog.AwaitableGetPermissionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">AwaitableGetPermissionsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.AwaitableGetPermissionsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_datadog.AwaitableGetRoleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">AwaitableGetRoleResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_count</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.AwaitableGetRoleResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_datadog.AwaitableGetSecurityMonitoringRulesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">AwaitableGetSecurityMonitoringRulesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">default_only_filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rule_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags_filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_only_filter</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.AwaitableGetSecurityMonitoringRulesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_datadog.AwaitableGetSyntheticsLocationsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">AwaitableGetSyntheticsLocationsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locations</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.AwaitableGetSyntheticsLocationsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_datadog.Dashboard">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">Dashboard</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dashboard_lists</span><span class="p">:</span> <span class="n">Union[Sequence[Union[int, Awaitable[int], Output[T]]], Awaitable[Sequence[Union[int, Awaitable[int], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_read_only</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">layout_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_lists</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_variable_presets</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DashboardTemplateVariablePresetArgs, Mapping[str, Any], Awaitable[Union[DashboardTemplateVariablePresetArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DashboardTemplateVariablePresetArgs, Mapping[str, Any], Awaitable[Union[DashboardTemplateVariablePresetArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_variables</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DashboardTemplateVariableArgs, Mapping[str, Any], Awaitable[Union[DashboardTemplateVariableArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DashboardTemplateVariableArgs, Mapping[str, Any], Awaitable[Union[DashboardTemplateVariableArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">title</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">widgets</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DashboardWidgetArgs, Mapping[str, Any], Awaitable[Union[DashboardWidgetArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DashboardWidgetArgs, Mapping[str, Any], Awaitable[Union[DashboardWidgetArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.Dashboard" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Datadog dashboard resource. This can be used to create and manage Datadog dashboards.</p>
<blockquote>
<div><p><strong>Note:</strong> This resource uses the new <a class="reference external" href="https://docs.datadoghq.com/api/v1/dashboards/">Dashboard API</a> which adds new features like better validation and support for the <a class="reference external" href="https://docs.datadoghq.com/dashboards/widgets/group/">Group widget</a>. Additionally, this resource unifies <code class="docutils literal notranslate"><span class="pre">TimeBoard</span></code> and <code class="docutils literal notranslate"><span class="pre">ScreenBoard</span></code> resources to allow you to manage all of your dashboards using a single format.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="n">ordered_dashboard</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">Dashboard</span><span class="p">(</span><span class="s2">&quot;orderedDashboard&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Created using the Datadog provider in Terraform&quot;</span><span class="p">,</span>
    <span class="n">is_read_only</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">layout_type</span><span class="o">=</span><span class="s2">&quot;ordered&quot;</span><span class="p">,</span>
    <span class="n">template_variables</span><span class="o">=</span><span class="p">[</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">DashboardTemplateVariableArgs</span><span class="p">(</span>
            <span class="n">default</span><span class="o">=</span><span class="s2">&quot;aws&quot;</span><span class="p">,</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">&quot;var_1&quot;</span><span class="p">,</span>
            <span class="n">prefix</span><span class="o">=</span><span class="s2">&quot;host&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">DashboardTemplateVariableArgs</span><span class="p">(</span>
            <span class="n">default</span><span class="o">=</span><span class="s2">&quot;autoscaling&quot;</span><span class="p">,</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">&quot;var_2&quot;</span><span class="p">,</span>
            <span class="n">prefix</span><span class="o">=</span><span class="s2">&quot;service_name&quot;</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">],</span>
    <span class="n">template_variable_presets</span><span class="o">=</span><span class="p">[</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardTemplateVariablePresetArgs</span><span class="p">(</span>
        <span class="n">name</span><span class="o">=</span><span class="s2">&quot;preset_1&quot;</span><span class="p">,</span>
        <span class="n">template_variables</span><span class="o">=</span><span class="p">[</span>
            <span class="p">{</span>
                <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;var_1&quot;</span><span class="p">,</span>
                <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;host.dc&quot;</span><span class="p">,</span>
            <span class="p">},</span>
            <span class="p">{</span>
                <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;var_2&quot;</span><span class="p">,</span>
                <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;my_service&quot;</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">],</span>
    <span class="p">)],</span>
    <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Ordered Layout Dashboard&quot;</span><span class="p">,</span>
    <span class="n">widgets</span><span class="o">=</span><span class="p">[</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetArgs</span><span class="p">(</span>
            <span class="n">alert_graph_definition</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetAlertGraphDefinitionArgs</span><span class="p">(</span>
                <span class="n">alert_id</span><span class="o">=</span><span class="s2">&quot;895605&quot;</span><span class="p">,</span>
                <span class="n">time</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetAlertGraphDefinitionTimeArgs</span><span class="p">(</span>
                    <span class="n">live_span</span><span class="o">=</span><span class="s2">&quot;1h&quot;</span><span class="p">,</span>
                <span class="p">),</span>
                <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Widget Title&quot;</span><span class="p">,</span>
                <span class="n">viz_type</span><span class="o">=</span><span class="s2">&quot;timeseries&quot;</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetArgs</span><span class="p">(</span>
            <span class="n">alert_value_definition</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetAlertValueDefinitionArgs</span><span class="p">(</span>
                <span class="n">alert_id</span><span class="o">=</span><span class="s2">&quot;895605&quot;</span><span class="p">,</span>
                <span class="n">precision</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
                <span class="n">text_align</span><span class="o">=</span><span class="s2">&quot;center&quot;</span><span class="p">,</span>
                <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Widget Title&quot;</span><span class="p">,</span>
                <span class="n">unit</span><span class="o">=</span><span class="s2">&quot;b&quot;</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetArgs</span><span class="p">(</span>
            <span class="n">alert_value_definition</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetAlertValueDefinitionArgs</span><span class="p">(</span>
                <span class="n">alert_id</span><span class="o">=</span><span class="s2">&quot;895605&quot;</span><span class="p">,</span>
                <span class="n">precision</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
                <span class="n">text_align</span><span class="o">=</span><span class="s2">&quot;center&quot;</span><span class="p">,</span>
                <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Widget Title&quot;</span><span class="p">,</span>
                <span class="n">unit</span><span class="o">=</span><span class="s2">&quot;b&quot;</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetArgs</span><span class="p">(</span>
            <span class="n">change_definition</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetChangeDefinitionArgs</span><span class="p">(</span>
                <span class="n">request</span><span class="o">=</span><span class="p">[{</span>
                    <span class="s2">&quot;changeType&quot;</span><span class="p">:</span> <span class="s2">&quot;absolute&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;compareTo&quot;</span><span class="p">:</span> <span class="s2">&quot;week_before&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;increaseGood&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
                    <span class="s2">&quot;orderBy&quot;</span><span class="p">:</span> <span class="s2">&quot;name&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;orderDir&quot;</span><span class="p">:</span> <span class="s2">&quot;desc&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;q&quot;</span><span class="p">:</span> <span class="s2">&quot;avg:system.load.1{env:staging} by </span><span class="si">{account}</span><span class="s2">&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;showPresent&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
                <span class="p">}],</span>
                <span class="n">time</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetChangeDefinitionTimeArgs</span><span class="p">(</span>
                    <span class="n">live_span</span><span class="o">=</span><span class="s2">&quot;1h&quot;</span><span class="p">,</span>
                <span class="p">),</span>
                <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Widget Title&quot;</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetArgs</span><span class="p">(</span>
            <span class="n">distribution_definition</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetDistributionDefinitionArgs</span><span class="p">(</span>
                <span class="n">request</span><span class="o">=</span><span class="p">[{</span>
                    <span class="s2">&quot;q&quot;</span><span class="p">:</span> <span class="s2">&quot;avg:system.load.1{env:staging} by </span><span class="si">{account}</span><span class="s2">&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;style&quot;</span><span class="p">:</span> <span class="p">{</span>
                        <span class="s2">&quot;palette&quot;</span><span class="p">:</span> <span class="s2">&quot;warm&quot;</span><span class="p">,</span>
                    <span class="p">},</span>
                <span class="p">}],</span>
                <span class="n">time</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetDistributionDefinitionTimeArgs</span><span class="p">(</span>
                    <span class="n">live_span</span><span class="o">=</span><span class="s2">&quot;1h&quot;</span><span class="p">,</span>
                <span class="p">),</span>
                <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Widget Title&quot;</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetArgs</span><span class="p">(</span>
            <span class="n">check_status_definition</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetCheckStatusDefinitionArgs</span><span class="p">(</span>
                <span class="n">check</span><span class="o">=</span><span class="s2">&quot;aws.ecs.agent_connected&quot;</span><span class="p">,</span>
                <span class="n">group_by</span><span class="o">=</span><span class="p">[</span>
                    <span class="s2">&quot;account&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;cluster&quot;</span><span class="p">,</span>
                <span class="p">],</span>
                <span class="n">grouping</span><span class="o">=</span><span class="s2">&quot;cluster&quot;</span><span class="p">,</span>
                <span class="n">tags</span><span class="o">=</span><span class="p">[</span>
                    <span class="s2">&quot;account:demo&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;cluster:awseb-ruthebdog-env-8-dn3m6u3gvk&quot;</span><span class="p">,</span>
                <span class="p">],</span>
                <span class="n">time</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetCheckStatusDefinitionTimeArgs</span><span class="p">(</span>
                    <span class="n">live_span</span><span class="o">=</span><span class="s2">&quot;1h&quot;</span><span class="p">,</span>
                <span class="p">),</span>
                <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Widget Title&quot;</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetArgs</span><span class="p">(</span>
            <span class="n">heatmap_definition</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetHeatmapDefinitionArgs</span><span class="p">(</span>
                <span class="n">request</span><span class="o">=</span><span class="p">[{</span>
                    <span class="s2">&quot;q&quot;</span><span class="p">:</span> <span class="s2">&quot;avg:system.load.1{env:staging} by </span><span class="si">{account}</span><span class="s2">&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;style&quot;</span><span class="p">:</span> <span class="p">{</span>
                        <span class="s2">&quot;palette&quot;</span><span class="p">:</span> <span class="s2">&quot;warm&quot;</span><span class="p">,</span>
                    <span class="p">},</span>
                <span class="p">}],</span>
                <span class="n">time</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetHeatmapDefinitionTimeArgs</span><span class="p">(</span>
                    <span class="n">live_span</span><span class="o">=</span><span class="s2">&quot;1h&quot;</span><span class="p">,</span>
                <span class="p">),</span>
                <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Widget Title&quot;</span><span class="p">,</span>
                <span class="n">yaxis</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetHeatmapDefinitionYaxisArgs</span><span class="p">(</span>
                    <span class="n">include_zero</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                    <span class="nb">max</span><span class="o">=</span><span class="s2">&quot;2&quot;</span><span class="p">,</span>
                    <span class="nb">min</span><span class="o">=</span><span class="s2">&quot;1&quot;</span><span class="p">,</span>
                    <span class="n">scale</span><span class="o">=</span><span class="s2">&quot;sqrt&quot;</span><span class="p">,</span>
                <span class="p">),</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetArgs</span><span class="p">(</span>
            <span class="n">hostmap_definition</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetHostmapDefinitionArgs</span><span class="p">(</span>
                <span class="n">group</span><span class="o">=</span><span class="p">[</span>
                    <span class="s2">&quot;host&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;region&quot;</span><span class="p">,</span>
                <span class="p">],</span>
                <span class="n">no_group_hosts</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">no_metric_hosts</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">node_type</span><span class="o">=</span><span class="s2">&quot;container&quot;</span><span class="p">,</span>
                <span class="n">request</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetHostmapDefinitionRequestArgs</span><span class="p">(</span>
                    <span class="n">fill</span><span class="o">=</span><span class="p">[{</span>
                        <span class="s2">&quot;q&quot;</span><span class="p">:</span> <span class="s2">&quot;avg:system.load.1{*} by </span><span class="si">{host}</span><span class="s2">&quot;</span><span class="p">,</span>
                    <span class="p">}],</span>
                    <span class="n">size</span><span class="o">=</span><span class="p">[{</span>
                        <span class="s2">&quot;q&quot;</span><span class="p">:</span> <span class="s2">&quot;avg:memcache.uptime{*} by </span><span class="si">{host}</span><span class="s2">&quot;</span><span class="p">,</span>
                    <span class="p">}],</span>
                <span class="p">),</span>
                <span class="n">scope</span><span class="o">=</span><span class="p">[</span>
                    <span class="s2">&quot;region:us-east-1&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;aws_account:727006795293&quot;</span><span class="p">,</span>
                <span class="p">],</span>
                <span class="n">style</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetHostmapDefinitionStyleArgs</span><span class="p">(</span>
                    <span class="n">fill_max</span><span class="o">=</span><span class="s2">&quot;20&quot;</span><span class="p">,</span>
                    <span class="n">fill_min</span><span class="o">=</span><span class="s2">&quot;10&quot;</span><span class="p">,</span>
                    <span class="n">palette</span><span class="o">=</span><span class="s2">&quot;yellow_to_green&quot;</span><span class="p">,</span>
                    <span class="n">palette_flip</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="p">),</span>
                <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Widget Title&quot;</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetArgs</span><span class="p">(</span>
            <span class="n">note_definition</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetNoteDefinitionArgs</span><span class="p">(</span>
                <span class="n">background_color</span><span class="o">=</span><span class="s2">&quot;pink&quot;</span><span class="p">,</span>
                <span class="n">content</span><span class="o">=</span><span class="s2">&quot;note text&quot;</span><span class="p">,</span>
                <span class="n">font_size</span><span class="o">=</span><span class="s2">&quot;14&quot;</span><span class="p">,</span>
                <span class="n">show_tick</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">text_align</span><span class="o">=</span><span class="s2">&quot;center&quot;</span><span class="p">,</span>
                <span class="n">tick_edge</span><span class="o">=</span><span class="s2">&quot;left&quot;</span><span class="p">,</span>
                <span class="n">tick_pos</span><span class="o">=</span><span class="s2">&quot;50%&quot;</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetArgs</span><span class="p">(</span>
            <span class="n">query_value_definition</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetQueryValueDefinitionArgs</span><span class="p">(</span>
                <span class="n">autoscale</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">custom_unit</span><span class="o">=</span><span class="s2">&quot;xx&quot;</span><span class="p">,</span>
                <span class="n">precision</span><span class="o">=</span><span class="mi">4</span><span class="p">,</span>
                <span class="n">request</span><span class="o">=</span><span class="p">[{</span>
                    <span class="s2">&quot;aggregator&quot;</span><span class="p">:</span> <span class="s2">&quot;sum&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;conditionalFormats&quot;</span><span class="p">:</span> <span class="p">[</span>
                        <span class="p">{</span>
                            <span class="s2">&quot;comparator&quot;</span><span class="p">:</span> <span class="s2">&quot;&lt;&quot;</span><span class="p">,</span>
                            <span class="s2">&quot;palette&quot;</span><span class="p">:</span> <span class="s2">&quot;white_on_green&quot;</span><span class="p">,</span>
                            <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;2&quot;</span><span class="p">,</span>
                        <span class="p">},</span>
                        <span class="p">{</span>
                            <span class="s2">&quot;comparator&quot;</span><span class="p">:</span> <span class="s2">&quot;&gt;&quot;</span><span class="p">,</span>
                            <span class="s2">&quot;palette&quot;</span><span class="p">:</span> <span class="s2">&quot;white_on_red&quot;</span><span class="p">,</span>
                            <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;2.2&quot;</span><span class="p">,</span>
                        <span class="p">},</span>
                    <span class="p">],</span>
                    <span class="s2">&quot;q&quot;</span><span class="p">:</span> <span class="s2">&quot;avg:system.load.1{env:staging} by </span><span class="si">{account}</span><span class="s2">&quot;</span><span class="p">,</span>
                <span class="p">}],</span>
                <span class="n">text_align</span><span class="o">=</span><span class="s2">&quot;right&quot;</span><span class="p">,</span>
                <span class="n">time</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetQueryValueDefinitionTimeArgs</span><span class="p">(</span>
                    <span class="n">live_span</span><span class="o">=</span><span class="s2">&quot;1h&quot;</span><span class="p">,</span>
                <span class="p">),</span>
                <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Widget Title&quot;</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetArgs</span><span class="p">(</span>
            <span class="n">query_table_definition</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetQueryTableDefinitionArgs</span><span class="p">(</span>
                <span class="n">request</span><span class="o">=</span><span class="p">[{</span>
                    <span class="s2">&quot;aggregator&quot;</span><span class="p">:</span> <span class="s2">&quot;sum&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;conditionalFormats&quot;</span><span class="p">:</span> <span class="p">[</span>
                        <span class="p">{</span>
                            <span class="s2">&quot;comparator&quot;</span><span class="p">:</span> <span class="s2">&quot;&lt;&quot;</span><span class="p">,</span>
                            <span class="s2">&quot;palette&quot;</span><span class="p">:</span> <span class="s2">&quot;white_on_green&quot;</span><span class="p">,</span>
                            <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;2&quot;</span><span class="p">,</span>
                        <span class="p">},</span>
                        <span class="p">{</span>
                            <span class="s2">&quot;comparator&quot;</span><span class="p">:</span> <span class="s2">&quot;&gt;&quot;</span><span class="p">,</span>
                            <span class="s2">&quot;palette&quot;</span><span class="p">:</span> <span class="s2">&quot;white_on_red&quot;</span><span class="p">,</span>
                            <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;2.2&quot;</span><span class="p">,</span>
                        <span class="p">},</span>
                    <span class="p">],</span>
                    <span class="s2">&quot;limit&quot;</span><span class="p">:</span> <span class="s2">&quot;10&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;q&quot;</span><span class="p">:</span> <span class="s2">&quot;avg:system.load.1{env:staging} by </span><span class="si">{account}</span><span class="s2">&quot;</span><span class="p">,</span>
                <span class="p">}],</span>
                <span class="n">time</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetQueryTableDefinitionTimeArgs</span><span class="p">(</span>
                    <span class="n">live_span</span><span class="o">=</span><span class="s2">&quot;1h&quot;</span><span class="p">,</span>
                <span class="p">),</span>
                <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Widget Title&quot;</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetArgs</span><span class="p">(</span>
            <span class="n">scatterplot_definition</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetScatterplotDefinitionArgs</span><span class="p">(</span>
                <span class="n">color_by_groups</span><span class="o">=</span><span class="p">[</span>
                    <span class="s2">&quot;account&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;apm-role-group&quot;</span><span class="p">,</span>
                <span class="p">],</span>
                <span class="n">request</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetScatterplotDefinitionRequestArgs</span><span class="p">(</span>
                    <span class="n">x</span><span class="o">=</span><span class="p">[{</span>
                        <span class="s2">&quot;aggregator&quot;</span><span class="p">:</span> <span class="s2">&quot;max&quot;</span><span class="p">,</span>
                        <span class="s2">&quot;q&quot;</span><span class="p">:</span> <span class="s2">&quot;avg:system.cpu.user{*} by {service, account}&quot;</span><span class="p">,</span>
                    <span class="p">}],</span>
                    <span class="n">y</span><span class="o">=</span><span class="p">[{</span>
                        <span class="s2">&quot;aggregator&quot;</span><span class="p">:</span> <span class="s2">&quot;min&quot;</span><span class="p">,</span>
                        <span class="s2">&quot;q&quot;</span><span class="p">:</span> <span class="s2">&quot;avg:system.mem.used{*} by {service, account}&quot;</span><span class="p">,</span>
                    <span class="p">}],</span>
                <span class="p">),</span>
                <span class="n">time</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetScatterplotDefinitionTimeArgs</span><span class="p">(</span>
                    <span class="n">live_span</span><span class="o">=</span><span class="s2">&quot;1h&quot;</span><span class="p">,</span>
                <span class="p">),</span>
                <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Widget Title&quot;</span><span class="p">,</span>
                <span class="n">xaxis</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetScatterplotDefinitionXaxisArgs</span><span class="p">(</span>
                    <span class="n">include_zero</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                    <span class="n">label</span><span class="o">=</span><span class="s2">&quot;x&quot;</span><span class="p">,</span>
                    <span class="nb">max</span><span class="o">=</span><span class="s2">&quot;2000&quot;</span><span class="p">,</span>
                    <span class="nb">min</span><span class="o">=</span><span class="s2">&quot;1&quot;</span><span class="p">,</span>
                    <span class="n">scale</span><span class="o">=</span><span class="s2">&quot;pow&quot;</span><span class="p">,</span>
                <span class="p">),</span>
                <span class="n">yaxis</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetScatterplotDefinitionYaxisArgs</span><span class="p">(</span>
                    <span class="n">include_zero</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
                    <span class="n">label</span><span class="o">=</span><span class="s2">&quot;y&quot;</span><span class="p">,</span>
                    <span class="nb">max</span><span class="o">=</span><span class="s2">&quot;2222&quot;</span><span class="p">,</span>
                    <span class="nb">min</span><span class="o">=</span><span class="s2">&quot;5&quot;</span><span class="p">,</span>
                    <span class="n">scale</span><span class="o">=</span><span class="s2">&quot;log&quot;</span><span class="p">,</span>
                <span class="p">),</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetArgs</span><span class="p">(</span>
            <span class="n">layout</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetLayoutArgs</span><span class="p">(</span>
                <span class="n">height</span><span class="o">=</span><span class="mi">43</span><span class="p">,</span>
                <span class="n">width</span><span class="o">=</span><span class="mi">32</span><span class="p">,</span>
                <span class="n">x</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
                <span class="n">y</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
            <span class="p">),</span>
            <span class="n">servicemap_definition</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetServicemapDefinitionArgs</span><span class="p">(</span>
                <span class="n">filters</span><span class="o">=</span><span class="p">[</span>
                    <span class="s2">&quot;env:prod&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;datacenter:us1.prod.dog&quot;</span><span class="p">,</span>
                <span class="p">],</span>
                <span class="n">service</span><span class="o">=</span><span class="s2">&quot;master-db&quot;</span><span class="p">,</span>
                <span class="n">title</span><span class="o">=</span><span class="s2">&quot;env: prod, datacenter:us1.prod.dog, service: master-db&quot;</span><span class="p">,</span>
                <span class="n">title_align</span><span class="o">=</span><span class="s2">&quot;left&quot;</span><span class="p">,</span>
                <span class="n">title_size</span><span class="o">=</span><span class="s2">&quot;16&quot;</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetArgs</span><span class="p">(</span>
            <span class="n">timeseries_definition</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetTimeseriesDefinitionArgs</span><span class="p">(</span>
                <span class="n">event</span><span class="o">=</span><span class="p">[</span>
                    <span class="p">{</span>
                        <span class="s2">&quot;q&quot;</span><span class="p">:</span> <span class="s2">&quot;sources:test tags:1&quot;</span><span class="p">,</span>
                    <span class="p">},</span>
                    <span class="p">{</span>
                        <span class="s2">&quot;q&quot;</span><span class="p">:</span> <span class="s2">&quot;sources:test tags:2&quot;</span><span class="p">,</span>
                    <span class="p">},</span>
                <span class="p">],</span>
                <span class="n">legend_size</span><span class="o">=</span><span class="s2">&quot;2&quot;</span><span class="p">,</span>
                <span class="n">marker</span><span class="o">=</span><span class="p">[</span>
                    <span class="p">{</span>
                        <span class="s2">&quot;displayType&quot;</span><span class="p">:</span> <span class="s2">&quot;error dashed&quot;</span><span class="p">,</span>
                        <span class="s2">&quot;label&quot;</span><span class="p">:</span> <span class="s2">&quot; z=6 &quot;</span><span class="p">,</span>
                        <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;y = 4&quot;</span><span class="p">,</span>
                    <span class="p">},</span>
                    <span class="p">{</span>
                        <span class="s2">&quot;displayType&quot;</span><span class="p">:</span> <span class="s2">&quot;ok solid&quot;</span><span class="p">,</span>
                        <span class="s2">&quot;label&quot;</span><span class="p">:</span> <span class="s2">&quot; x=8 &quot;</span><span class="p">,</span>
                        <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;10 &lt; y &lt; 999&quot;</span><span class="p">,</span>
                    <span class="p">},</span>
                <span class="p">],</span>
                <span class="n">request</span><span class="o">=</span><span class="p">[</span>
                    <span class="p">{</span>
                        <span class="s2">&quot;displayType&quot;</span><span class="p">:</span> <span class="s2">&quot;line&quot;</span><span class="p">,</span>
                        <span class="s2">&quot;metadata&quot;</span><span class="p">:</span> <span class="p">[{</span>
                            <span class="s2">&quot;aliasName&quot;</span><span class="p">:</span> <span class="s2">&quot;Alpha&quot;</span><span class="p">,</span>
                            <span class="s2">&quot;expression&quot;</span><span class="p">:</span> <span class="s2">&quot;avg:system.cpu.user{app:general} by </span><span class="si">{env}</span><span class="s2">&quot;</span><span class="p">,</span>
                        <span class="p">}],</span>
                        <span class="s2">&quot;q&quot;</span><span class="p">:</span> <span class="s2">&quot;avg:system.cpu.user{app:general} by </span><span class="si">{env}</span><span class="s2">&quot;</span><span class="p">,</span>
                        <span class="s2">&quot;style&quot;</span><span class="p">:</span> <span class="p">{</span>
                            <span class="s2">&quot;lineType&quot;</span><span class="p">:</span> <span class="s2">&quot;dashed&quot;</span><span class="p">,</span>
                            <span class="s2">&quot;lineWidth&quot;</span><span class="p">:</span> <span class="s2">&quot;thin&quot;</span><span class="p">,</span>
                            <span class="s2">&quot;palette&quot;</span><span class="p">:</span> <span class="s2">&quot;warm&quot;</span><span class="p">,</span>
                        <span class="p">},</span>
                    <span class="p">},</span>
                    <span class="p">{</span>
                        <span class="s2">&quot;displayType&quot;</span><span class="p">:</span> <span class="s2">&quot;area&quot;</span><span class="p">,</span>
                        <span class="s2">&quot;logQuery&quot;</span><span class="p">:</span> <span class="p">{</span>
                            <span class="s2">&quot;compute&quot;</span><span class="p">:</span> <span class="p">{</span>
                                <span class="s2">&quot;aggregation&quot;</span><span class="p">:</span> <span class="s2">&quot;avg&quot;</span><span class="p">,</span>
                                <span class="s2">&quot;facet&quot;</span><span class="p">:</span> <span class="s2">&quot;@duration&quot;</span><span class="p">,</span>
                                <span class="s2">&quot;interval&quot;</span><span class="p">:</span> <span class="mi">5000</span><span class="p">,</span>
                            <span class="p">},</span>
                            <span class="s2">&quot;groupBy&quot;</span><span class="p">:</span> <span class="p">[{</span>
                                <span class="s2">&quot;facet&quot;</span><span class="p">:</span> <span class="s2">&quot;host&quot;</span><span class="p">,</span>
                                <span class="s2">&quot;limit&quot;</span><span class="p">:</span> <span class="mi">10</span><span class="p">,</span>
                                <span class="s2">&quot;sort&quot;</span><span class="p">:</span> <span class="p">{</span>
                                    <span class="s2">&quot;aggregation&quot;</span><span class="p">:</span> <span class="s2">&quot;avg&quot;</span><span class="p">,</span>
                                    <span class="s2">&quot;facet&quot;</span><span class="p">:</span> <span class="s2">&quot;@duration&quot;</span><span class="p">,</span>
                                    <span class="s2">&quot;order&quot;</span><span class="p">:</span> <span class="s2">&quot;desc&quot;</span><span class="p">,</span>
                                <span class="p">},</span>
                            <span class="p">}],</span>
                            <span class="s2">&quot;index&quot;</span><span class="p">:</span> <span class="s2">&quot;mcnulty&quot;</span><span class="p">,</span>
                            <span class="s2">&quot;search&quot;</span><span class="p">:</span> <span class="p">{</span>
                                <span class="s2">&quot;query&quot;</span><span class="p">:</span> <span class="s2">&quot;status:info&quot;</span><span class="p">,</span>
                            <span class="p">},</span>
                        <span class="p">},</span>
                    <span class="p">},</span>
                    <span class="p">{</span>
                        <span class="s2">&quot;apmQuery&quot;</span><span class="p">:</span> <span class="p">{</span>
                            <span class="s2">&quot;compute&quot;</span><span class="p">:</span> <span class="p">{</span>
                                <span class="s2">&quot;aggregation&quot;</span><span class="p">:</span> <span class="s2">&quot;avg&quot;</span><span class="p">,</span>
                                <span class="s2">&quot;facet&quot;</span><span class="p">:</span> <span class="s2">&quot;@duration&quot;</span><span class="p">,</span>
                                <span class="s2">&quot;interval&quot;</span><span class="p">:</span> <span class="mi">5000</span><span class="p">,</span>
                            <span class="p">},</span>
                            <span class="s2">&quot;groupBy&quot;</span><span class="p">:</span> <span class="p">[{</span>
                                <span class="s2">&quot;facet&quot;</span><span class="p">:</span> <span class="s2">&quot;resource_name&quot;</span><span class="p">,</span>
                                <span class="s2">&quot;limit&quot;</span><span class="p">:</span> <span class="mi">50</span><span class="p">,</span>
                                <span class="s2">&quot;sort&quot;</span><span class="p">:</span> <span class="p">{</span>
                                    <span class="s2">&quot;aggregation&quot;</span><span class="p">:</span> <span class="s2">&quot;avg&quot;</span><span class="p">,</span>
                                    <span class="s2">&quot;facet&quot;</span><span class="p">:</span> <span class="s2">&quot;@string_query.interval&quot;</span><span class="p">,</span>
                                    <span class="s2">&quot;order&quot;</span><span class="p">:</span> <span class="s2">&quot;desc&quot;</span><span class="p">,</span>
                                <span class="p">},</span>
                            <span class="p">}],</span>
                            <span class="s2">&quot;index&quot;</span><span class="p">:</span> <span class="s2">&quot;apm-search&quot;</span><span class="p">,</span>
                            <span class="s2">&quot;search&quot;</span><span class="p">:</span> <span class="p">{</span>
                                <span class="s2">&quot;query&quot;</span><span class="p">:</span> <span class="s2">&quot;type:web&quot;</span><span class="p">,</span>
                            <span class="p">},</span>
                        <span class="p">},</span>
                        <span class="s2">&quot;displayType&quot;</span><span class="p">:</span> <span class="s2">&quot;bars&quot;</span><span class="p">,</span>
                    <span class="p">},</span>
                    <span class="p">{</span>
                        <span class="s2">&quot;displayType&quot;</span><span class="p">:</span> <span class="s2">&quot;area&quot;</span><span class="p">,</span>
                        <span class="s2">&quot;processQuery&quot;</span><span class="p">:</span> <span class="p">{</span>
                            <span class="s2">&quot;filterBy&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;active&quot;</span><span class="p">],</span>
                            <span class="s2">&quot;limit&quot;</span><span class="p">:</span> <span class="mi">50</span><span class="p">,</span>
                            <span class="s2">&quot;metric&quot;</span><span class="p">:</span> <span class="s2">&quot;process.stat.cpu.total_pct&quot;</span><span class="p">,</span>
                            <span class="s2">&quot;searchBy&quot;</span><span class="p">:</span> <span class="s2">&quot;error&quot;</span><span class="p">,</span>
                        <span class="p">},</span>
                    <span class="p">},</span>
                <span class="p">],</span>
                <span class="n">show_legend</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">time</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetTimeseriesDefinitionTimeArgs</span><span class="p">(</span>
                    <span class="n">live_span</span><span class="o">=</span><span class="s2">&quot;1h&quot;</span><span class="p">,</span>
                <span class="p">),</span>
                <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Widget Title&quot;</span><span class="p">,</span>
                <span class="n">yaxis</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetTimeseriesDefinitionYaxisArgs</span><span class="p">(</span>
                    <span class="n">include_zero</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
                    <span class="nb">max</span><span class="o">=</span><span class="s2">&quot;100&quot;</span><span class="p">,</span>
                    <span class="n">scale</span><span class="o">=</span><span class="s2">&quot;log&quot;</span><span class="p">,</span>
                <span class="p">),</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetArgs</span><span class="p">(</span>
            <span class="n">toplist_definition</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetToplistDefinitionArgs</span><span class="p">(</span>
                <span class="n">request</span><span class="o">=</span><span class="p">[{</span>
                    <span class="s2">&quot;conditionalFormats&quot;</span><span class="p">:</span> <span class="p">[</span>
                        <span class="p">{</span>
                            <span class="s2">&quot;comparator&quot;</span><span class="p">:</span> <span class="s2">&quot;&lt;&quot;</span><span class="p">,</span>
                            <span class="s2">&quot;palette&quot;</span><span class="p">:</span> <span class="s2">&quot;white_on_green&quot;</span><span class="p">,</span>
                            <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;2&quot;</span><span class="p">,</span>
                        <span class="p">},</span>
                        <span class="p">{</span>
                            <span class="s2">&quot;comparator&quot;</span><span class="p">:</span> <span class="s2">&quot;&gt;&quot;</span><span class="p">,</span>
                            <span class="s2">&quot;palette&quot;</span><span class="p">:</span> <span class="s2">&quot;white_on_red&quot;</span><span class="p">,</span>
                            <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;2.2&quot;</span><span class="p">,</span>
                        <span class="p">},</span>
                    <span class="p">],</span>
                    <span class="s2">&quot;q&quot;</span><span class="p">:</span> <span class="s2">&quot;avg:system.cpu.user{app:general} by </span><span class="si">{env}</span><span class="s2">&quot;</span><span class="p">,</span>
                <span class="p">}],</span>
                <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Widget Title&quot;</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetArgs</span><span class="p">(</span>
            <span class="n">group_definition</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetGroupDefinitionArgs</span><span class="p">(</span>
                <span class="n">layout_type</span><span class="o">=</span><span class="s2">&quot;ordered&quot;</span><span class="p">,</span>
                <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Group Widget&quot;</span><span class="p">,</span>
                <span class="n">widget</span><span class="o">=</span><span class="p">[</span>
                    <span class="p">{</span>
                        <span class="s2">&quot;noteDefinition&quot;</span><span class="p">:</span> <span class="p">{</span>
                            <span class="s2">&quot;backgroundColor&quot;</span><span class="p">:</span> <span class="s2">&quot;pink&quot;</span><span class="p">,</span>
                            <span class="s2">&quot;content&quot;</span><span class="p">:</span> <span class="s2">&quot;cluster note widget&quot;</span><span class="p">,</span>
                            <span class="s2">&quot;fontSize&quot;</span><span class="p">:</span> <span class="s2">&quot;14&quot;</span><span class="p">,</span>
                            <span class="s2">&quot;showTick&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
                            <span class="s2">&quot;textAlign&quot;</span><span class="p">:</span> <span class="s2">&quot;center&quot;</span><span class="p">,</span>
                            <span class="s2">&quot;tickEdge&quot;</span><span class="p">:</span> <span class="s2">&quot;left&quot;</span><span class="p">,</span>
                            <span class="s2">&quot;tickPos&quot;</span><span class="p">:</span> <span class="s2">&quot;50%&quot;</span><span class="p">,</span>
                        <span class="p">},</span>
                    <span class="p">},</span>
                    <span class="p">{</span>
                        <span class="s2">&quot;alertGraphDefinition&quot;</span><span class="p">:</span> <span class="p">{</span>
                            <span class="s2">&quot;alertId&quot;</span><span class="p">:</span> <span class="s2">&quot;123&quot;</span><span class="p">,</span>
                            <span class="s2">&quot;time&quot;</span><span class="p">:</span> <span class="p">{</span>
                                <span class="s2">&quot;liveSpan&quot;</span><span class="p">:</span> <span class="s2">&quot;1h&quot;</span><span class="p">,</span>
                            <span class="p">},</span>
                            <span class="s2">&quot;title&quot;</span><span class="p">:</span> <span class="s2">&quot;Alert Graph&quot;</span><span class="p">,</span>
                            <span class="s2">&quot;vizType&quot;</span><span class="p">:</span> <span class="s2">&quot;toplist&quot;</span><span class="p">,</span>
                        <span class="p">},</span>
                    <span class="p">},</span>
                <span class="p">],</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetArgs</span><span class="p">(</span>
            <span class="n">service_level_objective_definition</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetServiceLevelObjectiveDefinitionArgs</span><span class="p">(</span>
                <span class="n">show_error_budget</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">slo_id</span><span class="o">=</span><span class="s2">&quot;56789&quot;</span><span class="p">,</span>
                <span class="n">time_windows</span><span class="o">=</span><span class="p">[</span>
                    <span class="s2">&quot;7d&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;previous_week&quot;</span><span class="p">,</span>
                <span class="p">],</span>
                <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Widget Title&quot;</span><span class="p">,</span>
                <span class="n">view_mode</span><span class="o">=</span><span class="s2">&quot;overall&quot;</span><span class="p">,</span>
                <span class="n">view_type</span><span class="o">=</span><span class="s2">&quot;detail&quot;</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">),</span>
    <span class="p">])</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="n">free_dashboard</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">Dashboard</span><span class="p">(</span><span class="s2">&quot;freeDashboard&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Created using the Datadog provider in Terraform&quot;</span><span class="p">,</span>
    <span class="n">is_read_only</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">layout_type</span><span class="o">=</span><span class="s2">&quot;free&quot;</span><span class="p">,</span>
    <span class="n">template_variables</span><span class="o">=</span><span class="p">[</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">DashboardTemplateVariableArgs</span><span class="p">(</span>
            <span class="n">default</span><span class="o">=</span><span class="s2">&quot;aws&quot;</span><span class="p">,</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">&quot;var_1&quot;</span><span class="p">,</span>
            <span class="n">prefix</span><span class="o">=</span><span class="s2">&quot;host&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">DashboardTemplateVariableArgs</span><span class="p">(</span>
            <span class="n">default</span><span class="o">=</span><span class="s2">&quot;autoscaling&quot;</span><span class="p">,</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">&quot;var_2&quot;</span><span class="p">,</span>
            <span class="n">prefix</span><span class="o">=</span><span class="s2">&quot;service_name&quot;</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">],</span>
    <span class="n">template_variable_presets</span><span class="o">=</span><span class="p">[</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardTemplateVariablePresetArgs</span><span class="p">(</span>
        <span class="n">name</span><span class="o">=</span><span class="s2">&quot;preset_1&quot;</span><span class="p">,</span>
        <span class="n">template_variables</span><span class="o">=</span><span class="p">[</span>
            <span class="p">{</span>
                <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;var_1&quot;</span><span class="p">,</span>
                <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;host.dc&quot;</span><span class="p">,</span>
            <span class="p">},</span>
            <span class="p">{</span>
                <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;var_2&quot;</span><span class="p">,</span>
                <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;my_service&quot;</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">],</span>
    <span class="p">)],</span>
    <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Free Layout Dashboard&quot;</span><span class="p">,</span>
    <span class="n">widgets</span><span class="o">=</span><span class="p">[</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetArgs</span><span class="p">(</span>
            <span class="n">event_stream_definition</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetEventStreamDefinitionArgs</span><span class="p">(</span>
                <span class="n">event_size</span><span class="o">=</span><span class="s2">&quot;l&quot;</span><span class="p">,</span>
                <span class="n">query</span><span class="o">=</span><span class="s2">&quot;*&quot;</span><span class="p">,</span>
                <span class="n">time</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetEventStreamDefinitionTimeArgs</span><span class="p">(</span>
                    <span class="n">live_span</span><span class="o">=</span><span class="s2">&quot;1h&quot;</span><span class="p">,</span>
                <span class="p">),</span>
                <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Widget Title&quot;</span><span class="p">,</span>
                <span class="n">title_align</span><span class="o">=</span><span class="s2">&quot;left&quot;</span><span class="p">,</span>
                <span class="n">title_size</span><span class="o">=</span><span class="s2">&quot;16&quot;</span><span class="p">,</span>
            <span class="p">),</span>
            <span class="n">layout</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetLayoutArgs</span><span class="p">(</span>
                <span class="n">height</span><span class="o">=</span><span class="mi">43</span><span class="p">,</span>
                <span class="n">width</span><span class="o">=</span><span class="mi">32</span><span class="p">,</span>
                <span class="n">x</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
                <span class="n">y</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetArgs</span><span class="p">(</span>
            <span class="n">event_timeline_definition</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetEventTimelineDefinitionArgs</span><span class="p">(</span>
                <span class="n">query</span><span class="o">=</span><span class="s2">&quot;*&quot;</span><span class="p">,</span>
                <span class="n">time</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetEventTimelineDefinitionTimeArgs</span><span class="p">(</span>
                    <span class="n">live_span</span><span class="o">=</span><span class="s2">&quot;1h&quot;</span><span class="p">,</span>
                <span class="p">),</span>
                <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Widget Title&quot;</span><span class="p">,</span>
                <span class="n">title_align</span><span class="o">=</span><span class="s2">&quot;left&quot;</span><span class="p">,</span>
                <span class="n">title_size</span><span class="o">=</span><span class="s2">&quot;16&quot;</span><span class="p">,</span>
            <span class="p">),</span>
            <span class="n">layout</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetLayoutArgs</span><span class="p">(</span>
                <span class="n">height</span><span class="o">=</span><span class="mi">9</span><span class="p">,</span>
                <span class="n">width</span><span class="o">=</span><span class="mi">65</span><span class="p">,</span>
                <span class="n">x</span><span class="o">=</span><span class="mi">42</span><span class="p">,</span>
                <span class="n">y</span><span class="o">=</span><span class="mi">73</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetArgs</span><span class="p">(</span>
            <span class="n">free_text_definition</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetFreeTextDefinitionArgs</span><span class="p">(</span>
                <span class="n">color</span><span class="o">=</span><span class="s2">&quot;#d00&quot;</span><span class="p">,</span>
                <span class="n">font_size</span><span class="o">=</span><span class="s2">&quot;88&quot;</span><span class="p">,</span>
                <span class="n">text</span><span class="o">=</span><span class="s2">&quot;free text content&quot;</span><span class="p">,</span>
                <span class="n">text_align</span><span class="o">=</span><span class="s2">&quot;left&quot;</span><span class="p">,</span>
            <span class="p">),</span>
            <span class="n">layout</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetLayoutArgs</span><span class="p">(</span>
                <span class="n">height</span><span class="o">=</span><span class="mi">20</span><span class="p">,</span>
                <span class="n">width</span><span class="o">=</span><span class="mi">30</span><span class="p">,</span>
                <span class="n">x</span><span class="o">=</span><span class="mi">42</span><span class="p">,</span>
                <span class="n">y</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetArgs</span><span class="p">(</span>
            <span class="n">iframe_definition</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetIframeDefinitionArgs</span><span class="p">(</span>
                <span class="n">url</span><span class="o">=</span><span class="s2">&quot;http://google.com&quot;</span><span class="p">,</span>
            <span class="p">),</span>
            <span class="n">layout</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetLayoutArgs</span><span class="p">(</span>
                <span class="n">height</span><span class="o">=</span><span class="mi">46</span><span class="p">,</span>
                <span class="n">width</span><span class="o">=</span><span class="mi">39</span><span class="p">,</span>
                <span class="n">x</span><span class="o">=</span><span class="mi">111</span><span class="p">,</span>
                <span class="n">y</span><span class="o">=</span><span class="mi">8</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetArgs</span><span class="p">(</span>
            <span class="n">image_definition</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetImageDefinitionArgs</span><span class="p">(</span>
                <span class="n">margin</span><span class="o">=</span><span class="s2">&quot;small&quot;</span><span class="p">,</span>
                <span class="n">sizing</span><span class="o">=</span><span class="s2">&quot;fit&quot;</span><span class="p">,</span>
                <span class="n">url</span><span class="o">=</span><span class="s2">&quot;https://images.pexels.com/photos/67636/rose-blue-flower-rose-blooms-67636.jpeg?auto=compress&amp;cs=tinysrgb&amp;h=350&quot;</span><span class="p">,</span>
            <span class="p">),</span>
            <span class="n">layout</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetLayoutArgs</span><span class="p">(</span>
                <span class="n">height</span><span class="o">=</span><span class="mi">20</span><span class="p">,</span>
                <span class="n">width</span><span class="o">=</span><span class="mi">30</span><span class="p">,</span>
                <span class="n">x</span><span class="o">=</span><span class="mi">77</span><span class="p">,</span>
                <span class="n">y</span><span class="o">=</span><span class="mi">7</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetArgs</span><span class="p">(</span>
            <span class="n">layout</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetLayoutArgs</span><span class="p">(</span>
                <span class="n">height</span><span class="o">=</span><span class="mi">36</span><span class="p">,</span>
                <span class="n">width</span><span class="o">=</span><span class="mi">32</span><span class="p">,</span>
                <span class="n">x</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
                <span class="n">y</span><span class="o">=</span><span class="mi">51</span><span class="p">,</span>
            <span class="p">),</span>
            <span class="n">log_stream_definition</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetLogStreamDefinitionArgs</span><span class="p">(</span>
                <span class="n">columns</span><span class="o">=</span><span class="p">[</span>
                    <span class="s2">&quot;core_host&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;core_service&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;tag_source&quot;</span><span class="p">,</span>
                <span class="p">],</span>
                <span class="n">indexes</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;main&quot;</span><span class="p">],</span>
                <span class="n">message_display</span><span class="o">=</span><span class="s2">&quot;expanded-md&quot;</span><span class="p">,</span>
                <span class="n">query</span><span class="o">=</span><span class="s2">&quot;error&quot;</span><span class="p">,</span>
                <span class="n">show_date_column</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">show_message_column</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">sort</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetLogStreamDefinitionSortArgs</span><span class="p">(</span>
                    <span class="n">column</span><span class="o">=</span><span class="s2">&quot;time&quot;</span><span class="p">,</span>
                    <span class="n">order</span><span class="o">=</span><span class="s2">&quot;desc&quot;</span><span class="p">,</span>
                <span class="p">),</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetArgs</span><span class="p">(</span>
            <span class="n">layout</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetLayoutArgs</span><span class="p">(</span>
                <span class="n">height</span><span class="o">=</span><span class="mi">40</span><span class="p">,</span>
                <span class="n">width</span><span class="o">=</span><span class="mi">30</span><span class="p">,</span>
                <span class="n">x</span><span class="o">=</span><span class="mi">112</span><span class="p">,</span>
                <span class="n">y</span><span class="o">=</span><span class="mi">55</span><span class="p">,</span>
            <span class="p">),</span>
            <span class="n">manage_status_definition</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetManageStatusDefinitionArgs</span><span class="p">(</span>
                <span class="n">color_preference</span><span class="o">=</span><span class="s2">&quot;text&quot;</span><span class="p">,</span>
                <span class="n">display_format</span><span class="o">=</span><span class="s2">&quot;countsAndList&quot;</span><span class="p">,</span>
                <span class="n">hide_zero_counts</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">query</span><span class="o">=</span><span class="s2">&quot;type:metric&quot;</span><span class="p">,</span>
                <span class="n">show_last_triggered</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
                <span class="n">sort</span><span class="o">=</span><span class="s2">&quot;status,asc&quot;</span><span class="p">,</span>
                <span class="n">summary_type</span><span class="o">=</span><span class="s2">&quot;monitors&quot;</span><span class="p">,</span>
                <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Widget Title&quot;</span><span class="p">,</span>
                <span class="n">title_align</span><span class="o">=</span><span class="s2">&quot;left&quot;</span><span class="p">,</span>
                <span class="n">title_size</span><span class="o">=</span><span class="s2">&quot;16&quot;</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetArgs</span><span class="p">(</span>
            <span class="n">layout</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetLayoutArgs</span><span class="p">(</span>
                <span class="n">height</span><span class="o">=</span><span class="mi">38</span><span class="p">,</span>
                <span class="n">width</span><span class="o">=</span><span class="mi">67</span><span class="p">,</span>
                <span class="n">x</span><span class="o">=</span><span class="mi">40</span><span class="p">,</span>
                <span class="n">y</span><span class="o">=</span><span class="mi">28</span><span class="p">,</span>
            <span class="p">),</span>
            <span class="n">trace_service_definition</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetTraceServiceDefinitionArgs</span><span class="p">(</span>
                <span class="n">display_format</span><span class="o">=</span><span class="s2">&quot;three_column&quot;</span><span class="p">,</span>
                <span class="n">env</span><span class="o">=</span><span class="s2">&quot;datad0g.com&quot;</span><span class="p">,</span>
                <span class="n">service</span><span class="o">=</span><span class="s2">&quot;alerting-cassandra&quot;</span><span class="p">,</span>
                <span class="n">show_breakdown</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">show_distribution</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">show_errors</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">show_hits</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">show_latency</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
                <span class="n">show_resource_list</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
                <span class="n">size_format</span><span class="o">=</span><span class="s2">&quot;large&quot;</span><span class="p">,</span>
                <span class="n">span_name</span><span class="o">=</span><span class="s2">&quot;cassandra.query&quot;</span><span class="p">,</span>
                <span class="n">time</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetTraceServiceDefinitionTimeArgs</span><span class="p">(</span>
                    <span class="n">live_span</span><span class="o">=</span><span class="s2">&quot;1h&quot;</span><span class="p">,</span>
                <span class="p">),</span>
                <span class="n">title</span><span class="o">=</span><span class="s2">&quot;alerting-cassandra #env:datad0g.com&quot;</span><span class="p">,</span>
                <span class="n">title_align</span><span class="o">=</span><span class="s2">&quot;center&quot;</span><span class="p">,</span>
                <span class="n">title_size</span><span class="o">=</span><span class="s2">&quot;13&quot;</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">),</span>
    <span class="p">])</span>
</pre></div>
</div>
<p>dashboards can be imported using their ID, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import datadog:index/dashboard:Dashboard my_service_dashboard sv7-gyh-kas
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dashboard_lists</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>int</em><em>]</em><em>]</em><em>]</em>) – The list of dashboard lists this dashboard belongs to.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the dashboard.</p></li>
<li><p><strong>is_read_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this dashboard is read-only.</p></li>
<li><p><strong>layout_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The layout type of the dashboard, either ‘free’ or ‘ordered’.</p></li>
<li><p><strong>notify_lists</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The list of handles of users to notify when changes are made to this dashboard.</p></li>
<li><p><strong>template_variable_presets</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DashboardTemplateVariablePresetArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – The list of selectable template variable presets for this dashboard.</p></li>
<li><p><strong>template_variables</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DashboardTemplateVariableArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – The list of template variables for this dashboard.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The title of the dashboard.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the dashboard.</p></li>
<li><p><strong>widgets</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DashboardWidgetArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – The list of widgets to display on the dashboard.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_datadog.Dashboard.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dashboard_lists</span><span class="p">:</span> <span class="n">Union[Sequence[Union[int, Awaitable[int], Output[T]]], Awaitable[Sequence[Union[int, Awaitable[int], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dashboard_lists_removeds</span><span class="p">:</span> <span class="n">Union[Sequence[Union[int, Awaitable[int], Output[T]]], Awaitable[Sequence[Union[int, Awaitable[int], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_read_only</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">layout_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_lists</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_variable_presets</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DashboardTemplateVariablePresetArgs, Mapping[str, Any], Awaitable[Union[DashboardTemplateVariablePresetArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DashboardTemplateVariablePresetArgs, Mapping[str, Any], Awaitable[Union[DashboardTemplateVariablePresetArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_variables</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DashboardTemplateVariableArgs, Mapping[str, Any], Awaitable[Union[DashboardTemplateVariableArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DashboardTemplateVariableArgs, Mapping[str, Any], Awaitable[Union[DashboardTemplateVariableArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">title</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">widgets</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DashboardWidgetArgs, Mapping[str, Any], Awaitable[Union[DashboardWidgetArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DashboardWidgetArgs, Mapping[str, Any], Awaitable[Union[DashboardWidgetArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.dashboard.Dashboard<a class="headerlink" href="#pulumi_datadog.Dashboard.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Dashboard resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dashboard_lists</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>int</em><em>]</em><em>]</em><em>]</em>) – The list of dashboard lists this dashboard belongs to.</p></li>
<li><p><strong>dashboard_lists_removeds</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>int</em><em>]</em><em>]</em><em>]</em>) – The list of dashboard lists this dashboard should be removed from. Internal only.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the dashboard.</p></li>
<li><p><strong>is_read_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this dashboard is read-only.</p></li>
<li><p><strong>layout_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The layout type of the dashboard, either ‘free’ or ‘ordered’.</p></li>
<li><p><strong>notify_lists</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The list of handles of users to notify when changes are made to this dashboard.</p></li>
<li><p><strong>template_variable_presets</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DashboardTemplateVariablePresetArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – The list of selectable template variable presets for this dashboard.</p></li>
<li><p><strong>template_variables</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DashboardTemplateVariableArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – The list of template variables for this dashboard.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The title of the dashboard.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the dashboard.</p></li>
<li><p><strong>widgets</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DashboardWidgetArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – The list of widgets to display on the dashboard.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Dashboard.dashboard_lists">
<em class="property">property </em><code class="sig-name descname">dashboard_lists</code><a class="headerlink" href="#pulumi_datadog.Dashboard.dashboard_lists" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of dashboard lists this dashboard belongs to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Dashboard.dashboard_lists_removeds">
<em class="property">property </em><code class="sig-name descname">dashboard_lists_removeds</code><a class="headerlink" href="#pulumi_datadog.Dashboard.dashboard_lists_removeds" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of dashboard lists this dashboard should be removed from. Internal only.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Dashboard.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_datadog.Dashboard.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the dashboard.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Dashboard.is_read_only">
<em class="property">property </em><code class="sig-name descname">is_read_only</code><a class="headerlink" href="#pulumi_datadog.Dashboard.is_read_only" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this dashboard is read-only.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Dashboard.layout_type">
<em class="property">property </em><code class="sig-name descname">layout_type</code><a class="headerlink" href="#pulumi_datadog.Dashboard.layout_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The layout type of the dashboard, either ‘free’ or ‘ordered’.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Dashboard.notify_lists">
<em class="property">property </em><code class="sig-name descname">notify_lists</code><a class="headerlink" href="#pulumi_datadog.Dashboard.notify_lists" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of handles of users to notify when changes are made to this dashboard.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Dashboard.template_variable_presets">
<em class="property">property </em><code class="sig-name descname">template_variable_presets</code><a class="headerlink" href="#pulumi_datadog.Dashboard.template_variable_presets" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of selectable template variable presets for this dashboard.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Dashboard.template_variables">
<em class="property">property </em><code class="sig-name descname">template_variables</code><a class="headerlink" href="#pulumi_datadog.Dashboard.template_variables" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of template variables for this dashboard.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Dashboard.title">
<em class="property">property </em><code class="sig-name descname">title</code><a class="headerlink" href="#pulumi_datadog.Dashboard.title" title="Permalink to this definition">¶</a></dt>
<dd><p>The title of the dashboard.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Dashboard.url">
<em class="property">property </em><code class="sig-name descname">url</code><a class="headerlink" href="#pulumi_datadog.Dashboard.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the dashboard.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Dashboard.widgets">
<em class="property">property </em><code class="sig-name descname">widgets</code><a class="headerlink" href="#pulumi_datadog.Dashboard.widgets" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of widgets to display on the dashboard.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Dashboard.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.Dashboard.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.Dashboard.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.Dashboard.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.DashboardList">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">DashboardList</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dash_items</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DashboardListDashItemArgs, Mapping[str, Any], Awaitable[Union[DashboardListDashItemArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DashboardListDashItemArgs, Mapping[str, Any], Awaitable[Union[DashboardListDashItemArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.DashboardList" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Datadog dashboard_list resource. This can be used to create and manage Datadog Dashboard Lists and the individual dashboards within them.</p>
<p>Create a new Dashboard list with two dashboards</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="n">time</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">Dashboard</span><span class="p">(</span><span class="s2">&quot;time&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Created using the Datadog provider in TF&quot;</span><span class="p">,</span>
    <span class="n">is_read_only</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">layout_type</span><span class="o">=</span><span class="s2">&quot;ordered&quot;</span><span class="p">,</span>
    <span class="n">title</span><span class="o">=</span><span class="s2">&quot;TF Test Layout Dashboard&quot;</span><span class="p">,</span>
    <span class="n">widgets</span><span class="o">=</span><span class="p">[</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetArgs</span><span class="p">(</span>
        <span class="n">alert_graph_definition</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetAlertGraphDefinitionArgs</span><span class="p">(</span>
            <span class="n">alert_id</span><span class="o">=</span><span class="s2">&quot;1234&quot;</span><span class="p">,</span>
            <span class="n">time</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetAlertGraphDefinitionTimeArgs</span><span class="p">(</span>
                <span class="n">live_span</span><span class="o">=</span><span class="s2">&quot;1h&quot;</span><span class="p">,</span>
            <span class="p">),</span>
            <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Widget Title&quot;</span><span class="p">,</span>
            <span class="n">viz_type</span><span class="o">=</span><span class="s2">&quot;timeseries&quot;</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">)])</span>
<span class="n">screen</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">Dashboard</span><span class="p">(</span><span class="s2">&quot;screen&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Created using the Datadog provider in TF&quot;</span><span class="p">,</span>
    <span class="n">is_read_only</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">layout_type</span><span class="o">=</span><span class="s2">&quot;free&quot;</span><span class="p">,</span>
    <span class="n">title</span><span class="o">=</span><span class="s2">&quot;TF Test Free Layout Dashboard&quot;</span><span class="p">,</span>
    <span class="n">widgets</span><span class="o">=</span><span class="p">[</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetArgs</span><span class="p">(</span>
        <span class="n">event_stream_definition</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetEventStreamDefinitionArgs</span><span class="p">(</span>
            <span class="n">event_size</span><span class="o">=</span><span class="s2">&quot;l&quot;</span><span class="p">,</span>
            <span class="n">query</span><span class="o">=</span><span class="s2">&quot;*&quot;</span><span class="p">,</span>
            <span class="n">time</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetEventStreamDefinitionTimeArgs</span><span class="p">(</span>
                <span class="n">live_span</span><span class="o">=</span><span class="s2">&quot;1h&quot;</span><span class="p">,</span>
            <span class="p">),</span>
            <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Widget Title&quot;</span><span class="p">,</span>
            <span class="n">title_align</span><span class="o">=</span><span class="s2">&quot;left&quot;</span><span class="p">,</span>
            <span class="n">title_size</span><span class="o">=</span><span class="s2">&quot;16&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">layout</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DashboardWidgetLayoutArgs</span><span class="p">(</span>
            <span class="n">height</span><span class="o">=</span><span class="mi">43</span><span class="p">,</span>
            <span class="n">width</span><span class="o">=</span><span class="mi">32</span><span class="p">,</span>
            <span class="n">x</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
            <span class="n">y</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">)])</span>
<span class="n">new_list</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">DashboardList</span><span class="p">(</span><span class="s2">&quot;newList&quot;</span><span class="p">,</span>
    <span class="n">dash_items</span><span class="o">=</span><span class="p">[</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">DashboardListDashItemArgs</span><span class="p">(</span>
            <span class="n">dash_id</span><span class="o">=</span><span class="n">time</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;custom_timeboard&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">DashboardListDashItemArgs</span><span class="p">(</span>
            <span class="n">dash_id</span><span class="o">=</span><span class="n">screen</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;custom_screenboard&quot;</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">],</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;TF Created List&quot;</span><span class="p">,</span>
    <span class="n">opts</span><span class="o">=</span><span class="n">pulumi</span><span class="o">.</span><span class="n">ResourceOptions</span><span class="p">(</span><span class="n">depends_on</span><span class="o">=</span><span class="p">[</span>
            <span class="s2">&quot;datadog_dashboard.screen&quot;</span><span class="p">,</span>
            <span class="s2">&quot;datadog_dashboard.time&quot;</span><span class="p">,</span>
        <span class="p">]))</span>
</pre></div>
</div>
<p>dashboard lists can be imported using their id, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import datadog:index/dashboardList:DashboardList new_list <span class="m">123456</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dash_items</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DashboardListDashItemArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A set of dashbaord items that belong to this list</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Dashboard List</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_datadog.DashboardList.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dash_items</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DashboardListDashItemArgs, Mapping[str, Any], Awaitable[Union[DashboardListDashItemArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DashboardListDashItemArgs, Mapping[str, Any], Awaitable[Union[DashboardListDashItemArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.dashboard_list.DashboardList<a class="headerlink" href="#pulumi_datadog.DashboardList.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DashboardList resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dash_items</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DashboardListDashItemArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A set of dashbaord items that belong to this list</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Dashboard List</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.DashboardList.dash_items">
<em class="property">property </em><code class="sig-name descname">dash_items</code><a class="headerlink" href="#pulumi_datadog.DashboardList.dash_items" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of dashbaord items that belong to this list</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.DashboardList.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_datadog.DashboardList.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Dashboard List</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.DashboardList.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.DashboardList.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.DashboardList.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.DashboardList.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.Downtime">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">Downtime</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">active</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_date</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitor_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitor_tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recurrence</span><span class="p">:</span> <span class="n">Union[DowntimeRecurrenceArgs, Mapping[str, Any], Awaitable[Union[DowntimeRecurrenceArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scopes</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_date</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timezone</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.Downtime" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Datadog downtime resource. This can be used to create and manage Datadog downtimes.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="c1"># Create a new daily 1700-0900 Datadog downtime for a specific monitor id</span>
<span class="n">foo</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">Downtime</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">end</span><span class="o">=</span><span class="mi">1483365600</span><span class="p">,</span>
    <span class="n">monitor_id</span><span class="o">=</span><span class="mi">12345</span><span class="p">,</span>
    <span class="n">recurrence</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DowntimeRecurrenceArgs</span><span class="p">(</span>
        <span class="n">period</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
        <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;days&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">scopes</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;*&quot;</span><span class="p">],</span>
    <span class="n">start</span><span class="o">=</span><span class="mi">1483308000</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="c1"># Create a new daily 1700-0900 Datadog downtime for all monitors</span>
<span class="n">foo</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">Downtime</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">end</span><span class="o">=</span><span class="mi">1483365600</span><span class="p">,</span>
    <span class="n">recurrence</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">DowntimeRecurrenceArgs</span><span class="p">(</span>
        <span class="n">period</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
        <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;days&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">scopes</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;*&quot;</span><span class="p">],</span>
    <span class="n">start</span><span class="o">=</span><span class="mi">1483308000</span><span class="p">)</span>
</pre></div>
</div>
<p>Downtimes can be imported using their numeric ID, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import datadog:index/downtime:Downtime bytes_received_localhost <span class="m">2081</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>active</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true indicates this downtime is being actively applied</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true indicates this downtime is not being applied</p></li>
<li><p><strong>end</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Optionally specify an end date when this downtime should expire</p></li>
<li><p><strong>end_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String representing date and time to end the downtime in RFC3339 format.</p></li>
<li><p><strong>message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional message to provide when creating the downtime, can include notification handles</p></li>
<li><p><strong>monitor_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – When specified, this downtime will only apply to this monitor</p></li>
<li><p><strong>monitor_tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of monitor tags (up to 25), i.e. tags that are applied directly to monitors to which the downtime applies</p></li>
<li><p><strong>recurrence</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DowntimeRecurrenceArgs'</em><em>]</em><em>]</em>) – Optional recurring schedule for this downtime</p></li>
<li><p><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – specify the group scope to which this downtime applies. For everything use ‘*’</p></li>
<li><p><strong>start</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Specify when this downtime should start</p></li>
<li><p><strong>start_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String representing date and time to start the downtime in RFC3339 format.</p></li>
<li><p><strong>timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The timezone for the downtime, default UTC</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_datadog.Downtime.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">active</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_date</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitor_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitor_tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recurrence</span><span class="p">:</span> <span class="n">Union[DowntimeRecurrenceArgs, Mapping[str, Any], Awaitable[Union[DowntimeRecurrenceArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scopes</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_date</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timezone</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.downtime.Downtime<a class="headerlink" href="#pulumi_datadog.Downtime.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Downtime resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>active</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true indicates this downtime is being actively applied</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – When true indicates this downtime is not being applied</p></li>
<li><p><strong>end</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Optionally specify an end date when this downtime should expire</p></li>
<li><p><strong>end_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String representing date and time to end the downtime in RFC3339 format.</p></li>
<li><p><strong>message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional message to provide when creating the downtime, can include notification handles</p></li>
<li><p><strong>monitor_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – When specified, this downtime will only apply to this monitor</p></li>
<li><p><strong>monitor_tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of monitor tags (up to 25), i.e. tags that are applied directly to monitors to which the downtime applies</p></li>
<li><p><strong>recurrence</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DowntimeRecurrenceArgs'</em><em>]</em><em>]</em>) – Optional recurring schedule for this downtime</p></li>
<li><p><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – specify the group scope to which this downtime applies. For everything use ‘*’</p></li>
<li><p><strong>start</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Specify when this downtime should start</p></li>
<li><p><strong>start_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String representing date and time to start the downtime in RFC3339 format.</p></li>
<li><p><strong>timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The timezone for the downtime, default UTC</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Downtime.active">
<em class="property">property </em><code class="sig-name descname">active</code><a class="headerlink" href="#pulumi_datadog.Downtime.active" title="Permalink to this definition">¶</a></dt>
<dd><p>When true indicates this downtime is being actively applied</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Downtime.disabled">
<em class="property">property </em><code class="sig-name descname">disabled</code><a class="headerlink" href="#pulumi_datadog.Downtime.disabled" title="Permalink to this definition">¶</a></dt>
<dd><p>When true indicates this downtime is not being applied</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Downtime.end">
<em class="property">property </em><code class="sig-name descname">end</code><a class="headerlink" href="#pulumi_datadog.Downtime.end" title="Permalink to this definition">¶</a></dt>
<dd><p>Optionally specify an end date when this downtime should expire</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Downtime.end_date">
<em class="property">property </em><code class="sig-name descname">end_date</code><a class="headerlink" href="#pulumi_datadog.Downtime.end_date" title="Permalink to this definition">¶</a></dt>
<dd><p>String representing date and time to end the downtime in RFC3339 format.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Downtime.message">
<em class="property">property </em><code class="sig-name descname">message</code><a class="headerlink" href="#pulumi_datadog.Downtime.message" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional message to provide when creating the downtime, can include notification handles</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Downtime.monitor_id">
<em class="property">property </em><code class="sig-name descname">monitor_id</code><a class="headerlink" href="#pulumi_datadog.Downtime.monitor_id" title="Permalink to this definition">¶</a></dt>
<dd><p>When specified, this downtime will only apply to this monitor</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Downtime.monitor_tags">
<em class="property">property </em><code class="sig-name descname">monitor_tags</code><a class="headerlink" href="#pulumi_datadog.Downtime.monitor_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of monitor tags (up to 25), i.e. tags that are applied directly to monitors to which the downtime applies</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Downtime.recurrence">
<em class="property">property </em><code class="sig-name descname">recurrence</code><a class="headerlink" href="#pulumi_datadog.Downtime.recurrence" title="Permalink to this definition">¶</a></dt>
<dd><p>Optional recurring schedule for this downtime</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Downtime.scopes">
<em class="property">property </em><code class="sig-name descname">scopes</code><a class="headerlink" href="#pulumi_datadog.Downtime.scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>specify the group scope to which this downtime applies. For everything use ‘*’</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Downtime.start">
<em class="property">property </em><code class="sig-name descname">start</code><a class="headerlink" href="#pulumi_datadog.Downtime.start" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify when this downtime should start</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Downtime.start_date">
<em class="property">property </em><code class="sig-name descname">start_date</code><a class="headerlink" href="#pulumi_datadog.Downtime.start_date" title="Permalink to this definition">¶</a></dt>
<dd><p>String representing date and time to start the downtime in RFC3339 format.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Downtime.timezone">
<em class="property">property </em><code class="sig-name descname">timezone</code><a class="headerlink" href="#pulumi_datadog.Downtime.timezone" title="Permalink to this definition">¶</a></dt>
<dd><p>The timezone for the downtime, default UTC</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Downtime.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.Downtime.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.Downtime.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.Downtime.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.GetDashboardListResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">GetDashboardListResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.GetDashboardListResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDashboardList.</p>
<dl class="py method">
<dt id="pulumi_datadog.GetDashboardListResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_datadog.GetDashboardListResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_datadog.GetDashboardResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">GetDashboardResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">title</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.GetDashboardResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDashboard.</p>
<dl class="py method">
<dt id="pulumi_datadog.GetDashboardResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_datadog.GetDashboardResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_datadog.GetIpRangesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">GetIpRangesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">agents_ipv4s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">agents_ipv6s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_ipv4s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_ipv6s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">apm_ipv4s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">apm_ipv6s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logs_ipv4s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logs_ipv6s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">process_ipv4s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">process_ipv6s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">synthetics_ipv4s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">synthetics_ipv6s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">webhooks_ipv4s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">webhooks_ipv6s</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.GetIpRangesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getIpRanges.</p>
<dl class="py method">
<dt id="pulumi_datadog.GetIpRangesResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_datadog.GetIpRangesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_datadog.GetMonitorResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">GetMonitorResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">enable_logs_sample</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">escalation_message</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">evaluation_delay</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">include_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locked</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitor_tags_filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitor_threshold_windows</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitor_thresholds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">new_host_delay</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">no_data_timeframe</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_audit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_no_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">renotify_interval</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">require_full_window</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags_filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">threshold_windows</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">thresholds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout_h</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.GetMonitorResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getMonitor.</p>
<dl class="py method">
<dt id="pulumi_datadog.GetMonitorResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_datadog.GetMonitorResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_datadog.GetPermissionsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">GetPermissionsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.GetPermissionsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPermissions.</p>
<dl class="py method">
<dt id="pulumi_datadog.GetPermissionsResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_datadog.GetPermissionsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_datadog.GetRoleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">GetRoleResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_count</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.GetRoleResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRole.</p>
<dl class="py method">
<dt id="pulumi_datadog.GetRoleResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_datadog.GetRoleResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_datadog.GetSecurityMonitoringRulesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">GetSecurityMonitoringRulesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">default_only_filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rule_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags_filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_only_filter</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.GetSecurityMonitoringRulesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSecurityMonitoringRules.</p>
<dl class="py method">
<dt id="pulumi_datadog.GetSecurityMonitoringRulesResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_datadog.GetSecurityMonitoringRulesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_datadog.GetSyntheticsLocationsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">GetSyntheticsLocationsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locations</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.GetSyntheticsLocationsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSyntheticsLocations.</p>
<dl class="py method">
<dt id="pulumi_datadog.GetSyntheticsLocationsResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_datadog.GetSyntheticsLocationsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_datadog.LogsArchive">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">LogsArchive</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azure</span><span class="p">:</span> <span class="n">Union[LogsArchiveAzureArgs, Mapping[str, Any], Awaitable[Union[LogsArchiveAzureArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azure_archive</span><span class="p">:</span> <span class="n">Union[LogsArchiveAzureArchiveArgs, Mapping[str, Any], Awaitable[Union[LogsArchiveAzureArchiveArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gcs</span><span class="p">:</span> <span class="n">Union[LogsArchiveGcsArgs, Mapping[str, Any], Awaitable[Union[LogsArchiveGcsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gcs_archive</span><span class="p">:</span> <span class="n">Union[LogsArchiveGcsArchiveArgs, Mapping[str, Any], Awaitable[Union[LogsArchiveGcsArchiveArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">include_tags</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rehydration_tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">s3</span><span class="p">:</span> <span class="n">Union[LogsArchiveS3Args, Mapping[str, Any], Awaitable[Union[LogsArchiveS3Args, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">s3_archive</span><span class="p">:</span> <span class="n">Union[LogsArchiveS3ArchiveArgs, Mapping[str, Any], Awaitable[Union[LogsArchiveS3ArchiveArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.LogsArchive" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Datadog Logs Archive API resource, which is used to create and manage Datadog logs archives.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="n">my_s3_archive</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">LogsArchive</span><span class="p">(</span><span class="s2">&quot;myS3Archive&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;my s3 archive&quot;</span><span class="p">,</span>
    <span class="n">query</span><span class="o">=</span><span class="s2">&quot;service:myservice&quot;</span><span class="p">,</span>
    <span class="n">s3_archive</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">LogsArchiveS3ArchiveArgs</span><span class="p">(</span>
        <span class="n">account_id</span><span class="o">=</span><span class="s2">&quot;001234567888&quot;</span><span class="p">,</span>
        <span class="n">bucket</span><span class="o">=</span><span class="s2">&quot;my-bucket&quot;</span><span class="p">,</span>
        <span class="n">path</span><span class="o">=</span><span class="s2">&quot;/path/foo&quot;</span><span class="p">,</span>
        <span class="n">role_name</span><span class="o">=</span><span class="s2">&quot;my-role-name&quot;</span><span class="p">,</span>
    <span class="p">))</span>
</pre></div>
</div>
<ul class="simple">
<li><p><strong>name</strong> (String, Required) Your archive name.</p></li>
<li><p><strong>query</strong> (String, Required) The archive query/filter. Logs matching this query are included in the archive.</p></li>
</ul>
<ul class="simple">
<li><p><strong>azure</strong> (Map of String, Optional, Deprecated) Definition of an azure archive.</p></li>
<li><p><strong>azure_archive</strong> (Block List, Max: 1) Definition of an azure archive. (see below for nested schema)</p></li>
<li><p><strong>gcs</strong> (Map of String, Optional, Deprecated) Definition of a GCS archive.</p></li>
<li><p><strong>gcs_archive</strong> (Block List, Max: 1) Definition of a GCS archive. (see below for nested schema)</p></li>
<li><p><strong>id</strong> (String, Optional) The ID of this resource.</p></li>
<li><p><strong>include_tags</strong> (Boolean, Optional) To store the tags in the archive, set the value <code class="docutils literal notranslate"><span class="pre">true</span></code>. If it is set to <code class="docutils literal notranslate"><span class="pre">false</span></code>, the tags will be dropped when the logs are sent to the archive.</p></li>
<li><p><strong>rehydration_tags</strong> (List of String, Optional) An array of tags to add to rehydrated logs from an archive.</p></li>
<li><p><strong>s3</strong> (Map of String, Optional, Deprecated) Definition of an s3 archive.</p></li>
<li><p><strong>s3_archive</strong> (Block List, Max: 1) Definition of an s3 archive. (see below for nested schema)</p></li>
</ul>
<p><span class="raw-html-m2r"><a id="nestedblock--azure_archive"></a></span></p>
<p>Required:</p>
<ul class="simple">
<li><p><strong>client_id</strong> (String, Required) Your client id.</p></li>
<li><p><strong>container</strong> (String, Required) The container where the archive will be stored.</p></li>
<li><p><strong>storage_account</strong> (String, Required) The associated storage account.</p></li>
<li><p><strong>tenant_id</strong> (String, Required) Your tenant id.</p></li>
</ul>
<p>Optional:</p>
<ul class="simple">
<li><p><strong>path</strong> (String, Optional) The path where the archive will be stored.</p></li>
</ul>
<p><span class="raw-html-m2r"><a id="nestedblock--gcs_archive"></a></span></p>
<p>Required:</p>
<ul class="simple">
<li><p><strong>bucket</strong> (String, Required) Name of your GCS bucket.</p></li>
<li><p><strong>client_email</strong> (String, Required) Your client email.</p></li>
<li><p><strong>path</strong> (String, Required) Path where the archive will be stored.</p></li>
<li><p><strong>project_id</strong> (String, Required) Your project id.</p></li>
</ul>
<p><span class="raw-html-m2r"><a id="nestedblock--s3_archive"></a></span></p>
<p>Required:</p>
<ul class="simple">
<li><p><strong>account_id</strong> (String, Required) Your AWS account id.</p></li>
<li><p><strong>bucket</strong> (String, Required) Name of your s3 bucket.</p></li>
<li><p><strong>path</strong> (String, Required) Path where the archive will be stored.</p></li>
<li><p><strong>role_name</strong> (String, Required) Your AWS role name</p></li>
</ul>
<p>Import is supported using the following syntax</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import datadog:index/logsArchive:LogsArchive my_s3_archive 1Aabc2_dfQPLnXy3HlfK4hi
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>azure</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LogsArchiveAzureArgs'</em><em>]</em><em>]</em>) – Definition of an azure archive.</p></li>
<li><p><strong>azure_archive</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LogsArchiveAzureArchiveArgs'</em><em>]</em><em>]</em>) – Definition of an azure archive.</p></li>
<li><p><strong>gcs</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LogsArchiveGcsArgs'</em><em>]</em><em>]</em>) – Definition of a GCS archive.</p></li>
<li><p><strong>gcs_archive</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LogsArchiveGcsArchiveArgs'</em><em>]</em><em>]</em>) – Definition of a GCS archive.</p></li>
<li><p><strong>include_tags</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – To store the tags in the archive, set the value <code class="docutils literal notranslate"><span class="pre">true</span></code>. If it is set to <code class="docutils literal notranslate"><span class="pre">false</span></code>, the tags will be dropped when the logs
are sent to the archive.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your archive name.</p></li>
<li><p><strong>query</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The archive query/filter. Logs matching this query are included in the archive.</p></li>
<li><p><strong>rehydration_tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – An array of tags to add to rehydrated logs from an archive.</p></li>
<li><p><strong>s3</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LogsArchiveS3Args'</em><em>]</em><em>]</em>) – Definition of an s3 archive.</p></li>
<li><p><strong>s3_archive</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LogsArchiveS3ArchiveArgs'</em><em>]</em><em>]</em>) – Definition of an s3 archive.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_datadog.LogsArchive.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azure</span><span class="p">:</span> <span class="n">Union[LogsArchiveAzureArgs, Mapping[str, Any], Awaitable[Union[LogsArchiveAzureArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azure_archive</span><span class="p">:</span> <span class="n">Union[LogsArchiveAzureArchiveArgs, Mapping[str, Any], Awaitable[Union[LogsArchiveAzureArchiveArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gcs</span><span class="p">:</span> <span class="n">Union[LogsArchiveGcsArgs, Mapping[str, Any], Awaitable[Union[LogsArchiveGcsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gcs_archive</span><span class="p">:</span> <span class="n">Union[LogsArchiveGcsArchiveArgs, Mapping[str, Any], Awaitable[Union[LogsArchiveGcsArchiveArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">include_tags</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rehydration_tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">s3</span><span class="p">:</span> <span class="n">Union[LogsArchiveS3Args, Mapping[str, Any], Awaitable[Union[LogsArchiveS3Args, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">s3_archive</span><span class="p">:</span> <span class="n">Union[LogsArchiveS3ArchiveArgs, Mapping[str, Any], Awaitable[Union[LogsArchiveS3ArchiveArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.logs_archive.LogsArchive<a class="headerlink" href="#pulumi_datadog.LogsArchive.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LogsArchive resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>azure</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LogsArchiveAzureArgs'</em><em>]</em><em>]</em>) – Definition of an azure archive.</p></li>
<li><p><strong>azure_archive</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LogsArchiveAzureArchiveArgs'</em><em>]</em><em>]</em>) – Definition of an azure archive.</p></li>
<li><p><strong>gcs</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LogsArchiveGcsArgs'</em><em>]</em><em>]</em>) – Definition of a GCS archive.</p></li>
<li><p><strong>gcs_archive</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LogsArchiveGcsArchiveArgs'</em><em>]</em><em>]</em>) – Definition of a GCS archive.</p></li>
<li><p><strong>include_tags</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – To store the tags in the archive, set the value <code class="docutils literal notranslate"><span class="pre">true</span></code>. If it is set to <code class="docutils literal notranslate"><span class="pre">false</span></code>, the tags will be dropped when the logs
are sent to the archive.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your archive name.</p></li>
<li><p><strong>query</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The archive query/filter. Logs matching this query are included in the archive.</p></li>
<li><p><strong>rehydration_tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – An array of tags to add to rehydrated logs from an archive.</p></li>
<li><p><strong>s3</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LogsArchiveS3Args'</em><em>]</em><em>]</em>) – Definition of an s3 archive.</p></li>
<li><p><strong>s3_archive</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LogsArchiveS3ArchiveArgs'</em><em>]</em><em>]</em>) – Definition of an s3 archive.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.LogsArchive.azure">
<em class="property">property </em><code class="sig-name descname">azure</code><a class="headerlink" href="#pulumi_datadog.LogsArchive.azure" title="Permalink to this definition">¶</a></dt>
<dd><p>Definition of an azure archive.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.LogsArchive.azure_archive">
<em class="property">property </em><code class="sig-name descname">azure_archive</code><a class="headerlink" href="#pulumi_datadog.LogsArchive.azure_archive" title="Permalink to this definition">¶</a></dt>
<dd><p>Definition of an azure archive.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.LogsArchive.gcs">
<em class="property">property </em><code class="sig-name descname">gcs</code><a class="headerlink" href="#pulumi_datadog.LogsArchive.gcs" title="Permalink to this definition">¶</a></dt>
<dd><p>Definition of a GCS archive.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.LogsArchive.gcs_archive">
<em class="property">property </em><code class="sig-name descname">gcs_archive</code><a class="headerlink" href="#pulumi_datadog.LogsArchive.gcs_archive" title="Permalink to this definition">¶</a></dt>
<dd><p>Definition of a GCS archive.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.LogsArchive.include_tags">
<em class="property">property </em><code class="sig-name descname">include_tags</code><a class="headerlink" href="#pulumi_datadog.LogsArchive.include_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>To store the tags in the archive, set the value <code class="docutils literal notranslate"><span class="pre">true</span></code>. If it is set to <code class="docutils literal notranslate"><span class="pre">false</span></code>, the tags will be dropped when the logs
are sent to the archive.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.LogsArchive.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_datadog.LogsArchive.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Your archive name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.LogsArchive.query">
<em class="property">property </em><code class="sig-name descname">query</code><a class="headerlink" href="#pulumi_datadog.LogsArchive.query" title="Permalink to this definition">¶</a></dt>
<dd><p>The archive query/filter. Logs matching this query are included in the archive.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.LogsArchive.rehydration_tags">
<em class="property">property </em><code class="sig-name descname">rehydration_tags</code><a class="headerlink" href="#pulumi_datadog.LogsArchive.rehydration_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of tags to add to rehydrated logs from an archive.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.LogsArchive.s3">
<em class="property">property </em><code class="sig-name descname">s3</code><a class="headerlink" href="#pulumi_datadog.LogsArchive.s3" title="Permalink to this definition">¶</a></dt>
<dd><p>Definition of an s3 archive.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.LogsArchive.s3_archive">
<em class="property">property </em><code class="sig-name descname">s3_archive</code><a class="headerlink" href="#pulumi_datadog.LogsArchive.s3_archive" title="Permalink to this definition">¶</a></dt>
<dd><p>Definition of an s3 archive.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.LogsArchive.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.LogsArchive.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.LogsArchive.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.LogsArchive.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.LogsArchiveOrder">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">LogsArchiveOrder</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">archive_ids</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.LogsArchiveOrder" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Datadog <a class="reference external" href="https://docs.datadoghq.com/api/v2/logs-archives/">Logs Archive API</a> resource, which is used to manage Datadog log archives order.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="n">sample_archive_order</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">LogsArchiveOrder</span><span class="p">(</span><span class="s2">&quot;sampleArchiveOrder&quot;</span><span class="p">,</span> <span class="n">archive_ids</span><span class="o">=</span><span class="p">[</span>
    <span class="n">datadog_logs_archive</span><span class="p">[</span><span class="s2">&quot;sample_archive_1&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">datadog_logs_archive</span><span class="p">[</span><span class="s2">&quot;sample_archive_2&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
<span class="p">])</span>
</pre></div>
</div>
<p>There must be at most one <code class="docutils literal notranslate"><span class="pre">datadog_logs_archive_order</span></code> resource. You can import the <code class="docutils literal notranslate"><span class="pre">datadog_logs_archive_order</span></code> or create an archive order.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import datadog:index/logsArchiveOrder:LogsArchiveOrder name&gt; archiveOrderID
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>archive_ids</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The archive IDs list. The order of archive IDs in this attribute defines the overall archive order for logs. If
<code class="docutils literal notranslate"><span class="pre">archive_ids</span></code> is empty or not specified, it will import the actual archive order, and create the resource. Otherwise, it
will try to update the order.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_datadog.LogsArchiveOrder.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">archive_ids</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.logs_archive_order.LogsArchiveOrder<a class="headerlink" href="#pulumi_datadog.LogsArchiveOrder.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LogsArchiveOrder resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>archive_ids</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The archive IDs list. The order of archive IDs in this attribute defines the overall archive order for logs. If
<code class="docutils literal notranslate"><span class="pre">archive_ids</span></code> is empty or not specified, it will import the actual archive order, and create the resource. Otherwise, it
will try to update the order.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.LogsArchiveOrder.archive_ids">
<em class="property">property </em><code class="sig-name descname">archive_ids</code><a class="headerlink" href="#pulumi_datadog.LogsArchiveOrder.archive_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>The archive IDs list. The order of archive IDs in this attribute defines the overall archive order for logs. If
<code class="docutils literal notranslate"><span class="pre">archive_ids</span></code> is empty or not specified, it will import the actual archive order, and create the resource. Otherwise, it
will try to update the order.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.LogsArchiveOrder.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.LogsArchiveOrder.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.LogsArchiveOrder.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.LogsArchiveOrder.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.LogsCustomPipeline">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">LogsCustomPipeline</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="p">:</span> <span class="n">Union[Sequence[Union[LogsCustomPipelineFilterArgs, Mapping[str, Any], Awaitable[Union[LogsCustomPipelineFilterArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[LogsCustomPipelineFilterArgs, Mapping[str, Any], Awaitable[Union[LogsCustomPipelineFilterArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">processors</span><span class="p">:</span> <span class="n">Union[Sequence[Union[LogsCustomPipelineProcessorArgs, Mapping[str, Any], Awaitable[Union[LogsCustomPipelineProcessorArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[LogsCustomPipelineProcessorArgs, Mapping[str, Any], Awaitable[Union[LogsCustomPipelineProcessorArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.LogsCustomPipeline" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Datadog <a class="reference external" href="https://docs.datadoghq.com/api/v1/logs-pipelines/">Logs Pipeline API</a> resource, which is used to create and manage Datadog logs custom pipelines.</p>
<p>Create a Datadog logs pipeline:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="n">sample_pipeline</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">LogsCustomPipeline</span><span class="p">(</span><span class="s2">&quot;samplePipeline&quot;</span><span class="p">,</span>
    <span class="n">filters</span><span class="o">=</span><span class="p">[</span><span class="n">datadog</span><span class="o">.</span><span class="n">LogsCustomPipelineFilterArgs</span><span class="p">(</span>
        <span class="n">query</span><span class="o">=</span><span class="s2">&quot;source:foo&quot;</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="n">is_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;sample pipeline&quot;</span><span class="p">,</span>
    <span class="n">processors</span><span class="o">=</span><span class="p">[</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">LogsCustomPipelineProcessorArgs</span><span class="p">(</span>
            <span class="n">arithmetic_processor</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">LogsCustomPipelineProcessorArithmeticProcessorArgs</span><span class="p">(</span>
                <span class="n">expression</span><span class="o">=</span><span class="s2">&quot;(time1 - time2)*1000&quot;</span><span class="p">,</span>
                <span class="n">is_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">is_replace_missing</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">name</span><span class="o">=</span><span class="s2">&quot;sample arithmetic processor&quot;</span><span class="p">,</span>
                <span class="n">target</span><span class="o">=</span><span class="s2">&quot;my_arithmetic&quot;</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">LogsCustomPipelineProcessorArgs</span><span class="p">(</span>
            <span class="n">attribute_remapper</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">LogsCustomPipelineProcessorAttributeRemapperArgs</span><span class="p">(</span>
                <span class="n">is_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">name</span><span class="o">=</span><span class="s2">&quot;sample attribute processor&quot;</span><span class="p">,</span>
                <span class="n">override_on_conflict</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
                <span class="n">preserve_source</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">source_type</span><span class="o">=</span><span class="s2">&quot;tag&quot;</span><span class="p">,</span>
                <span class="n">sources</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;db.instance&quot;</span><span class="p">],</span>
                <span class="n">target</span><span class="o">=</span><span class="s2">&quot;db&quot;</span><span class="p">,</span>
                <span class="n">target_format</span><span class="o">=</span><span class="s2">&quot;string&quot;</span><span class="p">,</span>
                <span class="n">target_type</span><span class="o">=</span><span class="s2">&quot;attribute&quot;</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">LogsCustomPipelineProcessorArgs</span><span class="p">(</span>
            <span class="n">category_processor</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">LogsCustomPipelineProcessorCategoryProcessorArgs</span><span class="p">(</span>
                <span class="n">category</span><span class="o">=</span><span class="p">[</span>
                    <span class="p">{</span>
                        <span class="s2">&quot;filter&quot;</span><span class="p">:</span> <span class="p">{</span>
                            <span class="s2">&quot;query&quot;</span><span class="p">:</span> <span class="s2">&quot;@severity: &quot;</span><span class="o">.</span><span class="s2">&quot;&quot;</span><span class="p">,</span>
                        <span class="p">},</span>
                        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;debug&quot;</span><span class="p">,</span>
                    <span class="p">},</span>
                    <span class="p">{</span>
                        <span class="s2">&quot;filter&quot;</span><span class="p">:</span> <span class="p">{</span>
                            <span class="s2">&quot;query&quot;</span><span class="p">:</span> <span class="s2">&quot;@severity: &quot;</span><span class="o">-</span><span class="s2">&quot;&quot;</span><span class="p">,</span>
                        <span class="p">},</span>
                        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;verbose&quot;</span><span class="p">,</span>
                    <span class="p">},</span>
                <span class="p">],</span>
                <span class="n">is_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">name</span><span class="o">=</span><span class="s2">&quot;sample category processor&quot;</span><span class="p">,</span>
                <span class="n">target</span><span class="o">=</span><span class="s2">&quot;foo.severity&quot;</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">LogsCustomPipelineProcessorArgs</span><span class="p">(</span>
            <span class="n">date_remapper</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">LogsCustomPipelineProcessorDateRemapperArgs</span><span class="p">(</span>
                <span class="n">is_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">name</span><span class="o">=</span><span class="s2">&quot;sample date remapper&quot;</span><span class="p">,</span>
                <span class="n">sources</span><span class="o">=</span><span class="p">[</span>
                    <span class="s2">&quot;_timestamp&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;published_date&quot;</span><span class="p">,</span>
                <span class="p">],</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">LogsCustomPipelineProcessorArgs</span><span class="p">(</span>
            <span class="n">geo_ip_parser</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">LogsCustomPipelineProcessorGeoIpParserArgs</span><span class="p">(</span>
                <span class="n">is_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">name</span><span class="o">=</span><span class="s2">&quot;sample geo ip parser&quot;</span><span class="p">,</span>
                <span class="n">sources</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;network.client.ip&quot;</span><span class="p">],</span>
                <span class="n">target</span><span class="o">=</span><span class="s2">&quot;network.client.geoip&quot;</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">LogsCustomPipelineProcessorArgs</span><span class="p">(</span>
            <span class="n">grok_parser</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">LogsCustomPipelineProcessorGrokParserArgs</span><span class="p">(</span>
                <span class="n">grok</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">LogsCustomPipelineProcessorGrokParserGrokArgs</span><span class="p">(</span>
                    <span class="n">match_rules</span><span class="o">=</span><span class="s2">&quot;Rule %{word:my_word2} %{number:my_float2}&quot;</span><span class="p">,</span>
                    <span class="n">support_rules</span><span class="o">=</span><span class="s2">&quot;&quot;</span><span class="p">,</span>
                <span class="p">),</span>
                <span class="n">is_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">name</span><span class="o">=</span><span class="s2">&quot;sample grok parser&quot;</span><span class="p">,</span>
                <span class="n">samples</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;sample log 1&quot;</span><span class="p">],</span>
                <span class="n">source</span><span class="o">=</span><span class="s2">&quot;message&quot;</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">LogsCustomPipelineProcessorArgs</span><span class="p">(</span>
            <span class="n">lookup_processor</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">LogsCustomPipelineProcessorLookupProcessorArgs</span><span class="p">(</span>
                <span class="n">default_lookup</span><span class="o">=</span><span class="s2">&quot;unknown service&quot;</span><span class="p">,</span>
                <span class="n">is_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">lookup_table</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;1,my service&quot;</span><span class="p">],</span>
                <span class="n">name</span><span class="o">=</span><span class="s2">&quot;sample lookup processor&quot;</span><span class="p">,</span>
                <span class="n">source</span><span class="o">=</span><span class="s2">&quot;service_id&quot;</span><span class="p">,</span>
                <span class="n">target</span><span class="o">=</span><span class="s2">&quot;service_name&quot;</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">LogsCustomPipelineProcessorArgs</span><span class="p">(</span>
            <span class="n">message_remapper</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">LogsCustomPipelineProcessorMessageRemapperArgs</span><span class="p">(</span>
                <span class="n">is_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">name</span><span class="o">=</span><span class="s2">&quot;sample message remapper&quot;</span><span class="p">,</span>
                <span class="n">sources</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;msg&quot;</span><span class="p">],</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">LogsCustomPipelineProcessorArgs</span><span class="p">(</span>
            <span class="n">pipeline</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">LogsCustomPipelineProcessorPipelineArgs</span><span class="p">(</span>
                <span class="nb">filter</span><span class="o">=</span><span class="p">[{</span>
                    <span class="s2">&quot;query&quot;</span><span class="p">:</span> <span class="s2">&quot;source:foo&quot;</span><span class="p">,</span>
                <span class="p">}],</span>
                <span class="n">is_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">name</span><span class="o">=</span><span class="s2">&quot;nested pipeline&quot;</span><span class="p">,</span>
                <span class="n">processor</span><span class="o">=</span><span class="p">[{</span>
                    <span class="s2">&quot;urlParser&quot;</span><span class="p">:</span> <span class="p">{</span>
                        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;sample url parser&quot;</span><span class="p">,</span>
                        <span class="s2">&quot;normalizeEndingSlashes&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
                        <span class="s2">&quot;sources&quot;</span><span class="p">:</span> <span class="p">[</span>
                            <span class="s2">&quot;url&quot;</span><span class="p">,</span>
                            <span class="s2">&quot;extra&quot;</span><span class="p">,</span>
                        <span class="p">],</span>
                        <span class="s2">&quot;target&quot;</span><span class="p">:</span> <span class="s2">&quot;http_url&quot;</span><span class="p">,</span>
                    <span class="p">},</span>
                <span class="p">}],</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">LogsCustomPipelineProcessorArgs</span><span class="p">(</span>
            <span class="n">service_remapper</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">LogsCustomPipelineProcessorServiceRemapperArgs</span><span class="p">(</span>
                <span class="n">is_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">name</span><span class="o">=</span><span class="s2">&quot;sample service remapper&quot;</span><span class="p">,</span>
                <span class="n">sources</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;service&quot;</span><span class="p">],</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">LogsCustomPipelineProcessorArgs</span><span class="p">(</span>
            <span class="n">status_remapper</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">LogsCustomPipelineProcessorStatusRemapperArgs</span><span class="p">(</span>
                <span class="n">is_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">name</span><span class="o">=</span><span class="s2">&quot;sample status remapper&quot;</span><span class="p">,</span>
                <span class="n">sources</span><span class="o">=</span><span class="p">[</span>
                    <span class="s2">&quot;info&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;trace&quot;</span><span class="p">,</span>
                <span class="p">],</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">LogsCustomPipelineProcessorArgs</span><span class="p">(</span>
            <span class="n">string_builder_processor</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">LogsCustomPipelineProcessorStringBuilderProcessorArgs</span><span class="p">(</span>
                <span class="n">is_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">is_replace_missing</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
                <span class="n">name</span><span class="o">=</span><span class="s2">&quot;sample string builder processor&quot;</span><span class="p">,</span>
                <span class="n">target</span><span class="o">=</span><span class="s2">&quot;user_activity&quot;</span><span class="p">,</span>
                <span class="n">template</span><span class="o">=</span><span class="s2">&quot;%</span><span class="si">{user.name}</span><span class="s2"> logged in at %</span><span class="si">{timestamp}</span><span class="s2">&quot;</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">LogsCustomPipelineProcessorArgs</span><span class="p">(</span>
            <span class="n">trace_id_remapper</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">LogsCustomPipelineProcessorTraceIdRemapperArgs</span><span class="p">(</span>
                <span class="n">is_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">name</span><span class="o">=</span><span class="s2">&quot;sample trace id remapper&quot;</span><span class="p">,</span>
                <span class="n">sources</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;dd.trace_id&quot;</span><span class="p">],</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">LogsCustomPipelineProcessorArgs</span><span class="p">(</span>
            <span class="n">user_agent_parser</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">LogsCustomPipelineProcessorUserAgentParserArgs</span><span class="p">(</span>
                <span class="n">is_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="n">is_encoded</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
                <span class="n">name</span><span class="o">=</span><span class="s2">&quot;sample user agent parser&quot;</span><span class="p">,</span>
                <span class="n">sources</span><span class="o">=</span><span class="p">[</span>
                    <span class="s2">&quot;user&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;agent&quot;</span><span class="p">,</span>
                <span class="p">],</span>
                <span class="n">target</span><span class="o">=</span><span class="s2">&quot;http_agent&quot;</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">),</span>
    <span class="p">])</span>
</pre></div>
</div>
<p>Each <code class="docutils literal notranslate"><span class="pre">LogsCustomPipeline</span></code> resource defines a complete pipeline. The order of the pipelines is maintained in a different resource datadog_logs_pipeline_order. When creating a new pipeline, you need to <strong>explicitly</strong> add this pipeline to the <code class="docutils literal notranslate"><span class="pre">LogsPipelineOrder</span></code> resource to track the pipeline. Similarly, when a pipeline needs to be destroyed, remove its references from the <code class="docutils literal notranslate"><span class="pre">LogsPipelineOrder</span></code> resource.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import datadog:index/logsCustomPipeline:LogsCustomPipeline For the previously created custom pipelines, you can include them in Terraform with the <span class="sb">`</span>import<span class="sb">`</span> operation. Currently, Terraform requires you to explicitly create resources that match the existing pipelines to import them. Use <span class="sb">`</span>&lt;resource.name&gt; &lt;pipelineID&gt;<span class="sb">`</span> <span class="k">for</span> each existing pipeline.
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
<dt id="pulumi_datadog.LogsCustomPipeline.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="p">:</span> <span class="n">Union[Sequence[Union[LogsCustomPipelineFilterArgs, Mapping[str, Any], Awaitable[Union[LogsCustomPipelineFilterArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[LogsCustomPipelineFilterArgs, Mapping[str, Any], Awaitable[Union[LogsCustomPipelineFilterArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">processors</span><span class="p">:</span> <span class="n">Union[Sequence[Union[LogsCustomPipelineProcessorArgs, Mapping[str, Any], Awaitable[Union[LogsCustomPipelineProcessorArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[LogsCustomPipelineProcessorArgs, Mapping[str, Any], Awaitable[Union[LogsCustomPipelineProcessorArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.logs_custom_pipeline.LogsCustomPipeline<a class="headerlink" href="#pulumi_datadog.LogsCustomPipeline.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LogsCustomPipeline resource’s state with the given name, id, and optional extra
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
<dt id="pulumi_datadog.LogsCustomPipeline.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.LogsCustomPipeline.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.LogsCustomPipeline.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.LogsCustomPipeline.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.LogsIndex">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">LogsIndex</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">exclusion_filters</span><span class="p">:</span> <span class="n">Union[Sequence[Union[LogsIndexExclusionFilterArgs, Mapping[str, Any], Awaitable[Union[LogsIndexExclusionFilterArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[LogsIndexExclusionFilterArgs, Mapping[str, Any], Awaitable[Union[LogsIndexExclusionFilterArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="p">:</span> <span class="n">Union[Sequence[Union[LogsIndexFilterArgs, Mapping[str, Any], Awaitable[Union[LogsIndexFilterArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[LogsIndexFilterArgs, Mapping[str, Any], Awaitable[Union[LogsIndexFilterArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.LogsIndex" title="Permalink to this definition">¶</a></dt>
<dd><div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import datadog:index/logsIndex:LogsIndex The current Datadog Terraform provider version does not support the creation and deletion of indexes. To manage the existing indexes, <span class="k">do</span> <span class="sb">`</span>&lt;datadog_logs_index.name&gt; &lt;indexName&gt;<span class="sb">`</span> to import them to Terraform. If you create a resource which does not match the name of any existing index, <span class="sb">`</span>terraform apply<span class="sb">`</span> will throw <span class="sb">`</span>Not Found<span class="sb">`</span> error code.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>exclusion_filters</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LogsIndexExclusionFilterArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – List of exclusion filters.</p></li>
<li><p><strong>filters</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LogsIndexFilterArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Logs filter</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the index.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_datadog.LogsIndex.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">exclusion_filters</span><span class="p">:</span> <span class="n">Union[Sequence[Union[LogsIndexExclusionFilterArgs, Mapping[str, Any], Awaitable[Union[LogsIndexExclusionFilterArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[LogsIndexExclusionFilterArgs, Mapping[str, Any], Awaitable[Union[LogsIndexExclusionFilterArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="p">:</span> <span class="n">Union[Sequence[Union[LogsIndexFilterArgs, Mapping[str, Any], Awaitable[Union[LogsIndexFilterArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[LogsIndexFilterArgs, Mapping[str, Any], Awaitable[Union[LogsIndexFilterArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.logs_index.LogsIndex<a class="headerlink" href="#pulumi_datadog.LogsIndex.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LogsIndex resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>exclusion_filters</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LogsIndexExclusionFilterArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – List of exclusion filters.</p></li>
<li><p><strong>filters</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LogsIndexFilterArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Logs filter</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the index.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.LogsIndex.exclusion_filters">
<em class="property">property </em><code class="sig-name descname">exclusion_filters</code><a class="headerlink" href="#pulumi_datadog.LogsIndex.exclusion_filters" title="Permalink to this definition">¶</a></dt>
<dd><p>List of exclusion filters.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.LogsIndex.filters">
<em class="property">property </em><code class="sig-name descname">filters</code><a class="headerlink" href="#pulumi_datadog.LogsIndex.filters" title="Permalink to this definition">¶</a></dt>
<dd><p>Logs filter</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.LogsIndex.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_datadog.LogsIndex.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the index.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.LogsIndex.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.LogsIndex.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.LogsIndex.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.LogsIndex.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.LogsIndexOrder">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">LogsIndexOrder</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">indexes</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.LogsIndexOrder" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Datadog <a class="reference external" href="https://docs.datadoghq.com/api/v1/logs-indexes/">Logs Index API</a> resource. This can be used to manage the order of Datadog logs indexes.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="n">sample_index_order</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">LogsIndexOrder</span><span class="p">(</span><span class="s2">&quot;sampleIndexOrder&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;sample_index_order&quot;</span><span class="p">,</span>
    <span class="n">indexes</span><span class="o">=</span><span class="p">[</span><span class="n">datadog_logs_index</span><span class="p">[</span><span class="s2">&quot;sample_index&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">]],</span>
    <span class="n">opts</span><span class="o">=</span><span class="n">pulumi</span><span class="o">.</span><span class="n">ResourceOptions</span><span class="p">(</span><span class="n">depends_on</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;datadog_logs_index.sample_index&quot;</span><span class="p">]))</span>
</pre></div>
</div>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import datadog:index/logsIndexOrder:LogsIndexOrder The current Datadog Terraform provider version does not support the creation and deletion of index orders. Do <span class="sb">`</span>&lt;datadog_logs_index_order.name&gt; &lt;name&gt;<span class="sb">`</span> to import index order to Terraform. There must be at most one <span class="sb">`</span>datadog_logs_index_order<span class="sb">`</span> resource.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>indexes</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The index resource list. Logs are tested against the query filter of each index one by one following the order of the
list.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique name of the index order resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_datadog.LogsIndexOrder.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">indexes</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.logs_index_order.LogsIndexOrder<a class="headerlink" href="#pulumi_datadog.LogsIndexOrder.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LogsIndexOrder resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>indexes</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The index resource list. Logs are tested against the query filter of each index one by one following the order of the
list.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique name of the index order resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.LogsIndexOrder.indexes">
<em class="property">property </em><code class="sig-name descname">indexes</code><a class="headerlink" href="#pulumi_datadog.LogsIndexOrder.indexes" title="Permalink to this definition">¶</a></dt>
<dd><p>The index resource list. Logs are tested against the query filter of each index one by one following the order of the
list.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.LogsIndexOrder.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_datadog.LogsIndexOrder.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique name of the index order resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.LogsIndexOrder.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.LogsIndexOrder.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.LogsIndexOrder.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.LogsIndexOrder.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.LogsIntegrationPipeline">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">LogsIntegrationPipeline</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.LogsIntegrationPipeline" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Datadog <a class="reference external" href="https://docs.datadoghq.com/api/v1/logs-pipelines/">Logs Pipeline API</a> resource to manage the <a class="reference external" href="https://docs.datadoghq.com/logs/log_collection/?tab=tcpussite">integrations</a>.</p>
<p>Integration pipelines are the pipelines that are automatically installed for your organization when sending the logs with specific sources. You don’t need to maintain or update these types of pipelines. Keeping them as resources, however, allows you to manage the order of your pipelines by referencing them in your LogsPipelineOrder resource. If you don’t need the <code class="docutils literal notranslate"><span class="pre">pipeline_order</span></code> feature, this resource declaration can be omitted.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="n">python</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">LogsIntegrationPipeline</span><span class="p">(</span><span class="s2">&quot;python&quot;</span><span class="p">,</span> <span class="n">is_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import datadog:index/logsIntegrationPipeline:LogsIntegrationPipeline name&gt; &lt;pipelineID&gt;<span class="sb">`</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>is_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean value to enable your pipeline.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_datadog.LogsIntegrationPipeline.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.logs_integration_pipeline.LogsIntegrationPipeline<a class="headerlink" href="#pulumi_datadog.LogsIntegrationPipeline.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LogsIntegrationPipeline resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>is_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean value to enable your pipeline.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.LogsIntegrationPipeline.is_enabled">
<em class="property">property </em><code class="sig-name descname">is_enabled</code><a class="headerlink" href="#pulumi_datadog.LogsIntegrationPipeline.is_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean value to enable your pipeline.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.LogsIntegrationPipeline.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.LogsIntegrationPipeline.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.LogsIntegrationPipeline.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.LogsIntegrationPipeline.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.LogsMetric">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">LogsMetric</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">compute</span><span class="p">:</span> <span class="n">Union[LogsMetricComputeArgs, Mapping[str, Any], Awaitable[Union[LogsMetricComputeArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter</span><span class="p">:</span> <span class="n">Union[LogsMetricFilterArgs, Mapping[str, Any], Awaitable[Union[LogsMetricFilterArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_bies</span><span class="p">:</span> <span class="n">Union[Sequence[Union[LogsMetricGroupByArgs, Mapping[str, Any], Awaitable[Union[LogsMetricGroupByArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[LogsMetricGroupByArgs, Mapping[str, Any], Awaitable[Union[LogsMetricGroupByArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.LogsMetric" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource for interacting with the logs_metric API</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="n">testing_logs_metric</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">LogsMetric</span><span class="p">(</span><span class="s2">&quot;testingLogsMetric&quot;</span><span class="p">,</span>
    <span class="n">compute</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">LogsMetricComputeArgs</span><span class="p">(</span>
        <span class="n">aggregation_type</span><span class="o">=</span><span class="s2">&quot;distribution&quot;</span><span class="p">,</span>
        <span class="n">path</span><span class="o">=</span><span class="s2">&quot;@duration&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="nb">filter</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">LogsMetricFilterArgs</span><span class="p">(</span>
        <span class="n">query</span><span class="o">=</span><span class="s2">&quot;service:test&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">group_bies</span><span class="o">=</span><span class="p">[</span><span class="n">datadog</span><span class="o">.</span><span class="n">LogsMetricGroupByArgs</span><span class="p">(</span>
        <span class="n">path</span><span class="o">=</span><span class="s2">&quot;@status&quot;</span><span class="p">,</span>
        <span class="n">tag_name</span><span class="o">=</span><span class="s2">&quot;status&quot;</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;testing.logs.metric&quot;</span><span class="p">)</span>
</pre></div>
</div>
<ul class="simple">
<li><p><strong>compute</strong> (Block List, Min: 1, Max: 1) The compute rule to compute the log-based metric. This field can’t be updated after creation. (see below for nested schema)</p></li>
<li><p><strong>filter</strong> (Block List, Min: 1, Max: 1) The log-based metric filter. Logs matching this filter will be aggregated in this metric. (see below for nested schema)</p></li>
<li><p><strong>name</strong> (String, Required) The name of the log-based metric. This field can’t be updated after creation.</p></li>
</ul>
<ul class="simple">
<li><p><strong>group_by</strong> (Block List) The rules for the group by. (see below for nested schema)</p></li>
<li><p><strong>id</strong> (String, Optional) The ID of this resource.</p></li>
</ul>
<p><span class="raw-html-m2r"><a id="nestedblock--compute"></a></span></p>
<p>Required:</p>
<ul class="simple">
<li><p><strong>aggregation_type</strong> (String, Required) The type of aggregation to use. This field can’t be updated after creation.</p></li>
</ul>
<p>Optional:</p>
<ul class="simple">
<li><p><strong>path</strong> (String, Optional) The path to the value the log-based metric will aggregate on (only used if the aggregation type is a “distribution”). This field can’t be updated after creation.</p></li>
</ul>
<p><span class="raw-html-m2r"><a id="nestedblock--filter"></a></span></p>
<p>Required:</p>
<ul class="simple">
<li><p><strong>query</strong> (String, Required) The search query - following the log search syntax.</p></li>
</ul>
<p><span class="raw-html-m2r"><a id="nestedblock--group_by"></a></span></p>
<p>Required:</p>
<ul class="simple">
<li><p><strong>path</strong> (String, Required) The path to the value the log-based metric will be aggregated over.</p></li>
<li><p><strong>tag_name</strong> (String, Required) Name of the tag that gets created.</p></li>
</ul>
<p>Import is supported using the following syntax</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import datadog:index/logsMetric:LogsMetric testing_logs_metric testing.logs.metric
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>compute</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LogsMetricComputeArgs'</em><em>]</em><em>]</em>) – The compute rule to compute the log-based metric. This field can’t be updated after creation.</p></li>
<li><p><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LogsMetricFilterArgs'</em><em>]</em><em>]</em>) – The log-based metric filter. Logs matching this filter will be aggregated in this metric.</p></li>
<li><p><strong>group_bies</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LogsMetricGroupByArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – The rules for the group by.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the log-based metric. This field can’t be updated after creation.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_datadog.LogsMetric.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">compute</span><span class="p">:</span> <span class="n">Union[LogsMetricComputeArgs, Mapping[str, Any], Awaitable[Union[LogsMetricComputeArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filter</span><span class="p">:</span> <span class="n">Union[LogsMetricFilterArgs, Mapping[str, Any], Awaitable[Union[LogsMetricFilterArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_bies</span><span class="p">:</span> <span class="n">Union[Sequence[Union[LogsMetricGroupByArgs, Mapping[str, Any], Awaitable[Union[LogsMetricGroupByArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[LogsMetricGroupByArgs, Mapping[str, Any], Awaitable[Union[LogsMetricGroupByArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.logs_metric.LogsMetric<a class="headerlink" href="#pulumi_datadog.LogsMetric.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LogsMetric resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>compute</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LogsMetricComputeArgs'</em><em>]</em><em>]</em>) – The compute rule to compute the log-based metric. This field can’t be updated after creation.</p></li>
<li><p><strong>filter</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LogsMetricFilterArgs'</em><em>]</em><em>]</em>) – The log-based metric filter. Logs matching this filter will be aggregated in this metric.</p></li>
<li><p><strong>group_bies</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LogsMetricGroupByArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – The rules for the group by.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the log-based metric. This field can’t be updated after creation.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.LogsMetric.compute">
<em class="property">property </em><code class="sig-name descname">compute</code><a class="headerlink" href="#pulumi_datadog.LogsMetric.compute" title="Permalink to this definition">¶</a></dt>
<dd><p>The compute rule to compute the log-based metric. This field can’t be updated after creation.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.LogsMetric.filter">
<em class="property">property </em><code class="sig-name descname">filter</code><a class="headerlink" href="#pulumi_datadog.LogsMetric.filter" title="Permalink to this definition">¶</a></dt>
<dd><p>The log-based metric filter. Logs matching this filter will be aggregated in this metric.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.LogsMetric.group_bies">
<em class="property">property </em><code class="sig-name descname">group_bies</code><a class="headerlink" href="#pulumi_datadog.LogsMetric.group_bies" title="Permalink to this definition">¶</a></dt>
<dd><p>The rules for the group by.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.LogsMetric.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_datadog.LogsMetric.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the log-based metric. This field can’t be updated after creation.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.LogsMetric.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.LogsMetric.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.LogsMetric.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.LogsMetric.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.LogsPipelineOrder">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">LogsPipelineOrder</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pipelines</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.LogsPipelineOrder" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Datadog <a class="reference external" href="https://docs.datadoghq.com/api/v1/logs-pipelines/">Logs Pipeline API</a> resource, which is used to manage Datadog log pipelines order.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="n">sample_pipeline_order</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">LogsPipelineOrder</span><span class="p">(</span><span class="s2">&quot;samplePipelineOrder&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;sample_pipeline_order&quot;</span><span class="p">,</span>
    <span class="n">pipelines</span><span class="o">=</span><span class="p">[</span>
        <span class="n">datadog_logs_custom_pipeline</span><span class="p">[</span><span class="s2">&quot;sample_pipeline&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
        <span class="n">datadog_logs_integration_pipeline</span><span class="p">[</span><span class="s2">&quot;python&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="p">],</span>
    <span class="n">opts</span><span class="o">=</span><span class="n">pulumi</span><span class="o">.</span><span class="n">ResourceOptions</span><span class="p">(</span><span class="n">depends_on</span><span class="o">=</span><span class="p">[</span>
            <span class="s2">&quot;datadog_logs_custom_pipeline.sample_pipeline&quot;</span><span class="p">,</span>
            <span class="s2">&quot;datadog_logs_integration_pipeline.python&quot;</span><span class="p">,</span>
        <span class="p">]))</span>
</pre></div>
</div>
<p>There must be at most one <code class="docutils literal notranslate"><span class="pre">datadog_logs_pipeline_order</span></code> resource. Pipeline order creation is not supported from logs config API. You can import the <code class="docutils literal notranslate"><span class="pre">datadog_logs_pipeline_order</span></code> or create a pipeline order (which is actually doing the update operation).</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import datadog:index/logsPipelineOrder:LogsPipelineOrder name&gt; &lt;name&gt;
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name attribute in the resource <code class="docutils literal notranslate"><span class="pre">datadog_logs_pipeline_order</span></code> needs to be unique. It’s recommended to use the same
value as the resource name. No related field is available in <a class="reference external" href="https://docs.datadoghq.com/api/v1/logs-pipelines/#get-pipeline-order">Logs Pipeline
API</a>.</p>
</p></li>
<li><p><strong>pipelines</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The pipeline IDs list. The order of pipeline IDs in this attribute defines the overall pipeline order for logs.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_datadog.LogsPipelineOrder.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pipelines</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.logs_pipeline_order.LogsPipelineOrder<a class="headerlink" href="#pulumi_datadog.LogsPipelineOrder.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LogsPipelineOrder resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name attribute in the resource <code class="docutils literal notranslate"><span class="pre">datadog_logs_pipeline_order</span></code> needs to be unique. It’s recommended to use the same
value as the resource name. No related field is available in <a class="reference external" href="https://docs.datadoghq.com/api/v1/logs-pipelines/#get-pipeline-order">Logs Pipeline
API</a>.</p>
</p></li>
<li><p><strong>pipelines</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The pipeline IDs list. The order of pipeline IDs in this attribute defines the overall pipeline order for logs.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.LogsPipelineOrder.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_datadog.LogsPipelineOrder.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name attribute in the resource <code class="docutils literal notranslate"><span class="pre">datadog_logs_pipeline_order</span></code> needs to be unique. It’s recommended to use the same
value as the resource name. No related field is available in <a class="reference external" href="https://docs.datadoghq.com/api/v1/logs-pipelines/#get-pipeline-order">Logs Pipeline
API</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.LogsPipelineOrder.pipelines">
<em class="property">property </em><code class="sig-name descname">pipelines</code><a class="headerlink" href="#pulumi_datadog.LogsPipelineOrder.pipelines" title="Permalink to this definition">¶</a></dt>
<dd><p>The pipeline IDs list. The order of pipeline IDs in this attribute defines the overall pipeline order for logs.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.LogsPipelineOrder.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.LogsPipelineOrder.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.LogsPipelineOrder.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.LogsPipelineOrder.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.MetricMetadata">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">MetricMetadata</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">per_unit</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">short_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">statsd_interval</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">unit</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.MetricMetadata" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Datadog metric_metadata resource. This can be used to manage a metric’s metadata.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="c1"># Manage a Datadog metric&#39;s metadata</span>
<span class="n">request_time</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">MetricMetadata</span><span class="p">(</span><span class="s2">&quot;requestTime&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;99th percentile request time in millseconds&quot;</span><span class="p">,</span>
    <span class="n">metric</span><span class="o">=</span><span class="s2">&quot;request.time&quot;</span><span class="p">,</span>
    <span class="n">short_name</span><span class="o">=</span><span class="s2">&quot;Request time&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;gauge&quot;</span><span class="p">,</span>
    <span class="n">unit</span><span class="o">=</span><span class="s2">&quot;millisecond&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the metric.</p></li>
<li><p><strong>metric</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the metric.</p></li>
<li><p><strong>per_unit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Per unit of the metric such as <code class="docutils literal notranslate"><span class="pre">second</span></code> in <code class="docutils literal notranslate"><span class="pre">bytes</span> <span class="pre">per</span> <span class="pre">second</span></code>.</p></li>
<li><p><strong>short_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A short name of the metric.</p></li>
<li><p><strong>statsd_interval</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – If applicable, statsd flush interval in seconds for the metric.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the metric.</p></li>
<li><p><strong>unit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Primary unit of the metric such as <code class="docutils literal notranslate"><span class="pre">byte</span></code> or <code class="docutils literal notranslate"><span class="pre">operation</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_datadog.MetricMetadata.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">per_unit</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">short_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">statsd_interval</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">unit</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.metric_metadata.MetricMetadata<a class="headerlink" href="#pulumi_datadog.MetricMetadata.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MetricMetadata resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the metric.</p></li>
<li><p><strong>metric</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the metric.</p></li>
<li><p><strong>per_unit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Per unit of the metric such as <code class="docutils literal notranslate"><span class="pre">second</span></code> in <code class="docutils literal notranslate"><span class="pre">bytes</span> <span class="pre">per</span> <span class="pre">second</span></code>.</p></li>
<li><p><strong>short_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A short name of the metric.</p></li>
<li><p><strong>statsd_interval</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – If applicable, statsd flush interval in seconds for the metric.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of the metric.</p></li>
<li><p><strong>unit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Primary unit of the metric such as <code class="docutils literal notranslate"><span class="pre">byte</span></code> or <code class="docutils literal notranslate"><span class="pre">operation</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.MetricMetadata.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_datadog.MetricMetadata.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the metric.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.MetricMetadata.metric">
<em class="property">property </em><code class="sig-name descname">metric</code><a class="headerlink" href="#pulumi_datadog.MetricMetadata.metric" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the metric.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.MetricMetadata.per_unit">
<em class="property">property </em><code class="sig-name descname">per_unit</code><a class="headerlink" href="#pulumi_datadog.MetricMetadata.per_unit" title="Permalink to this definition">¶</a></dt>
<dd><p>Per unit of the metric such as <code class="docutils literal notranslate"><span class="pre">second</span></code> in <code class="docutils literal notranslate"><span class="pre">bytes</span> <span class="pre">per</span> <span class="pre">second</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.MetricMetadata.short_name">
<em class="property">property </em><code class="sig-name descname">short_name</code><a class="headerlink" href="#pulumi_datadog.MetricMetadata.short_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A short name of the metric.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.MetricMetadata.statsd_interval">
<em class="property">property </em><code class="sig-name descname">statsd_interval</code><a class="headerlink" href="#pulumi_datadog.MetricMetadata.statsd_interval" title="Permalink to this definition">¶</a></dt>
<dd><p>If applicable, statsd flush interval in seconds for the metric.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.MetricMetadata.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_datadog.MetricMetadata.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of the metric.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.MetricMetadata.unit">
<em class="property">property </em><code class="sig-name descname">unit</code><a class="headerlink" href="#pulumi_datadog.MetricMetadata.unit" title="Permalink to this definition">¶</a></dt>
<dd><p>Primary unit of the metric such as <code class="docutils literal notranslate"><span class="pre">byte</span></code> or <code class="docutils literal notranslate"><span class="pre">operation</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.MetricMetadata.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.MetricMetadata.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.MetricMetadata.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.MetricMetadata.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.Monitor">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">Monitor</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_logs_sample</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">escalation_message</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">evaluation_delay</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_delete</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">include_tags</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locked</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitor_threshold_windows</span><span class="p">:</span> <span class="n">Union[MonitorMonitorThresholdWindowsArgs, Mapping[str, Any], Awaitable[Union[MonitorMonitorThresholdWindowsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitor_thresholds</span><span class="p">:</span> <span class="n">Union[MonitorMonitorThresholdsArgs, Mapping[str, Any], Awaitable[Union[MonitorMonitorThresholdsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">new_host_delay</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">no_data_timeframe</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_audit</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_no_data</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">renotify_interval</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">require_full_window</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">silenced</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">threshold_windows</span><span class="p">:</span> <span class="n">Union[MonitorThresholdWindowsArgs, Mapping[str, Any], Awaitable[Union[MonitorThresholdWindowsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">thresholds</span><span class="p">:</span> <span class="n">Union[MonitorThresholdsArgs, Mapping[str, Any], Awaitable[Union[MonitorThresholdsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout_h</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">validate</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.Monitor" title="Permalink to this definition">¶</a></dt>
<dd><p>Import is supported using the following syntax</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import datadog:index/monitor:Monitor bytes_received_localhost <span class="m">2081</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enable_logs_sample</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether or not to include a list of log values which triggered the alert. This is only used by log
monitors. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>escalation_message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A message to include with a re-notification. Supports the <code class="docutils literal notranslate"><span class="pre">&#64;username</span></code> notification allowed elsewhere.</p></li>
<li><p><strong>evaluation_delay</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – (Only applies to metric alert) Time (in seconds) to delay evaluation, as a non-negative integer. For example, if the
value is set to <code class="docutils literal notranslate"><span class="pre">300</span></code> (5min), the <code class="docutils literal notranslate"><span class="pre">timeframe</span></code> is set to <code class="docutils literal notranslate"><span class="pre">last_5m</span></code> and the time is 7:00, the monitor will evaluate data
from 6:50 to 6:55. This is useful for AWS CloudWatch and other backfilled metrics to ensure the monitor will always have
data during evaluation.</p></li>
<li><p><strong>force_delete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether this monitor can be deleted even if it’s referenced by other resources (e.g. SLO,
composite monitor).</p></li>
<li><p><strong>include_tags</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether notifications from this monitor automatically insert its triggering tags into the title.
Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>locked</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether changes to to this monitor should be restricted to the creator or admins. Defaults to
<code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A message to include with notifications for this monitor. Email notifications can be sent to specific users by using the
same <code class="docutils literal notranslate"><span class="pre">&#64;username</span></code> notation as events.</p></li>
<li><p><strong>monitor_threshold_windows</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'MonitorMonitorThresholdWindowsArgs'</em><em>]</em><em>]</em>) – A mapping containing <code class="docutils literal notranslate"><span class="pre">recovery_window</span></code> and <code class="docutils literal notranslate"><span class="pre">trigger_window</span></code> values, e.g. <code class="docutils literal notranslate"><span class="pre">last_15m</span></code> . Can only be used for, and are
required for, anomaly monitors.</p></li>
<li><p><strong>monitor_thresholds</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'MonitorMonitorThresholdsArgs'</em><em>]</em><em>]</em>) – Alert thresholds of the monitor.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Datadog monitor.</p></li>
<li><p><strong>new_host_delay</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Time (in seconds) to allow a host to boot and applications to fully start before starting the evaluation of monitor
results. Should be a non negative integer. Defaults to <code class="docutils literal notranslate"><span class="pre">300</span></code>.</p></li>
<li><p><strong>no_data_timeframe</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of minutes before a monitor will notify when data stops reporting. Provider defaults to 10 minutes. We
recommend at least 2x the monitor timeframe for metric alerts or 2 minutes for service checks.</p></li>
<li><p><strong>notify_audit</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether tagged users will be notified on changes to this monitor. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>notify_no_data</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether this monitor will notify when data stops reporting. Defaults to false.</p></li>
<li><p><strong>query</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The monitor query to notify on. Note this is not the same query you see in the UI and the syntax is different depending
on the monitor type, please see the <a class="reference external" href="https://docs.datadoghq.com/api/v1/monitors/#create-a-monitor">API Reference</a> for
details. Warning: <code class="docutils literal notranslate"><span class="pre">terraform</span> <span class="pre">plan</span></code> won’t perform any validation of the query contents.</p></li>
<li><p><strong>renotify_interval</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of minutes after the last notification before a monitor will re-notify on the current status. It will only
re-notify if it’s not resolved.</p></li>
<li><p><strong>require_full_window</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether this monitor needs a full window of data before it’s evaluated. We highly recommend you set
this to <code class="docutils literal notranslate"><span class="pre">false</span></code> for s metrics, otherwise some evaluations will be skipped. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code> for <code class="docutils literal notranslate"><span class="pre">on</span> <span class="pre">average</span></code>, <code class="docutils literal notranslate"><span class="pre">at</span> <span class="pre">all</span>
<span class="pre">times</span></code> and <code class="docutils literal notranslate"><span class="pre">in</span> <span class="pre">total</span></code> aggregation. <code class="docutils literal notranslate"><span class="pre">false</span></code> otherwise.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>silenced</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Each scope will be muted until the given POSIX timestamp or forever if the value is <code class="docutils literal notranslate"><span class="pre">0</span></code>. Use <code class="docutils literal notranslate"><span class="pre">-1</span></code> if you want to unmute
the scope. Deprecated: the silenced parameter is being deprecated in favor of the downtime resource. This will be
removed in the next major version of the Terraform Provider.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of tags to associate with your monitor. This can help you categorize and filter monitors in the manage monitors
page of the UI. Note: it’s not currently possible to filter by these tags when querying via the API</p></li>
<li><p><strong>threshold_windows</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'MonitorThresholdWindowsArgs'</em><em>]</em><em>]</em>) – A mapping containing <code class="docutils literal notranslate"><span class="pre">recovery_window</span></code> and <code class="docutils literal notranslate"><span class="pre">trigger_window</span></code> values, e.g. <code class="docutils literal notranslate"><span class="pre">last_15m</span></code>. Can only be used for, and are
required for, anomaly monitors.</p></li>
<li><p><strong>thresholds</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'MonitorThresholdsArgs'</em><em>]</em><em>]</em>) – Alert thresholds of the monitor.</p></li>
<li><p><strong>timeout_h</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of hours of the monitor not reporting data before it will automatically resolve from a triggered state.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the monitor. The mapping from these types to the types found in the Datadog Web UI can be found in the
Datadog API <a class="reference external" href="https://docs.datadoghq.com/api/v1/monitors/#create-a-monitor">documentation page</a>. Note: The monitor type
cannot be changed after a monitor is created.</p></li>
<li><p><strong>validate</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">false</span></code>, skip the validation call done during plan.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_datadog.Monitor.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_logs_sample</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">escalation_message</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">evaluation_delay</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_delete</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">include_tags</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locked</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitor_threshold_windows</span><span class="p">:</span> <span class="n">Union[MonitorMonitorThresholdWindowsArgs, Mapping[str, Any], Awaitable[Union[MonitorMonitorThresholdWindowsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitor_thresholds</span><span class="p">:</span> <span class="n">Union[MonitorMonitorThresholdsArgs, Mapping[str, Any], Awaitable[Union[MonitorMonitorThresholdsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">new_host_delay</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">no_data_timeframe</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_audit</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_no_data</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">renotify_interval</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">require_full_window</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">silenced</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">threshold_windows</span><span class="p">:</span> <span class="n">Union[MonitorThresholdWindowsArgs, Mapping[str, Any], Awaitable[Union[MonitorThresholdWindowsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">thresholds</span><span class="p">:</span> <span class="n">Union[MonitorThresholdsArgs, Mapping[str, Any], Awaitable[Union[MonitorThresholdsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout_h</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">validate</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.monitor.Monitor<a class="headerlink" href="#pulumi_datadog.Monitor.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Monitor resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enable_logs_sample</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether or not to include a list of log values which triggered the alert. This is only used by log
monitors. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>escalation_message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A message to include with a re-notification. Supports the <code class="docutils literal notranslate"><span class="pre">&#64;username</span></code> notification allowed elsewhere.</p></li>
<li><p><strong>evaluation_delay</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – (Only applies to metric alert) Time (in seconds) to delay evaluation, as a non-negative integer. For example, if the
value is set to <code class="docutils literal notranslate"><span class="pre">300</span></code> (5min), the <code class="docutils literal notranslate"><span class="pre">timeframe</span></code> is set to <code class="docutils literal notranslate"><span class="pre">last_5m</span></code> and the time is 7:00, the monitor will evaluate data
from 6:50 to 6:55. This is useful for AWS CloudWatch and other backfilled metrics to ensure the monitor will always have
data during evaluation.</p></li>
<li><p><strong>force_delete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether this monitor can be deleted even if it’s referenced by other resources (e.g. SLO,
composite monitor).</p></li>
<li><p><strong>include_tags</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether notifications from this monitor automatically insert its triggering tags into the title.
Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>locked</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether changes to to this monitor should be restricted to the creator or admins. Defaults to
<code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A message to include with notifications for this monitor. Email notifications can be sent to specific users by using the
same <code class="docutils literal notranslate"><span class="pre">&#64;username</span></code> notation as events.</p></li>
<li><p><strong>monitor_threshold_windows</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'MonitorMonitorThresholdWindowsArgs'</em><em>]</em><em>]</em>) – A mapping containing <code class="docutils literal notranslate"><span class="pre">recovery_window</span></code> and <code class="docutils literal notranslate"><span class="pre">trigger_window</span></code> values, e.g. <code class="docutils literal notranslate"><span class="pre">last_15m</span></code> . Can only be used for, and are
required for, anomaly monitors.</p></li>
<li><p><strong>monitor_thresholds</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'MonitorMonitorThresholdsArgs'</em><em>]</em><em>]</em>) – Alert thresholds of the monitor.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Datadog monitor.</p></li>
<li><p><strong>new_host_delay</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Time (in seconds) to allow a host to boot and applications to fully start before starting the evaluation of monitor
results. Should be a non negative integer. Defaults to <code class="docutils literal notranslate"><span class="pre">300</span></code>.</p></li>
<li><p><strong>no_data_timeframe</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of minutes before a monitor will notify when data stops reporting. Provider defaults to 10 minutes. We
recommend at least 2x the monitor timeframe for metric alerts or 2 minutes for service checks.</p></li>
<li><p><strong>notify_audit</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether tagged users will be notified on changes to this monitor. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>notify_no_data</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether this monitor will notify when data stops reporting. Defaults to false.</p></li>
<li><p><strong>query</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The monitor query to notify on. Note this is not the same query you see in the UI and the syntax is different depending
on the monitor type, please see the <a class="reference external" href="https://docs.datadoghq.com/api/v1/monitors/#create-a-monitor">API Reference</a> for
details. Warning: <code class="docutils literal notranslate"><span class="pre">terraform</span> <span class="pre">plan</span></code> won’t perform any validation of the query contents.</p>
</p></li>
<li><p><strong>renotify_interval</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of minutes after the last notification before a monitor will re-notify on the current status. It will only
re-notify if it’s not resolved.</p></li>
<li><p><strong>require_full_window</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether this monitor needs a full window of data before it’s evaluated. We highly recommend you set
this to <code class="docutils literal notranslate"><span class="pre">false</span></code> for s metrics, otherwise some evaluations will be skipped. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code> for <code class="docutils literal notranslate"><span class="pre">on</span> <span class="pre">average</span></code>, <code class="docutils literal notranslate"><span class="pre">at</span> <span class="pre">all</span>
<span class="pre">times</span></code> and <code class="docutils literal notranslate"><span class="pre">in</span> <span class="pre">total</span></code> aggregation. <code class="docutils literal notranslate"><span class="pre">false</span></code> otherwise.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>silenced</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Each scope will be muted until the given POSIX timestamp or forever if the value is <code class="docutils literal notranslate"><span class="pre">0</span></code>. Use <code class="docutils literal notranslate"><span class="pre">-1</span></code> if you want to unmute
the scope. Deprecated: the silenced parameter is being deprecated in favor of the downtime resource. This will be
removed in the next major version of the Terraform Provider.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of tags to associate with your monitor. This can help you categorize and filter monitors in the manage monitors
page of the UI. Note: it’s not currently possible to filter by these tags when querying via the API</p></li>
<li><p><strong>threshold_windows</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'MonitorThresholdWindowsArgs'</em><em>]</em><em>]</em>) – A mapping containing <code class="docutils literal notranslate"><span class="pre">recovery_window</span></code> and <code class="docutils literal notranslate"><span class="pre">trigger_window</span></code> values, e.g. <code class="docutils literal notranslate"><span class="pre">last_15m</span></code>. Can only be used for, and are
required for, anomaly monitors.</p></li>
<li><p><strong>thresholds</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'MonitorThresholdsArgs'</em><em>]</em><em>]</em>) – Alert thresholds of the monitor.</p></li>
<li><p><strong>timeout_h</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of hours of the monitor not reporting data before it will automatically resolve from a triggered state.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The type of the monitor. The mapping from these types to the types found in the Datadog Web UI can be found in the
Datadog API <a class="reference external" href="https://docs.datadoghq.com/api/v1/monitors/#create-a-monitor">documentation page</a>. Note: The monitor type
cannot be changed after a monitor is created.</p>
</p></li>
<li><p><strong>validate</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">false</span></code>, skip the validation call done during plan.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.enable_logs_sample">
<em class="property">property </em><code class="sig-name descname">enable_logs_sample</code><a class="headerlink" href="#pulumi_datadog.Monitor.enable_logs_sample" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean indicating whether or not to include a list of log values which triggered the alert. This is only used by log
monitors. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.escalation_message">
<em class="property">property </em><code class="sig-name descname">escalation_message</code><a class="headerlink" href="#pulumi_datadog.Monitor.escalation_message" title="Permalink to this definition">¶</a></dt>
<dd><p>A message to include with a re-notification. Supports the <code class="docutils literal notranslate"><span class="pre">&#64;username</span></code> notification allowed elsewhere.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.evaluation_delay">
<em class="property">property </em><code class="sig-name descname">evaluation_delay</code><a class="headerlink" href="#pulumi_datadog.Monitor.evaluation_delay" title="Permalink to this definition">¶</a></dt>
<dd><p>(Only applies to metric alert) Time (in seconds) to delay evaluation, as a non-negative integer. For example, if the
value is set to <code class="docutils literal notranslate"><span class="pre">300</span></code> (5min), the <code class="docutils literal notranslate"><span class="pre">timeframe</span></code> is set to <code class="docutils literal notranslate"><span class="pre">last_5m</span></code> and the time is 7:00, the monitor will evaluate data
from 6:50 to 6:55. This is useful for AWS CloudWatch and other backfilled metrics to ensure the monitor will always have
data during evaluation.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.force_delete">
<em class="property">property </em><code class="sig-name descname">force_delete</code><a class="headerlink" href="#pulumi_datadog.Monitor.force_delete" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean indicating whether this monitor can be deleted even if it’s referenced by other resources (e.g. SLO,
composite monitor).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.include_tags">
<em class="property">property </em><code class="sig-name descname">include_tags</code><a class="headerlink" href="#pulumi_datadog.Monitor.include_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean indicating whether notifications from this monitor automatically insert its triggering tags into the title.
Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.locked">
<em class="property">property </em><code class="sig-name descname">locked</code><a class="headerlink" href="#pulumi_datadog.Monitor.locked" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean indicating whether changes to to this monitor should be restricted to the creator or admins. Defaults to
<code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.message">
<em class="property">property </em><code class="sig-name descname">message</code><a class="headerlink" href="#pulumi_datadog.Monitor.message" title="Permalink to this definition">¶</a></dt>
<dd><p>A message to include with notifications for this monitor. Email notifications can be sent to specific users by using the
same <code class="docutils literal notranslate"><span class="pre">&#64;username</span></code> notation as events.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.monitor_threshold_windows">
<em class="property">property </em><code class="sig-name descname">monitor_threshold_windows</code><a class="headerlink" href="#pulumi_datadog.Monitor.monitor_threshold_windows" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping containing <code class="docutils literal notranslate"><span class="pre">recovery_window</span></code> and <code class="docutils literal notranslate"><span class="pre">trigger_window</span></code> values, e.g. <code class="docutils literal notranslate"><span class="pre">last_15m</span></code> . Can only be used for, and are
required for, anomaly monitors.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.monitor_thresholds">
<em class="property">property </em><code class="sig-name descname">monitor_thresholds</code><a class="headerlink" href="#pulumi_datadog.Monitor.monitor_thresholds" title="Permalink to this definition">¶</a></dt>
<dd><p>Alert thresholds of the monitor.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_datadog.Monitor.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of Datadog monitor.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.new_host_delay">
<em class="property">property </em><code class="sig-name descname">new_host_delay</code><a class="headerlink" href="#pulumi_datadog.Monitor.new_host_delay" title="Permalink to this definition">¶</a></dt>
<dd><p>Time (in seconds) to allow a host to boot and applications to fully start before starting the evaluation of monitor
results. Should be a non negative integer. Defaults to <code class="docutils literal notranslate"><span class="pre">300</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.no_data_timeframe">
<em class="property">property </em><code class="sig-name descname">no_data_timeframe</code><a class="headerlink" href="#pulumi_datadog.Monitor.no_data_timeframe" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of minutes before a monitor will notify when data stops reporting. Provider defaults to 10 minutes. We
recommend at least 2x the monitor timeframe for metric alerts or 2 minutes for service checks.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.notify_audit">
<em class="property">property </em><code class="sig-name descname">notify_audit</code><a class="headerlink" href="#pulumi_datadog.Monitor.notify_audit" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean indicating whether tagged users will be notified on changes to this monitor. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.notify_no_data">
<em class="property">property </em><code class="sig-name descname">notify_no_data</code><a class="headerlink" href="#pulumi_datadog.Monitor.notify_no_data" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean indicating whether this monitor will notify when data stops reporting. Defaults to false.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.query">
<em class="property">property </em><code class="sig-name descname">query</code><a class="headerlink" href="#pulumi_datadog.Monitor.query" title="Permalink to this definition">¶</a></dt>
<dd><p>The monitor query to notify on. Note this is not the same query you see in the UI and the syntax is different depending
on the monitor type, please see the <a class="reference external" href="https://docs.datadoghq.com/api/v1/monitors/#create-a-monitor">API Reference</a> for
details. Warning: <code class="docutils literal notranslate"><span class="pre">terraform</span> <span class="pre">plan</span></code> won’t perform any validation of the query contents.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.renotify_interval">
<em class="property">property </em><code class="sig-name descname">renotify_interval</code><a class="headerlink" href="#pulumi_datadog.Monitor.renotify_interval" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of minutes after the last notification before a monitor will re-notify on the current status. It will only
re-notify if it’s not resolved.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.require_full_window">
<em class="property">property </em><code class="sig-name descname">require_full_window</code><a class="headerlink" href="#pulumi_datadog.Monitor.require_full_window" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean indicating whether this monitor needs a full window of data before it’s evaluated. We highly recommend you set
this to <code class="docutils literal notranslate"><span class="pre">false</span></code> for s metrics, otherwise some evaluations will be skipped. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code> for <code class="docutils literal notranslate"><span class="pre">on</span> <span class="pre">average</span></code>, <code class="docutils literal notranslate"><span class="pre">at</span> <span class="pre">all</span>
<span class="pre">times</span></code> and <code class="docutils literal notranslate"><span class="pre">in</span> <span class="pre">total</span></code> aggregation. <code class="docutils literal notranslate"><span class="pre">false</span></code> otherwise.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.silenced">
<em class="property">property </em><code class="sig-name descname">silenced</code><a class="headerlink" href="#pulumi_datadog.Monitor.silenced" title="Permalink to this definition">¶</a></dt>
<dd><p>Each scope will be muted until the given POSIX timestamp or forever if the value is <code class="docutils literal notranslate"><span class="pre">0</span></code>. Use <code class="docutils literal notranslate"><span class="pre">-1</span></code> if you want to unmute
the scope. Deprecated: the silenced parameter is being deprecated in favor of the downtime resource. This will be
removed in the next major version of the Terraform Provider.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_datadog.Monitor.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tags to associate with your monitor. This can help you categorize and filter monitors in the manage monitors
page of the UI. Note: it’s not currently possible to filter by these tags when querying via the API</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.threshold_windows">
<em class="property">property </em><code class="sig-name descname">threshold_windows</code><a class="headerlink" href="#pulumi_datadog.Monitor.threshold_windows" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping containing <code class="docutils literal notranslate"><span class="pre">recovery_window</span></code> and <code class="docutils literal notranslate"><span class="pre">trigger_window</span></code> values, e.g. <code class="docutils literal notranslate"><span class="pre">last_15m</span></code>. Can only be used for, and are
required for, anomaly monitors.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.thresholds">
<em class="property">property </em><code class="sig-name descname">thresholds</code><a class="headerlink" href="#pulumi_datadog.Monitor.thresholds" title="Permalink to this definition">¶</a></dt>
<dd><p>Alert thresholds of the monitor.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.timeout_h">
<em class="property">property </em><code class="sig-name descname">timeout_h</code><a class="headerlink" href="#pulumi_datadog.Monitor.timeout_h" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of hours of the monitor not reporting data before it will automatically resolve from a triggered state.
Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_datadog.Monitor.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the monitor. The mapping from these types to the types found in the Datadog Web UI can be found in the
Datadog API <a class="reference external" href="https://docs.datadoghq.com/api/v1/monitors/#create-a-monitor">documentation page</a>. Note: The monitor type
cannot be changed after a monitor is created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.validate">
<em class="property">property </em><code class="sig-name descname">validate</code><a class="headerlink" href="#pulumi_datadog.Monitor.validate" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to <code class="docutils literal notranslate"><span class="pre">false</span></code>, skip the validation call done during plan.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.Monitor.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.Monitor.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.Monitor.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">validate</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the datadog package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>api_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Required unless validate is false) Datadog API key. This can also be set via the DD_API_KEY environment variable.</p></li>
<li><p><strong>api_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The API Url. This can also be set via the DD_HOST environment variable. Note that this URL must not end with the /api/
path. For example, <a class="reference external" href="https://api.datadoghq.com/">https://api.datadoghq.com/</a> is a correct value, while <a class="reference external" href="https://api.datadoghq.com/api/">https://api.datadoghq.com/api/</a> is not. And if
you’re working with “EU” version of Datadog, use <a class="reference external" href="https://api.datadoghq.eu/">https://api.datadoghq.eu/</a>.</p></li>
<li><p><strong>app_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Required unless validate is false) Datadog APP key. This can also be set via the DD_APP_KEY environment variable.</p></li>
<li><p><strong>validate</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enables validation of the provided API and APP keys during provider initialization. Default is true. When false, api_key
and app_key won’t be checked.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_datadog.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.Role">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">Role</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="p">:</span> <span class="n">Union[Sequence[Union[RolePermissionArgs, Mapping[str, Any], Awaitable[Union[RolePermissionArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[RolePermissionArgs, Mapping[str, Any], Awaitable[Union[RolePermissionArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.Role" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Datadog role resource. This can be used to create and manage Datadog roles.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="n">bar</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">get_permissions</span><span class="p">()</span>
<span class="c1"># Create a new Datadog role</span>
<span class="n">foo</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">Role</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">permissions</span><span class="o">=</span><span class="p">[</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">RolePermissionArgs</span><span class="p">(</span>
            <span class="nb">id</span><span class="o">=</span><span class="n">bar</span><span class="o">.</span><span class="n">permissions</span><span class="p">[</span><span class="s2">&quot;monitorsDowntime&quot;</span><span class="p">],</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">RolePermissionArgs</span><span class="p">(</span>
            <span class="nb">id</span><span class="o">=</span><span class="n">bar</span><span class="o">.</span><span class="n">permissions</span><span class="p">[</span><span class="s2">&quot;monitorsWrite&quot;</span><span class="p">],</span>
        <span class="p">),</span>
    <span class="p">])</span>
</pre></div>
</div>
<p>Roles can be imported using their ID, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import datadog:index/role:Role example_role <span class="m">000000</span>-0000-0000-0000-000000000000
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the role.</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'RolePermissionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Set of objects containing the permission ID and the name of the permissions granted to this role.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_datadog.Role.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="p">:</span> <span class="n">Union[Sequence[Union[RolePermissionArgs, Mapping[str, Any], Awaitable[Union[RolePermissionArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[RolePermissionArgs, Mapping[str, Any], Awaitable[Union[RolePermissionArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_count</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.role.Role<a class="headerlink" href="#pulumi_datadog.Role.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Role resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the role.</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'RolePermissionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Set of objects containing the permission ID and the name of the permissions granted to this role.</p></li>
<li><p><strong>user_count</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Number of users that have this role.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Role.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_datadog.Role.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the role.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Role.permissions">
<em class="property">property </em><code class="sig-name descname">permissions</code><a class="headerlink" href="#pulumi_datadog.Role.permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of objects containing the permission ID and the name of the permissions granted to this role.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Role.user_count">
<em class="property">property </em><code class="sig-name descname">user_count</code><a class="headerlink" href="#pulumi_datadog.Role.user_count" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of users that have this role.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Role.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.Role.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.Role.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.Role.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.ScreenBoard">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">ScreenBoard</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">height</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">read_only</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shared</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_variables</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ScreenBoardTemplateVariableArgs, Mapping[str, Any], Awaitable[Union[ScreenBoardTemplateVariableArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ScreenBoardTemplateVariableArgs, Mapping[str, Any], Awaitable[Union[ScreenBoardTemplateVariableArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">title</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">widgets</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ScreenBoardWidgetArgs, Mapping[str, Any], Awaitable[Union[ScreenBoardWidgetArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ScreenBoardWidgetArgs, Mapping[str, Any], Awaitable[Union[ScreenBoardWidgetArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">width</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.ScreenBoard" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Datadog screenboard resource. This can be used to create and manage Datadog screenboards.</p>
<blockquote>
<div><p><strong>Note:</strong> This resource is outdated. Use the new <code class="docutils literal notranslate"><span class="pre">Dashboard</span></code> resource instead.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">json</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="c1"># Create a new Datadog screenboard</span>
<span class="n">acceptance_test</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoard</span><span class="p">(</span><span class="s2">&quot;acceptanceTest&quot;</span><span class="p">,</span>
    <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Test Screenboard&quot;</span><span class="p">,</span>
    <span class="n">read_only</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">template_variables</span><span class="o">=</span><span class="p">[</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardTemplateVariableArgs</span><span class="p">(</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">&quot;varname 1&quot;</span><span class="p">,</span>
            <span class="n">prefix</span><span class="o">=</span><span class="s2">&quot;pod_name&quot;</span><span class="p">,</span>
            <span class="n">default</span><span class="o">=</span><span class="s2">&quot;*&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardTemplateVariableArgs</span><span class="p">(</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">&quot;varname 2&quot;</span><span class="p">,</span>
            <span class="n">prefix</span><span class="o">=</span><span class="s2">&quot;service_name&quot;</span><span class="p">,</span>
            <span class="n">default</span><span class="o">=</span><span class="s2">&quot;autoscaling&quot;</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">],</span>
    <span class="n">widgets</span><span class="o">=</span><span class="p">[</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetArgs</span><span class="p">(</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;free_text&quot;</span><span class="p">,</span>
            <span class="n">x</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
            <span class="n">y</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
            <span class="n">text</span><span class="o">=</span><span class="s2">&quot;test text&quot;</span><span class="p">,</span>
            <span class="n">text_align</span><span class="o">=</span><span class="s2">&quot;right&quot;</span><span class="p">,</span>
            <span class="n">font_size</span><span class="o">=</span><span class="s2">&quot;36&quot;</span><span class="p">,</span>
            <span class="n">color</span><span class="o">=</span><span class="s2">&quot;#ffc0cb&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetArgs</span><span class="p">(</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;timeseries&quot;</span><span class="p">,</span>
            <span class="n">x</span><span class="o">=</span><span class="mi">25</span><span class="p">,</span>
            <span class="n">y</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
            <span class="n">title</span><span class="o">=</span><span class="s2">&quot;graph title terraform&quot;</span><span class="p">,</span>
            <span class="n">title_size</span><span class="o">=</span><span class="mi">16</span><span class="p">,</span>
            <span class="n">title_align</span><span class="o">=</span><span class="s2">&quot;right&quot;</span><span class="p">,</span>
            <span class="n">legend</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="n">legend_size</span><span class="o">=</span><span class="s2">&quot;16&quot;</span><span class="p">,</span>
            <span class="n">time</span><span class="o">=</span><span class="p">{</span>
                <span class="s2">&quot;live_span&quot;</span><span class="p">:</span> <span class="s2">&quot;1d&quot;</span><span class="p">,</span>
            <span class="p">},</span>
            <span class="n">tile_deves</span><span class="o">=</span><span class="p">[</span><span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetTileDefArgs</span><span class="p">(</span>
                <span class="n">viz</span><span class="o">=</span><span class="s2">&quot;timeseries&quot;</span><span class="p">,</span>
                <span class="n">requests</span><span class="o">=</span><span class="p">[</span>
                    <span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetTileDefRequestArgs</span><span class="p">(</span>
                        <span class="n">q</span><span class="o">=</span><span class="s2">&quot;avg:system.cpu.user{*}&quot;</span><span class="p">,</span>
                        <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;line&quot;</span><span class="p">,</span>
                        <span class="n">style</span><span class="o">=</span><span class="p">{</span>
                            <span class="s2">&quot;palette&quot;</span><span class="p">:</span> <span class="s2">&quot;purple&quot;</span><span class="p">,</span>
                            <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;dashed&quot;</span><span class="p">,</span>
                            <span class="s2">&quot;width&quot;</span><span class="p">:</span> <span class="s2">&quot;thin&quot;</span><span class="p">,</span>
                        <span class="p">},</span>
                        <span class="n">metadata_json</span><span class="o">=</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">({</span>
                            <span class="s2">&quot;avg:system.cpu.user{*}&quot;</span><span class="p">:</span> <span class="p">{</span>
                                <span class="s2">&quot;alias&quot;</span><span class="p">:</span> <span class="s2">&quot;CPU Usage&quot;</span><span class="p">,</span>
                            <span class="p">},</span>
                        <span class="p">}),</span>
                    <span class="p">),</span>
                    <span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetTileDefRequestArgs</span><span class="p">(</span>
                        <span class="n">log_query</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetTileDefRequestLogQueryArgs</span><span class="p">(</span>
                            <span class="n">index</span><span class="o">=</span><span class="s2">&quot;mcnulty&quot;</span><span class="p">,</span>
                            <span class="n">compute</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetTileDefRequestLogQueryComputeArgs</span><span class="p">(</span>
                                <span class="n">aggregation</span><span class="o">=</span><span class="s2">&quot;avg&quot;</span><span class="p">,</span>
                                <span class="n">facet</span><span class="o">=</span><span class="s2">&quot;@duration&quot;</span><span class="p">,</span>
                                <span class="n">interval</span><span class="o">=</span><span class="s2">&quot;5000&quot;</span><span class="p">,</span>
                            <span class="p">),</span>
                            <span class="n">search</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetTileDefRequestLogQuerySearchArgs</span><span class="p">(</span>
                                <span class="n">query</span><span class="o">=</span><span class="s2">&quot;status:info&quot;</span><span class="p">,</span>
                            <span class="p">),</span>
                            <span class="n">group_bies</span><span class="o">=</span><span class="p">[{</span>
                                <span class="s2">&quot;facet&quot;</span><span class="p">:</span> <span class="s2">&quot;host&quot;</span><span class="p">,</span>
                                <span class="s2">&quot;limit&quot;</span><span class="p">:</span> <span class="mi">10</span><span class="p">,</span>
                                <span class="s2">&quot;sort&quot;</span><span class="p">:</span> <span class="p">{</span>
                                    <span class="s2">&quot;aggregation&quot;</span><span class="p">:</span> <span class="s2">&quot;avg&quot;</span><span class="p">,</span>
                                    <span class="s2">&quot;order&quot;</span><span class="p">:</span> <span class="s2">&quot;desc&quot;</span><span class="p">,</span>
                                    <span class="s2">&quot;facet&quot;</span><span class="p">:</span> <span class="s2">&quot;@duration&quot;</span><span class="p">,</span>
                                <span class="p">},</span>
                            <span class="p">}],</span>
                        <span class="p">),</span>
                        <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;area&quot;</span><span class="p">,</span>
                    <span class="p">),</span>
                    <span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetTileDefRequestArgs</span><span class="p">(</span>
                        <span class="n">apm_query</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetTileDefRequestApmQueryArgs</span><span class="p">(</span>
                            <span class="n">index</span><span class="o">=</span><span class="s2">&quot;apm-search&quot;</span><span class="p">,</span>
                            <span class="n">compute</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetTileDefRequestApmQueryComputeArgs</span><span class="p">(</span>
                                <span class="n">aggregation</span><span class="o">=</span><span class="s2">&quot;avg&quot;</span><span class="p">,</span>
                                <span class="n">facet</span><span class="o">=</span><span class="s2">&quot;@duration&quot;</span><span class="p">,</span>
                                <span class="n">interval</span><span class="o">=</span><span class="s2">&quot;5000&quot;</span><span class="p">,</span>
                            <span class="p">),</span>
                            <span class="n">search</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetTileDefRequestApmQuerySearchArgs</span><span class="p">(</span>
                                <span class="n">query</span><span class="o">=</span><span class="s2">&quot;type:web&quot;</span><span class="p">,</span>
                            <span class="p">),</span>
                            <span class="n">group_bies</span><span class="o">=</span><span class="p">[{</span>
                                <span class="s2">&quot;facet&quot;</span><span class="p">:</span> <span class="s2">&quot;resource_name&quot;</span><span class="p">,</span>
                                <span class="s2">&quot;limit&quot;</span><span class="p">:</span> <span class="mi">50</span><span class="p">,</span>
                                <span class="s2">&quot;sort&quot;</span><span class="p">:</span> <span class="p">{</span>
                                    <span class="s2">&quot;aggregation&quot;</span><span class="p">:</span> <span class="s2">&quot;avg&quot;</span><span class="p">,</span>
                                    <span class="s2">&quot;order&quot;</span><span class="p">:</span> <span class="s2">&quot;desc&quot;</span><span class="p">,</span>
                                    <span class="s2">&quot;facet&quot;</span><span class="p">:</span> <span class="s2">&quot;@string_query.interval&quot;</span><span class="p">,</span>
                                <span class="p">},</span>
                            <span class="p">}],</span>
                        <span class="p">),</span>
                        <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;bars&quot;</span><span class="p">,</span>
                    <span class="p">),</span>
                    <span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetTileDefRequestArgs</span><span class="p">(</span>
                        <span class="n">process_query</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetTileDefRequestProcessQueryArgs</span><span class="p">(</span>
                            <span class="n">metric</span><span class="o">=</span><span class="s2">&quot;process.stat.cpu.total_pct&quot;</span><span class="p">,</span>
                            <span class="n">search_by</span><span class="o">=</span><span class="s2">&quot;error&quot;</span><span class="p">,</span>
                            <span class="n">filter_bies</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;active&quot;</span><span class="p">],</span>
                            <span class="n">limit</span><span class="o">=</span><span class="mi">50</span><span class="p">,</span>
                        <span class="p">),</span>
                        <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;area&quot;</span><span class="p">,</span>
                    <span class="p">),</span>
                <span class="p">],</span>
                <span class="n">markers</span><span class="o">=</span><span class="p">[</span><span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetTileDefMarkerArgs</span><span class="p">(</span>
                    <span class="n">label</span><span class="o">=</span><span class="s2">&quot;test marker&quot;</span><span class="p">,</span>
                    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;error dashed&quot;</span><span class="p">,</span>
                    <span class="n">value</span><span class="o">=</span><span class="s2">&quot;y &lt; 6&quot;</span><span class="p">,</span>
                <span class="p">)],</span>
                <span class="n">events</span><span class="o">=</span><span class="p">[</span><span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetTileDefEventArgs</span><span class="p">(</span>
                    <span class="n">q</span><span class="o">=</span><span class="s2">&quot;test event&quot;</span><span class="p">,</span>
                <span class="p">)],</span>
            <span class="p">)],</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetArgs</span><span class="p">(</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;query_value&quot;</span><span class="p">,</span>
            <span class="n">x</span><span class="o">=</span><span class="mi">45</span><span class="p">,</span>
            <span class="n">y</span><span class="o">=</span><span class="mi">25</span><span class="p">,</span>
            <span class="n">title</span><span class="o">=</span><span class="s2">&quot;query value title terraform&quot;</span><span class="p">,</span>
            <span class="n">title_size</span><span class="o">=</span><span class="mi">20</span><span class="p">,</span>
            <span class="n">title_align</span><span class="o">=</span><span class="s2">&quot;center&quot;</span><span class="p">,</span>
            <span class="n">legend</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="n">legend_size</span><span class="o">=</span><span class="s2">&quot;16&quot;</span><span class="p">,</span>
            <span class="n">tile_deves</span><span class="o">=</span><span class="p">[</span><span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetTileDefArgs</span><span class="p">(</span>
                <span class="n">viz</span><span class="o">=</span><span class="s2">&quot;query_value&quot;</span><span class="p">,</span>
                <span class="n">requests</span><span class="o">=</span><span class="p">[</span><span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetTileDefRequestArgs</span><span class="p">(</span>
                    <span class="n">q</span><span class="o">=</span><span class="s2">&quot;avg:system.cpu.user{*}&quot;</span><span class="p">,</span>
                    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;line&quot;</span><span class="p">,</span>
                    <span class="n">style</span><span class="o">=</span><span class="p">{</span>
                        <span class="s2">&quot;palette&quot;</span><span class="p">:</span> <span class="s2">&quot;purple&quot;</span><span class="p">,</span>
                        <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;dashed&quot;</span><span class="p">,</span>
                        <span class="s2">&quot;width&quot;</span><span class="p">:</span> <span class="s2">&quot;thin&quot;</span><span class="p">,</span>
                    <span class="p">},</span>
                    <span class="n">conditional_formats</span><span class="o">=</span><span class="p">[</span>
                        <span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetTileDefRequestConditionalFormatArgs</span><span class="p">(</span>
                            <span class="n">comparator</span><span class="o">=</span><span class="s2">&quot;&gt;&quot;</span><span class="p">,</span>
                            <span class="n">value</span><span class="o">=</span><span class="s2">&quot;1&quot;</span><span class="p">,</span>
                            <span class="n">palette</span><span class="o">=</span><span class="s2">&quot;white_on_red&quot;</span><span class="p">,</span>
                        <span class="p">),</span>
                        <span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetTileDefRequestConditionalFormatArgs</span><span class="p">(</span>
                            <span class="n">comparator</span><span class="o">=</span><span class="s2">&quot;&gt;=&quot;</span><span class="p">,</span>
                            <span class="n">value</span><span class="o">=</span><span class="s2">&quot;2&quot;</span><span class="p">,</span>
                            <span class="n">palette</span><span class="o">=</span><span class="s2">&quot;white_on_yellow&quot;</span><span class="p">,</span>
                        <span class="p">),</span>
                    <span class="p">],</span>
                    <span class="n">aggregator</span><span class="o">=</span><span class="s2">&quot;max&quot;</span><span class="p">,</span>
                <span class="p">)],</span>
                <span class="n">custom_unit</span><span class="o">=</span><span class="s2">&quot;%&quot;</span><span class="p">,</span>
                <span class="n">autoscale</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
                <span class="n">precision</span><span class="o">=</span><span class="s2">&quot;6&quot;</span><span class="p">,</span>
                <span class="n">text_align</span><span class="o">=</span><span class="s2">&quot;right&quot;</span><span class="p">,</span>
            <span class="p">)],</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetArgs</span><span class="p">(</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;toplist&quot;</span><span class="p">,</span>
            <span class="n">x</span><span class="o">=</span><span class="mi">65</span><span class="p">,</span>
            <span class="n">y</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
            <span class="n">title</span><span class="o">=</span><span class="s2">&quot;toplist title terraform&quot;</span><span class="p">,</span>
            <span class="n">legend</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="n">legend_size</span><span class="o">=</span><span class="s2">&quot;auto&quot;</span><span class="p">,</span>
            <span class="n">time</span><span class="o">=</span><span class="p">{</span>
                <span class="s2">&quot;live_span&quot;</span><span class="p">:</span> <span class="s2">&quot;1d&quot;</span><span class="p">,</span>
            <span class="p">},</span>
            <span class="n">tile_deves</span><span class="o">=</span><span class="p">[</span><span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetTileDefArgs</span><span class="p">(</span>
                <span class="n">viz</span><span class="o">=</span><span class="s2">&quot;toplist&quot;</span><span class="p">,</span>
                <span class="n">requests</span><span class="o">=</span><span class="p">[</span><span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetTileDefRequestArgs</span><span class="p">(</span>
                    <span class="n">q</span><span class="o">=</span><span class="s2">&quot;top(avg:system.load.1{*} by </span><span class="si">{host}</span><span class="s2">, 10, &#39;mean&#39;, &#39;desc&#39;)&quot;</span><span class="p">,</span>
                    <span class="n">style</span><span class="o">=</span><span class="p">{</span>
                        <span class="s2">&quot;palette&quot;</span><span class="p">:</span> <span class="s2">&quot;purple&quot;</span><span class="p">,</span>
                        <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;dashed&quot;</span><span class="p">,</span>
                        <span class="s2">&quot;width&quot;</span><span class="p">:</span> <span class="s2">&quot;thin&quot;</span><span class="p">,</span>
                    <span class="p">},</span>
                    <span class="n">conditional_formats</span><span class="o">=</span><span class="p">[</span><span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetTileDefRequestConditionalFormatArgs</span><span class="p">(</span>
                        <span class="n">comparator</span><span class="o">=</span><span class="s2">&quot;&gt;&quot;</span><span class="p">,</span>
                        <span class="n">value</span><span class="o">=</span><span class="s2">&quot;4&quot;</span><span class="p">,</span>
                        <span class="n">palette</span><span class="o">=</span><span class="s2">&quot;white_on_green&quot;</span><span class="p">,</span>
                    <span class="p">)],</span>
                <span class="p">)],</span>
            <span class="p">)],</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetArgs</span><span class="p">(</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;change&quot;</span><span class="p">,</span>
            <span class="n">x</span><span class="o">=</span><span class="mi">85</span><span class="p">,</span>
            <span class="n">y</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
            <span class="n">title</span><span class="o">=</span><span class="s2">&quot;change title terraform&quot;</span><span class="p">,</span>
            <span class="n">tile_deves</span><span class="o">=</span><span class="p">[</span><span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetTileDefArgs</span><span class="p">(</span>
                <span class="n">viz</span><span class="o">=</span><span class="s2">&quot;change&quot;</span><span class="p">,</span>
                <span class="n">requests</span><span class="o">=</span><span class="p">[</span><span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetTileDefRequestArgs</span><span class="p">(</span>
                    <span class="n">q</span><span class="o">=</span><span class="s2">&quot;min:system.load.1{*} by </span><span class="si">{host}</span><span class="s2">&quot;</span><span class="p">,</span>
                    <span class="n">compare_to</span><span class="o">=</span><span class="s2">&quot;week_before&quot;</span><span class="p">,</span>
                    <span class="n">change_type</span><span class="o">=</span><span class="s2">&quot;relative&quot;</span><span class="p">,</span>
                    <span class="n">order_by</span><span class="o">=</span><span class="s2">&quot;present&quot;</span><span class="p">,</span>
                    <span class="n">order_dir</span><span class="o">=</span><span class="s2">&quot;asc&quot;</span><span class="p">,</span>
                    <span class="n">extra_col</span><span class="o">=</span><span class="s2">&quot;&quot;</span><span class="p">,</span>
                    <span class="n">increase_good</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
                <span class="p">)],</span>
            <span class="p">)],</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetArgs</span><span class="p">(</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;event_timeline&quot;</span><span class="p">,</span>
            <span class="n">x</span><span class="o">=</span><span class="mi">105</span><span class="p">,</span>
            <span class="n">y</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
            <span class="n">title</span><span class="o">=</span><span class="s2">&quot;event_timeline title terraform&quot;</span><span class="p">,</span>
            <span class="n">query</span><span class="o">=</span><span class="s2">&quot;status:error&quot;</span><span class="p">,</span>
            <span class="n">time</span><span class="o">=</span><span class="p">{</span>
                <span class="s2">&quot;live_span&quot;</span><span class="p">:</span> <span class="s2">&quot;1d&quot;</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetArgs</span><span class="p">(</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;event_stream&quot;</span><span class="p">,</span>
            <span class="n">x</span><span class="o">=</span><span class="mi">115</span><span class="p">,</span>
            <span class="n">y</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
            <span class="n">title</span><span class="o">=</span><span class="s2">&quot;event_stream title terraform&quot;</span><span class="p">,</span>
            <span class="n">query</span><span class="o">=</span><span class="s2">&quot;*&quot;</span><span class="p">,</span>
            <span class="n">event_size</span><span class="o">=</span><span class="s2">&quot;l&quot;</span><span class="p">,</span>
            <span class="n">time</span><span class="o">=</span><span class="p">{</span>
                <span class="s2">&quot;live_span&quot;</span><span class="p">:</span> <span class="s2">&quot;4h&quot;</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetArgs</span><span class="p">(</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;image&quot;</span><span class="p">,</span>
            <span class="n">x</span><span class="o">=</span><span class="mi">145</span><span class="p">,</span>
            <span class="n">y</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
            <span class="n">title</span><span class="o">=</span><span class="s2">&quot;image title terraform&quot;</span><span class="p">,</span>
            <span class="n">sizing</span><span class="o">=</span><span class="s2">&quot;fit&quot;</span><span class="p">,</span>
            <span class="n">margin</span><span class="o">=</span><span class="s2">&quot;large&quot;</span><span class="p">,</span>
            <span class="n">url</span><span class="o">=</span><span class="s2">&quot;https://datadog-prod.imgix.net/img/dd_logo_70x75.png&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetArgs</span><span class="p">(</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;note&quot;</span><span class="p">,</span>
            <span class="n">x</span><span class="o">=</span><span class="mi">165</span><span class="p">,</span>
            <span class="n">y</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
            <span class="n">bgcolor</span><span class="o">=</span><span class="s2">&quot;pink&quot;</span><span class="p">,</span>
            <span class="n">text_align</span><span class="o">=</span><span class="s2">&quot;right&quot;</span><span class="p">,</span>
            <span class="n">font_size</span><span class="o">=</span><span class="s2">&quot;36&quot;</span><span class="p">,</span>
            <span class="n">tick</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="n">tick_edge</span><span class="o">=</span><span class="s2">&quot;bottom&quot;</span><span class="p">,</span>
            <span class="n">tick_pos</span><span class="o">=</span><span class="s2">&quot;50%&quot;</span><span class="p">,</span>
            <span class="n">html</span><span class="o">=</span><span class="s2">&quot;&lt;b&gt;test note&lt;/b&gt;&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetArgs</span><span class="p">(</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;alert_graph&quot;</span><span class="p">,</span>
            <span class="n">x</span><span class="o">=</span><span class="mi">185</span><span class="p">,</span>
            <span class="n">y</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
            <span class="n">title</span><span class="o">=</span><span class="s2">&quot;alert graph title terraform&quot;</span><span class="p">,</span>
            <span class="n">alert_id</span><span class="o">=</span><span class="mi">123456</span><span class="p">,</span>
            <span class="n">viz_type</span><span class="o">=</span><span class="s2">&quot;toplist&quot;</span><span class="p">,</span>
            <span class="n">time</span><span class="o">=</span><span class="p">{</span>
                <span class="s2">&quot;live_span&quot;</span><span class="p">:</span> <span class="s2">&quot;15m&quot;</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetArgs</span><span class="p">(</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;alert_value&quot;</span><span class="p">,</span>
            <span class="n">x</span><span class="o">=</span><span class="mi">205</span><span class="p">,</span>
            <span class="n">y</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
            <span class="n">title</span><span class="o">=</span><span class="s2">&quot;alert value title terraform&quot;</span><span class="p">,</span>
            <span class="n">alert_id</span><span class="o">=</span><span class="mi">123456</span><span class="p">,</span>
            <span class="n">text_size</span><span class="o">=</span><span class="s2">&quot;fill_height&quot;</span><span class="p">,</span>
            <span class="n">text_align</span><span class="o">=</span><span class="s2">&quot;right&quot;</span><span class="p">,</span>
            <span class="n">precision</span><span class="o">=</span><span class="s2">&quot;*&quot;</span><span class="p">,</span>
            <span class="n">unit</span><span class="o">=</span><span class="s2">&quot;b&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetArgs</span><span class="p">(</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;iframe&quot;</span><span class="p">,</span>
            <span class="n">x</span><span class="o">=</span><span class="mi">225</span><span class="p">,</span>
            <span class="n">y</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
            <span class="n">url</span><span class="o">=</span><span class="s2">&quot;https://www.datadoghq.org&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetArgs</span><span class="p">(</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;check_status&quot;</span><span class="p">,</span>
            <span class="n">x</span><span class="o">=</span><span class="mi">245</span><span class="p">,</span>
            <span class="n">y</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
            <span class="n">title</span><span class="o">=</span><span class="s2">&quot;test title&quot;</span><span class="p">,</span>
            <span class="n">title_align</span><span class="o">=</span><span class="s2">&quot;left&quot;</span><span class="p">,</span>
            <span class="n">grouping</span><span class="o">=</span><span class="s2">&quot;check&quot;</span><span class="p">,</span>
            <span class="n">check</span><span class="o">=</span><span class="s2">&quot;aws.ecs.agent_connected&quot;</span><span class="p">,</span>
            <span class="n">tags</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;*&quot;</span><span class="p">],</span>
            <span class="n">group</span><span class="o">=</span><span class="s2">&quot;cluster:test&quot;</span><span class="p">,</span>
            <span class="n">time</span><span class="o">=</span><span class="p">{</span>
                <span class="s2">&quot;live_span&quot;</span><span class="p">:</span> <span class="s2">&quot;30m&quot;</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetArgs</span><span class="p">(</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;trace_service&quot;</span><span class="p">,</span>
            <span class="n">x</span><span class="o">=</span><span class="mi">265</span><span class="p">,</span>
            <span class="n">y</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
            <span class="n">env</span><span class="o">=</span><span class="s2">&quot;testEnv&quot;</span><span class="p">,</span>
            <span class="n">service_service</span><span class="o">=</span><span class="s2">&quot;&quot;</span><span class="p">,</span>
            <span class="n">service_name</span><span class="o">=</span><span class="s2">&quot;&quot;</span><span class="p">,</span>
            <span class="n">size_version</span><span class="o">=</span><span class="s2">&quot;large&quot;</span><span class="p">,</span>
            <span class="n">layout_version</span><span class="o">=</span><span class="s2">&quot;three_column&quot;</span><span class="p">,</span>
            <span class="n">must_show_hits</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="n">must_show_errors</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="n">must_show_latency</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="n">must_show_breakdown</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="n">must_show_distribution</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="n">must_show_resource_list</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="n">time</span><span class="o">=</span><span class="p">{</span>
                <span class="s2">&quot;live_span&quot;</span><span class="p">:</span> <span class="s2">&quot;30m&quot;</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetArgs</span><span class="p">(</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;hostmap&quot;</span><span class="p">,</span>
            <span class="n">x</span><span class="o">=</span><span class="mi">285</span><span class="p">,</span>
            <span class="n">y</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
            <span class="n">query</span><span class="o">=</span><span class="s2">&quot;avg:system.load.1{*} by </span><span class="si">{host}</span><span class="s2">&quot;</span><span class="p">,</span>
            <span class="n">tile_deves</span><span class="o">=</span><span class="p">[</span><span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetTileDefArgs</span><span class="p">(</span>
                <span class="n">viz</span><span class="o">=</span><span class="s2">&quot;hostmap&quot;</span><span class="p">,</span>
                <span class="n">node_type</span><span class="o">=</span><span class="s2">&quot;container&quot;</span><span class="p">,</span>
                <span class="n">scopes</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;datacenter:test&quot;</span><span class="p">],</span>
                <span class="n">groups</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;pod_name&quot;</span><span class="p">],</span>
                <span class="n">no_group_hosts</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
                <span class="n">no_metric_hosts</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
                <span class="n">requests</span><span class="o">=</span><span class="p">[</span><span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetTileDefRequestArgs</span><span class="p">(</span>
                    <span class="n">q</span><span class="o">=</span><span class="s2">&quot;max:process.stat.container.io.wbps{datacenter:test} by </span><span class="si">{host}</span><span class="s2">&quot;</span><span class="p">,</span>
                    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;fill&quot;</span><span class="p">,</span>
                <span class="p">)],</span>
                <span class="n">style</span><span class="o">=</span><span class="p">{</span>
                    <span class="s2">&quot;palette&quot;</span><span class="p">:</span> <span class="s2">&quot;hostmap_blues&quot;</span><span class="p">,</span>
                    <span class="s2">&quot;palette_flip&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
                    <span class="s2">&quot;fill_min&quot;</span><span class="p">:</span> <span class="mi">20</span><span class="p">,</span>
                    <span class="s2">&quot;fill_max&quot;</span><span class="p">:</span> <span class="mi">300</span><span class="p">,</span>
                <span class="p">},</span>
            <span class="p">)],</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetArgs</span><span class="p">(</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;manage_status&quot;</span><span class="p">,</span>
            <span class="n">x</span><span class="o">=</span><span class="mi">305</span><span class="p">,</span>
            <span class="n">y</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
            <span class="n">summary_type</span><span class="o">=</span><span class="s2">&quot;monitors&quot;</span><span class="p">,</span>
            <span class="n">display_format</span><span class="o">=</span><span class="s2">&quot;countsAndList&quot;</span><span class="p">,</span>
            <span class="n">color_preference</span><span class="o">=</span><span class="s2">&quot;background&quot;</span><span class="p">,</span>
            <span class="n">hide_zero_counts</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="n">show_last_triggered</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
            <span class="n">manage_status_show_title</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
            <span class="n">manage_status_title_text</span><span class="o">=</span><span class="s2">&quot;test title&quot;</span><span class="p">,</span>
            <span class="n">manage_status_title_size</span><span class="o">=</span><span class="s2">&quot;20&quot;</span><span class="p">,</span>
            <span class="n">manage_status_title_align</span><span class="o">=</span><span class="s2">&quot;right&quot;</span><span class="p">,</span>
            <span class="n">params</span><span class="o">=</span><span class="p">{</span>
                <span class="s2">&quot;sort&quot;</span><span class="p">:</span> <span class="s2">&quot;status,asc&quot;</span><span class="p">,</span>
                <span class="s2">&quot;text&quot;</span><span class="p">:</span> <span class="s2">&quot;status:alert&quot;</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetArgs</span><span class="p">(</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;log_stream&quot;</span><span class="p">,</span>
            <span class="n">x</span><span class="o">=</span><span class="mi">325</span><span class="p">,</span>
            <span class="n">y</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
            <span class="n">query</span><span class="o">=</span><span class="s2">&quot;source:kubernetes&quot;</span><span class="p">,</span>
            <span class="n">columns</span><span class="o">=</span><span class="s2">&quot;[&quot;</span><span class="n">column1</span><span class="s2">&quot;,&quot;</span><span class="n">column2</span><span class="s2">&quot;,&quot;</span><span class="n">column3</span><span class="s2">&quot;]&quot;</span><span class="p">,</span>
            <span class="n">logset</span><span class="o">=</span><span class="s2">&quot;1234&quot;</span><span class="p">,</span>
            <span class="n">time</span><span class="o">=</span><span class="p">{</span>
                <span class="s2">&quot;live_span&quot;</span><span class="p">:</span> <span class="s2">&quot;1h&quot;</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetArgs</span><span class="p">(</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;process&quot;</span><span class="p">,</span>
            <span class="n">x</span><span class="o">=</span><span class="mi">365</span><span class="p">,</span>
            <span class="n">y</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
            <span class="n">tile_deves</span><span class="o">=</span><span class="p">[</span><span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetTileDefArgs</span><span class="p">(</span>
                <span class="n">viz</span><span class="o">=</span><span class="s2">&quot;process&quot;</span><span class="p">,</span>
                <span class="n">requests</span><span class="o">=</span><span class="p">[</span><span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetTileDefRequestArgs</span><span class="p">(</span>
                    <span class="n">query_type</span><span class="o">=</span><span class="s2">&quot;process&quot;</span><span class="p">,</span>
                    <span class="n">metric</span><span class="o">=</span><span class="s2">&quot;process.stat.cpu.total_pct&quot;</span><span class="p">,</span>
                    <span class="n">text_filter</span><span class="o">=</span><span class="s2">&quot;&quot;</span><span class="p">,</span>
                    <span class="n">tag_filters</span><span class="o">=</span><span class="p">[],</span>
                    <span class="n">limit</span><span class="o">=</span><span class="mi">200</span><span class="p">,</span>
                    <span class="n">style</span><span class="o">=</span><span class="p">{</span>
                        <span class="s2">&quot;palette&quot;</span><span class="p">:</span> <span class="s2">&quot;dog_classic_area&quot;</span><span class="p">,</span>
                    <span class="p">},</span>
                <span class="p">)],</span>
            <span class="p">)],</span>
        <span class="p">),</span>
    <span class="p">])</span>
</pre></div>
</div>
<p>screenboards can be imported using their numeric ID, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import datadog:index/screenBoard:ScreenBoard my_service_screenboard <span class="m">2081</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>height</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Height of the screenboard</p></li>
<li><p><strong>read_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The read-only status of the screenboard. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>shared</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the screenboard is shared or not</p></li>
<li><p><strong>template_variables</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ScreenBoardTemplateVariableArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A list of template variables for using Dashboard templating.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the screenboard</p></li>
<li><p><strong>widgets</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ScreenBoardWidgetArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A list of widget definitions.</p></li>
<li><p><strong>width</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Width of the screenboard</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_datadog.ScreenBoard.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">height</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">read_only</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shared</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_variables</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ScreenBoardTemplateVariableArgs, Mapping[str, Any], Awaitable[Union[ScreenBoardTemplateVariableArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ScreenBoardTemplateVariableArgs, Mapping[str, Any], Awaitable[Union[ScreenBoardTemplateVariableArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">title</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">widgets</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ScreenBoardWidgetArgs, Mapping[str, Any], Awaitable[Union[ScreenBoardWidgetArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ScreenBoardWidgetArgs, Mapping[str, Any], Awaitable[Union[ScreenBoardWidgetArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">width</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.screen_board.ScreenBoard<a class="headerlink" href="#pulumi_datadog.ScreenBoard.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ScreenBoard resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>height</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Height of the screenboard</p></li>
<li><p><strong>read_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The read-only status of the screenboard. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>shared</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the screenboard is shared or not</p></li>
<li><p><strong>template_variables</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ScreenBoardTemplateVariableArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A list of template variables for using Dashboard templating.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the screenboard</p></li>
<li><p><strong>widgets</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ScreenBoardWidgetArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A list of widget definitions.</p></li>
<li><p><strong>width</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Width of the screenboard</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.ScreenBoard.height">
<em class="property">property </em><code class="sig-name descname">height</code><a class="headerlink" href="#pulumi_datadog.ScreenBoard.height" title="Permalink to this definition">¶</a></dt>
<dd><p>Height of the screenboard</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.ScreenBoard.read_only">
<em class="property">property </em><code class="sig-name descname">read_only</code><a class="headerlink" href="#pulumi_datadog.ScreenBoard.read_only" title="Permalink to this definition">¶</a></dt>
<dd><p>The read-only status of the screenboard. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.ScreenBoard.shared">
<em class="property">property </em><code class="sig-name descname">shared</code><a class="headerlink" href="#pulumi_datadog.ScreenBoard.shared" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the screenboard is shared or not</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.ScreenBoard.template_variables">
<em class="property">property </em><code class="sig-name descname">template_variables</code><a class="headerlink" href="#pulumi_datadog.ScreenBoard.template_variables" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of template variables for using Dashboard templating.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.ScreenBoard.title">
<em class="property">property </em><code class="sig-name descname">title</code><a class="headerlink" href="#pulumi_datadog.ScreenBoard.title" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the screenboard</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.ScreenBoard.widgets">
<em class="property">property </em><code class="sig-name descname">widgets</code><a class="headerlink" href="#pulumi_datadog.ScreenBoard.widgets" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of widget definitions.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.ScreenBoard.width">
<em class="property">property </em><code class="sig-name descname">width</code><a class="headerlink" href="#pulumi_datadog.ScreenBoard.width" title="Permalink to this definition">¶</a></dt>
<dd><p>Width of the screenboard</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.ScreenBoard.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.ScreenBoard.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.ScreenBoard.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.ScreenBoard.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.SecurityMonitoringRule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">SecurityMonitoringRule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cases</span><span class="p">:</span> <span class="n">Union[Sequence[Union[SecurityMonitoringRuleCaseArgs, Mapping[str, Any], Awaitable[Union[SecurityMonitoringRuleCaseArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[SecurityMonitoringRuleCaseArgs, Mapping[str, Any], Awaitable[Union[SecurityMonitoringRuleCaseArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">options</span><span class="p">:</span> <span class="n">Union[SecurityMonitoringRuleOptionsArgs, Mapping[str, Any], Awaitable[Union[SecurityMonitoringRuleOptionsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">queries</span><span class="p">:</span> <span class="n">Union[Sequence[Union[SecurityMonitoringRuleQueryArgs, Mapping[str, Any], Awaitable[Union[SecurityMonitoringRuleQueryArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[SecurityMonitoringRuleQueryArgs, Mapping[str, Any], Awaitable[Union[SecurityMonitoringRuleQueryArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.SecurityMonitoringRule" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Datadog <a class="reference external" href="https://docs.datadoghq.com/api/v2/security-monitoring/">Security Monitoring Rule API</a> resource. This can be used to create and manage Datadog security monitoring rules. To change settings for a default rule use <a class="reference external" href="https://www.terraform.io/resources/security_monitoring_default_rule">datadog_security_default_rule</a> instead.</p>
<p>Create a simple security monitoring rule.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="n">myrule</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">SecurityMonitoringRule</span><span class="p">(</span><span class="s2">&quot;myrule&quot;</span><span class="p">,</span>
    <span class="n">cases</span><span class="o">=</span><span class="p">[</span><span class="n">datadog</span><span class="o">.</span><span class="n">SecurityMonitoringRuleCaseArgs</span><span class="p">(</span>
        <span class="n">condition</span><span class="o">=</span><span class="s2">&quot;errors &gt; 3 &amp;&amp; warnings &gt; 10&quot;</span><span class="p">,</span>
        <span class="n">notifications</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;@user&quot;</span><span class="p">],</span>
        <span class="n">status</span><span class="o">=</span><span class="s2">&quot;high&quot;</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">message</span><span class="o">=</span><span class="s2">&quot;The rule has triggered.&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;My rule&quot;</span><span class="p">,</span>
    <span class="n">options</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">SecurityMonitoringRuleOptionsArgs</span><span class="p">(</span>
        <span class="n">evaluation_window</span><span class="o">=</span><span class="mi">300</span><span class="p">,</span>
        <span class="n">keep_alive</span><span class="o">=</span><span class="mi">600</span><span class="p">,</span>
        <span class="n">max_signal_duration</span><span class="o">=</span><span class="mi">900</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">queries</span><span class="o">=</span><span class="p">[</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">SecurityMonitoringRuleQueryArgs</span><span class="p">(</span>
            <span class="n">aggregation</span><span class="o">=</span><span class="s2">&quot;count&quot;</span><span class="p">,</span>
            <span class="n">group_by_fields</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;host&quot;</span><span class="p">],</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">&quot;errors&quot;</span><span class="p">,</span>
            <span class="n">query</span><span class="o">=</span><span class="s2">&quot;status:error&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">SecurityMonitoringRuleQueryArgs</span><span class="p">(</span>
            <span class="n">aggregation</span><span class="o">=</span><span class="s2">&quot;count&quot;</span><span class="p">,</span>
            <span class="n">group_by_fields</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;host&quot;</span><span class="p">],</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">&quot;warnings&quot;</span><span class="p">,</span>
            <span class="n">query</span><span class="o">=</span><span class="s2">&quot;status:warning&quot;</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">],</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;type:dos&quot;</span><span class="p">])</span>
</pre></div>
</div>
<p>Security monitoring rules can be imported using ID, e.g. console</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import datadog:index/securityMonitoringRule:SecurityMonitoringRule my_monitor m0o-hto-lkb
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cases</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SecurityMonitoringRuleCaseArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Cases for generating signals.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the rule is enabled.</p></li>
<li><p><strong>message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Message for generated signals.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the rule.</p></li>
<li><p><strong>options</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SecurityMonitoringRuleOptionsArgs'</em><em>]</em><em>]</em>) – Options on rules.</p></li>
<li><p><strong>queries</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SecurityMonitoringRuleQueryArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Queries for selecting logs which are part of the rule.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Tags for generated signals.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_datadog.SecurityMonitoringRule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cases</span><span class="p">:</span> <span class="n">Union[Sequence[Union[SecurityMonitoringRuleCaseArgs, Mapping[str, Any], Awaitable[Union[SecurityMonitoringRuleCaseArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[SecurityMonitoringRuleCaseArgs, Mapping[str, Any], Awaitable[Union[SecurityMonitoringRuleCaseArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">options</span><span class="p">:</span> <span class="n">Union[SecurityMonitoringRuleOptionsArgs, Mapping[str, Any], Awaitable[Union[SecurityMonitoringRuleOptionsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">queries</span><span class="p">:</span> <span class="n">Union[Sequence[Union[SecurityMonitoringRuleQueryArgs, Mapping[str, Any], Awaitable[Union[SecurityMonitoringRuleQueryArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[SecurityMonitoringRuleQueryArgs, Mapping[str, Any], Awaitable[Union[SecurityMonitoringRuleQueryArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.security_monitoring_rule.SecurityMonitoringRule<a class="headerlink" href="#pulumi_datadog.SecurityMonitoringRule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SecurityMonitoringRule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cases</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SecurityMonitoringRuleCaseArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Cases for generating signals.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the rule is enabled.</p></li>
<li><p><strong>message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Message for generated signals.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the rule.</p></li>
<li><p><strong>options</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SecurityMonitoringRuleOptionsArgs'</em><em>]</em><em>]</em>) – Options on rules.</p></li>
<li><p><strong>queries</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SecurityMonitoringRuleQueryArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Queries for selecting logs which are part of the rule.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Tags for generated signals.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SecurityMonitoringRule.cases">
<em class="property">property </em><code class="sig-name descname">cases</code><a class="headerlink" href="#pulumi_datadog.SecurityMonitoringRule.cases" title="Permalink to this definition">¶</a></dt>
<dd><p>Cases for generating signals.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SecurityMonitoringRule.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_datadog.SecurityMonitoringRule.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the rule is enabled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SecurityMonitoringRule.message">
<em class="property">property </em><code class="sig-name descname">message</code><a class="headerlink" href="#pulumi_datadog.SecurityMonitoringRule.message" title="Permalink to this definition">¶</a></dt>
<dd><p>Message for generated signals.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SecurityMonitoringRule.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_datadog.SecurityMonitoringRule.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the rule.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SecurityMonitoringRule.options">
<em class="property">property </em><code class="sig-name descname">options</code><a class="headerlink" href="#pulumi_datadog.SecurityMonitoringRule.options" title="Permalink to this definition">¶</a></dt>
<dd><p>Options on rules.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SecurityMonitoringRule.queries">
<em class="property">property </em><code class="sig-name descname">queries</code><a class="headerlink" href="#pulumi_datadog.SecurityMonitoringRule.queries" title="Permalink to this definition">¶</a></dt>
<dd><p>Queries for selecting logs which are part of the rule.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SecurityMonitoringRule.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_datadog.SecurityMonitoringRule.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Tags for generated signals.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SecurityMonitoringRule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.SecurityMonitoringRule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.SecurityMonitoringRule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.SecurityMonitoringRule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.ServiceLevelObjective">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">ServiceLevelObjective</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_delete</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitor_ids</span><span class="p">:</span> <span class="n">Union[Sequence[Union[int, Awaitable[int], Output[T]]], Awaitable[Sequence[Union[int, Awaitable[int], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="p">:</span> <span class="n">Union[ServiceLevelObjectiveQueryArgs, Mapping[str, Any], Awaitable[Union[ServiceLevelObjectiveQueryArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">thresholds</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ServiceLevelObjectiveThresholdArgs, Mapping[str, Any], Awaitable[Union[ServiceLevelObjectiveThresholdArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ServiceLevelObjectiveThresholdArgs, Mapping[str, Any], Awaitable[Union[ServiceLevelObjectiveThresholdArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">validate</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.ServiceLevelObjective" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Datadog service level objective resource. This can be used to create and manage Datadog service level objectives.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="c1"># Create a new Datadog service level objective</span>
<span class="n">foo</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">ServiceLevelObjective</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;My custom metric SLO&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Example Metric SLO&quot;</span><span class="p">,</span>
    <span class="n">query</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">ServiceLevelObjectiveQueryArgs</span><span class="p">(</span>
        <span class="n">denominator</span><span class="o">=</span><span class="s2">&quot;sum:my.custom.count.metric{*}.as_count()&quot;</span><span class="p">,</span>
        <span class="n">numerator</span><span class="o">=</span><span class="s2">&quot;sum:my.custom.count.metric{type:good_events}.as_count()&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;foo:bar&quot;</span><span class="p">,</span>
        <span class="s2">&quot;baz&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">thresholds</span><span class="o">=</span><span class="p">[</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">ServiceLevelObjectiveThresholdArgs</span><span class="p">(</span>
            <span class="n">target</span><span class="o">=</span><span class="mf">99.9</span><span class="p">,</span>
            <span class="n">target_display</span><span class="o">=</span><span class="s2">&quot;99.900&quot;</span><span class="p">,</span>
            <span class="n">timeframe</span><span class="o">=</span><span class="s2">&quot;7d&quot;</span><span class="p">,</span>
            <span class="n">warning</span><span class="o">=</span><span class="mf">99.99</span><span class="p">,</span>
            <span class="n">warning_display</span><span class="o">=</span><span class="s2">&quot;99.990&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">ServiceLevelObjectiveThresholdArgs</span><span class="p">(</span>
            <span class="n">target</span><span class="o">=</span><span class="mf">99.9</span><span class="p">,</span>
            <span class="n">target_display</span><span class="o">=</span><span class="s2">&quot;99.900&quot;</span><span class="p">,</span>
            <span class="n">timeframe</span><span class="o">=</span><span class="s2">&quot;30d&quot;</span><span class="p">,</span>
            <span class="n">warning</span><span class="o">=</span><span class="mf">99.99</span><span class="p">,</span>
            <span class="n">warning_display</span><span class="o">=</span><span class="s2">&quot;99.990&quot;</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">],</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;metric&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="c1"># Create a new Datadog service level objective</span>
<span class="n">bar</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">ServiceLevelObjective</span><span class="p">(</span><span class="s2">&quot;bar&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;My custom monitor SLO&quot;</span><span class="p">,</span>
    <span class="n">monitor_ids</span><span class="o">=</span><span class="p">[</span>
        <span class="mi">1</span><span class="p">,</span>
        <span class="mi">2</span><span class="p">,</span>
        <span class="mi">3</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Example Monitor SLO&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;foo:bar&quot;</span><span class="p">,</span>
        <span class="s2">&quot;baz&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">thresholds</span><span class="o">=</span><span class="p">[</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">ServiceLevelObjectiveThresholdArgs</span><span class="p">(</span>
            <span class="n">target</span><span class="o">=</span><span class="mf">99.9</span><span class="p">,</span>
            <span class="n">timeframe</span><span class="o">=</span><span class="s2">&quot;7d&quot;</span><span class="p">,</span>
            <span class="n">warning</span><span class="o">=</span><span class="mf">99.99</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">ServiceLevelObjectiveThresholdArgs</span><span class="p">(</span>
            <span class="n">target</span><span class="o">=</span><span class="mf">99.9</span><span class="p">,</span>
            <span class="n">timeframe</span><span class="o">=</span><span class="s2">&quot;30d&quot;</span><span class="p">,</span>
            <span class="n">warning</span><span class="o">=</span><span class="mf">99.99</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">],</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;monitor&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Service Level Objectives can be imported using their string ID, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import datadog:index/serviceLevelObjective:ServiceLevelObjective baz <span class="m">12345678901234567890123456789012</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of this service level objective.</p></li>
<li><p><strong>force_delete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether this monitor can be deleted even if it’s referenced by other resources (e.g. dashboards).</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>-   `thresholds`: (Required) - A list of thresholds and targets that define the service level objectives from the provided SLIs.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A static set of groups to filter monitor-based SLOs</p></li>
<li><p><strong>monitor_ids</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>int</em><em>]</em><em>]</em><em>]</em>) – A static set of monitor IDs to use as part of the SLO</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Datadog service level objective</p></li>
<li><p><strong>query</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceLevelObjectiveQueryArgs'</em><em>]</em><em>]</em>) – The metric query of good / total events</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of tags to associate with your service level objective. This can help you categorize and filter service level objectives in the service level objectives page of the UI. Note: it’s not currently possible to filter by these tags when querying via the API</p></li>
<li><p><strong>thresholds</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceLevelObjectiveThresholdArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A list of thresholds and targets that define the service level objectives from the provided SLIs.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The type of the service level objective. The mapping from these types to the types found in the Datadog Web UI can be
found in the Datadog API <a class="reference external" href="https://docs.datadoghq.com/api/v1/service-level-objectives/#create-a-slo-object">documentation
page</a>. Available options to choose from
are: <code class="docutils literal notranslate"><span class="pre">metric</span></code> and <code class="docutils literal notranslate"><span class="pre">monitor</span></code>.</p>
</p></li>
<li><p><strong>validate</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not to validate the SLO.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_datadog.ServiceLevelObjective.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_delete</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitor_ids</span><span class="p">:</span> <span class="n">Union[Sequence[Union[int, Awaitable[int], Output[T]]], Awaitable[Sequence[Union[int, Awaitable[int], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="p">:</span> <span class="n">Union[ServiceLevelObjectiveQueryArgs, Mapping[str, Any], Awaitable[Union[ServiceLevelObjectiveQueryArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">thresholds</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ServiceLevelObjectiveThresholdArgs, Mapping[str, Any], Awaitable[Union[ServiceLevelObjectiveThresholdArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ServiceLevelObjectiveThresholdArgs, Mapping[str, Any], Awaitable[Union[ServiceLevelObjectiveThresholdArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">validate</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.service_level_objective.ServiceLevelObjective<a class="headerlink" href="#pulumi_datadog.ServiceLevelObjective.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceLevelObjective resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of this service level objective.</p></li>
<li><p><strong>force_delete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether this monitor can be deleted even if it’s referenced by other resources (e.g. dashboards).</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>-   `thresholds`: (Required) - A list of thresholds and targets that define the service level objectives from the provided SLIs.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A static set of groups to filter monitor-based SLOs</p></li>
<li><p><strong>monitor_ids</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>int</em><em>]</em><em>]</em><em>]</em>) – A static set of monitor IDs to use as part of the SLO</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Datadog service level objective</p></li>
<li><p><strong>query</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceLevelObjectiveQueryArgs'</em><em>]</em><em>]</em>) – The metric query of good / total events</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of tags to associate with your service level objective. This can help you categorize and filter service level objectives in the service level objectives page of the UI. Note: it’s not currently possible to filter by these tags when querying via the API</p></li>
<li><p><strong>thresholds</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceLevelObjectiveThresholdArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A list of thresholds and targets that define the service level objectives from the provided SLIs.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The type of the service level objective. The mapping from these types to the types found in the Datadog Web UI can be
found in the Datadog API <a class="reference external" href="https://docs.datadoghq.com/api/v1/service-level-objectives/#create-a-slo-object">documentation
page</a>. Available options to choose from
are: <code class="docutils literal notranslate"><span class="pre">metric</span></code> and <code class="docutils literal notranslate"><span class="pre">monitor</span></code>.</p>
</p></li>
<li><p><strong>validate</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not to validate the SLO.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.ServiceLevelObjective.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_datadog.ServiceLevelObjective.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of this service level objective.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.ServiceLevelObjective.force_delete">
<em class="property">property </em><code class="sig-name descname">force_delete</code><a class="headerlink" href="#pulumi_datadog.ServiceLevelObjective.force_delete" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean indicating whether this monitor can be deleted even if it’s referenced by other resources (e.g. dashboards).</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">thresholds</span></code>: (Required) - A list of thresholds and targets that define the service level objectives from the provided SLIs.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.ServiceLevelObjective.groups">
<em class="property">property </em><code class="sig-name descname">groups</code><a class="headerlink" href="#pulumi_datadog.ServiceLevelObjective.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>A static set of groups to filter monitor-based SLOs</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.ServiceLevelObjective.monitor_ids">
<em class="property">property </em><code class="sig-name descname">monitor_ids</code><a class="headerlink" href="#pulumi_datadog.ServiceLevelObjective.monitor_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A static set of monitor IDs to use as part of the SLO</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.ServiceLevelObjective.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_datadog.ServiceLevelObjective.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of Datadog service level objective</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.ServiceLevelObjective.query">
<em class="property">property </em><code class="sig-name descname">query</code><a class="headerlink" href="#pulumi_datadog.ServiceLevelObjective.query" title="Permalink to this definition">¶</a></dt>
<dd><p>The metric query of good / total events</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.ServiceLevelObjective.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_datadog.ServiceLevelObjective.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tags to associate with your service level objective. This can help you categorize and filter service level objectives in the service level objectives page of the UI. Note: it’s not currently possible to filter by these tags when querying via the API</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.ServiceLevelObjective.thresholds">
<em class="property">property </em><code class="sig-name descname">thresholds</code><a class="headerlink" href="#pulumi_datadog.ServiceLevelObjective.thresholds" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of thresholds and targets that define the service level objectives from the provided SLIs.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.ServiceLevelObjective.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_datadog.ServiceLevelObjective.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the service level objective. The mapping from these types to the types found in the Datadog Web UI can be
found in the Datadog API <a class="reference external" href="https://docs.datadoghq.com/api/v1/service-level-objectives/#create-a-slo-object">documentation
page</a>. Available options to choose from
are: <code class="docutils literal notranslate"><span class="pre">metric</span></code> and <code class="docutils literal notranslate"><span class="pre">monitor</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.ServiceLevelObjective.validate">
<em class="property">property </em><code class="sig-name descname">validate</code><a class="headerlink" href="#pulumi_datadog.ServiceLevelObjective.validate" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not to validate the SLO.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.ServiceLevelObjective.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.ServiceLevelObjective.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.ServiceLevelObjective.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.ServiceLevelObjective.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.SyntheticsGlobalVariable">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">SyntheticsGlobalVariable</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parse_test_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parse_test_options</span><span class="p">:</span> <span class="n">Union[SyntheticsGlobalVariableParseTestOptionsArgs, Mapping[str, Any], Awaitable[Union[SyntheticsGlobalVariableParseTestOptionsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secure</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.SyntheticsGlobalVariable" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Datadog synthetics global variable resource. This can be used to create and manage Datadog synthetics global variables.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="n">test_variable</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">SyntheticsGlobalVariable</span><span class="p">(</span><span class="s2">&quot;testVariable&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Description of the variable&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;EXAMPLE_VARIABLE&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;foo:bar&quot;</span><span class="p">,</span>
        <span class="s2">&quot;env:test&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">value</span><span class="o">=</span><span class="s2">&quot;variable-value&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Synthetics global variables can be imported using their string ID, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import datadog:index/syntheticsGlobalVariable:SyntheticsGlobalVariable fizz abcde123-fghi-456-jkl-mnopqrstuv
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the global variable.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Synthetics global variable name.</p></li>
<li><p><strong>parse_test_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Id of the Synthetics test to use for a variable from test.</p></li>
<li><p><strong>parse_test_options</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SyntheticsGlobalVariableParseTestOptionsArgs'</em><em>]</em><em>]</em>) – ID of the Synthetics test to use a source of the global variable value.</p></li>
<li><p><strong>secure</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Sets the variable as secure. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of tags to associate with your synthetics global variable.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of the global variable.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_datadog.SyntheticsGlobalVariable.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parse_test_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parse_test_options</span><span class="p">:</span> <span class="n">Union[SyntheticsGlobalVariableParseTestOptionsArgs, Mapping[str, Any], Awaitable[Union[SyntheticsGlobalVariableParseTestOptionsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secure</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.synthetics_global_variable.SyntheticsGlobalVariable<a class="headerlink" href="#pulumi_datadog.SyntheticsGlobalVariable.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SyntheticsGlobalVariable resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the global variable.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Synthetics global variable name.</p></li>
<li><p><strong>parse_test_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Id of the Synthetics test to use for a variable from test.</p></li>
<li><p><strong>parse_test_options</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SyntheticsGlobalVariableParseTestOptionsArgs'</em><em>]</em><em>]</em>) – ID of the Synthetics test to use a source of the global variable value.</p></li>
<li><p><strong>secure</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Sets the variable as secure. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of tags to associate with your synthetics global variable.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of the global variable.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsGlobalVariable.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_datadog.SyntheticsGlobalVariable.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the global variable.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsGlobalVariable.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_datadog.SyntheticsGlobalVariable.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Synthetics global variable name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsGlobalVariable.parse_test_id">
<em class="property">property </em><code class="sig-name descname">parse_test_id</code><a class="headerlink" href="#pulumi_datadog.SyntheticsGlobalVariable.parse_test_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Id of the Synthetics test to use for a variable from test.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsGlobalVariable.parse_test_options">
<em class="property">property </em><code class="sig-name descname">parse_test_options</code><a class="headerlink" href="#pulumi_datadog.SyntheticsGlobalVariable.parse_test_options" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the Synthetics test to use a source of the global variable value.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsGlobalVariable.secure">
<em class="property">property </em><code class="sig-name descname">secure</code><a class="headerlink" href="#pulumi_datadog.SyntheticsGlobalVariable.secure" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets the variable as secure. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsGlobalVariable.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_datadog.SyntheticsGlobalVariable.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tags to associate with your synthetics global variable.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsGlobalVariable.value">
<em class="property">property </em><code class="sig-name descname">value</code><a class="headerlink" href="#pulumi_datadog.SyntheticsGlobalVariable.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the global variable.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsGlobalVariable.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.SyntheticsGlobalVariable.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.SyntheticsGlobalVariable.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.SyntheticsGlobalVariable.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.SyntheticsPrivateLocation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">SyntheticsPrivateLocation</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.SyntheticsPrivateLocation" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Datadog synthetics private location resource. This can be used to create and manage Datadog synthetics private locations.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="n">private_location</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">SyntheticsPrivateLocation</span><span class="p">(</span><span class="s2">&quot;privateLocation&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Description of the private location&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;First private location&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;foo:bar&quot;</span><span class="p">,</span>
        <span class="s2">&quot;env:test&quot;</span><span class="p">,</span>
    <span class="p">])</span>
</pre></div>
</div>
<p>Synthetics private locations can be imported using their string ID, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import datadog:index/syntheticsPrivateLocation:SyntheticsPrivateLocation bar pl:private-location-name-abcdef123456
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the private location.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Synthetics private location name.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of tags to associate with your synthetics private location.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_datadog.SyntheticsPrivateLocation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.synthetics_private_location.SyntheticsPrivateLocation<a class="headerlink" href="#pulumi_datadog.SyntheticsPrivateLocation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SyntheticsPrivateLocation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>config</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Configuration skeleton for the private location. See installation instructions of the private location on how to use
this configuration.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the private location.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Synthetics private location name.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of tags to associate with your synthetics private location.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsPrivateLocation.config">
<em class="property">property </em><code class="sig-name descname">config</code><a class="headerlink" href="#pulumi_datadog.SyntheticsPrivateLocation.config" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration skeleton for the private location. See installation instructions of the private location on how to use
this configuration.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsPrivateLocation.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_datadog.SyntheticsPrivateLocation.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the private location.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsPrivateLocation.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_datadog.SyntheticsPrivateLocation.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Synthetics private location name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsPrivateLocation.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_datadog.SyntheticsPrivateLocation.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tags to associate with your synthetics private location.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsPrivateLocation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.SyntheticsPrivateLocation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.SyntheticsPrivateLocation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.SyntheticsPrivateLocation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.SyntheticsTest">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">SyntheticsTest</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">assertions</span><span class="p">:</span> <span class="n">Union[Sequence[Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T]]], Awaitable[Sequence[Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">browser_variables</span><span class="p">:</span> <span class="n">Union[Sequence[Union[SyntheticsTestBrowserVariableArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestBrowserVariableArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[SyntheticsTestBrowserVariableArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestBrowserVariableArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config_variables</span><span class="p">:</span> <span class="n">Union[Sequence[Union[SyntheticsTestConfigVariableArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestConfigVariableArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[SyntheticsTestConfigVariableArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestConfigVariableArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_ids</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locations</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">options</span><span class="p">:</span> <span class="n">Union[SyntheticsTestOptionsArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestOptionsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">options_list</span><span class="p">:</span> <span class="n">Union[SyntheticsTestOptionsListArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestOptionsListArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request</span><span class="p">:</span> <span class="n">Union[SyntheticsTestRequestArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestRequestArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_basicauth</span><span class="p">:</span> <span class="n">Union[SyntheticsTestRequestBasicauthArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestRequestBasicauthArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_client_certificate</span><span class="p">:</span> <span class="n">Union[SyntheticsTestRequestClientCertificateArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestRequestClientCertificateArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_headers</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_query</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">steps</span><span class="p">:</span> <span class="n">Union[Sequence[Union[SyntheticsTestStepArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestStepArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[SyntheticsTestStepArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestStepArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subtype</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">variables</span><span class="p">:</span> <span class="n">Union[Sequence[Union[SyntheticsTestVariableArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestVariableArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[SyntheticsTestVariableArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestVariableArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.SyntheticsTest" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Datadog synthetics test resource. This can be used to create and manage Datadog synthetics test.</p>
<p>Create a new Datadog Synthetics API/HTTP test on <a class="reference external" href="https://www.example.org">https://www.example.org</a></p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="n">test_api</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">SyntheticsTest</span><span class="p">(</span><span class="s2">&quot;testApi&quot;</span><span class="p">,</span>
    <span class="n">assertions</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;operator&quot;</span><span class="p">:</span> <span class="s2">&quot;is&quot;</span><span class="p">,</span>
        <span class="s2">&quot;target&quot;</span><span class="p">:</span> <span class="s2">&quot;200&quot;</span><span class="p">,</span>
        <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;statusCode&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">locations</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;aws:eu-central-1&quot;</span><span class="p">],</span>
    <span class="n">message</span><span class="o">=</span><span class="s2">&quot;Notify @pagerduty&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;An API test on example.org&quot;</span><span class="p">,</span>
    <span class="n">options_list</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">SyntheticsTestOptionsListArgs</span><span class="p">(</span>
        <span class="n">monitor_options</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">SyntheticsTestOptionsListMonitorOptionsArgs</span><span class="p">(</span>
            <span class="n">renotify_interval</span><span class="o">=</span><span class="mi">100</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">retry</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">SyntheticsTestOptionsListRetryArgs</span><span class="p">(</span>
            <span class="n">count</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
            <span class="n">interval</span><span class="o">=</span><span class="mi">300</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">tick_every</span><span class="o">=</span><span class="mi">900</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">request</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">SyntheticsTestRequestArgs</span><span class="p">(</span>
        <span class="n">method</span><span class="o">=</span><span class="s2">&quot;GET&quot;</span><span class="p">,</span>
        <span class="n">url</span><span class="o">=</span><span class="s2">&quot;https://www.example.org&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">request_headers</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;Authentication&quot;</span><span class="p">:</span> <span class="s2">&quot;Token: 1234566789&quot;</span><span class="p">,</span>
        <span class="s2">&quot;Content-Type&quot;</span><span class="p">:</span> <span class="s2">&quot;application/json&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">status</span><span class="o">=</span><span class="s2">&quot;live&quot;</span><span class="p">,</span>
    <span class="n">subtype</span><span class="o">=</span><span class="s2">&quot;http&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;foo:bar&quot;</span><span class="p">,</span>
        <span class="s2">&quot;foo&quot;</span><span class="p">,</span>
        <span class="s2">&quot;env:test&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;api&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Create a new Datadog Synthetics API/SSL test on example.org</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="n">test_ssl</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">SyntheticsTest</span><span class="p">(</span><span class="s2">&quot;testSsl&quot;</span><span class="p">,</span>
    <span class="n">assertions</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;operator&quot;</span><span class="p">:</span> <span class="s2">&quot;isInMoreThan&quot;</span><span class="p">,</span>
        <span class="s2">&quot;target&quot;</span><span class="p">:</span> <span class="mi">30</span><span class="p">,</span>
        <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;certificate&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">locations</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;aws:eu-central-1&quot;</span><span class="p">],</span>
    <span class="n">message</span><span class="o">=</span><span class="s2">&quot;Notify @pagerduty&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;An API test on example.org&quot;</span><span class="p">,</span>
    <span class="n">options_list</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">SyntheticsTestOptionsListArgs</span><span class="p">(</span>
        <span class="n">accept_self_signed</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">tick_every</span><span class="o">=</span><span class="mi">900</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">request</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">SyntheticsTestRequestArgs</span><span class="p">(</span>
        <span class="n">host</span><span class="o">=</span><span class="s2">&quot;example.org&quot;</span><span class="p">,</span>
        <span class="n">port</span><span class="o">=</span><span class="mi">443</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">status</span><span class="o">=</span><span class="s2">&quot;live&quot;</span><span class="p">,</span>
    <span class="n">subtype</span><span class="o">=</span><span class="s2">&quot;ssl&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;foo:bar&quot;</span><span class="p">,</span>
        <span class="s2">&quot;foo&quot;</span><span class="p">,</span>
        <span class="s2">&quot;env:test&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;api&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Create a new Datadog Synthetics API/TCP test on example.org</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="n">test_tcp</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">SyntheticsTest</span><span class="p">(</span><span class="s2">&quot;testTcp&quot;</span><span class="p">,</span>
    <span class="n">assertions</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;operator&quot;</span><span class="p">:</span> <span class="s2">&quot;lessThan&quot;</span><span class="p">,</span>
        <span class="s2">&quot;target&quot;</span><span class="p">:</span> <span class="mi">2000</span><span class="p">,</span>
        <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;responseTime&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">locations</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;aws:eu-central-1&quot;</span><span class="p">],</span>
    <span class="n">message</span><span class="o">=</span><span class="s2">&quot;Notify @pagerduty&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;An API test on example.org&quot;</span><span class="p">,</span>
    <span class="n">options_list</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">SyntheticsTestOptionsListArgs</span><span class="p">(</span>
        <span class="n">tick_every</span><span class="o">=</span><span class="mi">900</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">request</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">SyntheticsTestRequestArgs</span><span class="p">(</span>
        <span class="n">host</span><span class="o">=</span><span class="s2">&quot;example.org&quot;</span><span class="p">,</span>
        <span class="n">port</span><span class="o">=</span><span class="mi">443</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">status</span><span class="o">=</span><span class="s2">&quot;live&quot;</span><span class="p">,</span>
    <span class="n">subtype</span><span class="o">=</span><span class="s2">&quot;tcp&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;foo:bar&quot;</span><span class="p">,</span>
        <span class="s2">&quot;foo&quot;</span><span class="p">,</span>
        <span class="s2">&quot;env:test&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;api&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Create a new Datadog Synthetics API/DNS test on example.org</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="n">test_dns</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">SyntheticsTest</span><span class="p">(</span><span class="s2">&quot;testDns&quot;</span><span class="p">,</span>
    <span class="n">assertions</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;operator&quot;</span><span class="p">:</span> <span class="s2">&quot;is&quot;</span><span class="p">,</span>
        <span class="s2">&quot;property&quot;</span><span class="p">:</span> <span class="s2">&quot;A&quot;</span><span class="p">,</span>
        <span class="s2">&quot;target&quot;</span><span class="p">:</span> <span class="s2">&quot;0.0.0.0&quot;</span><span class="p">,</span>
        <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;recordSome&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">locations</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;aws:eu-central-1&quot;</span><span class="p">],</span>
    <span class="n">message</span><span class="o">=</span><span class="s2">&quot;Notify @pagerduty&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;An API test on example.org&quot;</span><span class="p">,</span>
    <span class="n">options_list</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">SyntheticsTestOptionsListArgs</span><span class="p">(</span>
        <span class="n">tick_every</span><span class="o">=</span><span class="mi">900</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">request</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">SyntheticsTestRequestArgs</span><span class="p">(</span>
        <span class="n">host</span><span class="o">=</span><span class="s2">&quot;example.org&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">status</span><span class="o">=</span><span class="s2">&quot;live&quot;</span><span class="p">,</span>
    <span class="n">subtype</span><span class="o">=</span><span class="s2">&quot;dns&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;foo:bar&quot;</span><span class="p">,</span>
        <span class="s2">&quot;foo&quot;</span><span class="p">,</span>
        <span class="s2">&quot;env:test&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;api&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Support for Synthetics Browser test steps is limited (see below)</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">json</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="c1"># Create a new Datadog Synthetics Browser test starting on https://www.example.org</span>
<span class="n">test_browser</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">SyntheticsTest</span><span class="p">(</span><span class="s2">&quot;testBrowser&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;browser&quot;</span><span class="p">,</span>
    <span class="n">request</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">SyntheticsTestRequestArgs</span><span class="p">(</span>
        <span class="n">method</span><span class="o">=</span><span class="s2">&quot;GET&quot;</span><span class="p">,</span>
        <span class="n">url</span><span class="o">=</span><span class="s2">&quot;https://app.datadoghq.com&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">device_ids</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;laptop_large&quot;</span><span class="p">],</span>
    <span class="n">locations</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;aws:eu-central-1&quot;</span><span class="p">],</span>
    <span class="n">options_list</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">SyntheticsTestOptionsListArgs</span><span class="p">(</span>
        <span class="n">tick_every</span><span class="o">=</span><span class="mi">3600</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;A Browser test on example.org&quot;</span><span class="p">,</span>
    <span class="n">message</span><span class="o">=</span><span class="s2">&quot;Notify @qa&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[],</span>
    <span class="n">status</span><span class="o">=</span><span class="s2">&quot;paused&quot;</span><span class="p">,</span>
    <span class="n">steps</span><span class="o">=</span><span class="p">[</span><span class="n">datadog</span><span class="o">.</span><span class="n">SyntheticsTestStepArgs</span><span class="p">(</span>
        <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Check current url&quot;</span><span class="p">,</span>
        <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;assertCurrentUrl&quot;</span><span class="p">,</span>
        <span class="n">params</span><span class="o">=</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">({</span>
            <span class="s2">&quot;check&quot;</span><span class="p">:</span> <span class="s2">&quot;contains&quot;</span><span class="p">,</span>
            <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;datadoghq&quot;</span><span class="p">,</span>
        <span class="p">}),</span>
    <span class="p">)],</span>
    <span class="n">browser_variables</span><span class="o">=</span><span class="p">[</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">SyntheticsTestBrowserVariableArgs</span><span class="p">(</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;text&quot;</span><span class="p">,</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">&quot;MY_PATTERN_VAR&quot;</span><span class="p">,</span>
            <span class="n">pattern</span><span class="o">=</span><span class="s2">&quot;{{numeric(3)}}&quot;</span><span class="p">,</span>
            <span class="n">example</span><span class="o">=</span><span class="s2">&quot;597&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">SyntheticsTestBrowserVariableArgs</span><span class="p">(</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;email&quot;</span><span class="p">,</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">&quot;MY_EMAIL_VAR&quot;</span><span class="p">,</span>
            <span class="n">pattern</span><span class="o">=</span><span class="s2">&quot;jd8-afe-ydv.{{ numeric(10) }}@synthetics.dtdg.co&quot;</span><span class="p">,</span>
            <span class="n">example</span><span class="o">=</span><span class="s2">&quot;jd8-afe-ydv.4546132139@synthetics.dtdg.co&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">SyntheticsTestBrowserVariableArgs</span><span class="p">(</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;global&quot;</span><span class="p">,</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">&quot;MY_GLOBAL_VAR&quot;</span><span class="p">,</span>
            <span class="nb">id</span><span class="o">=</span><span class="s2">&quot;76636cd1-82e2-4aeb-9cfe-51366a8198a2&quot;</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">])</span>
</pre></div>
</div>
<p>Support for Synthetics Browser test is limited when creating steps. Some steps types (like steps involving elements) cannot be created, but they can be imported.</p>
<p>The resource was changed to have assertions be a list of <code class="docutils literal notranslate"><span class="pre">assertion</span></code> blocks instead of single <code class="docutils literal notranslate"><span class="pre">assertions</span></code> array, to support the JSON path operations. We’ll remove <code class="docutils literal notranslate"><span class="pre">assertions</span></code> support in the future: to migrate, rename your attribute to <code class="docutils literal notranslate"><span class="pre">assertion</span></code> and turn array elements into independent blocks. For example:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="n">test_api</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">SyntheticsTest</span><span class="p">(</span><span class="s2">&quot;testApi&quot;</span><span class="p">,</span> <span class="n">assertions</span><span class="o">=</span><span class="p">[</span>
    <span class="p">{</span>
        <span class="s2">&quot;operator&quot;</span><span class="p">:</span> <span class="s2">&quot;is&quot;</span><span class="p">,</span>
        <span class="s2">&quot;target&quot;</span><span class="p">:</span> <span class="s2">&quot;200&quot;</span><span class="p">,</span>
        <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;statusCode&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="p">{</span>
        <span class="s2">&quot;operator&quot;</span><span class="p">:</span> <span class="s2">&quot;lessThan&quot;</span><span class="p">,</span>
        <span class="s2">&quot;target&quot;</span><span class="p">:</span> <span class="s2">&quot;1000&quot;</span><span class="p">,</span>
        <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;responseTime&quot;</span><span class="p">,</span>
    <span class="p">},</span>
<span class="p">])</span>
</pre></div>
</div>
<p>turns into:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="n">test_api</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">SyntheticsTest</span><span class="p">(</span><span class="s2">&quot;testApi&quot;</span><span class="p">,</span> <span class="n">assertions</span><span class="o">=</span><span class="p">[</span>
    <span class="p">{</span>
        <span class="s2">&quot;operator&quot;</span><span class="p">:</span> <span class="s2">&quot;is&quot;</span><span class="p">,</span>
        <span class="s2">&quot;target&quot;</span><span class="p">:</span> <span class="s2">&quot;200&quot;</span><span class="p">,</span>
        <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;statusCode&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="p">{</span>
        <span class="s2">&quot;operator&quot;</span><span class="p">:</span> <span class="s2">&quot;lessThan&quot;</span><span class="p">,</span>
        <span class="s2">&quot;target&quot;</span><span class="p">:</span> <span class="s2">&quot;1000&quot;</span><span class="p">,</span>
        <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;responseTime&quot;</span><span class="p">,</span>
    <span class="p">},</span>
<span class="p">])</span>
</pre></div>
</div>
<p>Synthetics tests can be imported using their public string ID, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import datadog:index/syntheticsTest:SyntheticsTest fizz abc-123-xyz
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>assertions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – List of assertions.</p></li>
<li><p><strong>browser_variables</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SyntheticsTestBrowserVariableArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Variables used for a browser test steps. Multiple <code class="docutils literal notranslate"><span class="pre">variable</span></code> blocks are allowed with the structure below.</p></li>
<li><p><strong>config_variables</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SyntheticsTestConfigVariableArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Variables used for the test configuration. Multiple <code class="docutils literal notranslate"><span class="pre">config_variable</span></code> blocks are allowed with the structure below.</p></li>
<li><p><strong>device_ids</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Array with the different device IDs used to run the test. Allowed enum values: <code class="docutils literal notranslate"><span class="pre">laptop_large</span></code>, <code class="docutils literal notranslate"><span class="pre">tablet</span></code>, <code class="docutils literal notranslate"><span class="pre">mobile_small</span></code>
(only available for <code class="docutils literal notranslate"><span class="pre">browser</span></code> tests).</p></li>
<li><p><strong>locations</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Array of locations used to run the test. Refer to <a class="reference external" href="https://docs.datadoghq.com/synthetics/api_test/#request">Datadog
documentation</a> for available locations (e.g.
<code class="docutils literal notranslate"><span class="pre">aws:eu-central-1</span></code>).</p></li>
<li><p><strong>message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A message to include with notifications for this synthetics test. Email notifications can be sent to specific users by
using the same <code class="docutils literal notranslate"><span class="pre">&#64;username</span></code> notation as events.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Datadog synthetics test.</p></li>
<li><p><strong>request</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SyntheticsTestRequestArgs'</em><em>]</em><em>]</em>) – The synthetics test request. Required if <code class="docutils literal notranslate"><span class="pre">type</span> <span class="pre">=</span> <span class="pre">&quot;api&quot;</span></code> and <code class="docutils literal notranslate"><span class="pre">subtype</span> <span class="pre">=</span> <span class="pre">&quot;http&quot;</span></code>.</p></li>
<li><p><strong>request_basicauth</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SyntheticsTestRequestBasicauthArgs'</em><em>]</em><em>]</em>) – The HTTP basic authentication credentials. Exactly one nested block is allowed with the structure below.</p></li>
<li><p><strong>request_client_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SyntheticsTestRequestClientCertificateArgs'</em><em>]</em><em>]</em>) – Client certificate to use when performing the test request. Exactly one nested block is allowed with the structure
below.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>request_headers</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Header name and value map.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>request_query</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Query arguments name and value map.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Define whether you want to start (<code class="docutils literal notranslate"><span class="pre">live</span></code>) or pause (<code class="docutils literal notranslate"><span class="pre">paused</span></code>) a Synthetic test. Allowed enum values: <code class="docutils literal notranslate"><span class="pre">live</span></code>, <code class="docutils literal notranslate"><span class="pre">paused</span></code></p></li>
<li><p><strong>steps</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SyntheticsTestStepArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Steps for browser tests.</p></li>
<li><p><strong>subtype</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">api</span></code>, choose from <code class="docutils literal notranslate"><span class="pre">http</span></code>, <code class="docutils literal notranslate"><span class="pre">ssl</span></code>, <code class="docutils literal notranslate"><span class="pre">tcp</span></code> or <code class="docutils literal notranslate"><span class="pre">dns</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">http</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of tags to associate with your synthetics test. This can help you categorize and filter tests in the manage
synthetics page of the UI. Default is an empty list (<code class="docutils literal notranslate"><span class="pre">[]</span></code>).</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Synthetics test type (<code class="docutils literal notranslate"><span class="pre">api</span></code> or <code class="docutils literal notranslate"><span class="pre">browser</span></code>).</p></li>
<li><p><strong>variables</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SyntheticsTestVariableArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Variables used for a browser test steps. Multiple <code class="docutils literal notranslate"><span class="pre">browser_variable</span></code> blocks are allowed with the structure below.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_datadog.SyntheticsTest.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">assertions</span><span class="p">:</span> <span class="n">Union[Sequence[Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T]]], Awaitable[Sequence[Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">browser_variables</span><span class="p">:</span> <span class="n">Union[Sequence[Union[SyntheticsTestBrowserVariableArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestBrowserVariableArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[SyntheticsTestBrowserVariableArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestBrowserVariableArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">config_variables</span><span class="p">:</span> <span class="n">Union[Sequence[Union[SyntheticsTestConfigVariableArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestConfigVariableArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[SyntheticsTestConfigVariableArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestConfigVariableArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_ids</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locations</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitor_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">options</span><span class="p">:</span> <span class="n">Union[SyntheticsTestOptionsArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestOptionsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">options_list</span><span class="p">:</span> <span class="n">Union[SyntheticsTestOptionsListArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestOptionsListArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request</span><span class="p">:</span> <span class="n">Union[SyntheticsTestRequestArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestRequestArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_basicauth</span><span class="p">:</span> <span class="n">Union[SyntheticsTestRequestBasicauthArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestRequestBasicauthArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_client_certificate</span><span class="p">:</span> <span class="n">Union[SyntheticsTestRequestClientCertificateArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestRequestClientCertificateArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_headers</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_query</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">steps</span><span class="p">:</span> <span class="n">Union[Sequence[Union[SyntheticsTestStepArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestStepArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[SyntheticsTestStepArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestStepArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subtype</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">variables</span><span class="p">:</span> <span class="n">Union[Sequence[Union[SyntheticsTestVariableArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestVariableArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[SyntheticsTestVariableArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestVariableArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.synthetics_test.SyntheticsTest<a class="headerlink" href="#pulumi_datadog.SyntheticsTest.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SyntheticsTest resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>assertions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – List of assertions.</p></li>
<li><p><strong>browser_variables</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SyntheticsTestBrowserVariableArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Variables used for a browser test steps. Multiple <code class="docutils literal notranslate"><span class="pre">variable</span></code> blocks are allowed with the structure below.</p></li>
<li><p><strong>config_variables</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SyntheticsTestConfigVariableArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Variables used for the test configuration. Multiple <code class="docutils literal notranslate"><span class="pre">config_variable</span></code> blocks are allowed with the structure below.</p></li>
<li><p><strong>device_ids</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Array with the different device IDs used to run the test. Allowed enum values: <code class="docutils literal notranslate"><span class="pre">laptop_large</span></code>, <code class="docutils literal notranslate"><span class="pre">tablet</span></code>, <code class="docutils literal notranslate"><span class="pre">mobile_small</span></code>
(only available for <code class="docutils literal notranslate"><span class="pre">browser</span></code> tests).</p></li>
<li><p><strong>locations</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – <p>Array of locations used to run the test. Refer to <a class="reference external" href="https://docs.datadoghq.com/synthetics/api_test/#request">Datadog
documentation</a> for available locations (e.g.
<code class="docutils literal notranslate"><span class="pre">aws:eu-central-1</span></code>).</p>
</p></li>
<li><p><strong>message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A message to include with notifications for this synthetics test. Email notifications can be sent to specific users by
using the same <code class="docutils literal notranslate"><span class="pre">&#64;username</span></code> notation as events.</p></li>
<li><p><strong>monitor_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – ID of the monitor associated with the Datadog synthetics test.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Datadog synthetics test.</p></li>
<li><p><strong>request</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SyntheticsTestRequestArgs'</em><em>]</em><em>]</em>) – The synthetics test request. Required if <code class="docutils literal notranslate"><span class="pre">type</span> <span class="pre">=</span> <span class="pre">&quot;api&quot;</span></code> and <code class="docutils literal notranslate"><span class="pre">subtype</span> <span class="pre">=</span> <span class="pre">&quot;http&quot;</span></code>.</p></li>
<li><p><strong>request_basicauth</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SyntheticsTestRequestBasicauthArgs'</em><em>]</em><em>]</em>) – The HTTP basic authentication credentials. Exactly one nested block is allowed with the structure below.</p></li>
<li><p><strong>request_client_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SyntheticsTestRequestClientCertificateArgs'</em><em>]</em><em>]</em>) – Client certificate to use when performing the test request. Exactly one nested block is allowed with the structure
below.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>request_headers</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Header name and value map.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>request_query</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Query arguments name and value map.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Define whether you want to start (<code class="docutils literal notranslate"><span class="pre">live</span></code>) or pause (<code class="docutils literal notranslate"><span class="pre">paused</span></code>) a Synthetic test. Allowed enum values: <code class="docutils literal notranslate"><span class="pre">live</span></code>, <code class="docutils literal notranslate"><span class="pre">paused</span></code></p></li>
<li><p><strong>steps</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SyntheticsTestStepArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Steps for browser tests.</p></li>
<li><p><strong>subtype</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">api</span></code>, choose from <code class="docutils literal notranslate"><span class="pre">http</span></code>, <code class="docutils literal notranslate"><span class="pre">ssl</span></code>, <code class="docutils literal notranslate"><span class="pre">tcp</span></code> or <code class="docutils literal notranslate"><span class="pre">dns</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">http</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of tags to associate with your synthetics test. This can help you categorize and filter tests in the manage
synthetics page of the UI. Default is an empty list (<code class="docutils literal notranslate"><span class="pre">[]</span></code>).</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Synthetics test type (<code class="docutils literal notranslate"><span class="pre">api</span></code> or <code class="docutils literal notranslate"><span class="pre">browser</span></code>).</p></li>
<li><p><strong>variables</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SyntheticsTestVariableArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Variables used for a browser test steps. Multiple <code class="docutils literal notranslate"><span class="pre">browser_variable</span></code> blocks are allowed with the structure below.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsTest.assertions">
<em class="property">property </em><code class="sig-name descname">assertions</code><a class="headerlink" href="#pulumi_datadog.SyntheticsTest.assertions" title="Permalink to this definition">¶</a></dt>
<dd><p>List of assertions.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsTest.browser_variables">
<em class="property">property </em><code class="sig-name descname">browser_variables</code><a class="headerlink" href="#pulumi_datadog.SyntheticsTest.browser_variables" title="Permalink to this definition">¶</a></dt>
<dd><p>Variables used for a browser test steps. Multiple <code class="docutils literal notranslate"><span class="pre">variable</span></code> blocks are allowed with the structure below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsTest.config_variables">
<em class="property">property </em><code class="sig-name descname">config_variables</code><a class="headerlink" href="#pulumi_datadog.SyntheticsTest.config_variables" title="Permalink to this definition">¶</a></dt>
<dd><p>Variables used for the test configuration. Multiple <code class="docutils literal notranslate"><span class="pre">config_variable</span></code> blocks are allowed with the structure below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsTest.device_ids">
<em class="property">property </em><code class="sig-name descname">device_ids</code><a class="headerlink" href="#pulumi_datadog.SyntheticsTest.device_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>Array with the different device IDs used to run the test. Allowed enum values: <code class="docutils literal notranslate"><span class="pre">laptop_large</span></code>, <code class="docutils literal notranslate"><span class="pre">tablet</span></code>, <code class="docutils literal notranslate"><span class="pre">mobile_small</span></code>
(only available for <code class="docutils literal notranslate"><span class="pre">browser</span></code> tests).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsTest.locations">
<em class="property">property </em><code class="sig-name descname">locations</code><a class="headerlink" href="#pulumi_datadog.SyntheticsTest.locations" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of locations used to run the test. Refer to <a class="reference external" href="https://docs.datadoghq.com/synthetics/api_test/#request">Datadog
documentation</a> for available locations (e.g.
<code class="docutils literal notranslate"><span class="pre">aws:eu-central-1</span></code>).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsTest.message">
<em class="property">property </em><code class="sig-name descname">message</code><a class="headerlink" href="#pulumi_datadog.SyntheticsTest.message" title="Permalink to this definition">¶</a></dt>
<dd><p>A message to include with notifications for this synthetics test. Email notifications can be sent to specific users by
using the same <code class="docutils literal notranslate"><span class="pre">&#64;username</span></code> notation as events.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsTest.monitor_id">
<em class="property">property </em><code class="sig-name descname">monitor_id</code><a class="headerlink" href="#pulumi_datadog.SyntheticsTest.monitor_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the monitor associated with the Datadog synthetics test.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsTest.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_datadog.SyntheticsTest.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of Datadog synthetics test.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsTest.request">
<em class="property">property </em><code class="sig-name descname">request</code><a class="headerlink" href="#pulumi_datadog.SyntheticsTest.request" title="Permalink to this definition">¶</a></dt>
<dd><p>The synthetics test request. Required if <code class="docutils literal notranslate"><span class="pre">type</span> <span class="pre">=</span> <span class="pre">&quot;api&quot;</span></code> and <code class="docutils literal notranslate"><span class="pre">subtype</span> <span class="pre">=</span> <span class="pre">&quot;http&quot;</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsTest.request_basicauth">
<em class="property">property </em><code class="sig-name descname">request_basicauth</code><a class="headerlink" href="#pulumi_datadog.SyntheticsTest.request_basicauth" title="Permalink to this definition">¶</a></dt>
<dd><p>The HTTP basic authentication credentials. Exactly one nested block is allowed with the structure below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsTest.request_client_certificate">
<em class="property">property </em><code class="sig-name descname">request_client_certificate</code><a class="headerlink" href="#pulumi_datadog.SyntheticsTest.request_client_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Client certificate to use when performing the test request. Exactly one nested block is allowed with the structure
below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsTest.request_headers">
<em class="property">property </em><code class="sig-name descname">request_headers</code><a class="headerlink" href="#pulumi_datadog.SyntheticsTest.request_headers" title="Permalink to this definition">¶</a></dt>
<dd><p>Header name and value map.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsTest.request_query">
<em class="property">property </em><code class="sig-name descname">request_query</code><a class="headerlink" href="#pulumi_datadog.SyntheticsTest.request_query" title="Permalink to this definition">¶</a></dt>
<dd><p>Query arguments name and value map.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsTest.status">
<em class="property">property </em><code class="sig-name descname">status</code><a class="headerlink" href="#pulumi_datadog.SyntheticsTest.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Define whether you want to start (<code class="docutils literal notranslate"><span class="pre">live</span></code>) or pause (<code class="docutils literal notranslate"><span class="pre">paused</span></code>) a Synthetic test. Allowed enum values: <code class="docutils literal notranslate"><span class="pre">live</span></code>, <code class="docutils literal notranslate"><span class="pre">paused</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsTest.steps">
<em class="property">property </em><code class="sig-name descname">steps</code><a class="headerlink" href="#pulumi_datadog.SyntheticsTest.steps" title="Permalink to this definition">¶</a></dt>
<dd><p>Steps for browser tests.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsTest.subtype">
<em class="property">property </em><code class="sig-name descname">subtype</code><a class="headerlink" href="#pulumi_datadog.SyntheticsTest.subtype" title="Permalink to this definition">¶</a></dt>
<dd><p>When <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">api</span></code>, choose from <code class="docutils literal notranslate"><span class="pre">http</span></code>, <code class="docutils literal notranslate"><span class="pre">ssl</span></code>, <code class="docutils literal notranslate"><span class="pre">tcp</span></code> or <code class="docutils literal notranslate"><span class="pre">dns</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">http</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsTest.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_datadog.SyntheticsTest.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tags to associate with your synthetics test. This can help you categorize and filter tests in the manage
synthetics page of the UI. Default is an empty list (<code class="docutils literal notranslate"><span class="pre">[]</span></code>).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsTest.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_datadog.SyntheticsTest.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Synthetics test type (<code class="docutils literal notranslate"><span class="pre">api</span></code> or <code class="docutils literal notranslate"><span class="pre">browser</span></code>).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsTest.variables">
<em class="property">property </em><code class="sig-name descname">variables</code><a class="headerlink" href="#pulumi_datadog.SyntheticsTest.variables" title="Permalink to this definition">¶</a></dt>
<dd><p>Variables used for a browser test steps. Multiple <code class="docutils literal notranslate"><span class="pre">browser_variable</span></code> blocks are allowed with the structure below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsTest.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.SyntheticsTest.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.SyntheticsTest.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.SyntheticsTest.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.TimeBoard">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">TimeBoard</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">graphs</span><span class="p">:</span> <span class="n">Union[Sequence[Union[TimeBoardGraphArgs, Mapping[str, Any], Awaitable[Union[TimeBoardGraphArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[TimeBoardGraphArgs, Mapping[str, Any], Awaitable[Union[TimeBoardGraphArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">read_only</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_variables</span><span class="p">:</span> <span class="n">Union[Sequence[Union[TimeBoardTemplateVariableArgs, Mapping[str, Any], Awaitable[Union[TimeBoardTemplateVariableArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[TimeBoardTemplateVariableArgs, Mapping[str, Any], Awaitable[Union[TimeBoardTemplateVariableArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">title</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.TimeBoard" title="Permalink to this definition">¶</a></dt>
<dd><p>Timeboards can be imported using their numeric ID, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import datadog:index/timeBoard:TimeBoard my_service_timeboard <span class="m">2081</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the dashboard’s content.</p></li>
<li><p><strong>graphs</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TimeBoardGraphArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A list of graph definitions.</p></li>
<li><p><strong>read_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The read-only status of the timeboard. Default is false.</p></li>
<li><p><strong>template_variables</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TimeBoardTemplateVariableArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A list of template variables for using Dashboard templating.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the dashboard.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_datadog.TimeBoard.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">graphs</span><span class="p">:</span> <span class="n">Union[Sequence[Union[TimeBoardGraphArgs, Mapping[str, Any], Awaitable[Union[TimeBoardGraphArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[TimeBoardGraphArgs, Mapping[str, Any], Awaitable[Union[TimeBoardGraphArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">read_only</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_variables</span><span class="p">:</span> <span class="n">Union[Sequence[Union[TimeBoardTemplateVariableArgs, Mapping[str, Any], Awaitable[Union[TimeBoardTemplateVariableArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[TimeBoardTemplateVariableArgs, Mapping[str, Any], Awaitable[Union[TimeBoardTemplateVariableArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">title</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.time_board.TimeBoard<a class="headerlink" href="#pulumi_datadog.TimeBoard.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TimeBoard resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the dashboard’s content.</p></li>
<li><p><strong>graphs</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TimeBoardGraphArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A list of graph definitions.</p></li>
<li><p><strong>read_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The read-only status of the timeboard. Default is false.</p></li>
<li><p><strong>template_variables</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TimeBoardTemplateVariableArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A list of template variables for using Dashboard templating.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the dashboard.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.TimeBoard.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_datadog.TimeBoard.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the dashboard’s content.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.TimeBoard.graphs">
<em class="property">property </em><code class="sig-name descname">graphs</code><a class="headerlink" href="#pulumi_datadog.TimeBoard.graphs" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of graph definitions.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.TimeBoard.read_only">
<em class="property">property </em><code class="sig-name descname">read_only</code><a class="headerlink" href="#pulumi_datadog.TimeBoard.read_only" title="Permalink to this definition">¶</a></dt>
<dd><p>The read-only status of the timeboard. Default is false.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.TimeBoard.template_variables">
<em class="property">property </em><code class="sig-name descname">template_variables</code><a class="headerlink" href="#pulumi_datadog.TimeBoard.template_variables" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of template variables for using Dashboard templating.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.TimeBoard.title">
<em class="property">property </em><code class="sig-name descname">title</code><a class="headerlink" href="#pulumi_datadog.TimeBoard.title" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the dashboard.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.TimeBoard.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.TimeBoard.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.TimeBoard.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.TimeBoard.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.User">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">User</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_role</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">handle</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_admin</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">roles</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">send_user_invitation</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.User" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Datadog user resource. This can be used to create and manage Datadog users.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="n">ro_role</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">get_role</span><span class="p">(</span><span class="nb">filter</span><span class="o">=</span><span class="s2">&quot;Datadog Read Only Role&quot;</span><span class="p">)</span>
<span class="c1"># Create a new Datadog user</span>
<span class="n">foo</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">email</span><span class="o">=</span><span class="s2">&quot;new@example.com&quot;</span><span class="p">,</span>
    <span class="n">roles</span><span class="o">=</span><span class="p">[</span><span class="n">ro_role</span><span class="o">.</span><span class="n">id</span><span class="p">])</span>
</pre></div>
</div>
<ul class="simple">
<li><p><strong>email</strong> (String) Email address for user.</p></li>
</ul>
<ul class="simple">
<li><p><strong>access_role</strong> (String, Deprecated) Role description for user. Can be <code class="docutils literal notranslate"><span class="pre">st</span></code> (standard user), <code class="docutils literal notranslate"><span class="pre">adm</span></code> (admin user) or <code class="docutils literal notranslate"><span class="pre">ro</span></code> (read-only user). Default is <code class="docutils literal notranslate"><span class="pre">st</span></code>. <code class="docutils literal notranslate"><span class="pre">access_role</span></code> is ignored for new users created with this resource. New users have to use the <code class="docutils literal notranslate"><span class="pre">roles</span></code> attribute.</p></li>
<li><p><strong>disabled</strong> (Boolean) Whether the user is disabled.</p></li>
<li><p><strong>handle</strong> (String, Deprecated) The user handle, must be a valid email.</p></li>
<li><p><strong>id</strong> (String) The ID of this resource.</p></li>
<li><p><strong>is_admin</strong> (Boolean, Deprecated) Whether the user is an administrator. Warning: the corresponding query parameter is ignored by the Datadog API, thus the argument would always trigger an execution plan.</p></li>
<li><p><strong>name</strong> (String) Name for user.</p></li>
<li><p><strong>role</strong> (String, Deprecated) Role description for user. Warning: the corresponding query parameter is ignored by the Datadog API, thus the argument would always trigger an execution plan.</p></li>
<li><p><strong>roles</strong> (Set of String) A list a role IDs to assign to the user.</p></li>
<li><p><strong>send_user_invitation</strong> (Boolean) Whether an invitation email should be sent when the user is created.</p></li>
</ul>
<ul class="simple">
<li><p><strong>user_invitation_id</strong> (String) The ID of the user invitation that was sent when creating the user.</p></li>
<li><p><strong>verified</strong> (Boolean) Returns true if Datadog user is verified.</p></li>
</ul>
<p>Import is supported using the following syntax</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import datadog:index/user:User example_user 6f1b44c0-30b2-11eb-86bc-279f7c1ebaa4
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Role description for user. Can be <code class="docutils literal notranslate"><span class="pre">st</span></code> (standard user), <code class="docutils literal notranslate"><span class="pre">adm</span></code> (admin user) or <code class="docutils literal notranslate"><span class="pre">ro</span></code> (read-only user). Default is <code class="docutils literal notranslate"><span class="pre">st</span></code>.
<code class="docutils literal notranslate"><span class="pre">access_role</span></code> is ignored for new users created with this resource. New users have to use the <code class="docutils literal notranslate"><span class="pre">roles</span></code> attribute.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user is disabled.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Email address for user.</p></li>
<li><p><strong>handle</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user handle, must be a valid email.</p></li>
<li><p><strong>is_admin</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user is an administrator. Warning: the corresponding query parameter is ignored by the Datadog API, thus the
argument would always trigger an execution plan.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name for user.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Role description for user. Warning: the corresponding query parameter is ignored by the Datadog API, thus the argument
would always trigger an execution plan.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list a role IDs to assign to the user.</p></li>
<li><p><strong>send_user_invitation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether an invitation email should be sent when the user is created.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_datadog.User.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_role</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">handle</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_admin</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">roles</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">send_user_invitation</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_invitation_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">verified</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.user.User<a class="headerlink" href="#pulumi_datadog.User.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing User resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Role description for user. Can be <code class="docutils literal notranslate"><span class="pre">st</span></code> (standard user), <code class="docutils literal notranslate"><span class="pre">adm</span></code> (admin user) or <code class="docutils literal notranslate"><span class="pre">ro</span></code> (read-only user). Default is <code class="docutils literal notranslate"><span class="pre">st</span></code>.
<code class="docutils literal notranslate"><span class="pre">access_role</span></code> is ignored for new users created with this resource. New users have to use the <code class="docutils literal notranslate"><span class="pre">roles</span></code> attribute.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user is disabled.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Email address for user.</p></li>
<li><p><strong>handle</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user handle, must be a valid email.</p></li>
<li><p><strong>is_admin</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user is an administrator. Warning: the corresponding query parameter is ignored by the Datadog API, thus the
argument would always trigger an execution plan.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name for user.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Role description for user. Warning: the corresponding query parameter is ignored by the Datadog API, thus the argument
would always trigger an execution plan.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list a role IDs to assign to the user.</p></li>
<li><p><strong>send_user_invitation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether an invitation email should be sent when the user is created.</p></li>
<li><p><strong>user_invitation_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the user invitation that was sent when creating the user.</p></li>
<li><p><strong>verified</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Returns true if Datadog user is verified.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.User.access_role">
<em class="property">property </em><code class="sig-name descname">access_role</code><a class="headerlink" href="#pulumi_datadog.User.access_role" title="Permalink to this definition">¶</a></dt>
<dd><p>Role description for user. Can be <code class="docutils literal notranslate"><span class="pre">st</span></code> (standard user), <code class="docutils literal notranslate"><span class="pre">adm</span></code> (admin user) or <code class="docutils literal notranslate"><span class="pre">ro</span></code> (read-only user). Default is <code class="docutils literal notranslate"><span class="pre">st</span></code>.
<code class="docutils literal notranslate"><span class="pre">access_role</span></code> is ignored for new users created with this resource. New users have to use the <code class="docutils literal notranslate"><span class="pre">roles</span></code> attribute.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.User.disabled">
<em class="property">property </em><code class="sig-name descname">disabled</code><a class="headerlink" href="#pulumi_datadog.User.disabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user is disabled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.User.email">
<em class="property">property </em><code class="sig-name descname">email</code><a class="headerlink" href="#pulumi_datadog.User.email" title="Permalink to this definition">¶</a></dt>
<dd><p>Email address for user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.User.handle">
<em class="property">property </em><code class="sig-name descname">handle</code><a class="headerlink" href="#pulumi_datadog.User.handle" title="Permalink to this definition">¶</a></dt>
<dd><p>The user handle, must be a valid email.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.User.is_admin">
<em class="property">property </em><code class="sig-name descname">is_admin</code><a class="headerlink" href="#pulumi_datadog.User.is_admin" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user is an administrator. Warning: the corresponding query parameter is ignored by the Datadog API, thus the
argument would always trigger an execution plan.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.User.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_datadog.User.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name for user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.User.role">
<em class="property">property </em><code class="sig-name descname">role</code><a class="headerlink" href="#pulumi_datadog.User.role" title="Permalink to this definition">¶</a></dt>
<dd><p>Role description for user. Warning: the corresponding query parameter is ignored by the Datadog API, thus the argument
would always trigger an execution plan.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.User.roles">
<em class="property">property </em><code class="sig-name descname">roles</code><a class="headerlink" href="#pulumi_datadog.User.roles" title="Permalink to this definition">¶</a></dt>
<dd><p>A list a role IDs to assign to the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.User.send_user_invitation">
<em class="property">property </em><code class="sig-name descname">send_user_invitation</code><a class="headerlink" href="#pulumi_datadog.User.send_user_invitation" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether an invitation email should be sent when the user is created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.User.user_invitation_id">
<em class="property">property </em><code class="sig-name descname">user_invitation_id</code><a class="headerlink" href="#pulumi_datadog.User.user_invitation_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the user invitation that was sent when creating the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.User.verified">
<em class="property">property </em><code class="sig-name descname">verified</code><a class="headerlink" href="#pulumi_datadog.User.verified" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns true if Datadog user is verified.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.User.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.User.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.User.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.User.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.get_dashboard">
<code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">get_dashboard</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.get_dashboard.AwaitableGetDashboardResult<a class="headerlink" href="#pulumi_datadog.get_dashboard" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve information about an existing dashboard, for use in other resources. In particular, it can be used in a monitor message to link to a specific dashboard.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">get_dashboard</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;My super dashboard&quot;</span><span class="p">)</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_datadog.get_dashboard_list">
<code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">get_dashboard_list</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.get_dashboard_list.AwaitableGetDashboardListResult<a class="headerlink" href="#pulumi_datadog.get_dashboard_list" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve information about an existing dashboard list, for use in other resources. In particular, it can be used in a dashboard to register it in the list.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">get_dashboard_list</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;My super list&quot;</span><span class="p">)</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_datadog.get_ip_ranges">
<code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">get_ip_ranges</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.get_ip_ranges.AwaitableGetIpRangesResult<a class="headerlink" href="#pulumi_datadog.get_ip_ranges" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve information about Datadog’s IP addresses.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">get_ip_ranges</span><span class="p">()</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_datadog.get_monitor">
<code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">get_monitor</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">monitor_tags_filters</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_filter</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags_filters</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.get_monitor.AwaitableGetMonitorResult<a class="headerlink" href="#pulumi_datadog.get_monitor" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve information about an existing monitor for use in other resources.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">get_monitor</span><span class="p">(</span><span class="n">monitor_tags_filters</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;foo:bar&quot;</span><span class="p">],</span>
    <span class="n">name_filter</span><span class="o">=</span><span class="s2">&quot;My awesome monitor&quot;</span><span class="p">)</span>
</pre></div>
</div>
<ul class="simple">
<li><p><strong>id</strong> (String) The ID of this resource.</p></li>
<li><p><strong>monitor_tags_filter</strong> (List of String) A list of monitor tags to limit the search. This filters on the tags set on the monitor itself.</p></li>
<li><p><strong>name_filter</strong> (String) A monitor name to limit the search.</p></li>
<li><p><strong>tags_filter</strong> (List of String) A list of tags to limit the search. This filters on the monitor scope.</p></li>
</ul>
<ul class="simple">
<li><p><strong>enable_logs_sample</strong> (Boolean) Whether or not a list of log values which triggered the alert is included. This is only used by log monitors.</p></li>
<li><p><strong>escalation_message</strong> (String) Message included with a re-notification for this monitor.</p></li>
<li><p><strong>evaluation_delay</strong> (Number) Time (in seconds) for which evaluation is delayed. This is only used by metric monitors.</p></li>
<li><p><strong>include_tags</strong> (Boolean) Whether or not notifications from the monitor automatically inserts its triggering tags into the title.</p></li>
<li><p><strong>locked</strong> (Boolean) Whether or not changes to the monitor are restricted to the creator or admins.</p></li>
<li><p><strong>message</strong> (String) Message included with notifications for this monitor</p></li>
<li><p><strong>monitor_threshold_windows</strong> (List of Object) Mapping containing <code class="docutils literal notranslate"><span class="pre">recovery_window</span></code> and <code class="docutils literal notranslate"><span class="pre">trigger_window</span></code> values, e.g. <code class="docutils literal notranslate"><span class="pre">last_15m</span></code>. This is only used by anomaly monitors. (see below for nested schema)</p></li>
<li><p><strong>monitor_thresholds</strong> (List of Object) Alert thresholds of the monitor. (see below for nested schema)</p></li>
<li><p><strong>name</strong> (String) Name of the monitor</p></li>
<li><p><strong>new_host_delay</strong> (Number) Time (in seconds) allowing a host to boot and applications to fully start before starting the evaluation of monitor results.</p></li>
<li><p><strong>no_data_timeframe</strong> (Number) The number of minutes before the monitor notifies when data stops reporting.</p></li>
<li><p><strong>notify_audit</strong> (Boolean) Whether or not tagged users are notified on changes to the monitor.</p></li>
<li><p><strong>notify_no_data</strong> (Boolean) Whether or not this monitor notifies when data stops reporting.</p></li>
<li><p><strong>query</strong> (String) Query of the monitor.</p></li>
<li><p><strong>renotify_interval</strong> (Number) The number of minutes after the last notification before the monitor re-notifies on the current status.</p></li>
<li><p><strong>require_full_window</strong> (Boolean) Whether or not the monitor needs a full window of data before it is evaluated.</p></li>
<li><p><strong>tags</strong> (Set of String) List of tags associated with the monitor.</p></li>
<li><p><strong>threshold_windows</strong> (Map of String, Deprecated) Mapping containing <code class="docutils literal notranslate"><span class="pre">recovery_window</span></code> and <code class="docutils literal notranslate"><span class="pre">trigger_window</span></code> values, e.g. <code class="docutils literal notranslate"><span class="pre">last_15m</span></code>. This is only used by anomaly monitors.</p></li>
<li><p><strong>thresholds</strong> (Map of String, Deprecated) Alert thresholds of the monitor.</p></li>
<li><p><strong>timeout_h</strong> (Number) Number of hours of the monitor not reporting data before it automatically resolves from a triggered state.</p></li>
<li><p><strong>type</strong> (String) Type of the monitor.</p></li>
</ul>
<p><span class="raw-html-m2r"><a id="nestedatt--monitor_threshold_windows"></a></span></p>
<p>Read-only:</p>
<ul class="simple">
<li><p><strong>recovery_window</strong> (String)</p></li>
<li><p><strong>trigger_window</strong> (String)</p></li>
</ul>
<p><span class="raw-html-m2r"><a id="nestedatt--monitor_thresholds"></a></span></p>
<p>Read-only:</p>
<ul class="simple">
<li><p><strong>critical</strong> (String)</p></li>
<li><p><strong>critical_recovery</strong> (String)</p></li>
<li><p><strong>ok</strong> (String)</p></li>
<li><p><strong>unknown</strong> (String)</p></li>
<li><p><strong>warning</strong> (String)</p></li>
<li><p><strong>warning_recovery</strong> (String)</p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_datadog.get_permissions">
<code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">get_permissions</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.get_permissions.AwaitableGetPermissionsResult<a class="headerlink" href="#pulumi_datadog.get_permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve the list of Datadog permissions by name and their corresponding ID, for use in the role resource.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="n">permissions</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">get_permissions</span><span class="p">()</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_datadog.get_role">
<code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">get_role</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">filter</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.get_role.AwaitableGetRoleResult<a class="headerlink" href="#pulumi_datadog.get_role" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve information about an existing role for use in other resources.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">get_role</span><span class="p">(</span><span class="nb">filter</span><span class="o">=</span><span class="s2">&quot;Datadog Standard Role&quot;</span><span class="p">)</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_datadog.get_security_monitoring_rules">
<code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">get_security_monitoring_rules</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">default_only_filter</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_filter</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags_filters</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_only_filter</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.get_security_monitoring_rules.AwaitableGetSecurityMonitoringRulesResult<a class="headerlink" href="#pulumi_datadog.get_security_monitoring_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve information about existing security monitoring rules for use in other resources.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">get_security_monitoring_rules</span><span class="p">(</span><span class="n">default_only_filter</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">name_filter</span><span class="o">=</span><span class="s2">&quot;attack&quot;</span><span class="p">,</span>
    <span class="n">tags_filters</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;foo:bar&quot;</span><span class="p">])</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_datadog.get_synthetics_locations">
<code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">get_synthetics_locations</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.get_synthetics_locations.AwaitableGetSyntheticsLocationsResult<a class="headerlink" href="#pulumi_datadog.get_synthetics_locations" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve Datadog’s Synthetics Locations (to be used in Synthetics tests).</p>
</dd></dl>

</div>
