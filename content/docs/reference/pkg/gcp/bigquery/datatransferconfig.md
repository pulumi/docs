
---
title: "DataTransferConfig"
block_external_search_index: true
---



Represents a data transfer configuration. A transfer configuration
contains all metadata needed to perform a data transfer.


To get more information about Config, see:

* [API documentation](https://cloud.google.com/bigquery/docs/reference/datatransfer/rest/v1/projects.locations.transferConfigs/create)
* How-to Guides
    * [Official Documentation](https://cloud.google.com/bigquery/docs/reference/datatransfer/rest/)

> This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/bigquery_data_transfer_config.html.markdown.



## Create a DataTransferConfig Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/bigquery/#DataTransferConfig">DataTransferConfig</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/bigquery/#DataTransferConfigArgs">DataTransferConfigArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">DataTransferConfig</span><span class="p">(resource_name, opts=None, </span>data_refresh_window_days=None<span class="p">, </span>data_source_id=None<span class="p">, </span>destination_dataset_id=None<span class="p">, </span>disabled=None<span class="p">, </span>display_name=None<span class="p">, </span>location=None<span class="p">, </span>params=None<span class="p">, </span>project=None<span class="p">, </span>schedule=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewDataTransferConfig<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/bigquery?tab=doc#DataTransferConfigArgs">DataTransferConfigArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/bigquery?tab=doc#DataTransferConfig">DataTransferConfig</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Bigquery.DataTransferConfig.html">DataTransferConfig</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.BigQuery.DataTransferConfigArgs.html">DataTransferConfigArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Data<wbr>Refresh<wbr>Window<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of days to look back to automatically refresh the data. For example, if dataRefreshWindowDays = 10, then
every day BigQuery reingests data for [today-10, today-1], rather than ingesting data for just [today-1]. Only valid if
the data source supports the feature. Set the value to 0 to use the default value.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Data<wbr>Source<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The data source id. Cannot be changed once the transfer config is created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Destination<wbr>Dataset<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The BigQuery target dataset id.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}When set to true, no runs are scheduled for a given transfer.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The user specified display name for the transfer config.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The geographic location where the transfer config should reside. Examples: US, EU, asia-northeast1. The default value is
US.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Params</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string></span>
    </dt>
    <dd>{{% md %}}These parameters are specific to each data source.
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
        <span>Schedule</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Data transfer schedule. If the data source does not support a custom schedule, this should be empty. If it is empty, the
default value for the data source will be used. The specified times are in UTC. Examples of valid format: 1st,3rd monday
of month 15:30, every wed,fri of jan, jun 13:15, and first sunday of quarter 00:00. See more explanation about the
format here: https://cloud.google.com/appengine/docs/flexible/python/scheduling-jobs-with-cron-yaml#the_schedule_format
NOTE: the granularity should be at least 8 hours, or less frequent.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Data<wbr>Refresh<wbr>Window<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of days to look back to automatically refresh the data. For example, if dataRefreshWindowDays = 10, then
every day BigQuery reingests data for [today-10, today-1], rather than ingesting data for just [today-1]. Only valid if
the data source supports the feature. Set the value to 0 to use the default value.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Data<wbr>Source<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The data source id. Cannot be changed once the transfer config is created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Destination<wbr>Dataset<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The BigQuery target dataset id.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}When set to true, no runs are scheduled for a given transfer.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The user specified display name for the transfer config.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The geographic location where the transfer config should reside. Examples: US, EU, asia-northeast1. The default value is
US.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Params</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}These parameters are specific to each data source.
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
        <span>Schedule</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Data transfer schedule. If the data source does not support a custom schedule, this should be empty. If it is empty, the
default value for the data source will be used. The specified times are in UTC. Examples of valid format: 1st,3rd monday
of month 15:30, every wed,fri of jan, jun 13:15, and first sunday of quarter 00:00. See more explanation about the
format here: https://cloud.google.com/appengine/docs/flexible/python/scheduling-jobs-with-cron-yaml#the_schedule_format
NOTE: the granularity should be at least 8 hours, or less frequent.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>data<wbr>Refresh<wbr>Window<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of days to look back to automatically refresh the data. For example, if dataRefreshWindowDays = 10, then
every day BigQuery reingests data for [today-10, today-1], rather than ingesting data for just [today-1]. Only valid if
the data source supports the feature. Set the value to 0 to use the default value.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>data<wbr>Source<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The data source id. Cannot be changed once the transfer config is created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>destination<wbr>Dataset<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The BigQuery target dataset id.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}When set to true, no runs are scheduled for a given transfer.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The user specified display name for the transfer config.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The geographic location where the transfer config should reside. Examples: US, EU, asia-northeast1. The default value is
US.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>params</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}These parameters are specific to each data source.
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
        <span>schedule</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Data transfer schedule. If the data source does not support a custom schedule, this should be empty. If it is empty, the
default value for the data source will be used. The specified times are in UTC. Examples of valid format: 1st,3rd monday
of month 15:30, every wed,fri of jan, jun 13:15, and first sunday of quarter 00:00. See more explanation about the
format here: https://cloud.google.com/appengine/docs/flexible/python/scheduling-jobs-with-cron-yaml#the_schedule_format
NOTE: the granularity should be at least 8 hours, or less frequent.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>data_<wbr>refresh_<wbr>window_<wbr>days</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of days to look back to automatically refresh the data. For example, if dataRefreshWindowDays = 10, then
every day BigQuery reingests data for [today-10, today-1], rather than ingesting data for just [today-1]. Only valid if
the data source supports the feature. Set the value to 0 to use the default value.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>data_<wbr>source_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The data source id. Cannot be changed once the transfer config is created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>destination_<wbr>dataset_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The BigQuery target dataset id.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When set to true, no runs are scheduled for a given transfer.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>display_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The user specified display name for the transfer config.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The geographic location where the transfer config should reside. Examples: US, EU, asia-northeast1. The default value is
US.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>params</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}These parameters are specific to each data source.
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
        <span>schedule</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Data transfer schedule. If the data source does not support a custom schedule, this should be empty. If it is empty, the
default value for the data source will be used. The specified times are in UTC. Examples of valid format: 1st,3rd monday
of month 15:30, every wed,fri of jan, jun 13:15, and first sunday of quarter 00:00. See more explanation about the
format here: https://cloud.google.com/appengine/docs/flexible/python/scheduling-jobs-with-cron-yaml#the_schedule_format
NOTE: the granularity should be at least 8 hours, or less frequent.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## DataTransferConfig Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Data<wbr>Refresh<wbr>Window<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of days to look back to automatically refresh the data. For example, if dataRefreshWindowDays = 10, then
every day BigQuery reingests data for [today-10, today-1], rather than ingesting data for just [today-1]. Only valid if
the data source supports the feature. Set the value to 0 to use the default value.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Data<wbr>Source<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The data source id. Cannot be changed once the transfer config is created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Destination<wbr>Dataset<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The BigQuery target dataset id.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}When set to true, no runs are scheduled for a given transfer.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The user specified display name for the transfer config.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The geographic location where the transfer config should reside. Examples: US, EU, asia-northeast1. The default value is
US.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The resource name of the transfer config. Transfer config names have the form
projects/{projectId}/locations/{location}/transferConfigs/{configId}. Where configId is usually a uuid, but this is not
required. The name is ignored when creating a transfer config.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Params</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string></span>
    </dt>
    <dd>{{% md %}}These parameters are specific to each data source.
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
        <span>Schedule</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Data transfer schedule. If the data source does not support a custom schedule, this should be empty. If it is empty, the
default value for the data source will be used. The specified times are in UTC. Examples of valid format: 1st,3rd monday
of month 15:30, every wed,fri of jan, jun 13:15, and first sunday of quarter 00:00. See more explanation about the
format here: https://cloud.google.com/appengine/docs/flexible/python/scheduling-jobs-with-cron-yaml#the_schedule_format
NOTE: the granularity should be at least 8 hours, or less frequent.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Data<wbr>Refresh<wbr>Window<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of days to look back to automatically refresh the data. For example, if dataRefreshWindowDays = 10, then
every day BigQuery reingests data for [today-10, today-1], rather than ingesting data for just [today-1]. Only valid if
the data source supports the feature. Set the value to 0 to use the default value.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Data<wbr>Source<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The data source id. Cannot be changed once the transfer config is created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Destination<wbr>Dataset<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The BigQuery target dataset id.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}When set to true, no runs are scheduled for a given transfer.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The user specified display name for the transfer config.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The geographic location where the transfer config should reside. Examples: US, EU, asia-northeast1. The default value is
US.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The resource name of the transfer config. Transfer config names have the form
projects/{projectId}/locations/{location}/transferConfigs/{configId}. Where configId is usually a uuid, but this is not
required. The name is ignored when creating a transfer config.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Params</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}These parameters are specific to each data source.
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
        <span>Schedule</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Data transfer schedule. If the data source does not support a custom schedule, this should be empty. If it is empty, the
default value for the data source will be used. The specified times are in UTC. Examples of valid format: 1st,3rd monday
of month 15:30, every wed,fri of jan, jun 13:15, and first sunday of quarter 00:00. See more explanation about the
format here: https://cloud.google.com/appengine/docs/flexible/python/scheduling-jobs-with-cron-yaml#the_schedule_format
NOTE: the granularity should be at least 8 hours, or less frequent.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>data<wbr>Refresh<wbr>Window<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of days to look back to automatically refresh the data. For example, if dataRefreshWindowDays = 10, then
every day BigQuery reingests data for [today-10, today-1], rather than ingesting data for just [today-1]. Only valid if
the data source supports the feature. Set the value to 0 to use the default value.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>data<wbr>Source<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The data source id. Cannot be changed once the transfer config is created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>destination<wbr>Dataset<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The BigQuery target dataset id.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}When set to true, no runs are scheduled for a given transfer.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The user specified display name for the transfer config.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The geographic location where the transfer config should reside. Examples: US, EU, asia-northeast1. The default value is
US.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The resource name of the transfer config. Transfer config names have the form
projects/{projectId}/locations/{location}/transferConfigs/{configId}. Where configId is usually a uuid, but this is not
required. The name is ignored when creating a transfer config.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>params</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}These parameters are specific to each data source.
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
        <span>schedule</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Data transfer schedule. If the data source does not support a custom schedule, this should be empty. If it is empty, the
default value for the data source will be used. The specified times are in UTC. Examples of valid format: 1st,3rd monday
of month 15:30, every wed,fri of jan, jun 13:15, and first sunday of quarter 00:00. See more explanation about the
format here: https://cloud.google.com/appengine/docs/flexible/python/scheduling-jobs-with-cron-yaml#the_schedule_format
NOTE: the granularity should be at least 8 hours, or less frequent.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>data_<wbr>refresh_<wbr>window_<wbr>days</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of days to look back to automatically refresh the data. For example, if dataRefreshWindowDays = 10, then
every day BigQuery reingests data for [today-10, today-1], rather than ingesting data for just [today-1]. Only valid if
the data source supports the feature. Set the value to 0 to use the default value.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>data_<wbr>source_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The data source id. Cannot be changed once the transfer config is created.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>destination_<wbr>dataset_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The BigQuery target dataset id.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When set to true, no runs are scheduled for a given transfer.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>display_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The user specified display name for the transfer config.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The geographic location where the transfer config should reside. Examples: US, EU, asia-northeast1. The default value is
US.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The resource name of the transfer config. Transfer config names have the form
projects/{projectId}/locations/{location}/transferConfigs/{configId}. Where configId is usually a uuid, but this is not
required. The name is ignored when creating a transfer config.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>params</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}These parameters are specific to each data source.
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
        <span>schedule</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Data transfer schedule. If the data source does not support a custom schedule, this should be empty. If it is empty, the
default value for the data source will be used. The specified times are in UTC. Examples of valid format: 1st,3rd monday
of month 15:30, every wed,fri of jan, jun 13:15, and first sunday of quarter 00:00. See more explanation about the
format here: https://cloud.google.com/appengine/docs/flexible/python/scheduling-jobs-with-cron-yaml#the_schedule_format
NOTE: the granularity should be at least 8 hours, or less frequent.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing DataTransferConfig Resource

Get an existing DataTransferConfig resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/bigquery/#DataTransferConfigState">DataTransferConfigState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/bigquery/#DataTransferConfig">DataTransferConfig</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>data_refresh_window_days=None<span class="p">, </span>data_source_id=None<span class="p">, </span>destination_dataset_id=None<span class="p">, </span>disabled=None<span class="p">, </span>display_name=None<span class="p">, </span>location=None<span class="p">, </span>name=None<span class="p">, </span>params=None<span class="p">, </span>project=None<span class="p">, </span>schedule=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetDataTransferConfig<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/bigquery?tab=doc#DataTransferConfigState">DataTransferConfigState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/bigquery?tab=doc#DataTransferConfig">DataTransferConfig</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Bigquery.DataTransferConfig.html">DataTransferConfig</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Bigquery.DataTransferConfigState.html">DataTransferConfigState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Data<wbr>Refresh<wbr>Window<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of days to look back to automatically refresh the data. For example, if dataRefreshWindowDays = 10, then
every day BigQuery reingests data for [today-10, today-1], rather than ingesting data for just [today-1]. Only valid if
the data source supports the feature. Set the value to 0 to use the default value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Data<wbr>Source<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The data source id. Cannot be changed once the transfer config is created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Destination<wbr>Dataset<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The BigQuery target dataset id.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}When set to true, no runs are scheduled for a given transfer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The user specified display name for the transfer config.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The geographic location where the transfer config should reside. Examples: US, EU, asia-northeast1. The default value is
US.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The resource name of the transfer config. Transfer config names have the form
projects/{projectId}/locations/{location}/transferConfigs/{configId}. Where configId is usually a uuid, but this is not
required. The name is ignored when creating a transfer config.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Params</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, string>?</span>
    </dt>
    <dd>{{% md %}}These parameters are specific to each data source.
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
        <span>Schedule</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Data transfer schedule. If the data source does not support a custom schedule, this should be empty. If it is empty, the
default value for the data source will be used. The specified times are in UTC. Examples of valid format: 1st,3rd monday
of month 15:30, every wed,fri of jan, jun 13:15, and first sunday of quarter 00:00. See more explanation about the
format here: https://cloud.google.com/appengine/docs/flexible/python/scheduling-jobs-with-cron-yaml#the_schedule_format
NOTE: the granularity should be at least 8 hours, or less frequent.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Data<wbr>Refresh<wbr>Window<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of days to look back to automatically refresh the data. For example, if dataRefreshWindowDays = 10, then
every day BigQuery reingests data for [today-10, today-1], rather than ingesting data for just [today-1]. Only valid if
the data source supports the feature. Set the value to 0 to use the default value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Data<wbr>Source<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The data source id. Cannot be changed once the transfer config is created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Destination<wbr>Dataset<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The BigQuery target dataset id.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}When set to true, no runs are scheduled for a given transfer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The user specified display name for the transfer config.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The geographic location where the transfer config should reside. Examples: US, EU, asia-northeast1. The default value is
US.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The resource name of the transfer config. Transfer config names have the form
projects/{projectId}/locations/{location}/transferConfigs/{configId}. Where configId is usually a uuid, but this is not
required. The name is ignored when creating a transfer config.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Params</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}These parameters are specific to each data source.
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
        <span>Schedule</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Data transfer schedule. If the data source does not support a custom schedule, this should be empty. If it is empty, the
default value for the data source will be used. The specified times are in UTC. Examples of valid format: 1st,3rd monday
of month 15:30, every wed,fri of jan, jun 13:15, and first sunday of quarter 00:00. See more explanation about the
format here: https://cloud.google.com/appengine/docs/flexible/python/scheduling-jobs-with-cron-yaml#the_schedule_format
NOTE: the granularity should be at least 8 hours, or less frequent.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>data<wbr>Refresh<wbr>Window<wbr>Days</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of days to look back to automatically refresh the data. For example, if dataRefreshWindowDays = 10, then
every day BigQuery reingests data for [today-10, today-1], rather than ingesting data for just [today-1]. Only valid if
the data source supports the feature. Set the value to 0 to use the default value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>data<wbr>Source<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The data source id. Cannot be changed once the transfer config is created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>destination<wbr>Dataset<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The BigQuery target dataset id.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}When set to true, no runs are scheduled for a given transfer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>display<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The user specified display name for the transfer config.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The geographic location where the transfer config should reside. Examples: US, EU, asia-northeast1. The default value is
US.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The resource name of the transfer config. Transfer config names have the form
projects/{projectId}/locations/{location}/transferConfigs/{configId}. Where configId is usually a uuid, but this is not
required. The name is ignored when creating a transfer config.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>params</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}?</span>
    </dt>
    <dd>{{% md %}}These parameters are specific to each data source.
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
        <span>schedule</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Data transfer schedule. If the data source does not support a custom schedule, this should be empty. If it is empty, the
default value for the data source will be used. The specified times are in UTC. Examples of valid format: 1st,3rd monday
of month 15:30, every wed,fri of jan, jun 13:15, and first sunday of quarter 00:00. See more explanation about the
format here: https://cloud.google.com/appengine/docs/flexible/python/scheduling-jobs-with-cron-yaml#the_schedule_format
NOTE: the granularity should be at least 8 hours, or less frequent.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>data_<wbr>refresh_<wbr>window_<wbr>days</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of days to look back to automatically refresh the data. For example, if dataRefreshWindowDays = 10, then
every day BigQuery reingests data for [today-10, today-1], rather than ingesting data for just [today-1]. Only valid if
the data source supports the feature. Set the value to 0 to use the default value.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>data_<wbr>source_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The data source id. Cannot be changed once the transfer config is created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>destination_<wbr>dataset_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The BigQuery target dataset id.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>disabled</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}When set to true, no runs are scheduled for a given transfer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>display_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The user specified display name for the transfer config.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The geographic location where the transfer config should reside. Examples: US, EU, asia-northeast1. The default value is
US.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The resource name of the transfer config. Transfer config names have the form
projects/{projectId}/locations/{location}/transferConfigs/{configId}. Where configId is usually a uuid, but this is not
required. The name is ignored when creating a transfer config.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>params</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}These parameters are specific to each data source.
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
        <span>schedule</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Data transfer schedule. If the data source does not support a custom schedule, this should be empty. If it is empty, the
default value for the data source will be used. The specified times are in UTC. Examples of valid format: 1st,3rd monday
of month 15:30, every wed,fri of jan, jun 13:15, and first sunday of quarter 00:00. See more explanation about the
format here: https://cloud.google.com/appengine/docs/flexible/python/scheduling-jobs-with-cron-yaml#the_schedule_format
NOTE: the granularity should be at least 8 hours, or less frequent.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}











<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-gcp">https://github.com/pulumi/pulumi-gcp</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

