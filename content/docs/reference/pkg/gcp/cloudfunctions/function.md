
---
title: "Function"
block_external_search_index: true
---

Creates a new Cloud Function. For more information see
[the official documentation](https://cloud.google.com/functions/docs/)
and
[API](https://cloud.google.com/functions/docs/apis).

> **Warning:** As of November 1, 2019, newly created Functions are
private-by-default and will require [appropriate IAM permissions](https://cloud.google.com/functions/docs/reference/iam/roles)
to be invoked. See below examples for how to set up the appropriate permissions,
or view the [Cloud Functions IAM resources](https://www.terraform.io/docs/providers/google/r/cloudfunctions_cloud_function_iam.html)
for Cloud Functions.

> This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/cloudfunctions_function.html.markdown.



## Create a Function Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/cloudfunctions/#Function">Function</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/cloudfunctions/#FunctionArgs">FunctionArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Function</span><span class="p">(resource_name, opts=None, </span>available_memory_mb=None<span class="p">, </span>description=None<span class="p">, </span>entry_point=None<span class="p">, </span>environment_variables=None<span class="p">, </span>event_trigger=None<span class="p">, </span>https_trigger_url=None<span class="p">, </span>labels=None<span class="p">, </span>max_instances=None<span class="p">, </span>name=None<span class="p">, </span>project=None<span class="p">, </span>region=None<span class="p">, </span>runtime=None<span class="p">, </span>service_account_email=None<span class="p">, </span>source_archive_bucket=None<span class="p">, </span>source_archive_object=None<span class="p">, </span>source_repository=None<span class="p">, </span>timeout=None<span class="p">, </span>trigger_http=None<span class="p">, </span>vpc_connector=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewFunction<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/cloudfunctions?tab=doc#FunctionArgs">FunctionArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/cloudfunctions?tab=doc#Function">Function</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Cloudfunctions.Function.html">Function</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.CloudFunctions.Inputs.FunctionArgs.html">FunctionArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Available<wbr>Memory<wbr>Mb</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Memory (in MB), available to the function. Default value is 256MB. Allowed values are: 128MB, 256MB, 512MB, 1024MB, and 2048MB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of the function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Entry<wbr>Point</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the function that will be executed when the Google Cloud Function is triggered.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Environment<wbr>Variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}A set of key/value environment variable pairs to assign to the function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Event<wbr>Trigger</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functioneventtrigger">Pulumi.<wbr>Gcp.<wbr>Cloud<wbr>Functions.<wbr>Inputs.<wbr>Function<wbr>Event<wbr>Trigger<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A source that fires events in response to a condition in another service. Structure is documented below. Cannot be used with `trigger_http`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Https<wbr>Trigger<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}URL which triggers function execution. Returned only if `trigger_http` is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to the function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The limit on the maximum number of function instances that may coexist at a given time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A user-defined name of the function. Function names must be unique globally.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Project of the function. If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Region of function. Currently can be only "us-central1". If it is not provided, the provider region is used.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Runtime</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The runtime in which the function is going to run.
Eg. `"nodejs8"`, `"nodejs10"`, `"python37"`, `"go111"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Account<wbr>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If provided, the self-provided service account to run the function with.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Archive<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The GCS bucket containing the zip archive which contains the function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Archive<wbr>Object</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The source archive object (file) in archive bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Repository</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functionsourcerepository">Pulumi.<wbr>Gcp.<wbr>Cloud<wbr>Functions.<wbr>Inputs.<wbr>Function<wbr>Source<wbr>Repository<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Represents parameters related to source repository where a function is hosted.
Cannot be set alongside `source_archive_bucket` or `source_archive_object`. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for the function. Default value is 60 seconds. Cannot be more than 540 seconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Trigger<wbr>Http</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Boolean variable. Any HTTP request (of a supported type) to the endpoint will trigger function execution. Supported HTTP request types are: POST, PUT, GET, DELETE, and OPTIONS. Endpoint is returned as `https_trigger_url`. Cannot be used with `trigger_bucket` and `trigger_topic`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpc<wbr>Connector</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The VPC Network Connector that this cloud function can connect to. It can be either the fully-qualified URI, or the short name of the network connector resource. The format of this field is `projects/*/locations/*/connectors/*`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Available<wbr>Memory<wbr>Mb</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Memory (in MB), available to the function. Default value is 256MB. Allowed values are: 128MB, 256MB, 512MB, 1024MB, and 2048MB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Description of the function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Entry<wbr>Point</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the function that will be executed when the Google Cloud Function is triggered.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Environment<wbr>Variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A set of key/value environment variable pairs to assign to the function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Event<wbr>Trigger</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functioneventtrigger">*Function<wbr>Event<wbr>Trigger</a></span>
    </dt>
    <dd>{{% md %}}A source that fires events in response to a condition in another service. Structure is documented below. Cannot be used with `trigger_http`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Https<wbr>Trigger<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}URL which triggers function execution. Returned only if `trigger_http` is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to the function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The limit on the maximum number of function instances that may coexist at a given time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A user-defined name of the function. Function names must be unique globally.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Project of the function. If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Region of function. Currently can be only "us-central1". If it is not provided, the provider region is used.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Runtime</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The runtime in which the function is going to run.
Eg. `"nodejs8"`, `"nodejs10"`, `"python37"`, `"go111"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Account<wbr>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}If provided, the self-provided service account to run the function with.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Archive<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The GCS bucket containing the zip archive which contains the function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Archive<wbr>Object</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The source archive object (file) in archive bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Repository</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functionsourcerepository">*Function<wbr>Source<wbr>Repository</a></span>
    </dt>
    <dd>{{% md %}}Represents parameters related to source repository where a function is hosted.
Cannot be set alongside `source_archive_bucket` or `source_archive_object`. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for the function. Default value is 60 seconds. Cannot be more than 540 seconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Trigger<wbr>Http</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Boolean variable. Any HTTP request (of a supported type) to the endpoint will trigger function execution. Supported HTTP request types are: POST, PUT, GET, DELETE, and OPTIONS. Endpoint is returned as `https_trigger_url`. Cannot be used with `trigger_bucket` and `trigger_topic`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpc<wbr>Connector</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The VPC Network Connector that this cloud function can connect to. It can be either the fully-qualified URI, or the short name of the network connector resource. The format of this field is `projects/*/locations/*/connectors/*`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>available<wbr>Memory<wbr>Mb</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Memory (in MB), available to the function. Default value is 256MB. Allowed values are: 128MB, 256MB, 512MB, 1024MB, and 2048MB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of the function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>entry<wbr>Point</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the function that will be executed when the Google Cloud Function is triggered.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>environment<wbr>Variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}A set of key/value environment variable pairs to assign to the function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>event<wbr>Trigger</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functioneventtrigger">Function<wbr>Event<wbr>Trigger?</a></span>
    </dt>
    <dd>{{% md %}}A source that fires events in response to a condition in another service. Structure is documented below. Cannot be used with `trigger_http`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>https<wbr>Trigger<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}URL which triggers function execution. Returned only if `trigger_http` is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to the function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The limit on the maximum number of function instances that may coexist at a given time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A user-defined name of the function. Function names must be unique globally.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Project of the function. If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Region of function. Currently can be only "us-central1". If it is not provided, the provider region is used.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>runtime</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The runtime in which the function is going to run.
Eg. `"nodejs8"`, `"nodejs10"`, `"python37"`, `"go111"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service<wbr>Account<wbr>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If provided, the self-provided service account to run the function with.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source<wbr>Archive<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The GCS bucket containing the zip archive which contains the function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source<wbr>Archive<wbr>Object</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The source archive object (file) in archive bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source<wbr>Repository</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functionsourcerepository">Function<wbr>Source<wbr>Repository?</a></span>
    </dt>
    <dd>{{% md %}}Represents parameters related to source repository where a function is hosted.
Cannot be set alongside `source_archive_bucket` or `source_archive_object`. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for the function. Default value is 60 seconds. Cannot be more than 540 seconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>trigger<wbr>Http</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Boolean variable. Any HTTP request (of a supported type) to the endpoint will trigger function execution. Supported HTTP request types are: POST, PUT, GET, DELETE, and OPTIONS. Endpoint is returned as `https_trigger_url`. Cannot be used with `trigger_bucket` and `trigger_topic`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpc<wbr>Connector</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The VPC Network Connector that this cloud function can connect to. It can be either the fully-qualified URI, or the short name of the network connector resource. The format of this field is `projects/*/locations/*/connectors/*`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>available_<wbr>memory_<wbr>mb</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Memory (in MB), available to the function. Default value is 256MB. Allowed values are: 128MB, 256MB, 512MB, 1024MB, and 2048MB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Description of the function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>entry_<wbr>point</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the function that will be executed when the Google Cloud Function is triggered.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>environment_<wbr>variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A set of key/value environment variable pairs to assign to the function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>event_<wbr>trigger</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functioneventtrigger">Dict[Function<wbr>Event<wbr>Trigger]</a></span>
    </dt>
    <dd>{{% md %}}A source that fires events in response to a condition in another service. Structure is documented below. Cannot be used with `trigger_http`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>https_<wbr>trigger_<wbr>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}URL which triggers function execution. Returned only if `trigger_http` is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to the function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max_<wbr>instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The limit on the maximum number of function instances that may coexist at a given time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A user-defined name of the function. Function names must be unique globally.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Project of the function. If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Region of function. Currently can be only "us-central1". If it is not provided, the provider region is used.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>runtime</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The runtime in which the function is going to run.
Eg. `"nodejs8"`, `"nodejs10"`, `"python37"`, `"go111"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service_<wbr>account_<wbr>email</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}If provided, the self-provided service account to run the function with.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source_<wbr>archive_<wbr>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The GCS bucket containing the zip archive which contains the function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source_<wbr>archive_<wbr>object</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The source archive object (file) in archive bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source_<wbr>repository</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functionsourcerepository">Dict[Function<wbr>Source<wbr>Repository]</a></span>
    </dt>
    <dd>{{% md %}}Represents parameters related to source repository where a function is hosted.
Cannot be set alongside `source_archive_bucket` or `source_archive_object`. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for the function. Default value is 60 seconds. Cannot be more than 540 seconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>trigger_<wbr>http</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Boolean variable. Any HTTP request (of a supported type) to the endpoint will trigger function execution. Supported HTTP request types are: POST, PUT, GET, DELETE, and OPTIONS. Endpoint is returned as `https_trigger_url`. Cannot be used with `trigger_bucket` and `trigger_topic`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpc_<wbr>connector</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The VPC Network Connector that this cloud function can connect to. It can be either the fully-qualified URI, or the short name of the network connector resource. The format of this field is `projects/*/locations/*/connectors/*`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Function Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Available<wbr>Memory<wbr>Mb</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Memory (in MB), available to the function. Default value is 256MB. Allowed values are: 128MB, 256MB, 512MB, 1024MB, and 2048MB.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of the function.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Entry<wbr>Point</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the function that will be executed when the Google Cloud Function is triggered.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Environment<wbr>Variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}A set of key/value environment variable pairs to assign to the function.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Event<wbr>Trigger</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functioneventtrigger">Pulumi.<wbr>Gcp.<wbr>Cloud<wbr>Functions.<wbr>Outputs.<wbr>Function<wbr>Event<wbr>Trigger</a></span>
    </dt>
    <dd>{{% md %}}A source that fires events in response to a condition in another service. Structure is documented below. Cannot be used with `trigger_http`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Https<wbr>Trigger<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URL which triggers function execution. Returned only if `trigger_http` is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to the function.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Max<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The limit on the maximum number of function instances that may coexist at a given time.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A user-defined name of the function. Function names must be unique globally.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Project of the function. If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Region of function. Currently can be only "us-central1". If it is not provided, the provider region is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Runtime</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The runtime in which the function is going to run.
Eg. `"nodejs8"`, `"nodejs10"`, `"python37"`, `"go111"`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Service<wbr>Account<wbr>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}If provided, the self-provided service account to run the function with.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Source<wbr>Archive<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The GCS bucket containing the zip archive which contains the function.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Source<wbr>Archive<wbr>Object</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The source archive object (file) in archive bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Source<wbr>Repository</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functionsourcerepository">Pulumi.<wbr>Gcp.<wbr>Cloud<wbr>Functions.<wbr>Outputs.<wbr>Function<wbr>Source<wbr>Repository?</a></span>
    </dt>
    <dd>{{% md %}}Represents parameters related to source repository where a function is hosted.
Cannot be set alongside `source_archive_bucket` or `source_archive_object`. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for the function. Default value is 60 seconds. Cannot be more than 540 seconds.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Trigger<wbr>Http</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Boolean variable. Any HTTP request (of a supported type) to the endpoint will trigger function execution. Supported HTTP request types are: POST, PUT, GET, DELETE, and OPTIONS. Endpoint is returned as `https_trigger_url`. Cannot be used with `trigger_bucket` and `trigger_topic`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vpc<wbr>Connector</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The VPC Network Connector that this cloud function can connect to. It can be either the fully-qualified URI, or the short name of the network connector resource. The format of this field is `projects/*/locations/*/connectors/*`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Available<wbr>Memory<wbr>Mb</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Memory (in MB), available to the function. Default value is 256MB. Allowed values are: 128MB, 256MB, 512MB, 1024MB, and 2048MB.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Description of the function.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Entry<wbr>Point</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the function that will be executed when the Google Cloud Function is triggered.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Environment<wbr>Variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A set of key/value environment variable pairs to assign to the function.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Event<wbr>Trigger</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functioneventtrigger">Function<wbr>Event<wbr>Trigger</a></span>
    </dt>
    <dd>{{% md %}}A source that fires events in response to a condition in another service. Structure is documented below. Cannot be used with `trigger_http`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Https<wbr>Trigger<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URL which triggers function execution. Returned only if `trigger_http` is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to the function.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Max<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The limit on the maximum number of function instances that may coexist at a given time.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A user-defined name of the function. Function names must be unique globally.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Project of the function. If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Region of function. Currently can be only "us-central1". If it is not provided, the provider region is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Runtime</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The runtime in which the function is going to run.
Eg. `"nodejs8"`, `"nodejs10"`, `"python37"`, `"go111"`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Service<wbr>Account<wbr>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}If provided, the self-provided service account to run the function with.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Source<wbr>Archive<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The GCS bucket containing the zip archive which contains the function.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Source<wbr>Archive<wbr>Object</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The source archive object (file) in archive bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Source<wbr>Repository</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functionsourcerepository">*Function<wbr>Source<wbr>Repository</a></span>
    </dt>
    <dd>{{% md %}}Represents parameters related to source repository where a function is hosted.
Cannot be set alongside `source_archive_bucket` or `source_archive_object`. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for the function. Default value is 60 seconds. Cannot be more than 540 seconds.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Trigger<wbr>Http</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Boolean variable. Any HTTP request (of a supported type) to the endpoint will trigger function execution. Supported HTTP request types are: POST, PUT, GET, DELETE, and OPTIONS. Endpoint is returned as `https_trigger_url`. Cannot be used with `trigger_bucket` and `trigger_topic`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Vpc<wbr>Connector</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The VPC Network Connector that this cloud function can connect to. It can be either the fully-qualified URI, or the short name of the network connector resource. The format of this field is `projects/*/locations/*/connectors/*`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>available<wbr>Memory<wbr>Mb</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Memory (in MB), available to the function. Default value is 256MB. Allowed values are: 128MB, 256MB, 512MB, 1024MB, and 2048MB.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of the function.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>entry<wbr>Point</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the function that will be executed when the Google Cloud Function is triggered.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>environment<wbr>Variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}A set of key/value environment variable pairs to assign to the function.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>event<wbr>Trigger</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functioneventtrigger">Function<wbr>Event<wbr>Trigger</a></span>
    </dt>
    <dd>{{% md %}}A source that fires events in response to a condition in another service. Structure is documented below. Cannot be used with `trigger_http`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>https<wbr>Trigger<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}URL which triggers function execution. Returned only if `trigger_http` is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to the function.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>max<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The limit on the maximum number of function instances that may coexist at a given time.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A user-defined name of the function. Function names must be unique globally.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Project of the function. If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Region of function. Currently can be only "us-central1". If it is not provided, the provider region is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>runtime</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The runtime in which the function is going to run.
Eg. `"nodejs8"`, `"nodejs10"`, `"python37"`, `"go111"`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>service<wbr>Account<wbr>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}If provided, the self-provided service account to run the function with.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>source<wbr>Archive<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The GCS bucket containing the zip archive which contains the function.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>source<wbr>Archive<wbr>Object</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The source archive object (file) in archive bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>source<wbr>Repository</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functionsourcerepository">Function<wbr>Source<wbr>Repository?</a></span>
    </dt>
    <dd>{{% md %}}Represents parameters related to source repository where a function is hosted.
Cannot be set alongside `source_archive_bucket` or `source_archive_object`. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for the function. Default value is 60 seconds. Cannot be more than 540 seconds.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>trigger<wbr>Http</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Boolean variable. Any HTTP request (of a supported type) to the endpoint will trigger function execution. Supported HTTP request types are: POST, PUT, GET, DELETE, and OPTIONS. Endpoint is returned as `https_trigger_url`. Cannot be used with `trigger_bucket` and `trigger_topic`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vpc<wbr>Connector</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The VPC Network Connector that this cloud function can connect to. It can be either the fully-qualified URI, or the short name of the network connector resource. The format of this field is `projects/*/locations/*/connectors/*`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>available_<wbr>memory_<wbr>mb</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Memory (in MB), available to the function. Default value is 256MB. Allowed values are: 128MB, 256MB, 512MB, 1024MB, and 2048MB.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Description of the function.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>entry_<wbr>point</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the function that will be executed when the Google Cloud Function is triggered.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>environment_<wbr>variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A set of key/value environment variable pairs to assign to the function.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>event_<wbr>trigger</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functioneventtrigger">Dict[Function<wbr>Event<wbr>Trigger]</a></span>
    </dt>
    <dd>{{% md %}}A source that fires events in response to a condition in another service. Structure is documented below. Cannot be used with `trigger_http`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>https_<wbr>trigger_<wbr>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}URL which triggers function execution. Returned only if `trigger_http` is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to the function.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>max_<wbr>instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The limit on the maximum number of function instances that may coexist at a given time.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A user-defined name of the function. Function names must be unique globally.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Project of the function. If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Region of function. Currently can be only "us-central1". If it is not provided, the provider region is used.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>runtime</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The runtime in which the function is going to run.
Eg. `"nodejs8"`, `"nodejs10"`, `"python37"`, `"go111"`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>service_<wbr>account_<wbr>email</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}If provided, the self-provided service account to run the function with.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>source_<wbr>archive_<wbr>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The GCS bucket containing the zip archive which contains the function.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>source_<wbr>archive_<wbr>object</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The source archive object (file) in archive bucket.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>source_<wbr>repository</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functionsourcerepository">Dict[Function<wbr>Source<wbr>Repository]</a></span>
    </dt>
    <dd>{{% md %}}Represents parameters related to source repository where a function is hosted.
Cannot be set alongside `source_archive_bucket` or `source_archive_object`. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for the function. Default value is 60 seconds. Cannot be more than 540 seconds.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>trigger_<wbr>http</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Boolean variable. Any HTTP request (of a supported type) to the endpoint will trigger function execution. Supported HTTP request types are: POST, PUT, GET, DELETE, and OPTIONS. Endpoint is returned as `https_trigger_url`. Cannot be used with `trigger_bucket` and `trigger_topic`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>vpc_<wbr>connector</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The VPC Network Connector that this cloud function can connect to. It can be either the fully-qualified URI, or the short name of the network connector resource. The format of this field is `projects/*/locations/*/connectors/*`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Function Resource

Get an existing Function resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/cloudfunctions/#FunctionState">FunctionState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/cloudfunctions/#Function">Function</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>available_memory_mb=None<span class="p">, </span>description=None<span class="p">, </span>entry_point=None<span class="p">, </span>environment_variables=None<span class="p">, </span>event_trigger=None<span class="p">, </span>https_trigger_url=None<span class="p">, </span>labels=None<span class="p">, </span>max_instances=None<span class="p">, </span>name=None<span class="p">, </span>project=None<span class="p">, </span>region=None<span class="p">, </span>runtime=None<span class="p">, </span>service_account_email=None<span class="p">, </span>source_archive_bucket=None<span class="p">, </span>source_archive_object=None<span class="p">, </span>source_repository=None<span class="p">, </span>timeout=None<span class="p">, </span>trigger_http=None<span class="p">, </span>vpc_connector=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetFunction<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/cloudfunctions?tab=doc#FunctionState">FunctionState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/cloudfunctions?tab=doc#Function">Function</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Cloudfunctions.Function.html">Function</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Cloudfunctions.FunctionState.html">FunctionState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Available<wbr>Memory<wbr>Mb</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Memory (in MB), available to the function. Default value is 256MB. Allowed values are: 128MB, 256MB, 512MB, 1024MB, and 2048MB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of the function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Entry<wbr>Point</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the function that will be executed when the Google Cloud Function is triggered.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Environment<wbr>Variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}A set of key/value environment variable pairs to assign to the function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Event<wbr>Trigger</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functioneventtrigger">Pulumi.<wbr>Gcp.<wbr>Cloud<wbr>Functions.<wbr>Inputs.<wbr>Function<wbr>Event<wbr>Trigger<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}A source that fires events in response to a condition in another service. Structure is documented below. Cannot be used with `trigger_http`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Https<wbr>Trigger<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}URL which triggers function execution. Returned only if `trigger_http` is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to the function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The limit on the maximum number of function instances that may coexist at a given time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A user-defined name of the function. Function names must be unique globally.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Project of the function. If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Region of function. Currently can be only "us-central1". If it is not provided, the provider region is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Runtime</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The runtime in which the function is going to run.
Eg. `"nodejs8"`, `"nodejs10"`, `"python37"`, `"go111"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Account<wbr>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If provided, the self-provided service account to run the function with.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Archive<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The GCS bucket containing the zip archive which contains the function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Archive<wbr>Object</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The source archive object (file) in archive bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Repository</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functionsourcerepository">Pulumi.<wbr>Gcp.<wbr>Cloud<wbr>Functions.<wbr>Inputs.<wbr>Function<wbr>Source<wbr>Repository<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Represents parameters related to source repository where a function is hosted.
Cannot be set alongside `source_archive_bucket` or `source_archive_object`. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for the function. Default value is 60 seconds. Cannot be more than 540 seconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Trigger<wbr>Http</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Boolean variable. Any HTTP request (of a supported type) to the endpoint will trigger function execution. Supported HTTP request types are: POST, PUT, GET, DELETE, and OPTIONS. Endpoint is returned as `https_trigger_url`. Cannot be used with `trigger_bucket` and `trigger_topic`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpc<wbr>Connector</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The VPC Network Connector that this cloud function can connect to. It can be either the fully-qualified URI, or the short name of the network connector resource. The format of this field is `projects/*/locations/*/connectors/*`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Available<wbr>Memory<wbr>Mb</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Memory (in MB), available to the function. Default value is 256MB. Allowed values are: 128MB, 256MB, 512MB, 1024MB, and 2048MB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Description of the function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Entry<wbr>Point</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Name of the function that will be executed when the Google Cloud Function is triggered.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Environment<wbr>Variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A set of key/value environment variable pairs to assign to the function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Event<wbr>Trigger</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functioneventtrigger">*Function<wbr>Event<wbr>Trigger</a></span>
    </dt>
    <dd>{{% md %}}A source that fires events in response to a condition in another service. Structure is documented below. Cannot be used with `trigger_http`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Https<wbr>Trigger<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}URL which triggers function execution. Returned only if `trigger_http` is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to the function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The limit on the maximum number of function instances that may coexist at a given time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A user-defined name of the function. Function names must be unique globally.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Project of the function. If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Region of function. Currently can be only "us-central1". If it is not provided, the provider region is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Runtime</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The runtime in which the function is going to run.
Eg. `"nodejs8"`, `"nodejs10"`, `"python37"`, `"go111"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Account<wbr>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}If provided, the self-provided service account to run the function with.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Archive<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The GCS bucket containing the zip archive which contains the function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Archive<wbr>Object</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The source archive object (file) in archive bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Source<wbr>Repository</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functionsourcerepository">*Function<wbr>Source<wbr>Repository</a></span>
    </dt>
    <dd>{{% md %}}Represents parameters related to source repository where a function is hosted.
Cannot be set alongside `source_archive_bucket` or `source_archive_object`. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for the function. Default value is 60 seconds. Cannot be more than 540 seconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Trigger<wbr>Http</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Boolean variable. Any HTTP request (of a supported type) to the endpoint will trigger function execution. Supported HTTP request types are: POST, PUT, GET, DELETE, and OPTIONS. Endpoint is returned as `https_trigger_url`. Cannot be used with `trigger_bucket` and `trigger_topic`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Vpc<wbr>Connector</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The VPC Network Connector that this cloud function can connect to. It can be either the fully-qualified URI, or the short name of the network connector resource. The format of this field is `projects/*/locations/*/connectors/*`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>available<wbr>Memory<wbr>Mb</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Memory (in MB), available to the function. Default value is 256MB. Allowed values are: 128MB, 256MB, 512MB, 1024MB, and 2048MB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Description of the function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>entry<wbr>Point</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Name of the function that will be executed when the Google Cloud Function is triggered.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>environment<wbr>Variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}A set of key/value environment variable pairs to assign to the function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>event<wbr>Trigger</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functioneventtrigger">Function<wbr>Event<wbr>Trigger?</a></span>
    </dt>
    <dd>{{% md %}}A source that fires events in response to a condition in another service. Structure is documented below. Cannot be used with `trigger_http`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>https<wbr>Trigger<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}URL which triggers function execution. Returned only if `trigger_http` is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to the function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The limit on the maximum number of function instances that may coexist at a given time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A user-defined name of the function. Function names must be unique globally.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Project of the function. If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Region of function. Currently can be only "us-central1". If it is not provided, the provider region is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>runtime</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The runtime in which the function is going to run.
Eg. `"nodejs8"`, `"nodejs10"`, `"python37"`, `"go111"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service<wbr>Account<wbr>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}If provided, the self-provided service account to run the function with.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source<wbr>Archive<wbr>Bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The GCS bucket containing the zip archive which contains the function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source<wbr>Archive<wbr>Object</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The source archive object (file) in archive bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source<wbr>Repository</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functionsourcerepository">Function<wbr>Source<wbr>Repository?</a></span>
    </dt>
    <dd>{{% md %}}Represents parameters related to source repository where a function is hosted.
Cannot be set alongside `source_archive_bucket` or `source_archive_object`. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for the function. Default value is 60 seconds. Cannot be more than 540 seconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>trigger<wbr>Http</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Boolean variable. Any HTTP request (of a supported type) to the endpoint will trigger function execution. Supported HTTP request types are: POST, PUT, GET, DELETE, and OPTIONS. Endpoint is returned as `https_trigger_url`. Cannot be used with `trigger_bucket` and `trigger_topic`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpc<wbr>Connector</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The VPC Network Connector that this cloud function can connect to. It can be either the fully-qualified URI, or the short name of the network connector resource. The format of this field is `projects/*/locations/*/connectors/*`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>available_<wbr>memory_<wbr>mb</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Memory (in MB), available to the function. Default value is 256MB. Allowed values are: 128MB, 256MB, 512MB, 1024MB, and 2048MB.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Description of the function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>entry_<wbr>point</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the function that will be executed when the Google Cloud Function is triggered.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>environment_<wbr>variables</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A set of key/value environment variable pairs to assign to the function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>event_<wbr>trigger</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functioneventtrigger">Dict[Function<wbr>Event<wbr>Trigger]</a></span>
    </dt>
    <dd>{{% md %}}A source that fires events in response to a condition in another service. Structure is documented below. Cannot be used with `trigger_http`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>https_<wbr>trigger_<wbr>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}URL which triggers function execution. Returned only if `trigger_http` is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}A set of key/value label pairs to assign to the function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max_<wbr>instances</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The limit on the maximum number of function instances that may coexist at a given time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A user-defined name of the function. Function names must be unique globally.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Project of the function. If it is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Region of function. Currently can be only "us-central1". If it is not provided, the provider region is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>runtime</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The runtime in which the function is going to run.
Eg. `"nodejs8"`, `"nodejs10"`, `"python37"`, `"go111"`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service_<wbr>account_<wbr>email</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}If provided, the self-provided service account to run the function with.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source_<wbr>archive_<wbr>bucket</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The GCS bucket containing the zip archive which contains the function.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source_<wbr>archive_<wbr>object</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The source archive object (file) in archive bucket.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>source_<wbr>repository</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functionsourcerepository">Dict[Function<wbr>Source<wbr>Repository]</a></span>
    </dt>
    <dd>{{% md %}}Represents parameters related to source repository where a function is hosted.
Cannot be set alongside `source_archive_bucket` or `source_archive_object`. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>timeout</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}Timeout (in seconds) for the function. Default value is 60 seconds. Cannot be more than 540 seconds.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>trigger_<wbr>http</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Boolean variable. Any HTTP request (of a supported type) to the endpoint will trigger function execution. Supported HTTP request types are: POST, PUT, GET, DELETE, and OPTIONS. Endpoint is returned as `https_trigger_url`. Cannot be used with `trigger_bucket` and `trigger_topic`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>vpc_<wbr>connector</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The VPC Network Connector that this cloud function can connect to. It can be either the fully-qualified URI, or the short name of the network connector resource. The format of this field is `projects/*/locations/*/connectors/*`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Function<wbr>Event<wbr>Trigger</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#FunctionEventTrigger">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#FunctionEventTrigger">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/cloudfunctions?tab=doc#FunctionEventTriggerArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/cloudfunctions?tab=doc#FunctionEventTriggerOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Event<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of event to observe. For example: `"google.storage.object.finalize"`.
See the documentation on [calling Cloud Functions](https://cloud.google.com/functions/docs/calling/) for a
full reference of accepted triggers.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Failure<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functioneventtriggerfailurepolicy">Pulumi.<wbr>Gcp.<wbr>Cloud<wbr>Functions.<wbr>Inputs.<wbr>Function<wbr>Event<wbr>Trigger<wbr>Failure<wbr>Policy<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Specifies policy for failed executions. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Required. The name or partial URI of the resource from
which to observe events. For example, `"myBucket"` or `"projects/my-project/topics/my-topic"`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Event<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of event to observe. For example: `"google.storage.object.finalize"`.
See the documentation on [calling Cloud Functions](https://cloud.google.com/functions/docs/calling/) for a
full reference of accepted triggers.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Failure<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functioneventtriggerfailurepolicy">*Function<wbr>Event<wbr>Trigger<wbr>Failure<wbr>Policy</a></span>
    </dt>
    <dd>{{% md %}}Specifies policy for failed executions. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Resource</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Required. The name or partial URI of the resource from
which to observe events. For example, `"myBucket"` or `"projects/my-project/topics/my-topic"`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>event<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of event to observe. For example: `"google.storage.object.finalize"`.
See the documentation on [calling Cloud Functions](https://cloud.google.com/functions/docs/calling/) for a
full reference of accepted triggers.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>failure<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functioneventtriggerfailurepolicy">Function<wbr>Event<wbr>Trigger<wbr>Failure<wbr>Policy?</a></span>
    </dt>
    <dd>{{% md %}}Specifies policy for failed executions. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Required. The name or partial URI of the resource from
which to observe events. For example, `"myBucket"` or `"projects/my-project/topics/my-topic"`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>event<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of event to observe. For example: `"google.storage.object.finalize"`.
See the documentation on [calling Cloud Functions](https://cloud.google.com/functions/docs/calling/) for a
full reference of accepted triggers.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>failure<wbr>Policy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#functioneventtriggerfailurepolicy">Dict[Function<wbr>Event<wbr>Trigger<wbr>Failure<wbr>Policy]</a></span>
    </dt>
    <dd>{{% md %}}Specifies policy for failed executions. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>resource</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Required. The name or partial URI of the resource from
which to observe events. For example, `"myBucket"` or `"projects/my-project/topics/my-topic"`
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Function<wbr>Event<wbr>Trigger<wbr>Failure<wbr>Policy</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#FunctionEventTriggerFailurePolicy">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#FunctionEventTriggerFailurePolicy">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/cloudfunctions?tab=doc#FunctionEventTriggerFailurePolicyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/cloudfunctions?tab=doc#FunctionEventTriggerFailurePolicyOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Retry</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the function should be retried on failure. Defaults to `false`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Retry</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the function should be retried on failure. Defaults to `false`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>retry</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Whether the function should be retried on failure. Defaults to `false`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>retry</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether the function should be retried on failure. Defaults to `false`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Function<wbr>Source<wbr>Repository</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#FunctionSourceRepository">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#FunctionSourceRepository">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/cloudfunctions?tab=doc#FunctionSourceRepositoryArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/cloudfunctions?tab=doc#FunctionSourceRepositoryOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Deployed<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The URL pointing to the hosted repository where the function is defined. There are supported Cloud Source Repository URLs in the following formats:
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Deployed<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The URL pointing to the hosted repository where the function is defined. There are supported Cloud Source Repository URLs in the following formats:
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>deployed<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The URL pointing to the hosted repository where the function is defined. There are supported Cloud Source Repository URLs in the following formats:
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>deployed<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The URL pointing to the hosted repository where the function is defined. There are supported Cloud Source Repository URLs in the following formats:
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







