
---
title: "Job"
block_external_search_index: true
---



A scheduled job that can publish a pubsub message or a http request
every X interval of time, using crontab format string.

To use Cloud Scheduler your project must contain an App Engine app
that is located in one of the supported regions. If your project
does not have an App Engine app, you must create one.


To get more information about Job, see:

* [API documentation](https://cloud.google.com/scheduler/docs/reference/rest/)
* How-to Guides
    * [Official Documentation](https://cloud.google.com/scheduler/)

> This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/cloud_scheduler_job.html.markdown.



## Create a Job Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/cloudscheduler/#Job">Job</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/cloudscheduler/#JobArgs">JobArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Job</span><span class="p">(resource_name, opts=None, </span>app_engine_http_target=None<span class="p">, </span>attempt_deadline=None<span class="p">, </span>description=None<span class="p">, </span>http_target=None<span class="p">, </span>name=None<span class="p">, </span>project=None<span class="p">, </span>pubsub_target=None<span class="p">, </span>region=None<span class="p">, </span>retry_config=None<span class="p">, </span>schedule=None<span class="p">, </span>time_zone=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewJob<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/cloudscheduler?tab=doc#JobArgs">JobArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/cloudscheduler?tab=doc#Job">Job</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Cloudscheduler.Job.html">Job</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.CloudScheduler.JobArgs.html">JobArgs</a></span>? <span class="nx">args = null<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>App<wbr>Engine<wbr>Http<wbr>Target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobappenginehttptarget">Job<wbr>App<wbr>Engine<wbr>Http<wbr>Target<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}App Engine HTTP target. If the job providers a App Engine HTTP target the cron will send a request to the service
instance
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Attempt<wbr>Deadline</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The deadline for job attempts. If the request handler does not respond by this deadline then the request is cancelled
and the attempt is marked as a DEADLINE_EXCEEDED failure. The failed attempt can be viewed in execution logs. Cloud
Scheduler will retry the job according to the RetryConfig. The allowed duration for this deadline is: * For HTTP
targets, between 15 seconds and 30 minutes. * For App Engine HTTP targets, between 15 seconds and 24 hours. A duration
in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s"
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A human-readable description for the job. This string must not contain more than 500 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhttptarget">Job<wbr>Http<wbr>Target<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}HTTP target. If the job providers a http_target the cron will send a request to the targeted url
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the job.
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
        <span>Pubsub<wbr>Target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobpubsubtarget">Job<wbr>Pubsub<wbr>Target<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Pub/Sub target If the job providers a Pub/Sub target the cron will publish a message to the provided topic
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Region where the scheduler job resides
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retry<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobretryconfig">Job<wbr>Retry<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}By default, if a job does not complete successfully, meaning that an acknowledgement is not received from the handler,
then it will be retried with exponential backoff according to the settings
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Schedule</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Describes the schedule on which the job will be executed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the time zone to be used in interpreting schedule. The value of this field must be a time zone name from the
tz database.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>App<wbr>Engine<wbr>Http<wbr>Target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobappenginehttptarget">*Job<wbr>App<wbr>Engine<wbr>Http<wbr>Target</a></span>
    </dt>
    <dd>{{% md %}}App Engine HTTP target. If the job providers a App Engine HTTP target the cron will send a request to the service
instance
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Attempt<wbr>Deadline</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The deadline for job attempts. If the request handler does not respond by this deadline then the request is cancelled
and the attempt is marked as a DEADLINE_EXCEEDED failure. The failed attempt can be viewed in execution logs. Cloud
Scheduler will retry the job according to the RetryConfig. The allowed duration for this deadline is: * For HTTP
targets, between 15 seconds and 30 minutes. * For App Engine HTTP targets, between 15 seconds and 24 hours. A duration
in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s"
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A human-readable description for the job. This string must not contain more than 500 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhttptarget">*Job<wbr>Http<wbr>Target</a></span>
    </dt>
    <dd>{{% md %}}HTTP target. If the job providers a http_target the cron will send a request to the targeted url
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the job.
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
        <span>Pubsub<wbr>Target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobpubsubtarget">*Job<wbr>Pubsub<wbr>Target</a></span>
    </dt>
    <dd>{{% md %}}Pub/Sub target If the job providers a Pub/Sub target the cron will publish a message to the provided topic
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Region where the scheduler job resides
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retry<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobretryconfig">*Job<wbr>Retry<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}By default, if a job does not complete successfully, meaning that an acknowledgement is not received from the handler,
then it will be retried with exponential backoff according to the settings
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Schedule</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Describes the schedule on which the job will be executed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the time zone to be used in interpreting schedule. The value of this field must be a time zone name from the
tz database.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>app<wbr>Engine<wbr>Http<wbr>Target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobappenginehttptarget">Job<wbr>App<wbr>Engine<wbr>Http<wbr>Target?</a></span>
    </dt>
    <dd>{{% md %}}App Engine HTTP target. If the job providers a App Engine HTTP target the cron will send a request to the service
instance
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>attempt<wbr>Deadline</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The deadline for job attempts. If the request handler does not respond by this deadline then the request is cancelled
and the attempt is marked as a DEADLINE_EXCEEDED failure. The failed attempt can be viewed in execution logs. Cloud
Scheduler will retry the job according to the RetryConfig. The allowed duration for this deadline is: * For HTTP
targets, between 15 seconds and 30 minutes. * For App Engine HTTP targets, between 15 seconds and 24 hours. A duration
in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s"
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A human-readable description for the job. This string must not contain more than 500 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http<wbr>Target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhttptarget">Job<wbr>Http<wbr>Target?</a></span>
    </dt>
    <dd>{{% md %}}HTTP target. If the job providers a http_target the cron will send a request to the targeted url
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the job.
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
        <span>pubsub<wbr>Target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobpubsubtarget">Job<wbr>Pubsub<wbr>Target?</a></span>
    </dt>
    <dd>{{% md %}}Pub/Sub target If the job providers a Pub/Sub target the cron will publish a message to the provided topic
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Region where the scheduler job resides
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retry<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobretryconfig">Job<wbr>Retry<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}By default, if a job does not complete successfully, meaning that an acknowledgement is not received from the handler,
then it will be retried with exponential backoff according to the settings
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>schedule</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Describes the schedule on which the job will be executed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>time<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the time zone to be used in interpreting schedule. The value of this field must be a time zone name from the
tz database.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>app_<wbr>engine_<wbr>http_<wbr>target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobappenginehttptarget">Dict[Job<wbr>App<wbr>Engine<wbr>Http<wbr>Target]</a></span>
    </dt>
    <dd>{{% md %}}App Engine HTTP target. If the job providers a App Engine HTTP target the cron will send a request to the service
instance
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>attempt_<wbr>deadline</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The deadline for job attempts. If the request handler does not respond by this deadline then the request is cancelled
and the attempt is marked as a DEADLINE_EXCEEDED failure. The failed attempt can be viewed in execution logs. Cloud
Scheduler will retry the job according to the RetryConfig. The allowed duration for this deadline is: * For HTTP
targets, between 15 seconds and 30 minutes. * For App Engine HTTP targets, between 15 seconds and 24 hours. A duration
in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s"
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A human-readable description for the job. This string must not contain more than 500 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http_<wbr>target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhttptarget">Dict[Job<wbr>Http<wbr>Target]</a></span>
    </dt>
    <dd>{{% md %}}HTTP target. If the job providers a http_target the cron will send a request to the targeted url
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the job.
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
        <span>pubsub_<wbr>target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobpubsubtarget">Dict[Job<wbr>Pubsub<wbr>Target]</a></span>
    </dt>
    <dd>{{% md %}}Pub/Sub target If the job providers a Pub/Sub target the cron will publish a message to the provided topic
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Region where the scheduler job resides
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retry_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobretryconfig">Dict[Job<wbr>Retry<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}By default, if a job does not complete successfully, meaning that an acknowledgement is not received from the handler,
then it will be retried with exponential backoff according to the settings
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>schedule</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Describes the schedule on which the job will be executed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>time_<wbr>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the time zone to be used in interpreting schedule. The value of this field must be a time zone name from the
tz database.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Job Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>App<wbr>Engine<wbr>Http<wbr>Target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobappenginehttptarget">Job<wbr>App<wbr>Engine<wbr>Http<wbr>Target?</a></span>
    </dt>
    <dd>{{% md %}}App Engine HTTP target. If the job providers a App Engine HTTP target the cron will send a request to the service
instance
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Attempt<wbr>Deadline</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The deadline for job attempts. If the request handler does not respond by this deadline then the request is cancelled
and the attempt is marked as a DEADLINE_EXCEEDED failure. The failed attempt can be viewed in execution logs. Cloud
Scheduler will retry the job according to the RetryConfig. The allowed duration for this deadline is: * For HTTP
targets, between 15 seconds and 30 minutes. * For App Engine HTTP targets, between 15 seconds and 24 hours. A duration
in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s"
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A human-readable description for the job. This string must not contain more than 500 characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Http<wbr>Target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhttptarget">Job<wbr>Http<wbr>Target?</a></span>
    </dt>
    <dd>{{% md %}}HTTP target. If the job providers a http_target the cron will send a request to the targeted url
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the job.
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
        <span>Pubsub<wbr>Target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobpubsubtarget">Job<wbr>Pubsub<wbr>Target?</a></span>
    </dt>
    <dd>{{% md %}}Pub/Sub target If the job providers a Pub/Sub target the cron will publish a message to the provided topic
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Region where the scheduler job resides
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Retry<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobretryconfig">Job<wbr>Retry<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}By default, if a job does not complete successfully, meaning that an acknowledgement is not received from the handler,
then it will be retried with exponential backoff according to the settings
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Schedule</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Describes the schedule on which the job will be executed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Time<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the time zone to be used in interpreting schedule. The value of this field must be a time zone name from the
tz database.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>App<wbr>Engine<wbr>Http<wbr>Target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobappenginehttptarget">*Job<wbr>App<wbr>Engine<wbr>Http<wbr>Target</a></span>
    </dt>
    <dd>{{% md %}}App Engine HTTP target. If the job providers a App Engine HTTP target the cron will send a request to the service
instance
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Attempt<wbr>Deadline</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The deadline for job attempts. If the request handler does not respond by this deadline then the request is cancelled
and the attempt is marked as a DEADLINE_EXCEEDED failure. The failed attempt can be viewed in execution logs. Cloud
Scheduler will retry the job according to the RetryConfig. The allowed duration for this deadline is: * For HTTP
targets, between 15 seconds and 30 minutes. * For App Engine HTTP targets, between 15 seconds and 24 hours. A duration
in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s"
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A human-readable description for the job. This string must not contain more than 500 characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Http<wbr>Target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhttptarget">*Job<wbr>Http<wbr>Target</a></span>
    </dt>
    <dd>{{% md %}}HTTP target. If the job providers a http_target the cron will send a request to the targeted url
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the job.
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
        <span>Pubsub<wbr>Target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobpubsubtarget">*Job<wbr>Pubsub<wbr>Target</a></span>
    </dt>
    <dd>{{% md %}}Pub/Sub target If the job providers a Pub/Sub target the cron will publish a message to the provided topic
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Region where the scheduler job resides
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Retry<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobretryconfig">*Job<wbr>Retry<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}By default, if a job does not complete successfully, meaning that an acknowledgement is not received from the handler,
then it will be retried with exponential backoff according to the settings
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Schedule</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Describes the schedule on which the job will be executed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Time<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the time zone to be used in interpreting schedule. The value of this field must be a time zone name from the
tz database.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>app<wbr>Engine<wbr>Http<wbr>Target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobappenginehttptarget">Job<wbr>App<wbr>Engine<wbr>Http<wbr>Target?</a></span>
    </dt>
    <dd>{{% md %}}App Engine HTTP target. If the job providers a App Engine HTTP target the cron will send a request to the service
instance
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>attempt<wbr>Deadline</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The deadline for job attempts. If the request handler does not respond by this deadline then the request is cancelled
and the attempt is marked as a DEADLINE_EXCEEDED failure. The failed attempt can be viewed in execution logs. Cloud
Scheduler will retry the job according to the RetryConfig. The allowed duration for this deadline is: * For HTTP
targets, between 15 seconds and 30 minutes. * For App Engine HTTP targets, between 15 seconds and 24 hours. A duration
in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s"
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A human-readable description for the job. This string must not contain more than 500 characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>http<wbr>Target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhttptarget">Job<wbr>Http<wbr>Target?</a></span>
    </dt>
    <dd>{{% md %}}HTTP target. If the job providers a http_target the cron will send a request to the targeted url
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the job.
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
        <span>pubsub<wbr>Target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobpubsubtarget">Job<wbr>Pubsub<wbr>Target?</a></span>
    </dt>
    <dd>{{% md %}}Pub/Sub target If the job providers a Pub/Sub target the cron will publish a message to the provided topic
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Region where the scheduler job resides
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>retry<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobretryconfig">Job<wbr>Retry<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}By default, if a job does not complete successfully, meaning that an acknowledgement is not received from the handler,
then it will be retried with exponential backoff according to the settings
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>schedule</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Describes the schedule on which the job will be executed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>time<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the time zone to be used in interpreting schedule. The value of this field must be a time zone name from the
tz database.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>app_<wbr>engine_<wbr>http_<wbr>target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobappenginehttptarget">Dict[Job<wbr>App<wbr>Engine<wbr>Http<wbr>Target]</a></span>
    </dt>
    <dd>{{% md %}}App Engine HTTP target. If the job providers a App Engine HTTP target the cron will send a request to the service
instance
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>attempt_<wbr>deadline</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The deadline for job attempts. If the request handler does not respond by this deadline then the request is cancelled
and the attempt is marked as a DEADLINE_EXCEEDED failure. The failed attempt can be viewed in execution logs. Cloud
Scheduler will retry the job according to the RetryConfig. The allowed duration for this deadline is: * For HTTP
targets, between 15 seconds and 30 minutes. * For App Engine HTTP targets, between 15 seconds and 24 hours. A duration
in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s"
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A human-readable description for the job. This string must not contain more than 500 characters.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>http_<wbr>target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhttptarget">Dict[Job<wbr>Http<wbr>Target]</a></span>
    </dt>
    <dd>{{% md %}}HTTP target. If the job providers a http_target the cron will send a request to the targeted url
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the job.
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
        <span>pubsub_<wbr>target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobpubsubtarget">Dict[Job<wbr>Pubsub<wbr>Target]</a></span>
    </dt>
    <dd>{{% md %}}Pub/Sub target If the job providers a Pub/Sub target the cron will publish a message to the provided topic
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Region where the scheduler job resides
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>retry_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobretryconfig">Dict[Job<wbr>Retry<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}By default, if a job does not complete successfully, meaning that an acknowledgement is not received from the handler,
then it will be retried with exponential backoff according to the settings
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>schedule</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Describes the schedule on which the job will be executed.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>time_<wbr>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the time zone to be used in interpreting schedule. The value of this field must be a time zone name from the
tz database.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Job Resource

Get an existing Job resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/cloudscheduler/#JobState">JobState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/cloudscheduler/#Job">Job</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>app_engine_http_target=None<span class="p">, </span>attempt_deadline=None<span class="p">, </span>description=None<span class="p">, </span>http_target=None<span class="p">, </span>name=None<span class="p">, </span>project=None<span class="p">, </span>pubsub_target=None<span class="p">, </span>region=None<span class="p">, </span>retry_config=None<span class="p">, </span>schedule=None<span class="p">, </span>time_zone=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetJob<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/cloudscheduler?tab=doc#JobState">JobState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/cloudscheduler?tab=doc#Job">Job</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Cloudscheduler.Job.html">Job</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Cloudscheduler.JobState.html">JobState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>App<wbr>Engine<wbr>Http<wbr>Target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobappenginehttptarget">Job<wbr>App<wbr>Engine<wbr>Http<wbr>Target<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}App Engine HTTP target. If the job providers a App Engine HTTP target the cron will send a request to the service
instance
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Attempt<wbr>Deadline</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The deadline for job attempts. If the request handler does not respond by this deadline then the request is cancelled
and the attempt is marked as a DEADLINE_EXCEEDED failure. The failed attempt can be viewed in execution logs. Cloud
Scheduler will retry the job according to the RetryConfig. The allowed duration for this deadline is: * For HTTP
targets, between 15 seconds and 30 minutes. * For App Engine HTTP targets, between 15 seconds and 24 hours. A duration
in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s"
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A human-readable description for the job. This string must not contain more than 500 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhttptarget">Job<wbr>Http<wbr>Target<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}HTTP target. If the job providers a http_target the cron will send a request to the targeted url
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the job.
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
        <span>Pubsub<wbr>Target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobpubsubtarget">Job<wbr>Pubsub<wbr>Target<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Pub/Sub target If the job providers a Pub/Sub target the cron will publish a message to the provided topic
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Region where the scheduler job resides
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retry<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobretryconfig">Job<wbr>Retry<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}By default, if a job does not complete successfully, meaning that an acknowledgement is not received from the handler,
then it will be retried with exponential backoff according to the settings
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Schedule</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Describes the schedule on which the job will be executed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the time zone to be used in interpreting schedule. The value of this field must be a time zone name from the
tz database.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>App<wbr>Engine<wbr>Http<wbr>Target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobappenginehttptarget">*Job<wbr>App<wbr>Engine<wbr>Http<wbr>Target</a></span>
    </dt>
    <dd>{{% md %}}App Engine HTTP target. If the job providers a App Engine HTTP target the cron will send a request to the service
instance
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Attempt<wbr>Deadline</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The deadline for job attempts. If the request handler does not respond by this deadline then the request is cancelled
and the attempt is marked as a DEADLINE_EXCEEDED failure. The failed attempt can be viewed in execution logs. Cloud
Scheduler will retry the job according to the RetryConfig. The allowed duration for this deadline is: * For HTTP
targets, between 15 seconds and 30 minutes. * For App Engine HTTP targets, between 15 seconds and 24 hours. A duration
in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s"
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A human-readable description for the job. This string must not contain more than 500 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhttptarget">*Job<wbr>Http<wbr>Target</a></span>
    </dt>
    <dd>{{% md %}}HTTP target. If the job providers a http_target the cron will send a request to the targeted url
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the job.
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
        <span>Pubsub<wbr>Target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobpubsubtarget">*Job<wbr>Pubsub<wbr>Target</a></span>
    </dt>
    <dd>{{% md %}}Pub/Sub target If the job providers a Pub/Sub target the cron will publish a message to the provided topic
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Region where the scheduler job resides
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retry<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobretryconfig">*Job<wbr>Retry<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}By default, if a job does not complete successfully, meaning that an acknowledgement is not received from the handler,
then it will be retried with exponential backoff according to the settings
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Schedule</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Describes the schedule on which the job will be executed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Specifies the time zone to be used in interpreting schedule. The value of this field must be a time zone name from the
tz database.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>app<wbr>Engine<wbr>Http<wbr>Target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobappenginehttptarget">Job<wbr>App<wbr>Engine<wbr>Http<wbr>Target?</a></span>
    </dt>
    <dd>{{% md %}}App Engine HTTP target. If the job providers a App Engine HTTP target the cron will send a request to the service
instance
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>attempt<wbr>Deadline</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The deadline for job attempts. If the request handler does not respond by this deadline then the request is cancelled
and the attempt is marked as a DEADLINE_EXCEEDED failure. The failed attempt can be viewed in execution logs. Cloud
Scheduler will retry the job according to the RetryConfig. The allowed duration for this deadline is: * For HTTP
targets, between 15 seconds and 30 minutes. * For App Engine HTTP targets, between 15 seconds and 24 hours. A duration
in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s"
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A human-readable description for the job. This string must not contain more than 500 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http<wbr>Target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhttptarget">Job<wbr>Http<wbr>Target?</a></span>
    </dt>
    <dd>{{% md %}}HTTP target. If the job providers a http_target the cron will send a request to the targeted url
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the job.
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
        <span>pubsub<wbr>Target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobpubsubtarget">Job<wbr>Pubsub<wbr>Target?</a></span>
    </dt>
    <dd>{{% md %}}Pub/Sub target If the job providers a Pub/Sub target the cron will publish a message to the provided topic
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Region where the scheduler job resides
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retry<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobretryconfig">Job<wbr>Retry<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}By default, if a job does not complete successfully, meaning that an acknowledgement is not received from the handler,
then it will be retried with exponential backoff according to the settings
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>schedule</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Describes the schedule on which the job will be executed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>time<wbr>Zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Specifies the time zone to be used in interpreting schedule. The value of this field must be a time zone name from the
tz database.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>app_<wbr>engine_<wbr>http_<wbr>target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobappenginehttptarget">Dict[Job<wbr>App<wbr>Engine<wbr>Http<wbr>Target]</a></span>
    </dt>
    <dd>{{% md %}}App Engine HTTP target. If the job providers a App Engine HTTP target the cron will send a request to the service
instance
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>attempt_<wbr>deadline</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The deadline for job attempts. If the request handler does not respond by this deadline then the request is cancelled
and the attempt is marked as a DEADLINE_EXCEEDED failure. The failed attempt can be viewed in execution logs. Cloud
Scheduler will retry the job according to the RetryConfig. The allowed duration for this deadline is: * For HTTP
targets, between 15 seconds and 30 minutes. * For App Engine HTTP targets, between 15 seconds and 24 hours. A duration
in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s"
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A human-readable description for the job. This string must not contain more than 500 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http_<wbr>target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhttptarget">Dict[Job<wbr>Http<wbr>Target]</a></span>
    </dt>
    <dd>{{% md %}}HTTP target. If the job providers a http_target the cron will send a request to the targeted url
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the job.
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
        <span>pubsub_<wbr>target</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobpubsubtarget">Dict[Job<wbr>Pubsub<wbr>Target]</a></span>
    </dt>
    <dd>{{% md %}}Pub/Sub target If the job providers a Pub/Sub target the cron will publish a message to the provided topic
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Region where the scheduler job resides
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retry_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobretryconfig">Dict[Job<wbr>Retry<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}By default, if a job does not complete successfully, meaning that an acknowledgement is not received from the handler,
then it will be retried with exponential backoff according to the settings
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>schedule</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Describes the schedule on which the job will be executed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>time_<wbr>zone</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Specifies the time zone to be used in interpreting schedule. The value of this field must be a time zone name from the
tz database.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Job<wbr>App<wbr>Engine<wbr>Http<wbr>Target</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#JobAppEngineHttpTarget">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#JobAppEngineHttpTarget">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/cloudscheduler?tab=doc#JobAppEngineHttpTargetArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/cloudscheduler?tab=doc#JobAppEngineHttpTargetOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>App<wbr>Engine<wbr>Routing</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobappenginehttptargetappenginerouting">Job<wbr>App<wbr>Engine<wbr>Http<wbr>Target<wbr>App<wbr>Engine<wbr>Routing<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Body</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Method</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Relative<wbr>Uri</span>
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
        <span>App<wbr>Engine<wbr>Routing</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobappenginehttptargetappenginerouting">*Job<wbr>App<wbr>Engine<wbr>Http<wbr>Target<wbr>App<wbr>Engine<wbr>Routing</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Body</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Method</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Relative<wbr>Uri</span>
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
        <span>app<wbr>Engine<wbr>Routing</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobappenginehttptargetappenginerouting">Job<wbr>App<wbr>Engine<wbr>Http<wbr>Target<wbr>App<wbr>Engine<wbr>Routing?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>body</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http<wbr>Method</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>relative<wbr>Uri</span>
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
        <span>app<wbr>Engine<wbr>Routing</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobappenginehttptargetappenginerouting">Dict[Job<wbr>App<wbr>Engine<wbr>Http<wbr>Target<wbr>App<wbr>Engine<wbr>Routing]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>body</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http<wbr>Method</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>relative<wbr>Uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Job<wbr>App<wbr>Engine<wbr>Http<wbr>Target<wbr>App<wbr>Engine<wbr>Routing</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#JobAppEngineHttpTargetAppEngineRouting">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#JobAppEngineHttpTargetAppEngineRouting">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/cloudscheduler?tab=doc#JobAppEngineHttpTargetAppEngineRoutingArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/cloudscheduler?tab=doc#JobAppEngineHttpTargetAppEngineRoutingOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Instance</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Version</span>
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
        <span>Instance</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Version</span>
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
        <span>instance</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>version</span>
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
        <span>instance</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Job<wbr>Http<wbr>Target</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#JobHttpTarget">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#JobHttpTarget">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/cloudscheduler?tab=doc#JobHttpTargetArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/cloudscheduler?tab=doc#JobHttpTargetOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Body</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Method</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oauth<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhttptargetoauthtoken">Job<wbr>Http<wbr>Target<wbr>Oauth<wbr>Token<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oidc<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhttptargetoidctoken">Job<wbr>Http<wbr>Target<wbr>Oidc<wbr>Token<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Uri</span>
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
        <span>Body</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Method</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oauth<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhttptargetoauthtoken">*Job<wbr>Http<wbr>Target<wbr>Oauth<wbr>Token</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Oidc<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhttptargetoidctoken">*Job<wbr>Http<wbr>Target<wbr>Oidc<wbr>Token</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Uri</span>
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
        <span>body</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http<wbr>Method</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>oauth<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhttptargetoauthtoken">Job<wbr>Http<wbr>Target<wbr>Oauth<wbr>Token?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>oidc<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhttptargetoidctoken">Job<wbr>Http<wbr>Target<wbr>Oidc<wbr>Token?</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>uri</span>
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
        <span>body</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>headers</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http<wbr>Method</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>oauth<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhttptargetoauthtoken">Dict[Job<wbr>Http<wbr>Target<wbr>Oauth<wbr>Token]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>oidc<wbr>Token</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#jobhttptargetoidctoken">Dict[Job<wbr>Http<wbr>Target<wbr>Oidc<wbr>Token]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>uri</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Job<wbr>Http<wbr>Target<wbr>Oauth<wbr>Token</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#JobHttpTargetOauthToken">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#JobHttpTargetOauthToken">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/cloudscheduler?tab=doc#JobHttpTargetOauthTokenArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/cloudscheduler?tab=doc#JobHttpTargetOauthTokenOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Scope</span>
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
        <span>Scope</span>
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
        <span>scope</span>
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
        <span>scope</span>
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





<h4>Job<wbr>Http<wbr>Target<wbr>Oidc<wbr>Token</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#JobHttpTargetOidcToken">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#JobHttpTargetOidcToken">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/cloudscheduler?tab=doc#JobHttpTargetOidcTokenArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/cloudscheduler?tab=doc#JobHttpTargetOidcTokenOutput">output</a> API doc for this type.
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





<h4>Job<wbr>Pubsub<wbr>Target</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#JobPubsubTarget">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#JobPubsubTarget">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/cloudscheduler?tab=doc#JobPubsubTargetArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/cloudscheduler?tab=doc#JobPubsubTargetOutput">output</a> API doc for this type.
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
        <span>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Topic<wbr>Name</span>
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
        <span>Data</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Topic<wbr>Name</span>
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
        <span>data</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>topic<wbr>Name</span>
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
        <span>data</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>topic<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Job<wbr>Retry<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#JobRetryConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#JobRetryConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/cloudscheduler?tab=doc#JobRetryConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/cloudscheduler?tab=doc#JobRetryConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Backoff<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Doublings</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Retry<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Backoff<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retry<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Backoff<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Doublings</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Retry<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Min<wbr>Backoff<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Retry<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Backoff<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Doublings</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Retry<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min<wbr>Backoff<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retry<wbr>Count</span>
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
        <span>max<wbr>Backoff<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Doublings</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Retry<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>min<wbr>Backoff<wbr>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>retry<wbr>Count</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
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

