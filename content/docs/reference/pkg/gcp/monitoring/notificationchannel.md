
---
title: "NotificationChannel"
block_external_search_index: true
---



A NotificationChannel is a medium through which an alert is delivered
when a policy violation is detected. Examples of channels include email, SMS,
and third-party messaging applications. Fields containing sensitive information
like authentication tokens or contact info are only partially populated on retrieval.

Notification Channels are designed to be flexible and are made up of a supported `type`
and labels to configure that channel. Each `type` has specific labels that need to be
present for that channel to be correctly configured. The labels that are required to be
present for one channel `type` are often different than those required for another.
Due to these loose constraints it's often best to set up a channel through the UI
and import it to the provider when setting up a brand new channel type to determine which
labels are required.

A list of supported channels per project the `list` endpoint can be
accessed programmatically or through the api explorer at  https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/list .
This provides the channel type and all of the required labels that must be passed.


To get more information about NotificationChannel, see:

* [API documentation](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannels)
* How-to Guides
    * [Notification Options](https://cloud.google.com/monitoring/support/notification-options)
    * [Monitoring API Documentation](https://cloud.google.com/monitoring/api/v3/)

## Example Usage - Notification Channel Basic


```typescript
import * as pulumi from "@pulumi/pulumi";
import * as gcp from "@pulumi/gcp";

const basic = new gcp.monitoring.NotificationChannel("basic", {
    displayName: "Test Notification Channel",
    labels: {
        email_address: "fake_email@blahblah.com",
    },
    type: "email",
});
```
## Example Usage - Notification Channel Sensitive


```typescript
import * as pulumi from "@pulumi/pulumi";
import * as gcp from "@pulumi/gcp";

const defaultNotificationChannel = new gcp.monitoring.NotificationChannel("default", {
    displayName: "Test Slack Channel",
    labels: {
        channel_name: "#foobar",
    },
    sensitiveLabels: {
        authToken: "one",
    },
    type: "slack",
});
```



## Create a NotificationChannel Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/monitoring/#NotificationChannel">NotificationChannel</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/monitoring/#NotificationChannelArgs">NotificationChannelArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">NotificationChannel</span><span class="p">(resource_name, opts=None, </span>description=None<span class="p">, </span>display_name=None<span class="p">, </span>enabled=None<span class="p">, </span>labels=None<span class="p">, </span>project=None<span class="p">, </span>sensitive_labels=None<span class="p">, </span>type=None<span class="p">, </span>user_labels=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewNotificationChannel<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/monitoring?tab=doc#NotificationChannelArgs">NotificationChannelArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/monitoring?tab=doc#NotificationChannel">NotificationChannel</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Monitoring.NotificationChannel.html">NotificationChannel</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Monitoring.NotificationChannelArgs.html">NotificationChannelArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}An optional human-readable name for this notification channel. It is recommended that you specify a non-empty and unique
name in order to make it easier to identify the channels in your project, though this is not enforced. The display name
is limited to 512 Unicode characters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The type of the notification channel. This field matches the value of the NotificationChannelDescriptor.type field. See
https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/list to get the list of
valid values such as "email", "slack", etc...
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}An optional human-readable description of this notification channel. This description may provide additional details,
beyond the display name, for the channel. This may not exceed 1024 Unicode characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether notifications are forwarded to the described channel. This makes it possible to disable delivery of
notifications to a particular channel without removing the channel from all alerting policies that reference the
channel. This is a more convenient approach when the change is temporary and you want to receive notifications from the
same set of alerting policies on the channel at some point in the future.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}Configuration fields that define the channel and its behavior. The permissible and required labels are specified in the
NotificationChannelDescriptor corresponding to the type field. Labels with sensitive data are obfuscated by the API and
therefore Terraform cannot determine if there are upstream changes to these fields. They can also be configured via the
sensitive_labels block, but cannot be configured in both places.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sensitive<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#notificationchannelsensitivelabels">Notification<wbr>Channel<wbr>Sensitive<wbr>Labels<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Different notification type behaviors are configured primarily using the the 'labels' field on this resource. This block
contains the labels which contain secrets or passwords so that they can be marked sensitive and hidden from plan output.
The name of the field, eg: password, will be the key in the 'labels' map in the api request. Credentials may not be
specified in both locations and will cause an error. Changing from one location to a different credential configuration
in the config will require an apply to update state.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>User<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}User-supplied key/value data that does not need to conform to the corresponding NotificationChannelDescriptor's schema,
unlike the labels field. This field is intended to be used for organizing and identifying the NotificationChannel
objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes,
whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must
begin with a letter.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}An optional human-readable name for this notification channel. It is recommended that you specify a non-empty and unique
name in order to make it easier to identify the channels in your project, though this is not enforced. The display name
is limited to 512 Unicode characters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of the notification channel. This field matches the value of the NotificationChannelDescriptor.type field. See
https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/list to get the list of
valid values such as "email", "slack", etc...
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}An optional human-readable description of this notification channel. This description may provide additional details,
beyond the display name, for the channel. This may not exceed 1024 Unicode characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether notifications are forwarded to the described channel. This makes it possible to disable delivery of
notifications to a particular channel without removing the channel from all alerting policies that reference the
channel. This is a more convenient approach when the change is temporary and you want to receive notifications from the
same set of alerting policies on the channel at some point in the future.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Configuration fields that define the channel and its behavior. The permissible and required labels are specified in the
NotificationChannelDescriptor corresponding to the type field. Labels with sensitive data are obfuscated by the API and
therefore Terraform cannot determine if there are upstream changes to these fields. They can also be configured via the
sensitive_labels block, but cannot be configured in both places.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sensitive<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#notificationchannelsensitivelabels">Notification<wbr>Channel<wbr>Sensitive<wbr>Labels</a></span>
    </dt>
    <dd>{{% md %}}Different notification type behaviors are configured primarily using the the 'labels' field on this resource. This block
contains the labels which contain secrets or passwords so that they can be marked sensitive and hidden from plan output.
The name of the field, eg: password, will be the key in the 'labels' map in the api request. Credentials may not be
specified in both locations and will cause an error. Changing from one location to a different credential configuration
in the config will require an apply to update state.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>User<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}User-supplied key/value data that does not need to conform to the corresponding NotificationChannelDescriptor's schema,
unlike the labels field. This field is intended to be used for organizing and identifying the NotificationChannel
objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes,
whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must
begin with a letter.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}An optional human-readable name for this notification channel. It is recommended that you specify a non-empty and unique
name in order to make it easier to identify the channels in your project, though this is not enforced. The display name
is limited to 512 Unicode characters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of the notification channel. This field matches the value of the NotificationChannelDescriptor.type field. See
https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/list to get the list of
valid values such as "email", "slack", etc...
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}An optional human-readable description of this notification channel. This description may provide additional details,
beyond the display name, for the channel. This may not exceed 1024 Unicode characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Whether notifications are forwarded to the described channel. This makes it possible to disable delivery of
notifications to a particular channel without removing the channel from all alerting policies that reference the
channel. This is a more convenient approach when the change is temporary and you want to receive notifications from the
same set of alerting policies on the channel at some point in the future.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}Configuration fields that define the channel and its behavior. The permissible and required labels are specified in the
NotificationChannelDescriptor corresponding to the type field. Labels with sensitive data are obfuscated by the API and
therefore Terraform cannot determine if there are upstream changes to these fields. They can also be configured via the
sensitive_labels block, but cannot be configured in both places.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sensitive<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#notificationchannelsensitivelabels">Notification<wbr>Channel<wbr>Sensitive<wbr>Labels</a></span>
    </dt>
    <dd>{{% md %}}Different notification type behaviors are configured primarily using the the 'labels' field on this resource. This block
contains the labels which contain secrets or passwords so that they can be marked sensitive and hidden from plan output.
The name of the field, eg: password, will be the key in the 'labels' map in the api request. Credentials may not be
specified in both locations and will cause an error. Changing from one location to a different credential configuration
in the config will require an apply to update state.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>user<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}User-supplied key/value data that does not need to conform to the corresponding NotificationChannelDescriptor's schema,
unlike the labels field. This field is intended to be used for organizing and identifying the NotificationChannel
objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes,
whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must
begin with a letter.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>display_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}An optional human-readable name for this notification channel. It is recommended that you specify a non-empty and unique
name in order to make it easier to identify the channels in your project, though this is not enforced. The display name
is limited to 512 Unicode characters.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The type of the notification channel. This field matches the value of the NotificationChannelDescriptor.type field. See
https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/list to get the list of
valid values such as "email", "slack", etc...
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}An optional human-readable description of this notification channel. This description may provide additional details,
beyond the display name, for the channel. This may not exceed 1024 Unicode characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether notifications are forwarded to the described channel. This makes it possible to disable delivery of
notifications to a particular channel without removing the channel from all alerting policies that reference the
channel. This is a more convenient approach when the change is temporary and you want to receive notifications from the
same set of alerting policies on the channel at some point in the future.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Configuration fields that define the channel and its behavior. The permissible and required labels are specified in the
NotificationChannelDescriptor corresponding to the type field. Labels with sensitive data are obfuscated by the API and
therefore Terraform cannot determine if there are upstream changes to these fields. They can also be configured via the
sensitive_labels block, but cannot be configured in both places.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sensitive_<wbr>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#notificationchannelsensitivelabels">Dict[Notification<wbr>Channel<wbr>Sensitive<wbr>Labels]</a></span>
    </dt>
    <dd>{{% md %}}Different notification type behaviors are configured primarily using the the 'labels' field on this resource. This block
contains the labels which contain secrets or passwords so that they can be marked sensitive and hidden from plan output.
The name of the field, eg: password, will be the key in the 'labels' map in the api request. Credentials may not be
specified in both locations and will cause an error. Changing from one location to a different credential configuration
in the config will require an apply to update state.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>user_<wbr>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}User-supplied key/value data that does not need to conform to the corresponding NotificationChannelDescriptor's schema,
unlike the labels field. This field is intended to be used for organizing and identifying the NotificationChannel
objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes,
whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must
begin with a letter.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## NotificationChannel Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The full REST resource name for this channel. The syntax is: projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID] The
[CHANNEL_ID] is automatically assigned by the server on creation.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Verification<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether this channel has been verified or not. On a ListNotificationChannels or GetNotificationChannel
operation, this field is expected to be populated.If the value is UNVERIFIED, then it indicates that the channel is
non-functioning (it both requires verification and lacks verification); otherwise, it is assumed that the channel
works.If the channel is neither VERIFIED nor UNVERIFIED, it implies that the channel is of a type that does not require
verification or that this specific channel has been exempted from verification because it was created prior to
verification being required for channels of this type.This field cannot be modified using a standard
UpdateNotificationChannel operation. To change the value of this field, you must call VerifyNotificationChannel.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The full REST resource name for this channel. The syntax is: projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID] The
[CHANNEL_ID] is automatically assigned by the server on creation.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Verification<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether this channel has been verified or not. On a ListNotificationChannels or GetNotificationChannel
operation, this field is expected to be populated.If the value is UNVERIFIED, then it indicates that the channel is
non-functioning (it both requires verification and lacks verification); otherwise, it is assumed that the channel
works.If the channel is neither VERIFIED nor UNVERIFIED, it implies that the channel is of a type that does not require
verification or that this specific channel has been exempted from verification because it was created prior to
verification being required for channels of this type.This field cannot be modified using a standard
UpdateNotificationChannel operation. To change the value of this field, you must call VerifyNotificationChannel.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The full REST resource name for this channel. The syntax is: projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID] The
[CHANNEL_ID] is automatically assigned by the server on creation.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>verification<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether this channel has been verified or not. On a ListNotificationChannels or GetNotificationChannel
operation, this field is expected to be populated.If the value is UNVERIFIED, then it indicates that the channel is
non-functioning (it both requires verification and lacks verification); otherwise, it is assumed that the channel
works.If the channel is neither VERIFIED nor UNVERIFIED, it implies that the channel is of a type that does not require
verification or that this specific channel has been exempted from verification because it was created prior to
verification being required for channels of this type.This field cannot be modified using a standard
UpdateNotificationChannel operation. To change the value of this field, you must call VerifyNotificationChannel.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The full REST resource name for this channel. The syntax is: projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID] The
[CHANNEL_ID] is automatically assigned by the server on creation.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>verification_<wbr>status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether this channel has been verified or not. On a ListNotificationChannels or GetNotificationChannel
operation, this field is expected to be populated.If the value is UNVERIFIED, then it indicates that the channel is
non-functioning (it both requires verification and lacks verification); otherwise, it is assumed that the channel
works.If the channel is neither VERIFIED nor UNVERIFIED, it implies that the channel is of a type that does not require
verification or that this specific channel has been exempted from verification because it was created prior to
verification being required for channels of this type.This field cannot be modified using a standard
UpdateNotificationChannel operation. To change the value of this field, you must call VerifyNotificationChannel.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing NotificationChannel Resource

Get an existing NotificationChannel resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/monitoring/#NotificationChannelState">NotificationChannelState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/monitoring/#NotificationChannel">NotificationChannel</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>description=None<span class="p">, </span>display_name=None<span class="p">, </span>enabled=None<span class="p">, </span>labels=None<span class="p">, </span>name=None<span class="p">, </span>project=None<span class="p">, </span>sensitive_labels=None<span class="p">, </span>type=None<span class="p">, </span>user_labels=None<span class="p">, </span>verification_status=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetNotificationChannel<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/monitoring?tab=doc#NotificationChannelState">NotificationChannelState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/monitoring?tab=doc#NotificationChannel">NotificationChannel</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Monitoring.NotificationChannel.html">NotificationChannel</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Monitoring.NotificationChannelState.html">NotificationChannelState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}An optional human-readable description of this notification channel. This description may provide additional details,
beyond the display name, for the channel. This may not exceed 1024 Unicode characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}An optional human-readable name for this notification channel. It is recommended that you specify a non-empty and unique
name in order to make it easier to identify the channels in your project, though this is not enforced. The display name
is limited to 512 Unicode characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether notifications are forwarded to the described channel. This makes it possible to disable delivery of
notifications to a particular channel without removing the channel from all alerting policies that reference the
channel. This is a more convenient approach when the change is temporary and you want to receive notifications from the
same set of alerting policies on the channel at some point in the future.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}Configuration fields that define the channel and its behavior. The permissible and required labels are specified in the
NotificationChannelDescriptor corresponding to the type field. Labels with sensitive data are obfuscated by the API and
therefore Terraform cannot determine if there are upstream changes to these fields. They can also be configured via the
sensitive_labels block, but cannot be configured in both places.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The full REST resource name for this channel. The syntax is: projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID] The
[CHANNEL_ID] is automatically assigned by the server on creation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sensitive<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#notificationchannelsensitivelabels">Notification<wbr>Channel<wbr>Sensitive<wbr>Labels<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Different notification type behaviors are configured primarily using the the 'labels' field on this resource. This block
contains the labels which contain secrets or passwords so that they can be marked sensitive and hidden from plan output.
The name of the field, eg: password, will be the key in the 'labels' map in the api request. Credentials may not be
specified in both locations and will cause an error. Changing from one location to a different credential configuration
in the config will require an apply to update state.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The type of the notification channel. This field matches the value of the NotificationChannelDescriptor.type field. See
https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/list to get the list of
valid values such as "email", "slack", etc...
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>User<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}User-supplied key/value data that does not need to conform to the corresponding NotificationChannelDescriptor's schema,
unlike the labels field. This field is intended to be used for organizing and identifying the NotificationChannel
objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes,
whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must
begin with a letter.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Verification<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether this channel has been verified or not. On a ListNotificationChannels or GetNotificationChannel
operation, this field is expected to be populated.If the value is UNVERIFIED, then it indicates that the channel is
non-functioning (it both requires verification and lacks verification); otherwise, it is assumed that the channel
works.If the channel is neither VERIFIED nor UNVERIFIED, it implies that the channel is of a type that does not require
verification or that this specific channel has been exempted from verification because it was created prior to
verification being required for channels of this type.This field cannot be modified using a standard
UpdateNotificationChannel operation. To change the value of this field, you must call VerifyNotificationChannel.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}An optional human-readable description of this notification channel. This description may provide additional details,
beyond the display name, for the channel. This may not exceed 1024 Unicode characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}An optional human-readable name for this notification channel. It is recommended that you specify a non-empty and unique
name in order to make it easier to identify the channels in your project, though this is not enforced. The display name
is limited to 512 Unicode characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether notifications are forwarded to the described channel. This makes it possible to disable delivery of
notifications to a particular channel without removing the channel from all alerting policies that reference the
channel. This is a more convenient approach when the change is temporary and you want to receive notifications from the
same set of alerting policies on the channel at some point in the future.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}Configuration fields that define the channel and its behavior. The permissible and required labels are specified in the
NotificationChannelDescriptor corresponding to the type field. Labels with sensitive data are obfuscated by the API and
therefore Terraform cannot determine if there are upstream changes to these fields. They can also be configured via the
sensitive_labels block, but cannot be configured in both places.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The full REST resource name for this channel. The syntax is: projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID] The
[CHANNEL_ID] is automatically assigned by the server on creation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sensitive<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#notificationchannelsensitivelabels">Notification<wbr>Channel<wbr>Sensitive<wbr>Labels</a></span>
    </dt>
    <dd>{{% md %}}Different notification type behaviors are configured primarily using the the 'labels' field on this resource. This block
contains the labels which contain secrets or passwords so that they can be marked sensitive and hidden from plan output.
The name of the field, eg: password, will be the key in the 'labels' map in the api request. Credentials may not be
specified in both locations and will cause an error. Changing from one location to a different credential configuration
in the config will require an apply to update state.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of the notification channel. This field matches the value of the NotificationChannelDescriptor.type field. See
https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/list to get the list of
valid values such as "email", "slack", etc...
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>User<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}User-supplied key/value data that does not need to conform to the corresponding NotificationChannelDescriptor's schema,
unlike the labels field. This field is intended to be used for organizing and identifying the NotificationChannel
objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes,
whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must
begin with a letter.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Verification<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether this channel has been verified or not. On a ListNotificationChannels or GetNotificationChannel
operation, this field is expected to be populated.If the value is UNVERIFIED, then it indicates that the channel is
non-functioning (it both requires verification and lacks verification); otherwise, it is assumed that the channel
works.If the channel is neither VERIFIED nor UNVERIFIED, it implies that the channel is of a type that does not require
verification or that this specific channel has been exempted from verification because it was created prior to
verification being required for channels of this type.This field cannot be modified using a standard
UpdateNotificationChannel operation. To change the value of this field, you must call VerifyNotificationChannel.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}An optional human-readable description of this notification channel. This description may provide additional details,
beyond the display name, for the channel. This may not exceed 1024 Unicode characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}An optional human-readable name for this notification channel. It is recommended that you specify a non-empty and unique
name in order to make it easier to identify the channels in your project, though this is not enforced. The display name
is limited to 512 Unicode characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Whether notifications are forwarded to the described channel. This makes it possible to disable delivery of
notifications to a particular channel without removing the channel from all alerting policies that reference the
channel. This is a more convenient approach when the change is temporary and you want to receive notifications from the
same set of alerting policies on the channel at some point in the future.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}Configuration fields that define the channel and its behavior. The permissible and required labels are specified in the
NotificationChannelDescriptor corresponding to the type field. Labels with sensitive data are obfuscated by the API and
therefore Terraform cannot determine if there are upstream changes to these fields. They can also be configured via the
sensitive_labels block, but cannot be configured in both places.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The full REST resource name for this channel. The syntax is: projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID] The
[CHANNEL_ID] is automatically assigned by the server on creation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sensitive<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#notificationchannelsensitivelabels">Notification<wbr>Channel<wbr>Sensitive<wbr>Labels</a></span>
    </dt>
    <dd>{{% md %}}Different notification type behaviors are configured primarily using the the 'labels' field on this resource. This block
contains the labels which contain secrets or passwords so that they can be marked sensitive and hidden from plan output.
The name of the field, eg: password, will be the key in the 'labels' map in the api request. Credentials may not be
specified in both locations and will cause an error. Changing from one location to a different credential configuration
in the config will require an apply to update state.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The type of the notification channel. This field matches the value of the NotificationChannelDescriptor.type field. See
https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/list to get the list of
valid values such as "email", "slack", etc...
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>user<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}User-supplied key/value data that does not need to conform to the corresponding NotificationChannelDescriptor's schema,
unlike the labels field. This field is intended to be used for organizing and identifying the NotificationChannel
objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes,
whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must
begin with a letter.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>verification<wbr>Status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether this channel has been verified or not. On a ListNotificationChannels or GetNotificationChannel
operation, this field is expected to be populated.If the value is UNVERIFIED, then it indicates that the channel is
non-functioning (it both requires verification and lacks verification); otherwise, it is assumed that the channel
works.If the channel is neither VERIFIED nor UNVERIFIED, it implies that the channel is of a type that does not require
verification or that this specific channel has been exempted from verification because it was created prior to
verification being required for channels of this type.This field cannot be modified using a standard
UpdateNotificationChannel operation. To change the value of this field, you must call VerifyNotificationChannel.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}An optional human-readable description of this notification channel. This description may provide additional details,
beyond the display name, for the channel. This may not exceed 1024 Unicode characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>display_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}An optional human-readable name for this notification channel. It is recommended that you specify a non-empty and unique
name in order to make it easier to identify the channels in your project, though this is not enforced. The display name
is limited to 512 Unicode characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Whether notifications are forwarded to the described channel. This makes it possible to disable delivery of
notifications to a particular channel without removing the channel from all alerting policies that reference the
channel. This is a more convenient approach when the change is temporary and you want to receive notifications from the
same set of alerting policies on the channel at some point in the future.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}Configuration fields that define the channel and its behavior. The permissible and required labels are specified in the
NotificationChannelDescriptor corresponding to the type field. Labels with sensitive data are obfuscated by the API and
therefore Terraform cannot determine if there are upstream changes to these fields. They can also be configured via the
sensitive_labels block, but cannot be configured in both places.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The full REST resource name for this channel. The syntax is: projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID] The
[CHANNEL_ID] is automatically assigned by the server on creation.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sensitive_<wbr>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#notificationchannelsensitivelabels">Dict[Notification<wbr>Channel<wbr>Sensitive<wbr>Labels]</a></span>
    </dt>
    <dd>{{% md %}}Different notification type behaviors are configured primarily using the the 'labels' field on this resource. This block
contains the labels which contain secrets or passwords so that they can be marked sensitive and hidden from plan output.
The name of the field, eg: password, will be the key in the 'labels' map in the api request. Credentials may not be
specified in both locations and will cause an error. Changing from one location to a different credential configuration
in the config will require an apply to update state.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The type of the notification channel. This field matches the value of the NotificationChannelDescriptor.type field. See
https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.notificationChannelDescriptors/list to get the list of
valid values such as "email", "slack", etc...
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>user_<wbr>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}User-supplied key/value data that does not need to conform to the corresponding NotificationChannelDescriptor's schema,
unlike the labels field. This field is intended to be used for organizing and identifying the NotificationChannel
objects.The field can contain up to 64 entries. Each key and value is limited to 63 Unicode characters or 128 bytes,
whichever is smaller. Labels and values can contain only lowercase letters, numerals, underscores, and dashes. Keys must
begin with a letter.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>verification_<wbr>status</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Indicates whether this channel has been verified or not. On a ListNotificationChannels or GetNotificationChannel
operation, this field is expected to be populated.If the value is UNVERIFIED, then it indicates that the channel is
non-functioning (it both requires verification and lacks verification); otherwise, it is assumed that the channel
works.If the channel is neither VERIFIED nor UNVERIFIED, it implies that the channel is of a type that does not require
verification or that this specific channel has been exempted from verification because it was created prior to
verification being required for channels of this type.This field cannot be modified using a standard
UpdateNotificationChannel operation. To change the value of this field, you must call VerifyNotificationChannel.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Notification<wbr>Channel<wbr>Sensitive<wbr>Labels</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#NotificationChannelSensitiveLabels">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#NotificationChannelSensitiveLabels">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/monitoring?tab=doc#NotificationChannelSensitiveLabelsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/monitoring?tab=doc#NotificationChannelSensitiveLabelsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Auth<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Auth<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>auth<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>auth<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>password</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service<wbr>Key</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
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
    <dt>Notes</dt>
	<dd>This Pulumi package is based on the [`google-beta` Terraform Provider](https://github.com/terraform-providers/terraform-provider-google-beta).</dd>
</dl>

