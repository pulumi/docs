
---
title: "Notification"
block_external_search_index: true
---

Creates a new notification configuration on a specified bucket, establishing a flow of event notifications from GCS to a Cloud Pub/Sub topic.
 For more information see 
[the official documentation](https://cloud.google.com/storage/docs/pubsub-notifications) 
and 
[API](https://cloud.google.com/storage/docs/json_api/v1/notifications).

In order to enable notifications, a special Google Cloud Storage service account unique to the project
must have the IAM permission "projects.topics.publish" for a Cloud Pub/Sub topic in the project. To get the service
account's email address, use the `gcp.storage.getProjectServiceAccount` datasource's `email_address` value, and see below
for an example of enabling notifications by granting the correct IAM permission. See
[the notifications documentation](https://cloud.google.com/storage/docs/gsutil/commands/notification) for more details.

>**NOTE**: This resource can affect your storage IAM policy. If you are using this in the same config as your storage IAM policy resources, consider
making this resource dependent on those IAM resources via `depends_on`. This will safeguard against errors due to IAM race conditions.

> This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/storage_notification.html.markdown.



## Create a Notification Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/storage/#Notification">Notification</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/storage/#NotificationArgs">NotificationArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Notification</span><span class="p">(resource_name, opts=None, </span>bucket=None<span class="p">, </span>custom_attributes=None<span class="p">, </span>event_types=None<span class="p">, </span>object_name_prefix=None<span class="p">, </span>payload_format=None<span class="p">, </span>topic=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewNotification<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/storage?tab=doc#NotificationArgs">NotificationArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/storage?tab=doc#Notification">Notification</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Storage.Notification.html">Notification</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Storage.NotificationArgs.html">NotificationArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A set of key/value attribute pairs to attach to each Cloud PubSub message published for this notification subscription
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Event<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of event type filters for this notification config. If not specified, Cloud Storage will send notifications for all event types. The valid types are: `"OBJECT_FINALIZE"`, `"OBJECT_METADATA_UPDATE"`, `"OBJECT_DELETE"`, `"OBJECT_ARCHIVE"`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Object<wbr>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a prefix path filter for this notification config. Cloud Storage will only send notifications for objects in this bucket whose names begin with the specified prefix.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Payload<wbr>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The desired content of the Payload. One of `"JSON_API_V1"` or `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Topic</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Cloud PubSub topic to which this subscription publishes. Expects either the 
topic name, assumed to belong to the default GCP provider project, or the project-level name,
i.e. `projects/my-gcp-project/topics/my-topic` or `my-topic`. If the project is not set in the provider,
you will need to use the project-level name.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A set of key/value attribute pairs to attach to each Cloud PubSub message published for this notification subscription
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Event<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of event type filters for this notification config. If not specified, Cloud Storage will send notifications for all event types. The valid types are: `"OBJECT_FINALIZE"`, `"OBJECT_METADATA_UPDATE"`, `"OBJECT_DELETE"`, `"OBJECT_ARCHIVE"`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Object<wbr>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies a prefix path filter for this notification config. Cloud Storage will only send notifications for objects in this bucket whose names begin with the specified prefix.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Payload<wbr>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The desired content of the Payload. One of `"JSON_API_V1"` or `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Topic</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Cloud PubSub topic to which this subscription publishes. Expects either the 
topic name, assumed to belong to the default GCP provider project, or the project-level name,
i.e. `projects/my-gcp-project/topics/my-topic` or `my-topic`. If the project is not set in the provider,
you will need to use the project-level name.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A set of key/value attribute pairs to attach to each Cloud PubSub message published for this notification subscription
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>event<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of event type filters for this notification config. If not specified, Cloud Storage will send notifications for all event types. The valid types are: `"OBJECT_FINALIZE"`, `"OBJECT_METADATA_UPDATE"`, `"OBJECT_DELETE"`, `"OBJECT_ARCHIVE"`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>object<wbr>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a prefix path filter for this notification config. Cloud Storage will only send notifications for objects in this bucket whose names begin with the specified prefix.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>payload<wbr>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The desired content of the Payload. One of `"JSON_API_V1"` or `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>topic</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Cloud PubSub topic to which this subscription publishes. Expects either the 
topic name, assumed to belong to the default GCP provider project, or the project-level name,
i.e. `projects/my-gcp-project/topics/my-topic` or `my-topic`. If the project is not set in the provider,
you will need to use the project-level name.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom_<wbr>attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A set of key/value attribute pairs to attach to each Cloud PubSub message published for this notification subscription
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>event_<wbr>types</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of event type filters for this notification config. If not specified, Cloud Storage will send notifications for all event types. The valid types are: `"OBJECT_FINALIZE"`, `"OBJECT_METADATA_UPDATE"`, `"OBJECT_DELETE"`, `"OBJECT_ARCHIVE"`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>object_<wbr>name_<wbr>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies a prefix path filter for this notification config. Cloud Storage will only send notifications for objects in this bucket whose names begin with the specified prefix.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>payload_<wbr>format</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The desired content of the Payload. One of `"JSON_API_V1"` or `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>topic</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Cloud PubSub topic to which this subscription publishes. Expects either the 
topic name, assumed to belong to the default GCP provider project, or the project-level name,
i.e. `projects/my-gcp-project/topics/my-topic` or `my-topic`. If the project is not set in the provider,
you will need to use the project-level name.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Notification Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Custom<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A set of key/value attribute pairs to attach to each Cloud PubSub message published for this notification subscription
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Event<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of event type filters for this notification config. If not specified, Cloud Storage will send notifications for all event types. The valid types are: `"OBJECT_FINALIZE"`, `"OBJECT_METADATA_UPDATE"`, `"OBJECT_DELETE"`, `"OBJECT_ARCHIVE"`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Notification<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the created notification.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Object<wbr>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a prefix path filter for this notification config. Cloud Storage will only send notifications for objects in this bucket whose names begin with the specified prefix.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Payload<wbr>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The desired content of the Payload. One of `"JSON_API_V1"` or `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Topic</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Cloud PubSub topic to which this subscription publishes. Expects either the 
topic name, assumed to belong to the default GCP provider project, or the project-level name,
i.e. `projects/my-gcp-project/topics/my-topic` or `my-topic`. If the project is not set in the provider,
you will need to use the project-level name.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Custom<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A set of key/value attribute pairs to attach to each Cloud PubSub message published for this notification subscription
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Event<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of event type filters for this notification config. If not specified, Cloud Storage will send notifications for all event types. The valid types are: `"OBJECT_FINALIZE"`, `"OBJECT_METADATA_UPDATE"`, `"OBJECT_DELETE"`, `"OBJECT_ARCHIVE"`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Notification<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the created notification.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Object<wbr>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies a prefix path filter for this notification config. Cloud Storage will only send notifications for objects in this bucket whose names begin with the specified prefix.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Payload<wbr>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The desired content of the Payload. One of `"JSON_API_V1"` or `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Topic</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Cloud PubSub topic to which this subscription publishes. Expects either the 
topic name, assumed to belong to the default GCP provider project, or the project-level name,
i.e. `projects/my-gcp-project/topics/my-topic` or `my-topic`. If the project is not set in the provider,
you will need to use the project-level name.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>custom<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A set of key/value attribute pairs to attach to each Cloud PubSub message published for this notification subscription
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>event<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of event type filters for this notification config. If not specified, Cloud Storage will send notifications for all event types. The valid types are: `"OBJECT_FINALIZE"`, `"OBJECT_METADATA_UPDATE"`, `"OBJECT_DELETE"`, `"OBJECT_ARCHIVE"`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>notification<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ID of the created notification.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>object<wbr>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a prefix path filter for this notification config. Cloud Storage will only send notifications for objects in this bucket whose names begin with the specified prefix.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>payload<wbr>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The desired content of the Payload. One of `"JSON_API_V1"` or `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>topic</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The Cloud PubSub topic to which this subscription publishes. Expects either the 
topic name, assumed to belong to the default GCP provider project, or the project-level name,
i.e. `projects/my-gcp-project/topics/my-topic` or `my-topic`. If the project is not set in the provider,
you will need to use the project-level name.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>custom_<wbr>attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A set of key/value attribute pairs to attach to each Cloud PubSub message published for this notification subscription
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>event_<wbr>types</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of event type filters for this notification config. If not specified, Cloud Storage will send notifications for all event types. The valid types are: `"OBJECT_FINALIZE"`, `"OBJECT_METADATA_UPDATE"`, `"OBJECT_DELETE"`, `"OBJECT_ARCHIVE"`
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>notification_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the created notification.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>object_<wbr>name_<wbr>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies a prefix path filter for this notification config. Cloud Storage will only send notifications for objects in this bucket whose names begin with the specified prefix.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>payload_<wbr>format</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The desired content of the Payload. One of `"JSON_API_V1"` or `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>self_<wbr>link</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>topic</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Cloud PubSub topic to which this subscription publishes. Expects either the 
topic name, assumed to belong to the default GCP provider project, or the project-level name,
i.e. `projects/my-gcp-project/topics/my-topic` or `my-topic`. If the project is not set in the provider,
you will need to use the project-level name.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Notification Resource

Get an existing Notification resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/storage/#NotificationState">NotificationState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/storage/#Notification">Notification</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>bucket=None<span class="p">, </span>custom_attributes=None<span class="p">, </span>event_types=None<span class="p">, </span>notification_id=None<span class="p">, </span>object_name_prefix=None<span class="p">, </span>payload_format=None<span class="p">, </span>self_link=None<span class="p">, </span>topic=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetNotification<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/storage?tab=doc#NotificationState">NotificationState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/storage?tab=doc#Notification">Notification</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Storage.Notification.html">Notification</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Storage.NotificationState.html">NotificationState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}A set of key/value attribute pairs to attach to each Cloud PubSub message published for this notification subscription
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Event<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}List of event type filters for this notification config. If not specified, Cloud Storage will send notifications for all event types. The valid types are: `"OBJECT_FINALIZE"`, `"OBJECT_METADATA_UPDATE"`, `"OBJECT_DELETE"`, `"OBJECT_ARCHIVE"`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Notification<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the created notification.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Object<wbr>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a prefix path filter for this notification config. Cloud Storage will only send notifications for objects in this bucket whose names begin with the specified prefix.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Payload<wbr>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The desired content of the Payload. One of `"JSON_API_V1"` or `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Topic</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Cloud PubSub topic to which this subscription publishes. Expects either the 
topic name, assumed to belong to the default GCP provider project, or the project-level name,
i.e. `projects/my-gcp-project/topics/my-topic` or `my-topic`. If the project is not set in the provider,
you will need to use the project-level name.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Custom<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A set of key/value attribute pairs to attach to each Cloud PubSub message published for this notification subscription
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Event<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}List of event type filters for this notification config. If not specified, Cloud Storage will send notifications for all event types. The valid types are: `"OBJECT_FINALIZE"`, `"OBJECT_METADATA_UPDATE"`, `"OBJECT_DELETE"`, `"OBJECT_ARCHIVE"`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Notification<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ID of the created notification.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Object<wbr>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies a prefix path filter for this notification config. Cloud Storage will only send notifications for objects in this bucket whose names begin with the specified prefix.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Payload<wbr>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The desired content of the Payload. One of `"JSON_API_V1"` or `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Topic</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Cloud PubSub topic to which this subscription publishes. Expects either the 
topic name, assumed to belong to the default GCP provider project, or the project-level name,
i.e. `projects/my-gcp-project/topics/my-topic` or `my-topic`. If the project is not set in the provider,
you will need to use the project-level name.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom<wbr>Attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}A set of key/value attribute pairs to attach to each Cloud PubSub message published for this notification subscription
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>event<wbr>Types</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}List of event type filters for this notification config. If not specified, Cloud Storage will send notifications for all event types. The valid types are: `"OBJECT_FINALIZE"`, `"OBJECT_METADATA_UPDATE"`, `"OBJECT_DELETE"`, `"OBJECT_ARCHIVE"`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>notification<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ID of the created notification.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>object<wbr>Name<wbr>Prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies a prefix path filter for this notification config. Cloud Storage will only send notifications for objects in this bucket whose names begin with the specified prefix.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>payload<wbr>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The desired content of the Payload. One of `"JSON_API_V1"` or `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>topic</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Cloud PubSub topic to which this subscription publishes. Expects either the 
topic name, assumed to belong to the default GCP provider project, or the project-level name,
i.e. `projects/my-gcp-project/topics/my-topic` or `my-topic`. If the project is not set in the provider,
you will need to use the project-level name.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>custom_<wbr>attributes</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A set of key/value attribute pairs to attach to each Cloud PubSub message published for this notification subscription
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>event_<wbr>types</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}List of event type filters for this notification config. If not specified, Cloud Storage will send notifications for all event types. The valid types are: `"OBJECT_FINALIZE"`, `"OBJECT_METADATA_UPDATE"`, `"OBJECT_DELETE"`, `"OBJECT_ARCHIVE"`
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>notification_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ID of the created notification.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>object_<wbr>name_<wbr>prefix</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies a prefix path filter for this notification config. Cloud Storage will only send notifications for objects in this bucket whose names begin with the specified prefix.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>payload_<wbr>format</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The desired content of the Payload. One of `"JSON_API_V1"` or `"NONE"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>self_<wbr>link</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>topic</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Cloud PubSub topic to which this subscription publishes. Expects either the 
topic name, assumed to belong to the default GCP provider project, or the project-level name,
i.e. `projects/my-gcp-project/topics/my-topic` or `my-topic`. If the project is not set in the provider,
you will need to use the project-level name.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-gcp">https://github.com/pulumi/pulumi-gcp</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd></dl>
