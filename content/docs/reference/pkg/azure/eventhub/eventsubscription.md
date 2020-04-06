
---
title: "EventSubscription"
block_external_search_index: true
---



Manages an EventGrid Event Subscription

> This content is derived from https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/eventgrid_event_subscription.html.markdown.



## Create a EventSubscription Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/eventhub/#EventSubscription">EventSubscription</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/eventhub/#EventSubscriptionArgs">EventSubscriptionArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">EventSubscription</span><span class="p">(resource_name, opts=None, </span>event_delivery_schema=None<span class="p">, </span>eventhub_endpoint=None<span class="p">, </span>hybrid_connection_endpoint=None<span class="p">, </span>included_event_types=None<span class="p">, </span>labels=None<span class="p">, </span>name=None<span class="p">, </span>retry_policy=None<span class="p">, </span>scope=None<span class="p">, </span>storage_blob_dead_letter_destination=None<span class="p">, </span>storage_queue_endpoint=None<span class="p">, </span>subject_filter=None<span class="p">, </span>topic_name=None<span class="p">, </span>webhook_endpoint=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewEventSubscription<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/eventhub?tab=doc#EventSubscriptionArgs">EventSubscriptionArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/eventhub?tab=doc#EventSubscription">EventSubscription</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Eventhub.EventSubscription.html">EventSubscription</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.EventHub.EventSubscriptionArgs.html">EventSubscriptionArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Event<wbr>Delivery<wbr>Schema</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the event delivery schema for the event subscription. Possible values include: `EventGridSchema`, `CloudEventV01Schema`, `CustomInputSchema`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Eventhub<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptioneventhubendpoint">Event<wbr>Subscription<wbr>Eventhub<wbr>Endpoint<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `eventhub_endpoint` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hybrid<wbr>Connection<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionhybridconnectionendpoint">Event<wbr>Subscription<wbr>Hybrid<wbr>Connection<wbr>Endpoint<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `hybrid_connection_endpoint` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Included<wbr>Event<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of applicable event types that need to be part of the event subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of labels to assign to the event subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the EventGrid Event Subscription resource. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retry<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionretrypolicy">Event<wbr>Subscription<wbr>Retry<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `retry_policy` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Scope</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the scope at which the EventGrid Event Subscription should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Blob<wbr>Dead<wbr>Letter<wbr>Destination</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionstorageblobdeadletterdestination">Event<wbr>Subscription<wbr>Storage<wbr>Blob<wbr>Dead<wbr>Letter<wbr>Destination<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `storage_blob_dead_letter_destination` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Queue<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionstoragequeueendpoint">Event<wbr>Subscription<wbr>Storage<wbr>Queue<wbr>Endpoint<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `storage_queue_endpoint` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subject<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionsubjectfilter">Event<wbr>Subscription<wbr>Subject<wbr>Filter<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `subject_filter` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Topic<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the topic to associate with the event subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Webhook<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionwebhookendpoint">Event<wbr>Subscription<wbr>Webhook<wbr>Endpoint<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `webhook_endpoint` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Event<wbr>Delivery<wbr>Schema</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the event delivery schema for the event subscription. Possible values include: `EventGridSchema`, `CloudEventV01Schema`, `CustomInputSchema`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Eventhub<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptioneventhubendpoint">*Event<wbr>Subscription<wbr>Eventhub<wbr>Endpoint</a></span>
    </dt>
    <dd>{{% md %}}A `eventhub_endpoint` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hybrid<wbr>Connection<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionhybridconnectionendpoint">*Event<wbr>Subscription<wbr>Hybrid<wbr>Connection<wbr>Endpoint</a></span>
    </dt>
    <dd>{{% md %}}A `hybrid_connection_endpoint` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Included<wbr>Event<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of applicable event types that need to be part of the event subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of labels to assign to the event subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the EventGrid Event Subscription resource. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retry<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionretrypolicy">*Event<wbr>Subscription<wbr>Retry<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A `retry_policy` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Scope</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the scope at which the EventGrid Event Subscription should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Blob<wbr>Dead<wbr>Letter<wbr>Destination</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionstorageblobdeadletterdestination">*Event<wbr>Subscription<wbr>Storage<wbr>Blob<wbr>Dead<wbr>Letter<wbr>Destination</a></span>
    </dt>
    <dd>{{% md %}}A `storage_blob_dead_letter_destination` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Queue<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionstoragequeueendpoint">*Event<wbr>Subscription<wbr>Storage<wbr>Queue<wbr>Endpoint</a></span>
    </dt>
    <dd>{{% md %}}A `storage_queue_endpoint` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subject<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionsubjectfilter">*Event<wbr>Subscription<wbr>Subject<wbr>Filter</a></span>
    </dt>
    <dd>{{% md %}}A `subject_filter` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Topic<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the topic to associate with the event subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Webhook<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionwebhookendpoint">*Event<wbr>Subscription<wbr>Webhook<wbr>Endpoint</a></span>
    </dt>
    <dd>{{% md %}}A `webhook_endpoint` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>event<wbr>Delivery<wbr>Schema</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the event delivery schema for the event subscription. Possible values include: `EventGridSchema`, `CloudEventV01Schema`, `CustomInputSchema`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>eventhub<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptioneventhubendpoint">Event<wbr>Subscription<wbr>Eventhub<wbr>Endpoint?</a></span>
    </dt>
    <dd>{{% md %}}A `eventhub_endpoint` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hybrid<wbr>Connection<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionhybridconnectionendpoint">Event<wbr>Subscription<wbr>Hybrid<wbr>Connection<wbr>Endpoint?</a></span>
    </dt>
    <dd>{{% md %}}A `hybrid_connection_endpoint` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>included<wbr>Event<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of applicable event types that need to be part of the event subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of labels to assign to the event subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the EventGrid Event Subscription resource. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retry<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionretrypolicy">Event<wbr>Subscription<wbr>Retry<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}A `retry_policy` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>scope</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the scope at which the EventGrid Event Subscription should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage<wbr>Blob<wbr>Dead<wbr>Letter<wbr>Destination</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionstorageblobdeadletterdestination">Event<wbr>Subscription<wbr>Storage<wbr>Blob<wbr>Dead<wbr>Letter<wbr>Destination?</a></span>
    </dt>
    <dd>{{% md %}}A `storage_blob_dead_letter_destination` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage<wbr>Queue<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionstoragequeueendpoint">Event<wbr>Subscription<wbr>Storage<wbr>Queue<wbr>Endpoint?</a></span>
    </dt>
    <dd>{{% md %}}A `storage_queue_endpoint` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subject<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionsubjectfilter">Event<wbr>Subscription<wbr>Subject<wbr>Filter?</a></span>
    </dt>
    <dd>{{% md %}}A `subject_filter` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>topic<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the topic to associate with the event subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>webhook<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionwebhookendpoint">Event<wbr>Subscription<wbr>Webhook<wbr>Endpoint?</a></span>
    </dt>
    <dd>{{% md %}}A `webhook_endpoint` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>event_<wbr>delivery_<wbr>schema</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the event delivery schema for the event subscription. Possible values include: `EventGridSchema`, `CloudEventV01Schema`, `CustomInputSchema`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>eventhub_<wbr>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptioneventhubendpoint">Dict[Event<wbr>Subscription<wbr>Eventhub<wbr>Endpoint]</a></span>
    </dt>
    <dd>{{% md %}}A `eventhub_endpoint` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hybrid_<wbr>connection_<wbr>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionhybridconnectionendpoint">Dict[Event<wbr>Subscription<wbr>Hybrid<wbr>Connection<wbr>Endpoint]</a></span>
    </dt>
    <dd>{{% md %}}A `hybrid_connection_endpoint` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>included_<wbr>event_<wbr>types</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of applicable event types that need to be part of the event subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of labels to assign to the event subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the EventGrid Event Subscription resource. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retry_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionretrypolicy">Dict[Event<wbr>Subscription<wbr>Retry<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A `retry_policy` block as defined below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>scope</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the scope at which the EventGrid Event Subscription should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage_<wbr>blob_<wbr>dead_<wbr>letter_<wbr>destination</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionstorageblobdeadletterdestination">Dict[Event<wbr>Subscription<wbr>Storage<wbr>Blob<wbr>Dead<wbr>Letter<wbr>Destination]</a></span>
    </dt>
    <dd>{{% md %}}A `storage_blob_dead_letter_destination` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage_<wbr>queue_<wbr>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionstoragequeueendpoint">Dict[Event<wbr>Subscription<wbr>Storage<wbr>Queue<wbr>Endpoint]</a></span>
    </dt>
    <dd>{{% md %}}A `storage_queue_endpoint` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subject_<wbr>filter</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionsubjectfilter">Dict[Event<wbr>Subscription<wbr>Subject<wbr>Filter]</a></span>
    </dt>
    <dd>{{% md %}}A `subject_filter` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>topic_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the topic to associate with the event subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>webhook_<wbr>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionwebhookendpoint">Dict[Event<wbr>Subscription<wbr>Webhook<wbr>Endpoint]</a></span>
    </dt>
    <dd>{{% md %}}A `webhook_endpoint` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## EventSubscription Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Event<wbr>Delivery<wbr>Schema</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the event delivery schema for the event subscription. Possible values include: `EventGridSchema`, `CloudEventV01Schema`, `CustomInputSchema`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Eventhub<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptioneventhubendpoint">Event<wbr>Subscription<wbr>Eventhub<wbr>Endpoint?</a></span>
    </dt>
    <dd>{{% md %}}A `eventhub_endpoint` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Hybrid<wbr>Connection<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionhybridconnectionendpoint">Event<wbr>Subscription<wbr>Hybrid<wbr>Connection<wbr>Endpoint?</a></span>
    </dt>
    <dd>{{% md %}}A `hybrid_connection_endpoint` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Included<wbr>Event<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}A list of applicable event types that need to be part of the event subscription.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of labels to assign to the event subscription.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the EventGrid Event Subscription resource. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Retry<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionretrypolicy">Event<wbr>Subscription<wbr>Retry<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A `retry_policy` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Scope</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the scope at which the EventGrid Event Subscription should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Storage<wbr>Blob<wbr>Dead<wbr>Letter<wbr>Destination</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionstorageblobdeadletterdestination">Event<wbr>Subscription<wbr>Storage<wbr>Blob<wbr>Dead<wbr>Letter<wbr>Destination?</a></span>
    </dt>
    <dd>{{% md %}}A `storage_blob_dead_letter_destination` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Storage<wbr>Queue<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionstoragequeueendpoint">Event<wbr>Subscription<wbr>Storage<wbr>Queue<wbr>Endpoint?</a></span>
    </dt>
    <dd>{{% md %}}A `storage_queue_endpoint` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Subject<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionsubjectfilter">Event<wbr>Subscription<wbr>Subject<wbr>Filter?</a></span>
    </dt>
    <dd>{{% md %}}A `subject_filter` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Topic<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the topic to associate with the event subscription.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Webhook<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionwebhookendpoint">Event<wbr>Subscription<wbr>Webhook<wbr>Endpoint?</a></span>
    </dt>
    <dd>{{% md %}}A `webhook_endpoint` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Event<wbr>Delivery<wbr>Schema</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the event delivery schema for the event subscription. Possible values include: `EventGridSchema`, `CloudEventV01Schema`, `CustomInputSchema`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Eventhub<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptioneventhubendpoint">*Event<wbr>Subscription<wbr>Eventhub<wbr>Endpoint</a></span>
    </dt>
    <dd>{{% md %}}A `eventhub_endpoint` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Hybrid<wbr>Connection<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionhybridconnectionendpoint">*Event<wbr>Subscription<wbr>Hybrid<wbr>Connection<wbr>Endpoint</a></span>
    </dt>
    <dd>{{% md %}}A `hybrid_connection_endpoint` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Included<wbr>Event<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of applicable event types that need to be part of the event subscription.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of labels to assign to the event subscription.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the EventGrid Event Subscription resource. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Retry<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionretrypolicy">Event<wbr>Subscription<wbr>Retry<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A `retry_policy` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Scope</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the scope at which the EventGrid Event Subscription should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Storage<wbr>Blob<wbr>Dead<wbr>Letter<wbr>Destination</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionstorageblobdeadletterdestination">*Event<wbr>Subscription<wbr>Storage<wbr>Blob<wbr>Dead<wbr>Letter<wbr>Destination</a></span>
    </dt>
    <dd>{{% md %}}A `storage_blob_dead_letter_destination` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Storage<wbr>Queue<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionstoragequeueendpoint">*Event<wbr>Subscription<wbr>Storage<wbr>Queue<wbr>Endpoint</a></span>
    </dt>
    <dd>{{% md %}}A `storage_queue_endpoint` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Subject<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionsubjectfilter">*Event<wbr>Subscription<wbr>Subject<wbr>Filter</a></span>
    </dt>
    <dd>{{% md %}}A `subject_filter` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Topic<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the topic to associate with the event subscription.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Webhook<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionwebhookendpoint">*Event<wbr>Subscription<wbr>Webhook<wbr>Endpoint</a></span>
    </dt>
    <dd>{{% md %}}A `webhook_endpoint` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>event<wbr>Delivery<wbr>Schema</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the event delivery schema for the event subscription. Possible values include: `EventGridSchema`, `CloudEventV01Schema`, `CustomInputSchema`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>eventhub<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptioneventhubendpoint">Event<wbr>Subscription<wbr>Eventhub<wbr>Endpoint?</a></span>
    </dt>
    <dd>{{% md %}}A `eventhub_endpoint` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>hybrid<wbr>Connection<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionhybridconnectionendpoint">Event<wbr>Subscription<wbr>Hybrid<wbr>Connection<wbr>Endpoint?</a></span>
    </dt>
    <dd>{{% md %}}A `hybrid_connection_endpoint` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>included<wbr>Event<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of applicable event types that need to be part of the event subscription.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of labels to assign to the event subscription.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the EventGrid Event Subscription resource. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>retry<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionretrypolicy">Event<wbr>Subscription<wbr>Retry<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A `retry_policy` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>scope</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the scope at which the EventGrid Event Subscription should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>storage<wbr>Blob<wbr>Dead<wbr>Letter<wbr>Destination</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionstorageblobdeadletterdestination">Event<wbr>Subscription<wbr>Storage<wbr>Blob<wbr>Dead<wbr>Letter<wbr>Destination?</a></span>
    </dt>
    <dd>{{% md %}}A `storage_blob_dead_letter_destination` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>storage<wbr>Queue<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionstoragequeueendpoint">Event<wbr>Subscription<wbr>Storage<wbr>Queue<wbr>Endpoint?</a></span>
    </dt>
    <dd>{{% md %}}A `storage_queue_endpoint` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>subject<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionsubjectfilter">Event<wbr>Subscription<wbr>Subject<wbr>Filter?</a></span>
    </dt>
    <dd>{{% md %}}A `subject_filter` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>topic<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the topic to associate with the event subscription.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>webhook<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionwebhookendpoint">Event<wbr>Subscription<wbr>Webhook<wbr>Endpoint?</a></span>
    </dt>
    <dd>{{% md %}}A `webhook_endpoint` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>event_<wbr>delivery_<wbr>schema</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the event delivery schema for the event subscription. Possible values include: `EventGridSchema`, `CloudEventV01Schema`, `CustomInputSchema`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>eventhub_<wbr>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptioneventhubendpoint">Dict[Event<wbr>Subscription<wbr>Eventhub<wbr>Endpoint]</a></span>
    </dt>
    <dd>{{% md %}}A `eventhub_endpoint` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>hybrid_<wbr>connection_<wbr>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionhybridconnectionendpoint">Dict[Event<wbr>Subscription<wbr>Hybrid<wbr>Connection<wbr>Endpoint]</a></span>
    </dt>
    <dd>{{% md %}}A `hybrid_connection_endpoint` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>included_<wbr>event_<wbr>types</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of applicable event types that need to be part of the event subscription.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of labels to assign to the event subscription.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the EventGrid Event Subscription resource. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>retry_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionretrypolicy">Dict[Event<wbr>Subscription<wbr>Retry<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A `retry_policy` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>scope</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the scope at which the EventGrid Event Subscription should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>storage_<wbr>blob_<wbr>dead_<wbr>letter_<wbr>destination</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionstorageblobdeadletterdestination">Dict[Event<wbr>Subscription<wbr>Storage<wbr>Blob<wbr>Dead<wbr>Letter<wbr>Destination]</a></span>
    </dt>
    <dd>{{% md %}}A `storage_blob_dead_letter_destination` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>storage_<wbr>queue_<wbr>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionstoragequeueendpoint">Dict[Event<wbr>Subscription<wbr>Storage<wbr>Queue<wbr>Endpoint]</a></span>
    </dt>
    <dd>{{% md %}}A `storage_queue_endpoint` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>subject_<wbr>filter</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionsubjectfilter">Dict[Event<wbr>Subscription<wbr>Subject<wbr>Filter]</a></span>
    </dt>
    <dd>{{% md %}}A `subject_filter` block as defined below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>topic_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the topic to associate with the event subscription.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>webhook_<wbr>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionwebhookendpoint">Dict[Event<wbr>Subscription<wbr>Webhook<wbr>Endpoint]</a></span>
    </dt>
    <dd>{{% md %}}A `webhook_endpoint` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing EventSubscription Resource

Get an existing EventSubscription resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/eventhub/#EventSubscriptionState">EventSubscriptionState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/azure/eventhub/#EventSubscription">EventSubscription</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>event_delivery_schema=None<span class="p">, </span>eventhub_endpoint=None<span class="p">, </span>hybrid_connection_endpoint=None<span class="p">, </span>included_event_types=None<span class="p">, </span>labels=None<span class="p">, </span>name=None<span class="p">, </span>retry_policy=None<span class="p">, </span>scope=None<span class="p">, </span>storage_blob_dead_letter_destination=None<span class="p">, </span>storage_queue_endpoint=None<span class="p">, </span>subject_filter=None<span class="p">, </span>topic_name=None<span class="p">, </span>webhook_endpoint=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetEventSubscription<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/eventhub?tab=doc#EventSubscriptionState">EventSubscriptionState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/eventhub?tab=doc#EventSubscription">EventSubscription</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Eventhub.EventSubscription.html">EventSubscription</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Azure/Pulumi.Azure.Eventhub.EventSubscriptionState.html">EventSubscriptionState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Event<wbr>Delivery<wbr>Schema</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the event delivery schema for the event subscription. Possible values include: `EventGridSchema`, `CloudEventV01Schema`, `CustomInputSchema`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Eventhub<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptioneventhubendpoint">Event<wbr>Subscription<wbr>Eventhub<wbr>Endpoint<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `eventhub_endpoint` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hybrid<wbr>Connection<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionhybridconnectionendpoint">Event<wbr>Subscription<wbr>Hybrid<wbr>Connection<wbr>Endpoint<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `hybrid_connection_endpoint` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Included<wbr>Event<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of applicable event types that need to be part of the event subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of labels to assign to the event subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the EventGrid Event Subscription resource. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retry<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionretrypolicy">Event<wbr>Subscription<wbr>Retry<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `retry_policy` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scope</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the scope at which the EventGrid Event Subscription should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Blob<wbr>Dead<wbr>Letter<wbr>Destination</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionstorageblobdeadletterdestination">Event<wbr>Subscription<wbr>Storage<wbr>Blob<wbr>Dead<wbr>Letter<wbr>Destination<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `storage_blob_dead_letter_destination` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Queue<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionstoragequeueendpoint">Event<wbr>Subscription<wbr>Storage<wbr>Queue<wbr>Endpoint<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `storage_queue_endpoint` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subject<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionsubjectfilter">Event<wbr>Subscription<wbr>Subject<wbr>Filter<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `subject_filter` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Topic<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the topic to associate with the event subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Webhook<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionwebhookendpoint">Event<wbr>Subscription<wbr>Webhook<wbr>Endpoint<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A `webhook_endpoint` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Event<wbr>Delivery<wbr>Schema</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the event delivery schema for the event subscription. Possible values include: `EventGridSchema`, `CloudEventV01Schema`, `CustomInputSchema`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Eventhub<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptioneventhubendpoint">*Event<wbr>Subscription<wbr>Eventhub<wbr>Endpoint</a></span>
    </dt>
    <dd>{{% md %}}A `eventhub_endpoint` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Hybrid<wbr>Connection<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionhybridconnectionendpoint">*Event<wbr>Subscription<wbr>Hybrid<wbr>Connection<wbr>Endpoint</a></span>
    </dt>
    <dd>{{% md %}}A `hybrid_connection_endpoint` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Included<wbr>Event<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of applicable event types that need to be part of the event subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of labels to assign to the event subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the EventGrid Event Subscription resource. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retry<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionretrypolicy">*Event<wbr>Subscription<wbr>Retry<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A `retry_policy` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Scope</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the scope at which the EventGrid Event Subscription should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Blob<wbr>Dead<wbr>Letter<wbr>Destination</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionstorageblobdeadletterdestination">*Event<wbr>Subscription<wbr>Storage<wbr>Blob<wbr>Dead<wbr>Letter<wbr>Destination</a></span>
    </dt>
    <dd>{{% md %}}A `storage_blob_dead_letter_destination` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Storage<wbr>Queue<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionstoragequeueendpoint">*Event<wbr>Subscription<wbr>Storage<wbr>Queue<wbr>Endpoint</a></span>
    </dt>
    <dd>{{% md %}}A `storage_queue_endpoint` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subject<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionsubjectfilter">*Event<wbr>Subscription<wbr>Subject<wbr>Filter</a></span>
    </dt>
    <dd>{{% md %}}A `subject_filter` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Topic<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the topic to associate with the event subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Webhook<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionwebhookendpoint">*Event<wbr>Subscription<wbr>Webhook<wbr>Endpoint</a></span>
    </dt>
    <dd>{{% md %}}A `webhook_endpoint` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>event<wbr>Delivery<wbr>Schema</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the event delivery schema for the event subscription. Possible values include: `EventGridSchema`, `CloudEventV01Schema`, `CustomInputSchema`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>eventhub<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptioneventhubendpoint">Event<wbr>Subscription<wbr>Eventhub<wbr>Endpoint?</a></span>
    </dt>
    <dd>{{% md %}}A `eventhub_endpoint` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hybrid<wbr>Connection<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionhybridconnectionendpoint">Event<wbr>Subscription<wbr>Hybrid<wbr>Connection<wbr>Endpoint?</a></span>
    </dt>
    <dd>{{% md %}}A `hybrid_connection_endpoint` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>included<wbr>Event<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of applicable event types that need to be part of the event subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of labels to assign to the event subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the EventGrid Event Subscription resource. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retry<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionretrypolicy">Event<wbr>Subscription<wbr>Retry<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}A `retry_policy` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scope</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the scope at which the EventGrid Event Subscription should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage<wbr>Blob<wbr>Dead<wbr>Letter<wbr>Destination</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionstorageblobdeadletterdestination">Event<wbr>Subscription<wbr>Storage<wbr>Blob<wbr>Dead<wbr>Letter<wbr>Destination?</a></span>
    </dt>
    <dd>{{% md %}}A `storage_blob_dead_letter_destination` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage<wbr>Queue<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionstoragequeueendpoint">Event<wbr>Subscription<wbr>Storage<wbr>Queue<wbr>Endpoint?</a></span>
    </dt>
    <dd>{{% md %}}A `storage_queue_endpoint` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subject<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionsubjectfilter">Event<wbr>Subscription<wbr>Subject<wbr>Filter?</a></span>
    </dt>
    <dd>{{% md %}}A `subject_filter` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>topic<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the topic to associate with the event subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>webhook<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionwebhookendpoint">Event<wbr>Subscription<wbr>Webhook<wbr>Endpoint?</a></span>
    </dt>
    <dd>{{% md %}}A `webhook_endpoint` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>event_<wbr>delivery_<wbr>schema</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the event delivery schema for the event subscription. Possible values include: `EventGridSchema`, `CloudEventV01Schema`, `CustomInputSchema`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>eventhub_<wbr>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptioneventhubendpoint">Dict[Event<wbr>Subscription<wbr>Eventhub<wbr>Endpoint]</a></span>
    </dt>
    <dd>{{% md %}}A `eventhub_endpoint` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>hybrid_<wbr>connection_<wbr>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionhybridconnectionendpoint">Dict[Event<wbr>Subscription<wbr>Hybrid<wbr>Connection<wbr>Endpoint]</a></span>
    </dt>
    <dd>{{% md %}}A `hybrid_connection_endpoint` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>included_<wbr>event_<wbr>types</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of applicable event types that need to be part of the event subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of labels to assign to the event subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the EventGrid Event Subscription resource. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retry_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionretrypolicy">Dict[Event<wbr>Subscription<wbr>Retry<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A `retry_policy` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>scope</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the scope at which the EventGrid Event Subscription should be created. Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage_<wbr>blob_<wbr>dead_<wbr>letter_<wbr>destination</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionstorageblobdeadletterdestination">Dict[Event<wbr>Subscription<wbr>Storage<wbr>Blob<wbr>Dead<wbr>Letter<wbr>Destination]</a></span>
    </dt>
    <dd>{{% md %}}A `storage_blob_dead_letter_destination` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>storage_<wbr>queue_<wbr>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionstoragequeueendpoint">Dict[Event<wbr>Subscription<wbr>Storage<wbr>Queue<wbr>Endpoint]</a></span>
    </dt>
    <dd>{{% md %}}A `storage_queue_endpoint` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subject_<wbr>filter</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionsubjectfilter">Dict[Event<wbr>Subscription<wbr>Subject<wbr>Filter]</a></span>
    </dt>
    <dd>{{% md %}}A `subject_filter` block as defined below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>topic_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the topic to associate with the event subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>webhook_<wbr>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#eventsubscriptionwebhookendpoint">Dict[Event<wbr>Subscription<wbr>Webhook<wbr>Endpoint]</a></span>
    </dt>
    <dd>{{% md %}}A `webhook_endpoint` block as defined below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Event<wbr>Subscription<wbr>Eventhub<wbr>Endpoint</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#EventSubscriptionEventhubEndpoint">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#EventSubscriptionEventhubEndpoint">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/eventhub?tab=doc#EventSubscriptionEventhubEndpointArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/eventhub?tab=doc#EventSubscriptionEventhubEndpointOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Eventhub<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the id of the eventhub where the Event Subscription will receive events.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Eventhub<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the id of the eventhub where the Event Subscription will receive events.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>eventhub<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the id of the eventhub where the Event Subscription will receive events.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>eventhub_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the id of the eventhub where the Event Subscription will receive events.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Event<wbr>Subscription<wbr>Hybrid<wbr>Connection<wbr>Endpoint</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#EventSubscriptionHybridConnectionEndpoint">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#EventSubscriptionHybridConnectionEndpoint">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/eventhub?tab=doc#EventSubscriptionHybridConnectionEndpointArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/eventhub?tab=doc#EventSubscriptionHybridConnectionEndpointOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Hybrid<wbr>Connection<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the id of the hybrid connection where the Event Subscription will receive events.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Hybrid<wbr>Connection<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the id of the hybrid connection where the Event Subscription will receive events.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>hybrid<wbr>Connection<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the id of the hybrid connection where the Event Subscription will receive events.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>hybrid<wbr>Connection<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the id of the hybrid connection where the Event Subscription will receive events.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Event<wbr>Subscription<wbr>Retry<wbr>Policy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#EventSubscriptionRetryPolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#EventSubscriptionRetryPolicy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/eventhub?tab=doc#EventSubscriptionRetryPolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/eventhub?tab=doc#EventSubscriptionRetryPolicyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Event<wbr>Time<wbr>To<wbr>Live</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Specifies the time to live (in minutes) for events.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Delivery<wbr>Attempts</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Specifies the maximum number of delivery retry attempts for events.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Event<wbr>Time<wbr>To<wbr>Live</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Specifies the time to live (in minutes) for events.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Max<wbr>Delivery<wbr>Attempts</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}Specifies the maximum number of delivery retry attempts for events.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>event<wbr>Time<wbr>To<wbr>Live</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Specifies the time to live (in minutes) for events.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Delivery<wbr>Attempts</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}Specifies the maximum number of delivery retry attempts for events.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>event<wbr>Time<wbr>To<wbr>Live</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Specifies the time to live (in minutes) for events.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>max<wbr>Delivery<wbr>Attempts</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Specifies the maximum number of delivery retry attempts for events.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Event<wbr>Subscription<wbr>Storage<wbr>Blob<wbr>Dead<wbr>Letter<wbr>Destination</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#EventSubscriptionStorageBlobDeadLetterDestination">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#EventSubscriptionStorageBlobDeadLetterDestination">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/eventhub?tab=doc#EventSubscriptionStorageBlobDeadLetterDestinationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/eventhub?tab=doc#EventSubscriptionStorageBlobDeadLetterDestinationOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Storage<wbr>Account<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the id of the storage account id where the storage blob is located.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Storage<wbr>Blob<wbr>Container<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Storage blob container that is the destination of the deadletter events
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Storage<wbr>Account<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the id of the storage account id where the storage blob is located.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Storage<wbr>Blob<wbr>Container<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Storage blob container that is the destination of the deadletter events
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>storage<wbr>Account<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the id of the storage account id where the storage blob is located.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>storage<wbr>Blob<wbr>Container<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Storage blob container that is the destination of the deadletter events
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>storage_<wbr>account_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the id of the storage account id where the storage blob is located.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>storage<wbr>Blob<wbr>Container<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the Storage blob container that is the destination of the deadletter events
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Event<wbr>Subscription<wbr>Storage<wbr>Queue<wbr>Endpoint</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#EventSubscriptionStorageQueueEndpoint">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#EventSubscriptionStorageQueueEndpoint">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/eventhub?tab=doc#EventSubscriptionStorageQueueEndpointArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/eventhub?tab=doc#EventSubscriptionStorageQueueEndpointOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Queue<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the storage queue where the Event Subscriptio will receive events.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Storage<wbr>Account<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the id of the storage account id where the storage queue is located.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Queue<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the storage queue where the Event Subscriptio will receive events.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Storage<wbr>Account<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the id of the storage account id where the storage queue is located.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>queue<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the storage queue where the Event Subscriptio will receive events.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>storage<wbr>Account<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the id of the storage account id where the storage queue is located.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>queue_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the name of the storage queue where the Event Subscriptio will receive events.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>storage_<wbr>account_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the id of the storage account id where the storage queue is located.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Event<wbr>Subscription<wbr>Subject<wbr>Filter</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#EventSubscriptionSubjectFilter">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#EventSubscriptionSubjectFilter">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/eventhub?tab=doc#EventSubscriptionSubjectFilterArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/eventhub?tab=doc#EventSubscriptionSubjectFilterOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Case<wbr>Sensitive</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Specifies if `subject_begins_with` and `subject_ends_with` case sensitive. This value defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subject<wbr>Begins<wbr>With</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A string to filter events for an event subscription based on a resource path prefix.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subject<wbr>Ends<wbr>With</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A string to filter events for an event subscription based on a resource path suffix.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Case<wbr>Sensitive</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Specifies if `subject_begins_with` and `subject_ends_with` case sensitive. This value defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subject<wbr>Begins<wbr>With</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A string to filter events for an event subscription based on a resource path prefix.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Subject<wbr>Ends<wbr>With</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A string to filter events for an event subscription based on a resource path suffix.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>case<wbr>Sensitive</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Specifies if `subject_begins_with` and `subject_ends_with` case sensitive. This value defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subject<wbr>Begins<wbr>With</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A string to filter events for an event subscription based on a resource path prefix.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subject<wbr>Ends<wbr>With</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A string to filter events for an event subscription based on a resource path suffix.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>case<wbr>Sensitive</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Specifies if `subject_begins_with` and `subject_ends_with` case sensitive. This value defaults to `false`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subject<wbr>Begins<wbr>With</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A string to filter events for an event subscription based on a resource path prefix.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>subject<wbr>Ends<wbr>With</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A string to filter events for an event subscription based on a resource path suffix.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Event<wbr>Subscription<wbr>Webhook<wbr>Endpoint</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/input/#EventSubscriptionWebhookEndpoint">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/azure/types/output/#EventSubscriptionWebhookEndpoint">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/eventhub?tab=doc#EventSubscriptionWebhookEndpointArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-azure/sdk/go/azure/eventhub?tab=doc#EventSubscriptionWebhookEndpointOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the url of the webhook where the Event Subscription will receive events.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the url of the webhook where the Event Subscription will receive events.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Specifies the url of the webhook where the Event Subscription will receive events.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the url of the webhook where the Event Subscription will receive events.
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

