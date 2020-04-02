
---
title: "FolderSink"
block_external_search_index: true
---

Manages a folder-level logging sink. For more information see
[the official documentation](https://cloud.google.com/logging/docs/) and
[Exporting Logs in the API](https://cloud.google.com/logging/docs/api/tasks/exporting-logs).

Note that you must have the "Logs Configuration Writer" IAM role (`roles/logging.configWriter`)
granted to the credentials used with this provider.

> This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/logging_folder_sink.html.markdown.



## Create a FolderSink Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/logging/#FolderSink">FolderSink</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/logging/#FolderSinkArgs">FolderSinkArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">FolderSink</span><span class="p">(resource_name, opts=None, </span>bigquery_options=None<span class="p">, </span>destination=None<span class="p">, </span>filter=None<span class="p">, </span>folder=None<span class="p">, </span>include_children=None<span class="p">, </span>name=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewFolderSink<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/logging?tab=doc#FolderSinkArgs">FolderSinkArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/logging?tab=doc#FolderSink">FolderSink</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Logging.FolderSink.html">FolderSink</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Logging.FolderSinkArgs.html">FolderSinkArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Bigquery<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#foldersinkbigqueryoptions">Folder<wbr>Sink<wbr>Bigquery<wbr>Options<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Options that affect sinks exporting data to BigQuery. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Destination</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
```typescript
import * as pulumi from "@pulumi/pulumi";
```
The writer associated with the sink must have access to write to the above resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Folder</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The folder to be exported to the sink. Note that either [FOLDER_ID] or "folders/[FOLDER_ID]" is
accepted.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Include<wbr>Children</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether or not to include children folders in the sink export. If true, logs
associated with child projects are also exported; otherwise only logs relating to the provided folder are included.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the logging sink.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Bigquery<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#foldersinkbigqueryoptions">*Folder<wbr>Sink<wbr>Bigquery<wbr>Options</a></span>
    </dt>
    <dd>{{% md %}}Options that affect sinks exporting data to BigQuery. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Destination</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
```typescript
import * as pulumi from "@pulumi/pulumi";
```
The writer associated with the sink must have access to write to the above resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Folder</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The folder to be exported to the sink. Note that either [FOLDER_ID] or "folders/[FOLDER_ID]" is
accepted.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Include<wbr>Children</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether or not to include children folders in the sink export. If true, logs
associated with child projects are also exported; otherwise only logs relating to the provided folder are included.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the logging sink.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>bigquery<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#foldersinkbigqueryoptions">Folder<wbr>Sink<wbr>Bigquery<wbr>Options?</a></span>
    </dt>
    <dd>{{% md %}}Options that affect sinks exporting data to BigQuery. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>destination</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
```typescript
import * as pulumi from "@pulumi/pulumi";
```
The writer associated with the sink must have access to write to the above resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>folder</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The folder to be exported to the sink. Note that either [FOLDER_ID] or "folders/[FOLDER_ID]" is
accepted.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>include<wbr>Children</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether or not to include children folders in the sink export. If true, logs
associated with child projects are also exported; otherwise only logs relating to the provided folder are included.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the logging sink.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>bigquery_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#foldersinkbigqueryoptions">Dict[Folder<wbr>Sink<wbr>Bigquery<wbr>Options]</a></span>
    </dt>
    <dd>{{% md %}}Options that affect sinks exporting data to BigQuery. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>destination</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
```typescript
import * as pulumi from "@pulumi/pulumi";
```
The writer associated with the sink must have access to write to the above resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>folder</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The folder to be exported to the sink. Note that either [FOLDER_ID] or "folders/[FOLDER_ID]" is
accepted.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>include_<wbr>children</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether or not to include children folders in the sink export. If true, logs
associated with child projects are also exported; otherwise only logs relating to the provided folder are included.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the logging sink.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## FolderSink Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Bigquery<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#foldersinkbigqueryoptions">Folder<wbr>Sink<wbr>Bigquery<wbr>Options</a></span>
    </dt>
    <dd>{{% md %}}Options that affect sinks exporting data to BigQuery. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Destination</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
```typescript
import * as pulumi from "@pulumi/pulumi";
```
The writer associated with the sink must have access to write to the above resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Folder</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The folder to be exported to the sink. Note that either [FOLDER_ID] or "folders/[FOLDER_ID]" is
accepted.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Include<wbr>Children</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether or not to include children folders in the sink export. If true, logs
associated with child projects are also exported; otherwise only logs relating to the provided folder are included.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the logging sink.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Writer<wbr>Identity</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The identity associated with this sink. This identity must be granted write access to the
configured `destination`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Bigquery<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#foldersinkbigqueryoptions">Folder<wbr>Sink<wbr>Bigquery<wbr>Options</a></span>
    </dt>
    <dd>{{% md %}}Options that affect sinks exporting data to BigQuery. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Destination</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
```typescript
import * as pulumi from "@pulumi/pulumi";
```
The writer associated with the sink must have access to write to the above resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Folder</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The folder to be exported to the sink. Note that either [FOLDER_ID] or "folders/[FOLDER_ID]" is
accepted.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Include<wbr>Children</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether or not to include children folders in the sink export. If true, logs
associated with child projects are also exported; otherwise only logs relating to the provided folder are included.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the logging sink.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Writer<wbr>Identity</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The identity associated with this sink. This identity must be granted write access to the
configured `destination`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>bigquery<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#foldersinkbigqueryoptions">Folder<wbr>Sink<wbr>Bigquery<wbr>Options</a></span>
    </dt>
    <dd>{{% md %}}Options that affect sinks exporting data to BigQuery. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>destination</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
```typescript
import * as pulumi from "@pulumi/pulumi";
```
The writer associated with the sink must have access to write to the above resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>folder</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The folder to be exported to the sink. Note that either [FOLDER_ID] or "folders/[FOLDER_ID]" is
accepted.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>include<wbr>Children</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether or not to include children folders in the sink export. If true, logs
associated with child projects are also exported; otherwise only logs relating to the provided folder are included.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the logging sink.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>writer<wbr>Identity</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The identity associated with this sink. This identity must be granted write access to the
configured `destination`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>bigquery_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#foldersinkbigqueryoptions">Dict[Folder<wbr>Sink<wbr>Bigquery<wbr>Options]</a></span>
    </dt>
    <dd>{{% md %}}Options that affect sinks exporting data to BigQuery. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>destination</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
```typescript
import * as pulumi from "@pulumi/pulumi";
```
The writer associated with the sink must have access to write to the above resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>folder</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The folder to be exported to the sink. Note that either [FOLDER_ID] or "folders/[FOLDER_ID]" is
accepted.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>include_<wbr>children</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether or not to include children folders in the sink export. If true, logs
associated with child projects are also exported; otherwise only logs relating to the provided folder are included.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the logging sink.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>writer_<wbr>identity</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The identity associated with this sink. This identity must be granted write access to the
configured `destination`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing FolderSink Resource

Get an existing FolderSink resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/logging/#FolderSinkState">FolderSinkState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/logging/#FolderSink">FolderSink</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>bigquery_options=None<span class="p">, </span>destination=None<span class="p">, </span>filter=None<span class="p">, </span>folder=None<span class="p">, </span>include_children=None<span class="p">, </span>name=None<span class="p">, </span>writer_identity=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetFolderSink<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/logging?tab=doc#FolderSinkState">FolderSinkState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/logging?tab=doc#FolderSink">FolderSink</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Logging.FolderSink.html">FolderSink</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.Logging.FolderSinkState.html">FolderSinkState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Bigquery<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#foldersinkbigqueryoptions">Folder<wbr>Sink<wbr>Bigquery<wbr>Options<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Options that affect sinks exporting data to BigQuery. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Destination</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
```typescript
import * as pulumi from "@pulumi/pulumi";
```
The writer associated with the sink must have access to write to the above resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Folder</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The folder to be exported to the sink. Note that either [FOLDER_ID] or "folders/[FOLDER_ID]" is
accepted.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Include<wbr>Children</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Whether or not to include children folders in the sink export. If true, logs
associated with child projects are also exported; otherwise only logs relating to the provided folder are included.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the logging sink.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Writer<wbr>Identity</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The identity associated with this sink. This identity must be granted write access to the
configured `destination`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Bigquery<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#foldersinkbigqueryoptions">*Folder<wbr>Sink<wbr>Bigquery<wbr>Options</a></span>
    </dt>
    <dd>{{% md %}}Options that affect sinks exporting data to BigQuery. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Destination</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
```typescript
import * as pulumi from "@pulumi/pulumi";
```
The writer associated with the sink must have access to write to the above resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Folder</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The folder to be exported to the sink. Note that either [FOLDER_ID] or "folders/[FOLDER_ID]" is
accepted.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Include<wbr>Children</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Whether or not to include children folders in the sink export. If true, logs
associated with child projects are also exported; otherwise only logs relating to the provided folder are included.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The name of the logging sink.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Writer<wbr>Identity</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The identity associated with this sink. This identity must be granted write access to the
configured `destination`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>bigquery<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#foldersinkbigqueryoptions">Folder<wbr>Sink<wbr>Bigquery<wbr>Options?</a></span>
    </dt>
    <dd>{{% md %}}Options that affect sinks exporting data to BigQuery. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>destination</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
```typescript
import * as pulumi from "@pulumi/pulumi";
```
The writer associated with the sink must have access to write to the above resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>folder</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The folder to be exported to the sink. Note that either [FOLDER_ID] or "folders/[FOLDER_ID]" is
accepted.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>include<wbr>Children</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Whether or not to include children folders in the sink export. If true, logs
associated with child projects are also exported; otherwise only logs relating to the provided folder are included.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The name of the logging sink.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>writer<wbr>Identity</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The identity associated with this sink. This identity must be granted write access to the
configured `destination`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>bigquery_<wbr>options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#foldersinkbigqueryoptions">Dict[Folder<wbr>Sink<wbr>Bigquery<wbr>Options]</a></span>
    </dt>
    <dd>{{% md %}}Options that affect sinks exporting data to BigQuery. Structure documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>destination</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The destination of the sink (or, in other words, where logs are written to). Can be a
Cloud Storage bucket, a PubSub topic, or a BigQuery dataset. Examples:
```typescript
import * as pulumi from "@pulumi/pulumi";
```
The writer associated with the sink must have access to write to the above resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>filter</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The filter to apply when exporting logs. Only log entries that match the filter are exported.
See [Advanced Log Filters](https://cloud.google.com/logging/docs/view/advanced_filters) for information on how to
write a filter.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>folder</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The folder to be exported to the sink. Note that either [FOLDER_ID] or "folders/[FOLDER_ID]" is
accepted.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>include_<wbr>children</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether or not to include children folders in the sink export. If true, logs
associated with child projects are also exported; otherwise only logs relating to the provided folder are included.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the logging sink.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>writer_<wbr>identity</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The identity associated with this sink. This identity must be granted write access to the
configured `destination`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Folder<wbr>Sink<wbr>Bigquery<wbr>Options</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#FolderSinkBigqueryOptions">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#FolderSinkBigqueryOptions">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/logging?tab=doc#FolderSinkBigqueryOptionsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/go/gcp/logging?tab=doc#FolderSinkBigqueryOptionsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Use<wbr>Partitioned<wbr>Tables</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to use [BigQuery's partition tables](https://cloud.google.com/bigquery/docs/partitioned-tables).
By default, Logging creates dated tables based on the log entries' timestamps, e.g. syslog_20170523. With partitioned
tables the date suffix is no longer present and [special query syntax](https://cloud.google.com/bigquery/docs/querying-partitioned-tables)
has to be used instead. In both cases, tables are sharded based on UTC timezone.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Use<wbr>Partitioned<wbr>Tables</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to use [BigQuery's partition tables](https://cloud.google.com/bigquery/docs/partitioned-tables).
By default, Logging creates dated tables based on the log entries' timestamps, e.g. syslog_20170523. With partitioned
tables the date suffix is no longer present and [special query syntax](https://cloud.google.com/bigquery/docs/querying-partitioned-tables)
has to be used instead. In both cases, tables are sharded based on UTC timezone.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>use<wbr>Partitioned<wbr>Tables</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean</span>
    </dt>
    <dd>{{% md %}}Whether to use [BigQuery's partition tables](https://cloud.google.com/bigquery/docs/partitioned-tables).
By default, Logging creates dated tables based on the log entries' timestamps, e.g. syslog_20170523. With partitioned
tables the date suffix is no longer present and [special query syntax](https://cloud.google.com/bigquery/docs/querying-partitioned-tables)
has to be used instead. In both cases, tables are sharded based on UTC timezone.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>use<wbr>Partitioned<wbr>Tables</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Whether to use [BigQuery's partition tables](https://cloud.google.com/bigquery/docs/partitioned-tables).
By default, Logging creates dated tables based on the log entries' timestamps, e.g. syslog_20170523. With partitioned
tables the date suffix is no longer present and [special query syntax](https://cloud.google.com/bigquery/docs/querying-partitioned-tables)
has to be used instead. In both cases, tables are sharded based on UTC timezone.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-gcp">https://github.com/pulumi/pulumi-gcp</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd></dl>
