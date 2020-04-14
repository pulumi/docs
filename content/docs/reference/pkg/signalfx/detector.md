
---
title: "Detector"
block_external_search_index: true
---



Provides a SignalFx detector resource. This can be used to create and manage detectors.

> **NOTE** If you're interested in using SignalFx detector features such as Historical Anomaly, Resource Running Out, or others then consider building them in the UI first then using the "Show SignalFlow" feature to extract the value for `program_text`. You may also consult the [documentation for detector functions in signalflow-library](https://github.com/signalfx/signalflow-library/tree/master/library/signalfx/detectors).

## Notification Format

As SignalFx supports different notification mechanisms a comma-delimited string is used to provide inputs. If you'd like to specify multiple notifications, then each should be a member in the list, like so:

```typescript
import * as pulumi from "@pulumi/pulumi";
```

This will likely be changed in a future iteration of the provider. See [SignalFx Docs](https://developers.signalfx.com/detectors_reference.html#operation/Create%20Single%20Detector) for more information. For now, here are some example of how to configure each notification type:

### Email

```typescript
import * as pulumi from "@pulumi/pulumi";
```

### Jira

Note that the `credentialId` is the SignalFx-provided ID shown after setting up your Jira integration. (See also `signalfx.jira.Integration`.)

```typescript
import * as pulumi from "@pulumi/pulumi";
```

### Opsgenie

Note that the `credentialId` is the SignalFx-provided ID shown after setting up your Opsgenie integration. `Team` here is hardcoded as the `responderType` as that is the only acceptable type as per the API docs.

```typescript
import * as pulumi from "@pulumi/pulumi";
```

### PagerDuty

```typescript
import * as pulumi from "@pulumi/pulumi";
```

### Slack

Exclude the `#` on the channel name!

```typescript
import * as pulumi from "@pulumi/pulumi";
```

### Team

Sends [notifications to a team](https://docs.signalfx.com/en/latest/managing/teams/team-notifications.html).

```typescript
import * as pulumi from "@pulumi/pulumi";
```

### Team

Sends an email to every member of a team.

```typescript
import * as pulumi from "@pulumi/pulumi";
```

### VictorOps

```typescript
import * as pulumi from "@pulumi/pulumi";
```

### Webhook

> **NOTE** You need to include all the commas even if you only use a credential id below.

You can either configure a Webhook to use an existing integration's credential id:
```typescript
import * as pulumi from "@pulumi/pulumi";
```

or configure one inline:
```typescript
import * as pulumi from "@pulumi/pulumi";
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-signalfx/blob/master/website/docs/r/detector.html.markdown.



## Create a Detector Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/signalfx/#Detector">Detector</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/signalfx/#DetectorArgs">DetectorArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Detector</span><span class="p">(resource_name, opts=None, </span>authorized_writer_teams=None<span class="p">, </span>authorized_writer_users=None<span class="p">, </span>description=None<span class="p">, </span>disable_sampling=None<span class="p">, </span>end_time=None<span class="p">, </span>max_delay=None<span class="p">, </span>name=None<span class="p">, </span>program_text=None<span class="p">, </span>rules=None<span class="p">, </span>show_data_markers=None<span class="p">, </span>show_event_lines=None<span class="p">, </span>start_time=None<span class="p">, </span>teams=None<span class="p">, </span>time_range=None<span class="p">, </span>viz_options=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewDetector<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#DetectorArgs">DetectorArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#Detector">Detector</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Signalfx/Pulumi.Signalfx.Detector.html">Detector</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Signalfx/Pulumi.SignalFx.DetectorArgs.html">DetectorArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
    <dd>{{% md %}}Signalflow program text for the detector. More info [in the SignalFx docs](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#detectorrule">List&lt;Pulumi.<wbr>Signal<wbr>Fx.<wbr>Inputs.<wbr>Detector<wbr>Rule<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}Set of rules used for alerting.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Authorized<wbr>Writer<wbr>Teams</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;</span>
    </dt>
    <dd>{{% md %}}Team IDs that have write access to this detector. Remember to use an admin's token if using this feature and to include that admin's team id (or user id in `authorized_writer_users`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Authorized<wbr>Writer<wbr>Users</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;</span>
    </dt>
    <dd>{{% md %}}User IDs that have write access to this detector. Remember to use an admin's token if using this feature and to include that admin's user id (or team id in `authorized_writer_teams`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Description for the rule. Displays as the alert condition in the Alert Rules tab of the detector editor in the web UI.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disable<wbr>Sampling</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When `false`, the visualization may sample the output timeseries rather than displaying them all. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>End<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}How long (in seconds) to wait for late datapoints. See [Delayed Datapoints](https://signalfx-product-docs.readthedocs-hosted.com/en/latest/charts/chart-builder.html#delayed-datapoints) for more info. Max value is `900` seconds (15 minutes). `Auto` (as little as possible) by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the detector.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Show<wbr>Data<wbr>Markers</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When `true`, markers will be drawn for each datapoint within the visualization. `true` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Show<wbr>Event<wbr>Lines</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When `true`, the visualization will display a vertical line for each event trigger. `false` by default.
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
        <span>Teams</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;</span>
    </dt>
    <dd>{{% md %}}Team IDs to associate the detector to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Seconds to display in the visualization. This is a rolling range from the current time. Example: `3600` corresponds to `-1h` in web UI. `3600` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Viz<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#detectorvizoption">List&lt;Pulumi.<wbr>Signal<wbr>Fx.<wbr>Inputs.<wbr>Detector<wbr>Viz<wbr>Option<wbr>Args&gt;</a></span>
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
    <dd>{{% md %}}Signalflow program text for the detector. More info [in the SignalFx docs](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#detectorrule">[]Detector<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}Set of rules used for alerting.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Authorized<wbr>Writer<wbr>Teams</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Team IDs that have write access to this detector. Remember to use an admin's token if using this feature and to include that admin's team id (or user id in `authorized_writer_users`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Authorized<wbr>Writer<wbr>Users</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}User IDs that have write access to this detector. Remember to use an admin's token if using this feature and to include that admin's user id (or team id in `authorized_writer_teams`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Description for the rule. Displays as the alert condition in the Alert Rules tab of the detector editor in the web UI.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disable<wbr>Sampling</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When `false`, the visualization may sample the output timeseries rather than displaying them all. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>End<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}How long (in seconds) to wait for late datapoints. See [Delayed Datapoints](https://signalfx-product-docs.readthedocs-hosted.com/en/latest/charts/chart-builder.html#delayed-datapoints) for more info. Max value is `900` seconds (15 minutes). `Auto` (as little as possible) by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the detector.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Show<wbr>Data<wbr>Markers</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When `true`, markers will be drawn for each datapoint within the visualization. `true` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Show<wbr>Event<wbr>Lines</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When `true`, the visualization will display a vertical line for each event trigger. `false` by default.
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
        <span>Teams</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Team IDs to associate the detector to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Seconds to display in the visualization. This is a rolling range from the current time. Example: `3600` corresponds to `-1h` in web UI. `3600` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Viz<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#detectorvizoption">[]Detector<wbr>Viz<wbr>Option</a></span>
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
    <dd>{{% md %}}Signalflow program text for the detector. More info [in the SignalFx docs](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#detectorrule">Detector<wbr>Rule[]</a></span>
    </dt>
    <dd>{{% md %}}Set of rules used for alerting.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>authorized<wbr>Writer<wbr>Teams</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}Team IDs that have write access to this detector. Remember to use an admin's token if using this feature and to include that admin's team id (or user id in `authorized_writer_users`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>authorized<wbr>Writer<wbr>Users</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}User IDs that have write access to this detector. Remember to use an admin's token if using this feature and to include that admin's user id (or team id in `authorized_writer_teams`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Description for the rule. Displays as the alert condition in the Alert Rules tab of the detector editor in the web UI.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disable<wbr>Sampling</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}When `false`, the visualization may sample the output timeseries rather than displaying them all. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>end<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}How long (in seconds) to wait for late datapoints. See [Delayed Datapoints](https://signalfx-product-docs.readthedocs-hosted.com/en/latest/charts/chart-builder.html#delayed-datapoints) for more info. Max value is `900` seconds (15 minutes). `Auto` (as little as possible) by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the detector.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>show<wbr>Data<wbr>Markers</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}When `true`, markers will be drawn for each datapoint within the visualization. `true` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>show<wbr>Event<wbr>Lines</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}When `true`, the visualization will display a vertical line for each event trigger. `false` by default.
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
        <span>teams</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}Team IDs to associate the detector to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>time<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Seconds to display in the visualization. This is a rolling range from the current time. Example: `3600` corresponds to `-1h` in web UI. `3600` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>viz<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#detectorvizoption">Detector<wbr>Viz<wbr>Option[]</a></span>
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
    <dd>{{% md %}}Signalflow program text for the detector. More info [in the SignalFx docs](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#detectorrule">List[Detector<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}Set of rules used for alerting.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>authorized_<wbr>writer_<wbr>teams</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Team IDs that have write access to this detector. Remember to use an admin's token if using this feature and to include that admin's team id (or user id in `authorized_writer_users`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>authorized_<wbr>writer_<wbr>users</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}User IDs that have write access to this detector. Remember to use an admin's token if using this feature and to include that admin's user id (or team id in `authorized_writer_teams`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Description for the rule. Displays as the alert condition in the Alert Rules tab of the detector editor in the web UI.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disable_<wbr>sampling</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When `false`, the visualization may sample the output timeseries rather than displaying them all. `false` by default.
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
        <span>max_<wbr>delay</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}How long (in seconds) to wait for late datapoints. See [Delayed Datapoints](https://signalfx-product-docs.readthedocs-hosted.com/en/latest/charts/chart-builder.html#delayed-datapoints) for more info. Max value is `900` seconds (15 minutes). `Auto` (as little as possible) by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the detector.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>show_<wbr>data_<wbr>markers</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When `true`, markers will be drawn for each datapoint within the visualization. `true` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>show_<wbr>event_<wbr>lines</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When `true`, the visualization will display a vertical line for each event trigger. `false` by default.
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
        <span>teams</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Team IDs to associate the detector to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>time_<wbr>range</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Seconds to display in the visualization. This is a rolling range from the current time. Example: `3600` corresponds to `-1h` in web UI. `3600` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>viz_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#detectorvizoption">List[Detector<wbr>Viz<wbr>Option]</a></span>
    </dt>
    <dd>{{% md %}}Plot-level customization options, associated with a publish statement.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Detector Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URL of the detector
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
    <dd>{{% md %}}URL of the detector
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
    <dd>{{% md %}}URL of the detector
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
    <dd>{{% md %}}URL of the detector
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Detector Resource

Get an existing Detector resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/signalfx/#DetectorState">DetectorState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/signalfx/#Detector">Detector</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>authorized_writer_teams=None<span class="p">, </span>authorized_writer_users=None<span class="p">, </span>description=None<span class="p">, </span>disable_sampling=None<span class="p">, </span>end_time=None<span class="p">, </span>max_delay=None<span class="p">, </span>name=None<span class="p">, </span>program_text=None<span class="p">, </span>rules=None<span class="p">, </span>show_data_markers=None<span class="p">, </span>show_event_lines=None<span class="p">, </span>start_time=None<span class="p">, </span>teams=None<span class="p">, </span>time_range=None<span class="p">, </span>url=None<span class="p">, </span>viz_options=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetDetector<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#DetectorState">DetectorState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#Detector">Detector</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Signalfx/Pulumi.Signalfx.Detector.html">Detector</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Signalfx/Pulumi.Signalfx..DetectorState.html">DetectorState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Authorized<wbr>Writer<wbr>Teams</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;</span>
    </dt>
    <dd>{{% md %}}Team IDs that have write access to this detector. Remember to use an admin's token if using this feature and to include that admin's team id (or user id in `authorized_writer_users`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Authorized<wbr>Writer<wbr>Users</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;</span>
    </dt>
    <dd>{{% md %}}User IDs that have write access to this detector. Remember to use an admin's token if using this feature and to include that admin's user id (or team id in `authorized_writer_teams`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Description for the rule. Displays as the alert condition in the Alert Rules tab of the detector editor in the web UI.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disable<wbr>Sampling</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When `false`, the visualization may sample the output timeseries rather than displaying them all. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>End<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}How long (in seconds) to wait for late datapoints. See [Delayed Datapoints](https://signalfx-product-docs.readthedocs-hosted.com/en/latest/charts/chart-builder.html#delayed-datapoints) for more info. Max value is `900` seconds (15 minutes). `Auto` (as little as possible) by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the detector.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Program<wbr>Text</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Signalflow program text for the detector. More info [in the SignalFx docs](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#detectorrule">List&lt;Pulumi.<wbr>Signal<wbr>Fx.<wbr>Inputs.<wbr>Detector<wbr>Rule<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}Set of rules used for alerting.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Show<wbr>Data<wbr>Markers</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When `true`, markers will be drawn for each datapoint within the visualization. `true` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Show<wbr>Event<wbr>Lines</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When `true`, the visualization will display a vertical line for each event trigger. `false` by default.
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
        <span>Teams</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;</span>
    </dt>
    <dd>{{% md %}}Team IDs to associate the detector to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Seconds to display in the visualization. This is a rolling range from the current time. Example: `3600` corresponds to `-1h` in web UI. `3600` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URL of the detector
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Viz<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#detectorvizoption">List&lt;Pulumi.<wbr>Signal<wbr>Fx.<wbr>Inputs.<wbr>Detector<wbr>Viz<wbr>Option<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}Plot-level customization options, associated with a publish statement.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Authorized<wbr>Writer<wbr>Teams</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Team IDs that have write access to this detector. Remember to use an admin's token if using this feature and to include that admin's team id (or user id in `authorized_writer_users`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Authorized<wbr>Writer<wbr>Users</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}User IDs that have write access to this detector. Remember to use an admin's token if using this feature and to include that admin's user id (or team id in `authorized_writer_teams`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Description for the rule. Displays as the alert condition in the Alert Rules tab of the detector editor in the web UI.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disable<wbr>Sampling</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When `false`, the visualization may sample the output timeseries rather than displaying them all. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>End<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}How long (in seconds) to wait for late datapoints. See [Delayed Datapoints](https://signalfx-product-docs.readthedocs-hosted.com/en/latest/charts/chart-builder.html#delayed-datapoints) for more info. Max value is `900` seconds (15 minutes). `Auto` (as little as possible) by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the detector.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Program<wbr>Text</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Signalflow program text for the detector. More info [in the SignalFx docs](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#detectorrule">[]Detector<wbr>Rule</a></span>
    </dt>
    <dd>{{% md %}}Set of rules used for alerting.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Show<wbr>Data<wbr>Markers</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When `true`, markers will be drawn for each datapoint within the visualization. `true` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Show<wbr>Event<wbr>Lines</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When `true`, the visualization will display a vertical line for each event trigger. `false` by default.
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
        <span>Teams</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Team IDs to associate the detector to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Seconds to display in the visualization. This is a rolling range from the current time. Example: `3600` corresponds to `-1h` in web UI. `3600` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URL of the detector
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Viz<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#detectorvizoption">[]Detector<wbr>Viz<wbr>Option</a></span>
    </dt>
    <dd>{{% md %}}Plot-level customization options, associated with a publish statement.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>authorized<wbr>Writer<wbr>Teams</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}Team IDs that have write access to this detector. Remember to use an admin's token if using this feature and to include that admin's team id (or user id in `authorized_writer_users`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>authorized<wbr>Writer<wbr>Users</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}User IDs that have write access to this detector. Remember to use an admin's token if using this feature and to include that admin's user id (or team id in `authorized_writer_teams`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Description for the rule. Displays as the alert condition in the Alert Rules tab of the detector editor in the web UI.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disable<wbr>Sampling</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}When `false`, the visualization may sample the output timeseries rather than displaying them all. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>end<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Seconds since epoch. Used for visualization. Conflicts with `time_range`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Delay</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}How long (in seconds) to wait for late datapoints. See [Delayed Datapoints](https://signalfx-product-docs.readthedocs-hosted.com/en/latest/charts/chart-builder.html#delayed-datapoints) for more info. Max value is `900` seconds (15 minutes). `Auto` (as little as possible) by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the detector.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>program<wbr>Text</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Signalflow program text for the detector. More info [in the SignalFx docs](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#detectorrule">Detector<wbr>Rule[]</a></span>
    </dt>
    <dd>{{% md %}}Set of rules used for alerting.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>show<wbr>Data<wbr>Markers</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}When `true`, markers will be drawn for each datapoint within the visualization. `true` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>show<wbr>Event<wbr>Lines</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}When `true`, the visualization will display a vertical line for each event trigger. `false` by default.
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
        <span>teams</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}Team IDs to associate the detector to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>time<wbr>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Seconds to display in the visualization. This is a rolling range from the current time. Example: `3600` corresponds to `-1h` in web UI. `3600` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URL of the detector
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>viz<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#detectorvizoption">Detector<wbr>Viz<wbr>Option[]</a></span>
    </dt>
    <dd>{{% md %}}Plot-level customization options, associated with a publish statement.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>authorized_<wbr>writer_<wbr>teams</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Team IDs that have write access to this detector. Remember to use an admin's token if using this feature and to include that admin's team id (or user id in `authorized_writer_users`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>authorized_<wbr>writer_<wbr>users</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}User IDs that have write access to this detector. Remember to use an admin's token if using this feature and to include that admin's user id (or team id in `authorized_writer_teams`).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Description for the rule. Displays as the alert condition in the Alert Rules tab of the detector editor in the web UI.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disable_<wbr>sampling</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When `false`, the visualization may sample the output timeseries rather than displaying them all. `false` by default.
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
        <span>max_<wbr>delay</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}How long (in seconds) to wait for late datapoints. See [Delayed Datapoints](https://signalfx-product-docs.readthedocs-hosted.com/en/latest/charts/chart-builder.html#delayed-datapoints) for more info. Max value is `900` seconds (15 minutes). `Auto` (as little as possible) by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the detector.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>program_<wbr>text</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Signalflow program text for the detector. More info [in the SignalFx docs](https://developers.signalfx.com/signalflow_analytics/signalflow_overview.html#_signalflow_programming_language).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>rules</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#detectorrule">List[Detector<wbr>Rule]</a></span>
    </dt>
    <dd>{{% md %}}Set of rules used for alerting.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>show_<wbr>data_<wbr>markers</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When `true`, markers will be drawn for each datapoint within the visualization. `true` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>show_<wbr>event_<wbr>lines</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When `true`, the visualization will display a vertical line for each event trigger. `false` by default.
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
        <span>teams</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Team IDs to associate the detector to.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>time_<wbr>range</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Seconds to display in the visualization. This is a rolling range from the current time. Example: `3600` corresponds to `-1h` in web UI. `3600` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}URL of the detector
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>viz_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#detectorvizoption">List[Detector<wbr>Viz<wbr>Option]</a></span>
    </dt>
    <dd>{{% md %}}Plot-level customization options, associated with a publish statement.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Detector<wbr>Rule</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/input/#DetectorRule">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/output/#DetectorRule">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#DetectorRuleArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#DetectorRuleOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Detect<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A detect label which matches a detect label within `program_text`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Severity</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The severity of the rule, must be one of: `"Critical"`, `"Major"`, `"Minor"`, `"Warning"`, `"Info"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Description for the rule. Displays as the alert condition in the Alert Rules tab of the detector editor in the web UI.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When true, notifications and events will not be generated for the detect label. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Notifications</span>
        <span class="property-indicator"></span>
        <span class="property-type">List&lt;string&gt;</span>
    </dt>
    <dd>{{% md %}}List of strings specifying where notifications will be sent when an incident occurs. See [Create A Single Detector](https://developers.signalfx.com/detectors_reference.html#operation/Create%20Single%20Detector) for more info.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Parameterized<wbr>Body</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Custom notification message body when an alert is triggered. See [Set Up Detectors to Trigger Alerts](https://docs.signalfx.com/en/latest/detect-alert/set-up-detectors.html#about-detectors#alert-settings) for more info.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Parameterized<wbr>Subject</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Custom notification message subject when an alert is triggered. See [Set Up Detectors to Trigger Alerts](https://docs.signalfx.com/en/latest/detect-alert/set-up-detectors.html#about-detectors#alert-settings) for more info.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Runbook<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URL of page to consult when an alert is triggered. This can be used with custom notification messages.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Plain text suggested first course of action, such as a command line to execute. This can be used with custom notification messages.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Detect<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A detect label which matches a detect label within `program_text`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Severity</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The severity of the rule, must be one of: `"Critical"`, `"Major"`, `"Minor"`, `"Warning"`, `"Info"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Description for the rule. Displays as the alert condition in the Alert Rules tab of the detector editor in the web UI.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When true, notifications and events will not be generated for the detect label. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Notifications</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of strings specifying where notifications will be sent when an incident occurs. See [Create A Single Detector](https://developers.signalfx.com/detectors_reference.html#operation/Create%20Single%20Detector) for more info.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Parameterized<wbr>Body</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Custom notification message body when an alert is triggered. See [Set Up Detectors to Trigger Alerts](https://docs.signalfx.com/en/latest/detect-alert/set-up-detectors.html#about-detectors#alert-settings) for more info.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Parameterized<wbr>Subject</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Custom notification message subject when an alert is triggered. See [Set Up Detectors to Trigger Alerts](https://docs.signalfx.com/en/latest/detect-alert/set-up-detectors.html#about-detectors#alert-settings) for more info.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Runbook<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URL of page to consult when an alert is triggered. This can be used with custom notification messages.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Tip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Plain text suggested first course of action, such as a command line to execute. This can be used with custom notification messages.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>detect<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A detect label which matches a detect label within `program_text`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>severity</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The severity of the rule, must be one of: `"Critical"`, `"Major"`, `"Minor"`, `"Warning"`, `"Info"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Description for the rule. Displays as the alert condition in the Alert Rules tab of the detector editor in the web UI.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}When true, notifications and events will not be generated for the detect label. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>notifications</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}List of strings specifying where notifications will be sent when an incident occurs. See [Create A Single Detector](https://developers.signalfx.com/detectors_reference.html#operation/Create%20Single%20Detector) for more info.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>parameterized<wbr>Body</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Custom notification message body when an alert is triggered. See [Set Up Detectors to Trigger Alerts](https://docs.signalfx.com/en/latest/detect-alert/set-up-detectors.html#about-detectors#alert-settings) for more info.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>parameterized<wbr>Subject</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Custom notification message subject when an alert is triggered. See [Set Up Detectors to Trigger Alerts](https://docs.signalfx.com/en/latest/detect-alert/set-up-detectors.html#about-detectors#alert-settings) for more info.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>runbook<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URL of page to consult when an alert is triggered. This can be used with custom notification messages.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tip</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Plain text suggested first course of action, such as a command line to execute. This can be used with custom notification messages.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>detect<wbr>Label</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A detect label which matches a detect label within `program_text`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>severity</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The severity of the rule, must be one of: `"Critical"`, `"Major"`, `"Minor"`, `"Warning"`, `"Info"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Description for the rule. Displays as the alert condition in the Alert Rules tab of the detector editor in the web UI.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When true, notifications and events will not be generated for the detect label. `false` by default.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>notifications</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of strings specifying where notifications will be sent when an incident occurs. See [Create A Single Detector](https://developers.signalfx.com/detectors_reference.html#operation/Create%20Single%20Detector) for more info.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>parameterized<wbr>Body</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Custom notification message body when an alert is triggered. See [Set Up Detectors to Trigger Alerts](https://docs.signalfx.com/en/latest/detect-alert/set-up-detectors.html#about-detectors#alert-settings) for more info.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>parameterized<wbr>Subject</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Custom notification message subject when an alert is triggered. See [Set Up Detectors to Trigger Alerts](https://docs.signalfx.com/en/latest/detect-alert/set-up-detectors.html#about-detectors#alert-settings) for more info.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>runbook<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}URL of page to consult when an alert is triggered. This can be used with custom notification messages.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>tip</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Plain text suggested first course of action, such as a command line to execute. This can be used with custom notification messages.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Detector<wbr>Viz<wbr>Option</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/input/#DetectorVizOption">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/output/#DetectorVizOption">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#DetectorVizOptionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#DetectorVizOptionOutput">output</a> API doc for this type.
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
    <dd>{{% md %}}Color to use : gray, blue, azure, navy, brown, orange, yellow, iris, magenta, pink, purple, violet, lilac, emerald, green, aquamarine.
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
    <dd>{{% md %}}Color to use : gray, blue, azure, navy, brown, orange, yellow, iris, magenta, pink, purple, violet, lilac, emerald, green, aquamarine.
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
    <dd>{{% md %}}Color to use : gray, blue, azure, navy, brown, orange, yellow, iris, magenta, pink, purple, violet, lilac, emerald, green, aquamarine.
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

