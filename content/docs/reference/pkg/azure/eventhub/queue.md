
---
title: "Queue"
block_external_search_index: true
---



Manages a ServiceBus Queue.

> This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/servicebus_queue.html.markdown.



## Create a Queue Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/eventhub/#Queue">Queue</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/eventhub/#QueueArgs">QueueArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Queue</span><span class="p">(resource_name, opts=None, </span>auto_delete_on_idle=None<span class="p">, </span>dead_lettering_on_message_expiration=None<span class="p">, </span>default_message_ttl=None<span class="p">, </span>duplicate_detection_history_time_window=None<span class="p">, </span>enable_express=None<span class="p">, </span>enable_partitioning=None<span class="p">, </span>lock_duration=None<span class="p">, </span>max_delivery_count=None<span class="p">, </span>max_size_in_megabytes=None<span class="p">, </span>name=None<span class="p">, </span>namespace_name=None<span class="p">, </span>requires_duplicate_detection=None<span class="p">, </span>requires_session=None<span class="p">, </span>resource_group_name=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewQueue<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/eventhub?tab=doc#QueueArgs">QueueArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/eventhub?tab=doc#Queue">Queue</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Eventhub.Queue.html">Queue</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.EventHub.QueueArgs.html">QueueArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Auto<wbr>Delete<wbr>On<wbr>Idle</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration of the idle interval after which the
Queue is automatically deleted, minimum of 5 minutes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dead<wbr>Lettering<wbr>On<wbr>Message<wbr>Expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether the Queue has dead letter support when a message expires. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Message<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration of the TTL of messages sent to this
queue. This is the default value used when TTL is not set on message itself.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Duplicate<wbr>Detection<wbr>History<wbr>Time<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration during which
duplicates can be detected. Default value is 10 minutes. (`PT10M`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Express</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether Express Entities
are enabled. An express queue holds a message in memory temporarily before writing
it to persistent storage. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Partitioning</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether to enable
the queue to be partitioned across multiple message brokers. Changing this forces
a new resource to be created. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lock<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. Maximum value is 5 minutes. Defaults to 1 minute. (`PT1M`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Delivery<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Integer value which controls when a message is automatically deadlettered. Defaults to `10`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Size<wbr>In<wbr>Megabytes</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Integer value which controls the size of
memory allocated for the queue. For supported values see the "Queue/topic size"
section of [this document](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the ServiceBus Queue resource. Changing this forces a
new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Namespace<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the ServiceBus Namespace to create
this queue in. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Requires<wbr>Duplicate<wbr>Detection</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether
the Queue requires duplicate detection. Changing this forces
a new resource to be created. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Requires<wbr>Session</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether the Queue requires sessions.
This will allow ordered handling of unbounded sequences of related messages. With sessions enabled
a queue can guarantee first-in-first-out delivery of messages.
Changing this forces a new resource to be created. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Delete<wbr>On<wbr>Idle</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration of the idle interval after which the
Queue is automatically deleted, minimum of 5 minutes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dead<wbr>Lettering<wbr>On<wbr>Message<wbr>Expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether the Queue has dead letter support when a message expires. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Message<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration of the TTL of messages sent to this
queue. This is the default value used when TTL is not set on message itself.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Duplicate<wbr>Detection<wbr>History<wbr>Time<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration during which
duplicates can be detected. Default value is 10 minutes. (`PT10M`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Express</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether Express Entities
are enabled. An express queue holds a message in memory temporarily before writing
it to persistent storage. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Partitioning</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether to enable
the queue to be partitioned across multiple message brokers. Changing this forces
a new resource to be created. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lock<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. Maximum value is 5 minutes. Defaults to 1 minute. (`PT1M`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Delivery<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Integer value which controls when a message is automatically deadlettered. Defaults to `10`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Size<wbr>In<wbr>Megabytes</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Integer value which controls the size of
memory allocated for the queue. For supported values see the "Queue/topic size"
section of [this document](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the ServiceBus Queue resource. Changing this forces a
new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Namespace<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the ServiceBus Namespace to create
this queue in. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Requires<wbr>Duplicate<wbr>Detection</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether
the Queue requires duplicate detection. Changing this forces
a new resource to be created. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Requires<wbr>Session</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether the Queue requires sessions.
This will allow ordered handling of unbounded sequences of related messages. With sessions enabled
a queue can guarantee first-in-first-out delivery of messages.
Changing this forces a new resource to be created. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>auto<wbr>Delete<wbr>On<wbr>Idle</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration of the idle interval after which the
Queue is automatically deleted, minimum of 5 minutes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dead<wbr>Lettering<wbr>On<wbr>Message<wbr>Expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether the Queue has dead letter support when a message expires. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Message<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration of the TTL of messages sent to this
queue. This is the default value used when TTL is not set on message itself.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>duplicate<wbr>Detection<wbr>History<wbr>Time<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration during which
duplicates can be detected. Default value is 10 minutes. (`PT10M`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Express</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether Express Entities
are enabled. An express queue holds a message in memory temporarily before writing
it to persistent storage. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Partitioning</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether to enable
the queue to be partitioned across multiple message brokers. Changing this forces
a new resource to be created. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lock<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. Maximum value is 5 minutes. Defaults to 1 minute. (`PT1M`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Delivery<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Integer value which controls when a message is automatically deadlettered. Defaults to `10`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Size<wbr>In<wbr>Megabytes</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Integer value which controls the size of
memory allocated for the queue. For supported values see the "Queue/topic size"
section of [this document](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the ServiceBus Queue resource. Changing this forces a
new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>namespace<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the ServiceBus Namespace to create
this queue in. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>requires<wbr>Duplicate<wbr>Detection</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether
the Queue requires duplicate detection. Changing this forces
a new resource to be created. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>requires<wbr>Session</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether the Queue requires sessions.
This will allow ordered handling of unbounded sequences of related messages. With sessions enabled
a queue can guarantee first-in-first-out delivery of messages.
Changing this forces a new resource to be created. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>auto_<wbr>delete_<wbr>on_<wbr>idle</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration of the idle interval after which the
Queue is automatically deleted, minimum of 5 minutes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dead_<wbr>lettering_<wbr>on_<wbr>message_<wbr>expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether the Queue has dead letter support when a message expires. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default_<wbr>message_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration of the TTL of messages sent to this
queue. This is the default value used when TTL is not set on message itself.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>duplicate_<wbr>detection_<wbr>history_<wbr>time_<wbr>window</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration during which
duplicates can be detected. Default value is 10 minutes. (`PT10M`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>express</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether Express Entities
are enabled. An express queue holds a message in memory temporarily before writing
it to persistent storage. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>partitioning</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether to enable
the queue to be partitioned across multiple message brokers. Changing this forces
a new resource to be created. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lock_<wbr>duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. Maximum value is 5 minutes. Defaults to 1 minute. (`PT1M`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max_<wbr>delivery_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Integer value which controls when a message is automatically deadlettered. Defaults to `10`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max_<wbr>size_<wbr>in_<wbr>megabytes</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Integer value which controls the size of
memory allocated for the queue. For supported values see the "Queue/topic size"
section of [this document](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the ServiceBus Queue resource. Changing this forces a
new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>namespace_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the ServiceBus Namespace to create
this queue in. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>requires_<wbr>duplicate_<wbr>detection</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether
the Queue requires duplicate detection. Changing this forces
a new resource to be created. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>requires_<wbr>session</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether the Queue requires sessions.
This will allow ordered handling of unbounded sequences of related messages. With sessions enabled
a queue can guarantee first-in-first-out delivery of messages.
Changing this forces a new resource to be created. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Queue Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Auto<wbr>Delete<wbr>On<wbr>Idle</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration of the idle interval after which the
Queue is automatically deleted, minimum of 5 minutes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Dead<wbr>Lettering<wbr>On<wbr>Message<wbr>Expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether the Queue has dead letter support when a message expires. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Default<wbr>Message<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration of the TTL of messages sent to this
queue. This is the default value used when TTL is not set on message itself.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Duplicate<wbr>Detection<wbr>History<wbr>Time<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration during which
duplicates can be detected. Default value is 10 minutes. (`PT10M`)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Express</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether Express Entities
are enabled. An express queue holds a message in memory temporarily before writing
it to persistent storage. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Partitioning</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether to enable
the queue to be partitioned across multiple message brokers. Changing this forces
a new resource to be created. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `true`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Lock<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. Maximum value is 5 minutes. Defaults to 1 minute. (`PT1M`)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Max<wbr>Delivery<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Integer value which controls when a message is automatically deadlettered. Defaults to `10`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Max<wbr>Size<wbr>In<wbr>Megabytes</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Integer value which controls the size of
memory allocated for the queue. For supported values see the "Queue/topic size"
section of [this document](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the ServiceBus Queue resource. Changing this forces a
new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Namespace<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the ServiceBus Namespace to create
this queue in. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Requires<wbr>Duplicate<wbr>Detection</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether
the Queue requires duplicate detection. Changing this forces
a new resource to be created. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Requires<wbr>Session</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether the Queue requires sessions.
This will allow ordered handling of unbounded sequences of related messages. With sessions enabled
a queue can guarantee first-in-first-out delivery of messages.
Changing this forces a new resource to be created. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Auto<wbr>Delete<wbr>On<wbr>Idle</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration of the idle interval after which the
Queue is automatically deleted, minimum of 5 minutes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Dead<wbr>Lettering<wbr>On<wbr>Message<wbr>Expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether the Queue has dead letter support when a message expires. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Default<wbr>Message<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration of the TTL of messages sent to this
queue. This is the default value used when TTL is not set on message itself.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Duplicate<wbr>Detection<wbr>History<wbr>Time<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration during which
duplicates can be detected. Default value is 10 minutes. (`PT10M`)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Express</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether Express Entities
are enabled. An express queue holds a message in memory temporarily before writing
it to persistent storage. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enable<wbr>Partitioning</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether to enable
the queue to be partitioned across multiple message brokers. Changing this forces
a new resource to be created. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `true`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Lock<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. Maximum value is 5 minutes. Defaults to 1 minute. (`PT1M`)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Max<wbr>Delivery<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Integer value which controls when a message is automatically deadlettered. Defaults to `10`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Max<wbr>Size<wbr>In<wbr>Megabytes</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Integer value which controls the size of
memory allocated for the queue. For supported values see the "Queue/topic size"
section of [this document](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the ServiceBus Queue resource. Changing this forces a
new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Namespace<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the ServiceBus Namespace to create
this queue in. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Requires<wbr>Duplicate<wbr>Detection</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether
the Queue requires duplicate detection. Changing this forces
a new resource to be created. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Requires<wbr>Session</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether the Queue requires sessions.
This will allow ordered handling of unbounded sequences of related messages. With sessions enabled
a queue can guarantee first-in-first-out delivery of messages.
Changing this forces a new resource to be created. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>auto<wbr>Delete<wbr>On<wbr>Idle</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration of the idle interval after which the
Queue is automatically deleted, minimum of 5 minutes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>dead<wbr>Lettering<wbr>On<wbr>Message<wbr>Expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether the Queue has dead letter support when a message expires. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>default<wbr>Message<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration of the TTL of messages sent to this
queue. This is the default value used when TTL is not set on message itself.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>duplicate<wbr>Detection<wbr>History<wbr>Time<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration during which
duplicates can be detected. Default value is 10 minutes. (`PT10M`)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable<wbr>Express</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether Express Entities
are enabled. An express queue holds a message in memory temporarily before writing
it to persistent storage. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable<wbr>Partitioning</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether to enable
the queue to be partitioned across multiple message brokers. Changing this forces
a new resource to be created. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `true`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>lock<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. Maximum value is 5 minutes. Defaults to 1 minute. (`PT1M`)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>max<wbr>Delivery<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Integer value which controls when a message is automatically deadlettered. Defaults to `10`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>max<wbr>Size<wbr>In<wbr>Megabytes</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Integer value which controls the size of
memory allocated for the queue. For supported values see the "Queue/topic size"
section of [this document](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the ServiceBus Queue resource. Changing this forces a
new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>namespace<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the ServiceBus Namespace to create
this queue in. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>requires<wbr>Duplicate<wbr>Detection</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether
the Queue requires duplicate detection. Changing this forces
a new resource to be created. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>requires<wbr>Session</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether the Queue requires sessions.
This will allow ordered handling of unbounded sequences of related messages. With sessions enabled
a queue can guarantee first-in-first-out delivery of messages.
Changing this forces a new resource to be created. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>auto_<wbr>delete_<wbr>on_<wbr>idle</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration of the idle interval after which the
Queue is automatically deleted, minimum of 5 minutes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>dead_<wbr>lettering_<wbr>on_<wbr>message_<wbr>expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether the Queue has dead letter support when a message expires. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>default_<wbr>message_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration of the TTL of messages sent to this
queue. This is the default value used when TTL is not set on message itself.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>duplicate_<wbr>detection_<wbr>history_<wbr>time_<wbr>window</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration during which
duplicates can be detected. Default value is 10 minutes. (`PT10M`)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable_<wbr>express</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether Express Entities
are enabled. An express queue holds a message in memory temporarily before writing
it to persistent storage. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enable_<wbr>partitioning</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether to enable
the queue to be partitioned across multiple message brokers. Changing this forces
a new resource to be created. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `true`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>lock_<wbr>duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. Maximum value is 5 minutes. Defaults to 1 minute. (`PT1M`)
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>max_<wbr>delivery_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Integer value which controls when a message is automatically deadlettered. Defaults to `10`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>max_<wbr>size_<wbr>in_<wbr>megabytes</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Integer value which controls the size of
memory allocated for the queue. For supported values see the "Queue/topic size"
section of [this document](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas).
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the ServiceBus Queue resource. Changing this forces a
new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>namespace_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the ServiceBus Namespace to create
this queue in. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>requires_<wbr>duplicate_<wbr>detection</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether
the Queue requires duplicate detection. Changing this forces
a new resource to be created. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>requires_<wbr>session</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether the Queue requires sessions.
This will allow ordered handling of unbounded sequences of related messages. With sessions enabled
a queue can guarantee first-in-first-out delivery of messages.
Changing this forces a new resource to be created. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Queue Resource

Get an existing Queue resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/eventhub/#QueueState">QueueState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/eventhub/#Queue">Queue</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>auto_delete_on_idle=None<span class="p">, </span>dead_lettering_on_message_expiration=None<span class="p">, </span>default_message_ttl=None<span class="p">, </span>duplicate_detection_history_time_window=None<span class="p">, </span>enable_express=None<span class="p">, </span>enable_partitioning=None<span class="p">, </span>lock_duration=None<span class="p">, </span>max_delivery_count=None<span class="p">, </span>max_size_in_megabytes=None<span class="p">, </span>name=None<span class="p">, </span>namespace_name=None<span class="p">, </span>requires_duplicate_detection=None<span class="p">, </span>requires_session=None<span class="p">, </span>resource_group_name=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetQueue<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/eventhub?tab=doc#QueueState">QueueState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/eventhub?tab=doc#Queue">Queue</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Eventhub.Queue.html">Queue</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Eventhub.QueueState.html">QueueState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Auto<wbr>Delete<wbr>On<wbr>Idle</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration of the idle interval after which the
Queue is automatically deleted, minimum of 5 minutes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dead<wbr>Lettering<wbr>On<wbr>Message<wbr>Expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether the Queue has dead letter support when a message expires. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Message<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration of the TTL of messages sent to this
queue. This is the default value used when TTL is not set on message itself.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Duplicate<wbr>Detection<wbr>History<wbr>Time<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration during which
duplicates can be detected. Default value is 10 minutes. (`PT10M`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Express</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether Express Entities
are enabled. An express queue holds a message in memory temporarily before writing
it to persistent storage. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Partitioning</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether to enable
the queue to be partitioned across multiple message brokers. Changing this forces
a new resource to be created. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lock<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. Maximum value is 5 minutes. Defaults to 1 minute. (`PT1M`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Delivery<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Integer value which controls when a message is automatically deadlettered. Defaults to `10`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Size<wbr>In<wbr>Megabytes</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Integer value which controls the size of
memory allocated for the queue. For supported values see the "Queue/topic size"
section of [this document](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the ServiceBus Queue resource. Changing this forces a
new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Namespace<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the ServiceBus Namespace to create
this queue in. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Requires<wbr>Duplicate<wbr>Detection</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether
the Queue requires duplicate detection. Changing this forces
a new resource to be created. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Requires<wbr>Session</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether the Queue requires sessions.
This will allow ordered handling of unbounded sequences of related messages. With sessions enabled
a queue can guarantee first-in-first-out delivery of messages.
Changing this forces a new resource to be created. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Auto<wbr>Delete<wbr>On<wbr>Idle</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration of the idle interval after which the
Queue is automatically deleted, minimum of 5 minutes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dead<wbr>Lettering<wbr>On<wbr>Message<wbr>Expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether the Queue has dead letter support when a message expires. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Message<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration of the TTL of messages sent to this
queue. This is the default value used when TTL is not set on message itself.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Duplicate<wbr>Detection<wbr>History<wbr>Time<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration during which
duplicates can be detected. Default value is 10 minutes. (`PT10M`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Express</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether Express Entities
are enabled. An express queue holds a message in memory temporarily before writing
it to persistent storage. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enable<wbr>Partitioning</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether to enable
the queue to be partitioned across multiple message brokers. Changing this forces
a new resource to be created. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lock<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. Maximum value is 5 minutes. Defaults to 1 minute. (`PT1M`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Delivery<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Integer value which controls when a message is automatically deadlettered. Defaults to `10`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Size<wbr>In<wbr>Megabytes</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Integer value which controls the size of
memory allocated for the queue. For supported values see the "Queue/topic size"
section of [this document](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the ServiceBus Queue resource. Changing this forces a
new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Namespace<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the ServiceBus Namespace to create
this queue in. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Requires<wbr>Duplicate<wbr>Detection</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether
the Queue requires duplicate detection. Changing this forces
a new resource to be created. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Requires<wbr>Session</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether the Queue requires sessions.
This will allow ordered handling of unbounded sequences of related messages. With sessions enabled
a queue can guarantee first-in-first-out delivery of messages.
Changing this forces a new resource to be created. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>auto<wbr>Delete<wbr>On<wbr>Idle</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration of the idle interval after which the
Queue is automatically deleted, minimum of 5 minutes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dead<wbr>Lettering<wbr>On<wbr>Message<wbr>Expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether the Queue has dead letter support when a message expires. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Message<wbr>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration of the TTL of messages sent to this
queue. This is the default value used when TTL is not set on message itself.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>duplicate<wbr>Detection<wbr>History<wbr>Time<wbr>Window</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration during which
duplicates can be detected. Default value is 10 minutes. (`PT10M`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Express</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether Express Entities
are enabled. An express queue holds a message in memory temporarily before writing
it to persistent storage. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable<wbr>Partitioning</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether to enable
the queue to be partitioned across multiple message brokers. Changing this forces
a new resource to be created. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lock<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. Maximum value is 5 minutes. Defaults to 1 minute. (`PT1M`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Delivery<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Integer value which controls when a message is automatically deadlettered. Defaults to `10`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Size<wbr>In<wbr>Megabytes</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Integer value which controls the size of
memory allocated for the queue. For supported values see the "Queue/topic size"
section of [this document](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the ServiceBus Queue resource. Changing this forces a
new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>namespace<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the ServiceBus Namespace to create
this queue in. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>requires<wbr>Duplicate<wbr>Detection</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether
the Queue requires duplicate detection. Changing this forces
a new resource to be created. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>requires<wbr>Session</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether the Queue requires sessions.
This will allow ordered handling of unbounded sequences of related messages. With sessions enabled
a queue can guarantee first-in-first-out delivery of messages.
Changing this forces a new resource to be created. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource<wbr>Group<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>auto_<wbr>delete_<wbr>on_<wbr>idle</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration of the idle interval after which the
Queue is automatically deleted, minimum of 5 minutes.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dead_<wbr>lettering_<wbr>on_<wbr>message_<wbr>expiration</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether the Queue has dead letter support when a message expires. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default_<wbr>message_<wbr>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration of the TTL of messages sent to this
queue. This is the default value used when TTL is not set on message itself.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>duplicate_<wbr>detection_<wbr>history_<wbr>time_<wbr>window</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration during which
duplicates can be detected. Default value is 10 minutes. (`PT10M`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>express</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether Express Entities
are enabled. An express queue holds a message in memory temporarily before writing
it to persistent storage. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enable_<wbr>partitioning</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether to enable
the queue to be partitioned across multiple message brokers. Changing this forces
a new resource to be created. Defaults to `false` for Basic and Standard. For Premium, it MUST
be set to `true`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lock_<wbr>duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ISO 8601 timespan duration of a peek-lock; that is, the amount of time that the message is locked for other receivers. Maximum value is 5 minutes. Defaults to 1 minute. (`PT1M`)
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max_<wbr>delivery_<wbr>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Integer value which controls when a message is automatically deadlettered. Defaults to `10`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max_<wbr>size_<wbr>in_<wbr>megabytes</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Integer value which controls the size of
memory allocated for the queue. For supported values see the "Queue/topic size"
section of [this document](https://docs.microsoft.com/en-us/azure/service-bus-messaging/service-bus-quotas).
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the ServiceBus Queue resource. Changing this forces a
new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>namespace_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the ServiceBus Namespace to create
this queue in. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>requires_<wbr>duplicate_<wbr>detection</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether
the Queue requires duplicate detection. Changing this forces
a new resource to be created. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>requires_<wbr>session</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Boolean flag which controls whether the Queue requires sessions.
This will allow ordered handling of unbounded sequences of related messages. With sessions enabled
a queue can guarantee first-in-first-out delivery of messages.
Changing this forces a new resource to be created. Defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>resource_<wbr>group_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}











<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-azure">https://github.com/pulumi/pulumi-azure</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

