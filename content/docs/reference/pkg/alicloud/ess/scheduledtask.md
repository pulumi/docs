
---
title: "ScheduledTask"
block_external_search_index: true
---






## Create a ScheduledTask Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/ess/#ScheduledTask">ScheduledTask</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/ess/#ScheduledTaskArgs">ScheduledTaskArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">ScheduledTask</span><span class="p">(resource_name, opts=None, </span>description=None<span class="p">, </span>launch_expiration_time=None<span class="p">, </span>launch_time=None<span class="p">, </span>recurrence_end_time=None<span class="p">, </span>recurrence_type=None<span class="p">, </span>recurrence_value=None<span class="p">, </span>scheduled_action=None<span class="p">, </span>scheduled_task_name=None<span class="p">, </span>task_enabled=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewScheduledTask<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/ess?tab=doc#ScheduledTaskArgs">ScheduledTaskArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/ess?tab=doc#ScheduledTask">ScheduledTask</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Ess.ScheduledTask.html">ScheduledTask</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Ess.ScheduledTaskArgs.html">ScheduledTaskArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of the scheduled task, which is 2-200 characters (English or Chinese) long.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Launch<wbr>Expiration<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The time period during which a failed scheduled task is retried. Unit: seconds. Valid values: 0 to 21600. Default value: 600
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Launch<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The time at which the scheduled task is triggered. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. 
The time must be in UTC. You cannot enter a time point later than 90 days from the date of scheduled task creation.
If the `recurrence_type` parameter is specified, the task is executed repeatedly at the time specified by LaunchTime.
Otherwise, the task is only executed once at the date and time specified by LaunchTime.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Recurrence<wbr>End<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the end time after which the scheduled task is no longer repeated. 
Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format.
The time must be in UTC. You cannot enter a time point later than 365 days from the date of scheduled task creation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Recurrence<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the recurrence type of the scheduled task. 
If set, both `recurrence_value` and `recurrence_end_time` must be set. Valid values:
- Daily: The scheduled task is executed once every specified number of days.
- Weekly: The scheduled task is executed on each specified day of a week.
- Monthly: The scheduled task is executed on each specified day of a month.
- Cron: (Available in 1.60.0+) The scheduled task is executed based on the specified cron expression.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Recurrence<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies how often a scheduled task recurs. The valid value depends on `recurrence_type`
- Daily: You can enter one value. Valid values: 1 to 31.
- Weekly: You can enter multiple values and separate them with commas (,). For example, the values 0 to 6 correspond to the days of the week in sequence from Sunday to Saturday.
- Monthly: You can enter two values in A-B format. Valid values of A and B: 1 to 31. The value of B must be greater than or equal to the value of A.
- Cron: You can enter a cron expression which is written in UTC and consists of five fields: minute, hour, day of month (date), month, and day of week. The expression can contain wildcard characters including commas (,), question marks (?), hyphens (-), asterisks (*), number signs (#), forward slashes (/), and the L and W letters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Scheduled<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The operation to be performed when a scheduled task is triggered. Enter the unique identifier of a scaling rule.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scheduled<wbr>Task<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Display name of the scheduled task, which must be 2-40 characters (English or Chinese) long.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Task<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Specifies whether to start the scheduled task. Default to true.
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
    <dd>{{% md %}}Description of the scheduled task, which is 2-200 characters (English or Chinese) long.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Launch<wbr>Expiration<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The time period during which a failed scheduled task is retried. Unit: seconds. Valid values: 0 to 21600. Default value: 600
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Launch<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The time at which the scheduled task is triggered. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. 
The time must be in UTC. You cannot enter a time point later than 90 days from the date of scheduled task creation.
If the `recurrence_type` parameter is specified, the task is executed repeatedly at the time specified by LaunchTime.
Otherwise, the task is only executed once at the date and time specified by LaunchTime.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Recurrence<wbr>End<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the end time after which the scheduled task is no longer repeated. 
Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format.
The time must be in UTC. You cannot enter a time point later than 365 days from the date of scheduled task creation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Recurrence<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the recurrence type of the scheduled task. 
If set, both `recurrence_value` and `recurrence_end_time` must be set. Valid values:
- Daily: The scheduled task is executed once every specified number of days.
- Weekly: The scheduled task is executed on each specified day of a week.
- Monthly: The scheduled task is executed on each specified day of a month.
- Cron: (Available in 1.60.0+) The scheduled task is executed based on the specified cron expression.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Recurrence<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies how often a scheduled task recurs. The valid value depends on `recurrence_type`
- Daily: You can enter one value. Valid values: 1 to 31.
- Weekly: You can enter multiple values and separate them with commas (,). For example, the values 0 to 6 correspond to the days of the week in sequence from Sunday to Saturday.
- Monthly: You can enter two values in A-B format. Valid values of A and B: 1 to 31. The value of B must be greater than or equal to the value of A.
- Cron: You can enter a cron expression which is written in UTC and consists of five fields: minute, hour, day of month (date), month, and day of week. The expression can contain wildcard characters including commas (,), question marks (?), hyphens (-), asterisks (*), number signs (#), forward slashes (/), and the L and W letters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Scheduled<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The operation to be performed when a scheduled task is triggered. Enter the unique identifier of a scaling rule.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scheduled<wbr>Task<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Display name of the scheduled task, which must be 2-40 characters (English or Chinese) long.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Task<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Specifies whether to start the scheduled task. Default to true.
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
    <dd>{{% md %}}Description of the scheduled task, which is 2-200 characters (English or Chinese) long.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>launch<wbr>Expiration<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The time period during which a failed scheduled task is retried. Unit: seconds. Valid values: 0 to 21600. Default value: 600
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>launch<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The time at which the scheduled task is triggered. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. 
The time must be in UTC. You cannot enter a time point later than 90 days from the date of scheduled task creation.
If the `recurrence_type` parameter is specified, the task is executed repeatedly at the time specified by LaunchTime.
Otherwise, the task is only executed once at the date and time specified by LaunchTime.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>recurrence<wbr>End<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the end time after which the scheduled task is no longer repeated. 
Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format.
The time must be in UTC. You cannot enter a time point later than 365 days from the date of scheduled task creation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>recurrence<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the recurrence type of the scheduled task. 
If set, both `recurrence_value` and `recurrence_end_time` must be set. Valid values:
- Daily: The scheduled task is executed once every specified number of days.
- Weekly: The scheduled task is executed on each specified day of a week.
- Monthly: The scheduled task is executed on each specified day of a month.
- Cron: (Available in 1.60.0+) The scheduled task is executed based on the specified cron expression.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>recurrence<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies how often a scheduled task recurs. The valid value depends on `recurrence_type`
- Daily: You can enter one value. Valid values: 1 to 31.
- Weekly: You can enter multiple values and separate them with commas (,). For example, the values 0 to 6 correspond to the days of the week in sequence from Sunday to Saturday.
- Monthly: You can enter two values in A-B format. Valid values of A and B: 1 to 31. The value of B must be greater than or equal to the value of A.
- Cron: You can enter a cron expression which is written in UTC and consists of five fields: minute, hour, day of month (date), month, and day of week. The expression can contain wildcard characters including commas (,), question marks (?), hyphens (-), asterisks (*), number signs (#), forward slashes (/), and the L and W letters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>scheduled<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The operation to be performed when a scheduled task is triggered. Enter the unique identifier of a scaling rule.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scheduled<wbr>Task<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Display name of the scheduled task, which must be 2-40 characters (English or Chinese) long.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>task<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Specifies whether to start the scheduled task. Default to true.
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
    <dd>{{% md %}}Description of the scheduled task, which is 2-200 characters (English or Chinese) long.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>launch_<wbr>expiration_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The time period during which a failed scheduled task is retried. Unit: seconds. Valid values: 0 to 21600. Default value: 600
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>launch_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The time at which the scheduled task is triggered. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. 
The time must be in UTC. You cannot enter a time point later than 90 days from the date of scheduled task creation.
If the `recurrence_type` parameter is specified, the task is executed repeatedly at the time specified by LaunchTime.
Otherwise, the task is only executed once at the date and time specified by LaunchTime.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>recurrence_<wbr>end_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the end time after which the scheduled task is no longer repeated. 
Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format.
The time must be in UTC. You cannot enter a time point later than 365 days from the date of scheduled task creation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>recurrence_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the recurrence type of the scheduled task. 
If set, both `recurrence_value` and `recurrence_end_time` must be set. Valid values:
- Daily: The scheduled task is executed once every specified number of days.
- Weekly: The scheduled task is executed on each specified day of a week.
- Monthly: The scheduled task is executed on each specified day of a month.
- Cron: (Available in 1.60.0+) The scheduled task is executed based on the specified cron expression.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>recurrence_<wbr>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies how often a scheduled task recurs. The valid value depends on `recurrence_type`
- Daily: You can enter one value. Valid values: 1 to 31.
- Weekly: You can enter multiple values and separate them with commas (,). For example, the values 0 to 6 correspond to the days of the week in sequence from Sunday to Saturday.
- Monthly: You can enter two values in A-B format. Valid values of A and B: 1 to 31. The value of B must be greater than or equal to the value of A.
- Cron: You can enter a cron expression which is written in UTC and consists of five fields: minute, hour, day of month (date), month, and day of week. The expression can contain wildcard characters including commas (,), question marks (?), hyphens (-), asterisks (*), number signs (#), forward slashes (/), and the L and W letters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>scheduled_<wbr>action</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The operation to be performed when a scheduled task is triggered. Enter the unique identifier of a scaling rule.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scheduled_<wbr>task_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Display name of the scheduled task, which must be 2-40 characters (English or Chinese) long.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>task_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specifies whether to start the scheduled task. Default to true.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## ScheduledTask Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Description of the scheduled task, which is 2-200 characters (English or Chinese) long.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Launch<wbr>Expiration<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The time period during which a failed scheduled task is retried. Unit: seconds. Valid values: 0 to 21600. Default value: 600
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Launch<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The time at which the scheduled task is triggered. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. 
The time must be in UTC. You cannot enter a time point later than 90 days from the date of scheduled task creation.
If the `recurrence_type` parameter is specified, the task is executed repeatedly at the time specified by LaunchTime.
Otherwise, the task is only executed once at the date and time specified by LaunchTime.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Recurrence<wbr>End<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the end time after which the scheduled task is no longer repeated. 
Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format.
The time must be in UTC. You cannot enter a time point later than 365 days from the date of scheduled task creation.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Recurrence<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the recurrence type of the scheduled task. 
If set, both `recurrence_value` and `recurrence_end_time` must be set. Valid values:
- Daily: The scheduled task is executed once every specified number of days.
- Weekly: The scheduled task is executed on each specified day of a week.
- Monthly: The scheduled task is executed on each specified day of a month.
- Cron: (Available in 1.60.0+) The scheduled task is executed based on the specified cron expression.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Recurrence<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies how often a scheduled task recurs. The valid value depends on `recurrence_type`
- Daily: You can enter one value. Valid values: 1 to 31.
- Weekly: You can enter multiple values and separate them with commas (,). For example, the values 0 to 6 correspond to the days of the week in sequence from Sunday to Saturday.
- Monthly: You can enter two values in A-B format. Valid values of A and B: 1 to 31. The value of B must be greater than or equal to the value of A.
- Cron: You can enter a cron expression which is written in UTC and consists of five fields: minute, hour, day of month (date), month, and day of week. The expression can contain wildcard characters including commas (,), question marks (?), hyphens (-), asterisks (*), number signs (#), forward slashes (/), and the L and W letters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Scheduled<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The operation to be performed when a scheduled task is triggered. Enter the unique identifier of a scaling rule.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Scheduled<wbr>Task<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Display name of the scheduled task, which must be 2-40 characters (English or Chinese) long.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Task<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Specifies whether to start the scheduled task. Default to true.
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
    <dd>{{% md %}}Description of the scheduled task, which is 2-200 characters (English or Chinese) long.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Launch<wbr>Expiration<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The time period during which a failed scheduled task is retried. Unit: seconds. Valid values: 0 to 21600. Default value: 600
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Launch<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The time at which the scheduled task is triggered. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. 
The time must be in UTC. You cannot enter a time point later than 90 days from the date of scheduled task creation.
If the `recurrence_type` parameter is specified, the task is executed repeatedly at the time specified by LaunchTime.
Otherwise, the task is only executed once at the date and time specified by LaunchTime.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Recurrence<wbr>End<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the end time after which the scheduled task is no longer repeated. 
Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format.
The time must be in UTC. You cannot enter a time point later than 365 days from the date of scheduled task creation.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Recurrence<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the recurrence type of the scheduled task. 
If set, both `recurrence_value` and `recurrence_end_time` must be set. Valid values:
- Daily: The scheduled task is executed once every specified number of days.
- Weekly: The scheduled task is executed on each specified day of a week.
- Monthly: The scheduled task is executed on each specified day of a month.
- Cron: (Available in 1.60.0+) The scheduled task is executed based on the specified cron expression.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Recurrence<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies how often a scheduled task recurs. The valid value depends on `recurrence_type`
- Daily: You can enter one value. Valid values: 1 to 31.
- Weekly: You can enter multiple values and separate them with commas (,). For example, the values 0 to 6 correspond to the days of the week in sequence from Sunday to Saturday.
- Monthly: You can enter two values in A-B format. Valid values of A and B: 1 to 31. The value of B must be greater than or equal to the value of A.
- Cron: You can enter a cron expression which is written in UTC and consists of five fields: minute, hour, day of month (date), month, and day of week. The expression can contain wildcard characters including commas (,), question marks (?), hyphens (-), asterisks (*), number signs (#), forward slashes (/), and the L and W letters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Scheduled<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The operation to be performed when a scheduled task is triggered. Enter the unique identifier of a scaling rule.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Scheduled<wbr>Task<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Display name of the scheduled task, which must be 2-40 characters (English or Chinese) long.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Task<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Specifies whether to start the scheduled task. Default to true.
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
    <dd>{{% md %}}Description of the scheduled task, which is 2-200 characters (English or Chinese) long.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>launch<wbr>Expiration<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The time period during which a failed scheduled task is retried. Unit: seconds. Valid values: 0 to 21600. Default value: 600
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>launch<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The time at which the scheduled task is triggered. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. 
The time must be in UTC. You cannot enter a time point later than 90 days from the date of scheduled task creation.
If the `recurrence_type` parameter is specified, the task is executed repeatedly at the time specified by LaunchTime.
Otherwise, the task is only executed once at the date and time specified by LaunchTime.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>recurrence<wbr>End<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the end time after which the scheduled task is no longer repeated. 
Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format.
The time must be in UTC. You cannot enter a time point later than 365 days from the date of scheduled task creation.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>recurrence<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the recurrence type of the scheduled task. 
If set, both `recurrence_value` and `recurrence_end_time` must be set. Valid values:
- Daily: The scheduled task is executed once every specified number of days.
- Weekly: The scheduled task is executed on each specified day of a week.
- Monthly: The scheduled task is executed on each specified day of a month.
- Cron: (Available in 1.60.0+) The scheduled task is executed based on the specified cron expression.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>recurrence<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies how often a scheduled task recurs. The valid value depends on `recurrence_type`
- Daily: You can enter one value. Valid values: 1 to 31.
- Weekly: You can enter multiple values and separate them with commas (,). For example, the values 0 to 6 correspond to the days of the week in sequence from Sunday to Saturday.
- Monthly: You can enter two values in A-B format. Valid values of A and B: 1 to 31. The value of B must be greater than or equal to the value of A.
- Cron: You can enter a cron expression which is written in UTC and consists of five fields: minute, hour, day of month (date), month, and day of week. The expression can contain wildcard characters including commas (,), question marks (?), hyphens (-), asterisks (*), number signs (#), forward slashes (/), and the L and W letters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>scheduled<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The operation to be performed when a scheduled task is triggered. Enter the unique identifier of a scaling rule.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>scheduled<wbr>Task<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Display name of the scheduled task, which must be 2-40 characters (English or Chinese) long.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>task<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Specifies whether to start the scheduled task. Default to true.
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
    <dd>{{% md %}}Description of the scheduled task, which is 2-200 characters (English or Chinese) long.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>launch_<wbr>expiration_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The time period during which a failed scheduled task is retried. Unit: seconds. Valid values: 0 to 21600. Default value: 600
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>launch_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The time at which the scheduled task is triggered. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. 
The time must be in UTC. You cannot enter a time point later than 90 days from the date of scheduled task creation.
If the `recurrence_type` parameter is specified, the task is executed repeatedly at the time specified by LaunchTime.
Otherwise, the task is only executed once at the date and time specified by LaunchTime.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>recurrence_<wbr>end_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the end time after which the scheduled task is no longer repeated. 
Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format.
The time must be in UTC. You cannot enter a time point later than 365 days from the date of scheduled task creation.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>recurrence_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the recurrence type of the scheduled task. 
If set, both `recurrence_value` and `recurrence_end_time` must be set. Valid values:
- Daily: The scheduled task is executed once every specified number of days.
- Weekly: The scheduled task is executed on each specified day of a week.
- Monthly: The scheduled task is executed on each specified day of a month.
- Cron: (Available in 1.60.0+) The scheduled task is executed based on the specified cron expression.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>recurrence_<wbr>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies how often a scheduled task recurs. The valid value depends on `recurrence_type`
- Daily: You can enter one value. Valid values: 1 to 31.
- Weekly: You can enter multiple values and separate them with commas (,). For example, the values 0 to 6 correspond to the days of the week in sequence from Sunday to Saturday.
- Monthly: You can enter two values in A-B format. Valid values of A and B: 1 to 31. The value of B must be greater than or equal to the value of A.
- Cron: You can enter a cron expression which is written in UTC and consists of five fields: minute, hour, day of month (date), month, and day of week. The expression can contain wildcard characters including commas (,), question marks (?), hyphens (-), asterisks (*), number signs (#), forward slashes (/), and the L and W letters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>scheduled_<wbr>action</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The operation to be performed when a scheduled task is triggered. Enter the unique identifier of a scaling rule.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>scheduled_<wbr>task_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Display name of the scheduled task, which must be 2-40 characters (English or Chinese) long.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>task_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specifies whether to start the scheduled task. Default to true.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing ScheduledTask Resource

Get an existing ScheduledTask resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/ess/#ScheduledTaskState">ScheduledTaskState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/ess/#ScheduledTask">ScheduledTask</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>description=None<span class="p">, </span>launch_expiration_time=None<span class="p">, </span>launch_time=None<span class="p">, </span>recurrence_end_time=None<span class="p">, </span>recurrence_type=None<span class="p">, </span>recurrence_value=None<span class="p">, </span>scheduled_action=None<span class="p">, </span>scheduled_task_name=None<span class="p">, </span>task_enabled=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetScheduledTask<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/ess?tab=doc#ScheduledTaskState">ScheduledTaskState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/ess?tab=doc#ScheduledTask">ScheduledTask</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Ess.ScheduledTask.html">ScheduledTask</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Ess.ScheduledTaskState.html">ScheduledTaskState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
    <dd>{{% md %}}Description of the scheduled task, which is 2-200 characters (English or Chinese) long.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Launch<wbr>Expiration<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The time period during which a failed scheduled task is retried. Unit: seconds. Valid values: 0 to 21600. Default value: 600
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Launch<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The time at which the scheduled task is triggered. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. 
The time must be in UTC. You cannot enter a time point later than 90 days from the date of scheduled task creation.
If the `recurrence_type` parameter is specified, the task is executed repeatedly at the time specified by LaunchTime.
Otherwise, the task is only executed once at the date and time specified by LaunchTime.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Recurrence<wbr>End<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the end time after which the scheduled task is no longer repeated. 
Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format.
The time must be in UTC. You cannot enter a time point later than 365 days from the date of scheduled task creation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Recurrence<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the recurrence type of the scheduled task. 
If set, both `recurrence_value` and `recurrence_end_time` must be set. Valid values:
- Daily: The scheduled task is executed once every specified number of days.
- Weekly: The scheduled task is executed on each specified day of a week.
- Monthly: The scheduled task is executed on each specified day of a month.
- Cron: (Available in 1.60.0+) The scheduled task is executed based on the specified cron expression.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Recurrence<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies how often a scheduled task recurs. The valid value depends on `recurrence_type`
- Daily: You can enter one value. Valid values: 1 to 31.
- Weekly: You can enter multiple values and separate them with commas (,). For example, the values 0 to 6 correspond to the days of the week in sequence from Sunday to Saturday.
- Monthly: You can enter two values in A-B format. Valid values of A and B: 1 to 31. The value of B must be greater than or equal to the value of A.
- Cron: You can enter a cron expression which is written in UTC and consists of five fields: minute, hour, day of month (date), month, and day of week. The expression can contain wildcard characters including commas (,), question marks (?), hyphens (-), asterisks (*), number signs (#), forward slashes (/), and the L and W letters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scheduled<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The operation to be performed when a scheduled task is triggered. Enter the unique identifier of a scaling rule.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scheduled<wbr>Task<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Display name of the scheduled task, which must be 2-40 characters (English or Chinese) long.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Task<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Specifies whether to start the scheduled task. Default to true.
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
    <dd>{{% md %}}Description of the scheduled task, which is 2-200 characters (English or Chinese) long.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Launch<wbr>Expiration<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The time period during which a failed scheduled task is retried. Unit: seconds. Valid values: 0 to 21600. Default value: 600
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Launch<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The time at which the scheduled task is triggered. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. 
The time must be in UTC. You cannot enter a time point later than 90 days from the date of scheduled task creation.
If the `recurrence_type` parameter is specified, the task is executed repeatedly at the time specified by LaunchTime.
Otherwise, the task is only executed once at the date and time specified by LaunchTime.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Recurrence<wbr>End<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the end time after which the scheduled task is no longer repeated. 
Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format.
The time must be in UTC. You cannot enter a time point later than 365 days from the date of scheduled task creation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Recurrence<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the recurrence type of the scheduled task. 
If set, both `recurrence_value` and `recurrence_end_time` must be set. Valid values:
- Daily: The scheduled task is executed once every specified number of days.
- Weekly: The scheduled task is executed on each specified day of a week.
- Monthly: The scheduled task is executed on each specified day of a month.
- Cron: (Available in 1.60.0+) The scheduled task is executed based on the specified cron expression.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Recurrence<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies how often a scheduled task recurs. The valid value depends on `recurrence_type`
- Daily: You can enter one value. Valid values: 1 to 31.
- Weekly: You can enter multiple values and separate them with commas (,). For example, the values 0 to 6 correspond to the days of the week in sequence from Sunday to Saturday.
- Monthly: You can enter two values in A-B format. Valid values of A and B: 1 to 31. The value of B must be greater than or equal to the value of A.
- Cron: You can enter a cron expression which is written in UTC and consists of five fields: minute, hour, day of month (date), month, and day of week. The expression can contain wildcard characters including commas (,), question marks (?), hyphens (-), asterisks (*), number signs (#), forward slashes (/), and the L and W letters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scheduled<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The operation to be performed when a scheduled task is triggered. Enter the unique identifier of a scaling rule.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scheduled<wbr>Task<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Display name of the scheduled task, which must be 2-40 characters (English or Chinese) long.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Task<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Specifies whether to start the scheduled task. Default to true.
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
    <dd>{{% md %}}Description of the scheduled task, which is 2-200 characters (English or Chinese) long.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>launch<wbr>Expiration<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The time period during which a failed scheduled task is retried. Unit: seconds. Valid values: 0 to 21600. Default value: 600
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>launch<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The time at which the scheduled task is triggered. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. 
The time must be in UTC. You cannot enter a time point later than 90 days from the date of scheduled task creation.
If the `recurrence_type` parameter is specified, the task is executed repeatedly at the time specified by LaunchTime.
Otherwise, the task is only executed once at the date and time specified by LaunchTime.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>recurrence<wbr>End<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the end time after which the scheduled task is no longer repeated. 
Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format.
The time must be in UTC. You cannot enter a time point later than 365 days from the date of scheduled task creation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>recurrence<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the recurrence type of the scheduled task. 
If set, both `recurrence_value` and `recurrence_end_time` must be set. Valid values:
- Daily: The scheduled task is executed once every specified number of days.
- Weekly: The scheduled task is executed on each specified day of a week.
- Monthly: The scheduled task is executed on each specified day of a month.
- Cron: (Available in 1.60.0+) The scheduled task is executed based on the specified cron expression.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>recurrence<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies how often a scheduled task recurs. The valid value depends on `recurrence_type`
- Daily: You can enter one value. Valid values: 1 to 31.
- Weekly: You can enter multiple values and separate them with commas (,). For example, the values 0 to 6 correspond to the days of the week in sequence from Sunday to Saturday.
- Monthly: You can enter two values in A-B format. Valid values of A and B: 1 to 31. The value of B must be greater than or equal to the value of A.
- Cron: You can enter a cron expression which is written in UTC and consists of five fields: minute, hour, day of month (date), month, and day of week. The expression can contain wildcard characters including commas (,), question marks (?), hyphens (-), asterisks (*), number signs (#), forward slashes (/), and the L and W letters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scheduled<wbr>Action</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The operation to be performed when a scheduled task is triggered. Enter the unique identifier of a scaling rule.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scheduled<wbr>Task<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Display name of the scheduled task, which must be 2-40 characters (English or Chinese) long.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>task<wbr>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Specifies whether to start the scheduled task. Default to true.
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
    <dd>{{% md %}}Description of the scheduled task, which is 2-200 characters (English or Chinese) long.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>launch_<wbr>expiration_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The time period during which a failed scheduled task is retried. Unit: seconds. Valid values: 0 to 21600. Default value: 600
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>launch_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The time at which the scheduled task is triggered. Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format. 
The time must be in UTC. You cannot enter a time point later than 90 days from the date of scheduled task creation.
If the `recurrence_type` parameter is specified, the task is executed repeatedly at the time specified by LaunchTime.
Otherwise, the task is only executed once at the date and time specified by LaunchTime.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>recurrence_<wbr>end_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the end time after which the scheduled task is no longer repeated. 
Specify the time in the ISO 8601 standard in the YYYY-MM-DDThh:mm:ssZ format.
The time must be in UTC. You cannot enter a time point later than 365 days from the date of scheduled task creation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>recurrence_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the recurrence type of the scheduled task. 
If set, both `recurrence_value` and `recurrence_end_time` must be set. Valid values:
- Daily: The scheduled task is executed once every specified number of days.
- Weekly: The scheduled task is executed on each specified day of a week.
- Monthly: The scheduled task is executed on each specified day of a month.
- Cron: (Available in 1.60.0+) The scheduled task is executed based on the specified cron expression.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>recurrence_<wbr>value</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies how often a scheduled task recurs. The valid value depends on `recurrence_type`
- Daily: You can enter one value. Valid values: 1 to 31.
- Weekly: You can enter multiple values and separate them with commas (,). For example, the values 0 to 6 correspond to the days of the week in sequence from Sunday to Saturday.
- Monthly: You can enter two values in A-B format. Valid values of A and B: 1 to 31. The value of B must be greater than or equal to the value of A.
- Cron: You can enter a cron expression which is written in UTC and consists of five fields: minute, hour, day of month (date), month, and day of week. The expression can contain wildcard characters including commas (,), question marks (?), hyphens (-), asterisks (*), number signs (#), forward slashes (/), and the L and W letters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scheduled_<wbr>action</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The operation to be performed when a scheduled task is triggered. Enter the unique identifier of a scaling rule.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scheduled_<wbr>task_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Display name of the scheduled task, which must be 2-40 characters (English or Chinese) long.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>task_<wbr>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specifies whether to start the scheduled task. Default to true.
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

