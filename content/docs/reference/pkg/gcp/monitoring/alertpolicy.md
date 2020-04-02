
---
title: "AlertPolicy"
block_external_search_index: true
---

A description of the conditions under which some aspect of your system is
considered to be "unhealthy" and the ways to notify people or services
about this state.


To get more information about AlertPolicy, see:

* [API documentation](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies)
* How-to Guides
    * [Official Documentation](https://cloud.google.com/monitoring/alerts/)

> This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/monitoring_alert_policy.html.markdown.



## Create a AlertPolicy Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/monitoring/#AlertPolicy">AlertPolicy</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/monitoring/#AlertPolicyArgs">AlertPolicyArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">AlertPolicy</span><span class="p">(resource_name, opts=None, </span>combiner=None<span class="p">, </span>conditions=None<span class="p">, </span>display_name=None<span class="p">, </span>documentation=None<span class="p">, </span>enabled=None<span class="p">, </span>notification_channels=None<span class="p">, </span>project=None<span class="p">, </span>user_labels=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewAlertPolicy<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#AlertPolicyArgs">AlertPolicyArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#AlertPolicy">AlertPolicy</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Monitoring.AlertPolicy.html">AlertPolicy</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Monitoring.AlertPolicyArgs.html">AlertPolicyArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Combiner</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}How to combine the results of multiple conditions to determine if an incident should be opened.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Conditions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicycondition">List&lt;Alert<wbr>Policy<wbr>Condition<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of conditions for the policy. The conditions are combined by AND or OR according to the combiner field. If the
combined conditions evaluate to true, then an incident is created. A policy can have from one to six conditions.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion,
don't use the same display name for multiple policies in the same project. The name is limited to 512 Unicode
characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Documentation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicydocumentation">Alert<wbr>Policy<wbr>Documentation<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion,
don't use the same display name for multiple policies in the same project. The name is limited to 512 Unicode
characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether or not the policy is enabled. The default is true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Notification<wbr>Channels</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Identifies the notification channels to which notifications should be sent when incidents are opened or closed or when
new violations occur on an already opened incident. Each element of this array corresponds to the name field in each of
the NotificationChannel objects that are returned from the notificationChannels.list method. The syntax of the entries
in this field is 'projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID]'
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
        <span>User<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}This field is intended to be used for organizing and identifying the AlertPolicy objects.The field can contain up to 64
entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values
can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Combiner</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}How to combine the results of multiple conditions to determine if an incident should be opened.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Conditions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicycondition">[]Alert<wbr>Policy<wbr>Condition</a></span>
    </dt>
    <dd>{{% md %}}A list of conditions for the policy. The conditions are combined by AND or OR according to the combiner field. If the
combined conditions evaluate to true, then an incident is created. A policy can have from one to six conditions.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion,
don't use the same display name for multiple policies in the same project. The name is limited to 512 Unicode
characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Documentation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicydocumentation">*Alert<wbr>Policy<wbr>Documentation</a></span>
    </dt>
    <dd>{{% md %}}A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion,
don't use the same display name for multiple policies in the same project. The name is limited to 512 Unicode
characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether or not the policy is enabled. The default is true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Notification<wbr>Channels</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Identifies the notification channels to which notifications should be sent when incidents are opened or closed or when
new violations occur on an already opened incident. Each element of this array corresponds to the name field in each of
the NotificationChannel objects that are returned from the notificationChannels.list method. The syntax of the entries
in this field is 'projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID]'
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
        <span>User<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}This field is intended to be used for organizing and identifying the AlertPolicy objects.The field can contain up to 64
entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values
can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>combiner</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}How to combine the results of multiple conditions to determine if an incident should be opened.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>conditions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicycondition">Alert<wbr>Policy<wbr>Condition[]</a></span>
    </dt>
    <dd>{{% md %}}A list of conditions for the policy. The conditions are combined by AND or OR according to the combiner field. If the
combined conditions evaluate to true, then an incident is created. A policy can have from one to six conditions.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion,
don't use the same display name for multiple policies in the same project. The name is limited to 512 Unicode
characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>documentation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicydocumentation">Alert<wbr>Policy<wbr>Documentation?</a></span>
    </dt>
    <dd>{{% md %}}A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion,
don't use the same display name for multiple policies in the same project. The name is limited to 512 Unicode
characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether or not the policy is enabled. The default is true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>notification<wbr>Channels</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Identifies the notification channels to which notifications should be sent when incidents are opened or closed or when
new violations occur on an already opened incident. Each element of this array corresponds to the name field in each of
the NotificationChannel objects that are returned from the notificationChannels.list method. The syntax of the entries
in this field is 'projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID]'
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
        <span>user<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}This field is intended to be used for organizing and identifying the AlertPolicy objects.The field can contain up to 64
entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values
can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>combiner</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}How to combine the results of multiple conditions to determine if an incident should be opened.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>conditions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicycondition">List[Alert<wbr>Policy<wbr>Condition]</a></span>
    </dt>
    <dd>{{% md %}}A list of conditions for the policy. The conditions are combined by AND or OR according to the combiner field. If the
combined conditions evaluate to true, then an incident is created. A policy can have from one to six conditions.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>display_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion,
don't use the same display name for multiple policies in the same project. The name is limited to 512 Unicode
characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>documentation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicydocumentation">Dict[Alert<wbr>Policy<wbr>Documentation]</a></span>
    </dt>
    <dd>{{% md %}}A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion,
don't use the same display name for multiple policies in the same project. The name is limited to 512 Unicode
characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether or not the policy is enabled. The default is true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>notification_<wbr>channels</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Identifies the notification channels to which notifications should be sent when incidents are opened or closed or when
new violations occur on an already opened incident. Each element of this array corresponds to the name field in each of
the NotificationChannel objects that are returned from the notificationChannels.list method. The syntax of the entries
in this field is 'projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID]'
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
        <span>user_<wbr>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}This field is intended to be used for organizing and identifying the AlertPolicy objects.The field can contain up to 64
entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values
can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## AlertPolicy Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Combiner</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}How to combine the results of multiple conditions to determine if an incident should be opened.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Conditions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicycondition">List&lt;Alert<wbr>Policy<wbr>Condition&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of conditions for the policy. The conditions are combined by AND or OR according to the combiner field. If the
combined conditions evaluate to true, then an incident is created. A policy can have from one to six conditions.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Creation<wbr>Record</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicycreationrecord">Alert<wbr>Policy<wbr>Creation<wbr>Record</a></span>
    </dt>
    <dd>{{% md %}}A read-only record of the creation of the alerting policy. If provided in a call to create or update, this field will be
ignored.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion,
don't use the same display name for multiple policies in the same project. The name is limited to 512 Unicode
characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Documentation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicydocumentation">Alert<wbr>Policy<wbr>Documentation?</a></span>
    </dt>
    <dd>{{% md %}}A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion,
don't use the same display name for multiple policies in the same project. The name is limited to 512 Unicode
characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether or not the policy is enabled. The default is true.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The unique resource name for this policy. Its syntax is: projects/[PROJECT_ID]/alertPolicies/[ALERT_POLICY_ID]
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Notification<wbr>Channels</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Identifies the notification channels to which notifications should be sent when incidents are opened or closed or when
new violations occur on an already opened incident. Each element of this array corresponds to the name field in each of
the NotificationChannel objects that are returned from the notificationChannels.list method. The syntax of the entries
in this field is 'projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID]'
{{% /md %}}</dd>

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
        <span>User<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}This field is intended to be used for organizing and identifying the AlertPolicy objects.The field can contain up to 64
entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values
can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Combiner</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}How to combine the results of multiple conditions to determine if an incident should be opened.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Conditions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicycondition">[]Alert<wbr>Policy<wbr>Condition</a></span>
    </dt>
    <dd>{{% md %}}A list of conditions for the policy. The conditions are combined by AND or OR according to the combiner field. If the
combined conditions evaluate to true, then an incident is created. A policy can have from one to six conditions.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Creation<wbr>Record</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicycreationrecord">Alert<wbr>Policy<wbr>Creation<wbr>Record</a></span>
    </dt>
    <dd>{{% md %}}A read-only record of the creation of the alerting policy. If provided in a call to create or update, this field will be
ignored.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion,
don't use the same display name for multiple policies in the same project. The name is limited to 512 Unicode
characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Documentation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicydocumentation">*Alert<wbr>Policy<wbr>Documentation</a></span>
    </dt>
    <dd>{{% md %}}A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion,
don't use the same display name for multiple policies in the same project. The name is limited to 512 Unicode
characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether or not the policy is enabled. The default is true.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The unique resource name for this policy. Its syntax is: projects/[PROJECT_ID]/alertPolicies/[ALERT_POLICY_ID]
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Notification<wbr>Channels</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Identifies the notification channels to which notifications should be sent when incidents are opened or closed or when
new violations occur on an already opened incident. Each element of this array corresponds to the name field in each of
the NotificationChannel objects that are returned from the notificationChannels.list method. The syntax of the entries
in this field is 'projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID]'
{{% /md %}}</dd>

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
        <span>User<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}This field is intended to be used for organizing and identifying the AlertPolicy objects.The field can contain up to 64
entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values
can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>combiner</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}How to combine the results of multiple conditions to determine if an incident should be opened.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>conditions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicycondition">Alert<wbr>Policy<wbr>Condition[]</a></span>
    </dt>
    <dd>{{% md %}}A list of conditions for the policy. The conditions are combined by AND or OR according to the combiner field. If the
combined conditions evaluate to true, then an incident is created. A policy can have from one to six conditions.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>creation<wbr>Record</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicycreationrecord">Alert<wbr>Policy<wbr>Creation<wbr>Record</a></span>
    </dt>
    <dd>{{% md %}}A read-only record of the creation of the alerting policy. If provided in a call to create or update, this field will be
ignored.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion,
don't use the same display name for multiple policies in the same project. The name is limited to 512 Unicode
characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>documentation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicydocumentation">Alert<wbr>Policy<wbr>Documentation?</a></span>
    </dt>
    <dd>{{% md %}}A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion,
don't use the same display name for multiple policies in the same project. The name is limited to 512 Unicode
characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether or not the policy is enabled. The default is true.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The unique resource name for this policy. Its syntax is: projects/[PROJECT_ID]/alertPolicies/[ALERT_POLICY_ID]
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>notification<wbr>Channels</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Identifies the notification channels to which notifications should be sent when incidents are opened or closed or when
new violations occur on an already opened incident. Each element of this array corresponds to the name field in each of
the NotificationChannel objects that are returned from the notificationChannels.list method. The syntax of the entries
in this field is 'projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID]'
{{% /md %}}</dd>

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
        <span>user<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}This field is intended to be used for organizing and identifying the AlertPolicy objects.The field can contain up to 64
entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values
can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>combiner</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}How to combine the results of multiple conditions to determine if an incident should be opened.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>conditions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicycondition">List[Alert<wbr>Policy<wbr>Condition]</a></span>
    </dt>
    <dd>{{% md %}}A list of conditions for the policy. The conditions are combined by AND or OR according to the combiner field. If the
combined conditions evaluate to true, then an incident is created. A policy can have from one to six conditions.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>creation_<wbr>record</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicycreationrecord">Dict[Alert<wbr>Policy<wbr>Creation<wbr>Record]</a></span>
    </dt>
    <dd>{{% md %}}A read-only record of the creation of the alerting policy. If provided in a call to create or update, this field will be
ignored.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>display_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion,
don't use the same display name for multiple policies in the same project. The name is limited to 512 Unicode
characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>documentation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicydocumentation">Dict[Alert<wbr>Policy<wbr>Documentation]</a></span>
    </dt>
    <dd>{{% md %}}A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion,
don't use the same display name for multiple policies in the same project. The name is limited to 512 Unicode
characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether or not the policy is enabled. The default is true.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The unique resource name for this policy. Its syntax is: projects/[PROJECT_ID]/alertPolicies/[ALERT_POLICY_ID]
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>notification_<wbr>channels</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Identifies the notification channels to which notifications should be sent when incidents are opened or closed or when
new violations occur on an already opened incident. Each element of this array corresponds to the name field in each of
the NotificationChannel objects that are returned from the notificationChannels.list method. The syntax of the entries
in this field is 'projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID]'
{{% /md %}}</dd>

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
        <span>user_<wbr>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}This field is intended to be used for organizing and identifying the AlertPolicy objects.The field can contain up to 64
entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values
can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing AlertPolicy Resource

Get an existing AlertPolicy resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/monitoring/#AlertPolicyState">AlertPolicyState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/monitoring/#AlertPolicy">AlertPolicy</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>combiner=None<span class="p">, </span>conditions=None<span class="p">, </span>creation_record=None<span class="p">, </span>display_name=None<span class="p">, </span>documentation=None<span class="p">, </span>enabled=None<span class="p">, </span>name=None<span class="p">, </span>notification_channels=None<span class="p">, </span>project=None<span class="p">, </span>user_labels=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetAlertPolicy<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#AlertPolicyState">AlertPolicyState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#AlertPolicy">AlertPolicy</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Monitoring.AlertPolicy.html">AlertPolicy</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Monitoring.AlertPolicyState.html">AlertPolicyState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Combiner</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}How to combine the results of multiple conditions to determine if an incident should be opened.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Conditions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicycondition">List&lt;Alert<wbr>Policy<wbr>Condition<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}A list of conditions for the policy. The conditions are combined by AND or OR according to the combiner field. If the
combined conditions evaluate to true, then an incident is created. A policy can have from one to six conditions.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Creation<wbr>Record</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicycreationrecord">Alert<wbr>Policy<wbr>Creation<wbr>Record<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A read-only record of the creation of the alerting policy. If provided in a call to create or update, this field will be
ignored.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion,
don't use the same display name for multiple policies in the same project. The name is limited to 512 Unicode
characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Documentation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicydocumentation">Alert<wbr>Policy<wbr>Documentation<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion,
don't use the same display name for multiple policies in the same project. The name is limited to 512 Unicode
characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether or not the policy is enabled. The default is true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The unique resource name for this policy. Its syntax is: projects/[PROJECT_ID]/alertPolicies/[ALERT_POLICY_ID]
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Notification<wbr>Channels</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}Identifies the notification channels to which notifications should be sent when incidents are opened or closed or when
new violations occur on an already opened incident. Each element of this array corresponds to the name field in each of
the NotificationChannel objects that are returned from the notificationChannels.list method. The syntax of the entries
in this field is 'projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID]'
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
        <span>User<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}This field is intended to be used for organizing and identifying the AlertPolicy objects.The field can contain up to 64
entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values
can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Combiner</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}How to combine the results of multiple conditions to determine if an incident should be opened.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Conditions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicycondition">[]Alert<wbr>Policy<wbr>Condition</a></span>
    </dt>
    <dd>{{% md %}}A list of conditions for the policy. The conditions are combined by AND or OR according to the combiner field. If the
combined conditions evaluate to true, then an incident is created. A policy can have from one to six conditions.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Creation<wbr>Record</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicycreationrecord">*Alert<wbr>Policy<wbr>Creation<wbr>Record</a></span>
    </dt>
    <dd>{{% md %}}A read-only record of the creation of the alerting policy. If provided in a call to create or update, this field will be
ignored.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion,
don't use the same display name for multiple policies in the same project. The name is limited to 512 Unicode
characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Documentation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicydocumentation">*Alert<wbr>Policy<wbr>Documentation</a></span>
    </dt>
    <dd>{{% md %}}A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion,
don't use the same display name for multiple policies in the same project. The name is limited to 512 Unicode
characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether or not the policy is enabled. The default is true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The unique resource name for this policy. Its syntax is: projects/[PROJECT_ID]/alertPolicies/[ALERT_POLICY_ID]
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Notification<wbr>Channels</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}Identifies the notification channels to which notifications should be sent when incidents are opened or closed or when
new violations occur on an already opened incident. Each element of this array corresponds to the name field in each of
the NotificationChannel objects that are returned from the notificationChannels.list method. The syntax of the entries
in this field is 'projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID]'
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
        <span>User<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}This field is intended to be used for organizing and identifying the AlertPolicy objects.The field can contain up to 64
entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values
can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>combiner</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}How to combine the results of multiple conditions to determine if an incident should be opened.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>conditions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicycondition">Alert<wbr>Policy<wbr>Condition[]?</a></span>
    </dt>
    <dd>{{% md %}}A list of conditions for the policy. The conditions are combined by AND or OR according to the combiner field. If the
combined conditions evaluate to true, then an incident is created. A policy can have from one to six conditions.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>creation<wbr>Record</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicycreationrecord">Alert<wbr>Policy<wbr>Creation<wbr>Record?</a></span>
    </dt>
    <dd>{{% md %}}A read-only record of the creation of the alerting policy. If provided in a call to create or update, this field will be
ignored.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion,
don't use the same display name for multiple policies in the same project. The name is limited to 512 Unicode
characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>documentation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicydocumentation">Alert<wbr>Policy<wbr>Documentation?</a></span>
    </dt>
    <dd>{{% md %}}A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion,
don't use the same display name for multiple policies in the same project. The name is limited to 512 Unicode
characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether or not the policy is enabled. The default is true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The unique resource name for this policy. Its syntax is: projects/[PROJECT_ID]/alertPolicies/[ALERT_POLICY_ID]
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>notification<wbr>Channels</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}Identifies the notification channels to which notifications should be sent when incidents are opened or closed or when
new violations occur on an already opened incident. Each element of this array corresponds to the name field in each of
the NotificationChannel objects that are returned from the notificationChannels.list method. The syntax of the entries
in this field is 'projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID]'
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
        <span>user<wbr>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}This field is intended to be used for organizing and identifying the AlertPolicy objects.The field can contain up to 64
entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values
can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>combiner</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}How to combine the results of multiple conditions to determine if an incident should be opened.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>conditions</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicycondition">List[Alert<wbr>Policy<wbr>Condition]</a></span>
    </dt>
    <dd>{{% md %}}A list of conditions for the policy. The conditions are combined by AND or OR according to the combiner field. If the
combined conditions evaluate to true, then an incident is created. A policy can have from one to six conditions.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>creation_<wbr>record</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicycreationrecord">Dict[Alert<wbr>Policy<wbr>Creation<wbr>Record]</a></span>
    </dt>
    <dd>{{% md %}}A read-only record of the creation of the alerting policy. If provided in a call to create or update, this field will be
ignored.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>display_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion,
don't use the same display name for multiple policies in the same project. The name is limited to 512 Unicode
characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>documentation</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicydocumentation">Dict[Alert<wbr>Policy<wbr>Documentation]</a></span>
    </dt>
    <dd>{{% md %}}A short name or phrase used to identify the policy in dashboards, notifications, and incidents. To avoid confusion,
don't use the same display name for multiple policies in the same project. The name is limited to 512 Unicode
characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>enabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether or not the policy is enabled. The default is true.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The unique resource name for this policy. Its syntax is: projects/[PROJECT_ID]/alertPolicies/[ALERT_POLICY_ID]
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>notification_<wbr>channels</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}Identifies the notification channels to which notifications should be sent when incidents are opened or closed or when
new violations occur on an already opened incident. Each element of this array corresponds to the name field in each of
the NotificationChannel objects that are returned from the notificationChannels.list method. The syntax of the entries
in this field is 'projects/[PROJECT_ID]/notificationChannels/[CHANNEL_ID]'
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
        <span>user_<wbr>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}This field is intended to be used for organizing and identifying the AlertPolicy objects.The field can contain up to 64
entries. Each key and value is limited to 63 Unicode characters or 128 bytes, whichever is smaller. Labels and values
can contain only lowercase letters, numerals, underscores, and dashes. Keys must begin with a letter.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Alert<wbr>Policy<wbr>Condition</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#AlertPolicyCondition">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#AlertPolicyCondition">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#AlertPolicyConditionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#AlertPolicyConditionOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Condition<wbr>Absent</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicyconditionconditionabsent">Alert<wbr>Policy<wbr>Condition<wbr>Condition<wbr>Absent<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Condition<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicyconditionconditionthreshold">Alert<wbr>Policy<wbr>Condition<wbr>Condition<wbr>Threshold<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Condition<wbr>Absent</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicyconditionconditionabsent">*Alert<wbr>Policy<wbr>Condition<wbr>Condition<wbr>Absent</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Condition<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicyconditionconditionthreshold">*Alert<wbr>Policy<wbr>Condition<wbr>Condition<wbr>Threshold</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>condition<wbr>Absent</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicyconditionconditionabsent">Alert<wbr>Policy<wbr>Condition<wbr>Condition<wbr>Absent?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>condition<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicyconditionconditionthreshold">Alert<wbr>Policy<wbr>Condition<wbr>Condition<wbr>Threshold?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>condition<wbr>Absent</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicyconditionconditionabsent">Dict[Alert<wbr>Policy<wbr>Condition<wbr>Condition<wbr>Absent]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>condition<wbr>Threshold</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicyconditionconditionthreshold">Dict[Alert<wbr>Policy<wbr>Condition<wbr>Condition<wbr>Threshold]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>display_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Alert<wbr>Policy<wbr>Condition<wbr>Condition<wbr>Absent</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#AlertPolicyConditionConditionAbsent">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#AlertPolicyConditionConditionAbsent">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#AlertPolicyConditionConditionAbsentArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#AlertPolicyConditionConditionAbsentOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Aggregations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicyconditionconditionabsentaggregation">List&lt;Alert<wbr>Policy<wbr>Condition<wbr>Condition<wbr>Absent<wbr>Aggregation<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Trigger</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicyconditionconditionabsenttrigger">Alert<wbr>Policy<wbr>Condition<wbr>Condition<wbr>Absent<wbr>Trigger<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Aggregations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicyconditionconditionabsentaggregation">[]Alert<wbr>Policy<wbr>Condition<wbr>Condition<wbr>Absent<wbr>Aggregation</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Trigger</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicyconditionconditionabsenttrigger">*Alert<wbr>Policy<wbr>Condition<wbr>Condition<wbr>Absent<wbr>Trigger</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>aggregations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicyconditionconditionabsentaggregation">Alert<wbr>Policy<wbr>Condition<wbr>Condition<wbr>Absent<wbr>Aggregation[]?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>trigger</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicyconditionconditionabsenttrigger">Alert<wbr>Policy<wbr>Condition<wbr>Condition<wbr>Absent<wbr>Trigger?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>aggregations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicyconditionconditionabsentaggregation">List[Alert<wbr>Policy<wbr>Condition<wbr>Condition<wbr>Absent<wbr>Aggregation]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>trigger</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicyconditionconditionabsenttrigger">Dict[Alert<wbr>Policy<wbr>Condition<wbr>Condition<wbr>Absent<wbr>Trigger]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Alert<wbr>Policy<wbr>Condition<wbr>Condition<wbr>Absent<wbr>Aggregation</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#AlertPolicyConditionConditionAbsentAggregation">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#AlertPolicyConditionConditionAbsentAggregation">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#AlertPolicyConditionConditionAbsentAggregationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#AlertPolicyConditionConditionAbsentAggregationOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Alignment<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cross<wbr>Series<wbr>Reducer</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Group<wbr>By<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Per<wbr>Series<wbr>Aligner</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Alignment<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cross<wbr>Series<wbr>Reducer</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Group<wbr>By<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Per<wbr>Series<wbr>Aligner</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>alignment<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cross<wbr>Series<wbr>Reducer</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>group<wbr>By<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>per<wbr>Series<wbr>Aligner</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>alignment<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cross<wbr>Series<wbr>Reducer</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>group<wbr>By<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>per<wbr>Series<wbr>Aligner</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Alert<wbr>Policy<wbr>Condition<wbr>Condition<wbr>Absent<wbr>Trigger</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#AlertPolicyConditionConditionAbsentTrigger">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#AlertPolicyConditionConditionAbsentTrigger">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#AlertPolicyConditionConditionAbsentTriggerArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#AlertPolicyConditionConditionAbsentTriggerOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Percent</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Percent</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>percent</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>percent</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Alert<wbr>Policy<wbr>Condition<wbr>Condition<wbr>Threshold</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#AlertPolicyConditionConditionThreshold">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#AlertPolicyConditionConditionThreshold">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#AlertPolicyConditionConditionThresholdArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#AlertPolicyConditionConditionThresholdOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Aggregations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicyconditionconditionthresholdaggregation">List&lt;Alert<wbr>Policy<wbr>Condition<wbr>Condition<wbr>Threshold<wbr>Aggregation<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Comparison</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Denominator<wbr>Aggregations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicyconditionconditionthresholddenominatoraggregation">List&lt;Alert<wbr>Policy<wbr>Condition<wbr>Condition<wbr>Threshold<wbr>Denominator<wbr>Aggregation<wbr>Args&gt;?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Denominator<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Threshold<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Trigger</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicyconditionconditionthresholdtrigger">Alert<wbr>Policy<wbr>Condition<wbr>Condition<wbr>Threshold<wbr>Trigger<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Aggregations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicyconditionconditionthresholdaggregation">[]Alert<wbr>Policy<wbr>Condition<wbr>Condition<wbr>Threshold<wbr>Aggregation</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Comparison</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Denominator<wbr>Aggregations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicyconditionconditionthresholddenominatoraggregation">[]Alert<wbr>Policy<wbr>Condition<wbr>Condition<wbr>Threshold<wbr>Denominator<wbr>Aggregation</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Denominator<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Threshold<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Trigger</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicyconditionconditionthresholdtrigger">*Alert<wbr>Policy<wbr>Condition<wbr>Condition<wbr>Threshold<wbr>Trigger</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>aggregations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicyconditionconditionthresholdaggregation">Alert<wbr>Policy<wbr>Condition<wbr>Condition<wbr>Threshold<wbr>Aggregation[]?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>comparison</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>denominator<wbr>Aggregations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicyconditionconditionthresholddenominatoraggregation">Alert<wbr>Policy<wbr>Condition<wbr>Condition<wbr>Threshold<wbr>Denominator<wbr>Aggregation[]?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>denominator<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>threshold<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>trigger</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicyconditionconditionthresholdtrigger">Alert<wbr>Policy<wbr>Condition<wbr>Condition<wbr>Threshold<wbr>Trigger?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>aggregations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicyconditionconditionthresholdaggregation">List[Alert<wbr>Policy<wbr>Condition<wbr>Condition<wbr>Threshold<wbr>Aggregation]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>comparison</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>denominator<wbr>Aggregations</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicyconditionconditionthresholddenominatoraggregation">List[Alert<wbr>Policy<wbr>Condition<wbr>Condition<wbr>Threshold<wbr>Denominator<wbr>Aggregation]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>denominator<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>threshold<wbr>Value</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>trigger</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#alertpolicyconditionconditionthresholdtrigger">Dict[Alert<wbr>Policy<wbr>Condition<wbr>Condition<wbr>Threshold<wbr>Trigger]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Alert<wbr>Policy<wbr>Condition<wbr>Condition<wbr>Threshold<wbr>Aggregation</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#AlertPolicyConditionConditionThresholdAggregation">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#AlertPolicyConditionConditionThresholdAggregation">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#AlertPolicyConditionConditionThresholdAggregationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#AlertPolicyConditionConditionThresholdAggregationOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Alignment<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cross<wbr>Series<wbr>Reducer</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Group<wbr>By<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Per<wbr>Series<wbr>Aligner</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Alignment<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cross<wbr>Series<wbr>Reducer</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Group<wbr>By<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Per<wbr>Series<wbr>Aligner</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>alignment<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cross<wbr>Series<wbr>Reducer</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>group<wbr>By<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>per<wbr>Series<wbr>Aligner</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>alignment<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cross<wbr>Series<wbr>Reducer</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>group<wbr>By<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>per<wbr>Series<wbr>Aligner</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Alert<wbr>Policy<wbr>Condition<wbr>Condition<wbr>Threshold<wbr>Denominator<wbr>Aggregation</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#AlertPolicyConditionConditionThresholdDenominatorAggregation">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#AlertPolicyConditionConditionThresholdDenominatorAggregation">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#AlertPolicyConditionConditionThresholdDenominatorAggregationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#AlertPolicyConditionConditionThresholdDenominatorAggregationOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Alignment<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cross<wbr>Series<wbr>Reducer</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Group<wbr>By<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Per<wbr>Series<wbr>Aligner</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Alignment<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Cross<wbr>Series<wbr>Reducer</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Group<wbr>By<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Per<wbr>Series<wbr>Aligner</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>alignment<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cross<wbr>Series<wbr>Reducer</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>group<wbr>By<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>per<wbr>Series<wbr>Aligner</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>alignment<wbr>Period</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>cross<wbr>Series<wbr>Reducer</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>group<wbr>By<wbr>Fields</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>per<wbr>Series<wbr>Aligner</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Alert<wbr>Policy<wbr>Condition<wbr>Condition<wbr>Threshold<wbr>Trigger</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#AlertPolicyConditionConditionThresholdTrigger">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#AlertPolicyConditionConditionThresholdTrigger">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#AlertPolicyConditionConditionThresholdTriggerArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#AlertPolicyConditionConditionThresholdTriggerOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Percent</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Percent</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>percent</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>percent</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Alert<wbr>Policy<wbr>Creation<wbr>Record</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#AlertPolicyCreationRecord">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#AlertPolicyCreationRecordOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Mutate<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mutated<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Mutate<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mutated<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>mutate<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mutated<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>mutate<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mutated<wbr>By</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Alert<wbr>Policy<wbr>Documentation</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#AlertPolicyDocumentation">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#AlertPolicyDocumentation">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#AlertPolicyDocumentationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/monitoring?tab=doc#AlertPolicyDocumentationOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Content</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mime<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Content</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Mime<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>content</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mime<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>content</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>mime<wbr>Type</span>
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
	<dd>Apache-2.0</dd></dl>
