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
<dt id="pulumi_datadog.AwaitableGetIpRangesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">AwaitableGetIpRangesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">agents_ipv4s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">agents_ipv6s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_ipv4s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_ipv6s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">apm_ipv4s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">apm_ipv6s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logs_ipv4s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logs_ipv6s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">process_ipv4s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">process_ipv6s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">synthetics_ipv4s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">synthetics_ipv6s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">webhooks_ipv4s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">webhooks_ipv6s</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.AwaitableGetIpRangesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_datadog.AwaitableGetMonitorResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">AwaitableGetMonitorResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">enable_logs_sample</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">escalation_message</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">evaluation_delay</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">include_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locked</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitor_tags_filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">new_host_delay</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">no_data_timeframe</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_audit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_no_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">renotify_interval</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">require_full_window</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags_filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">threshold_windows</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">thresholds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout_h</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.AwaitableGetMonitorResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_datadog.Dashboard">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">Dashboard</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_read_only</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">layout_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_lists</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_variable_presets</span><span class="p">:</span> <span class="n">Union[List[Union[DashboardTemplateVariablePresetArgs, Mapping[str, Any], Awaitable[Union[DashboardTemplateVariablePresetArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[DashboardTemplateVariablePresetArgs, Mapping[str, Any], Awaitable[Union[DashboardTemplateVariablePresetArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_variables</span><span class="p">:</span> <span class="n">Union[List[Union[DashboardTemplateVariableArgs, Mapping[str, Any], Awaitable[Union[DashboardTemplateVariableArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[DashboardTemplateVariableArgs, Mapping[str, Any], Awaitable[Union[DashboardTemplateVariableArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">title</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">widgets</span><span class="p">:</span> <span class="n">Union[List[Union[DashboardWidgetArgs, Mapping[str, Any], Awaitable[Union[DashboardWidgetArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[DashboardWidgetArgs, Mapping[str, Any], Awaitable[Union[DashboardWidgetArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.Dashboard" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Datadog dashboard resource. This can be used to create and manage Datadog dashboards.</p>
<blockquote>
<div><p><strong>Note:</strong> This resource uses the new <a class="reference external" href="https://docs.datadoghq.com/api/v1/dashboards/">Dashboard API</a> which adds new features like better validation and support for the <a class="reference external" href="https://docs.datadoghq.com/graphing/widgets/group/">Group widget</a>. Additionally, this resource unifies <code class="docutils literal notranslate"><span class="pre">TimeBoard</span></code> and <code class="docutils literal notranslate"><span class="pre">ScreenBoard</span></code> resources to allow you to manage all of your dashboards using a single format.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="n">ordered_dashboard</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">Dashboard</span><span class="p">(</span><span class="s2">&quot;orderedDashboard&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Created using the Datadog provider in TF&quot;</span><span class="p">,</span>
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
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Created using the Datadog provider in TF&quot;</span><span class="p">,</span>
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
                <span class="n">logset</span><span class="o">=</span><span class="s2">&quot;19&quot;</span><span class="p">,</span>
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
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the dashboard.</p></li>
<li><p><strong>is_read_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this dashboard is read-only. If <code class="docutils literal notranslate"><span class="pre">true</span></code>, only the author and admins can make changes to it.</p></li>
<li><p><strong>layout_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Layout type of the dashboard. Available values are: <code class="docutils literal notranslate"><span class="pre">ordered</span></code> (previous timeboard) or <code class="docutils literal notranslate"><span class="pre">free</span></code> (previous screenboard layout).
<span class="raw-html-m2r"><br></span><strong>Note: This value cannot be changed. Converting a dashboard from ``free`` &lt;&gt; ``ordered`` requires destroying and re-creating the dashboard.</strong> Instead of using <code class="docutils literal notranslate"><span class="pre">ForceNew</span></code>, this is a manual action as many underlying widget configs need to be updated to work for the updated layout, otherwise the new dashboard won’t be created properly.</p></li>
<li><p><strong>notify_lists</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of handles of users to notify when changes are made to this dashboard.</p></li>
<li><p><strong>template_variable_presets</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DashboardTemplateVariablePresetArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – The list of selectable template variable presets for this dashboard.</p></li>
<li><p><strong>template_variables</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DashboardTemplateVariableArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – The list of template variables for this dashboard.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Title of the dashboard.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Read only field - The URL of the dashboard.</p></li>
<li><p><strong>widgets</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DashboardWidgetArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Nested block describing a widget. The structure of this block is described below. Multiple <code class="docutils literal notranslate"><span class="pre">widget</span></code> blocks are allowed within a <code class="docutils literal notranslate"><span class="pre">Dashboard</span></code> resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_datadog.Dashboard.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_read_only</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">layout_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_lists</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_variable_presets</span><span class="p">:</span> <span class="n">Union[List[Union[DashboardTemplateVariablePresetArgs, Mapping[str, Any], Awaitable[Union[DashboardTemplateVariablePresetArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[DashboardTemplateVariablePresetArgs, Mapping[str, Any], Awaitable[Union[DashboardTemplateVariablePresetArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_variables</span><span class="p">:</span> <span class="n">Union[List[Union[DashboardTemplateVariableArgs, Mapping[str, Any], Awaitable[Union[DashboardTemplateVariableArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[DashboardTemplateVariableArgs, Mapping[str, Any], Awaitable[Union[DashboardTemplateVariableArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">title</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">widgets</span><span class="p">:</span> <span class="n">Union[List[Union[DashboardWidgetArgs, Mapping[str, Any], Awaitable[Union[DashboardWidgetArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[DashboardWidgetArgs, Mapping[str, Any], Awaitable[Union[DashboardWidgetArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.dashboard.Dashboard<a class="headerlink" href="#pulumi_datadog.Dashboard.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Dashboard resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the dashboard.</p></li>
<li><p><strong>is_read_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether this dashboard is read-only. If <code class="docutils literal notranslate"><span class="pre">true</span></code>, only the author and admins can make changes to it.</p></li>
<li><p><strong>layout_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Layout type of the dashboard. Available values are: <code class="docutils literal notranslate"><span class="pre">ordered</span></code> (previous timeboard) or <code class="docutils literal notranslate"><span class="pre">free</span></code> (previous screenboard layout).
<span class="raw-html-m2r"><br></span><strong>Note: This value cannot be changed. Converting a dashboard from ``free`` &lt;&gt; ``ordered`` requires destroying and re-creating the dashboard.</strong> Instead of using <code class="docutils literal notranslate"><span class="pre">ForceNew</span></code>, this is a manual action as many underlying widget configs need to be updated to work for the updated layout, otherwise the new dashboard won’t be created properly.</p></li>
<li><p><strong>notify_lists</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – List of handles of users to notify when changes are made to this dashboard.</p></li>
<li><p><strong>template_variable_presets</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DashboardTemplateVariablePresetArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – The list of selectable template variable presets for this dashboard.</p></li>
<li><p><strong>template_variables</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DashboardTemplateVariableArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – The list of template variables for this dashboard.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Title of the dashboard.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Read only field - The URL of the dashboard.</p></li>
<li><p><strong>widgets</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DashboardWidgetArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Nested block describing a widget. The structure of this block is described below. Multiple <code class="docutils literal notranslate"><span class="pre">widget</span></code> blocks are allowed within a <code class="docutils literal notranslate"><span class="pre">Dashboard</span></code> resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Dashboard.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_datadog.Dashboard.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the dashboard.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Dashboard.is_read_only">
<em class="property">property </em><code class="sig-name descname">is_read_only</code><a class="headerlink" href="#pulumi_datadog.Dashboard.is_read_only" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether this dashboard is read-only. If <code class="docutils literal notranslate"><span class="pre">true</span></code>, only the author and admins can make changes to it.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Dashboard.layout_type">
<em class="property">property </em><code class="sig-name descname">layout_type</code><a class="headerlink" href="#pulumi_datadog.Dashboard.layout_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Layout type of the dashboard. Available values are: <code class="docutils literal notranslate"><span class="pre">ordered</span></code> (previous timeboard) or <code class="docutils literal notranslate"><span class="pre">free</span></code> (previous screenboard layout).
<span class="raw-html-m2r"><br></span><strong>Note: This value cannot be changed. Converting a dashboard from ``free`` &lt;&gt; ``ordered`` requires destroying and re-creating the dashboard.</strong> Instead of using <code class="docutils literal notranslate"><span class="pre">ForceNew</span></code>, this is a manual action as many underlying widget configs need to be updated to work for the updated layout, otherwise the new dashboard won’t be created properly.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Dashboard.notify_lists">
<em class="property">property </em><code class="sig-name descname">notify_lists</code><a class="headerlink" href="#pulumi_datadog.Dashboard.notify_lists" title="Permalink to this definition">¶</a></dt>
<dd><p>List of handles of users to notify when changes are made to this dashboard.</p>
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
<dd><p>Title of the dashboard.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Dashboard.url">
<em class="property">property </em><code class="sig-name descname">url</code><a class="headerlink" href="#pulumi_datadog.Dashboard.url" title="Permalink to this definition">¶</a></dt>
<dd><p>Read only field - The URL of the dashboard.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Dashboard.widgets">
<em class="property">property </em><code class="sig-name descname">widgets</code><a class="headerlink" href="#pulumi_datadog.Dashboard.widgets" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested block describing a widget. The structure of this block is described below. Multiple <code class="docutils literal notranslate"><span class="pre">widget</span></code> blocks are allowed within a <code class="docutils literal notranslate"><span class="pre">Dashboard</span></code> resource.</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">DashboardList</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dash_items</span><span class="p">:</span> <span class="n">Union[List[Union[DashboardListDashItemArgs, Mapping[str, Any], Awaitable[Union[DashboardListDashItemArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[DashboardListDashItemArgs, Mapping[str, Any], Awaitable[Union[DashboardListDashItemArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.DashboardList" title="Permalink to this definition">¶</a></dt>
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
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dash_items</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DashboardListDashItemArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – An individual dashboard object to add to this Dashboard List. If present, must contain the following:</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this Dashboard List.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_datadog.DashboardList.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">dash_items</span><span class="p">:</span> <span class="n">Union[List[Union[DashboardListDashItemArgs, Mapping[str, Any], Awaitable[Union[DashboardListDashItemArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[DashboardListDashItemArgs, Mapping[str, Any], Awaitable[Union[DashboardListDashItemArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.dashboard_list.DashboardList<a class="headerlink" href="#pulumi_datadog.DashboardList.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DashboardList resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dash_items</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DashboardListDashItemArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – An individual dashboard object to add to this Dashboard List. If present, must contain the following:</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this Dashboard List.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.DashboardList.dash_items">
<em class="property">property </em><code class="sig-name descname">dash_items</code><a class="headerlink" href="#pulumi_datadog.DashboardList.dash_items" title="Permalink to this definition">¶</a></dt>
<dd><p>An individual dashboard object to add to this Dashboard List. If present, must contain the following:</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.DashboardList.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_datadog.DashboardList.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of this Dashboard List.</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">Downtime</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">active</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_date</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitor_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitor_tags</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recurrence</span><span class="p">:</span> <span class="n">Union[DowntimeRecurrenceArgs, Mapping[str, Any], Awaitable[Union[DowntimeRecurrenceArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scopes</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_date</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timezone</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.Downtime" title="Permalink to this definition">¶</a></dt>
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
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>active</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A flag indicating if the downtime is active now.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A flag indicating if the downtime was disabled.</p></li>
<li><p><strong>end</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – POSIX timestamp to end the downtime.</p></li>
<li><p><strong>end_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String representing date and time to end the downtime in RFC3339 format.</p></li>
<li><p><strong>message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A message to include with notifications for this downtime.</p></li>
<li><p><strong>monitor_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Reference to which monitor this downtime is applied. When scheduling downtime for a given monitor, datadog changes <code class="docutils literal notranslate"><span class="pre">silenced</span></code> property of the monitor to match the <code class="docutils literal notranslate"><span class="pre">end</span></code> POSIX timestamp. <strong>Note:</strong> this will effectively change the <code class="docutils literal notranslate"><span class="pre">silenced</span></code> attribute of the referenced monitor. If that monitor is also tracked by this provider and you don’t want it to be unmuted on the next <code class="docutils literal notranslate"><span class="pre">pulumi</span> <span class="pre">up</span></code>, see <code class="docutils literal notranslate"><span class="pre">silencing-by-hand-and-by-downtimes</span></code> in the monitor resource documentation. This option also conflicts with <code class="docutils literal notranslate"><span class="pre">monitor_tags</span></code> use none or one or the other.</p></li>
<li><p><strong>monitor_tags</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of monitor tags to match. The resulting downtime applies to monitors that match <strong>all</strong> provided monitor tags. This option conflicts with <code class="docutils literal notranslate"><span class="pre">monitor_id</span></code> as it will match all monitors that match these tags.</p></li>
<li><p><strong>recurrence</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DowntimeRecurrenceArgs'</em><em>]</em><em>]</em>) – A dictionary to configure the downtime to be recurring.</p></li>
<li><p><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The scope(s) to which the downtime applies, e.g. host:app2. Provide multiple scopes as a comma-separated list, e.g. env:dev,env:prod. The resulting downtime applies to sources that matches ALL provided scopes (i.e. env:dev AND env:prod), NOT any of them.</p></li>
<li><p><strong>start</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – POSIX timestamp to start the downtime.</p></li>
<li><p><strong>start_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String representing date and time to start the downtime in RFC3339 format.</p></li>
<li><p><strong>timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The timezone for the downtime, default UTC. It must be a valid IANA Time Zone.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_datadog.Downtime.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">active</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">end_date</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitor_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitor_tags</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recurrence</span><span class="p">:</span> <span class="n">Union[DowntimeRecurrenceArgs, Mapping[str, Any], Awaitable[Union[DowntimeRecurrenceArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scopes</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_date</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timezone</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.downtime.Downtime<a class="headerlink" href="#pulumi_datadog.Downtime.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Downtime resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>active</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A flag indicating if the downtime is active now.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A flag indicating if the downtime was disabled.</p></li>
<li><p><strong>end</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – POSIX timestamp to end the downtime.</p></li>
<li><p><strong>end_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String representing date and time to end the downtime in RFC3339 format.</p></li>
<li><p><strong>message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A message to include with notifications for this downtime.</p></li>
<li><p><strong>monitor_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Reference to which monitor this downtime is applied. When scheduling downtime for a given monitor, datadog changes <code class="docutils literal notranslate"><span class="pre">silenced</span></code> property of the monitor to match the <code class="docutils literal notranslate"><span class="pre">end</span></code> POSIX timestamp. <strong>Note:</strong> this will effectively change the <code class="docutils literal notranslate"><span class="pre">silenced</span></code> attribute of the referenced monitor. If that monitor is also tracked by this provider and you don’t want it to be unmuted on the next <code class="docutils literal notranslate"><span class="pre">pulumi</span> <span class="pre">up</span></code>, see <code class="docutils literal notranslate"><span class="pre">silencing-by-hand-and-by-downtimes</span></code> in the monitor resource documentation. This option also conflicts with <code class="docutils literal notranslate"><span class="pre">monitor_tags</span></code> use none or one or the other.</p></li>
<li><p><strong>monitor_tags</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of monitor tags to match. The resulting downtime applies to monitors that match <strong>all</strong> provided monitor tags. This option conflicts with <code class="docutils literal notranslate"><span class="pre">monitor_id</span></code> as it will match all monitors that match these tags.</p></li>
<li><p><strong>recurrence</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DowntimeRecurrenceArgs'</em><em>]</em><em>]</em>) – A dictionary to configure the downtime to be recurring.</p></li>
<li><p><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The scope(s) to which the downtime applies, e.g. host:app2. Provide multiple scopes as a comma-separated list, e.g. env:dev,env:prod. The resulting downtime applies to sources that matches ALL provided scopes (i.e. env:dev AND env:prod), NOT any of them.</p></li>
<li><p><strong>start</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – POSIX timestamp to start the downtime.</p></li>
<li><p><strong>start_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – String representing date and time to start the downtime in RFC3339 format.</p></li>
<li><p><strong>timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The timezone for the downtime, default UTC. It must be a valid IANA Time Zone.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Downtime.active">
<em class="property">property </em><code class="sig-name descname">active</code><a class="headerlink" href="#pulumi_datadog.Downtime.active" title="Permalink to this definition">¶</a></dt>
<dd><p>A flag indicating if the downtime is active now.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Downtime.disabled">
<em class="property">property </em><code class="sig-name descname">disabled</code><a class="headerlink" href="#pulumi_datadog.Downtime.disabled" title="Permalink to this definition">¶</a></dt>
<dd><p>A flag indicating if the downtime was disabled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Downtime.end">
<em class="property">property </em><code class="sig-name descname">end</code><a class="headerlink" href="#pulumi_datadog.Downtime.end" title="Permalink to this definition">¶</a></dt>
<dd><p>POSIX timestamp to end the downtime.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Downtime.end_date">
<em class="property">property </em><code class="sig-name descname">end_date</code><a class="headerlink" href="#pulumi_datadog.Downtime.end_date" title="Permalink to this definition">¶</a></dt>
<dd><p>String representing date and time to end the downtime in RFC3339 format.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Downtime.message">
<em class="property">property </em><code class="sig-name descname">message</code><a class="headerlink" href="#pulumi_datadog.Downtime.message" title="Permalink to this definition">¶</a></dt>
<dd><p>A message to include with notifications for this downtime.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Downtime.monitor_id">
<em class="property">property </em><code class="sig-name descname">monitor_id</code><a class="headerlink" href="#pulumi_datadog.Downtime.monitor_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Reference to which monitor this downtime is applied. When scheduling downtime for a given monitor, datadog changes <code class="docutils literal notranslate"><span class="pre">silenced</span></code> property of the monitor to match the <code class="docutils literal notranslate"><span class="pre">end</span></code> POSIX timestamp. <strong>Note:</strong> this will effectively change the <code class="docutils literal notranslate"><span class="pre">silenced</span></code> attribute of the referenced monitor. If that monitor is also tracked by this provider and you don’t want it to be unmuted on the next <code class="docutils literal notranslate"><span class="pre">pulumi</span> <span class="pre">up</span></code>, see <code class="docutils literal notranslate"><span class="pre">silencing-by-hand-and-by-downtimes</span></code> in the monitor resource documentation. This option also conflicts with <code class="docutils literal notranslate"><span class="pre">monitor_tags</span></code> use none or one or the other.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Downtime.monitor_tags">
<em class="property">property </em><code class="sig-name descname">monitor_tags</code><a class="headerlink" href="#pulumi_datadog.Downtime.monitor_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of monitor tags to match. The resulting downtime applies to monitors that match <strong>all</strong> provided monitor tags. This option conflicts with <code class="docutils literal notranslate"><span class="pre">monitor_id</span></code> as it will match all monitors that match these tags.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Downtime.recurrence">
<em class="property">property </em><code class="sig-name descname">recurrence</code><a class="headerlink" href="#pulumi_datadog.Downtime.recurrence" title="Permalink to this definition">¶</a></dt>
<dd><p>A dictionary to configure the downtime to be recurring.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Downtime.scopes">
<em class="property">property </em><code class="sig-name descname">scopes</code><a class="headerlink" href="#pulumi_datadog.Downtime.scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>The scope(s) to which the downtime applies, e.g. host:app2. Provide multiple scopes as a comma-separated list, e.g. env:dev,env:prod. The resulting downtime applies to sources that matches ALL provided scopes (i.e. env:dev AND env:prod), NOT any of them.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Downtime.start">
<em class="property">property </em><code class="sig-name descname">start</code><a class="headerlink" href="#pulumi_datadog.Downtime.start" title="Permalink to this definition">¶</a></dt>
<dd><p>POSIX timestamp to start the downtime.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Downtime.start_date">
<em class="property">property </em><code class="sig-name descname">start_date</code><a class="headerlink" href="#pulumi_datadog.Downtime.start_date" title="Permalink to this definition">¶</a></dt>
<dd><p>String representing date and time to start the downtime in RFC3339 format.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Downtime.timezone">
<em class="property">property </em><code class="sig-name descname">timezone</code><a class="headerlink" href="#pulumi_datadog.Downtime.timezone" title="Permalink to this definition">¶</a></dt>
<dd><p>The timezone for the downtime, default UTC. It must be a valid IANA Time Zone.</p>
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
<dt id="pulumi_datadog.GetIpRangesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">GetIpRangesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">agents_ipv4s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">agents_ipv6s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_ipv4s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_ipv6s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">apm_ipv4s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">apm_ipv6s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logs_ipv4s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logs_ipv6s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">process_ipv4s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">process_ipv6s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">synthetics_ipv4s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">synthetics_ipv6s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">webhooks_ipv4s</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">webhooks_ipv6s</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.GetIpRangesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getIpRanges.</p>
<dl class="py method">
<dt id="pulumi_datadog.GetIpRangesResult.agents_ipv4s">
<em class="property">property </em><code class="sig-name descname">agents_ipv4s</code><a class="headerlink" href="#pulumi_datadog.GetIpRangesResult.agents_ipv4s" title="Permalink to this definition">¶</a></dt>
<dd><p>An Array of IPv4 addresses in CIDR format specifying the A records for the agent endpoint.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.GetIpRangesResult.agents_ipv6s">
<em class="property">property </em><code class="sig-name descname">agents_ipv6s</code><a class="headerlink" href="#pulumi_datadog.GetIpRangesResult.agents_ipv6s" title="Permalink to this definition">¶</a></dt>
<dd><p>An Array of IPv6 addresses in CIDR format specifying the A records for the agent endpoint.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.GetIpRangesResult.api_ipv4s">
<em class="property">property </em><code class="sig-name descname">api_ipv4s</code><a class="headerlink" href="#pulumi_datadog.GetIpRangesResult.api_ipv4s" title="Permalink to this definition">¶</a></dt>
<dd><p>An Array of IPv4 addresses in CIDR format specifying the A records for the api endpoint.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.GetIpRangesResult.api_ipv6s">
<em class="property">property </em><code class="sig-name descname">api_ipv6s</code><a class="headerlink" href="#pulumi_datadog.GetIpRangesResult.api_ipv6s" title="Permalink to this definition">¶</a></dt>
<dd><p>An Array of IPv6 addresses in CIDR format specifying the A records for the api endpoint.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.GetIpRangesResult.apm_ipv4s">
<em class="property">property </em><code class="sig-name descname">apm_ipv4s</code><a class="headerlink" href="#pulumi_datadog.GetIpRangesResult.apm_ipv4s" title="Permalink to this definition">¶</a></dt>
<dd><p>An Array of IPv4 addresses in CIDR format specifying the A records for the apm endpoint.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.GetIpRangesResult.apm_ipv6s">
<em class="property">property </em><code class="sig-name descname">apm_ipv6s</code><a class="headerlink" href="#pulumi_datadog.GetIpRangesResult.apm_ipv6s" title="Permalink to this definition">¶</a></dt>
<dd><p>An Array of IPv6 addresses in CIDR format specifying the A records for the apm endpoint.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.GetIpRangesResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_datadog.GetIpRangesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.GetIpRangesResult.logs_ipv4s">
<em class="property">property </em><code class="sig-name descname">logs_ipv4s</code><a class="headerlink" href="#pulumi_datadog.GetIpRangesResult.logs_ipv4s" title="Permalink to this definition">¶</a></dt>
<dd><p>An Array of IPv4 addresses in CIDR format specifying the A records for the logs endpoint.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.GetIpRangesResult.logs_ipv6s">
<em class="property">property </em><code class="sig-name descname">logs_ipv6s</code><a class="headerlink" href="#pulumi_datadog.GetIpRangesResult.logs_ipv6s" title="Permalink to this definition">¶</a></dt>
<dd><p>An Array of IPv6 addresses in CIDR format specifying the A records for the logs endpoint.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.GetIpRangesResult.process_ipv4s">
<em class="property">property </em><code class="sig-name descname">process_ipv4s</code><a class="headerlink" href="#pulumi_datadog.GetIpRangesResult.process_ipv4s" title="Permalink to this definition">¶</a></dt>
<dd><p>An Array of IPv4 addresses in CIDR format specifying the A records for the process endpoint.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.GetIpRangesResult.process_ipv6s">
<em class="property">property </em><code class="sig-name descname">process_ipv6s</code><a class="headerlink" href="#pulumi_datadog.GetIpRangesResult.process_ipv6s" title="Permalink to this definition">¶</a></dt>
<dd><p>An Array of IPv6 addresses in CIDR format specifying the A records for the process endpoint.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.GetIpRangesResult.synthetics_ipv4s">
<em class="property">property </em><code class="sig-name descname">synthetics_ipv4s</code><a class="headerlink" href="#pulumi_datadog.GetIpRangesResult.synthetics_ipv4s" title="Permalink to this definition">¶</a></dt>
<dd><p>An Array of IPv4 addresses in CIDR format specifying the A records for the synthetics endpoint.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.GetIpRangesResult.synthetics_ipv6s">
<em class="property">property </em><code class="sig-name descname">synthetics_ipv6s</code><a class="headerlink" href="#pulumi_datadog.GetIpRangesResult.synthetics_ipv6s" title="Permalink to this definition">¶</a></dt>
<dd><p>An Array of IPv6 addresses in CIDR format specifying the A records for the synthetics endpoint.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.GetIpRangesResult.webhooks_ipv4s">
<em class="property">property </em><code class="sig-name descname">webhooks_ipv4s</code><a class="headerlink" href="#pulumi_datadog.GetIpRangesResult.webhooks_ipv4s" title="Permalink to this definition">¶</a></dt>
<dd><p>An Array of IPv4 addresses in CIDR format specifying the A records for the webhooks endpoint.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.GetIpRangesResult.webhooks_ipv6s">
<em class="property">property </em><code class="sig-name descname">webhooks_ipv6s</code><a class="headerlink" href="#pulumi_datadog.GetIpRangesResult.webhooks_ipv6s" title="Permalink to this definition">¶</a></dt>
<dd><p>An Array of IPv6 addresses in CIDR format specifying the A records for the webhooks endpoint.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_datadog.GetMonitorResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">GetMonitorResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">enable_logs_sample</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">escalation_message</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">evaluation_delay</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">include_tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locked</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitor_tags_filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">new_host_delay</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">no_data_timeframe</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_audit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_no_data</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">renotify_interval</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">require_full_window</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags_filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">threshold_windows</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">thresholds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout_h</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.GetMonitorResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getMonitor.</p>
<dl class="py method">
<dt id="pulumi_datadog.GetMonitorResult.enable_logs_sample">
<em class="property">property </em><code class="sig-name descname">enable_logs_sample</code><a class="headerlink" href="#pulumi_datadog.GetMonitorResult.enable_logs_sample" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not a list of log values which triggered the alert is included. This is only used by log monitors.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.GetMonitorResult.escalation_message">
<em class="property">property </em><code class="sig-name descname">escalation_message</code><a class="headerlink" href="#pulumi_datadog.GetMonitorResult.escalation_message" title="Permalink to this definition">¶</a></dt>
<dd><p>Message included with a re-notification for this monitor.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.GetMonitorResult.evaluation_delay">
<em class="property">property </em><code class="sig-name descname">evaluation_delay</code><a class="headerlink" href="#pulumi_datadog.GetMonitorResult.evaluation_delay" title="Permalink to this definition">¶</a></dt>
<dd><p>Time (in seconds) for which evaluation is delayed. This is only used by metric monitors.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.GetMonitorResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_datadog.GetMonitorResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.GetMonitorResult.include_tags">
<em class="property">property </em><code class="sig-name descname">include_tags</code><a class="headerlink" href="#pulumi_datadog.GetMonitorResult.include_tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not notifications from the monitor automatically inserts its triggering tags into the title.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.GetMonitorResult.locked">
<em class="property">property </em><code class="sig-name descname">locked</code><a class="headerlink" href="#pulumi_datadog.GetMonitorResult.locked" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not changes to the monitor are restricted to the creator or admins.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.GetMonitorResult.message">
<em class="property">property </em><code class="sig-name descname">message</code><a class="headerlink" href="#pulumi_datadog.GetMonitorResult.message" title="Permalink to this definition">¶</a></dt>
<dd><p>Message included with notifications for this monitor.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.GetMonitorResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_datadog.GetMonitorResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the monitor.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.GetMonitorResult.new_host_delay">
<em class="property">property </em><code class="sig-name descname">new_host_delay</code><a class="headerlink" href="#pulumi_datadog.GetMonitorResult.new_host_delay" title="Permalink to this definition">¶</a></dt>
<dd><p>Time (in seconds) allowing a host to boot and
applications to fully start before starting the evaluation of monitor
results.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.GetMonitorResult.no_data_timeframe">
<em class="property">property </em><code class="sig-name descname">no_data_timeframe</code><a class="headerlink" href="#pulumi_datadog.GetMonitorResult.no_data_timeframe" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of minutes before the monitor notifies when data stops reporting.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.GetMonitorResult.notify_audit">
<em class="property">property </em><code class="sig-name descname">notify_audit</code><a class="headerlink" href="#pulumi_datadog.GetMonitorResult.notify_audit" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not tagged users are notified on changes to the monitor.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.GetMonitorResult.notify_no_data">
<em class="property">property </em><code class="sig-name descname">notify_no_data</code><a class="headerlink" href="#pulumi_datadog.GetMonitorResult.notify_no_data" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not this monitor notifies when data stops reporting.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.GetMonitorResult.query">
<em class="property">property </em><code class="sig-name descname">query</code><a class="headerlink" href="#pulumi_datadog.GetMonitorResult.query" title="Permalink to this definition">¶</a></dt>
<dd><p>Query of the monitor.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.GetMonitorResult.renotify_interval">
<em class="property">property </em><code class="sig-name descname">renotify_interval</code><a class="headerlink" href="#pulumi_datadog.GetMonitorResult.renotify_interval" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of minutes after the last notification before the monitor re-notifies on the current status.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.GetMonitorResult.require_full_window">
<em class="property">property </em><code class="sig-name descname">require_full_window</code><a class="headerlink" href="#pulumi_datadog.GetMonitorResult.require_full_window" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not the monitor needs a full window of data before it is evaluated.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.GetMonitorResult.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_datadog.GetMonitorResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>List of tags associated with the monitor.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.GetMonitorResult.threshold_windows">
<em class="property">property </em><code class="sig-name descname">threshold_windows</code><a class="headerlink" href="#pulumi_datadog.GetMonitorResult.threshold_windows" title="Permalink to this definition">¶</a></dt>
<dd><p>Mapping containing <code class="docutils literal notranslate"><span class="pre">recovery_window</span></code> and <code class="docutils literal notranslate"><span class="pre">trigger_window</span></code> values, e.g. <code class="docutils literal notranslate"><span class="pre">last_15m</span></code>. This is only used by anomaly monitors.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.GetMonitorResult.thresholds">
<em class="property">property </em><code class="sig-name descname">thresholds</code><a class="headerlink" href="#pulumi_datadog.GetMonitorResult.thresholds" title="Permalink to this definition">¶</a></dt>
<dd><p>Alert thresholds of the monitor.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.GetMonitorResult.timeout_h">
<em class="property">property </em><code class="sig-name descname">timeout_h</code><a class="headerlink" href="#pulumi_datadog.GetMonitorResult.timeout_h" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of hours of the monitor not reporting data before it automatically resolves from a triggered state.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.GetMonitorResult.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_datadog.GetMonitorResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of the monitor.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_datadog.LogsArchive">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">LogsArchive</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azure</span><span class="p">:</span> <span class="n">Union[LogsArchiveAzureArgs, Mapping[str, Any], Awaitable[Union[LogsArchiveAzureArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gcs</span><span class="p">:</span> <span class="n">Union[LogsArchiveGcsArgs, Mapping[str, Any], Awaitable[Union[LogsArchiveGcsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">s3</span><span class="p">:</span> <span class="n">Union[LogsArchiveS3Args, Mapping[str, Any], Awaitable[Union[LogsArchiveS3Args, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.LogsArchive" title="Permalink to this definition">¶</a></dt>
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
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>azure</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LogsArchiveAzureArgs'</em><em>]</em><em>]</em>) – Definition of an azure archive.</p></li>
<li><p><strong>gcs</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LogsArchiveGcsArgs'</em><em>]</em><em>]</em>) – Definition of an gcs archive.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your archive name.</p></li>
<li><p><strong>query</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The archive query/filter. Logs matching this query are included in the archive.</p></li>
<li><p><strong>s3</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LogsArchiveS3Args'</em><em>]</em><em>]</em>) – Definition of an s3 archive.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_datadog.LogsArchive.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azure</span><span class="p">:</span> <span class="n">Union[LogsArchiveAzureArgs, Mapping[str, Any], Awaitable[Union[LogsArchiveAzureArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gcs</span><span class="p">:</span> <span class="n">Union[LogsArchiveGcsArgs, Mapping[str, Any], Awaitable[Union[LogsArchiveGcsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">s3</span><span class="p">:</span> <span class="n">Union[LogsArchiveS3Args, Mapping[str, Any], Awaitable[Union[LogsArchiveS3Args, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.logs_archive.LogsArchive<a class="headerlink" href="#pulumi_datadog.LogsArchive.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LogsArchive resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>azure</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LogsArchiveAzureArgs'</em><em>]</em><em>]</em>) – Definition of an azure archive.</p></li>
<li><p><strong>gcs</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LogsArchiveGcsArgs'</em><em>]</em><em>]</em>) – Definition of an gcs archive.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your archive name.</p></li>
<li><p><strong>query</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The archive query/filter. Logs matching this query are included in the archive.</p></li>
<li><p><strong>s3</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LogsArchiveS3Args'</em><em>]</em><em>]</em>) – Definition of an s3 archive.</p></li>
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
<dt id="pulumi_datadog.LogsArchive.gcs">
<em class="property">property </em><code class="sig-name descname">gcs</code><a class="headerlink" href="#pulumi_datadog.LogsArchive.gcs" title="Permalink to this definition">¶</a></dt>
<dd><p>Definition of an gcs archive.</p>
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
<dt id="pulumi_datadog.LogsArchive.s3">
<em class="property">property </em><code class="sig-name descname">s3</code><a class="headerlink" href="#pulumi_datadog.LogsArchive.s3" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_datadog.LogsCustomPipeline">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">LogsCustomPipeline</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="p">:</span> <span class="n">Union[List[Union[LogsCustomPipelineFilterArgs, Mapping[str, Any], Awaitable[Union[LogsCustomPipelineFilterArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[LogsCustomPipelineFilterArgs, Mapping[str, Any], Awaitable[Union[LogsCustomPipelineFilterArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">processors</span><span class="p">:</span> <span class="n">Union[List[Union[LogsCustomPipelineProcessorArgs, Mapping[str, Any], Awaitable[Union[LogsCustomPipelineProcessorArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[LogsCustomPipelineProcessorArgs, Mapping[str, Any], Awaitable[Union[LogsCustomPipelineProcessorArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.LogsCustomPipeline" title="Permalink to this definition">¶</a></dt>
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
                <span class="n">target_type</span><span class="o">=</span><span class="s2">&quot;tag&quot;</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">LogsCustomPipelineProcessorArgs</span><span class="p">(</span>
            <span class="n">category_processor</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">LogsCustomPipelineProcessorCategoryProcessorArgs</span><span class="p">(</span>
                <span class="n">category</span><span class="o">=</span><span class="p">[</span>
                    <span class="p">{</span>
                        <span class="s2">&quot;filter&quot;</span><span class="p">:</span> <span class="p">[{</span>
                            <span class="s2">&quot;query&quot;</span><span class="p">:</span> <span class="s2">&quot;@severity: &quot;</span><span class="o">.</span><span class="s2">&quot;&quot;</span><span class="p">,</span>
                        <span class="p">}],</span>
                        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;debug&quot;</span><span class="p">,</span>
                    <span class="p">},</span>
                    <span class="p">{</span>
                        <span class="s2">&quot;filter&quot;</span><span class="p">:</span> <span class="p">[{</span>
                            <span class="s2">&quot;query&quot;</span><span class="p">:</span> <span class="s2">&quot;@severity: &quot;</span><span class="o">-</span><span class="s2">&quot;&quot;</span><span class="p">,</span>
                        <span class="p">}],</span>
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
<p>Each <code class="docutils literal notranslate"><span class="pre">LogsCustomPipeline</span></code> resource defines a complete pipeline. The order of the pipelines is maintained in
a different resource datadog_logs_pipeline_order.
When creating a new pipeline, you need to <strong>explicitly</strong> add this pipeline to the <code class="docutils literal notranslate"><span class="pre">LogsPipelineOrder</span></code>
resource to track the pipeline. Similarly, when a pipeline needs to be destroyed, remove its references from the
<code class="docutils literal notranslate"><span class="pre">LogsPipelineOrder</span></code> resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>filters</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LogsCustomPipelineFilterArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Defines the nested pipeline filter. Only logs that match the filter criteria are processed by this pipeline.</p></li>
<li><p><strong>is_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If the processor is enabled or not.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the processor</p></li>
<li><p><strong>processors</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LogsCustomPipelineProcessorArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Processors. Nested pipeline can’t take any other nested pipeline as its processor.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_datadog.LogsCustomPipeline.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="p">:</span> <span class="n">Union[List[Union[LogsCustomPipelineFilterArgs, Mapping[str, Any], Awaitable[Union[LogsCustomPipelineFilterArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[LogsCustomPipelineFilterArgs, Mapping[str, Any], Awaitable[Union[LogsCustomPipelineFilterArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">processors</span><span class="p">:</span> <span class="n">Union[List[Union[LogsCustomPipelineProcessorArgs, Mapping[str, Any], Awaitable[Union[LogsCustomPipelineProcessorArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[LogsCustomPipelineProcessorArgs, Mapping[str, Any], Awaitable[Union[LogsCustomPipelineProcessorArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.logs_custom_pipeline.LogsCustomPipeline<a class="headerlink" href="#pulumi_datadog.LogsCustomPipeline.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LogsCustomPipeline resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>filters</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LogsCustomPipelineFilterArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Defines the nested pipeline filter. Only logs that match the filter criteria are processed by this pipeline.</p></li>
<li><p><strong>is_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If the processor is enabled or not.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the processor</p></li>
<li><p><strong>processors</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LogsCustomPipelineProcessorArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Processors. Nested pipeline can’t take any other nested pipeline as its processor.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.LogsCustomPipeline.filters">
<em class="property">property </em><code class="sig-name descname">filters</code><a class="headerlink" href="#pulumi_datadog.LogsCustomPipeline.filters" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines the nested pipeline filter. Only logs that match the filter criteria are processed by this pipeline.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.LogsCustomPipeline.is_enabled">
<em class="property">property </em><code class="sig-name descname">is_enabled</code><a class="headerlink" href="#pulumi_datadog.LogsCustomPipeline.is_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>If the processor is enabled or not.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.LogsCustomPipeline.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_datadog.LogsCustomPipeline.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the processor</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.LogsCustomPipeline.processors">
<em class="property">property </em><code class="sig-name descname">processors</code><a class="headerlink" href="#pulumi_datadog.LogsCustomPipeline.processors" title="Permalink to this definition">¶</a></dt>
<dd><p>Processors. Nested pipeline can’t take any other nested pipeline as its processor.</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">LogsIndex</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">exclusion_filters</span><span class="p">:</span> <span class="n">Union[List[Union[LogsIndexExclusionFilterArgs, Mapping[str, Any], Awaitable[Union[LogsIndexExclusionFilterArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[LogsIndexExclusionFilterArgs, Mapping[str, Any], Awaitable[Union[LogsIndexExclusionFilterArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="p">:</span> <span class="n">Union[List[Union[LogsIndexFilterArgs, Mapping[str, Any], Awaitable[Union[LogsIndexFilterArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[LogsIndexFilterArgs, Mapping[str, Any], Awaitable[Union[LogsIndexFilterArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.LogsIndex" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Datadog <a class="reference external" href="https://docs.datadoghq.com/api/v1/logs-indexes/">Logs Index API</a> resource. This can be used to create and manage Datadog logs indexes.</p>
<p>A sample Datadog logs index resource definition. Note that at this point, it is not possible to create new logs indexes
through this provider, so the <code class="docutils literal notranslate"><span class="pre">name</span></code> field must match a name of an already existing index. If you want to keep the current
state of the index, we suggest importing it (see below).</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="n">sample_index</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">LogsIndex</span><span class="p">(</span><span class="s2">&quot;sampleIndex&quot;</span><span class="p">,</span>
    <span class="n">exclusion_filters</span><span class="o">=</span><span class="p">[</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">LogsIndexExclusionFilterArgs</span><span class="p">(</span>
            <span class="n">filters</span><span class="o">=</span><span class="p">[</span><span class="n">datadog</span><span class="o">.</span><span class="n">LogsIndexExclusionFilterFilterArgs</span><span class="p">(</span>
                <span class="n">query</span><span class="o">=</span><span class="s2">&quot;app:coredns&quot;</span><span class="p">,</span>
                <span class="n">sample_rate</span><span class="o">=</span><span class="mf">0.97</span><span class="p">,</span>
            <span class="p">)],</span>
            <span class="n">is_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Filter coredns logs&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">LogsIndexExclusionFilterArgs</span><span class="p">(</span>
            <span class="n">filters</span><span class="o">=</span><span class="p">[</span><span class="n">datadog</span><span class="o">.</span><span class="n">LogsIndexExclusionFilterFilterArgs</span><span class="p">(</span>
                <span class="n">query</span><span class="o">=</span><span class="s2">&quot;service:kube_apiserver&quot;</span><span class="p">,</span>
                <span class="n">sample_rate</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
            <span class="p">)],</span>
            <span class="n">is_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Kubernetes apiserver&quot;</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">],</span>
    <span class="n">filters</span><span class="o">=</span><span class="p">[</span><span class="n">datadog</span><span class="o">.</span><span class="n">LogsIndexFilterArgs</span><span class="p">(</span>
        <span class="n">query</span><span class="o">=</span><span class="s2">&quot;*&quot;</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;your index&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>The order of indexes is maintained in the separated resource datadog_logs_index_order.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>exclusion_filters</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LogsIndexExclusionFilterArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – List of exclusion filters.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the exclusion filter.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_datadog.LogsIndex.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">exclusion_filters</span><span class="p">:</span> <span class="n">Union[List[Union[LogsIndexExclusionFilterArgs, Mapping[str, Any], Awaitable[Union[LogsIndexExclusionFilterArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[LogsIndexExclusionFilterArgs, Mapping[str, Any], Awaitable[Union[LogsIndexExclusionFilterArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">filters</span><span class="p">:</span> <span class="n">Union[List[Union[LogsIndexFilterArgs, Mapping[str, Any], Awaitable[Union[LogsIndexFilterArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[LogsIndexFilterArgs, Mapping[str, Any], Awaitable[Union[LogsIndexFilterArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.logs_index.LogsIndex<a class="headerlink" href="#pulumi_datadog.LogsIndex.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LogsIndex resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>exclusion_filters</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'LogsIndexExclusionFilterArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – List of exclusion filters.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the exclusion filter.</p></li>
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
<dt id="pulumi_datadog.LogsIndex.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_datadog.LogsIndex.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the exclusion filter.</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">LogsIndexOrder</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">indexes</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.LogsIndexOrder" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Datadog <a class="reference external" href="https://docs.datadoghq.com/api/v1/logs-indexes/">Logs Index API</a> resource. This can be used to manage the order of Datadog logs indexes.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="n">sample_index_order</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">LogsIndexOrder</span><span class="p">(</span><span class="s2">&quot;sampleIndexOrder&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;sample_index_order&quot;</span><span class="p">,</span>
    <span class="n">indexes</span><span class="o">=</span><span class="p">[</span><span class="n">datadog_logs_index</span><span class="p">[</span><span class="s2">&quot;sample_index&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">]],</span>
    <span class="n">opts</span><span class="o">=</span><span class="n">ResourceOptions</span><span class="p">(</span><span class="n">depends_on</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;datadog_logs_index.sample_index&quot;</span><span class="p">]))</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>indexes</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The index resource list. Logs are tested against the query filter of each index one by one following the order of the list.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique name of the index order resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_datadog.LogsIndexOrder.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">indexes</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.logs_index_order.LogsIndexOrder<a class="headerlink" href="#pulumi_datadog.LogsIndexOrder.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LogsIndexOrder resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>indexes</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The index resource list. Logs are tested against the query filter of each index one by one following the order of the list.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique name of the index order resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.LogsIndexOrder.indexes">
<em class="property">property </em><code class="sig-name descname">indexes</code><a class="headerlink" href="#pulumi_datadog.LogsIndexOrder.indexes" title="Permalink to this definition">¶</a></dt>
<dd><p>The index resource list. Logs are tested against the query filter of each index one by one following the order of the list.</p>
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
<dd><p>Provides a Datadog <a class="reference external" href="https://docs.datadoghq.com/api/v1/logs-pipelines/">Logs Pipeline API</a> resource to manage
the <a class="reference external" href="https://docs.datadoghq.com/logs/log_collection/?tab=tcpussite">integrations</a>.</p>
<p>Integration pipelines are the pipelines that are automatically installed for your organization when sending the logs with
specific sources. You don’t need to maintain or update these types of pipelines. Keeping them as resources, however,
allows you to manage the order of your pipelines by referencing them in your
LogsPipelineOrder resource. If you don’t need the
<code class="docutils literal notranslate"><span class="pre">pipeline_order</span></code> feature, this resource declaration can be omitted.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="n">python</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">LogsIntegrationPipeline</span><span class="p">(</span><span class="s2">&quot;python&quot;</span><span class="p">,</span> <span class="n">is_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
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
<dt id="pulumi_datadog.LogsPipelineOrder">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">LogsPipelineOrder</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pipelines</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.LogsPipelineOrder" title="Permalink to this definition">¶</a></dt>
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
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name attribute in the resource <code class="docutils literal notranslate"><span class="pre">LogsPipelineOrder</span></code> needs to be unique. It’s recommended to use the same value as the resource <code class="docutils literal notranslate"><span class="pre">NAME</span></code>.
No related field is available in  <a class="reference external" href="https://docs.datadoghq.com/api/v1/logs-pipelines/#get-pipeline-orderr">Logs Pipeline API</a>.</p>
</p></li>
<li><p><strong>pipelines</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The pipeline IDs list. The order of pipeline IDs in this attribute defines the overall pipeline order for logs.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_datadog.LogsPipelineOrder.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pipelines</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.logs_pipeline_order.LogsPipelineOrder<a class="headerlink" href="#pulumi_datadog.LogsPipelineOrder.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LogsPipelineOrder resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name attribute in the resource <code class="docutils literal notranslate"><span class="pre">LogsPipelineOrder</span></code> needs to be unique. It’s recommended to use the same value as the resource <code class="docutils literal notranslate"><span class="pre">NAME</span></code>.
No related field is available in  <a class="reference external" href="https://docs.datadoghq.com/api/v1/logs-pipelines/#get-pipeline-orderr">Logs Pipeline API</a>.</p>
</p></li>
<li><p><strong>pipelines</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The pipeline IDs list. The order of pipeline IDs in this attribute defines the overall pipeline order for logs.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.LogsPipelineOrder.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_datadog.LogsPipelineOrder.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name attribute in the resource <code class="docutils literal notranslate"><span class="pre">LogsPipelineOrder</span></code> needs to be unique. It’s recommended to use the same value as the resource <code class="docutils literal notranslate"><span class="pre">NAME</span></code>.
No related field is available in  <a class="reference external" href="https://docs.datadoghq.com/api/v1/logs-pipelines/#get-pipeline-orderr">Logs Pipeline API</a>.</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">MetricMetadata</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">per_unit</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">short_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">statsd_interval</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">unit</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.MetricMetadata" title="Permalink to this definition">¶</a></dt>
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
<li><p><strong>per_unit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ‘Per’ unit of the metric such as ‘second’ in ‘bytes per second’.</p></li>
<li><p><strong>short_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A short name of the metric.</p></li>
<li><p><strong>statsd_interval</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If applicable, stasd flush interval in seconds for the metric.</p></li>
<li><p><strong>unit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Primary unit of the metric such as ‘byte’ or ‘operation’.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_datadog.MetricMetadata.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">per_unit</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">short_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">statsd_interval</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">unit</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.metric_metadata.MetricMetadata<a class="headerlink" href="#pulumi_datadog.MetricMetadata.get" title="Permalink to this definition">¶</a></dt>
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
<li><p><strong>per_unit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ‘Per’ unit of the metric such as ‘second’ in ‘bytes per second’.</p></li>
<li><p><strong>short_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A short name of the metric.</p></li>
<li><p><strong>statsd_interval</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – If applicable, stasd flush interval in seconds for the metric.</p></li>
<li><p><strong>unit</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Primary unit of the metric such as ‘byte’ or ‘operation’.</p></li>
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
<dd><p>‘Per’ unit of the metric such as ‘second’ in ‘bytes per second’.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.MetricMetadata.short_name">
<em class="property">property </em><code class="sig-name descname">short_name</code><a class="headerlink" href="#pulumi_datadog.MetricMetadata.short_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A short name of the metric.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.MetricMetadata.statsd_interval">
<em class="property">property </em><code class="sig-name descname">statsd_interval</code><a class="headerlink" href="#pulumi_datadog.MetricMetadata.statsd_interval" title="Permalink to this definition">¶</a></dt>
<dd><p>If applicable, stasd flush interval in seconds for the metric.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.MetricMetadata.unit">
<em class="property">property </em><code class="sig-name descname">unit</code><a class="headerlink" href="#pulumi_datadog.MetricMetadata.unit" title="Permalink to this definition">¶</a></dt>
<dd><p>Primary unit of the metric such as ‘byte’ or ‘operation’.</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">Monitor</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_logs_sample</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">escalation_message</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">evaluation_delay</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_delete</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">include_tags</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locked</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">new_host_delay</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">no_data_timeframe</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_audit</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_no_data</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">renotify_interval</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">require_full_window</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">silenced</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">threshold_windows</span><span class="p">:</span> <span class="n">Union[MonitorThresholdWindowsArgs, Mapping[str, Any], Awaitable[Union[MonitorThresholdWindowsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">thresholds</span><span class="p">:</span> <span class="n">Union[MonitorThresholdsArgs, Mapping[str, Any], Awaitable[Union[MonitorThresholdsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout_h</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.Monitor" title="Permalink to this definition">¶</a></dt>
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
<p>This issue doesn’t apply to multi-monitor downtimes (those that don’t contain <code class="docutils literal notranslate"><span class="pre">monitor_id</span></code>), as these don’t influence contents of the <code class="docutils literal notranslate"><span class="pre">silenced</span></code> attribute.</p>
<p>You can compose monitors of all types in order to define more specific alert conditions (see the <a class="reference external" href="https://docs.datadoghq.com/monitors/monitor_types/composite/">doc</a>).
You just need to reuse the ID of your <code class="docutils literal notranslate"><span class="pre">Monitor</span></code> resources.
You can also compose any monitor with a <code class="docutils literal notranslate"><span class="pre">SyntheticsTest</span></code> by passing the computed <code class="docutils literal notranslate"><span class="pre">monitor_id</span></code> attribute in the query.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="n">bar</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">Monitor</span><span class="p">(</span><span class="s2">&quot;bar&quot;</span><span class="p">,</span>
    <span class="n">message</span><span class="o">=</span><span class="s2">&quot;This is a message&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Composite Monitor&quot;</span><span class="p">,</span>
    <span class="n">query</span><span class="o">=</span><span class="sa">f</span><span class="s2">&quot;</span><span class="si">{</span><span class="n">datadog_monitor</span><span class="p">[</span><span class="s1">&#39;foo&#39;</span><span class="p">][</span><span class="s1">&#39;id&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2"> || </span><span class="si">{</span><span class="n">datadog_synthetics_test</span><span class="p">[</span><span class="s1">&#39;foo&#39;</span><span class="p">][</span><span class="s1">&#39;monitor_id&#39;</span><span class="p">]</span><span class="si">}</span><span class="s2">&quot;</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;composite&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enable_logs_sample</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether or not to include a list of log values which triggered the alert. Defaults to false. This is only used by log monitors.
triggering tags into the title. Defaults to true.</p></li>
<li><p><strong>escalation_message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A message to include with a re-notification. Supports the <a class="reference external" href="mailto:'&#37;&#52;&#48;username">‘<span>&#64;</span>username</a>’
notification allowed elsewhere.</p></li>
<li><p><strong>evaluation_delay</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Time (in seconds) to delay evaluation, as a non-negative integer.
For example, if the value is set to 300 (5min), the timeframe is set to last_5m and the time is 7:00,
the monitor will evaluate data from 6:50 to 6:55. This is useful for AWS CloudWatch and other backfilled
metrics to ensure the monitor will always have data during evaluation.</p></li>
<li><p><strong>force_delete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether this monitor can be deleted even if it’s referenced by other resources (e.g. SLO, composite monitor).</p></li>
<li><p><strong>include_tags</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether notifications from this monitor automatically insert its triggering tags into the title. Defaults to true.</p></li>
<li><p><strong>locked</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether changes to to this monitor should be restricted to the creator or admins. Defaults to False.</p></li>
<li><p><strong>message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A message to include with notifications for this monitor.
Email notifications can be sent to specific users by using the same <a class="reference external" href="mailto:'&#37;&#52;&#48;username">‘<span>&#64;</span>username</a>’ notation as events.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Datadog monitor</p></li>
<li><p><strong>new_host_delay</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Time (in seconds) to allow a host to boot and
applications to fully start before starting the evaluation of monitor
results. Should be a non negative integer. Defaults to 300.</p></li>
<li><p><strong>no_data_timeframe</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of minutes before a monitor will notify when data stops reporting. Provider defaults to 10 minutes.
We recommend at least 2x the monitor timeframe for metric alerts or 2 minutes for service checks.</p></li>
<li><p><strong>notify_audit</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether tagged users will be notified on changes to this monitor.
Defaults to false.</p></li>
<li><p><strong>notify_no_data</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether this monitor will notify when data stops reporting. Defaults
to false.</p></li>
<li><p><strong>query</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The monitor query to notify on. Note this is not the same query you see in the UI and
the syntax is different depending on the monitor <code class="docutils literal notranslate"><span class="pre">type</span></code>, please see the <a class="reference external" href="https://docs.datadoghq.com/api/v1/monitors/#create-a-monitor">API Reference</a> for details. <strong>Warning:</strong> <code class="docutils literal notranslate"><span class="pre">pulumi</span> <span class="pre">preview</span></code> won’t perform any validation of the query contents.</p></li>
<li><p><strong>renotify_interval</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of minutes after the last notification before a monitor will re-notify
on the current status. It will only re-notify if it’s not resolved.</p></li>
<li><p><strong>require_full_window</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether this monitor needs a full window of data before it’s evaluated.
We highly recommend you set this to False for sparse metrics, otherwise some evaluations will be skipped.
Default: True for “on average”, “at all times” and “in total” aggregation. False otherwise.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>silenced</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Each scope will be muted until the given POSIX timestamp or forever if the value is 0. Use <code class="docutils literal notranslate"><span class="pre">-1</span></code> if you want to unmute the scope. <strong>Deprecated</strong> The <code class="docutils literal notranslate"><span class="pre">silenced</span></code> parameter is being deprecated in favor of the downtime resource.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of tags to associate with your monitor. This can help you categorize and filter monitors in the manage monitors page of the UI. Note: it’s not currently possible to filter by these tags when querying via the API</p></li>
<li><p><strong>threshold_windows</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'MonitorThresholdWindowsArgs'</em><em>]</em><em>]</em>) – A mapping containing <code class="docutils literal notranslate"><span class="pre">recovery_window</span></code> and <code class="docutils literal notranslate"><span class="pre">trigger_window</span></code> values, e.g. <code class="docutils literal notranslate"><span class="pre">last_15m</span></code>. Can only be used for, and are required for, anomaly monitors.</p></li>
<li><p><strong>thresholds</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'MonitorThresholdsArgs'</em><em>]</em><em>]</em>) – <ul>
<li><p>Metric alerts:</p></li>
</ul>
<p>A dictionary of thresholds by threshold type. Currently we have four threshold types for metric alerts: critical, critical recovery, warning, and warning recovery. Critical is defined in the query, but can also be specified in this option. Warning and recovery thresholds can only be specified using the thresholds option.
Example usage:</p>
</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>```python
import pulumi
```
**Warning:** the `critical` threshold value must match the one contained in the `query` argument. The `threshold` from the previous example is valid along with a query like `avg(last_1h):avg:system.disk.in_use{role:sqlserver} by {host} &gt; 90` but
along with something like `avg(last_1h):avg:system.disk.in_use{role:sqlserver} by {host} &gt; 95` would make the Datadog API return a HTTP error 400, complaining &quot;The value provided for parameter &#39;query&#39; is invalid&quot;.
* Service checks:
A dictionary of thresholds by status. Because service checks can have multiple thresholds, we don&#39;t define them directly in the query.
Default values:
```python
import pulumi
```
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>timeout_h</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of hours of the monitor not reporting data before it will automatically resolve
from a triggered state. Defaults to false.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the monitor. The mapping from these types to the types found in the Datadog Web UI can be found in the Datadog API <a class="reference external" href="https://docs.datadoghq.com/api/v1/monitors/#create-a-monitor">documentation</a> page. The available options are below. <strong>Note</strong>: The monitor type cannot be changed after a monitor is created.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `metric alert`
* `service check`
* `event alert`
* `query alert`
* `composite`
* `log alert`
</pre></div>
</div>
<dl class="py method">
<dt id="pulumi_datadog.Monitor.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_logs_sample</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">escalation_message</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">evaluation_delay</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force_delete</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">include_tags</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locked</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">new_host_delay</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">no_data_timeframe</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_audit</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_no_data</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">renotify_interval</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">require_full_window</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">silenced</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">threshold_windows</span><span class="p">:</span> <span class="n">Union[MonitorThresholdWindowsArgs, Mapping[str, Any], Awaitable[Union[MonitorThresholdWindowsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">thresholds</span><span class="p">:</span> <span class="n">Union[MonitorThresholdsArgs, Mapping[str, Any], Awaitable[Union[MonitorThresholdsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timeout_h</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.monitor.Monitor<a class="headerlink" href="#pulumi_datadog.Monitor.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Monitor resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enable_logs_sample</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether or not to include a list of log values which triggered the alert. Defaults to false. This is only used by log monitors.
triggering tags into the title. Defaults to true.</p></li>
<li><p><strong>escalation_message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A message to include with a re-notification. Supports the <a class="reference external" href="mailto:'&#37;&#52;&#48;username">‘<span>&#64;</span>username</a>’
notification allowed elsewhere.</p></li>
<li><p><strong>evaluation_delay</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Time (in seconds) to delay evaluation, as a non-negative integer.
For example, if the value is set to 300 (5min), the timeframe is set to last_5m and the time is 7:00,
the monitor will evaluate data from 6:50 to 6:55. This is useful for AWS CloudWatch and other backfilled
metrics to ensure the monitor will always have data during evaluation.</p></li>
<li><p><strong>force_delete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether this monitor can be deleted even if it’s referenced by other resources (e.g. SLO, composite monitor).</p></li>
<li><p><strong>include_tags</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether notifications from this monitor automatically insert its triggering tags into the title. Defaults to true.</p></li>
<li><p><strong>locked</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether changes to to this monitor should be restricted to the creator or admins. Defaults to False.</p></li>
<li><p><strong>message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A message to include with notifications for this monitor.
Email notifications can be sent to specific users by using the same <a class="reference external" href="mailto:'&#37;&#52;&#48;username">‘<span>&#64;</span>username</a>’ notation as events.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Datadog monitor</p></li>
<li><p><strong>new_host_delay</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Time (in seconds) to allow a host to boot and
applications to fully start before starting the evaluation of monitor
results. Should be a non negative integer. Defaults to 300.</p></li>
<li><p><strong>no_data_timeframe</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of minutes before a monitor will notify when data stops reporting. Provider defaults to 10 minutes.
We recommend at least 2x the monitor timeframe for metric alerts or 2 minutes for service checks.</p></li>
<li><p><strong>notify_audit</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether tagged users will be notified on changes to this monitor.
Defaults to false.</p></li>
<li><p><strong>notify_no_data</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether this monitor will notify when data stops reporting. Defaults
to false.</p></li>
<li><p><strong>query</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The monitor query to notify on. Note this is not the same query you see in the UI and
the syntax is different depending on the monitor <code class="docutils literal notranslate"><span class="pre">type</span></code>, please see the <a class="reference external" href="https://docs.datadoghq.com/api/v1/monitors/#create-a-monitor">API Reference</a> for details. <strong>Warning:</strong> <code class="docutils literal notranslate"><span class="pre">pulumi</span> <span class="pre">preview</span></code> won’t perform any validation of the query contents.</p>
</p></li>
<li><p><strong>renotify_interval</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of minutes after the last notification before a monitor will re-notify
on the current status. It will only re-notify if it’s not resolved.</p></li>
<li><p><strong>require_full_window</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean indicating whether this monitor needs a full window of data before it’s evaluated.
We highly recommend you set this to False for sparse metrics, otherwise some evaluations will be skipped.
Default: True for “on average”, “at all times” and “in total” aggregation. False otherwise.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>silenced</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Each scope will be muted until the given POSIX timestamp or forever if the value is 0. Use <code class="docutils literal notranslate"><span class="pre">-1</span></code> if you want to unmute the scope. <strong>Deprecated</strong> The <code class="docutils literal notranslate"><span class="pre">silenced</span></code> parameter is being deprecated in favor of the downtime resource.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of tags to associate with your monitor. This can help you categorize and filter monitors in the manage monitors page of the UI. Note: it’s not currently possible to filter by these tags when querying via the API</p></li>
<li><p><strong>threshold_windows</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'MonitorThresholdWindowsArgs'</em><em>]</em><em>]</em>) – A mapping containing <code class="docutils literal notranslate"><span class="pre">recovery_window</span></code> and <code class="docutils literal notranslate"><span class="pre">trigger_window</span></code> values, e.g. <code class="docutils literal notranslate"><span class="pre">last_15m</span></code>. Can only be used for, and are required for, anomaly monitors.</p></li>
<li><p><strong>thresholds</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'MonitorThresholdsArgs'</em><em>]</em><em>]</em>) – <ul>
<li><p>Metric alerts:</p></li>
</ul>
<p>A dictionary of thresholds by threshold type. Currently we have four threshold types for metric alerts: critical, critical recovery, warning, and warning recovery. Critical is defined in the query, but can also be specified in this option. Warning and recovery thresholds can only be specified using the thresholds option.
Example usage:</p>
</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>```python
import pulumi
```
**Warning:** the `critical` threshold value must match the one contained in the `query` argument. The `threshold` from the previous example is valid along with a query like `avg(last_1h):avg:system.disk.in_use{role:sqlserver} by {host} &gt; 90` but
along with something like `avg(last_1h):avg:system.disk.in_use{role:sqlserver} by {host} &gt; 95` would make the Datadog API return a HTTP error 400, complaining &quot;The value provided for parameter &#39;query&#39; is invalid&quot;.
* Service checks:
A dictionary of thresholds by status. Because service checks can have multiple thresholds, we don&#39;t define them directly in the query.
Default values:
```python
import pulumi
```
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>timeout_h</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of hours of the monitor not reporting data before it will automatically resolve
from a triggered state. Defaults to false.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The type of the monitor. The mapping from these types to the types found in the Datadog Web UI can be found in the Datadog API <a class="reference external" href="https://docs.datadoghq.com/api/v1/monitors/#create-a-monitor">documentation</a> page. The available options are below. <strong>Note</strong>: The monitor type cannot be changed after a monitor is created.</p>
</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `metric alert`
* `service check`
* `event alert`
* `query alert`
* `composite`
* `log alert`
</pre></div>
</div>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.enable_logs_sample">
<em class="property">property </em><code class="sig-name descname">enable_logs_sample</code><a class="headerlink" href="#pulumi_datadog.Monitor.enable_logs_sample" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean indicating whether or not to include a list of log values which triggered the alert. Defaults to false. This is only used by log monitors.
triggering tags into the title. Defaults to true.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.escalation_message">
<em class="property">property </em><code class="sig-name descname">escalation_message</code><a class="headerlink" href="#pulumi_datadog.Monitor.escalation_message" title="Permalink to this definition">¶</a></dt>
<dd><p>A message to include with a re-notification. Supports the <a class="reference external" href="mailto:'&#37;&#52;&#48;username">‘<span>&#64;</span>username</a>’
notification allowed elsewhere.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.evaluation_delay">
<em class="property">property </em><code class="sig-name descname">evaluation_delay</code><a class="headerlink" href="#pulumi_datadog.Monitor.evaluation_delay" title="Permalink to this definition">¶</a></dt>
<dd><p>Time (in seconds) to delay evaluation, as a non-negative integer.
For example, if the value is set to 300 (5min), the timeframe is set to last_5m and the time is 7:00,
the monitor will evaluate data from 6:50 to 6:55. This is useful for AWS CloudWatch and other backfilled
metrics to ensure the monitor will always have data during evaluation.</p>
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
<dt id="pulumi_datadog.Monitor.message">
<em class="property">property </em><code class="sig-name descname">message</code><a class="headerlink" href="#pulumi_datadog.Monitor.message" title="Permalink to this definition">¶</a></dt>
<dd><p>A message to include with notifications for this monitor.
Email notifications can be sent to specific users by using the same <a class="reference external" href="mailto:'&#37;&#52;&#48;username">‘<span>&#64;</span>username</a>’ notation as events.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_datadog.Monitor.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of Datadog monitor</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.new_host_delay">
<em class="property">property </em><code class="sig-name descname">new_host_delay</code><a class="headerlink" href="#pulumi_datadog.Monitor.new_host_delay" title="Permalink to this definition">¶</a></dt>
<dd><p>Time (in seconds) to allow a host to boot and
applications to fully start before starting the evaluation of monitor
results. Should be a non negative integer. Defaults to 300.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.no_data_timeframe">
<em class="property">property </em><code class="sig-name descname">no_data_timeframe</code><a class="headerlink" href="#pulumi_datadog.Monitor.no_data_timeframe" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of minutes before a monitor will notify when data stops reporting. Provider defaults to 10 minutes.
We recommend at least 2x the monitor timeframe for metric alerts or 2 minutes for service checks.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.notify_audit">
<em class="property">property </em><code class="sig-name descname">notify_audit</code><a class="headerlink" href="#pulumi_datadog.Monitor.notify_audit" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean indicating whether tagged users will be notified on changes to this monitor.
Defaults to false.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.notify_no_data">
<em class="property">property </em><code class="sig-name descname">notify_no_data</code><a class="headerlink" href="#pulumi_datadog.Monitor.notify_no_data" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean indicating whether this monitor will notify when data stops reporting. Defaults
to false.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.query">
<em class="property">property </em><code class="sig-name descname">query</code><a class="headerlink" href="#pulumi_datadog.Monitor.query" title="Permalink to this definition">¶</a></dt>
<dd><p>The monitor query to notify on. Note this is not the same query you see in the UI and
the syntax is different depending on the monitor <code class="docutils literal notranslate"><span class="pre">type</span></code>, please see the <a class="reference external" href="https://docs.datadoghq.com/api/v1/monitors/#create-a-monitor">API Reference</a> for details. <strong>Warning:</strong> <code class="docutils literal notranslate"><span class="pre">pulumi</span> <span class="pre">preview</span></code> won’t perform any validation of the query contents.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.renotify_interval">
<em class="property">property </em><code class="sig-name descname">renotify_interval</code><a class="headerlink" href="#pulumi_datadog.Monitor.renotify_interval" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of minutes after the last notification before a monitor will re-notify
on the current status. It will only re-notify if it’s not resolved.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.require_full_window">
<em class="property">property </em><code class="sig-name descname">require_full_window</code><a class="headerlink" href="#pulumi_datadog.Monitor.require_full_window" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean indicating whether this monitor needs a full window of data before it’s evaluated.
We highly recommend you set this to False for sparse metrics, otherwise some evaluations will be skipped.
Default: True for “on average”, “at all times” and “in total” aggregation. False otherwise.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.silenced">
<em class="property">property </em><code class="sig-name descname">silenced</code><a class="headerlink" href="#pulumi_datadog.Monitor.silenced" title="Permalink to this definition">¶</a></dt>
<dd><p>Each scope will be muted until the given POSIX timestamp or forever if the value is 0. Use <code class="docutils literal notranslate"><span class="pre">-1</span></code> if you want to unmute the scope. <strong>Deprecated</strong> The <code class="docutils literal notranslate"><span class="pre">silenced</span></code> parameter is being deprecated in favor of the downtime resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_datadog.Monitor.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tags to associate with your monitor. This can help you categorize and filter monitors in the manage monitors page of the UI. Note: it’s not currently possible to filter by these tags when querying via the API</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.threshold_windows">
<em class="property">property </em><code class="sig-name descname">threshold_windows</code><a class="headerlink" href="#pulumi_datadog.Monitor.threshold_windows" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping containing <code class="docutils literal notranslate"><span class="pre">recovery_window</span></code> and <code class="docutils literal notranslate"><span class="pre">trigger_window</span></code> values, e.g. <code class="docutils literal notranslate"><span class="pre">last_15m</span></code>. Can only be used for, and are required for, anomaly monitors.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.thresholds">
<em class="property">property </em><code class="sig-name descname">thresholds</code><a class="headerlink" href="#pulumi_datadog.Monitor.thresholds" title="Permalink to this definition">¶</a></dt>
<dd><ul>
<li><p>Metric alerts:
A dictionary of thresholds by threshold type. Currently we have four threshold types for metric alerts: critical, critical recovery, warning, and warning recovery. Critical is defined in the query, but can also be specified in this option. Warning and recovery thresholds can only be specified using the thresholds option.
Example usage:
.. code-block:: python</p>
<blockquote>
<div><p>import pulumi</p>
</div></blockquote>
<p><strong>Warning:</strong> the <code class="docutils literal notranslate"><span class="pre">critical</span></code> threshold value must match the one contained in the <code class="docutils literal notranslate"><span class="pre">query</span></code> argument. The <code class="docutils literal notranslate"><span class="pre">threshold</span></code> from the previous example is valid along with a query like <code class="docutils literal notranslate"><span class="pre">avg(last_1h):avg:system.disk.in_use{role:sqlserver}</span> <span class="pre">by</span> <span class="pre">{host}</span> <span class="pre">&gt;</span> <span class="pre">90</span></code> but
along with something like <code class="docutils literal notranslate"><span class="pre">avg(last_1h):avg:system.disk.in_use{role:sqlserver}</span> <span class="pre">by</span> <span class="pre">{host}</span> <span class="pre">&gt;</span> <span class="pre">95</span></code> would make the Datadog API return a HTTP error 400, complaining “The value provided for parameter ‘query’ is invalid”.</p>
</li>
<li><p>Service checks:
A dictionary of thresholds by status. Because service checks can have multiple thresholds, we don’t define them directly in the query.
Default values:
.. code-block:: python</p>
<blockquote>
<div><p>import pulumi</p>
</div></blockquote>
</li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.timeout_h">
<em class="property">property </em><code class="sig-name descname">timeout_h</code><a class="headerlink" href="#pulumi_datadog.Monitor.timeout_h" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of hours of the monitor not reporting data before it will automatically resolve
from a triggered state. Defaults to false.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.Monitor.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_datadog.Monitor.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the monitor. The mapping from these types to the types found in the Datadog Web UI can be found in the Datadog API <a class="reference external" href="https://docs.datadoghq.com/api/v1/monitors/#create-a-monitor">documentation</a> page. The available options are below. <strong>Note</strong>: The monitor type cannot be changed after a monitor is created.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">metric</span> <span class="pre">alert</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service</span> <span class="pre">check</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">event</span> <span class="pre">alert</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">query</span> <span class="pre">alert</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">composite</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">log</span> <span class="pre">alert</span></code></p></li>
</ul>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">ScreenBoard</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">height</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">read_only</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shared</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_variables</span><span class="p">:</span> <span class="n">Union[List[Union[ScreenBoardTemplateVariableArgs, Mapping[str, Any], Awaitable[Union[ScreenBoardTemplateVariableArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[ScreenBoardTemplateVariableArgs, Mapping[str, Any], Awaitable[Union[ScreenBoardTemplateVariableArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">title</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">widgets</span><span class="p">:</span> <span class="n">Union[List[Union[ScreenBoardWidgetArgs, Mapping[str, Any], Awaitable[Union[ScreenBoardWidgetArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[ScreenBoardWidgetArgs, Mapping[str, Any], Awaitable[Union[ScreenBoardWidgetArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">width</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.ScreenBoard" title="Permalink to this definition">¶</a></dt>
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
            <span class="n">title</span><span class="o">=</span><span class="s2">&quot;graph title tf&quot;</span><span class="p">,</span>
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
            <span class="n">title</span><span class="o">=</span><span class="s2">&quot;query value title tf&quot;</span><span class="p">,</span>
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
            <span class="n">title</span><span class="o">=</span><span class="s2">&quot;toplist title tf&quot;</span><span class="p">,</span>
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
            <span class="n">title</span><span class="o">=</span><span class="s2">&quot;change title tf&quot;</span><span class="p">,</span>
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
            <span class="n">title</span><span class="o">=</span><span class="s2">&quot;event_timeline title tf&quot;</span><span class="p">,</span>
            <span class="n">query</span><span class="o">=</span><span class="s2">&quot;status:error&quot;</span><span class="p">,</span>
            <span class="n">time</span><span class="o">=</span><span class="p">{</span>
                <span class="s2">&quot;live_span&quot;</span><span class="p">:</span> <span class="s2">&quot;1d&quot;</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">ScreenBoardWidgetArgs</span><span class="p">(</span>
            <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;event_stream&quot;</span><span class="p">,</span>
            <span class="n">x</span><span class="o">=</span><span class="mi">115</span><span class="p">,</span>
            <span class="n">y</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
            <span class="n">title</span><span class="o">=</span><span class="s2">&quot;event_stream title tf&quot;</span><span class="p">,</span>
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
            <span class="n">title</span><span class="o">=</span><span class="s2">&quot;image title tf&quot;</span><span class="p">,</span>
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
            <span class="n">title</span><span class="o">=</span><span class="s2">&quot;alert graph title tf&quot;</span><span class="p">,</span>
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
            <span class="n">title</span><span class="o">=</span><span class="s2">&quot;alert value title tf&quot;</span><span class="p">,</span>
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
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>height</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The screenboard’s height.</p></li>
<li><p><strong>read_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The read-only status of the screenboard. Default is false.</p></li>
<li><p><strong>shared</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the screenboard is shared or not. Default is false.</p></li>
<li><p><strong>template_variables</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ScreenBoardTemplateVariableArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Nested block describing a template variable. The structure of this block is described below. Multiple template_variable blocks are allowed within a ScreenBoard resource.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the screenboard.</p></li>
<li><p><strong>widgets</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ScreenBoardWidgetArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Nested block describing a widget. The structure of this block is described below. Multiple widget blocks are allowed within a ScreenBoard resource.</p></li>
<li><p><strong>width</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The screenboard’s width.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_datadog.ScreenBoard.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">height</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">read_only</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shared</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_variables</span><span class="p">:</span> <span class="n">Union[List[Union[ScreenBoardTemplateVariableArgs, Mapping[str, Any], Awaitable[Union[ScreenBoardTemplateVariableArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[ScreenBoardTemplateVariableArgs, Mapping[str, Any], Awaitable[Union[ScreenBoardTemplateVariableArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">title</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">widgets</span><span class="p">:</span> <span class="n">Union[List[Union[ScreenBoardWidgetArgs, Mapping[str, Any], Awaitable[Union[ScreenBoardWidgetArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[ScreenBoardWidgetArgs, Mapping[str, Any], Awaitable[Union[ScreenBoardWidgetArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">width</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.screen_board.ScreenBoard<a class="headerlink" href="#pulumi_datadog.ScreenBoard.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ScreenBoard resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>height</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The screenboard’s height.</p></li>
<li><p><strong>read_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The read-only status of the screenboard. Default is false.</p></li>
<li><p><strong>shared</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the screenboard is shared or not. Default is false.</p></li>
<li><p><strong>template_variables</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ScreenBoardTemplateVariableArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Nested block describing a template variable. The structure of this block is described below. Multiple template_variable blocks are allowed within a ScreenBoard resource.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the screenboard.</p></li>
<li><p><strong>widgets</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ScreenBoardWidgetArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Nested block describing a widget. The structure of this block is described below. Multiple widget blocks are allowed within a ScreenBoard resource.</p></li>
<li><p><strong>width</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The screenboard’s width.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.ScreenBoard.height">
<em class="property">property </em><code class="sig-name descname">height</code><a class="headerlink" href="#pulumi_datadog.ScreenBoard.height" title="Permalink to this definition">¶</a></dt>
<dd><p>The screenboard’s height.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.ScreenBoard.read_only">
<em class="property">property </em><code class="sig-name descname">read_only</code><a class="headerlink" href="#pulumi_datadog.ScreenBoard.read_only" title="Permalink to this definition">¶</a></dt>
<dd><p>The read-only status of the screenboard. Default is false.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.ScreenBoard.shared">
<em class="property">property </em><code class="sig-name descname">shared</code><a class="headerlink" href="#pulumi_datadog.ScreenBoard.shared" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the screenboard is shared or not. Default is false.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.ScreenBoard.template_variables">
<em class="property">property </em><code class="sig-name descname">template_variables</code><a class="headerlink" href="#pulumi_datadog.ScreenBoard.template_variables" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested block describing a template variable. The structure of this block is described below. Multiple template_variable blocks are allowed within a ScreenBoard resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.ScreenBoard.title">
<em class="property">property </em><code class="sig-name descname">title</code><a class="headerlink" href="#pulumi_datadog.ScreenBoard.title" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the screenboard.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.ScreenBoard.widgets">
<em class="property">property </em><code class="sig-name descname">widgets</code><a class="headerlink" href="#pulumi_datadog.ScreenBoard.widgets" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested block describing a widget. The structure of this block is described below. Multiple widget blocks are allowed within a ScreenBoard resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.ScreenBoard.width">
<em class="property">property </em><code class="sig-name descname">width</code><a class="headerlink" href="#pulumi_datadog.ScreenBoard.width" title="Permalink to this definition">¶</a></dt>
<dd><p>The screenboard’s width.</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">ServiceLevelObjective</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitor_ids</span><span class="p">:</span> <span class="n">Union[List[Union[float, Awaitable[float], Output[T]]], Awaitable[List[Union[float, Awaitable[float], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="p">:</span> <span class="n">Union[ServiceLevelObjectiveQueryArgs, Mapping[str, Any], Awaitable[Union[ServiceLevelObjectiveQueryArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">thresholds</span><span class="p">:</span> <span class="n">Union[List[Union[ServiceLevelObjectiveThresholdArgs, Mapping[str, Any], Awaitable[Union[ServiceLevelObjectiveThresholdArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[ServiceLevelObjectiveThresholdArgs, Mapping[str, Any], Awaitable[Union[ServiceLevelObjectiveThresholdArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.ServiceLevelObjective" title="Permalink to this definition">¶</a></dt>
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
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of this service level objective.</p></li>
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A custom set of groups from the monitor(s) for which to use as the SLI instead of all the groups.</p></li>
<li><p><strong>monitor_ids</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>float</em><em>]</em><em>]</em><em>]</em>) – A list of numeric monitor IDs for which to use as SLIs. Their tags will be auto-imported into <code class="docutils literal notranslate"><span class="pre">monitor_tags</span></code> field in the API resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Datadog service level objective</p></li>
<li><p><strong>query</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceLevelObjectiveQueryArgs'</em><em>]</em><em>]</em>) – The metric query configuration to use for the SLI. This is a dictionary and requires both the <code class="docutils literal notranslate"><span class="pre">numerator</span></code> and <code class="docutils literal notranslate"><span class="pre">denominator</span></code> fields which should be <code class="docutils literal notranslate"><span class="pre">count</span></code> metrics using the <code class="docutils literal notranslate"><span class="pre">sum</span></code> aggregator.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of tags to associate with your service level objective. This can help you categorize and filter service level objectives in the service level objectives page of the UI. Note: it’s not currently possible to filter by these tags when querying via the API</p></li>
<li><p><strong>thresholds</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceLevelObjectiveThresholdArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – <ul>
<li><p>A list of thresholds and targets that define the service level objectives from the provided SLIs.</p></li>
</ul>
</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The type of the service level objective. The mapping from these types to the types found in the Datadog Web UI can be found in the Datadog API <a class="reference external" href="https://docs.datadoghq.com/api/v1/service-level-objectives/#create-a-slo-object">documentation</a> page. Available options to choose from are:</p>
</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `metric`
* `monitor`
</pre></div>
</div>
<dl class="py method">
<dt id="pulumi_datadog.ServiceLevelObjective.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitor_ids</span><span class="p">:</span> <span class="n">Union[List[Union[float, Awaitable[float], Output[T]]], Awaitable[List[Union[float, Awaitable[float], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="p">:</span> <span class="n">Union[ServiceLevelObjectiveQueryArgs, Mapping[str, Any], Awaitable[Union[ServiceLevelObjectiveQueryArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">thresholds</span><span class="p">:</span> <span class="n">Union[List[Union[ServiceLevelObjectiveThresholdArgs, Mapping[str, Any], Awaitable[Union[ServiceLevelObjectiveThresholdArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[ServiceLevelObjectiveThresholdArgs, Mapping[str, Any], Awaitable[Union[ServiceLevelObjectiveThresholdArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.service_level_objective.ServiceLevelObjective<a class="headerlink" href="#pulumi_datadog.ServiceLevelObjective.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceLevelObjective resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of this service level objective.</p></li>
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A custom set of groups from the monitor(s) for which to use as the SLI instead of all the groups.</p></li>
<li><p><strong>monitor_ids</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>float</em><em>]</em><em>]</em><em>]</em>) – A list of numeric monitor IDs for which to use as SLIs. Their tags will be auto-imported into <code class="docutils literal notranslate"><span class="pre">monitor_tags</span></code> field in the API resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Datadog service level objective</p></li>
<li><p><strong>query</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceLevelObjectiveQueryArgs'</em><em>]</em><em>]</em>) – The metric query configuration to use for the SLI. This is a dictionary and requires both the <code class="docutils literal notranslate"><span class="pre">numerator</span></code> and <code class="docutils literal notranslate"><span class="pre">denominator</span></code> fields which should be <code class="docutils literal notranslate"><span class="pre">count</span></code> metrics using the <code class="docutils literal notranslate"><span class="pre">sum</span></code> aggregator.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of tags to associate with your service level objective. This can help you categorize and filter service level objectives in the service level objectives page of the UI. Note: it’s not currently possible to filter by these tags when querying via the API</p></li>
<li><p><strong>thresholds</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceLevelObjectiveThresholdArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – <ul>
<li><p>A list of thresholds and targets that define the service level objectives from the provided SLIs.</p></li>
</ul>
</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The type of the service level objective. The mapping from these types to the types found in the Datadog Web UI can be found in the Datadog API <a class="reference external" href="https://docs.datadoghq.com/api/v1/service-level-objectives/#create-a-slo-object">documentation</a> page. Available options to choose from are:</p>
</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `metric`
* `monitor`
</pre></div>
</div>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.ServiceLevelObjective.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_datadog.ServiceLevelObjective.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of this service level objective.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.ServiceLevelObjective.groups">
<em class="property">property </em><code class="sig-name descname">groups</code><a class="headerlink" href="#pulumi_datadog.ServiceLevelObjective.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>A custom set of groups from the monitor(s) for which to use as the SLI instead of all the groups.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.ServiceLevelObjective.monitor_ids">
<em class="property">property </em><code class="sig-name descname">monitor_ids</code><a class="headerlink" href="#pulumi_datadog.ServiceLevelObjective.monitor_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of numeric monitor IDs for which to use as SLIs. Their tags will be auto-imported into <code class="docutils literal notranslate"><span class="pre">monitor_tags</span></code> field in the API resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.ServiceLevelObjective.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_datadog.ServiceLevelObjective.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of Datadog service level objective</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.ServiceLevelObjective.query">
<em class="property">property </em><code class="sig-name descname">query</code><a class="headerlink" href="#pulumi_datadog.ServiceLevelObjective.query" title="Permalink to this definition">¶</a></dt>
<dd><p>The metric query configuration to use for the SLI. This is a dictionary and requires both the <code class="docutils literal notranslate"><span class="pre">numerator</span></code> and <code class="docutils literal notranslate"><span class="pre">denominator</span></code> fields which should be <code class="docutils literal notranslate"><span class="pre">count</span></code> metrics using the <code class="docutils literal notranslate"><span class="pre">sum</span></code> aggregator.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.ServiceLevelObjective.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_datadog.ServiceLevelObjective.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tags to associate with your service level objective. This can help you categorize and filter service level objectives in the service level objectives page of the UI. Note: it’s not currently possible to filter by these tags when querying via the API</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.ServiceLevelObjective.thresholds">
<em class="property">property </em><code class="sig-name descname">thresholds</code><a class="headerlink" href="#pulumi_datadog.ServiceLevelObjective.thresholds" title="Permalink to this definition">¶</a></dt>
<dd><ul class="simple">
<li><p>A list of thresholds and targets that define the service level objectives from the provided SLIs.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.ServiceLevelObjective.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_datadog.ServiceLevelObjective.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the service level objective. The mapping from these types to the types found in the Datadog Web UI can be found in the Datadog API <a class="reference external" href="https://docs.datadoghq.com/api/v1/service-level-objectives/#create-a-slo-object">documentation</a> page. Available options to choose from are:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">metric</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">monitor</span></code></p></li>
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
<dt id="pulumi_datadog.SyntheticsTest">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">SyntheticsTest</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">assertions</span><span class="p">:</span> <span class="n">Union[List[Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T]]], Awaitable[List[Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_ids</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locations</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">options</span><span class="p">:</span> <span class="n">Union[SyntheticsTestOptionsArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestOptionsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request</span><span class="p">:</span> <span class="n">Union[SyntheticsTestRequestArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestRequestArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_basicauth</span><span class="p">:</span> <span class="n">Union[SyntheticsTestRequestBasicauthArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestRequestBasicauthArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_headers</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_query</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subtype</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.SyntheticsTest" title="Permalink to this definition">¶</a></dt>
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
    <span class="n">options</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">SyntheticsTestOptionsArgs</span><span class="p">(</span>
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
    <span class="n">options</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">SyntheticsTestOptionsArgs</span><span class="p">(</span>
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
<p>Support for Synthetics Browser test is limited (see below)</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="c1"># Create a new Datadog Synthetics Browser test starting on https://www.example.org</span>
<span class="n">test_browser</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">SyntheticsTest</span><span class="p">(</span><span class="s2">&quot;testBrowser&quot;</span><span class="p">,</span>
    <span class="n">device_ids</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;laptop_large&quot;</span><span class="p">],</span>
    <span class="n">locations</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;aws:eu-central-1&quot;</span><span class="p">],</span>
    <span class="n">message</span><span class="o">=</span><span class="s2">&quot;Notify @qa&quot;</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;A Browser test on example.org&quot;</span><span class="p">,</span>
    <span class="n">options</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">SyntheticsTestOptionsArgs</span><span class="p">(</span>
        <span class="n">tick_every</span><span class="o">=</span><span class="mi">3600</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">request</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">SyntheticsTestRequestArgs</span><span class="p">(</span>
        <span class="n">method</span><span class="o">=</span><span class="s2">&quot;GET&quot;</span><span class="p">,</span>
        <span class="n">url</span><span class="o">=</span><span class="s2">&quot;https://app.datadoghq.com&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">status</span><span class="o">=</span><span class="s2">&quot;paused&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">[],</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;browser&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Support for Synthetics Browser test is limited to creating shallow Synthetics Browser test (cf. example usage below)</p>
<p>You cannot create/edit/delete steps or assertions via this provider unless you use <a class="reference external" href="https://app.datadoghq.com/synthetics/list">Datadog WebUI</a> in conjunction with the provider.</p>
<p>We are considering adding support for Synthetics Browser test steps and assertions in the future but can’t share any release date on that matter.</p>
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
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>device_ids</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – “laptop_large”, “tablet” or “mobile_small” (only available if type=browser)</p></li>
<li><p><strong>locations</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Please refer to <a class="reference external" href="https://docs.datadoghq.com/synthetics/api_test/#request">Datadog documentation</a> for available locations (e.g. “aws:eu-central-1”)</p></li>
<li><p><strong>message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A message to include with notifications for this synthetics test.
Email notifications can be sent to specific users by using the same <a class="reference external" href="mailto:'&#37;&#52;&#48;username">‘<span>&#64;</span>username</a>’ notation as events.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Datadog synthetics test</p></li>
<li><p><strong>request</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SyntheticsTestRequestArgs'</em><em>]</em><em>]</em>) – if type=browser</p></li>
<li><p><strong>request_basicauth</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SyntheticsTestRequestBasicauthArgs'</em><em>]</em><em>]</em>) – Array of 1 item containing HTTP basic authentication credentials</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>request_headers</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Header name and value map</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>request_query</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Query arguments name and value map</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – “live”, “paused”</p></li>
<li><p><strong>subtype</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – For type=api, http or ssl (Default = http)</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of tags to associate with your synthetics test. This can help you categorize and filter tests in the manage synthetics page of the UI.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – body, header, responseTime, statusCode</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_datadog.SyntheticsTest.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">assertions</span><span class="p">:</span> <span class="n">Union[List[Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T]]], Awaitable[List[Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">device_ids</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">locations</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">message</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">monitor_id</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">options</span><span class="p">:</span> <span class="n">Union[SyntheticsTestOptionsArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestOptionsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request</span><span class="p">:</span> <span class="n">Union[SyntheticsTestRequestArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestRequestArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_basicauth</span><span class="p">:</span> <span class="n">Union[SyntheticsTestRequestBasicauthArgs, Mapping[str, Any], Awaitable[Union[SyntheticsTestRequestBasicauthArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_headers</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_query</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subtype</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[List[Union[str, Awaitable[str], Output[T]]], Awaitable[List[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.synthetics_test.SyntheticsTest<a class="headerlink" href="#pulumi_datadog.SyntheticsTest.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SyntheticsTest resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>device_ids</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – “laptop_large”, “tablet” or “mobile_small” (only available if type=browser)</p></li>
<li><p><strong>locations</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – <p>Please refer to <a class="reference external" href="https://docs.datadoghq.com/synthetics/api_test/#request">Datadog documentation</a> for available locations (e.g. “aws:eu-central-1”)</p>
</p></li>
<li><p><strong>message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A message to include with notifications for this synthetics test.
Email notifications can be sent to specific users by using the same <a class="reference external" href="mailto:'&#37;&#52;&#48;username">‘<span>&#64;</span>username</a>’ notation as events.</p></li>
<li><p><strong>monitor_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – ID of the monitor associated with the Datadog synthetics test</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Datadog synthetics test</p></li>
<li><p><strong>request</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SyntheticsTestRequestArgs'</em><em>]</em><em>]</em>) – if type=browser</p></li>
<li><p><strong>request_basicauth</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'SyntheticsTestRequestBasicauthArgs'</em><em>]</em><em>]</em>) – Array of 1 item containing HTTP basic authentication credentials</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>request_headers</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Header name and value map</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>request_query</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Query arguments name and value map</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – “live”, “paused”</p></li>
<li><p><strong>subtype</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – For type=api, http or ssl (Default = http)</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of tags to associate with your synthetics test. This can help you categorize and filter tests in the manage synthetics page of the UI.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – body, header, responseTime, statusCode</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsTest.device_ids">
<em class="property">property </em><code class="sig-name descname">device_ids</code><a class="headerlink" href="#pulumi_datadog.SyntheticsTest.device_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>“laptop_large”, “tablet” or “mobile_small” (only available if type=browser)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsTest.locations">
<em class="property">property </em><code class="sig-name descname">locations</code><a class="headerlink" href="#pulumi_datadog.SyntheticsTest.locations" title="Permalink to this definition">¶</a></dt>
<dd><p>Please refer to <a class="reference external" href="https://docs.datadoghq.com/synthetics/api_test/#request">Datadog documentation</a> for available locations (e.g. “aws:eu-central-1”)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsTest.message">
<em class="property">property </em><code class="sig-name descname">message</code><a class="headerlink" href="#pulumi_datadog.SyntheticsTest.message" title="Permalink to this definition">¶</a></dt>
<dd><p>A message to include with notifications for this synthetics test.
Email notifications can be sent to specific users by using the same <a class="reference external" href="mailto:'&#37;&#52;&#48;username">‘<span>&#64;</span>username</a>’ notation as events.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsTest.monitor_id">
<em class="property">property </em><code class="sig-name descname">monitor_id</code><a class="headerlink" href="#pulumi_datadog.SyntheticsTest.monitor_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the monitor associated with the Datadog synthetics test</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsTest.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_datadog.SyntheticsTest.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of Datadog synthetics test</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsTest.request">
<em class="property">property </em><code class="sig-name descname">request</code><a class="headerlink" href="#pulumi_datadog.SyntheticsTest.request" title="Permalink to this definition">¶</a></dt>
<dd><p>if type=browser</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsTest.request_basicauth">
<em class="property">property </em><code class="sig-name descname">request_basicauth</code><a class="headerlink" href="#pulumi_datadog.SyntheticsTest.request_basicauth" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of 1 item containing HTTP basic authentication credentials</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsTest.request_headers">
<em class="property">property </em><code class="sig-name descname">request_headers</code><a class="headerlink" href="#pulumi_datadog.SyntheticsTest.request_headers" title="Permalink to this definition">¶</a></dt>
<dd><p>Header name and value map</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsTest.request_query">
<em class="property">property </em><code class="sig-name descname">request_query</code><a class="headerlink" href="#pulumi_datadog.SyntheticsTest.request_query" title="Permalink to this definition">¶</a></dt>
<dd><p>Query arguments name and value map</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsTest.status">
<em class="property">property </em><code class="sig-name descname">status</code><a class="headerlink" href="#pulumi_datadog.SyntheticsTest.status" title="Permalink to this definition">¶</a></dt>
<dd><p>“live”, “paused”</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsTest.subtype">
<em class="property">property </em><code class="sig-name descname">subtype</code><a class="headerlink" href="#pulumi_datadog.SyntheticsTest.subtype" title="Permalink to this definition">¶</a></dt>
<dd><p>For type=api, http or ssl (Default = http)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsTest.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_datadog.SyntheticsTest.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of tags to associate with your synthetics test. This can help you categorize and filter tests in the manage synthetics page of the UI.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.SyntheticsTest.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_datadog.SyntheticsTest.type" title="Permalink to this definition">¶</a></dt>
<dd><p>body, header, responseTime, statusCode</p>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">TimeBoard</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">graphs</span><span class="p">:</span> <span class="n">Union[List[Union[TimeBoardGraphArgs, Mapping[str, Any], Awaitable[Union[TimeBoardGraphArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[TimeBoardGraphArgs, Mapping[str, Any], Awaitable[Union[TimeBoardGraphArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">read_only</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_variables</span><span class="p">:</span> <span class="n">Union[List[Union[TimeBoardTemplateVariableArgs, Mapping[str, Any], Awaitable[Union[TimeBoardTemplateVariableArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[TimeBoardTemplateVariableArgs, Mapping[str, Any], Awaitable[Union[TimeBoardTemplateVariableArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">title</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_datadog.TimeBoard" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a Datadog timeboard resource. This can be used to create and manage Datadog timeboards.</p>
<blockquote>
<div><p><strong>Note:</strong>This resource is outdated. Use the new <code class="docutils literal notranslate"><span class="pre">Dashboard</span></code> resource instead.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">json</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="c1"># Create a new Datadog timeboard</span>
<span class="n">redis</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">TimeBoard</span><span class="p">(</span><span class="s2">&quot;redis&quot;</span><span class="p">,</span>
    <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Redis Timeboard (created via TF)&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;created using the Datadog provider in TF&quot;</span><span class="p">,</span>
    <span class="n">read_only</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">graphs</span><span class="o">=</span><span class="p">[</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">TimeBoardGraphArgs</span><span class="p">(</span>
            <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Redis latency (ms)&quot;</span><span class="p">,</span>
            <span class="n">viz</span><span class="o">=</span><span class="s2">&quot;timeseries&quot;</span><span class="p">,</span>
            <span class="n">requests</span><span class="o">=</span><span class="p">[</span>
                <span class="n">datadog</span><span class="o">.</span><span class="n">TimeBoardGraphRequestArgs</span><span class="p">(</span>
                    <span class="n">q</span><span class="o">=</span><span class="s2">&quot;avg:redis.info.latency_ms{$host}&quot;</span><span class="p">,</span>
                    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;bars&quot;</span><span class="p">,</span>
                    <span class="n">metadata_json</span><span class="o">=</span><span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">({</span>
                        <span class="s2">&quot;avg:redis.info.latency_ms{$host}&quot;</span><span class="p">:</span> <span class="p">{</span>
                            <span class="s2">&quot;alias&quot;</span><span class="p">:</span> <span class="s2">&quot;Redis latency&quot;</span><span class="p">,</span>
                        <span class="p">},</span>
                    <span class="p">}),</span>
                <span class="p">),</span>
                <span class="n">datadog</span><span class="o">.</span><span class="n">TimeBoardGraphRequestArgs</span><span class="p">(</span>
                    <span class="n">log_query</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">TimeBoardGraphRequestLogQueryArgs</span><span class="p">(</span>
                        <span class="n">index</span><span class="o">=</span><span class="s2">&quot;mcnulty&quot;</span><span class="p">,</span>
                        <span class="n">compute</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">TimeBoardGraphRequestLogQueryComputeArgs</span><span class="p">(</span>
                            <span class="n">aggregation</span><span class="o">=</span><span class="s2">&quot;avg&quot;</span><span class="p">,</span>
                            <span class="n">facet</span><span class="o">=</span><span class="s2">&quot;@duration&quot;</span><span class="p">,</span>
                            <span class="n">interval</span><span class="o">=</span><span class="mi">5000</span><span class="p">,</span>
                        <span class="p">),</span>
                        <span class="n">search</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">TimeBoardGraphRequestLogQuerySearchArgs</span><span class="p">(</span>
                            <span class="n">query</span><span class="o">=</span><span class="s2">&quot;status:info&quot;</span><span class="p">,</span>
                        <span class="p">),</span>
                        <span class="n">group_bies</span><span class="o">=</span><span class="p">[</span><span class="n">datadog</span><span class="o">.</span><span class="n">TimeBoardGraphRequestLogQueryGroupByArgs</span><span class="p">(</span>
                            <span class="n">facet</span><span class="o">=</span><span class="s2">&quot;host&quot;</span><span class="p">,</span>
                            <span class="n">limit</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span>
                            <span class="n">sort</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">TimeBoardGraphRequestLogQueryGroupBySortArgs</span><span class="p">(</span>
                                <span class="n">aggregation</span><span class="o">=</span><span class="s2">&quot;avg&quot;</span><span class="p">,</span>
                                <span class="n">order</span><span class="o">=</span><span class="s2">&quot;desc&quot;</span><span class="p">,</span>
                                <span class="n">facet</span><span class="o">=</span><span class="s2">&quot;@duration&quot;</span><span class="p">,</span>
                            <span class="p">),</span>
                        <span class="p">)],</span>
                    <span class="p">),</span>
                    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;area&quot;</span><span class="p">,</span>
                <span class="p">),</span>
                <span class="n">datadog</span><span class="o">.</span><span class="n">TimeBoardGraphRequestArgs</span><span class="p">(</span>
                    <span class="n">apm_query</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">TimeBoardGraphRequestApmQueryArgs</span><span class="p">(</span>
                        <span class="n">index</span><span class="o">=</span><span class="s2">&quot;apm-search&quot;</span><span class="p">,</span>
                        <span class="n">compute</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">TimeBoardGraphRequestApmQueryComputeArgs</span><span class="p">(</span>
                            <span class="n">aggregation</span><span class="o">=</span><span class="s2">&quot;avg&quot;</span><span class="p">,</span>
                            <span class="n">facet</span><span class="o">=</span><span class="s2">&quot;@duration&quot;</span><span class="p">,</span>
                            <span class="n">interval</span><span class="o">=</span><span class="mi">5000</span><span class="p">,</span>
                        <span class="p">),</span>
                        <span class="n">search</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">TimeBoardGraphRequestApmQuerySearchArgs</span><span class="p">(</span>
                            <span class="n">query</span><span class="o">=</span><span class="s2">&quot;type:web&quot;</span><span class="p">,</span>
                        <span class="p">),</span>
                        <span class="n">group_bies</span><span class="o">=</span><span class="p">[</span><span class="n">datadog</span><span class="o">.</span><span class="n">TimeBoardGraphRequestApmQueryGroupByArgs</span><span class="p">(</span>
                            <span class="n">facet</span><span class="o">=</span><span class="s2">&quot;resource_name&quot;</span><span class="p">,</span>
                            <span class="n">limit</span><span class="o">=</span><span class="mi">50</span><span class="p">,</span>
                            <span class="n">sort</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">TimeBoardGraphRequestApmQueryGroupBySortArgs</span><span class="p">(</span>
                                <span class="n">aggregation</span><span class="o">=</span><span class="s2">&quot;avg&quot;</span><span class="p">,</span>
                                <span class="n">order</span><span class="o">=</span><span class="s2">&quot;desc&quot;</span><span class="p">,</span>
                                <span class="n">facet</span><span class="o">=</span><span class="s2">&quot;@string_query.interval&quot;</span><span class="p">,</span>
                            <span class="p">),</span>
                        <span class="p">)],</span>
                    <span class="p">),</span>
                    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;bars&quot;</span><span class="p">,</span>
                <span class="p">),</span>
                <span class="n">datadog</span><span class="o">.</span><span class="n">TimeBoardGraphRequestArgs</span><span class="p">(</span>
                    <span class="n">process_query</span><span class="o">=</span><span class="n">datadog</span><span class="o">.</span><span class="n">TimeBoardGraphRequestProcessQueryArgs</span><span class="p">(</span>
                        <span class="n">metric</span><span class="o">=</span><span class="s2">&quot;process.stat.cpu.total_pct&quot;</span><span class="p">,</span>
                        <span class="n">search_by</span><span class="o">=</span><span class="s2">&quot;error&quot;</span><span class="p">,</span>
                        <span class="n">filter_bies</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;active&quot;</span><span class="p">],</span>
                        <span class="n">limit</span><span class="o">=</span><span class="mi">50</span><span class="p">,</span>
                    <span class="p">),</span>
                    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;area&quot;</span><span class="p">,</span>
                <span class="p">),</span>
            <span class="p">],</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">TimeBoardGraphArgs</span><span class="p">(</span>
            <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Redis memory usage&quot;</span><span class="p">,</span>
            <span class="n">viz</span><span class="o">=</span><span class="s2">&quot;timeseries&quot;</span><span class="p">,</span>
            <span class="n">requests</span><span class="o">=</span><span class="p">[</span>
                <span class="n">datadog</span><span class="o">.</span><span class="n">TimeBoardGraphRequestArgs</span><span class="p">(</span>
                    <span class="n">q</span><span class="o">=</span><span class="s2">&quot;avg:redis.mem.used{$host} - avg:redis.mem.lua{$host}, avg:redis.mem.lua{$host}&quot;</span><span class="p">,</span>
                    <span class="n">stacked</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
                <span class="p">),</span>
                <span class="n">datadog</span><span class="o">.</span><span class="n">TimeBoardGraphRequestArgs</span><span class="p">(</span>
                    <span class="n">q</span><span class="o">=</span><span class="s2">&quot;avg:redis.mem.rss{$host}&quot;</span><span class="p">,</span>
                    <span class="n">style</span><span class="o">=</span><span class="p">{</span>
                        <span class="s2">&quot;palette&quot;</span><span class="p">:</span> <span class="s2">&quot;warm&quot;</span><span class="p">,</span>
                    <span class="p">},</span>
                <span class="p">),</span>
            <span class="p">],</span>
        <span class="p">),</span>
        <span class="n">datadog</span><span class="o">.</span><span class="n">TimeBoardGraphArgs</span><span class="p">(</span>
            <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Top System CPU by Docker container&quot;</span><span class="p">,</span>
            <span class="n">viz</span><span class="o">=</span><span class="s2">&quot;toplist&quot;</span><span class="p">,</span>
            <span class="n">requests</span><span class="o">=</span><span class="p">[</span><span class="n">datadog</span><span class="o">.</span><span class="n">TimeBoardGraphRequestArgs</span><span class="p">(</span>
                <span class="n">q</span><span class="o">=</span><span class="s2">&quot;top(avg:docker.cpu.system{*} by </span><span class="si">{container_name}</span><span class="s2">, 10, &#39;mean&#39;, &#39;desc&#39;)&quot;</span><span class="p">,</span>
            <span class="p">)],</span>
        <span class="p">),</span>
    <span class="p">],</span>
    <span class="n">template_variables</span><span class="o">=</span><span class="p">[</span><span class="n">datadog</span><span class="o">.</span><span class="n">TimeBoardTemplateVariableArgs</span><span class="p">(</span>
        <span class="n">name</span><span class="o">=</span><span class="s2">&quot;host&quot;</span><span class="p">,</span>
        <span class="n">prefix</span><span class="o">=</span><span class="s2">&quot;host&quot;</span><span class="p">,</span>
    <span class="p">)])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the dashboard’s content.</p></li>
<li><p><strong>graphs</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TimeBoardGraphArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Nested block describing a graph definition. The structure of this block is described below. Multiple graph blocks are allowed within a TimeBoard resource.</p></li>
<li><p><strong>read_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The read-only status of the timeboard. Default is false.</p></li>
<li><p><strong>template_variables</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TimeBoardTemplateVariableArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Nested block describing a template variable. The structure of this block is described below. Multiple template_variable blocks are allowed within a TimeBoard resource.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the dashboard.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_datadog.TimeBoard.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">graphs</span><span class="p">:</span> <span class="n">Union[List[Union[TimeBoardGraphArgs, Mapping[str, Any], Awaitable[Union[TimeBoardGraphArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[TimeBoardGraphArgs, Mapping[str, Any], Awaitable[Union[TimeBoardGraphArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">read_only</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_variables</span><span class="p">:</span> <span class="n">Union[List[Union[TimeBoardTemplateVariableArgs, Mapping[str, Any], Awaitable[Union[TimeBoardTemplateVariableArgs, Mapping[str, Any]]], Output[T]]], Awaitable[List[Union[TimeBoardTemplateVariableArgs, Mapping[str, Any], Awaitable[Union[TimeBoardTemplateVariableArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">title</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.time_board.TimeBoard<a class="headerlink" href="#pulumi_datadog.TimeBoard.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TimeBoard resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the dashboard’s content.</p></li>
<li><p><strong>graphs</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TimeBoardGraphArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Nested block describing a graph definition. The structure of this block is described below. Multiple graph blocks are allowed within a TimeBoard resource.</p></li>
<li><p><strong>read_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The read-only status of the timeboard. Default is false.</p></li>
<li><p><strong>template_variables</strong> (<em>pulumi.Input</em><em>[</em><em>List</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'TimeBoardTemplateVariableArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Nested block describing a template variable. The structure of this block is described below. Multiple template_variable blocks are allowed within a TimeBoard resource.</p></li>
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
<dd><p>Nested block describing a graph definition. The structure of this block is described below. Multiple graph blocks are allowed within a TimeBoard resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.TimeBoard.read_only">
<em class="property">property </em><code class="sig-name descname">read_only</code><a class="headerlink" href="#pulumi_datadog.TimeBoard.read_only" title="Permalink to this definition">¶</a></dt>
<dd><p>The read-only status of the timeboard. Default is false.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.TimeBoard.template_variables">
<em class="property">property </em><code class="sig-name descname">template_variables</code><a class="headerlink" href="#pulumi_datadog.TimeBoard.template_variables" title="Permalink to this definition">¶</a></dt>
<dd><p>Nested block describing a template variable. The structure of this block is described below. Multiple template_variable blocks are allowed within a TimeBoard resource.</p>
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
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Role description for user. Can be <code class="docutils literal notranslate"><span class="pre">st</span></code> (standard user), <code class="docutils literal notranslate"><span class="pre">adm</span></code> (admin user) or <code class="docutils literal notranslate"><span class="pre">ro</span></code> (read-only user).  Default is <code class="docutils literal notranslate"><span class="pre">st</span></code>.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user is disabled</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Email address for user</p></li>
<li><p><strong>handle</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user handle, must be a valid email.</p></li>
<li><p><strong>is_admin</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – (Optional) Whether the user is an administrator. <strong>Warning</strong>: the corresponding query parameter is ignored by the Datadog API, thus the argument would always trigger an execution plan.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name for user</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Role description for user. <strong>Warning</strong>: the corresponding query parameter is ignored by the Datadog API, thus the argument would always trigger an execution plan.</p></li>
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
<li><p><strong>access_role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Role description for user. Can be <code class="docutils literal notranslate"><span class="pre">st</span></code> (standard user), <code class="docutils literal notranslate"><span class="pre">adm</span></code> (admin user) or <code class="docutils literal notranslate"><span class="pre">ro</span></code> (read-only user).  Default is <code class="docutils literal notranslate"><span class="pre">st</span></code>.</p></li>
<li><p><strong>disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the user is disabled</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Email address for user</p></li>
<li><p><strong>handle</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user handle, must be a valid email.</p></li>
<li><p><strong>is_admin</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – (Optional) Whether the user is an administrator. <strong>Warning</strong>: the corresponding query parameter is ignored by the Datadog API, thus the argument would always trigger an execution plan.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name for user</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Role description for user. <strong>Warning</strong>: the corresponding query parameter is ignored by the Datadog API, thus the argument would always trigger an execution plan.</p></li>
<li><p><strong>verified</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Returns true if Datadog user is verified</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.User.access_role">
<em class="property">property </em><code class="sig-name descname">access_role</code><a class="headerlink" href="#pulumi_datadog.User.access_role" title="Permalink to this definition">¶</a></dt>
<dd><p>Role description for user. Can be <code class="docutils literal notranslate"><span class="pre">st</span></code> (standard user), <code class="docutils literal notranslate"><span class="pre">adm</span></code> (admin user) or <code class="docutils literal notranslate"><span class="pre">ro</span></code> (read-only user).  Default is <code class="docutils literal notranslate"><span class="pre">st</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.User.disabled">
<em class="property">property </em><code class="sig-name descname">disabled</code><a class="headerlink" href="#pulumi_datadog.User.disabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user is disabled</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.User.email">
<em class="property">property </em><code class="sig-name descname">email</code><a class="headerlink" href="#pulumi_datadog.User.email" title="Permalink to this definition">¶</a></dt>
<dd><p>Email address for user</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.User.handle">
<em class="property">property </em><code class="sig-name descname">handle</code><a class="headerlink" href="#pulumi_datadog.User.handle" title="Permalink to this definition">¶</a></dt>
<dd><p>The user handle, must be a valid email.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.User.is_admin">
<em class="property">property </em><code class="sig-name descname">is_admin</code><a class="headerlink" href="#pulumi_datadog.User.is_admin" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional) Whether the user is an administrator. <strong>Warning</strong>: the corresponding query parameter is ignored by the Datadog API, thus the argument would always trigger an execution plan.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.User.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_datadog.User.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name for user</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.User.role">
<em class="property">property </em><code class="sig-name descname">role</code><a class="headerlink" href="#pulumi_datadog.User.role" title="Permalink to this definition">¶</a></dt>
<dd><p>Role description for user. <strong>Warning</strong>: the corresponding query parameter is ignored by the Datadog API, thus the argument would always trigger an execution plan.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_datadog.User.verified">
<em class="property">property </em><code class="sig-name descname">verified</code><a class="headerlink" href="#pulumi_datadog.User.verified" title="Permalink to this definition">¶</a></dt>
<dd><p>Returns true if Datadog user is verified</p>
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
<code class="sig-prename descclassname">pulumi_datadog.</code><code class="sig-name descname">get_monitor</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">monitor_tags_filters</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name_filter</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags_filters</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>List<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_datadog.get_monitor.AwaitableGetMonitorResult<a class="headerlink" href="#pulumi_datadog.get_monitor" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve information about an existing monitor for use in other resources.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_datadog</span> <span class="k">as</span> <span class="nn">datadog</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">datadog</span><span class="o">.</span><span class="n">get_monitor</span><span class="p">(</span><span class="n">monitor_tags_filters</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;foo:bar&quot;</span><span class="p">],</span>
    <span class="n">name_filter</span><span class="o">=</span><span class="s2">&quot;My awesome monitor&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>monitor_tags_filters</strong> (<em>List</em><em>[</em><em>str</em><em>]</em>) – A list of monitor tags to limit the search. This filters on the tags set on the monitor itself.</p></li>
<li><p><strong>name_filter</strong> (<em>str</em>) – A monitor name to limit the search.</p></li>
<li><p><strong>tags_filters</strong> (<em>List</em><em>[</em><em>str</em><em>]</em>) – A list of tags to limit the search. This filters on the monitor scope.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
