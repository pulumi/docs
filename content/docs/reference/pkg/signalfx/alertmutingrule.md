
---
title: "AlertMutingRule"
block_external_search_index: true
---



Provides a SignalFx resource for managing alert muting rules. See [Mute Notifications](https://docs.signalfx.com/en/latest/detect-alert/mute-notifications.html) for more information.

> **WARNING** SignalFx does not allow the start time of a **currently active** muting rule to be modified. As such, attempting to modify a currently active rule will destroy the existing rule and create a new rule. This may result in the emission of notifications.

> This content is derived from https://github.com/terraform-providers/terraform-provider-signalfx/blob/master/website/docs/r/alert_muting_rule.html.markdown.



## Create a AlertMutingRule Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/signalfx/#AlertMutingRule">AlertMutingRule</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/signalfx/#AlertMutingRuleArgs">AlertMutingRuleArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">AlertMutingRule</span><span class="p">(resource_name, opts=None, </span>description=None<span class="p">, </span>detectors=None<span class="p">, </span>filters=None<span class="p">, </span>start_time=None<span class="p">, </span>stop_time=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewAlertMutingRule<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#AlertMutingRuleArgs">AlertMutingRuleArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#AlertMutingRule">AlertMutingRule</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Signalfx/Pulumi.Signalfx..AlertMutingRule.html">AlertMutingRule</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Signalfx/Pulumi.Signalfx.AlertMutingRuleArgs.html">AlertMutingRuleArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The description for this muting rule
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Detectors</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A convenience attribute that associated this muting rule with specific detector ids.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertmutingrulefilter">List&lt;Alert<wbr>Muting<wbr>Rule<wbr>Filter<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}Filters for this rule. See [Creating muting rules from scratch](https://docs.signalfx.com/en/latest/detect-alert/mute-notifications.html#rule-from-scratch) for more information.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Starting time of an alert muting rule as a Unit time stamp in seconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Stop<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Starting time of an alert muting rule as a Unix time stamp in seconds.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The description for this muting rule
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Detectors</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A convenience attribute that associated this muting rule with specific detector ids.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertmutingrulefilter">[]Alert<wbr>Muting<wbr>Rule<wbr>Filter</a></span>
    </dt>
    <dd>{{% md %}}Filters for this rule. See [Creating muting rules from scratch](https://docs.signalfx.com/en/latest/detect-alert/mute-notifications.html#rule-from-scratch) for more information.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Starting time of an alert muting rule as a Unit time stamp in seconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Stop<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Starting time of an alert muting rule as a Unix time stamp in seconds.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The description for this muting rule
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>detectors</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A convenience attribute that associated this muting rule with specific detector ids.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertmutingrulefilter">Alert<wbr>Muting<wbr>Rule<wbr>Filter[]</a></span>
    </dt>
    <dd>{{% md %}}Filters for this rule. See [Creating muting rules from scratch](https://docs.signalfx.com/en/latest/detect-alert/mute-notifications.html#rule-from-scratch) for more information.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Starting time of an alert muting rule as a Unit time stamp in seconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>stop<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Starting time of an alert muting rule as a Unix time stamp in seconds.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The description for this muting rule
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>detectors</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A convenience attribute that associated this muting rule with specific detector ids.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertmutingrulefilter">List[Alert<wbr>Muting<wbr>Rule<wbr>Filter]</a></span>
    </dt>
    <dd>{{% md %}}Filters for this rule. See [Creating muting rules from scratch](https://docs.signalfx.com/en/latest/detect-alert/mute-notifications.html#rule-from-scratch) for more information.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>start_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Starting time of an alert muting rule as a Unit time stamp in seconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>stop_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Starting time of an alert muting rule as a Unix time stamp in seconds.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## AlertMutingRule Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The description for this muting rule
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Detectors</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A convenience attribute that associated this muting rule with specific detector ids.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Effective<wbr>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertmutingrulefilter">List&lt;Alert<wbr>Muting<wbr>Rule<wbr>Filter&gt;</a></span>
    </dt>
    <dd>{{% md %}}Filters for this rule. See [Creating muting rules from scratch](https://docs.signalfx.com/en/latest/detect-alert/mute-notifications.html#rule-from-scratch) for more information.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Starting time of an alert muting rule as a Unit time stamp in seconds.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Stop<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Starting time of an alert muting rule as a Unix time stamp in seconds.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The description for this muting rule
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Detectors</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A convenience attribute that associated this muting rule with specific detector ids.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Effective<wbr>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertmutingrulefilter">[]Alert<wbr>Muting<wbr>Rule<wbr>Filter</a></span>
    </dt>
    <dd>{{% md %}}Filters for this rule. See [Creating muting rules from scratch](https://docs.signalfx.com/en/latest/detect-alert/mute-notifications.html#rule-from-scratch) for more information.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Starting time of an alert muting rule as a Unit time stamp in seconds.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Stop<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Starting time of an alert muting rule as a Unix time stamp in seconds.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The description for this muting rule
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>detectors</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A convenience attribute that associated this muting rule with specific detector ids.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>effective<wbr>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertmutingrulefilter">Alert<wbr>Muting<wbr>Rule<wbr>Filter[]</a></span>
    </dt>
    <dd>{{% md %}}Filters for this rule. See [Creating muting rules from scratch](https://docs.signalfx.com/en/latest/detect-alert/mute-notifications.html#rule-from-scratch) for more information.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Starting time of an alert muting rule as a Unit time stamp in seconds.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>stop<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Starting time of an alert muting rule as a Unix time stamp in seconds.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The description for this muting rule
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>detectors</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A convenience attribute that associated this muting rule with specific detector ids.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>effective_<wbr>start_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertmutingrulefilter">List[Alert<wbr>Muting<wbr>Rule<wbr>Filter]</a></span>
    </dt>
    <dd>{{% md %}}Filters for this rule. See [Creating muting rules from scratch](https://docs.signalfx.com/en/latest/detect-alert/mute-notifications.html#rule-from-scratch) for more information.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>start_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Starting time of an alert muting rule as a Unit time stamp in seconds.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>stop_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Starting time of an alert muting rule as a Unix time stamp in seconds.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing AlertMutingRule Resource

Get an existing AlertMutingRule resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/signalfx/#AlertMutingRuleState">AlertMutingRuleState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/signalfx/#AlertMutingRule">AlertMutingRule</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>description=None<span class="p">, </span>detectors=None<span class="p">, </span>effective_start_time=None<span class="p">, </span>filters=None<span class="p">, </span>start_time=None<span class="p">, </span>stop_time=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetAlertMutingRule<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#AlertMutingRuleState">AlertMutingRuleState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#AlertMutingRule">AlertMutingRule</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Signalfx/Pulumi.Signalfx..AlertMutingRule.html">AlertMutingRule</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Signalfx/Pulumi.Signalfx..AlertMutingRuleState.html">AlertMutingRuleState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The description for this muting rule
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Detectors</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A convenience attribute that associated this muting rule with specific detector ids.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Effective<wbr>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertmutingrulefilter">List&lt;Alert<wbr>Muting<wbr>Rule<wbr>Filter<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}Filters for this rule. See [Creating muting rules from scratch](https://docs.signalfx.com/en/latest/detect-alert/mute-notifications.html#rule-from-scratch) for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Starting time of an alert muting rule as a Unit time stamp in seconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Stop<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Starting time of an alert muting rule as a Unix time stamp in seconds.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The description for this muting rule
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Detectors</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A convenience attribute that associated this muting rule with specific detector ids.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Effective<wbr>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertmutingrulefilter">[]Alert<wbr>Muting<wbr>Rule<wbr>Filter</a></span>
    </dt>
    <dd>{{% md %}}Filters for this rule. See [Creating muting rules from scratch](https://docs.signalfx.com/en/latest/detect-alert/mute-notifications.html#rule-from-scratch) for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Starting time of an alert muting rule as a Unit time stamp in seconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Stop<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Starting time of an alert muting rule as a Unix time stamp in seconds.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The description for this muting rule
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>detectors</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A convenience attribute that associated this muting rule with specific detector ids.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>effective<wbr>Start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertmutingrulefilter">Alert<wbr>Muting<wbr>Rule<wbr>Filter[]?</a></span>
    </dt>
    <dd>{{% md %}}Filters for this rule. See [Creating muting rules from scratch](https://docs.signalfx.com/en/latest/detect-alert/mute-notifications.html#rule-from-scratch) for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>start<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Starting time of an alert muting rule as a Unit time stamp in seconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>stop<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Starting time of an alert muting rule as a Unix time stamp in seconds.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The description for this muting rule
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>detectors</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A convenience attribute that associated this muting rule with specific detector ids.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>effective_<wbr>start_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>filters</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertmutingrulefilter">List[Alert<wbr>Muting<wbr>Rule<wbr>Filter]</a></span>
    </dt>
    <dd>{{% md %}}Filters for this rule. See [Creating muting rules from scratch](https://docs.signalfx.com/en/latest/detect-alert/mute-notifications.html#rule-from-scratch) for more information.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>start_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Starting time of an alert muting rule as a Unit time stamp in seconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>stop_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Starting time of an alert muting rule as a Unix time stamp in seconds.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Alert<wbr>Muting<wbr>Rule<wbr>Filter</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/input/#AlertMutingRuleFilter">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/signalfx/types/output/#AlertMutingRuleFilter">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#AlertMutingRuleFilterArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-signalfx/sdk/go/signalfx/?tab=doc#AlertMutingRuleFilterOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Negated</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Determines if this is a "not" filter. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Property</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The property to filter.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Property<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The property value to filter.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Negated</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Determines if this is a "not" filter. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Property</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The property to filter.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Property<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The property value to filter.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>negated</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Determines if this is a "not" filter. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>property</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The property to filter.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>property<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The property value to filter.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>negated</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Determines if this is a "not" filter. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>property</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The property to filter.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>property_<wbr>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The property value to filter.
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

