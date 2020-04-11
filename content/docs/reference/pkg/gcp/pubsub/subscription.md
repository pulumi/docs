
---
title: "Subscription"
block_external_search_index: true
---



A named resource representing the stream of messages from a single,
specific topic, to be delivered to the subscribing application.


To get more information about Subscription, see:

* [API documentation](https://cloud.google.com/pubsub/docs/reference/rest/v1/projects.subscriptions)
* How-to Guides
    * [Managing Subscriptions](https://cloud.google.com/pubsub/docs/admin#managing_subscriptions)

> This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/pubsub_subscription.html.markdown.



## Create a Subscription Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/pubsub/#Subscription">Subscription</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/pubsub/#SubscriptionArgs">SubscriptionArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Subscription</span><span class="p">(resource_name, opts=None, </span>ack_deadline_seconds=None<span class="p">, </span>expiration_policy=None<span class="p">, </span>labels=None<span class="p">, </span>message_retention_duration=None<span class="p">, </span>name=None<span class="p">, </span>project=None<span class="p">, </span>push_config=None<span class="p">, </span>retain_acked_messages=None<span class="p">, </span>topic=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewSubscription<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/pubsub?tab=doc#SubscriptionArgs">SubscriptionArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/pubsub?tab=doc#Subscription">Subscription</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Pubsub.Subscription.html">Subscription</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.PubSub.SubscriptionArgs.html">SubscriptionArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Ack<wbr>Deadline<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}This value is the maximum time after a subscriber receives a message before the subscriber should acknowledge the
message. After message delivery but before the ack deadline expires and before the message is acknowledged, it is an
outstanding message and will not be delivered again during that time (on a best-effort basis). For pull subscriptions,
this value is used as the initial value for the ack deadline. To override this value for a given message, call
subscriptions.modifyAckDeadline with the corresponding ackId if using pull. The minimum custom deadline you can specify
is 10 seconds. The maximum custom deadline you can specify is 600 seconds (10 minutes). If this parameter is 0, a
default value of 10 seconds is used. For push delivery, this value is also used to set the request timeout for the call
to the push endpoint. If the subscriber never acknowledges the message, the Pub/Sub system will eventually redeliver the
message.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expiration<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subscriptionexpirationpolicy">Subscription<wbr>Expiration<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A policy that specifies the conditions for this subscription's expiration. A subscription is considered active as long
as any connected subscriber is successfully consuming messages from the subscription or is issuing operations on the
subscription. If expirationPolicy is not set, a default policy with ttl of 31 days will be used. If it is set but ttl is
"", the resource never expires. The minimum allowed value for expirationPolicy.ttl is 1 day.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to this Subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Message<wbr>Retention<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}How long to retain unacknowledged messages in the subscription's backlog, from the moment a message is published. If
retainAckedMessages is true, then this also configures the retention of acknowledged messages, and thus configures how
far back in time a subscriptions.seek can be done. Defaults to 7 days. Cannot be more than 7 days ('"604800s"') or less
than 10 minutes ('"600s"'). A duration in seconds with up to nine fractional digits, terminated by 's'. Example:
'"600.5s"'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Push<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subscriptionpushconfig">Subscription<wbr>Push<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}If push delivery is used with this subscription, this field is used to configure it. An empty pushConfig signifies that
the subscriber will pull and ack messages using API methods.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retain<wbr>Acked<wbr>Messages</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Indicates whether to retain acknowledged messages. If 'true', then messages are not expunged from the subscription's
backlog, even if they are acknowledged, until they fall out of the messageRetentionDuration window.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Topic</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A reference to a Topic resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Ack<wbr>Deadline<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}This value is the maximum time after a subscriber receives a message before the subscriber should acknowledge the
message. After message delivery but before the ack deadline expires and before the message is acknowledged, it is an
outstanding message and will not be delivered again during that time (on a best-effort basis). For pull subscriptions,
this value is used as the initial value for the ack deadline. To override this value for a given message, call
subscriptions.modifyAckDeadline with the corresponding ackId if using pull. The minimum custom deadline you can specify
is 10 seconds. The maximum custom deadline you can specify is 600 seconds (10 minutes). If this parameter is 0, a
default value of 10 seconds is used. For push delivery, this value is also used to set the request timeout for the call
to the push endpoint. If the subscriber never acknowledges the message, the Pub/Sub system will eventually redeliver the
message.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expiration<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subscriptionexpirationpolicy">*Subscription<wbr>Expiration<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A policy that specifies the conditions for this subscription's expiration. A subscription is considered active as long
as any connected subscriber is successfully consuming messages from the subscription or is issuing operations on the
subscription. If expirationPolicy is not set, a default policy with ttl of 31 days will be used. If it is set but ttl is
"", the resource never expires. The minimum allowed value for expirationPolicy.ttl is 1 day.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to this Subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Message<wbr>Retention<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}How long to retain unacknowledged messages in the subscription's backlog, from the moment a message is published. If
retainAckedMessages is true, then this also configures the retention of acknowledged messages, and thus configures how
far back in time a subscriptions.seek can be done. Defaults to 7 days. Cannot be more than 7 days ('"604800s"') or less
than 10 minutes ('"600s"'). A duration in seconds with up to nine fractional digits, terminated by 's'. Example:
'"600.5s"'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Push<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subscriptionpushconfig">*Subscription<wbr>Push<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}If push delivery is used with this subscription, this field is used to configure it. An empty pushConfig signifies that
the subscriber will pull and ack messages using API methods.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retain<wbr>Acked<wbr>Messages</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Indicates whether to retain acknowledged messages. If 'true', then messages are not expunged from the subscription's
backlog, even if they are acknowledged, until they fall out of the messageRetentionDuration window.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Topic</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A reference to a Topic resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>ack<wbr>Deadline<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}This value is the maximum time after a subscriber receives a message before the subscriber should acknowledge the
message. After message delivery but before the ack deadline expires and before the message is acknowledged, it is an
outstanding message and will not be delivered again during that time (on a best-effort basis). For pull subscriptions,
this value is used as the initial value for the ack deadline. To override this value for a given message, call
subscriptions.modifyAckDeadline with the corresponding ackId if using pull. The minimum custom deadline you can specify
is 10 seconds. The maximum custom deadline you can specify is 600 seconds (10 minutes). If this parameter is 0, a
default value of 10 seconds is used. For push delivery, this value is also used to set the request timeout for the call
to the push endpoint. If the subscriber never acknowledges the message, the Pub/Sub system will eventually redeliver the
message.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expiration<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subscriptionexpirationpolicy">Subscription<wbr>Expiration<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}A policy that specifies the conditions for this subscription's expiration. A subscription is considered active as long
as any connected subscriber is successfully consuming messages from the subscription or is issuing operations on the
subscription. If expirationPolicy is not set, a default policy with ttl of 31 days will be used. If it is set but ttl is
"", the resource never expires. The minimum allowed value for expirationPolicy.ttl is 1 day.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to this Subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>message<wbr>Retention<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}How long to retain unacknowledged messages in the subscription's backlog, from the moment a message is published. If
retainAckedMessages is true, then this also configures the retention of acknowledged messages, and thus configures how
far back in time a subscriptions.seek can be done. Defaults to 7 days. Cannot be more than 7 days ('"604800s"') or less
than 10 minutes ('"600s"'). A duration in seconds with up to nine fractional digits, terminated by 's'. Example:
'"600.5s"'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>push<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subscriptionpushconfig">Subscription<wbr>Push<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}If push delivery is used with this subscription, this field is used to configure it. An empty pushConfig signifies that
the subscriber will pull and ack messages using API methods.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retain<wbr>Acked<wbr>Messages</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Indicates whether to retain acknowledged messages. If 'true', then messages are not expunged from the subscription's
backlog, even if they are acknowledged, until they fall out of the messageRetentionDuration window.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>topic</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A reference to a Topic resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>ack_<wbr>deadline_<wbr>seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}This value is the maximum time after a subscriber receives a message before the subscriber should acknowledge the
message. After message delivery but before the ack deadline expires and before the message is acknowledged, it is an
outstanding message and will not be delivered again during that time (on a best-effort basis). For pull subscriptions,
this value is used as the initial value for the ack deadline. To override this value for a given message, call
subscriptions.modifyAckDeadline with the corresponding ackId if using pull. The minimum custom deadline you can specify
is 10 seconds. The maximum custom deadline you can specify is 600 seconds (10 minutes). If this parameter is 0, a
default value of 10 seconds is used. For push delivery, this value is also used to set the request timeout for the call
to the push endpoint. If the subscriber never acknowledges the message, the Pub/Sub system will eventually redeliver the
message.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expiration_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subscriptionexpirationpolicy">Dict[Subscription<wbr>Expiration<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A policy that specifies the conditions for this subscription's expiration. A subscription is considered active as long
as any connected subscriber is successfully consuming messages from the subscription or is issuing operations on the
subscription. If expirationPolicy is not set, a default policy with ttl of 31 days will be used. If it is set but ttl is
"", the resource never expires. The minimum allowed value for expirationPolicy.ttl is 1 day.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to this Subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>message_<wbr>retention_<wbr>duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}How long to retain unacknowledged messages in the subscription's backlog, from the moment a message is published. If
retainAckedMessages is true, then this also configures the retention of acknowledged messages, and thus configures how
far back in time a subscriptions.seek can be done. Defaults to 7 days. Cannot be more than 7 days ('"604800s"') or less
than 10 minutes ('"600s"'). A duration in seconds with up to nine fractional digits, terminated by 's'. Example:
'"600.5s"'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>push_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subscriptionpushconfig">Dict[Subscription<wbr>Push<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}If push delivery is used with this subscription, this field is used to configure it. An empty pushConfig signifies that
the subscriber will pull and ack messages using API methods.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retain_<wbr>acked_<wbr>messages</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Indicates whether to retain acknowledged messages. If 'true', then messages are not expunged from the subscription's
backlog, even if they are acknowledged, until they fall out of the messageRetentionDuration window.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>topic</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A reference to a Topic resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Subscription Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Ack<wbr>Deadline<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}This value is the maximum time after a subscriber receives a message before the subscriber should acknowledge the
message. After message delivery but before the ack deadline expires and before the message is acknowledged, it is an
outstanding message and will not be delivered again during that time (on a best-effort basis). For pull subscriptions,
this value is used as the initial value for the ack deadline. To override this value for a given message, call
subscriptions.modifyAckDeadline with the corresponding ackId if using pull. The minimum custom deadline you can specify
is 10 seconds. The maximum custom deadline you can specify is 600 seconds (10 minutes). If this parameter is 0, a
default value of 10 seconds is used. For push delivery, this value is also used to set the request timeout for the call
to the push endpoint. If the subscriber never acknowledges the message, the Pub/Sub system will eventually redeliver the
message.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Expiration<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subscriptionexpirationpolicy">Subscription<wbr>Expiration<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A policy that specifies the conditions for this subscription's expiration. A subscription is considered active as long
as any connected subscriber is successfully consuming messages from the subscription or is issuing operations on the
subscription. If expirationPolicy is not set, a default policy with ttl of 31 days will be used. If it is set but ttl is
"", the resource never expires. The minimum allowed value for expirationPolicy.ttl is 1 day.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to this Subscription.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Message<wbr>Retention<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}How long to retain unacknowledged messages in the subscription's backlog, from the moment a message is published. If
retainAckedMessages is true, then this also configures the retention of acknowledged messages, and thus configures how
far back in time a subscriptions.seek can be done. Defaults to 7 days. Cannot be more than 7 days ('"604800s"') or less
than 10 minutes ('"600s"'). A duration in seconds with up to nine fractional digits, terminated by 's'. Example:
'"600.5s"'.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the subscription.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Push<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subscriptionpushconfig">Subscription<wbr>Push<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}If push delivery is used with this subscription, this field is used to configure it. An empty pushConfig signifies that
the subscriber will pull and ack messages using API methods.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Retain<wbr>Acked<wbr>Messages</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Indicates whether to retain acknowledged messages. If 'true', then messages are not expunged from the subscription's
backlog, even if they are acknowledged, until they fall out of the messageRetentionDuration window.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Topic</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A reference to a Topic resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Ack<wbr>Deadline<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}This value is the maximum time after a subscriber receives a message before the subscriber should acknowledge the
message. After message delivery but before the ack deadline expires and before the message is acknowledged, it is an
outstanding message and will not be delivered again during that time (on a best-effort basis). For pull subscriptions,
this value is used as the initial value for the ack deadline. To override this value for a given message, call
subscriptions.modifyAckDeadline with the corresponding ackId if using pull. The minimum custom deadline you can specify
is 10 seconds. The maximum custom deadline you can specify is 600 seconds (10 minutes). If this parameter is 0, a
default value of 10 seconds is used. For push delivery, this value is also used to set the request timeout for the call
to the push endpoint. If the subscriber never acknowledges the message, the Pub/Sub system will eventually redeliver the
message.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Expiration<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subscriptionexpirationpolicy">Subscription<wbr>Expiration<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A policy that specifies the conditions for this subscription's expiration. A subscription is considered active as long
as any connected subscriber is successfully consuming messages from the subscription or is issuing operations on the
subscription. If expirationPolicy is not set, a default policy with ttl of 31 days will be used. If it is set but ttl is
"", the resource never expires. The minimum allowed value for expirationPolicy.ttl is 1 day.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to this Subscription.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Message<wbr>Retention<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}How long to retain unacknowledged messages in the subscription's backlog, from the moment a message is published. If
retainAckedMessages is true, then this also configures the retention of acknowledged messages, and thus configures how
far back in time a subscriptions.seek can be done. Defaults to 7 days. Cannot be more than 7 days ('"604800s"') or less
than 10 minutes ('"600s"'). A duration in seconds with up to nine fractional digits, terminated by 's'. Example:
'"600.5s"'.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the subscription.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Push<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subscriptionpushconfig">*Subscription<wbr>Push<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}If push delivery is used with this subscription, this field is used to configure it. An empty pushConfig signifies that
the subscriber will pull and ack messages using API methods.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Retain<wbr>Acked<wbr>Messages</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Indicates whether to retain acknowledged messages. If 'true', then messages are not expunged from the subscription's
backlog, even if they are acknowledged, until they fall out of the messageRetentionDuration window.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Topic</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A reference to a Topic resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>ack<wbr>Deadline<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}This value is the maximum time after a subscriber receives a message before the subscriber should acknowledge the
message. After message delivery but before the ack deadline expires and before the message is acknowledged, it is an
outstanding message and will not be delivered again during that time (on a best-effort basis). For pull subscriptions,
this value is used as the initial value for the ack deadline. To override this value for a given message, call
subscriptions.modifyAckDeadline with the corresponding ackId if using pull. The minimum custom deadline you can specify
is 10 seconds. The maximum custom deadline you can specify is 600 seconds (10 minutes). If this parameter is 0, a
default value of 10 seconds is used. For push delivery, this value is also used to set the request timeout for the call
to the push endpoint. If the subscriber never acknowledges the message, the Pub/Sub system will eventually redeliver the
message.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>expiration<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subscriptionexpirationpolicy">Subscription<wbr>Expiration<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A policy that specifies the conditions for this subscription's expiration. A subscription is considered active as long
as any connected subscriber is successfully consuming messages from the subscription or is issuing operations on the
subscription. If expirationPolicy is not set, a default policy with ttl of 31 days will be used. If it is set but ttl is
"", the resource never expires. The minimum allowed value for expirationPolicy.ttl is 1 day.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to this Subscription.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>message<wbr>Retention<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}How long to retain unacknowledged messages in the subscription's backlog, from the moment a message is published. If
retainAckedMessages is true, then this also configures the retention of acknowledged messages, and thus configures how
far back in time a subscriptions.seek can be done. Defaults to 7 days. Cannot be more than 7 days ('"604800s"') or less
than 10 minutes ('"600s"'). A duration in seconds with up to nine fractional digits, terminated by 's'. Example:
'"600.5s"'.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the subscription.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>push<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subscriptionpushconfig">Subscription<wbr>Push<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}If push delivery is used with this subscription, this field is used to configure it. An empty pushConfig signifies that
the subscriber will pull and ack messages using API methods.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>retain<wbr>Acked<wbr>Messages</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Indicates whether to retain acknowledged messages. If 'true', then messages are not expunged from the subscription's
backlog, even if they are acknowledged, until they fall out of the messageRetentionDuration window.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>topic</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A reference to a Topic resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>ack_<wbr>deadline_<wbr>seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}This value is the maximum time after a subscriber receives a message before the subscriber should acknowledge the
message. After message delivery but before the ack deadline expires and before the message is acknowledged, it is an
outstanding message and will not be delivered again during that time (on a best-effort basis). For pull subscriptions,
this value is used as the initial value for the ack deadline. To override this value for a given message, call
subscriptions.modifyAckDeadline with the corresponding ackId if using pull. The minimum custom deadline you can specify
is 10 seconds. The maximum custom deadline you can specify is 600 seconds (10 minutes). If this parameter is 0, a
default value of 10 seconds is used. For push delivery, this value is also used to set the request timeout for the call
to the push endpoint. If the subscriber never acknowledges the message, the Pub/Sub system will eventually redeliver the
message.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>expiration_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subscriptionexpirationpolicy">Dict[Subscription<wbr>Expiration<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A policy that specifies the conditions for this subscription's expiration. A subscription is considered active as long
as any connected subscriber is successfully consuming messages from the subscription or is issuing operations on the
subscription. If expirationPolicy is not set, a default policy with ttl of 31 days will be used. If it is set but ttl is
"", the resource never expires. The minimum allowed value for expirationPolicy.ttl is 1 day.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to this Subscription.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>message_<wbr>retention_<wbr>duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}How long to retain unacknowledged messages in the subscription's backlog, from the moment a message is published. If
retainAckedMessages is true, then this also configures the retention of acknowledged messages, and thus configures how
far back in time a subscriptions.seek can be done. Defaults to 7 days. Cannot be more than 7 days ('"604800s"') or less
than 10 minutes ('"600s"'). A duration in seconds with up to nine fractional digits, terminated by 's'. Example:
'"600.5s"'.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the subscription.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>push_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subscriptionpushconfig">Dict[Subscription<wbr>Push<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}If push delivery is used with this subscription, this field is used to configure it. An empty pushConfig signifies that
the subscriber will pull and ack messages using API methods.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>retain_<wbr>acked_<wbr>messages</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Indicates whether to retain acknowledged messages. If 'true', then messages are not expunged from the subscription's
backlog, even if they are acknowledged, until they fall out of the messageRetentionDuration window.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>topic</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A reference to a Topic resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Subscription Resource

Get an existing Subscription resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/pubsub/#SubscriptionState">SubscriptionState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/pubsub/#Subscription">Subscription</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>ack_deadline_seconds=None<span class="p">, </span>expiration_policy=None<span class="p">, </span>labels=None<span class="p">, </span>message_retention_duration=None<span class="p">, </span>name=None<span class="p">, </span>path=None<span class="p">, </span>project=None<span class="p">, </span>push_config=None<span class="p">, </span>retain_acked_messages=None<span class="p">, </span>topic=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetSubscription<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/pubsub?tab=doc#SubscriptionState">SubscriptionState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/pubsub?tab=doc#Subscription">Subscription</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Pubsub.Subscription.html">Subscription</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Pubsub.SubscriptionState.html">SubscriptionState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Ack<wbr>Deadline<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}This value is the maximum time after a subscriber receives a message before the subscriber should acknowledge the
message. After message delivery but before the ack deadline expires and before the message is acknowledged, it is an
outstanding message and will not be delivered again during that time (on a best-effort basis). For pull subscriptions,
this value is used as the initial value for the ack deadline. To override this value for a given message, call
subscriptions.modifyAckDeadline with the corresponding ackId if using pull. The minimum custom deadline you can specify
is 10 seconds. The maximum custom deadline you can specify is 600 seconds (10 minutes). If this parameter is 0, a
default value of 10 seconds is used. For push delivery, this value is also used to set the request timeout for the call
to the push endpoint. If the subscriber never acknowledges the message, the Pub/Sub system will eventually redeliver the
message.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expiration<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subscriptionexpirationpolicy">Subscription<wbr>Expiration<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A policy that specifies the conditions for this subscription's expiration. A subscription is considered active as long
as any connected subscriber is successfully consuming messages from the subscription or is issuing operations on the
subscription. If expirationPolicy is not set, a default policy with ttl of 31 days will be used. If it is set but ttl is
"", the resource never expires. The minimum allowed value for expirationPolicy.ttl is 1 day.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to this Subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Message<wbr>Retention<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}How long to retain unacknowledged messages in the subscription's backlog, from the moment a message is published. If
retainAckedMessages is true, then this also configures the retention of acknowledged messages, and thus configures how
far back in time a subscriptions.seek can be done. Defaults to 7 days. Cannot be more than 7 days ('"604800s"') or less
than 10 minutes ('"600s"'). A duration in seconds with up to nine fractional digits, terminated by 's'. Example:
'"600.5s"'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Push<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subscriptionpushconfig">Subscription<wbr>Push<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}If push delivery is used with this subscription, this field is used to configure it. An empty pushConfig signifies that
the subscriber will pull and ack messages using API methods.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retain<wbr>Acked<wbr>Messages</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Indicates whether to retain acknowledged messages. If 'true', then messages are not expunged from the subscription's
backlog, even if they are acknowledged, until they fall out of the messageRetentionDuration window.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Topic</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A reference to a Topic resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Ack<wbr>Deadline<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}This value is the maximum time after a subscriber receives a message before the subscriber should acknowledge the
message. After message delivery but before the ack deadline expires and before the message is acknowledged, it is an
outstanding message and will not be delivered again during that time (on a best-effort basis). For pull subscriptions,
this value is used as the initial value for the ack deadline. To override this value for a given message, call
subscriptions.modifyAckDeadline with the corresponding ackId if using pull. The minimum custom deadline you can specify
is 10 seconds. The maximum custom deadline you can specify is 600 seconds (10 minutes). If this parameter is 0, a
default value of 10 seconds is used. For push delivery, this value is also used to set the request timeout for the call
to the push endpoint. If the subscriber never acknowledges the message, the Pub/Sub system will eventually redeliver the
message.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expiration<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subscriptionexpirationpolicy">*Subscription<wbr>Expiration<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}A policy that specifies the conditions for this subscription's expiration. A subscription is considered active as long
as any connected subscriber is successfully consuming messages from the subscription or is issuing operations on the
subscription. If expirationPolicy is not set, a default policy with ttl of 31 days will be used. If it is set but ttl is
"", the resource never expires. The minimum allowed value for expirationPolicy.ttl is 1 day.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to this Subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Message<wbr>Retention<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}How long to retain unacknowledged messages in the subscription's backlog, from the moment a message is published. If
retainAckedMessages is true, then this also configures the retention of acknowledged messages, and thus configures how
far back in time a subscriptions.seek can be done. Defaults to 7 days. Cannot be more than 7 days ('"604800s"') or less
than 10 minutes ('"600s"'). A duration in seconds with up to nine fractional digits, terminated by 's'. Example:
'"600.5s"'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Path</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Push<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subscriptionpushconfig">*Subscription<wbr>Push<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}If push delivery is used with this subscription, this field is used to configure it. An empty pushConfig signifies that
the subscriber will pull and ack messages using API methods.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retain<wbr>Acked<wbr>Messages</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Indicates whether to retain acknowledged messages. If 'true', then messages are not expunged from the subscription's
backlog, even if they are acknowledged, until they fall out of the messageRetentionDuration window.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Topic</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A reference to a Topic resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>ack<wbr>Deadline<wbr>Seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}This value is the maximum time after a subscriber receives a message before the subscriber should acknowledge the
message. After message delivery but before the ack deadline expires and before the message is acknowledged, it is an
outstanding message and will not be delivered again during that time (on a best-effort basis). For pull subscriptions,
this value is used as the initial value for the ack deadline. To override this value for a given message, call
subscriptions.modifyAckDeadline with the corresponding ackId if using pull. The minimum custom deadline you can specify
is 10 seconds. The maximum custom deadline you can specify is 600 seconds (10 minutes). If this parameter is 0, a
default value of 10 seconds is used. For push delivery, this value is also used to set the request timeout for the call
to the push endpoint. If the subscriber never acknowledges the message, the Pub/Sub system will eventually redeliver the
message.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expiration<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subscriptionexpirationpolicy">Subscription<wbr>Expiration<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}A policy that specifies the conditions for this subscription's expiration. A subscription is considered active as long
as any connected subscriber is successfully consuming messages from the subscription or is issuing operations on the
subscription. If expirationPolicy is not set, a default policy with ttl of 31 days will be used. If it is set but ttl is
"", the resource never expires. The minimum allowed value for expirationPolicy.ttl is 1 day.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to this Subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>message<wbr>Retention<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}How long to retain unacknowledged messages in the subscription's backlog, from the moment a message is published. If
retainAckedMessages is true, then this also configures the retention of acknowledged messages, and thus configures how
far back in time a subscriptions.seek can be done. Defaults to 7 days. Cannot be more than 7 days ('"604800s"') or less
than 10 minutes ('"600s"'). A duration in seconds with up to nine fractional digits, terminated by 's'. Example:
'"600.5s"'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>push<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subscriptionpushconfig">Subscription<wbr>Push<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}If push delivery is used with this subscription, this field is used to configure it. An empty pushConfig signifies that
the subscriber will pull and ack messages using API methods.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retain<wbr>Acked<wbr>Messages</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Indicates whether to retain acknowledged messages. If 'true', then messages are not expunged from the subscription's
backlog, even if they are acknowledged, until they fall out of the messageRetentionDuration window.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>topic</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A reference to a Topic resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>ack_<wbr>deadline_<wbr>seconds</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}This value is the maximum time after a subscriber receives a message before the subscriber should acknowledge the
message. After message delivery but before the ack deadline expires and before the message is acknowledged, it is an
outstanding message and will not be delivered again during that time (on a best-effort basis). For pull subscriptions,
this value is used as the initial value for the ack deadline. To override this value for a given message, call
subscriptions.modifyAckDeadline with the corresponding ackId if using pull. The minimum custom deadline you can specify
is 10 seconds. The maximum custom deadline you can specify is 600 seconds (10 minutes). If this parameter is 0, a
default value of 10 seconds is used. For push delivery, this value is also used to set the request timeout for the call
to the push endpoint. If the subscriber never acknowledges the message, the Pub/Sub system will eventually redeliver the
message.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expiration_<wbr>policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subscriptionexpirationpolicy">Dict[Subscription<wbr>Expiration<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}A policy that specifies the conditions for this subscription's expiration. A subscription is considered active as long
as any connected subscriber is successfully consuming messages from the subscription or is issuing operations on the
subscription. If expirationPolicy is not set, a default policy with ttl of 31 days will be used. If it is set but ttl is
"", the resource never expires. The minimum allowed value for expirationPolicy.ttl is 1 day.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to this Subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>message_<wbr>retention_<wbr>duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}How long to retain unacknowledged messages in the subscription's backlog, from the moment a message is published. If
retainAckedMessages is true, then this also configures the retention of acknowledged messages, and thus configures how
far back in time a subscriptions.seek can be done. Defaults to 7 days. Cannot be more than 7 days ('"604800s"') or less
than 10 minutes ('"600s"'). A duration in seconds with up to nine fractional digits, terminated by 's'. Example:
'"600.5s"'.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the subscription.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>path</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>push_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subscriptionpushconfig">Dict[Subscription<wbr>Push<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}If push delivery is used with this subscription, this field is used to configure it. An empty pushConfig signifies that
the subscriber will pull and ack messages using API methods.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retain_<wbr>acked_<wbr>messages</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Indicates whether to retain acknowledged messages. If 'true', then messages are not expunged from the subscription's
backlog, even if they are acknowledged, until they fall out of the messageRetentionDuration window.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>topic</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A reference to a Topic resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Subscription<wbr>Expiration<wbr>Policy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#SubscriptionExpirationPolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#SubscriptionExpirationPolicy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/pubsub?tab=doc#SubscriptionExpirationPolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/pubsub?tab=doc#SubscriptionExpirationPolicyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>ttl</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Subscription<wbr>Push<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#SubscriptionPushConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#SubscriptionPushConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/pubsub?tab=doc#SubscriptionPushConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/pubsub?tab=doc#SubscriptionPushConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oidc<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subscriptionpushconfigoidctoken">Subscription<wbr>Push<wbr>Config<wbr>Oidc<wbr>Token<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Push<wbr>Endpoint</span>
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
        <span>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oidc<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subscriptionpushconfigoidctoken">*Subscription<wbr>Push<wbr>Config<wbr>Oidc<wbr>Token</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Push<wbr>Endpoint</span>
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
        <span>attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>oidc<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subscriptionpushconfigoidctoken">Subscription<wbr>Push<wbr>Config<wbr>Oidc<wbr>Token?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>push<wbr>Endpoint</span>
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
        <span>attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>oidc<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#subscriptionpushconfigoidctoken">Dict[Subscription<wbr>Push<wbr>Config<wbr>Oidc<wbr>Token]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>push<wbr>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Subscription<wbr>Push<wbr>Config<wbr>Oidc<wbr>Token</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#SubscriptionPushConfigOidcToken">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#SubscriptionPushConfigOidcToken">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/pubsub?tab=doc#SubscriptionPushConfigOidcTokenArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/pubsub?tab=doc#SubscriptionPushConfigOidcTokenOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Audience</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Service<wbr>Account<wbr>Email</span>
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
        <span>Audience</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Service<wbr>Account<wbr>Email</span>
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
        <span>audience</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>service<wbr>Account<wbr>Email</span>
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
        <span>audience</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>service_<wbr>account_<wbr>email</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-gcp">https://github.com/pulumi/pulumi-gcp</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

