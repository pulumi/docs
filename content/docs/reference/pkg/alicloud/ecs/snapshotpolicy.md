
---
title: "SnapshotPolicy"
block_external_search_index: true
---



Provides an ECS snapshot policy resource.

For information about snapshot policy and how to use it, see [Snapshot](https://www.alibabacloud.com/help/doc-detail/25460.html).

> **NOTE:** Available in 1.42.0+.

> This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/r/snapshot_policy.html.markdown.



## Create a SnapshotPolicy Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/ecs/#SnapshotPolicy">SnapshotPolicy</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/ecs/#SnapshotPolicyArgs">SnapshotPolicyArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">SnapshotPolicy</span><span class="p">(resource_name, opts=None, </span>name=None<span class="p">, </span>repeat_weekdays=None<span class="p">, </span>retention_days=None<span class="p">, </span>time_points=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewSnapshotPolicy<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/ecs?tab=doc#SnapshotPolicyArgs">SnapshotPolicyArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/ecs?tab=doc#SnapshotPolicy">SnapshotPolicy</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Ecs.SnapshotPolicy.html">SnapshotPolicy</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Ecs.SnapshotPolicyArgs.html">SnapshotPolicyArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The snapshot policy name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Repeat<wbr>Weekdays</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}The automatic snapshot repetition dates. The unit of measurement is day and the repeating cycle is a week. Value range: [1, 7], which represents days starting from Monday to Sunday, for example 1  indicates Monday. When you want to schedule multiple automatic snapshot tasks for a disk in a week, you can set the RepeatWeekdays to an array.
- A maximum of seven time points can be selected.
- The format is  an JSON array of ["1", "2", … "7"]  and the time points are separated by commas (,).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Retention<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The snapshot retention time, and the unit of measurement is day. Optional values:
- -1: The automatic snapshots are retained permanently.
- [1, 65536]: The number of days retained.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Time<wbr>Points</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}The automatic snapshot creation schedule, and the unit of measurement is hour. Value range: [0, 23], which represents from 00:00 to 24:00,  for example 1 indicates 01:00. When you want to schedule multiple automatic snapshot tasks for a disk in a day, you can set the TimePoints to an array.
- A maximum of 24 time points can be selected.
- The format is  an JSON array of ["0", "1", … "23"] and the time points are separated by commas (,).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The snapshot policy name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Repeat<wbr>Weekdays</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The automatic snapshot repetition dates. The unit of measurement is day and the repeating cycle is a week. Value range: [1, 7], which represents days starting from Monday to Sunday, for example 1  indicates Monday. When you want to schedule multiple automatic snapshot tasks for a disk in a week, you can set the RepeatWeekdays to an array.
- A maximum of seven time points can be selected.
- The format is  an JSON array of ["1", "2", … "7"]  and the time points are separated by commas (,).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Retention<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The snapshot retention time, and the unit of measurement is day. Optional values:
- -1: The automatic snapshots are retained permanently.
- [1, 65536]: The number of days retained.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Time<wbr>Points</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The automatic snapshot creation schedule, and the unit of measurement is hour. Value range: [0, 23], which represents from 00:00 to 24:00,  for example 1 indicates 01:00. When you want to schedule multiple automatic snapshot tasks for a disk in a day, you can set the TimePoints to an array.
- A maximum of 24 time points can be selected.
- The format is  an JSON array of ["0", "1", … "23"] and the time points are separated by commas (,).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The snapshot policy name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>repeat<wbr>Weekdays</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}The automatic snapshot repetition dates. The unit of measurement is day and the repeating cycle is a week. Value range: [1, 7], which represents days starting from Monday to Sunday, for example 1  indicates Monday. When you want to schedule multiple automatic snapshot tasks for a disk in a week, you can set the RepeatWeekdays to an array.
- A maximum of seven time points can be selected.
- The format is  an JSON array of ["1", "2", … "7"]  and the time points are separated by commas (,).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>retention<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The snapshot retention time, and the unit of measurement is day. Optional values:
- -1: The automatic snapshots are retained permanently.
- [1, 65536]: The number of days retained.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>time<wbr>Points</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}The automatic snapshot creation schedule, and the unit of measurement is hour. Value range: [0, 23], which represents from 00:00 to 24:00,  for example 1 indicates 01:00. When you want to schedule multiple automatic snapshot tasks for a disk in a day, you can set the TimePoints to an array.
- A maximum of 24 time points can be selected.
- The format is  an JSON array of ["0", "1", … "23"] and the time points are separated by commas (,).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The snapshot policy name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>repeat_<wbr>weekdays</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The automatic snapshot repetition dates. The unit of measurement is day and the repeating cycle is a week. Value range: [1, 7], which represents days starting from Monday to Sunday, for example 1  indicates Monday. When you want to schedule multiple automatic snapshot tasks for a disk in a week, you can set the RepeatWeekdays to an array.
- A maximum of seven time points can be selected.
- The format is  an JSON array of ["1", "2", … "7"]  and the time points are separated by commas (,).
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>retention_<wbr>days</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The snapshot retention time, and the unit of measurement is day. Optional values:
- -1: The automatic snapshots are retained permanently.
- [1, 65536]: The number of days retained.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>time_<wbr>points</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The automatic snapshot creation schedule, and the unit of measurement is hour. Value range: [0, 23], which represents from 00:00 to 24:00,  for example 1 indicates 01:00. When you want to schedule multiple automatic snapshot tasks for a disk in a day, you can set the TimePoints to an array.
- A maximum of 24 time points can be selected.
- The format is  an JSON array of ["0", "1", … "23"] and the time points are separated by commas (,).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## SnapshotPolicy Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The snapshot policy name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Repeat<wbr>Weekdays</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}The automatic snapshot repetition dates. The unit of measurement is day and the repeating cycle is a week. Value range: [1, 7], which represents days starting from Monday to Sunday, for example 1  indicates Monday. When you want to schedule multiple automatic snapshot tasks for a disk in a week, you can set the RepeatWeekdays to an array.
- A maximum of seven time points can be selected.
- The format is  an JSON array of ["1", "2", … "7"]  and the time points are separated by commas (,).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Retention<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The snapshot retention time, and the unit of measurement is day. Optional values:
- -1: The automatic snapshots are retained permanently.
- [1, 65536]: The number of days retained.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Time<wbr>Points</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}The automatic snapshot creation schedule, and the unit of measurement is hour. Value range: [0, 23], which represents from 00:00 to 24:00,  for example 1 indicates 01:00. When you want to schedule multiple automatic snapshot tasks for a disk in a day, you can set the TimePoints to an array.
- A maximum of 24 time points can be selected.
- The format is  an JSON array of ["0", "1", … "23"] and the time points are separated by commas (,).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The snapshot policy name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Repeat<wbr>Weekdays</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The automatic snapshot repetition dates. The unit of measurement is day and the repeating cycle is a week. Value range: [1, 7], which represents days starting from Monday to Sunday, for example 1  indicates Monday. When you want to schedule multiple automatic snapshot tasks for a disk in a week, you can set the RepeatWeekdays to an array.
- A maximum of seven time points can be selected.
- The format is  an JSON array of ["1", "2", … "7"]  and the time points are separated by commas (,).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Retention<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The snapshot retention time, and the unit of measurement is day. Optional values:
- -1: The automatic snapshots are retained permanently.
- [1, 65536]: The number of days retained.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Time<wbr>Points</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The automatic snapshot creation schedule, and the unit of measurement is hour. Value range: [0, 23], which represents from 00:00 to 24:00,  for example 1 indicates 01:00. When you want to schedule multiple automatic snapshot tasks for a disk in a day, you can set the TimePoints to an array.
- A maximum of 24 time points can be selected.
- The format is  an JSON array of ["0", "1", … "23"] and the time points are separated by commas (,).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The snapshot policy name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>repeat<wbr>Weekdays</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}The automatic snapshot repetition dates. The unit of measurement is day and the repeating cycle is a week. Value range: [1, 7], which represents days starting from Monday to Sunday, for example 1  indicates Monday. When you want to schedule multiple automatic snapshot tasks for a disk in a week, you can set the RepeatWeekdays to an array.
- A maximum of seven time points can be selected.
- The format is  an JSON array of ["1", "2", … "7"]  and the time points are separated by commas (,).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>retention<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The snapshot retention time, and the unit of measurement is day. Optional values:
- -1: The automatic snapshots are retained permanently.
- [1, 65536]: The number of days retained.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>time<wbr>Points</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}The automatic snapshot creation schedule, and the unit of measurement is hour. Value range: [0, 23], which represents from 00:00 to 24:00,  for example 1 indicates 01:00. When you want to schedule multiple automatic snapshot tasks for a disk in a day, you can set the TimePoints to an array.
- A maximum of 24 time points can be selected.
- The format is  an JSON array of ["0", "1", … "23"] and the time points are separated by commas (,).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The snapshot policy name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>repeat_<wbr>weekdays</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The automatic snapshot repetition dates. The unit of measurement is day and the repeating cycle is a week. Value range: [1, 7], which represents days starting from Monday to Sunday, for example 1  indicates Monday. When you want to schedule multiple automatic snapshot tasks for a disk in a week, you can set the RepeatWeekdays to an array.
- A maximum of seven time points can be selected.
- The format is  an JSON array of ["1", "2", … "7"]  and the time points are separated by commas (,).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>retention_<wbr>days</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The snapshot retention time, and the unit of measurement is day. Optional values:
- -1: The automatic snapshots are retained permanently.
- [1, 65536]: The number of days retained.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>time_<wbr>points</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The automatic snapshot creation schedule, and the unit of measurement is hour. Value range: [0, 23], which represents from 00:00 to 24:00,  for example 1 indicates 01:00. When you want to schedule multiple automatic snapshot tasks for a disk in a day, you can set the TimePoints to an array.
- A maximum of 24 time points can be selected.
- The format is  an JSON array of ["0", "1", … "23"] and the time points are separated by commas (,).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing SnapshotPolicy Resource

Get an existing SnapshotPolicy resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/ecs/#SnapshotPolicyState">SnapshotPolicyState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/ecs/#SnapshotPolicy">SnapshotPolicy</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>name=None<span class="p">, </span>repeat_weekdays=None<span class="p">, </span>retention_days=None<span class="p">, </span>time_points=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetSnapshotPolicy<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/ecs?tab=doc#SnapshotPolicyState">SnapshotPolicyState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/ecs?tab=doc#SnapshotPolicy">SnapshotPolicy</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Ecs.SnapshotPolicy.html">SnapshotPolicy</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Ecs.SnapshotPolicyState.html">SnapshotPolicyState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The snapshot policy name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Repeat<wbr>Weekdays</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The automatic snapshot repetition dates. The unit of measurement is day and the repeating cycle is a week. Value range: [1, 7], which represents days starting from Monday to Sunday, for example 1  indicates Monday. When you want to schedule multiple automatic snapshot tasks for a disk in a week, you can set the RepeatWeekdays to an array.
- A maximum of seven time points can be selected.
- The format is  an JSON array of ["1", "2", … "7"]  and the time points are separated by commas (,).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retention<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The snapshot retention time, and the unit of measurement is day. Optional values:
- -1: The automatic snapshots are retained permanently.
- [1, 65536]: The number of days retained.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time<wbr>Points</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The automatic snapshot creation schedule, and the unit of measurement is hour. Value range: [0, 23], which represents from 00:00 to 24:00,  for example 1 indicates 01:00. When you want to schedule multiple automatic snapshot tasks for a disk in a day, you can set the TimePoints to an array.
- A maximum of 24 time points can be selected.
- The format is  an JSON array of ["0", "1", … "23"] and the time points are separated by commas (,).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The snapshot policy name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Repeat<wbr>Weekdays</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The automatic snapshot repetition dates. The unit of measurement is day and the repeating cycle is a week. Value range: [1, 7], which represents days starting from Monday to Sunday, for example 1  indicates Monday. When you want to schedule multiple automatic snapshot tasks for a disk in a week, you can set the RepeatWeekdays to an array.
- A maximum of seven time points can be selected.
- The format is  an JSON array of ["1", "2", … "7"]  and the time points are separated by commas (,).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retention<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The snapshot retention time, and the unit of measurement is day. Optional values:
- -1: The automatic snapshots are retained permanently.
- [1, 65536]: The number of days retained.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time<wbr>Points</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The automatic snapshot creation schedule, and the unit of measurement is hour. Value range: [0, 23], which represents from 00:00 to 24:00,  for example 1 indicates 01:00. When you want to schedule multiple automatic snapshot tasks for a disk in a day, you can set the TimePoints to an array.
- A maximum of 24 time points can be selected.
- The format is  an JSON array of ["0", "1", … "23"] and the time points are separated by commas (,).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The snapshot policy name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>repeat<wbr>Weekdays</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The automatic snapshot repetition dates. The unit of measurement is day and the repeating cycle is a week. Value range: [1, 7], which represents days starting from Monday to Sunday, for example 1  indicates Monday. When you want to schedule multiple automatic snapshot tasks for a disk in a week, you can set the RepeatWeekdays to an array.
- A maximum of seven time points can be selected.
- The format is  an JSON array of ["1", "2", … "7"]  and the time points are separated by commas (,).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retention<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The snapshot retention time, and the unit of measurement is day. Optional values:
- -1: The automatic snapshots are retained permanently.
- [1, 65536]: The number of days retained.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>time<wbr>Points</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The automatic snapshot creation schedule, and the unit of measurement is hour. Value range: [0, 23], which represents from 00:00 to 24:00,  for example 1 indicates 01:00. When you want to schedule multiple automatic snapshot tasks for a disk in a day, you can set the TimePoints to an array.
- A maximum of 24 time points can be selected.
- The format is  an JSON array of ["0", "1", … "23"] and the time points are separated by commas (,).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The snapshot policy name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>repeat_<wbr>weekdays</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The automatic snapshot repetition dates. The unit of measurement is day and the repeating cycle is a week. Value range: [1, 7], which represents days starting from Monday to Sunday, for example 1  indicates Monday. When you want to schedule multiple automatic snapshot tasks for a disk in a week, you can set the RepeatWeekdays to an array.
- A maximum of seven time points can be selected.
- The format is  an JSON array of ["1", "2", … "7"]  and the time points are separated by commas (,).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retention_<wbr>days</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The snapshot retention time, and the unit of measurement is day. Optional values:
- -1: The automatic snapshots are retained permanently.
- [1, 65536]: The number of days retained.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>time_<wbr>points</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The automatic snapshot creation schedule, and the unit of measurement is hour. Value range: [0, 23], which represents from 00:00 to 24:00,  for example 1 indicates 01:00. When you want to schedule multiple automatic snapshot tasks for a disk in a day, you can set the TimePoints to an array.
- A maximum of 24 time points can be selected.
- The format is  an JSON array of ["0", "1", … "23"] and the time points are separated by commas (,).
{{% /md %}}</dd>

</dl>
{{% /choosable %}}











<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-alicloud">https://github.com/pulumi/pulumi-alicloud</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

