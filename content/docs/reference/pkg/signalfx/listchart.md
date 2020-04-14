
---
title: "ListChart"
block_external_search_index: true
---



This chart type displays current data values in a list format.

The name of each value in the chart reflects the name of the plot and any associated dimensions. We recommend you click the Pencil icon and give the plot a meaningful name, as in plot B below. Otherwise, just the raw metric name will be displayed on the chart, as in plot A below.


## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as signalfx from "@pulumi/signalfx";

const mylistchart0 = new signalfx.ListChart("mylistchart0", {
    colorBy: "Metric",
    description: "Very cool List Chart",
    disableSampling: true,
    legendOptionsFields: [
        {
            enabled: false,
            property: "collector",
        },
        {
            enabled: true,
            property: "cluster_name",
        },
        {
            enabled: true,
            property: "role",
        },
        {
            enabled: false,
            property: "collector",
        },
        {
            enabled: false,
            property: "host",
        },
    ],
    maxDelay: 2,
    maxPrecision: 2,
    programText: `myfilters = filter("cluster_name", "prod") and filter("role", "search")
data("cpu.total.idle", filter=myfilters).publish()
`,
    refreshInterval: 1,
    sortBy: "-value",
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-signalfx/blob/master/website/docs/r/list_chart.html.markdown.



## Create a ListChart Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/signalfx/#ListChart">ListChart</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/signalfx/#ListChartArgs">ListChartArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">ListChart</span><span class="p">(resource_name, opts=None, </span>color_by=None<span class="p">, </span>color_scales=None<span class="p">, </span>description=None<span class="p">, </span>disable_sampling=None<span class="p">, </span>end_time=None<span class="p">, </span>legend_fields_to_hides=None<span class="p">, </span>legend_options_fields=None<span class="p">, </span>max_delay=None<span class="p">, </span>max_precision=None<span class="p">, </span>name=None<span class="p">, </span>program_text=None<span class="p">, </span>refresh_interval=None<span class="p">, </span>secondary_visualization=None<span class="p">, </span>sort_by=None<span class="p">, </span>start_time=None<span class="p">, </span>time_range=None<span class="p">, </span>unit_prefix=None<span class="p">, </span>viz_options=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewListChart<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#ListChartArgs">ListChartArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#ListChart">ListChart</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Signalfx/Pulumi.Signalfx.ListChart.html">ListChart</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Signalfx/Pulumi.SignalFx.ListChartArgs.html">ListChartArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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

    <dt class="property-required"
            title="Required">
        <span>Program<wbr>Text</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Signalflow program text for the chart. More info[in the SignalFx docs](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Color<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Must be one of `"Scale"`, `"Dimension"` or `"Metric"`. `"Dimension"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Color<wbr>Scales</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listchartcolorscale">List&lt;Pulumi.<wbr>Signal<wbr>Fx.<wbr>Inputs.<wbr>List<wbr>Chart<wbr>Color<wbr>Scale<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}Single color range including both the color to display for that range and the borders of the range. Example: `[{ gt = 60, color = "blue" }, { lte = 60, color = "yellow" }]`. Look at this [link](https://docs.signalfx.com/en/latest/charts/chart-options-tab.html).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Description of the chart.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disable<wbr>Sampling</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `false`, samples a subset of the output MTS, which improves UI performance. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>End<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Legend<wbr>Fields<wbr>To<wbr>Hides</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;</span>
    </dt>
    <dd>{{% md %}}List of properties that should not be displayed in the chart legend (i.e. dimension names). All the properties are visible by default. Deprecated, please use `legend_options_fields`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Please use legend_options_fields{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Legend<wbr>Options<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listchartlegendoptionsfield">List&lt;Pulumi.<wbr>Signal<wbr>Fx.<wbr>Inputs.<wbr>List<wbr>Chart<wbr>Legend<wbr>Options<wbr>Field<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}List of property names and enabled flags that should be displayed in the data table for the chart, in the order provided. This option cannot be used with `legend_fields_to_hide`.
* `property` The name of the property to display. Note the special values of `plot_label` (corresponding with the API's `sf_metric`) which shows the label of the time series `publish()` and `metric` (corresponding with the API's `sf_originatingMetric`) that shows the name of the metric for the time series being displayed.
* `enabled` True or False depending on if you want the property to be shown or hidden.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}How long (in seconds) to wait for late datapoints.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Precision</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Maximum number of digits to display when rounding values up or down.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the chart.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Refresh<wbr>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}How often (in seconds) to refresh the values of the list.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secondary<wbr>Visualization</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of secondary visualization. Can be `None`, `Radial`, `Linear`, or `Sparkline`. If unset, the SignalFx default is used (`Sparkline`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sort<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The property to use when sorting the elements. Use `value` if you want to sort by value. Must be prepended with `+` for ascending or `-` for descending (e.g. `-foo`). Note there are some special values for some of the options provided in the UX: `"value"` for Value, `"sf_originatingMetric"` for Metric, and `"sf_metric"` for plot.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}How many seconds ago from which to display data. For example, the last hour would be `3600`, etc. Conflicts with `start_time` and `end_time`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Unit<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Must be `"Metric"` or `"Binary`". `"Metric"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Viz<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listchartvizoption">List&lt;Pulumi.<wbr>Signal<wbr>Fx.<wbr>Inputs.<wbr>List<wbr>Chart<wbr>Viz<wbr>Option<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}Plot-level customization options, associated with a publish statement.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Program<wbr>Text</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Signalflow program text for the chart. More info[in the SignalFx docs](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Color<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Must be one of `"Scale"`, `"Dimension"` or `"Metric"`. `"Dimension"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Color<wbr>Scales</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listchartcolorscale">[]List<wbr>Chart<wbr>Color<wbr>Scale</a></span>
    </dt>
    <dd>{{% md %}}Single color range including both the color to display for that range and the borders of the range. Example: `[{ gt = 60, color = "blue" }, { lte = 60, color = "yellow" }]`. Look at this [link](https://docs.signalfx.com/en/latest/charts/chart-options-tab.html).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Description of the chart.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disable<wbr>Sampling</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `false`, samples a subset of the output MTS, which improves UI performance. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>End<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
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
        <span class="property-type"><a href="#listchartlegendoptionsfield">[]List<wbr>Chart<wbr>Legend<wbr>Options<wbr>Field</a></span>
    </dt>
    <dd>{{% md %}}List of property names and enabled flags that should be displayed in the data table for the chart, in the order provided. This option cannot be used with `legend_fields_to_hide`.
* `property` The name of the property to display. Note the special values of `plot_label` (corresponding with the API's `sf_metric`) which shows the label of the time series `publish()` and `metric` (corresponding with the API's `sf_originatingMetric`) that shows the name of the metric for the time series being displayed.
* `enabled` True or False depending on if you want the property to be shown or hidden.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}How long (in seconds) to wait for late datapoints.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Precision</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Maximum number of digits to display when rounding values up or down.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the chart.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Refresh<wbr>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}How often (in seconds) to refresh the values of the list.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secondary<wbr>Visualization</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of secondary visualization. Can be `None`, `Radial`, `Linear`, or `Sparkline`. If unset, the SignalFx default is used (`Sparkline`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sort<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The property to use when sorting the elements. Use `value` if you want to sort by value. Must be prepended with `+` for ascending or `-` for descending (e.g. `-foo`). Note there are some special values for some of the options provided in the UX: `"value"` for Value, `"sf_originatingMetric"` for Metric, and `"sf_metric"` for plot.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}How many seconds ago from which to display data. For example, the last hour would be `3600`, etc. Conflicts with `start_time` and `end_time`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Unit<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Must be `"Metric"` or `"Binary`". `"Metric"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Viz<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listchartvizoption">[]List<wbr>Chart<wbr>Viz<wbr>Option</a></span>
    </dt>
    <dd>{{% md %}}Plot-level customization options, associated with a publish statement.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>program<wbr>Text</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Signalflow program text for the chart. More info[in the SignalFx docs](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>color<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Must be one of `"Scale"`, `"Dimension"` or `"Metric"`. `"Dimension"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>color<wbr>Scales</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listchartcolorscale">List<wbr>Chart<wbr>Color<wbr>Scale[]</a></span>
    </dt>
    <dd>{{% md %}}Single color range including both the color to display for that range and the borders of the range. Example: `[{ gt = 60, color = "blue" }, { lte = 60, color = "yellow" }]`. Look at this [link](https://docs.signalfx.com/en/latest/charts/chart-options-tab.html).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Description of the chart.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disable<wbr>Sampling</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}If `false`, samples a subset of the output MTS, which improves UI performance. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>end<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>legend<wbr>Fields<wbr>To<wbr>Hides</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}List of properties that should not be displayed in the chart legend (i.e. dimension names). All the properties are visible by default. Deprecated, please use `legend_options_fields`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Please use legend_options_fields{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>legend<wbr>Options<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listchartlegendoptionsfield">List<wbr>Chart<wbr>Legend<wbr>Options<wbr>Field[]</a></span>
    </dt>
    <dd>{{% md %}}List of property names and enabled flags that should be displayed in the data table for the chart, in the order provided. This option cannot be used with `legend_fields_to_hide`.
* `property` The name of the property to display. Note the special values of `plot_label` (corresponding with the API's `sf_metric`) which shows the label of the time series `publish()` and `metric` (corresponding with the API's `sf_originatingMetric`) that shows the name of the metric for the time series being displayed.
* `enabled` True or False depending on if you want the property to be shown or hidden.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}How long (in seconds) to wait for late datapoints.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Precision</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Maximum number of digits to display when rounding values up or down.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the chart.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>refresh<wbr>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}How often (in seconds) to refresh the values of the list.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secondary<wbr>Visualization</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of secondary visualization. Can be `None`, `Radial`, `Linear`, or `Sparkline`. If unset, the SignalFx default is used (`Sparkline`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sort<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The property to use when sorting the elements. Use `value` if you want to sort by value. Must be prepended with `+` for ascending or `-` for descending (e.g. `-foo`). Note there are some special values for some of the options provided in the UX: `"value"` for Value, `"sf_originatingMetric"` for Metric, and `"sf_metric"` for plot.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>time<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}How many seconds ago from which to display data. For example, the last hour would be `3600`, etc. Conflicts with `start_time` and `end_time`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>unit<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Must be `"Metric"` or `"Binary`". `"Metric"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>viz<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listchartvizoption">List<wbr>Chart<wbr>Viz<wbr>Option[]</a></span>
    </dt>
    <dd>{{% md %}}Plot-level customization options, associated with a publish statement.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>program_<wbr>text</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Signalflow program text for the chart. More info[in the SignalFx docs](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>color_<wbr>by</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Must be one of `"Scale"`, `"Dimension"` or `"Metric"`. `"Dimension"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>color_<wbr>scales</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listchartcolorscale">List[List<wbr>Chart<wbr>Color<wbr>Scale]</a></span>
    </dt>
    <dd>{{% md %}}Single color range including both the color to display for that range and the borders of the range. Example: `[{ gt = 60, color = "blue" }, { lte = 60, color = "yellow" }]`. Look at this [link](https://docs.signalfx.com/en/latest/charts/chart-options-tab.html).
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
    <dd>{{% md %}}If `false`, samples a subset of the output MTS, which improves UI performance. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>end_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
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
        <span class="property-type"><a href="#listchartlegendoptionsfield">List[List<wbr>Chart<wbr>Legend<wbr>Options<wbr>Field]</a></span>
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
        <span>max_<wbr>precision</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Maximum number of digits to display when rounding values up or down.
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
        <span>refresh_<wbr>interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}How often (in seconds) to refresh the values of the list.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secondary_<wbr>visualization</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of secondary visualization. Can be `None`, `Radial`, `Linear`, or `Sparkline`. If unset, the SignalFx default is used (`Sparkline`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sort_<wbr>by</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The property to use when sorting the elements. Use `value` if you want to sort by value. Must be prepended with `+` for ascending or `-` for descending (e.g. `-foo`). Note there are some special values for some of the options provided in the UX: `"value"` for Value, `"sf_originatingMetric"` for Metric, and `"sf_metric"` for plot.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>start_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

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
        <span class="property-type"><a href="#listchartvizoption">List[List<wbr>Chart<wbr>Viz<wbr>Option]</a></span>
    </dt>
    <dd>{{% md %}}Plot-level customization options, associated with a publish statement.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## ListChart Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URL of the chart
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URL of the chart
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URL of the chart
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}URL of the chart
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing ListChart Resource

Get an existing ListChart resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/signalfx/#ListChartState">ListChartState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/signalfx/#ListChart">ListChart</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>color_by=None<span class="p">, </span>color_scales=None<span class="p">, </span>description=None<span class="p">, </span>disable_sampling=None<span class="p">, </span>end_time=None<span class="p">, </span>legend_fields_to_hides=None<span class="p">, </span>legend_options_fields=None<span class="p">, </span>max_delay=None<span class="p">, </span>max_precision=None<span class="p">, </span>name=None<span class="p">, </span>program_text=None<span class="p">, </span>refresh_interval=None<span class="p">, </span>secondary_visualization=None<span class="p">, </span>sort_by=None<span class="p">, </span>start_time=None<span class="p">, </span>time_range=None<span class="p">, </span>unit_prefix=None<span class="p">, </span>url=None<span class="p">, </span>viz_options=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetListChart<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#ListChartState">ListChartState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#ListChart">ListChart</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Signalfx/Pulumi.Signalfx.ListChart.html">ListChart</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Signalfx/Pulumi.Signalfx..ListChartState.html">ListChartState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Color<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Must be one of `"Scale"`, `"Dimension"` or `"Metric"`. `"Dimension"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Color<wbr>Scales</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listchartcolorscale">List&lt;Pulumi.<wbr>Signal<wbr>Fx.<wbr>Inputs.<wbr>List<wbr>Chart<wbr>Color<wbr>Scale<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}Single color range including both the color to display for that range and the borders of the range. Example: `[{ gt = 60, color = "blue" }, { lte = 60, color = "yellow" }]`. Look at this [link](https://docs.signalfx.com/en/latest/charts/chart-options-tab.html).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Description of the chart.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disable<wbr>Sampling</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `false`, samples a subset of the output MTS, which improves UI performance. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>End<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>Legend<wbr>Fields<wbr>To<wbr>Hides</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;</span>
    </dt>
    <dd>{{% md %}}List of properties that should not be displayed in the chart legend (i.e. dimension names). All the properties are visible by default. Deprecated, please use `legend_options_fields`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Please use legend_options_fields{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>Legend<wbr>Options<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listchartlegendoptionsfield">List&lt;Pulumi.<wbr>Signal<wbr>Fx.<wbr>Inputs.<wbr>List<wbr>Chart<wbr>Legend<wbr>Options<wbr>Field<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}List of property names and enabled flags that should be displayed in the data table for the chart, in the order provided. This option cannot be used with `legend_fields_to_hide`.
* `property` The name of the property to display. Note the special values of `plot_label` (corresponding with the API's `sf_metric`) which shows the label of the time series `publish()` and `metric` (corresponding with the API's `sf_originatingMetric`) that shows the name of the metric for the time series being displayed.
* `enabled` True or False depending on if you want the property to be shown or hidden.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}How long (in seconds) to wait for late datapoints.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Precision</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Maximum number of digits to display when rounding values up or down.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the chart.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Program<wbr>Text</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Signalflow program text for the chart. More info[in the SignalFx docs](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Refresh<wbr>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}How often (in seconds) to refresh the values of the list.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secondary<wbr>Visualization</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of secondary visualization. Can be `None`, `Radial`, `Linear`, or `Sparkline`. If unset, the SignalFx default is used (`Sparkline`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sort<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The property to use when sorting the elements. Use `value` if you want to sort by value. Must be prepended with `+` for ascending or `-` for descending (e.g. `-foo`). Note there are some special values for some of the options provided in the UX: `"value"` for Value, `"sf_originatingMetric"` for Metric, and `"sf_metric"` for plot.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}How many seconds ago from which to display data. For example, the last hour would be `3600`, etc. Conflicts with `start_time` and `end_time`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Unit<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Must be `"Metric"` or `"Binary`". `"Metric"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URL of the chart
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Viz<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listchartvizoption">List&lt;Pulumi.<wbr>Signal<wbr>Fx.<wbr>Inputs.<wbr>List<wbr>Chart<wbr>Viz<wbr>Option<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}Plot-level customization options, associated with a publish statement.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Color<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Must be one of `"Scale"`, `"Dimension"` or `"Metric"`. `"Dimension"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Color<wbr>Scales</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listchartcolorscale">[]List<wbr>Chart<wbr>Color<wbr>Scale</a></span>
    </dt>
    <dd>{{% md %}}Single color range including both the color to display for that range and the borders of the range. Example: `[{ gt = 60, color = "blue" }, { lte = 60, color = "yellow" }]`. Look at this [link](https://docs.signalfx.com/en/latest/charts/chart-options-tab.html).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Description of the chart.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disable<wbr>Sampling</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}If `false`, samples a subset of the output MTS, which improves UI performance. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>End<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
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
        <span class="property-type"><a href="#listchartlegendoptionsfield">[]List<wbr>Chart<wbr>Legend<wbr>Options<wbr>Field</a></span>
    </dt>
    <dd>{{% md %}}List of property names and enabled flags that should be displayed in the data table for the chart, in the order provided. This option cannot be used with `legend_fields_to_hide`.
* `property` The name of the property to display. Note the special values of `plot_label` (corresponding with the API's `sf_metric`) which shows the label of the time series `publish()` and `metric` (corresponding with the API's `sf_originatingMetric`) that shows the name of the metric for the time series being displayed.
* `enabled` True or False depending on if you want the property to be shown or hidden.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}How long (in seconds) to wait for late datapoints.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Precision</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Maximum number of digits to display when rounding values up or down.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the chart.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Program<wbr>Text</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Signalflow program text for the chart. More info[in the SignalFx docs](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Refresh<wbr>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}How often (in seconds) to refresh the values of the list.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Secondary<wbr>Visualization</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of secondary visualization. Can be `None`, `Radial`, `Linear`, or `Sparkline`. If unset, the SignalFx default is used (`Sparkline`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sort<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The property to use when sorting the elements. Use `value` if you want to sort by value. Must be prepended with `+` for ascending or `-` for descending (e.g. `-foo`). Note there are some special values for some of the options provided in the UX: `"value"` for Value, `"sf_originatingMetric"` for Metric, and `"sf_metric"` for plot.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}How many seconds ago from which to display data. For example, the last hour would be `3600`, etc. Conflicts with `start_time` and `end_time`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Unit<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Must be `"Metric"` or `"Binary`". `"Metric"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URL of the chart
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Viz<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listchartvizoption">[]List<wbr>Chart<wbr>Viz<wbr>Option</a></span>
    </dt>
    <dd>{{% md %}}Plot-level customization options, associated with a publish statement.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>color<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Must be one of `"Scale"`, `"Dimension"` or `"Metric"`. `"Dimension"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>color<wbr>Scales</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listchartcolorscale">List<wbr>Chart<wbr>Color<wbr>Scale[]</a></span>
    </dt>
    <dd>{{% md %}}Single color range including both the color to display for that range and the borders of the range. Example: `[{ gt = 60, color = "blue" }, { lte = 60, color = "yellow" }]`. Look at this [link](https://docs.signalfx.com/en/latest/charts/chart-options-tab.html).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Description of the chart.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disable<wbr>Sampling</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}If `false`, samples a subset of the output MTS, which improves UI performance. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>end<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property-optional property-deprecated"
            title="Optional, Deprecated">
        <span>legend<wbr>Fields<wbr>To<wbr>Hides</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}List of properties that should not be displayed in the chart legend (i.e. dimension names). All the properties are visible by default. Deprecated, please use `legend_options_fields`.
{{% /md %}}<p class="property-message">Deprecated: {{% md %}}Please use legend_options_fields{{% /md %}}</p></dd>

    <dt class="property-optional"
            title="Optional">
        <span>legend<wbr>Options<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listchartlegendoptionsfield">List<wbr>Chart<wbr>Legend<wbr>Options<wbr>Field[]</a></span>
    </dt>
    <dd>{{% md %}}List of property names and enabled flags that should be displayed in the data table for the chart, in the order provided. This option cannot be used with `legend_fields_to_hide`.
* `property` The name of the property to display. Note the special values of `plot_label` (corresponding with the API's `sf_metric`) which shows the label of the time series `publish()` and `metric` (corresponding with the API's `sf_originatingMetric`) that shows the name of the metric for the time series being displayed.
* `enabled` True or False depending on if you want the property to be shown or hidden.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}How long (in seconds) to wait for late datapoints.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Precision</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Maximum number of digits to display when rounding values up or down.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the chart.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>program<wbr>Text</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Signalflow program text for the chart. More info[in the SignalFx docs](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>refresh<wbr>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}How often (in seconds) to refresh the values of the list.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secondary<wbr>Visualization</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of secondary visualization. Can be `None`, `Radial`, `Linear`, or `Sparkline`. If unset, the SignalFx default is used (`Sparkline`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sort<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The property to use when sorting the elements. Use `value` if you want to sort by value. Must be prepended with `+` for ascending or `-` for descending (e.g. `-foo`). Note there are some special values for some of the options provided in the UX: `"value"` for Value, `"sf_originatingMetric"` for Metric, and `"sf_metric"` for plot.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>time<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}How many seconds ago from which to display data. For example, the last hour would be `3600`, etc. Conflicts with `start_time` and `end_time`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>unit<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Must be `"Metric"` or `"Binary`". `"Metric"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URL of the chart
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>viz<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listchartvizoption">List<wbr>Chart<wbr>Viz<wbr>Option[]</a></span>
    </dt>
    <dd>{{% md %}}Plot-level customization options, associated with a publish statement.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>color_<wbr>by</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Must be one of `"Scale"`, `"Dimension"` or `"Metric"`. `"Dimension"` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>color_<wbr>scales</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#listchartcolorscale">List[List<wbr>Chart<wbr>Color<wbr>Scale]</a></span>
    </dt>
    <dd>{{% md %}}Single color range including both the color to display for that range and the borders of the range. Example: `[{ gt = 60, color = "blue" }, { lte = 60, color = "yellow" }]`. Look at this [link](https://docs.signalfx.com/en/latest/charts/chart-options-tab.html).
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
    <dd>{{% md %}}If `false`, samples a subset of the output MTS, which improves UI performance. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>end_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
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
        <span class="property-type"><a href="#listchartlegendoptionsfield">List[List<wbr>Chart<wbr>Legend<wbr>Options<wbr>Field]</a></span>
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
        <span>max_<wbr>precision</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Maximum number of digits to display when rounding values up or down.
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
        <span>program_<wbr>text</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Signalflow program text for the chart. More info[in the SignalFx docs](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>refresh_<wbr>interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}How often (in seconds) to refresh the values of the list.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>secondary_<wbr>visualization</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of secondary visualization. Can be `None`, `Radial`, `Linear`, or `Sparkline`. If unset, the SignalFx default is used (`Sparkline`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sort_<wbr>by</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The property to use when sorting the elements. Use `value` if you want to sort by value. Must be prepended with `+` for ascending or `-` for descending (e.g. `-foo`). Note there are some special values for some of the options provided in the UX: `"value"` for Value, `"sf_originatingMetric"` for Metric, and `"sf_metric"` for plot.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>start_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

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
        <span class="property-type"><a href="#listchartvizoption">List[List<wbr>Chart<wbr>Viz<wbr>Option]</a></span>
    </dt>
    <dd>{{% md %}}Plot-level customization options, associated with a publish statement.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>List<wbr>Chart<wbr>Color<wbr>Scale</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/input/#ListChartColorScale">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/output/#ListChartColorScale">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#ListChartColorScaleArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#ListChartColorScaleOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Color</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The color range to use. Must be either gray, blue, navy, orange, yellow, magenta, purple, violet, lilac, green, aquamarine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Gt</span>
        <span class="property-indicator"></span>
        <span class="property-type">double</span>
    </dt>
    <dd>{{% md %}}Indicates the lower threshold non-inclusive value for this range.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Gte</span>
        <span class="property-indicator"></span>
        <span class="property-type">double</span>
    </dt>
    <dd>{{% md %}}Indicates the lower threshold inclusive value for this range.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lt</span>
        <span class="property-indicator"></span>
        <span class="property-type">double</span>
    </dt>
    <dd>{{% md %}}Indicates the upper threshold non-inculsive value for this range.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lte</span>
        <span class="property-indicator"></span>
        <span class="property-type">double</span>
    </dt>
    <dd>{{% md %}}Indicates the upper threshold inclusive value for this range.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Color</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The color range to use. Must be either gray, blue, navy, orange, yellow, magenta, purple, violet, lilac, green, aquamarine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Gt</span>
        <span class="property-indicator"></span>
        <span class="property-type">float64</span>
    </dt>
    <dd>{{% md %}}Indicates the lower threshold non-inclusive value for this range.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Gte</span>
        <span class="property-indicator"></span>
        <span class="property-type">float64</span>
    </dt>
    <dd>{{% md %}}Indicates the lower threshold inclusive value for this range.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lt</span>
        <span class="property-indicator"></span>
        <span class="property-type">float64</span>
    </dt>
    <dd>{{% md %}}Indicates the upper threshold non-inculsive value for this range.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lte</span>
        <span class="property-indicator"></span>
        <span class="property-type">float64</span>
    </dt>
    <dd>{{% md %}}Indicates the upper threshold inclusive value for this range.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>color</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The color range to use. Must be either gray, blue, navy, orange, yellow, magenta, purple, violet, lilac, green, aquamarine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>gt</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Indicates the lower threshold non-inclusive value for this range.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>gte</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Indicates the lower threshold inclusive value for this range.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lt</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Indicates the upper threshold non-inculsive value for this range.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lte</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Indicates the upper threshold inclusive value for this range.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>color</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The color range to use. Must be either gray, blue, navy, orange, yellow, magenta, purple, violet, lilac, green, aquamarine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>gt</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Indicates the lower threshold non-inclusive value for this range.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>gte</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Indicates the lower threshold inclusive value for this range.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lt</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Indicates the upper threshold non-inculsive value for this range.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lte</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Indicates the upper threshold inclusive value for this range.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>List<wbr>Chart<wbr>Legend<wbr>Options<wbr>Field</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/input/#ListChartLegendOptionsField">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/output/#ListChartLegendOptionsField">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#ListChartLegendOptionsFieldArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#ListChartLegendOptionsFieldOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Property</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Property</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>property</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>property</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>List<wbr>Chart<wbr>Viz<wbr>Option</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/input/#ListChartVizOption">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/output/#ListChartVizOption">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#ListChartVizOptionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#ListChartVizOptionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Label used in the publish statement that displays the plot (metric time series data) you want to customize.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Color</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The color range to use. Must be either gray, blue, navy, orange, yellow, magenta, purple, violet, lilac, green, aquamarine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies an alternate value for the Plot Name column of the Data Table associated with the chart.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value<wbr>Suffix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unit to attach to this plot. Units support automatic scaling (eg thousands of bytes will be displayed as kilobytes). Values values are `Bit, Kilobit, Megabit, Gigabit, Terabit, Petabit, Exabit, Zettabit, Yottabit, Byte, Kibibyte, Mebibyte, Gigibyte, Tebibyte, Pebibyte, Exbibyte, Zebibyte, Yobibyte, Nanosecond, Microsecond, Millisecond, Second, Minute, Hour, Day, Week`.
* `value_prefix`, `value_suffix` - (Optional) Arbitrary prefix/suffix to display with the value of this plot.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Label used in the publish statement that displays the plot (metric time series data) you want to customize.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Color</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The color range to use. Must be either gray, blue, navy, orange, yellow, magenta, purple, violet, lilac, green, aquamarine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies an alternate value for the Plot Name column of the Data Table associated with the chart.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value<wbr>Suffix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Value<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unit to attach to this plot. Units support automatic scaling (eg thousands of bytes will be displayed as kilobytes). Values values are `Bit, Kilobit, Megabit, Gigabit, Terabit, Petabit, Exabit, Zettabit, Yottabit, Byte, Kibibyte, Mebibyte, Gigibyte, Tebibyte, Pebibyte, Exbibyte, Zebibyte, Yobibyte, Nanosecond, Microsecond, Millisecond, Second, Minute, Hour, Day, Week`.
* `value_prefix`, `value_suffix` - (Optional) Arbitrary prefix/suffix to display with the value of this plot.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Label used in the publish statement that displays the plot (metric time series data) you want to customize.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>color</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The color range to use. Must be either gray, blue, navy, orange, yellow, magenta, purple, violet, lilac, green, aquamarine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies an alternate value for the Plot Name column of the Data Table associated with the chart.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value<wbr>Suffix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>value<wbr>Unit</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A unit to attach to this plot. Units support automatic scaling (eg thousands of bytes will be displayed as kilobytes). Values values are `Bit, Kilobit, Megabit, Gigabit, Terabit, Petabit, Exabit, Zettabit, Yottabit, Byte, Kibibyte, Mebibyte, Gigibyte, Tebibyte, Pebibyte, Exbibyte, Zebibyte, Yobibyte, Nanosecond, Microsecond, Millisecond, Second, Minute, Hour, Day, Week`.
* `value_prefix`, `value_suffix` - (Optional) Arbitrary prefix/suffix to display with the value of this plot.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>label</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Label used in the publish statement that displays the plot (metric time series data) you want to customize.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>color</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The color range to use. Must be either gray, blue, navy, orange, yellow, magenta, purple, violet, lilac, green, aquamarine.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies an alternate value for the Plot Name column of the Data Table associated with the chart.
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

