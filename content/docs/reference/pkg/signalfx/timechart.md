
---
title: "TimeChart"
block_external_search_index: true
---



Provides a SignalFx time chart resource. This can be used to create and manage the different types of time charts.

Time charts display data points over a period of time.

> This content is derived from https://github.com/terraform-providers/terraform-provider-signalfx/blob/master/website/docs/r/time_chart.html.markdown.



## Create a TimeChart Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/signalfx/#TimeChart">TimeChart</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/signalfx/#TimeChartArgs">TimeChartArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">TimeChart</span><span class="p">(resource_name, opts=None, </span>axes_include_zero=None<span class="p">, </span>axes_precision=None<span class="p">, </span>axis_left=None<span class="p">, </span>axis_right=None<span class="p">, </span>color_by=None<span class="p">, </span>description=None<span class="p">, </span>disable_sampling=None<span class="p">, </span>end_time=None<span class="p">, </span>event_options=None<span class="p">, </span>histogram_options=None<span class="p">, </span>legend_fields_to_hides=None<span class="p">, </span>legend_options_fields=None<span class="p">, </span>max_delay=None<span class="p">, </span>minimum_resolution=None<span class="p">, </span>name=None<span class="p">, </span>on_chart_legend_dimension=None<span class="p">, </span>plot_type=None<span class="p">, </span>program_text=None<span class="p">, </span>show_data_markers=None<span class="p">, </span>show_event_lines=None<span class="p">, </span>stacked=None<span class="p">, </span>start_time=None<span class="p">, </span>tags=None<span class="p">, </span>time_range=None<span class="p">, </span>timezone=None<span class="p">, </span>unit_prefix=None<span class="p">, </span>viz_options=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewTimeChart<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#TimeChartArgs">TimeChartArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#TimeChart">TimeChart</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Signalfx/Pulumi.Signalfx..TimeChart.html">TimeChart</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Signalfx/Pulumi.Signalfx.TimeChartArgs.html">TimeChartArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language nodejs %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language python %}}
<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>
{{% /choosable %}}

{{% choosable language go %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language csharp %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resource.</dd>
    <dt class="property-optional" title="Optional">
        <span>args</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The arguments to use to populate this resource's properties.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

#### Resource Arguments




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Axes<wbr>Include<wbr>Zero</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Force the chart to display zero on the y-axes, even if none of the data is near zero.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Axes<wbr>Precision</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Specifies the digits SignalFx displays for values plotted on the chart. Defaults to `3`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Axis<wbr>Left</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartaxisleft">Time<wbr>Chart<wbr>Axis<wbr>Left<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Set of axis options.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Axis<wbr>Right</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartaxisright">Time<wbr>Chart<wbr>Axis<wbr>Right<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Set of axis options.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Color<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Must be `"Dimension"` or `"Metric"`. `"Dimension"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of the chart.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disable<wbr>Sampling</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If `false`, samples a subset of the output MTS, which improves UI performance. `false` by default
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>End<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Event<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timecharteventoption">List&lt;Time<wbr>Chart<wbr>Event<wbr>Option<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Event customization options, associated with a publish statement. You will need to use this to change settings for any `events(…)` statements you use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Histogram<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timecharthistogramoption">List&lt;Time<wbr>Chart<wbr>Histogram<wbr>Option<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Only used when `plot_type` is `"Histogram"`. Histogram specific options.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Legend<wbr>Fields<wbr>To<wbr>Hides</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of properties that should not be displayed in the chart legend (i.e. dimension names). All the properties are visible by default. Deprecated, please use `legend_options_fields`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Please use legend_options_fields{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Legend<wbr>Options<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartlegendoptionsfield">List&lt;Time<wbr>Chart<wbr>Legend<wbr>Options<wbr>Field<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}List of property names and enabled flags that should be displayed in the data table for the chart, in the order provided. This option cannot be used with `legend_fields_to_hide`.
* `property` The name of the property to display. Note the special values of `plot_label` (corresponding with the API's `sf_metric`) which shows the label of the time series `publish()` and `metric` (corresponding with the API's `sf_originatingMetric`) that shows the name of the metric for the time series being displayed.
* `enabled` True or False depending on if you want the property to be shown or hidden.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}How long (in seconds) to wait for late datapoints.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Minimum<wbr>Resolution</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The minimum resolution (in seconds) to use for computing the underlying program.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the chart.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>On<wbr>Chart<wbr>Legend<wbr>Dimension</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Dimensions to show in the on-chart legend. On-chart legend is off unless a dimension is specified. Allowed: `"metric"`, `"plot_label"` and any dimension.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Plot<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The visualization style to use. Must be `"LineChart"`, `"AreaChart"`, `"ColumnChart"`, or `"Histogram"`. Chart level `plot_type` by default.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Program<wbr>Text</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Signalflow program text for the chart. More info [in the SignalFx docs](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Show<wbr>Data<wbr>Markers</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Show markers (circles) for each datapoint used to draw line or area charts. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Show<wbr>Event<wbr>Lines</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether vertical highlight lines should be drawn in the visualizations at times when events occurred. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Stacked</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether area and bar charts in the visualization should be stacked. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Tags associated with the chart
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}signalfx_time_chart.tags is being removed in the next release{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}How many seconds ago from which to display data. For example, the last hour would be `3600`, etc. Conflicts with `start_time` and `end_time`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Time zone that SignalFlow uses as the basis of calendar window transformation methods. For example, if you set "timezone": "Europe/Paris" and then use the transformation sum(cycle="week", cycle_start="Monday") in your chart's SignalFlow program, the calendar window starts on Monday, Paris time. See the [full list of timezones for more](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_supported_signalflow_time_zones). `"UTC"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Unit<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Must be `"Metric"` or `"Binary`". `"Metric"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Viz<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartvizoption">List&lt;Time<wbr>Chart<wbr>Viz<wbr>Option<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Plot-level customization options, associated with a publish statement.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Axes<wbr>Include<wbr>Zero</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Force the chart to display zero on the y-axes, even if none of the data is near zero.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Axes<wbr>Precision</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Specifies the digits SignalFx displays for values plotted on the chart. Defaults to `3`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Axis<wbr>Left</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartaxisleft">*Time<wbr>Chart<wbr>Axis<wbr>Left</a></span>
    </dt>
    <dd>{{% md %}}Set of axis options.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Axis<wbr>Right</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartaxisright">*Time<wbr>Chart<wbr>Axis<wbr>Right</a></span>
    </dt>
    <dd>{{% md %}}Set of axis options.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Color<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Must be `"Dimension"` or `"Metric"`. `"Dimension"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Description of the chart.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disable<wbr>Sampling</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If `false`, samples a subset of the output MTS, which improves UI performance. `false` by default
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>End<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Event<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timecharteventoption">[]Time<wbr>Chart<wbr>Event<wbr>Option</a></span>
    </dt>
    <dd>{{% md %}}Event customization options, associated with a publish statement. You will need to use this to change settings for any `events(…)` statements you use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Histogram<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timecharthistogramoption">[]Time<wbr>Chart<wbr>Histogram<wbr>Option</a></span>
    </dt>
    <dd>{{% md %}}Only used when `plot_type` is `"Histogram"`. Histogram specific options.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Legend<wbr>Fields<wbr>To<wbr>Hides</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of properties that should not be displayed in the chart legend (i.e. dimension names). All the properties are visible by default. Deprecated, please use `legend_options_fields`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Please use legend_options_fields{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Legend<wbr>Options<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartlegendoptionsfield">[]Time<wbr>Chart<wbr>Legend<wbr>Options<wbr>Field</a></span>
    </dt>
    <dd>{{% md %}}List of property names and enabled flags that should be displayed in the data table for the chart, in the order provided. This option cannot be used with `legend_fields_to_hide`.
* `property` The name of the property to display. Note the special values of `plot_label` (corresponding with the API's `sf_metric`) which shows the label of the time series `publish()` and `metric` (corresponding with the API's `sf_originatingMetric`) that shows the name of the metric for the time series being displayed.
* `enabled` True or False depending on if you want the property to be shown or hidden.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}How long (in seconds) to wait for late datapoints.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Minimum<wbr>Resolution</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The minimum resolution (in seconds) to use for computing the underlying program.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the chart.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>On<wbr>Chart<wbr>Legend<wbr>Dimension</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Dimensions to show in the on-chart legend. On-chart legend is off unless a dimension is specified. Allowed: `"metric"`, `"plot_label"` and any dimension.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Plot<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The visualization style to use. Must be `"LineChart"`, `"AreaChart"`, `"ColumnChart"`, or `"Histogram"`. Chart level `plot_type` by default.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Program<wbr>Text</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Signalflow program text for the chart. More info [in the SignalFx docs](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Show<wbr>Data<wbr>Markers</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Show markers (circles) for each datapoint used to draw line or area charts. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Show<wbr>Event<wbr>Lines</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether vertical highlight lines should be drawn in the visualizations at times when events occurred. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Stacked</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether area and bar charts in the visualization should be stacked. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Tags associated with the chart
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}signalfx_time_chart.tags is being removed in the next release{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}How many seconds ago from which to display data. For example, the last hour would be `3600`, etc. Conflicts with `start_time` and `end_time`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Time zone that SignalFlow uses as the basis of calendar window transformation methods. For example, if you set "timezone": "Europe/Paris" and then use the transformation sum(cycle="week", cycle_start="Monday") in your chart's SignalFlow program, the calendar window starts on Monday, Paris time. See the [full list of timezones for more](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_supported_signalflow_time_zones). `"UTC"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Unit<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Must be `"Metric"` or `"Binary`". `"Metric"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Viz<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartvizoption">[]Time<wbr>Chart<wbr>Viz<wbr>Option</a></span>
    </dt>
    <dd>{{% md %}}Plot-level customization options, associated with a publish statement.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>axes<wbr>Include<wbr>Zero</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Force the chart to display zero on the y-axes, even if none of the data is near zero.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>axes<wbr>Precision</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Specifies the digits SignalFx displays for values plotted on the chart. Defaults to `3`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>axis<wbr>Left</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartaxisleft">Time<wbr>Chart<wbr>Axis<wbr>Left?</a></span>
    </dt>
    <dd>{{% md %}}Set of axis options.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>axis<wbr>Right</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartaxisright">Time<wbr>Chart<wbr>Axis<wbr>Right?</a></span>
    </dt>
    <dd>{{% md %}}Set of axis options.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>color<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Must be `"Dimension"` or `"Metric"`. `"Dimension"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of the chart.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disable<wbr>Sampling</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If `false`, samples a subset of the output MTS, which improves UI performance. `false` by default
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>end<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>event<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timecharteventoption">Time<wbr>Chart<wbr>Event<wbr>Option[]?</a></span>
    </dt>
    <dd>{{% md %}}Event customization options, associated with a publish statement. You will need to use this to change settings for any `events(…)` statements you use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>histogram<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timecharthistogramoption">Time<wbr>Chart<wbr>Histogram<wbr>Option[]?</a></span>
    </dt>
    <dd>{{% md %}}Only used when `plot_type` is `"Histogram"`. Histogram specific options.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>legend<wbr>Fields<wbr>To<wbr>Hides</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of properties that should not be displayed in the chart legend (i.e. dimension names). All the properties are visible by default. Deprecated, please use `legend_options_fields`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Please use legend_options_fields{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>legend<wbr>Options<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartlegendoptionsfield">Time<wbr>Chart<wbr>Legend<wbr>Options<wbr>Field[]?</a></span>
    </dt>
    <dd>{{% md %}}List of property names and enabled flags that should be displayed in the data table for the chart, in the order provided. This option cannot be used with `legend_fields_to_hide`.
* `property` The name of the property to display. Note the special values of `plot_label` (corresponding with the API's `sf_metric`) which shows the label of the time series `publish()` and `metric` (corresponding with the API's `sf_originatingMetric`) that shows the name of the metric for the time series being displayed.
* `enabled` True or False depending on if you want the property to be shown or hidden.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}How long (in seconds) to wait for late datapoints.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>minimum<wbr>Resolution</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The minimum resolution (in seconds) to use for computing the underlying program.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the chart.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>on<wbr>Chart<wbr>Legend<wbr>Dimension</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Dimensions to show in the on-chart legend. On-chart legend is off unless a dimension is specified. Allowed: `"metric"`, `"plot_label"` and any dimension.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>plot<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The visualization style to use. Must be `"LineChart"`, `"AreaChart"`, `"ColumnChart"`, or `"Histogram"`. Chart level `plot_type` by default.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>program<wbr>Text</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Signalflow program text for the chart. More info [in the SignalFx docs](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>show<wbr>Data<wbr>Markers</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Show markers (circles) for each datapoint used to draw line or area charts. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>show<wbr>Event<wbr>Lines</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether vertical highlight lines should be drawn in the visualizations at times when events occurred. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>stacked</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether area and bar charts in the visualization should be stacked. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Tags associated with the chart
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}signalfx_time_chart.tags is being removed in the next release{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>time<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}How many seconds ago from which to display data. For example, the last hour would be `3600`, etc. Conflicts with `start_time` and `end_time`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Time zone that SignalFlow uses as the basis of calendar window transformation methods. For example, if you set "timezone": "Europe/Paris" and then use the transformation sum(cycle="week", cycle_start="Monday") in your chart's SignalFlow program, the calendar window starts on Monday, Paris time. See the [full list of timezones for more](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_supported_signalflow_time_zones). `"UTC"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>unit<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Must be `"Metric"` or `"Binary`". `"Metric"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>viz<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartvizoption">Time<wbr>Chart<wbr>Viz<wbr>Option[]?</a></span>
    </dt>
    <dd>{{% md %}}Plot-level customization options, associated with a publish statement.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>axes_<wbr>include_<wbr>zero</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Force the chart to display zero on the y-axes, even if none of the data is near zero.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>axes_<wbr>precision</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Specifies the digits SignalFx displays for values plotted on the chart. Defaults to `3`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>axis_<wbr>left</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartaxisleft">Dict[Time<wbr>Chart<wbr>Axis<wbr>Left]</a></span>
    </dt>
    <dd>{{% md %}}Set of axis options.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>axis_<wbr>right</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartaxisright">Dict[Time<wbr>Chart<wbr>Axis<wbr>Right]</a></span>
    </dt>
    <dd>{{% md %}}Set of axis options.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>color_<wbr>by</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Must be `"Dimension"` or `"Metric"`. `"Dimension"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Description of the chart.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disable_<wbr>sampling</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `false`, samples a subset of the output MTS, which improves UI performance. `false` by default
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>end_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>event_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timecharteventoption">List[Time<wbr>Chart<wbr>Event<wbr>Option]</a></span>
    </dt>
    <dd>{{% md %}}Event customization options, associated with a publish statement. You will need to use this to change settings for any `events(…)` statements you use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>histogram_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timecharthistogramoption">List[Time<wbr>Chart<wbr>Histogram<wbr>Option]</a></span>
    </dt>
    <dd>{{% md %}}Only used when `plot_type` is `"Histogram"`. Histogram specific options.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>legend_<wbr>fields_<wbr>to_<wbr>hides</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of properties that should not be displayed in the chart legend (i.e. dimension names). All the properties are visible by default. Deprecated, please use `legend_options_fields`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Please use legend_options_fields{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>legend_<wbr>options_<wbr>fields</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartlegendoptionsfield">List[Time<wbr>Chart<wbr>Legend<wbr>Options<wbr>Field]</a></span>
    </dt>
    <dd>{{% md %}}List of property names and enabled flags that should be displayed in the data table for the chart, in the order provided. This option cannot be used with `legend_fields_to_hide`.
* `property` The name of the property to display. Note the special values of `plot_label` (corresponding with the API's `sf_metric`) which shows the label of the time series `publish()` and `metric` (corresponding with the API's `sf_originatingMetric`) that shows the name of the metric for the time series being displayed.
* `enabled` True or False depending on if you want the property to be shown or hidden.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max_<wbr>delay</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}How long (in seconds) to wait for late datapoints.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>minimum_<wbr>resolution</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The minimum resolution (in seconds) to use for computing the underlying program.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the chart.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>on_<wbr>chart_<wbr>legend_<wbr>dimension</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Dimensions to show in the on-chart legend. On-chart legend is off unless a dimension is specified. Allowed: `"metric"`, `"plot_label"` and any dimension.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>plot_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The visualization style to use. Must be `"LineChart"`, `"AreaChart"`, `"ColumnChart"`, or `"Histogram"`. Chart level `plot_type` by default.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>program_<wbr>text</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Signalflow program text for the chart. More info [in the SignalFx docs](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>show_<wbr>data_<wbr>markers</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Show markers (circles) for each datapoint used to draw line or area charts. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>show_<wbr>event_<wbr>lines</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether vertical highlight lines should be drawn in the visualizations at times when events occurred. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>stacked</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether area and bar charts in the visualization should be stacked. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>start_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Tags associated with the chart
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}signalfx_time_chart.tags is being removed in the next release{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>time_<wbr>range</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}How many seconds ago from which to display data. For example, the last hour would be `3600`, etc. Conflicts with `start_time` and `end_time`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Time zone that SignalFlow uses as the basis of calendar window transformation methods. For example, if you set "timezone": "Europe/Paris" and then use the transformation sum(cycle="week", cycle_start="Monday") in your chart's SignalFlow program, the calendar window starts on Monday, Paris time. See the [full list of timezones for more](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_supported_signalflow_time_zones). `"UTC"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>unit_<wbr>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Must be `"Metric"` or `"Binary`". `"Metric"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>viz_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartvizoption">List[Time<wbr>Chart<wbr>Viz<wbr>Option]</a></span>
    </dt>
    <dd>{{% md %}}Plot-level customization options, associated with a publish statement.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## TimeChart Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Axes<wbr>Include<wbr>Zero</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Force the chart to display zero on the y-axes, even if none of the data is near zero.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Axes<wbr>Precision</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Specifies the digits SignalFx displays for values plotted on the chart. Defaults to `3`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Axis<wbr>Left</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartaxisleft">Time<wbr>Chart<wbr>Axis<wbr>Left?</a></span>
    </dt>
    <dd>{{% md %}}Set of axis options.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Axis<wbr>Right</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartaxisright">Time<wbr>Chart<wbr>Axis<wbr>Right?</a></span>
    </dt>
    <dd>{{% md %}}Set of axis options.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Color<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Must be `"Dimension"` or `"Metric"`. `"Dimension"` by default.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of the chart.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Disable<wbr>Sampling</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If `false`, samples a subset of the output MTS, which improves UI performance. `false` by default
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>End<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Event<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timecharteventoption">List&lt;Time<wbr>Chart<wbr>Event<wbr>Option&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Event customization options, associated with a publish statement. You will need to use this to change settings for any `events(…)` statements you use.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Histogram<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timecharthistogramoption">List&lt;Time<wbr>Chart<wbr>Histogram<wbr>Option&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Only used when `plot_type` is `"Histogram"`. Histogram specific options.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Legend<wbr>Fields<wbr>To<wbr>Hides</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of properties that should not be displayed in the chart legend (i.e. dimension names). All the properties are visible by default. Deprecated, please use `legend_options_fields`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Please use legend_options_fields{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Legend<wbr>Options<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartlegendoptionsfield">List&lt;Time<wbr>Chart<wbr>Legend<wbr>Options<wbr>Field&gt;?</a></span>
    </dt>
    <dd>{{% md %}}List of property names and enabled flags that should be displayed in the data table for the chart, in the order provided. This option cannot be used with `legend_fields_to_hide`.
* `property` The name of the property to display. Note the special values of `plot_label` (corresponding with the API's `sf_metric`) which shows the label of the time series `publish()` and `metric` (corresponding with the API's `sf_originatingMetric`) that shows the name of the metric for the time series being displayed.
* `enabled` True or False depending on if you want the property to be shown or hidden.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Max<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}How long (in seconds) to wait for late datapoints.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Minimum<wbr>Resolution</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The minimum resolution (in seconds) to use for computing the underlying program.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the chart.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>On<wbr>Chart<wbr>Legend<wbr>Dimension</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Dimensions to show in the on-chart legend. On-chart legend is off unless a dimension is specified. Allowed: `"metric"`, `"plot_label"` and any dimension.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Plot<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The visualization style to use. Must be `"LineChart"`, `"AreaChart"`, `"ColumnChart"`, or `"Histogram"`. Chart level `plot_type` by default.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Program<wbr>Text</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Signalflow program text for the chart. More info [in the SignalFx docs](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Show<wbr>Data<wbr>Markers</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Show markers (circles) for each datapoint used to draw line or area charts. `false` by default.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Show<wbr>Event<wbr>Lines</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether vertical highlight lines should be drawn in the visualizations at times when events occurred. `false` by default.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Stacked</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether area and bar charts in the visualization should be stacked. `false` by default.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Tags associated with the chart
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}signalfx_time_chart.tags is being removed in the next release{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Time<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}How many seconds ago from which to display data. For example, the last hour would be `3600`, etc. Conflicts with `start_time` and `end_time`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Time zone that SignalFlow uses as the basis of calendar window transformation methods. For example, if you set "timezone": "Europe/Paris" and then use the transformation sum(cycle="week", cycle_start="Monday") in your chart's SignalFlow program, the calendar window starts on Monday, Paris time. See the [full list of timezones for more](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_supported_signalflow_time_zones). `"UTC"` by default.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Unit<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Must be `"Metric"` or `"Binary`". `"Metric"` by default.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URL of the chart
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Viz<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartvizoption">List&lt;Time<wbr>Chart<wbr>Viz<wbr>Option&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Plot-level customization options, associated with a publish statement.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Axes<wbr>Include<wbr>Zero</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Force the chart to display zero on the y-axes, even if none of the data is near zero.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Axes<wbr>Precision</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Specifies the digits SignalFx displays for values plotted on the chart. Defaults to `3`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Axis<wbr>Left</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartaxisleft">*Time<wbr>Chart<wbr>Axis<wbr>Left</a></span>
    </dt>
    <dd>{{% md %}}Set of axis options.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Axis<wbr>Right</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartaxisright">*Time<wbr>Chart<wbr>Axis<wbr>Right</a></span>
    </dt>
    <dd>{{% md %}}Set of axis options.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Color<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Must be `"Dimension"` or `"Metric"`. `"Dimension"` by default.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Description of the chart.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Disable<wbr>Sampling</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If `false`, samples a subset of the output MTS, which improves UI performance. `false` by default
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>End<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Event<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timecharteventoption">[]Time<wbr>Chart<wbr>Event<wbr>Option</a></span>
    </dt>
    <dd>{{% md %}}Event customization options, associated with a publish statement. You will need to use this to change settings for any `events(…)` statements you use.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Histogram<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timecharthistogramoption">[]Time<wbr>Chart<wbr>Histogram<wbr>Option</a></span>
    </dt>
    <dd>{{% md %}}Only used when `plot_type` is `"Histogram"`. Histogram specific options.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Legend<wbr>Fields<wbr>To<wbr>Hides</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of properties that should not be displayed in the chart legend (i.e. dimension names). All the properties are visible by default. Deprecated, please use `legend_options_fields`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Please use legend_options_fields{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Legend<wbr>Options<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartlegendoptionsfield">[]Time<wbr>Chart<wbr>Legend<wbr>Options<wbr>Field</a></span>
    </dt>
    <dd>{{% md %}}List of property names and enabled flags that should be displayed in the data table for the chart, in the order provided. This option cannot be used with `legend_fields_to_hide`.
* `property` The name of the property to display. Note the special values of `plot_label` (corresponding with the API's `sf_metric`) which shows the label of the time series `publish()` and `metric` (corresponding with the API's `sf_originatingMetric`) that shows the name of the metric for the time series being displayed.
* `enabled` True or False depending on if you want the property to be shown or hidden.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Max<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}How long (in seconds) to wait for late datapoints.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Minimum<wbr>Resolution</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The minimum resolution (in seconds) to use for computing the underlying program.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the chart.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>On<wbr>Chart<wbr>Legend<wbr>Dimension</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Dimensions to show in the on-chart legend. On-chart legend is off unless a dimension is specified. Allowed: `"metric"`, `"plot_label"` and any dimension.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Plot<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The visualization style to use. Must be `"LineChart"`, `"AreaChart"`, `"ColumnChart"`, or `"Histogram"`. Chart level `plot_type` by default.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Program<wbr>Text</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Signalflow program text for the chart. More info [in the SignalFx docs](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Show<wbr>Data<wbr>Markers</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Show markers (circles) for each datapoint used to draw line or area charts. `false` by default.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Show<wbr>Event<wbr>Lines</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether vertical highlight lines should be drawn in the visualizations at times when events occurred. `false` by default.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Stacked</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether area and bar charts in the visualization should be stacked. `false` by default.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Tags associated with the chart
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}signalfx_time_chart.tags is being removed in the next release{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>Time<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}How many seconds ago from which to display data. For example, the last hour would be `3600`, etc. Conflicts with `start_time` and `end_time`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Time zone that SignalFlow uses as the basis of calendar window transformation methods. For example, if you set "timezone": "Europe/Paris" and then use the transformation sum(cycle="week", cycle_start="Monday") in your chart's SignalFlow program, the calendar window starts on Monday, Paris time. See the [full list of timezones for more](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_supported_signalflow_time_zones). `"UTC"` by default.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Unit<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Must be `"Metric"` or `"Binary`". `"Metric"` by default.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URL of the chart
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Viz<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartvizoption">[]Time<wbr>Chart<wbr>Viz<wbr>Option</a></span>
    </dt>
    <dd>{{% md %}}Plot-level customization options, associated with a publish statement.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>axes<wbr>Include<wbr>Zero</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Force the chart to display zero on the y-axes, even if none of the data is near zero.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>axes<wbr>Precision</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Specifies the digits SignalFx displays for values plotted on the chart. Defaults to `3`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>axis<wbr>Left</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartaxisleft">Time<wbr>Chart<wbr>Axis<wbr>Left?</a></span>
    </dt>
    <dd>{{% md %}}Set of axis options.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>axis<wbr>Right</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartaxisright">Time<wbr>Chart<wbr>Axis<wbr>Right?</a></span>
    </dt>
    <dd>{{% md %}}Set of axis options.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>color<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Must be `"Dimension"` or `"Metric"`. `"Dimension"` by default.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of the chart.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>disable<wbr>Sampling</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If `false`, samples a subset of the output MTS, which improves UI performance. `false` by default
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>end<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>event<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timecharteventoption">Time<wbr>Chart<wbr>Event<wbr>Option[]?</a></span>
    </dt>
    <dd>{{% md %}}Event customization options, associated with a publish statement. You will need to use this to change settings for any `events(…)` statements you use.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>histogram<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timecharthistogramoption">Time<wbr>Chart<wbr>Histogram<wbr>Option[]?</a></span>
    </dt>
    <dd>{{% md %}}Only used when `plot_type` is `"Histogram"`. Histogram specific options.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>legend<wbr>Fields<wbr>To<wbr>Hides</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of properties that should not be displayed in the chart legend (i.e. dimension names). All the properties are visible by default. Deprecated, please use `legend_options_fields`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Please use legend_options_fields{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>legend<wbr>Options<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartlegendoptionsfield">Time<wbr>Chart<wbr>Legend<wbr>Options<wbr>Field[]?</a></span>
    </dt>
    <dd>{{% md %}}List of property names and enabled flags that should be displayed in the data table for the chart, in the order provided. This option cannot be used with `legend_fields_to_hide`.
* `property` The name of the property to display. Note the special values of `plot_label` (corresponding with the API's `sf_metric`) which shows the label of the time series `publish()` and `metric` (corresponding with the API's `sf_originatingMetric`) that shows the name of the metric for the time series being displayed.
* `enabled` True or False depending on if you want the property to be shown or hidden.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>max<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}How long (in seconds) to wait for late datapoints.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>minimum<wbr>Resolution</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The minimum resolution (in seconds) to use for computing the underlying program.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the chart.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>on<wbr>Chart<wbr>Legend<wbr>Dimension</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Dimensions to show in the on-chart legend. On-chart legend is off unless a dimension is specified. Allowed: `"metric"`, `"plot_label"` and any dimension.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>plot<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The visualization style to use. Must be `"LineChart"`, `"AreaChart"`, `"ColumnChart"`, or `"Histogram"`. Chart level `plot_type` by default.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>program<wbr>Text</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Signalflow program text for the chart. More info [in the SignalFx docs](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>show<wbr>Data<wbr>Markers</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Show markers (circles) for each datapoint used to draw line or area charts. `false` by default.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>show<wbr>Event<wbr>Lines</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether vertical highlight lines should be drawn in the visualizations at times when events occurred. `false` by default.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>stacked</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether area and bar charts in the visualization should be stacked. `false` by default.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Tags associated with the chart
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}signalfx_time_chart.tags is being removed in the next release{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>time<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}How many seconds ago from which to display data. For example, the last hour would be `3600`, etc. Conflicts with `start_time` and `end_time`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Time zone that SignalFlow uses as the basis of calendar window transformation methods. For example, if you set "timezone": "Europe/Paris" and then use the transformation sum(cycle="week", cycle_start="Monday") in your chart's SignalFlow program, the calendar window starts on Monday, Paris time. See the [full list of timezones for more](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_supported_signalflow_time_zones). `"UTC"` by default.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>unit<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Must be `"Metric"` or `"Binary`". `"Metric"` by default.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URL of the chart
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>viz<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartvizoption">Time<wbr>Chart<wbr>Viz<wbr>Option[]?</a></span>
    </dt>
    <dd>{{% md %}}Plot-level customization options, associated with a publish statement.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>axes_<wbr>include_<wbr>zero</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Force the chart to display zero on the y-axes, even if none of the data is near zero.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>axes_<wbr>precision</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Specifies the digits SignalFx displays for values plotted on the chart. Defaults to `3`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>axis_<wbr>left</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartaxisleft">Dict[Time<wbr>Chart<wbr>Axis<wbr>Left]</a></span>
    </dt>
    <dd>{{% md %}}Set of axis options.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>axis_<wbr>right</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartaxisright">Dict[Time<wbr>Chart<wbr>Axis<wbr>Right]</a></span>
    </dt>
    <dd>{{% md %}}Set of axis options.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>color_<wbr>by</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Must be `"Dimension"` or `"Metric"`. `"Dimension"` by default.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Description of the chart.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>disable_<wbr>sampling</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `false`, samples a subset of the output MTS, which improves UI performance. `false` by default
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>end_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>event_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timecharteventoption">List[Time<wbr>Chart<wbr>Event<wbr>Option]</a></span>
    </dt>
    <dd>{{% md %}}Event customization options, associated with a publish statement. You will need to use this to change settings for any `events(…)` statements you use.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>histogram_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timecharthistogramoption">List[Time<wbr>Chart<wbr>Histogram<wbr>Option]</a></span>
    </dt>
    <dd>{{% md %}}Only used when `plot_type` is `"Histogram"`. Histogram specific options.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>legend_<wbr>fields_<wbr>to_<wbr>hides</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of properties that should not be displayed in the chart legend (i.e. dimension names). All the properties are visible by default. Deprecated, please use `legend_options_fields`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Please use legend_options_fields{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>legend_<wbr>options_<wbr>fields</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartlegendoptionsfield">List[Time<wbr>Chart<wbr>Legend<wbr>Options<wbr>Field]</a></span>
    </dt>
    <dd>{{% md %}}List of property names and enabled flags that should be displayed in the data table for the chart, in the order provided. This option cannot be used with `legend_fields_to_hide`.
* `property` The name of the property to display. Note the special values of `plot_label` (corresponding with the API's `sf_metric`) which shows the label of the time series `publish()` and `metric` (corresponding with the API's `sf_originatingMetric`) that shows the name of the metric for the time series being displayed.
* `enabled` True or False depending on if you want the property to be shown or hidden.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>max_<wbr>delay</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}How long (in seconds) to wait for late datapoints.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>minimum_<wbr>resolution</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The minimum resolution (in seconds) to use for computing the underlying program.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the chart.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>on_<wbr>chart_<wbr>legend_<wbr>dimension</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Dimensions to show in the on-chart legend. On-chart legend is off unless a dimension is specified. Allowed: `"metric"`, `"plot_label"` and any dimension.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>plot_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The visualization style to use. Must be `"LineChart"`, `"AreaChart"`, `"ColumnChart"`, or `"Histogram"`. Chart level `plot_type` by default.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>program_<wbr>text</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Signalflow program text for the chart. More info [in the SignalFx docs](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>show_<wbr>data_<wbr>markers</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Show markers (circles) for each datapoint used to draw line or area charts. `false` by default.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>show_<wbr>event_<wbr>lines</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether vertical highlight lines should be drawn in the visualizations at times when events occurred. `false` by default.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>stacked</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether area and bar charts in the visualization should be stacked. `false` by default.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>start_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property- property-deprecated"
            title=", Deprecated">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Tags associated with the chart
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}signalfx_time_chart.tags is being removed in the next release{{% /md %}}</p></dd>

    <dt class="property-"
            title="">
        <span>time_<wbr>range</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}How many seconds ago from which to display data. For example, the last hour would be `3600`, etc. Conflicts with `start_time` and `end_time`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Time zone that SignalFlow uses as the basis of calendar window transformation methods. For example, if you set "timezone": "Europe/Paris" and then use the transformation sum(cycle="week", cycle_start="Monday") in your chart's SignalFlow program, the calendar window starts on Monday, Paris time. See the [full list of timezones for more](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_supported_signalflow_time_zones). `"UTC"` by default.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>unit_<wbr>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Must be `"Metric"` or `"Binary`". `"Metric"` by default.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}URL of the chart
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>viz_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartvizoption">List[Time<wbr>Chart<wbr>Viz<wbr>Option]</a></span>
    </dt>
    <dd>{{% md %}}Plot-level customization options, associated with a publish statement.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing TimeChart Resource

Get an existing TimeChart resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/signalfx/#TimeChartState">TimeChartState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/signalfx/#TimeChart">TimeChart</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>axes_include_zero=None<span class="p">, </span>axes_precision=None<span class="p">, </span>axis_left=None<span class="p">, </span>axis_right=None<span class="p">, </span>color_by=None<span class="p">, </span>description=None<span class="p">, </span>disable_sampling=None<span class="p">, </span>end_time=None<span class="p">, </span>event_options=None<span class="p">, </span>histogram_options=None<span class="p">, </span>legend_fields_to_hides=None<span class="p">, </span>legend_options_fields=None<span class="p">, </span>max_delay=None<span class="p">, </span>minimum_resolution=None<span class="p">, </span>name=None<span class="p">, </span>on_chart_legend_dimension=None<span class="p">, </span>plot_type=None<span class="p">, </span>program_text=None<span class="p">, </span>show_data_markers=None<span class="p">, </span>show_event_lines=None<span class="p">, </span>stacked=None<span class="p">, </span>start_time=None<span class="p">, </span>tags=None<span class="p">, </span>time_range=None<span class="p">, </span>timezone=None<span class="p">, </span>unit_prefix=None<span class="p">, </span>url=None<span class="p">, </span>viz_options=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetTimeChart<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#TimeChartState">TimeChartState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#TimeChart">TimeChart</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Signalfx/Pulumi.Signalfx..TimeChart.html">TimeChart</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Signalfx/Pulumi.Signalfx..TimeChartState.html">TimeChartState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language nodejs %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language python %}}
<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>resource_name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Optional">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
</dl>
{{% /choosable %}}

{{% choosable language go %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

{{% choosable language csharp %}}

<dl class="resources-properties">
    <dt class="property-required" title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The unique name of the resulting resource.</dd>
    <dt class="property-required" title="Required">
        <span>id</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>The <em>unique</em> provider ID of the resource to lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>state</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>Any extra arguments used during the lookup.</dd>
    <dt class="property-optional" title="Optional">
        <span>opts</span>
        <span class="property-indicator"></span>
    </dt>
    <dd>A bag of options that control this resource's behavior.</dd>
</dl>

{{% /choosable %}}

The following state arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Axes<wbr>Include<wbr>Zero</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Force the chart to display zero on the y-axes, even if none of the data is near zero.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Axes<wbr>Precision</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Specifies the digits SignalFx displays for values plotted on the chart. Defaults to `3`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Axis<wbr>Left</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartaxisleft">Time<wbr>Chart<wbr>Axis<wbr>Left<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Set of axis options.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Axis<wbr>Right</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartaxisright">Time<wbr>Chart<wbr>Axis<wbr>Right<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Set of axis options.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Color<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Must be `"Dimension"` or `"Metric"`. `"Dimension"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of the chart.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disable<wbr>Sampling</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}If `false`, samples a subset of the output MTS, which improves UI performance. `false` by default
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>End<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Event<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timecharteventoption">List&lt;Time<wbr>Chart<wbr>Event<wbr>Option<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Event customization options, associated with a publish statement. You will need to use this to change settings for any `events(…)` statements you use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Histogram<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timecharthistogramoption">List&lt;Time<wbr>Chart<wbr>Histogram<wbr>Option<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Only used when `plot_type` is `"Histogram"`. Histogram specific options.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Legend<wbr>Fields<wbr>To<wbr>Hides</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of properties that should not be displayed in the chart legend (i.e. dimension names). All the properties are visible by default. Deprecated, please use `legend_options_fields`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Please use legend_options_fields{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Legend<wbr>Options<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartlegendoptionsfield">List&lt;Time<wbr>Chart<wbr>Legend<wbr>Options<wbr>Field<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}List of property names and enabled flags that should be displayed in the data table for the chart, in the order provided. This option cannot be used with `legend_fields_to_hide`.
* `property` The name of the property to display. Note the special values of `plot_label` (corresponding with the API's `sf_metric`) which shows the label of the time series `publish()` and `metric` (corresponding with the API's `sf_originatingMetric`) that shows the name of the metric for the time series being displayed.
* `enabled` True or False depending on if you want the property to be shown or hidden.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}How long (in seconds) to wait for late datapoints.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Minimum<wbr>Resolution</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The minimum resolution (in seconds) to use for computing the underlying program.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the chart.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>On<wbr>Chart<wbr>Legend<wbr>Dimension</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Dimensions to show in the on-chart legend. On-chart legend is off unless a dimension is specified. Allowed: `"metric"`, `"plot_label"` and any dimension.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Plot<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The visualization style to use. Must be `"LineChart"`, `"AreaChart"`, `"ColumnChart"`, or `"Histogram"`. Chart level `plot_type` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Program<wbr>Text</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Signalflow program text for the chart. More info [in the SignalFx docs](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Show<wbr>Data<wbr>Markers</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Show markers (circles) for each datapoint used to draw line or area charts. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Show<wbr>Event<wbr>Lines</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether vertical highlight lines should be drawn in the visualizations at times when events occurred. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Stacked</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether area and bar charts in the visualization should be stacked. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Tags associated with the chart
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}signalfx_time_chart.tags is being removed in the next release{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}How many seconds ago from which to display data. For example, the last hour would be `3600`, etc. Conflicts with `start_time` and `end_time`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Time zone that SignalFlow uses as the basis of calendar window transformation methods. For example, if you set "timezone": "Europe/Paris" and then use the transformation sum(cycle="week", cycle_start="Monday") in your chart's SignalFlow program, the calendar window starts on Monday, Paris time. See the [full list of timezones for more](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_supported_signalflow_time_zones). `"UTC"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Unit<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Must be `"Metric"` or `"Binary`". `"Metric"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}URL of the chart
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Viz<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartvizoption">List&lt;Time<wbr>Chart<wbr>Viz<wbr>Option<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Plot-level customization options, associated with a publish statement.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Axes<wbr>Include<wbr>Zero</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Force the chart to display zero on the y-axes, even if none of the data is near zero.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Axes<wbr>Precision</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Specifies the digits SignalFx displays for values plotted on the chart. Defaults to `3`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Axis<wbr>Left</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartaxisleft">*Time<wbr>Chart<wbr>Axis<wbr>Left</a></span>
    </dt>
    <dd>{{% md %}}Set of axis options.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Axis<wbr>Right</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartaxisright">*Time<wbr>Chart<wbr>Axis<wbr>Right</a></span>
    </dt>
    <dd>{{% md %}}Set of axis options.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Color<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Must be `"Dimension"` or `"Metric"`. `"Dimension"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Description of the chart.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disable<wbr>Sampling</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}If `false`, samples a subset of the output MTS, which improves UI performance. `false` by default
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>End<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Event<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timecharteventoption">[]Time<wbr>Chart<wbr>Event<wbr>Option</a></span>
    </dt>
    <dd>{{% md %}}Event customization options, associated with a publish statement. You will need to use this to change settings for any `events(…)` statements you use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Histogram<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timecharthistogramoption">[]Time<wbr>Chart<wbr>Histogram<wbr>Option</a></span>
    </dt>
    <dd>{{% md %}}Only used when `plot_type` is `"Histogram"`. Histogram specific options.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Legend<wbr>Fields<wbr>To<wbr>Hides</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of properties that should not be displayed in the chart legend (i.e. dimension names). All the properties are visible by default. Deprecated, please use `legend_options_fields`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Please use legend_options_fields{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Legend<wbr>Options<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartlegendoptionsfield">[]Time<wbr>Chart<wbr>Legend<wbr>Options<wbr>Field</a></span>
    </dt>
    <dd>{{% md %}}List of property names and enabled flags that should be displayed in the data table for the chart, in the order provided. This option cannot be used with `legend_fields_to_hide`.
* `property` The name of the property to display. Note the special values of `plot_label` (corresponding with the API's `sf_metric`) which shows the label of the time series `publish()` and `metric` (corresponding with the API's `sf_originatingMetric`) that shows the name of the metric for the time series being displayed.
* `enabled` True or False depending on if you want the property to be shown or hidden.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}How long (in seconds) to wait for late datapoints.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Minimum<wbr>Resolution</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The minimum resolution (in seconds) to use for computing the underlying program.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the chart.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>On<wbr>Chart<wbr>Legend<wbr>Dimension</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Dimensions to show in the on-chart legend. On-chart legend is off unless a dimension is specified. Allowed: `"metric"`, `"plot_label"` and any dimension.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Plot<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The visualization style to use. Must be `"LineChart"`, `"AreaChart"`, `"ColumnChart"`, or `"Histogram"`. Chart level `plot_type` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Program<wbr>Text</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Signalflow program text for the chart. More info [in the SignalFx docs](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Show<wbr>Data<wbr>Markers</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Show markers (circles) for each datapoint used to draw line or area charts. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Show<wbr>Event<wbr>Lines</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether vertical highlight lines should be drawn in the visualizations at times when events occurred. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Stacked</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether area and bar charts in the visualization should be stacked. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Tags associated with the chart
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}signalfx_time_chart.tags is being removed in the next release{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}How many seconds ago from which to display data. For example, the last hour would be `3600`, etc. Conflicts with `start_time` and `end_time`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Time zone that SignalFlow uses as the basis of calendar window transformation methods. For example, if you set "timezone": "Europe/Paris" and then use the transformation sum(cycle="week", cycle_start="Monday") in your chart's SignalFlow program, the calendar window starts on Monday, Paris time. See the [full list of timezones for more](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_supported_signalflow_time_zones). `"UTC"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Unit<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Must be `"Metric"` or `"Binary`". `"Metric"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}URL of the chart
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Viz<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartvizoption">[]Time<wbr>Chart<wbr>Viz<wbr>Option</a></span>
    </dt>
    <dd>{{% md %}}Plot-level customization options, associated with a publish statement.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>axes<wbr>Include<wbr>Zero</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Force the chart to display zero on the y-axes, even if none of the data is near zero.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>axes<wbr>Precision</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Specifies the digits SignalFx displays for values plotted on the chart. Defaults to `3`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>axis<wbr>Left</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartaxisleft">Time<wbr>Chart<wbr>Axis<wbr>Left?</a></span>
    </dt>
    <dd>{{% md %}}Set of axis options.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>axis<wbr>Right</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartaxisright">Time<wbr>Chart<wbr>Axis<wbr>Right?</a></span>
    </dt>
    <dd>{{% md %}}Set of axis options.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>color<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Must be `"Dimension"` or `"Metric"`. `"Dimension"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of the chart.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disable<wbr>Sampling</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}If `false`, samples a subset of the output MTS, which improves UI performance. `false` by default
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>end<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>event<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timecharteventoption">Time<wbr>Chart<wbr>Event<wbr>Option[]?</a></span>
    </dt>
    <dd>{{% md %}}Event customization options, associated with a publish statement. You will need to use this to change settings for any `events(…)` statements you use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>histogram<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timecharthistogramoption">Time<wbr>Chart<wbr>Histogram<wbr>Option[]?</a></span>
    </dt>
    <dd>{{% md %}}Only used when `plot_type` is `"Histogram"`. Histogram specific options.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>legend<wbr>Fields<wbr>To<wbr>Hides</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of properties that should not be displayed in the chart legend (i.e. dimension names). All the properties are visible by default. Deprecated, please use `legend_options_fields`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Please use legend_options_fields{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>legend<wbr>Options<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartlegendoptionsfield">Time<wbr>Chart<wbr>Legend<wbr>Options<wbr>Field[]?</a></span>
    </dt>
    <dd>{{% md %}}List of property names and enabled flags that should be displayed in the data table for the chart, in the order provided. This option cannot be used with `legend_fields_to_hide`.
* `property` The name of the property to display. Note the special values of `plot_label` (corresponding with the API's `sf_metric`) which shows the label of the time series `publish()` and `metric` (corresponding with the API's `sf_originatingMetric`) that shows the name of the metric for the time series being displayed.
* `enabled` True or False depending on if you want the property to be shown or hidden.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}How long (in seconds) to wait for late datapoints.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>minimum<wbr>Resolution</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The minimum resolution (in seconds) to use for computing the underlying program.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the chart.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>on<wbr>Chart<wbr>Legend<wbr>Dimension</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Dimensions to show in the on-chart legend. On-chart legend is off unless a dimension is specified. Allowed: `"metric"`, `"plot_label"` and any dimension.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>plot<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The visualization style to use. Must be `"LineChart"`, `"AreaChart"`, `"ColumnChart"`, or `"Histogram"`. Chart level `plot_type` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>program<wbr>Text</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Signalflow program text for the chart. More info [in the SignalFx docs](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>show<wbr>Data<wbr>Markers</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Show markers (circles) for each datapoint used to draw line or area charts. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>show<wbr>Event<wbr>Lines</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether vertical highlight lines should be drawn in the visualizations at times when events occurred. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>stacked</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether area and bar charts in the visualization should be stacked. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Tags associated with the chart
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}signalfx_time_chart.tags is being removed in the next release{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>time<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}How many seconds ago from which to display data. For example, the last hour would be `3600`, etc. Conflicts with `start_time` and `end_time`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Time zone that SignalFlow uses as the basis of calendar window transformation methods. For example, if you set "timezone": "Europe/Paris" and then use the transformation sum(cycle="week", cycle_start="Monday") in your chart's SignalFlow program, the calendar window starts on Monday, Paris time. See the [full list of timezones for more](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_supported_signalflow_time_zones). `"UTC"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>unit<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Must be `"Metric"` or `"Binary`". `"Metric"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}URL of the chart
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>viz<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartvizoption">Time<wbr>Chart<wbr>Viz<wbr>Option[]?</a></span>
    </dt>
    <dd>{{% md %}}Plot-level customization options, associated with a publish statement.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>axes_<wbr>include_<wbr>zero</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Force the chart to display zero on the y-axes, even if none of the data is near zero.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>axes_<wbr>precision</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Specifies the digits SignalFx displays for values plotted on the chart. Defaults to `3`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>axis_<wbr>left</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartaxisleft">Dict[Time<wbr>Chart<wbr>Axis<wbr>Left]</a></span>
    </dt>
    <dd>{{% md %}}Set of axis options.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>axis_<wbr>right</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartaxisright">Dict[Time<wbr>Chart<wbr>Axis<wbr>Right]</a></span>
    </dt>
    <dd>{{% md %}}Set of axis options.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>color_<wbr>by</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Must be `"Dimension"` or `"Metric"`. `"Dimension"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Description of the chart.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disable_<wbr>sampling</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `false`, samples a subset of the output MTS, which improves UI performance. `false` by default
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>end_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>event_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timecharteventoption">List[Time<wbr>Chart<wbr>Event<wbr>Option]</a></span>
    </dt>
    <dd>{{% md %}}Event customization options, associated with a publish statement. You will need to use this to change settings for any `events(…)` statements you use.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>histogram_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timecharthistogramoption">List[Time<wbr>Chart<wbr>Histogram<wbr>Option]</a></span>
    </dt>
    <dd>{{% md %}}Only used when `plot_type` is `"Histogram"`. Histogram specific options.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>legend_<wbr>fields_<wbr>to_<wbr>hides</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of properties that should not be displayed in the chart legend (i.e. dimension names). All the properties are visible by default. Deprecated, please use `legend_options_fields`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Please use legend_options_fields{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>legend_<wbr>options_<wbr>fields</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartlegendoptionsfield">List[Time<wbr>Chart<wbr>Legend<wbr>Options<wbr>Field]</a></span>
    </dt>
    <dd>{{% md %}}List of property names and enabled flags that should be displayed in the data table for the chart, in the order provided. This option cannot be used with `legend_fields_to_hide`.
* `property` The name of the property to display. Note the special values of `plot_label` (corresponding with the API's `sf_metric`) which shows the label of the time series `publish()` and `metric` (corresponding with the API's `sf_originatingMetric`) that shows the name of the metric for the time series being displayed.
* `enabled` True or False depending on if you want the property to be shown or hidden.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max_<wbr>delay</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}How long (in seconds) to wait for late datapoints.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>minimum_<wbr>resolution</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The minimum resolution (in seconds) to use for computing the underlying program.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the chart.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>on_<wbr>chart_<wbr>legend_<wbr>dimension</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Dimensions to show in the on-chart legend. On-chart legend is off unless a dimension is specified. Allowed: `"metric"`, `"plot_label"` and any dimension.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>plot_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The visualization style to use. Must be `"LineChart"`, `"AreaChart"`, `"ColumnChart"`, or `"Histogram"`. Chart level `plot_type` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>program_<wbr>text</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Signalflow program text for the chart. More info [in the SignalFx docs](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>show_<wbr>data_<wbr>markers</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Show markers (circles) for each datapoint used to draw line or area charts. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>show_<wbr>event_<wbr>lines</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether vertical highlight lines should be drawn in the visualizations at times when events occurred. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>stacked</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether area and bar charts in the visualization should be stacked. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>start_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Tags associated with the chart
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}signalfx_time_chart.tags is being removed in the next release{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>time_<wbr>range</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}How many seconds ago from which to display data. For example, the last hour would be `3600`, etc. Conflicts with `start_time` and `end_time`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timezone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Time zone that SignalFlow uses as the basis of calendar window transformation methods. For example, if you set "timezone": "Europe/Paris" and then use the transformation sum(cycle="week", cycle_start="Monday") in your chart's SignalFlow program, the calendar window starts on Monday, Paris time. See the [full list of timezones for more](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_supported_signalflow_time_zones). `"UTC"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>unit_<wbr>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Must be `"Metric"` or `"Binary`". `"Metric"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}URL of the chart
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>viz_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartvizoption">List[Time<wbr>Chart<wbr>Viz<wbr>Option]</a></span>
    </dt>
    <dd>{{% md %}}Plot-level customization options, associated with a publish statement.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Time<wbr>Chart<wbr>Axis<wbr>Left</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/input/#TimeChartAxisLeft">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/output/#TimeChartAxisLeft">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#TimeChartAxisLeftArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#TimeChartAxisLeftOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>High<wbr>Watermark</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}A line to draw as a high watermark.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>High<wbr>Watermark<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A label to attach to the high watermark line.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Label used in the publish statement that displays the event query you want to customize.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Low<wbr>Watermark</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}A line to draw as a low watermark.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Low<wbr>Watermark<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A label to attach to the low watermark line.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}The maximum value for the right axis.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}The minimum value for the right axis.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Watermarks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartaxisleftwatermark">List&lt;Time<wbr>Chart<wbr>Axis<wbr>Left<wbr>Watermark<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>High<wbr>Watermark</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}A line to draw as a high watermark.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>High<wbr>Watermark<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A label to attach to the high watermark line.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Label used in the publish statement that displays the event query you want to customize.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Low<wbr>Watermark</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}A line to draw as a low watermark.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Low<wbr>Watermark<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A label to attach to the low watermark line.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}The maximum value for the right axis.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}The minimum value for the right axis.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Watermarks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartaxisleftwatermark">[]Time<wbr>Chart<wbr>Axis<wbr>Left<wbr>Watermark</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>high<wbr>Watermark</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}A line to draw as a high watermark.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>high<wbr>Watermark<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A label to attach to the high watermark line.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Label used in the publish statement that displays the event query you want to customize.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>low<wbr>Watermark</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}A line to draw as a low watermark.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>low<wbr>Watermark<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A label to attach to the low watermark line.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum value for the right axis.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The minimum value for the right axis.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>watermarks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartaxisleftwatermark">Time<wbr>Chart<wbr>Axis<wbr>Left<wbr>Watermark[]?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>high<wbr>Watermark</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}A line to draw as a high watermark.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>high<wbr>Watermark<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A label to attach to the high watermark line.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>label</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Label used in the publish statement that displays the event query you want to customize.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>low<wbr>Watermark</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}A line to draw as a low watermark.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>low<wbr>Watermark<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A label to attach to the low watermark line.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum value for the right axis.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The minimum value for the right axis.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>watermarks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartaxisleftwatermark">List[Time<wbr>Chart<wbr>Axis<wbr>Left<wbr>Watermark]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Time<wbr>Chart<wbr>Axis<wbr>Left<wbr>Watermark</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/input/#TimeChartAxisLeftWatermark">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/output/#TimeChartAxisLeftWatermark">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#TimeChartAxisLeftWatermarkArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#TimeChartAxisLeftWatermarkOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Label used in the publish statement that displays the event query you want to customize.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">double</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Label used in the publish statement that displays the event query you want to customize.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">float64</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Label used in the publish statement that displays the event query you want to customize.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>label</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Label used in the publish statement that displays the event query you want to customize.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Time<wbr>Chart<wbr>Axis<wbr>Right</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/input/#TimeChartAxisRight">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/output/#TimeChartAxisRight">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#TimeChartAxisRightArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#TimeChartAxisRightOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>High<wbr>Watermark</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}A line to draw as a high watermark.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>High<wbr>Watermark<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A label to attach to the high watermark line.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Label used in the publish statement that displays the event query you want to customize.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Low<wbr>Watermark</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}A line to draw as a low watermark.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Low<wbr>Watermark<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A label to attach to the low watermark line.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}The maximum value for the right axis.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}The minimum value for the right axis.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Watermarks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartaxisrightwatermark">List&lt;Time<wbr>Chart<wbr>Axis<wbr>Right<wbr>Watermark<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>High<wbr>Watermark</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}A line to draw as a high watermark.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>High<wbr>Watermark<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A label to attach to the high watermark line.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Label used in the publish statement that displays the event query you want to customize.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Low<wbr>Watermark</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}A line to draw as a low watermark.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Low<wbr>Watermark<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A label to attach to the low watermark line.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}The maximum value for the right axis.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}The minimum value for the right axis.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Watermarks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartaxisrightwatermark">[]Time<wbr>Chart<wbr>Axis<wbr>Right<wbr>Watermark</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>high<wbr>Watermark</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}A line to draw as a high watermark.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>high<wbr>Watermark<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A label to attach to the high watermark line.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Label used in the publish statement that displays the event query you want to customize.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>low<wbr>Watermark</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}A line to draw as a low watermark.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>low<wbr>Watermark<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A label to attach to the low watermark line.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The maximum value for the right axis.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The minimum value for the right axis.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>watermarks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartaxisrightwatermark">Time<wbr>Chart<wbr>Axis<wbr>Right<wbr>Watermark[]?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>high<wbr>Watermark</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}A line to draw as a high watermark.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>high<wbr>Watermark<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A label to attach to the high watermark line.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>label</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Label used in the publish statement that displays the event query you want to customize.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>low<wbr>Watermark</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}A line to draw as a low watermark.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>low<wbr>Watermark<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A label to attach to the low watermark line.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum value for the right axis.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The minimum value for the right axis.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>watermarks</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#timechartaxisrightwatermark">List[Time<wbr>Chart<wbr>Axis<wbr>Right<wbr>Watermark]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Time<wbr>Chart<wbr>Axis<wbr>Right<wbr>Watermark</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/input/#TimeChartAxisRightWatermark">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/output/#TimeChartAxisRightWatermark">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#TimeChartAxisRightWatermarkArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#TimeChartAxisRightWatermarkOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Label used in the publish statement that displays the event query you want to customize.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">double</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Label used in the publish statement that displays the event query you want to customize.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">float64</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Label used in the publish statement that displays the event query you want to customize.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>label</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Label used in the publish statement that displays the event query you want to customize.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Time<wbr>Chart<wbr>Event<wbr>Option</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/input/#TimeChartEventOption">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/output/#TimeChartEventOption">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#TimeChartEventOptionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#TimeChartEventOptionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Color</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Color to use : gray, blue, azure, navy, brown, orange, yellow, iris, magenta, pink, purple, violet, lilac, emerald, green, aquamarine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies an alternate value for the Plot Name column of the Data Table associated with the chart.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Label used in the publish statement that displays the event query you want to customize.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Color</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Color to use : gray, blue, azure, navy, brown, orange, yellow, iris, magenta, pink, purple, violet, lilac, emerald, green, aquamarine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies an alternate value for the Plot Name column of the Data Table associated with the chart.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Label used in the publish statement that displays the event query you want to customize.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>color</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Color to use : gray, blue, azure, navy, brown, orange, yellow, iris, magenta, pink, purple, violet, lilac, emerald, green, aquamarine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies an alternate value for the Plot Name column of the Data Table associated with the chart.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Label used in the publish statement that displays the event query you want to customize.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>color</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Color to use : gray, blue, azure, navy, brown, orange, yellow, iris, magenta, pink, purple, violet, lilac, emerald, green, aquamarine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies an alternate value for the Plot Name column of the Data Table associated with the chart.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>label</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Label used in the publish statement that displays the event query you want to customize.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Time<wbr>Chart<wbr>Histogram<wbr>Option</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/input/#TimeChartHistogramOption">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/output/#TimeChartHistogramOption">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#TimeChartHistogramOptionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#TimeChartHistogramOptionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Color<wbr>Theme</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Color to use : gray, blue, azure, navy, brown, orange, yellow, iris, magenta, pink, purple, violet, lilac, emerald, green, aquamarine, red, gold, greenyellow, chartreuse, jade
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Color<wbr>Theme</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Color to use : gray, blue, azure, navy, brown, orange, yellow, iris, magenta, pink, purple, violet, lilac, emerald, green, aquamarine, red, gold, greenyellow, chartreuse, jade
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>color<wbr>Theme</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Color to use : gray, blue, azure, navy, brown, orange, yellow, iris, magenta, pink, purple, violet, lilac, emerald, green, aquamarine, red, gold, greenyellow, chartreuse, jade
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>color<wbr>Theme</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Color to use : gray, blue, azure, navy, brown, orange, yellow, iris, magenta, pink, purple, violet, lilac, emerald, green, aquamarine, red, gold, greenyellow, chartreuse, jade
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Time<wbr>Chart<wbr>Legend<wbr>Options<wbr>Field</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/input/#TimeChartLegendOptionsField">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/output/#TimeChartLegendOptionsField">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#TimeChartLegendOptionsFieldArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#TimeChartLegendOptionsFieldOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Property</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Property</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>property</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>property</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Time<wbr>Chart<wbr>Viz<wbr>Option</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/input/#TimeChartVizOption">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/output/#TimeChartVizOption">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#TimeChartVizOptionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#TimeChartVizOptionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Axis</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Y-axis associated with values for this plot. Must be either `right` or `left`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Color</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Color to use : gray, blue, azure, navy, brown, orange, yellow, iris, magenta, pink, purple, violet, lilac, emerald, green, aquamarine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies an alternate value for the Plot Name column of the Data Table associated with the chart.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Label used in the publish statement that displays the event query you want to customize.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Plot<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The visualization style to use. Must be `"LineChart"`, `"AreaChart"`, `"ColumnChart"`, or `"Histogram"`. Chart level `plot_type` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value<wbr>Suffix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A unit to attach to this plot. Units support automatic scaling (eg thousands of bytes will be displayed as kilobytes). Values values are `Bit, Kilobit, Megabit, Gigabit, Terabit, Petabit, Exabit, Zettabit, Yottabit, Byte, Kibibyte, Mebibyte, Gigibyte, Tebibyte, Pebibyte, Exbibyte, Zebibyte, Yobibyte, Nanosecond, Microsecond, Millisecond, Second, Minute, Hour, Day, Week`.
* `value_prefix`, `value_suffix` - (Optional) Arbitrary prefix/suffix to display with the value of this plot.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Axis</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Y-axis associated with values for this plot. Must be either `right` or `left`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Color</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Color to use : gray, blue, azure, navy, brown, orange, yellow, iris, magenta, pink, purple, violet, lilac, emerald, green, aquamarine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies an alternate value for the Plot Name column of the Data Table associated with the chart.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Label used in the publish statement that displays the event query you want to customize.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Plot<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The visualization style to use. Must be `"LineChart"`, `"AreaChart"`, `"ColumnChart"`, or `"Histogram"`. Chart level `plot_type` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value<wbr>Suffix</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A unit to attach to this plot. Units support automatic scaling (eg thousands of bytes will be displayed as kilobytes). Values values are `Bit, Kilobit, Megabit, Gigabit, Terabit, Petabit, Exabit, Zettabit, Yottabit, Byte, Kibibyte, Mebibyte, Gigibyte, Tebibyte, Pebibyte, Exbibyte, Zebibyte, Yobibyte, Nanosecond, Microsecond, Millisecond, Second, Minute, Hour, Day, Week`.
* `value_prefix`, `value_suffix` - (Optional) Arbitrary prefix/suffix to display with the value of this plot.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>axis</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Y-axis associated with values for this plot. Must be either `right` or `left`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>color</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Color to use : gray, blue, azure, navy, brown, orange, yellow, iris, magenta, pink, purple, violet, lilac, emerald, green, aquamarine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies an alternate value for the Plot Name column of the Data Table associated with the chart.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Label used in the publish statement that displays the event query you want to customize.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>plot<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The visualization style to use. Must be `"LineChart"`, `"AreaChart"`, `"ColumnChart"`, or `"Histogram"`. Chart level `plot_type` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value<wbr>Suffix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A unit to attach to this plot. Units support automatic scaling (eg thousands of bytes will be displayed as kilobytes). Values values are `Bit, Kilobit, Megabit, Gigabit, Terabit, Petabit, Exabit, Zettabit, Yottabit, Byte, Kibibyte, Mebibyte, Gigibyte, Tebibyte, Pebibyte, Exbibyte, Zebibyte, Yobibyte, Nanosecond, Microsecond, Millisecond, Second, Minute, Hour, Day, Week`.
* `value_prefix`, `value_suffix` - (Optional) Arbitrary prefix/suffix to display with the value of this plot.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>axis</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Y-axis associated with values for this plot. Must be either `right` or `left`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>color</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Color to use : gray, blue, azure, navy, brown, orange, yellow, iris, magenta, pink, purple, violet, lilac, emerald, green, aquamarine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies an alternate value for the Plot Name column of the Data Table associated with the chart.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>label</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Label used in the publish statement that displays the event query you want to customize.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>plot_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The visualization style to use. Must be `"LineChart"`, `"AreaChart"`, `"ColumnChart"`, or `"Histogram"`. Chart level `plot_type` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value<wbr>Suffix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A unit to attach to this plot. Units support automatic scaling (eg thousands of bytes will be displayed as kilobytes). Values values are `Bit, Kilobit, Megabit, Gigabit, Terabit, Petabit, Exabit, Zettabit, Yottabit, Byte, Kibibyte, Mebibyte, Gigibyte, Tebibyte, Pebibyte, Exbibyte, Zebibyte, Yobibyte, Nanosecond, Microsecond, Millisecond, Second, Minute, Hour, Day, Week`.
* `value_prefix`, `value_suffix` - (Optional) Arbitrary prefix/suffix to display with the value of this plot.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-signalfx">https://github.com/pulumi/pulumi-signalfx</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

