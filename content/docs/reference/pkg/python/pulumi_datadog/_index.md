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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">AwaitableGetMonitorResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">enable_logs_sample</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">escalation_message</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">evaluation_delay</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">include_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locked</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitor_tags_filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">new_host_delay</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">no_data_timeframe</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_audit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_no_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">renotify_interval</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">require_full_window</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags_filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">threshold_windows</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">thresholds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout_h</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.AwaitableGetMonitorResult" title="Permalink to this definition">¶</a></dt>
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
    <span class="n">opts</span><span class="o">=</span><span class="n">ResourceOptions</span><span class="p">(</span><span class="n">depends_on</span><span class="o">=</span><span class="p">[</span>
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
<li><p><strong>message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional message to provide when creating the downtime, can include notification handles</p></li>
<li><p><strong>monitor_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – When specified, this downtime will only apply to this monitor</p></li>
<li><p><strong>monitor_tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of monitor tags (up to 25), i.e. tags that are applied directly to monitors to which the downtime applies</p></li>
<li><p><strong>recurrence</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DowntimeRecurrenceArgs'</em><em>]</em><em>]</em>) – Optional recurring schedule for this downtime</p></li>
<li><p><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – specify the group scope to which this downtime applies. For everything use ‘*’</p></li>
<li><p><strong>start</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Specify when this downtime should start</p></li>
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
<li><p><strong>message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional message to provide when creating the downtime, can include notification handles</p></li>
<li><p><strong>monitor_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – When specified, this downtime will only apply to this monitor</p></li>
<li><p><strong>monitor_tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of monitor tags (up to 25), i.e. tags that are applied directly to monitors to which the downtime applies</p></li>
<li><p><strong>recurrence</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DowntimeRecurrenceArgs'</em><em>]</em><em>]</em>) – Optional recurring schedule for this downtime</p></li>
<li><p><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – specify the group scope to which this downtime applies. For everything use ‘*’</p></li>
<li><p><strong>start</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Specify when this downtime should start</p></li>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">GetMonitorResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">enable_logs_sample</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">escalation_message</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">evaluation_delay</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">include_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locked</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitor_tags_filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">new_host_delay</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">no_data_timeframe</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_audit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_no_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">renotify_interval</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">require_full_window</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags_filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">threshold_windows</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">thresholds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout_h</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.GetMonitorResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getMonitor.</p>
<dl class="py method">
<dt id="pulumi_datadog.GetMonitorResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_datadog.GetMonitorResult.id" title="Permalink to this definition">¶</a></dt>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">LogsArchive</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azure</span><span class="p">:</span> <span class="n">Union[LogsArchiveAzureArgs, Mapping[str, Any], Awaitable[Union[LogsArchiveAzureArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gcs</span><span class="p">:</span> <span class="n">Union[LogsArchiveGcsArgs, Mapping[str, Any], Awaitable[Union[LogsArchiveGcsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">include_tags</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rehydration_tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">s3</span><span class="p">:</span> <span class="n">Union[LogsArchiveS3Args, Mapping[str, Any], Awaitable[Union[LogsArchiveS3Args, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.LogsArchive" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Datadog <a class="reference external" href="https://docs.datadoghq.com/api/v2/logs-archives/">Logs Archive API</a> resource, which is used to create and manage Datadog logs archives.</p>
<p>Create a Datadog logs archive:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="n">my_s3_archive</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">LogsArchive</span><span class="p">(</span><span class="s2">&quot;myS3Archive&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;my s3 archive&quot;</span><span class="p">,</span>
    <span class="n">query</span><span class="o">=</span><span class="s2">&quot;service:myservice&quot;</span><span class="p">,</span>
    <span class="n">s3</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">LogsArchiveS3Args</span><span class="p">(</span>
        <span class="n">account_id</span><span class="o">=</span><span class="s2">&quot;001234567888&quot;</span><span class="p">,</span>
        <span class="n">bucket</span><span class="o">=</span><span class="s2">&quot;my-bucket&quot;</span><span class="p">,</span>
        <span class="n">path</span><span class="o">=</span><span class="s2">&quot;/path/foo&quot;</span><span class="p">,</span>
        <span class="n">role_name</span><span class="o">=</span><span class="s2">&quot;my-role-name&quot;</span><span class="p">,</span>
    <span class="p">))</span>
</pre></div>
</div>
<p>Logs archives can be imported using their public string ID, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import datadog:index/logsArchive:LogsArchive my_s3_archive 1Aabc2_dfQPLnXy3HlfK4hi
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
<dt id="pulumi_datadog.LogsArchive.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azure</span><span class="p">:</span> <span class="n">Union[LogsArchiveAzureArgs, Mapping[str, Any], Awaitable[Union[LogsArchiveAzureArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gcs</span><span class="p">:</span> <span class="n">Union[LogsArchiveGcsArgs, Mapping[str, Any], Awaitable[Union[LogsArchiveGcsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">include_tags</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rehydration_tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">s3</span><span class="p">:</span> <span class="n">Union[LogsArchiveS3Args, Mapping[str, Any], Awaitable[Union[LogsArchiveS3Args, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.logs_archive.LogsArchive<a class="headerlink" href="#pulumi_datadog.LogsArchive.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LogsArchive resource’s state with the given name, id, and optional extra
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
</ul>
</dd>
</dl>
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
</ul>
</dd>
</dl>
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
    <span class="n">opts</span><span class="o">=</span><span class="n">ResourceOptions</span><span class="p">(</span><span class="n">depends_on</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;datadog_logs_index.sample_index&quot;</span><span class="p">]))</span>
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
</ul>
</dd>
</dl>
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
</ul>
</dd>
</dl>
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
    <span class="n">opts</span><span class="o">=</span><span class="n">ResourceOptions</span><span class="p">(</span><span class="n">depends_on</span><span class="o">=</span><span class="p">[</span>
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
</ul>
</dd>
</dl>
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
</ul>
</dd>
</dl>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">Monitor</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_logs_sample</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">escalation_message</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">evaluation_delay</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_delete</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">include_tags</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locked</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">new_host_delay</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">no_data_timeframe</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_audit</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_no_data</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">renotify_interval</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">require_full_window</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">silenced</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">threshold_windows</span><span class="p">:</span> <span class="n">Union[MonitorThresholdWindowsArgs, Mapping[str, Any], Awaitable[Union[MonitorThresholdWindowsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">thresholds</span><span class="p">:</span> <span class="n">Union[MonitorThresholdsArgs, Mapping[str, Any], Awaitable[Union[MonitorThresholdsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout_h</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">validate</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.Monitor" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Datadog monitor resource. This can be used to create and manage Datadog monitors.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="c1"># Create a new Datadog monitor</span>
<span class="n">foo</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">Monitor</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Name for monitor foo&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;metric alert&quot;</span><span class="p">,</span>
    <span class="n">message</span><span class="o">=</span><span class="s2">&quot;Monitor triggered. Notify: @hipchat-channel&quot;</span><span class="p">,</span>
    <span class="n">escalation_message</span><span class="o">=</span><span class="s2">&quot;Escalation message @pagerduty&quot;</span><span class="p">,</span>
    <span class="n">query</span><span class="o">=</span><span class="s2">&quot;avg(last_1h):avg:aws.ec2.cpu{environment:foo,host:foo} by </span><span class="si">{host}</span><span class="s2"> &gt; 4&quot;</span><span class="p">,</span>
    <span class="n">thresholds</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">MonitorThresholdsArgs</span><span class="p">(</span>
        <span class="n">ok</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
        <span class="n">warning</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
        <span class="n">warning_recovery</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
        <span class="n">critical</span><span class="o">=</span><span class="mi">4</span><span class="p">,</span>
        <span class="n">critical_recovery</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">notify_no_data</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">renotify_interval</span><span class="o">=</span><span class="mi">60</span><span class="p">,</span>
    <span class="n">notify_audit</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">timeout_h</span><span class="o">=</span><span class="mi">60</span><span class="p">,</span>
    <span class="n">include_tags</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;foo:bar&quot;</span><span class="p">,</span>
        <span class="s2">&quot;baz&quot;</span><span class="p">,</span>
    <span class="p">])</span>
</pre></div>
</div>
<p>There are two ways how to silence a single monitor:</p>
<ul class="simple">
<li><p>Mute it by hand</p></li>
<li><p>Create a Downtime</p></li>
</ul>
<p>Both of these actions add a new value to the <code class="docutils literal notranslate"><span class="pre">silenced</span></code> map. This can be problematic if the <code class="docutils literal notranslate"><span class="pre">silenced</span></code> attribute doesn’t contain them in your application, as they would be removed on next <code class="docutils literal notranslate"><span class="pre">pulumi</span> <span class="pre">up</span></code> invocation. In order to prevent that from happening, you can add following to your monitor:</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
</pre></div>
</div>
<p>The above will make sure that any changes to the <code class="docutils literal notranslate"><span class="pre">silenced</span></code> attribute are ignored.</p>
<p>This issue doesn’t apply to multi-monitor downtimes (those that don’t contain <code class="docutils literal notranslate"><span class="pre">monitor_id</span></code> ), as these don’t influence contents of the <code class="docutils literal notranslate"><span class="pre">silenced</span></code> attribute.</p>
<p>You can compose monitors of all types in order to define more specific alert conditions (see the <a class="reference external" href="https://docs.datadoghq.com/monitors/monitor_types/composite/">doc</a>). You just need to reuse the ID of your <code class="docutils literal notranslate"><span class="pre">Monitor</span></code> resources. You can also compose any monitor with a <code class="docutils literal notranslate"><span class="pre">SyntheticsTest</span></code> by passing the computed <code class="docutils literal notranslate"><span class="pre">monitor_id</span></code> attribute in the query.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="n">bar</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">Monitor</span><span class="p">(</span><span class="s2">&quot;bar&quot;</span><span class="p">,</span>
    <span class="n">message</span><span class="o">=</span><span class="s2">&quot;This is a message&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Composite Monitor&quot;</span><span class="p">,</span>
    <span class="n">query</span><span class="o">=</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">datadog_monitor</span><span class="p">[</span><span class="s1">&#39;foo&#39;</span><span class="p">][</span><span class="s1">&#39;id&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2"> || </span><span class="si">{</span><span class="n">datadog_synthetics_test</span><span class="p">[</span><span class="s1">&#39;foo&#39;</span><span class="p">][</span><span class="s1">&#39;monitor_id&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;composite&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Monitors can be imported using their numeric ID, e.g. console</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import datadog:index/monitor:Monitor bytes_received_localhost <span class="m">2081</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enable_logs_sample</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether or not to include a list of log values which triggered the alert. Defaults to false. This is only used by log monitors.</p></li>
<li><p><strong>evaluation_delay</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Time (in seconds) to delay evaluation, as a non-negative integer.</p></li>
<li><p><strong>force_delete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether this monitor can be deleted even if it’s referenced by other resources (e.g. SLO, composite monitor).</p></li>
<li><p><strong>include_tags</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether notifications from this monitor automatically insert its triggering tags into the title. Defaults to true.</p></li>
<li><p><strong>locked</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether changes to to this monitor should be restricted to the creator or admins. Defaults to False.</p></li>
<li><p><strong>new_host_delay</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Time (in seconds) to allow a host to boot and</p></li>
<li><p><strong>no_data_timeframe</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of minutes before a monitor will notify when data stops reporting. Provider defaults to 10 minutes.</p></li>
<li><p><strong>notify_audit</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether tagged users will be notified on changes to this monitor.</p></li>
<li><p><strong>notify_no_data</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether this monitor will notify when data stops reporting. Defaults</p></li>
<li><p><strong>renotify_interval</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of minutes after the last notification before a monitor will re-notify</p></li>
<li><p><strong>require_full_window</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether this monitor needs a full window of data before it’s evaluated.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>silenced</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Each scope will be muted until the given POSIX timestamp or forever if the value is 0. Use <code class="docutils literal notranslate"><span class="pre">-1</span></code> if you want to unmute the scope. <strong>Deprecated</strong> The <code class="docutils literal notranslate"><span class="pre">silenced</span></code> parameter is being deprecated in favor of the downtime resource. This will be removed in the next major version of the provider Provider.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of tags to associate with your monitor. This can help you categorize and filter monitors in the manage monitors page of the UI. Note: it’s not currently possible to filter by these tags when querying via the API</p></li>
<li><p><strong>threshold_windows</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'MonitorThresholdWindowsArgs'</em><em>]</em><em>]</em>) – A mapping containing <code class="docutils literal notranslate"><span class="pre">recovery_window</span></code> and <code class="docutils literal notranslate"><span class="pre">trigger_window</span></code> values, e.g. <code class="docutils literal notranslate"><span class="pre">last_15m</span></code> . Can only be used for, and are required for, anomaly monitors.</p></li>
<li><p><strong>timeout_h</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of hours of the monitor not reporting data before it will automatically resolve</p></li>
<li><p><strong>validate</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to false, skip the validation call done during <code class="docutils literal notranslate"><span class="pre">plan</span></code> .</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_datadog.Monitor.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_logs_sample</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">escalation_message</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">evaluation_delay</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_delete</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">include_tags</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locked</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">new_host_delay</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">no_data_timeframe</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_audit</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_no_data</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">priority</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">renotify_interval</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">require_full_window</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">silenced</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">threshold_windows</span><span class="p">:</span> <span class="n">Union[MonitorThresholdWindowsArgs, Mapping[str, Any], Awaitable[Union[MonitorThresholdWindowsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">thresholds</span><span class="p">:</span> <span class="n">Union[MonitorThresholdsArgs, Mapping[str, Any], Awaitable[Union[MonitorThresholdsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout_h</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">validate</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.monitor.Monitor<a class="headerlink" href="#pulumi_datadog.Monitor.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Monitor resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enable_logs_sample</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether or not to include a list of log values which triggered the alert. Defaults to false. This is only used by log monitors.</p></li>
<li><p><strong>evaluation_delay</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Time (in seconds) to delay evaluation, as a non-negative integer.</p></li>
<li><p><strong>force_delete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether this monitor can be deleted even if it’s referenced by other resources (e.g. SLO, composite monitor).</p></li>
<li><p><strong>include_tags</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether notifications from this monitor automatically insert its triggering tags into the title. Defaults to true.</p></li>
<li><p><strong>locked</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether changes to to this monitor should be restricted to the creator or admins. Defaults to False.</p></li>
<li><p><strong>new_host_delay</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Time (in seconds) to allow a host to boot and</p></li>
<li><p><strong>no_data_timeframe</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of minutes before a monitor will notify when data stops reporting. Provider defaults to 10 minutes.</p></li>
<li><p><strong>notify_audit</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether tagged users will be notified on changes to this monitor.</p></li>
<li><p><strong>notify_no_data</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether this monitor will notify when data stops reporting. Defaults</p></li>
<li><p><strong>renotify_interval</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of minutes after the last notification before a monitor will re-notify</p></li>
<li><p><strong>require_full_window</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether this monitor needs a full window of data before it’s evaluated.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>silenced</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Each scope will be muted until the given POSIX timestamp or forever if the value is 0. Use <code class="docutils literal notranslate"><span class="pre">-1</span></code> if you want to unmute the scope. <strong>Deprecated</strong> The <code class="docutils literal notranslate"><span class="pre">silenced</span></code> parameter is being deprecated in favor of the downtime resource. This will be removed in the next major version of the provider Provider.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of tags to associate with your monitor. This can help you categorize and filter monitors in the manage monitors page of the UI. Note: it’s not currently possible to filter by these tags when querying via the API</p></li>
<li><p><strong>threshold_windows</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'MonitorThresholdWindowsArgs'</em><em>]</em><em>]</em>) – A mapping containing <code class="docutils literal notranslate"><span class="pre">recovery_window</span></code> and <code class="docutils literal notranslate"><span class="pre">trigger_window</span></code> values, e.g. <code class="docutils literal notranslate"><span class="pre">last_15m</span></code> . Can only be used for, and are required for, anomaly monitors.</p></li>
<li><p><strong>timeout_h</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of hours of the monitor not reporting data before it will automatically resolve</p></li>
<li><p><strong>validate</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to false, skip the validation call done during <code class="docutils literal notranslate"><span class="pre">plan</span></code> .</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.enable_logs_sample">
<em class="property">property </em><code class="sig-name descname">enable_logs_sample</code><a class="headerlink" href="#pulumi_datadog.Monitor.enable_logs_sample" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean indicating whether or not to include a list of log values which triggered the alert. Defaults to false. This is only used by log monitors.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.evaluation_delay">
<em class="property">property </em><code class="sig-name descname">evaluation_delay</code><a class="headerlink" href="#pulumi_datadog.Monitor.evaluation_delay" title="Permalink to this definition">¶</a></dt>
<dd><p>Time (in seconds) to delay evaluation, as a non-negative integer.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.force_delete">
<em class="property">property </em><code class="sig-name descname">force_delete</code><a class="headerlink" href="#pulumi_datadog.Monitor.force_delete" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean indicating whether this monitor can be deleted even if it’s referenced by other resources (e.g. SLO, composite monitor).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.include_tags">
<em class="property">property </em><code class="sig-name descname">include_tags</code><a class="headerlink" href="#pulumi_datadog.Monitor.include_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean indicating whether notifications from this monitor automatically insert its triggering tags into the title. Defaults to true.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.locked">
<em class="property">property </em><code class="sig-name descname">locked</code><a class="headerlink" href="#pulumi_datadog.Monitor.locked" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean indicating whether changes to to this monitor should be restricted to the creator or admins. Defaults to False.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.new_host_delay">
<em class="property">property </em><code class="sig-name descname">new_host_delay</code><a class="headerlink" href="#pulumi_datadog.Monitor.new_host_delay" title="Permalink to this definition">¶</a></dt>
<dd><p>Time (in seconds) to allow a host to boot and</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.no_data_timeframe">
<em class="property">property </em><code class="sig-name descname">no_data_timeframe</code><a class="headerlink" href="#pulumi_datadog.Monitor.no_data_timeframe" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of minutes before a monitor will notify when data stops reporting. Provider defaults to 10 minutes.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.notify_audit">
<em class="property">property </em><code class="sig-name descname">notify_audit</code><a class="headerlink" href="#pulumi_datadog.Monitor.notify_audit" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean indicating whether tagged users will be notified on changes to this monitor.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.notify_no_data">
<em class="property">property </em><code class="sig-name descname">notify_no_data</code><a class="headerlink" href="#pulumi_datadog.Monitor.notify_no_data" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean indicating whether this monitor will notify when data stops reporting. Defaults</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.renotify_interval">
<em class="property">property </em><code class="sig-name descname">renotify_interval</code><a class="headerlink" href="#pulumi_datadog.Monitor.renotify_interval" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of minutes after the last notification before a monitor will re-notify</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.require_full_window">
<em class="property">property </em><code class="sig-name descname">require_full_window</code><a class="headerlink" href="#pulumi_datadog.Monitor.require_full_window" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean indicating whether this monitor needs a full window of data before it’s evaluated.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.silenced">
<em class="property">property </em><code class="sig-name descname">silenced</code><a class="headerlink" href="#pulumi_datadog.Monitor.silenced" title="Permalink to this definition">¶</a></dt>
<dd><p>Each scope will be muted until the given POSIX timestamp or forever if the value is 0. Use <code class="docutils literal notranslate"><span class="pre">-1</span></code> if you want to unmute the scope. <strong>Deprecated</strong> The <code class="docutils literal notranslate"><span class="pre">silenced</span></code> parameter is being deprecated in favor of the downtime resource. This will be removed in the next major version of the provider Provider.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_datadog.Monitor.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tags to associate with your monitor. This can help you categorize and filter monitors in the manage monitors page of the UI. Note: it’s not currently possible to filter by these tags when querying via the API</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.threshold_windows">
<em class="property">property </em><code class="sig-name descname">threshold_windows</code><a class="headerlink" href="#pulumi_datadog.Monitor.threshold_windows" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping containing <code class="docutils literal notranslate"><span class="pre">recovery_window</span></code> and <code class="docutils literal notranslate"><span class="pre">trigger_window</span></code> values, e.g. <code class="docutils literal notranslate"><span class="pre">last_15m</span></code> . Can only be used for, and are required for, anomaly monitors.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.timeout_h">
<em class="property">property </em><code class="sig-name descname">timeout_h</code><a class="headerlink" href="#pulumi_datadog.Monitor.timeout_h" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of hours of the monitor not reporting data before it will automatically resolve</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.validate">
<em class="property">property </em><code class="sig-name descname">validate</code><a class="headerlink" href="#pulumi_datadog.Monitor.validate" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to false, skip the validation call done during <code class="docutils literal notranslate"><span class="pre">plan</span></code> .</p>
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
                            <span class="n">group_bies</span><span class="o">=</span><span class="p">[</span><span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetTileDefRequestLogQueryGroupByArgs</span><span class="p">(</span>
                                <span class="n">facet</span><span class="o">=</span><span class="s2">&quot;host&quot;</span><span class="p">,</span>
                                <span class="n">limit</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span>
                                <span class="n">sort</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetTileDefRequestLogQueryGroupBySortArgs</span><span class="p">(</span>
                                    <span class="n">aggregation</span><span class="o">=</span><span class="s2">&quot;avg&quot;</span><span class="p">,</span>
                                    <span class="n">order</span><span class="o">=</span><span class="s2">&quot;desc&quot;</span><span class="p">,</span>
                                    <span class="n">facet</span><span class="o">=</span><span class="s2">&quot;@duration&quot;</span><span class="p">,</span>
                                <span class="p">),</span>
                            <span class="p">)],</span>
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
                            <span class="n">group_bies</span><span class="o">=</span><span class="p">[</span><span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetTileDefRequestApmQueryGroupByArgs</span><span class="p">(</span>
                                <span class="n">facet</span><span class="o">=</span><span class="s2">&quot;resource_name&quot;</span><span class="p">,</span>
                                <span class="n">limit</span><span class="o">=</span><span class="mi">50</span><span class="p">,</span>
                                <span class="n">sort</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetTileDefRequestApmQueryGroupBySortArgs</span><span class="p">(</span>
                                    <span class="n">aggregation</span><span class="o">=</span><span class="s2">&quot;avg&quot;</span><span class="p">,</span>
                                    <span class="n">order</span><span class="o">=</span><span class="s2">&quot;desc&quot;</span><span class="p">,</span>
                                    <span class="n">facet</span><span class="o">=</span><span class="s2">&quot;@string_query.interval&quot;</span><span class="p">,</span>
                                <span class="p">),</span>
                            <span class="p">)],</span>
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
<dt id="pulumi_datadog.ServiceLevelObjective">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">ServiceLevelObjective</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitor_ids</span><span class="p">:</span> <span class="n">Union[Sequence[Union[int, Awaitable[int], Output[T]]], Awaitable[Sequence[Union[int, Awaitable[int], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="p">:</span> <span class="n">Union[ServiceLevelObjectiveQueryArgs, Mapping[str, Any], Awaitable[Union[ServiceLevelObjectiveQueryArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">thresholds</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ServiceLevelObjectiveThresholdArgs, Mapping[str, Any], Awaitable[Union[ServiceLevelObjectiveThresholdArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ServiceLevelObjectiveThresholdArgs, Mapping[str, Any], Awaitable[Union[ServiceLevelObjectiveThresholdArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">validate</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.ServiceLevelObjective" title="Permalink to this definition">¶</a></dt>
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
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A static set of groups to filter monitor-based SLOs</p></li>
<li><p><strong>monitor_ids</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>int</em><em>]</em><em>]</em><em>]</em>) – A static set of monitor IDs to use as part of the SLO</p></li>
<li><p><strong>query</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceLevelObjectiveQueryArgs'</em><em>]</em><em>]</em>) – The metric query of good / total events</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of tags to associate with your service level objective. This can help you categorize and filter service level objectives in the service level objectives page of the UI. Note: it’s not currently possible to filter by these tags when querying via the API</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>-   `thresholds`: (Required) - A list of thresholds and targets that define the service level objectives from the provided SLIs.
</pre></div>
</div>
<dl class="py method">
<dt id="pulumi_datadog.ServiceLevelObjective.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitor_ids</span><span class="p">:</span> <span class="n">Union[Sequence[Union[int, Awaitable[int], Output[T]]], Awaitable[Sequence[Union[int, Awaitable[int], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="p">:</span> <span class="n">Union[ServiceLevelObjectiveQueryArgs, Mapping[str, Any], Awaitable[Union[ServiceLevelObjectiveQueryArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">thresholds</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ServiceLevelObjectiveThresholdArgs, Mapping[str, Any], Awaitable[Union[ServiceLevelObjectiveThresholdArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ServiceLevelObjectiveThresholdArgs, Mapping[str, Any], Awaitable[Union[ServiceLevelObjectiveThresholdArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">validate</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.service_level_objective.ServiceLevelObjective<a class="headerlink" href="#pulumi_datadog.ServiceLevelObjective.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceLevelObjective resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A static set of groups to filter monitor-based SLOs</p></li>
<li><p><strong>monitor_ids</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>int</em><em>]</em><em>]</em><em>]</em>) – A static set of monitor IDs to use as part of the SLO</p></li>
<li><p><strong>query</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceLevelObjectiveQueryArgs'</em><em>]</em><em>]</em>) – The metric query of good / total events</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of tags to associate with your service level objective. This can help you categorize and filter service level objectives in the service level objectives page of the UI. Note: it’s not currently possible to filter by these tags when querying via the API</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>-   `thresholds`: (Required) - A list of thresholds and targets that define the service level objectives from the provided SLIs.
</pre></div>
</div>
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
<dt id="pulumi_datadog.ServiceLevelObjective.query">
<em class="property">property </em><code class="sig-name descname">query</code><a class="headerlink" href="#pulumi_datadog.ServiceLevelObjective.query" title="Permalink to this definition">¶</a></dt>
<dd><p>The metric query of good / total events</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.ServiceLevelObjective.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_datadog.ServiceLevelObjective.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tags to associate with your service level objective. This can help you categorize and filter service level objectives in the service level objectives page of the UI. Note: it’s not currently possible to filter by these tags when querying via the API</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">thresholds</span></code>: (Required) - A list of thresholds and targets that define the service level objectives from the provided SLIs.</p></li>
</ul>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">SyntheticsGlobalVariable</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.SyntheticsGlobalVariable" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Datadog synthetics global variable resource. This can be used to create and manage Datadog synthetics global variables.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="n">test_api</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">SyntheticsGlobalVariable</span><span class="p">(</span><span class="s2">&quot;testApi&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Description of the variable&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;EXAMPLE_VARIABLE&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;foo:bar&quot;</span><span class="p">,</span>
        <span class="s2">&quot;env:test&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">value</span><span class="o">=</span><span class="s2">&quot;variable-value&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Secure global variables are not supported for now.</p>
<p>Synthetics global variables can be imported using their string ID, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import datadog:index/syntheticsGlobalVariable:SyntheticsGlobalVariable fizz abcde123-fghi-456-jkl-mnopqrstuv
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
<dt id="pulumi_datadog.SyntheticsGlobalVariable.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.synthetics_global_variable.SyntheticsGlobalVariable<a class="headerlink" href="#pulumi_datadog.SyntheticsGlobalVariable.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SyntheticsGlobalVariable resource’s state with the given name, id, and optional extra
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
<dt id="pulumi_datadog.SyntheticsTest">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">SyntheticsTest</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">assertions</span><span class="p">:</span> <span class="n">Union[Sequence[Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T]]], Awaitable[Sequence[Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_ids</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locations</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">options</span><span class="p">:</span> <span class="n">Union[SyntheticsTestOptionsArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestOptionsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">options_list</span><span class="p">:</span> <span class="n">Union[SyntheticsTestOptionsListArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestOptionsListArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request</span><span class="p">:</span> <span class="n">Union[SyntheticsTestRequestArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestRequestArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_basicauth</span><span class="p">:</span> <span class="n">Union[SyntheticsTestRequestBasicauthArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestRequestBasicauthArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_client_certificate</span><span class="p">:</span> <span class="n">Union[SyntheticsTestRequestClientCertificateArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestRequestClientCertificateArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_headers</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_query</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">steps</span><span class="p">:</span> <span class="n">Union[Sequence[Union[SyntheticsTestStepArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestStepArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[SyntheticsTestStepArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestStepArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subtype</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">variables</span><span class="p">:</span> <span class="n">Union[Sequence[Union[SyntheticsTestVariableArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestVariableArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[SyntheticsTestVariableArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestVariableArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.SyntheticsTest" title="Permalink to this definition">¶</a></dt>
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

<span class="n">test_tcp</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">SyntheticsTest</span><span class="p">(</span><span class="s2">&quot;testTcp&quot;</span><span class="p">,</span>
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
    <span class="n">variables</span><span class="o">=</span><span class="p">[</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">SyntheticsTestVariableArgs</span><span class="p">(</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;text&quot;</span><span class="p">,</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">&quot;MY_PATTERN_VAR&quot;</span><span class="p">,</span>
            <span class="n">pattern</span><span class="o">=</span><span class="s2">&quot;{{numeric(3)}}&quot;</span><span class="p">,</span>
            <span class="n">example</span><span class="o">=</span><span class="s2">&quot;597&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">SyntheticsTestVariableArgs</span><span class="p">(</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;email&quot;</span><span class="p">,</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">&quot;MY_EMAIL_VAR&quot;</span><span class="p">,</span>
            <span class="n">pattern</span><span class="o">=</span><span class="s2">&quot;jd8-afe-ydv.{{ numeric(10) }}@synthetics.dtdg.co&quot;</span><span class="p">,</span>
            <span class="n">example</span><span class="o">=</span><span class="s2">&quot;jd8-afe-ydv.4546132139@synthetics.dtdg.co&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">SyntheticsTestVariableArgs</span><span class="p">(</span>
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
        <span class="s2">&quot;type&quot;</span><span class="p">:</span> <span class="s2">&quot;responsTime&quot;</span><span class="p">,</span>
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
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_datadog.SyntheticsTest.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">assertions</span><span class="p">:</span> <span class="n">Union[Sequence[Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T]]], Awaitable[Sequence[Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_ids</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locations</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitor_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">options</span><span class="p">:</span> <span class="n">Union[SyntheticsTestOptionsArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestOptionsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">options_list</span><span class="p">:</span> <span class="n">Union[SyntheticsTestOptionsListArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestOptionsListArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request</span><span class="p">:</span> <span class="n">Union[SyntheticsTestRequestArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestRequestArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_basicauth</span><span class="p">:</span> <span class="n">Union[SyntheticsTestRequestBasicauthArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestRequestBasicauthArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_client_certificate</span><span class="p">:</span> <span class="n">Union[SyntheticsTestRequestClientCertificateArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestRequestClientCertificateArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_headers</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_query</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">steps</span><span class="p">:</span> <span class="n">Union[Sequence[Union[SyntheticsTestStepArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestStepArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[SyntheticsTestStepArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestStepArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subtype</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">variables</span><span class="p">:</span> <span class="n">Union[Sequence[Union[SyntheticsTestVariableArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestVariableArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[SyntheticsTestVariableArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestVariableArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.synthetics_test.SyntheticsTest<a class="headerlink" href="#pulumi_datadog.SyntheticsTest.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SyntheticsTest resource’s state with the given name, id, and optional extra
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">User</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_role</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">handle</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_admin</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.User" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Datadog user resource. This can be used to create and manage Datadog users.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="c1"># Create a new Datadog user</span>
<span class="n">foo</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">email</span><span class="o">=</span><span class="s2">&quot;new@example.com&quot;</span><span class="p">,</span>
    <span class="n">handle</span><span class="o">=</span><span class="s2">&quot;new@example.com&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;New User&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>users can be imported using their handle, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import datadog:index/user:User example_user existing@example.com
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
<dt id="pulumi_datadog.User.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_role</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">handle</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_admin</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">verified</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.user.User<a class="headerlink" href="#pulumi_datadog.User.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing User resource’s state with the given name, id, and optional extra
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
</dd></dl>

<dl class="py function">
<dt id="pulumi_datadog.get_synthetics_locations">
<code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">get_synthetics_locations</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.get_synthetics_locations.AwaitableGetSyntheticsLocationsResult<a class="headerlink" href="#pulumi_datadog.get_synthetics_locations" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve Datadog’s Synthetics Locations (to be used in Synthetics tests).</p>
</dd></dl>

</div>
