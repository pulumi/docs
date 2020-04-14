
---
title: "HeatmapChart"
block_external_search_index: true
---



This chart type displays the specified plot in a heatmap fashion. This format is similar to the [Infrastructure Navigator](https://signalfx-product-docs.readthedocs-hosted.com/en/latest/built-in-content/infra-nav.html#infra), with squares representing each source for the selected metric, and the color of each square representing the value range of the metric.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as signalfx from "@pulumi/signalfx";

const myheatmapchart0 = new signalfx.HeatmapChart("myheatmapchart0", {
    // You must specify one of `color_range` or `color_scale`
    colorRange: {
        color: "#ff0000",
        maxValue: 100,
        minValue: 0,
    },
    description: "Very cool Heatmap",
    disableSampling: true,
    groupBies: [
        "hostname",
        "host",
    ],
    hideTimestamp: true,
    programText: `myfilters = filter("cluster_name", "prod") and filter("role", "search")
data("cpu.total.idle", filter=myfilters).publish()
`,
    sortBy: "+host",
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-signalfx/blob/master/website/docs/r/heatmap_chart.html.markdown.



## Create a HeatmapChart Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/signalfx/#HeatmapChart">HeatmapChart</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/signalfx/#HeatmapChartArgs">HeatmapChartArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">HeatmapChart</span><span class="p">(resource_name, opts=None, </span>color_range=None<span class="p">, </span>color_scales=None<span class="p">, </span>description=None<span class="p">, </span>disable_sampling=None<span class="p">, </span>group_bies=None<span class="p">, </span>hide_timestamp=None<span class="p">, </span>max_delay=None<span class="p">, </span>minimum_resolution=None<span class="p">, </span>name=None<span class="p">, </span>program_text=None<span class="p">, </span>refresh_interval=None<span class="p">, </span>sort_by=None<span class="p">, </span>unit_prefix=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewHeatmapChart<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#HeatmapChartArgs">HeatmapChartArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#HeatmapChart">HeatmapChart</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Signalfx/Pulumi.Signalfx.HeatmapChart.html">HeatmapChart</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Signalfx/Pulumi.SignalFx.HeatmapChartArgs.html">HeatmapChartArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
    <dd>{{% md %}}Signalflow program text for the chart. More info at <https://developers.signalfx.com/docs/signalflow-overview>.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Color<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#heatmapchartcolorrange">Pulumi.<wbr>Signal<wbr>Fx.<wbr>Inputs.<wbr>Heatmap<wbr>Chart<wbr>Color<wbr>Range<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Values and color for the color range. Example: `color_range : { min : 0, max : 100, color : "#0000ff" }`. Look at this [link](https://docs.signalfx.com/en/latest/charts/chart-options-tab.html).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Color<wbr>Scales</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#heatmapchartcolorscale">List&lt;Pulumi.<wbr>Signal<wbr>Fx.<wbr>Inputs.<wbr>Heatmap<wbr>Chart<wbr>Color<wbr>Scale<wbr>Args&gt;</a></span>
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
        <span>Group<wbr>Bies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;</span>
    </dt>
    <dd>{{% md %}}Properties to group by in the heatmap (in nesting order).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hide<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to show the timestamp in the chart. `false` by default.
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
        <span>Minimum<wbr>Resolution</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The minimum resolution (in seconds) to use for computing the underlying program.
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
    <dd>{{% md %}}How often (in seconds) to refresh the values of the heatmap.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sort<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The property to use when sorting the elements. Must be prepended with `+` for ascending or `-` for descending (e.g. `-foo`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Unit<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Must be `"Metric"` or `"Binary`". `"Metric"` by default.
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
    <dd>{{% md %}}Signalflow program text for the chart. More info at <https://developers.signalfx.com/docs/signalflow-overview>.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Color<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#heatmapchartcolorrange">Heatmap<wbr>Chart<wbr>Color<wbr>Range</a></span>
    </dt>
    <dd>{{% md %}}Values and color for the color range. Example: `color_range : { min : 0, max : 100, color : "#0000ff" }`. Look at this [link](https://docs.signalfx.com/en/latest/charts/chart-options-tab.html).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Color<wbr>Scales</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#heatmapchartcolorscale">[]Heatmap<wbr>Chart<wbr>Color<wbr>Scale</a></span>
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
        <span>Group<wbr>Bies</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Properties to group by in the heatmap (in nesting order).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hide<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to show the timestamp in the chart. `false` by default.
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
        <span>Minimum<wbr>Resolution</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The minimum resolution (in seconds) to use for computing the underlying program.
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
    <dd>{{% md %}}How often (in seconds) to refresh the values of the heatmap.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sort<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The property to use when sorting the elements. Must be prepended with `+` for ascending or `-` for descending (e.g. `-foo`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Unit<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Must be `"Metric"` or `"Binary`". `"Metric"` by default.
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
    <dd>{{% md %}}Signalflow program text for the chart. More info at <https://developers.signalfx.com/docs/signalflow-overview>.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>color<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#heatmapchartcolorrange">Heatmap<wbr>Chart<wbr>Color<wbr>Range</a></span>
    </dt>
    <dd>{{% md %}}Values and color for the color range. Example: `color_range : { min : 0, max : 100, color : "#0000ff" }`. Look at this [link](https://docs.signalfx.com/en/latest/charts/chart-options-tab.html).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>color<wbr>Scales</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#heatmapchartcolorscale">Heatmap<wbr>Chart<wbr>Color<wbr>Scale[]</a></span>
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
        <span>group<wbr>Bies</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}Properties to group by in the heatmap (in nesting order).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hide<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Whether to show the timestamp in the chart. `false` by default.
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
        <span>minimum<wbr>Resolution</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The minimum resolution (in seconds) to use for computing the underlying program.
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
    <dd>{{% md %}}How often (in seconds) to refresh the values of the heatmap.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sort<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The property to use when sorting the elements. Must be prepended with `+` for ascending or `-` for descending (e.g. `-foo`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>unit<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Must be `"Metric"` or `"Binary`". `"Metric"` by default.
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
    <dd>{{% md %}}Signalflow program text for the chart. More info at <https://developers.signalfx.com/docs/signalflow-overview>.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>color_<wbr>range</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#heatmapchartcolorrange">Dict[Heatmap<wbr>Chart<wbr>Color<wbr>Range]</a></span>
    </dt>
    <dd>{{% md %}}Values and color for the color range. Example: `color_range : { min : 0, max : 100, color : "#0000ff" }`. Look at this [link](https://docs.signalfx.com/en/latest/charts/chart-options-tab.html).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>color_<wbr>scales</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#heatmapchartcolorscale">List[Heatmap<wbr>Chart<wbr>Color<wbr>Scale]</a></span>
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
        <span>group_<wbr>bies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Properties to group by in the heatmap (in nesting order).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hide_<wbr>timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to show the timestamp in the chart. `false` by default.
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
        <span>refresh_<wbr>interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}How often (in seconds) to refresh the values of the heatmap.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sort_<wbr>by</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The property to use when sorting the elements. Must be prepended with `+` for ascending or `-` for descending (e.g. `-foo`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>unit_<wbr>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Must be `"Metric"` or `"Binary`". `"Metric"` by default.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## HeatmapChart Output Properties

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








## Look up an Existing HeatmapChart Resource

Get an existing HeatmapChart resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/signalfx/#HeatmapChartState">HeatmapChartState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/signalfx/#HeatmapChart">HeatmapChart</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>color_range=None<span class="p">, </span>color_scales=None<span class="p">, </span>description=None<span class="p">, </span>disable_sampling=None<span class="p">, </span>group_bies=None<span class="p">, </span>hide_timestamp=None<span class="p">, </span>max_delay=None<span class="p">, </span>minimum_resolution=None<span class="p">, </span>name=None<span class="p">, </span>program_text=None<span class="p">, </span>refresh_interval=None<span class="p">, </span>sort_by=None<span class="p">, </span>unit_prefix=None<span class="p">, </span>url=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetHeatmapChart<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#HeatmapChartState">HeatmapChartState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#HeatmapChart">HeatmapChart</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Signalfx/Pulumi.Signalfx.HeatmapChart.html">HeatmapChart</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Signalfx/Pulumi.Signalfx..HeatmapChartState.html">HeatmapChartState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Color<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#heatmapchartcolorrange">Pulumi.<wbr>Signal<wbr>Fx.<wbr>Inputs.<wbr>Heatmap<wbr>Chart<wbr>Color<wbr>Range<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Values and color for the color range. Example: `color_range : { min : 0, max : 100, color : "#0000ff" }`. Look at this [link](https://docs.signalfx.com/en/latest/charts/chart-options-tab.html).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Color<wbr>Scales</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#heatmapchartcolorscale">List&lt;Pulumi.<wbr>Signal<wbr>Fx.<wbr>Inputs.<wbr>Heatmap<wbr>Chart<wbr>Color<wbr>Scale<wbr>Args&gt;</a></span>
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
        <span>Group<wbr>Bies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;</span>
    </dt>
    <dd>{{% md %}}Properties to group by in the heatmap (in nesting order).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hide<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to show the timestamp in the chart. `false` by default.
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
        <span>Minimum<wbr>Resolution</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The minimum resolution (in seconds) to use for computing the underlying program.
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
    <dd>{{% md %}}Signalflow program text for the chart. More info at <https://developers.signalfx.com/docs/signalflow-overview>.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Refresh<wbr>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}How often (in seconds) to refresh the values of the heatmap.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sort<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The property to use when sorting the elements. Must be prepended with `+` for ascending or `-` for descending (e.g. `-foo`).
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

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Color<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#heatmapchartcolorrange">Heatmap<wbr>Chart<wbr>Color<wbr>Range</a></span>
    </dt>
    <dd>{{% md %}}Values and color for the color range. Example: `color_range : { min : 0, max : 100, color : "#0000ff" }`. Look at this [link](https://docs.signalfx.com/en/latest/charts/chart-options-tab.html).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Color<wbr>Scales</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#heatmapchartcolorscale">[]Heatmap<wbr>Chart<wbr>Color<wbr>Scale</a></span>
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
        <span>Group<wbr>Bies</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Properties to group by in the heatmap (in nesting order).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hide<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to show the timestamp in the chart. `false` by default.
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
        <span>Minimum<wbr>Resolution</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The minimum resolution (in seconds) to use for computing the underlying program.
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
    <dd>{{% md %}}Signalflow program text for the chart. More info at <https://developers.signalfx.com/docs/signalflow-overview>.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Refresh<wbr>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}How often (in seconds) to refresh the values of the heatmap.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sort<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The property to use when sorting the elements. Must be prepended with `+` for ascending or `-` for descending (e.g. `-foo`).
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

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>color<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#heatmapchartcolorrange">Heatmap<wbr>Chart<wbr>Color<wbr>Range</a></span>
    </dt>
    <dd>{{% md %}}Values and color for the color range. Example: `color_range : { min : 0, max : 100, color : "#0000ff" }`. Look at this [link](https://docs.signalfx.com/en/latest/charts/chart-options-tab.html).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>color<wbr>Scales</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#heatmapchartcolorscale">Heatmap<wbr>Chart<wbr>Color<wbr>Scale[]</a></span>
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
        <span>group<wbr>Bies</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}Properties to group by in the heatmap (in nesting order).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hide<wbr>Timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Whether to show the timestamp in the chart. `false` by default.
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
        <span>minimum<wbr>Resolution</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The minimum resolution (in seconds) to use for computing the underlying program.
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
    <dd>{{% md %}}Signalflow program text for the chart. More info at <https://developers.signalfx.com/docs/signalflow-overview>.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>refresh<wbr>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}How often (in seconds) to refresh the values of the heatmap.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sort<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The property to use when sorting the elements. Must be prepended with `+` for ascending or `-` for descending (e.g. `-foo`).
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

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>color_<wbr>range</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#heatmapchartcolorrange">Dict[Heatmap<wbr>Chart<wbr>Color<wbr>Range]</a></span>
    </dt>
    <dd>{{% md %}}Values and color for the color range. Example: `color_range : { min : 0, max : 100, color : "#0000ff" }`. Look at this [link](https://docs.signalfx.com/en/latest/charts/chart-options-tab.html).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>color_<wbr>scales</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#heatmapchartcolorscale">List[Heatmap<wbr>Chart<wbr>Color<wbr>Scale]</a></span>
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
        <span>group_<wbr>bies</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Properties to group by in the heatmap (in nesting order).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hide_<wbr>timestamp</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to show the timestamp in the chart. `false` by default.
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
        <span>program_<wbr>text</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Signalflow program text for the chart. More info at <https://developers.signalfx.com/docs/signalflow-overview>.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>refresh_<wbr>interval</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}How often (in seconds) to refresh the values of the heatmap.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sort_<wbr>by</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The property to use when sorting the elements. Must be prepended with `+` for ascending or `-` for descending (e.g. `-foo`).
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

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Heatmap<wbr>Chart<wbr>Color<wbr>Range</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/input/#HeatmapChartColorRange">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/output/#HeatmapChartColorRange">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#HeatmapChartColorRangeArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#HeatmapChartColorRangeOutput">output</a> API doc for this type.
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
        <span>Max<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">double</span>
    </dt>
    <dd>{{% md %}}The maximum value within the coloring range.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">double</span>
    </dt>
    <dd>{{% md %}}The minimum value within the coloring range.
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
        <span>Max<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">float64</span>
    </dt>
    <dd>{{% md %}}The maximum value within the coloring range.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">float64</span>
    </dt>
    <dd>{{% md %}}The minimum value within the coloring range.
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
        <span>max<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The maximum value within the coloring range.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The minimum value within the coloring range.
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
        <span>max<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The maximum value within the coloring range.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The minimum value within the coloring range.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Heatmap<wbr>Chart<wbr>Color<wbr>Scale</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/input/#HeatmapChartColorScale">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/output/#HeatmapChartColorScale">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#HeatmapChartColorScaleArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#HeatmapChartColorScaleOutput">output</a> API doc for this type.
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
    <dd>{{% md %}}Indicates the upper threshold non-inclusive value for this range.
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
    <dd>{{% md %}}Indicates the upper threshold non-inclusive value for this range.
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
    <dd>{{% md %}}Indicates the upper threshold non-inclusive value for this range.
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
    <dd>{{% md %}}Indicates the upper threshold non-inclusive value for this range.
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









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-signalfx">https://github.com/pulumi/pulumi-signalfx</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

