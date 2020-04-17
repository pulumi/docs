
---
title: "Table"
block_external_search_index: true
---



Creates a table resource in a dataset for Google BigQuery. For more information see
[the official documentation](https://cloud.google.com/bigquery/docs/) and
[API](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables).


{{% examples %}}
{{% /examples %}}



## Create a Table Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/bigquery/#Table">Table</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/bigquery/#TableArgs">TableArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Table</span><span class="p">(resource_name, opts=None, </span>clusterings=None<span class="p">, </span>dataset_id=None<span class="p">, </span>description=None<span class="p">, </span>encryption_configuration=None<span class="p">, </span>expiration_time=None<span class="p">, </span>external_data_configuration=None<span class="p">, </span>friendly_name=None<span class="p">, </span>labels=None<span class="p">, </span>project=None<span class="p">, </span>range_partitioning=None<span class="p">, </span>schema=None<span class="p">, </span>table_id=None<span class="p">, </span>time_partitioning=None<span class="p">, </span>view=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewTable<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/bigquery?tab=doc#TableArgs">TableArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/bigquery?tab=doc#Table">Table</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.BigQuery.Table.html">Table</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.BigQuery.TableArgs.html">TableArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Dataset<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The dataset ID to create the table in.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Table<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A unique ID for the resource.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Clusterings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}Specifies column names to use for data clustering.
Up to four top-level columns are allowed, and should be specified in
descending priority order.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The field description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Encryption<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tableencryptionconfiguration">Table<wbr>Encryption<wbr>Configuration<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Specifies how the table should be encrypted.
If left blank, the table will be encrypted with a Google-managed key; that process
is transparent to the user.  Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expiration<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The time when this table expires, in
milliseconds since the epoch. If not present, the table will persist
indefinitely. Expired tables will be deleted and their storage
reclaimed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>External<wbr>Data<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tableexternaldataconfiguration">Table<wbr>External<wbr>Data<wbr>Configuration<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Describes the data format,
location, and other properties of a table stored outside of BigQuery.
By defining these properties, the data source can then be queried as
if it were a standard BigQuery table. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Friendly<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A descriptive name for the table.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}A mapping of labels to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Range<wbr>Partitioning</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tablerangepartitioning">Table<wbr>Range<wbr>Partitioning<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}If specified, configures range-based
partitioning for this table. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Schema</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A JSON schema for the table. Schema is required
for CSV and JSON formats and is disallowed for Google Cloud
Bigtable, Cloud Datastore backups, and Avro formats when using
external tables. For more information see the
[BigQuery API documentation](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#resource).
~>**NOTE**: Because this field expects a JSON string, any changes to the
string will create a diff, even if the JSON itself hasn't changed.
If the API returns a different value for the same schema, e.g. it
switched the order of values or replaced `STRUCT` field type with `RECORD`
field type, we currently cannot suppress the recurring diff this causes.
As a workaround, we recommend using the schema as returned by the API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time<wbr>Partitioning</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tabletimepartitioning">Table<wbr>Time<wbr>Partitioning<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}If specified, configures time-based
partitioning for this table. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>View</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tableview">Table<wbr>View<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}If specified, configures this table as a view.
Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Dataset<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The dataset ID to create the table in.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Table<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A unique ID for the resource.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Clusterings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}Specifies column names to use for data clustering.
Up to four top-level columns are allowed, and should be specified in
descending priority order.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The field description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Encryption<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tableencryptionconfiguration">Table<wbr>Encryption<wbr>Configuration</a></span>
    </dt>
    <dd>{{% md %}}Specifies how the table should be encrypted.
If left blank, the table will be encrypted with a Google-managed key; that process
is transparent to the user.  Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expiration<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The time when this table expires, in
milliseconds since the epoch. If not present, the table will persist
indefinitely. Expired tables will be deleted and their storage
reclaimed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>External<wbr>Data<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tableexternaldataconfiguration">Table<wbr>External<wbr>Data<wbr>Configuration</a></span>
    </dt>
    <dd>{{% md %}}Describes the data format,
location, and other properties of a table stored outside of BigQuery.
By defining these properties, the data source can then be queried as
if it were a standard BigQuery table. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Friendly<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A descriptive name for the table.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A mapping of labels to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Range<wbr>Partitioning</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tablerangepartitioning">Table<wbr>Range<wbr>Partitioning</a></span>
    </dt>
    <dd>{{% md %}}If specified, configures range-based
partitioning for this table. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Schema</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A JSON schema for the table. Schema is required
for CSV and JSON formats and is disallowed for Google Cloud
Bigtable, Cloud Datastore backups, and Avro formats when using
external tables. For more information see the
[BigQuery API documentation](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#resource).
~>**NOTE**: Because this field expects a JSON string, any changes to the
string will create a diff, even if the JSON itself hasn't changed.
If the API returns a different value for the same schema, e.g. it
switched the order of values or replaced `STRUCT` field type with `RECORD`
field type, we currently cannot suppress the recurring diff this causes.
As a workaround, we recommend using the schema as returned by the API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time<wbr>Partitioning</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tabletimepartitioning">Table<wbr>Time<wbr>Partitioning</a></span>
    </dt>
    <dd>{{% md %}}If specified, configures time-based
partitioning for this table. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>View</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tableview">Table<wbr>View</a></span>
    </dt>
    <dd>{{% md %}}If specified, configures this table as a view.
Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>dataset<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The dataset ID to create the table in.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>table<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A unique ID for the resource.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>clusterings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}Specifies column names to use for data clustering.
Up to four top-level columns are allowed, and should be specified in
descending priority order.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The field description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>encryption<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tableencryptionconfiguration">Table<wbr>Encryption<wbr>Configuration</a></span>
    </dt>
    <dd>{{% md %}}Specifies how the table should be encrypted.
If left blank, the table will be encrypted with a Google-managed key; that process
is transparent to the user.  Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expiration<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The time when this table expires, in
milliseconds since the epoch. If not present, the table will persist
indefinitely. Expired tables will be deleted and their storage
reclaimed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>external<wbr>Data<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tableexternaldataconfiguration">Table<wbr>External<wbr>Data<wbr>Configuration</a></span>
    </dt>
    <dd>{{% md %}}Describes the data format,
location, and other properties of a table stored outside of BigQuery.
By defining these properties, the data source can then be queried as
if it were a standard BigQuery table. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>friendly<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A descriptive name for the table.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}A mapping of labels to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>range<wbr>Partitioning</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tablerangepartitioning">Table<wbr>Range<wbr>Partitioning</a></span>
    </dt>
    <dd>{{% md %}}If specified, configures range-based
partitioning for this table. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>schema</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A JSON schema for the table. Schema is required
for CSV and JSON formats and is disallowed for Google Cloud
Bigtable, Cloud Datastore backups, and Avro formats when using
external tables. For more information see the
[BigQuery API documentation](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#resource).
~>**NOTE**: Because this field expects a JSON string, any changes to the
string will create a diff, even if the JSON itself hasn't changed.
If the API returns a different value for the same schema, e.g. it
switched the order of values or replaced `STRUCT` field type with `RECORD`
field type, we currently cannot suppress the recurring diff this causes.
As a workaround, we recommend using the schema as returned by the API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>time<wbr>Partitioning</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tabletimepartitioning">Table<wbr>Time<wbr>Partitioning</a></span>
    </dt>
    <dd>{{% md %}}If specified, configures time-based
partitioning for this table. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>view</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tableview">Table<wbr>View</a></span>
    </dt>
    <dd>{{% md %}}If specified, configures this table as a view.
Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>dataset_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The dataset ID to create the table in.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>table_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A unique ID for the resource.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>clusterings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}Specifies column names to use for data clustering.
Up to four top-level columns are allowed, and should be specified in
descending priority order.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The field description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>encryption_<wbr>configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tableencryptionconfiguration">Dict[Table<wbr>Encryption<wbr>Configuration]</a></span>
    </dt>
    <dd>{{% md %}}Specifies how the table should be encrypted.
If left blank, the table will be encrypted with a Google-managed key; that process
is transparent to the user.  Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expiration_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The time when this table expires, in
milliseconds since the epoch. If not present, the table will persist
indefinitely. Expired tables will be deleted and their storage
reclaimed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>external_<wbr>data_<wbr>configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tableexternaldataconfiguration">Dict[Table<wbr>External<wbr>Data<wbr>Configuration]</a></span>
    </dt>
    <dd>{{% md %}}Describes the data format,
location, and other properties of a table stored outside of BigQuery.
By defining these properties, the data source can then be queried as
if it were a standard BigQuery table. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>friendly_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A descriptive name for the table.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of labels to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>range_<wbr>partitioning</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tablerangepartitioning">Dict[Table<wbr>Range<wbr>Partitioning]</a></span>
    </dt>
    <dd>{{% md %}}If specified, configures range-based
partitioning for this table. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>schema</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A JSON schema for the table. Schema is required
for CSV and JSON formats and is disallowed for Google Cloud
Bigtable, Cloud Datastore backups, and Avro formats when using
external tables. For more information see the
[BigQuery API documentation](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#resource).
~>**NOTE**: Because this field expects a JSON string, any changes to the
string will create a diff, even if the JSON itself hasn't changed.
If the API returns a different value for the same schema, e.g. it
switched the order of values or replaced `STRUCT` field type with `RECORD`
field type, we currently cannot suppress the recurring diff this causes.
As a workaround, we recommend using the schema as returned by the API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>time_<wbr>partitioning</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tabletimepartitioning">Dict[Table<wbr>Time<wbr>Partitioning]</a></span>
    </dt>
    <dd>{{% md %}}If specified, configures time-based
partitioning for this table. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>view</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tableview">Dict[Table<wbr>View]</a></span>
    </dt>
    <dd>{{% md %}}If specified, configures this table as a view.
Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Table Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Creation<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The time when this table was created, in milliseconds since the epoch.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Etag</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A hash of the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Last<wbr>Modified<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The time when this table was last modified, in milliseconds since the epoch.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The geographic location where the table resides. This value is inherited from the dataset.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Num<wbr>Bytes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The size of this table in bytes, excluding any data in the streaming buffer.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Num<wbr>Long<wbr>Term<wbr>Bytes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The number of bytes in the table that are considered "long-term storage".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Num<wbr>Rows</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The number of rows of data in this table, excluding any data in the streaming buffer.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The only type supported is DAY, which will generate
one partition per day based on data loading time.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Creation<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The time when this table was created, in milliseconds since the epoch.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Etag</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A hash of the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Last<wbr>Modified<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The time when this table was last modified, in milliseconds since the epoch.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The geographic location where the table resides. This value is inherited from the dataset.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Num<wbr>Bytes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The size of this table in bytes, excluding any data in the streaming buffer.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Num<wbr>Long<wbr>Term<wbr>Bytes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The number of bytes in the table that are considered "long-term storage".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Num<wbr>Rows</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The number of rows of data in this table, excluding any data in the streaming buffer.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The only type supported is DAY, which will generate
one partition per day based on data loading time.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>creation<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The time when this table was created, in milliseconds since the epoch.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>etag</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A hash of the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>last<wbr>Modified<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The time when this table was last modified, in milliseconds since the epoch.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The geographic location where the table resides. This value is inherited from the dataset.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>num<wbr>Bytes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The size of this table in bytes, excluding any data in the streaming buffer.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>num<wbr>Long<wbr>Term<wbr>Bytes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The number of bytes in the table that are considered "long-term storage".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>num<wbr>Rows</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The number of rows of data in this table, excluding any data in the streaming buffer.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The only type supported is DAY, which will generate
one partition per day based on data loading time.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>creation_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The time when this table was created, in milliseconds since the epoch.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>etag</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A hash of the resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>last_<wbr>modified_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The time when this table was last modified, in milliseconds since the epoch.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The geographic location where the table resides. This value is inherited from the dataset.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>num_<wbr>bytes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The size of this table in bytes, excluding any data in the streaming buffer.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>num_<wbr>long_<wbr>term_<wbr>bytes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The number of bytes in the table that are considered "long-term storage".
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>num_<wbr>rows</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The number of rows of data in this table, excluding any data in the streaming buffer.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>self_<wbr>link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The only type supported is DAY, which will generate
one partition per day based on data loading time.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Table Resource

Get an existing Table resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/bigquery/#TableState">TableState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/bigquery/#Table">Table</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>clusterings=None<span class="p">, </span>creation_time=None<span class="p">, </span>dataset_id=None<span class="p">, </span>description=None<span class="p">, </span>encryption_configuration=None<span class="p">, </span>etag=None<span class="p">, </span>expiration_time=None<span class="p">, </span>external_data_configuration=None<span class="p">, </span>friendly_name=None<span class="p">, </span>labels=None<span class="p">, </span>last_modified_time=None<span class="p">, </span>location=None<span class="p">, </span>num_bytes=None<span class="p">, </span>num_long_term_bytes=None<span class="p">, </span>num_rows=None<span class="p">, </span>project=None<span class="p">, </span>range_partitioning=None<span class="p">, </span>schema=None<span class="p">, </span>self_link=None<span class="p">, </span>table_id=None<span class="p">, </span>time_partitioning=None<span class="p">, </span>type=None<span class="p">, </span>view=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetTable<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/bigquery?tab=doc#TableState">TableState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/bigquery?tab=doc#Table">Table</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.BigQuery.Table.html">Table</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.BigQuery.TableState.html">TableState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Clusterings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}Specifies column names to use for data clustering.
Up to four top-level columns are allowed, and should be specified in
descending priority order.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Creation<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The time when this table was created, in milliseconds since the epoch.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dataset<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The dataset ID to create the table in.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The field description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Encryption<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tableencryptionconfiguration">Table<wbr>Encryption<wbr>Configuration<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Specifies how the table should be encrypted.
If left blank, the table will be encrypted with a Google-managed key; that process
is transparent to the user.  Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Etag</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A hash of the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expiration<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The time when this table expires, in
milliseconds since the epoch. If not present, the table will persist
indefinitely. Expired tables will be deleted and their storage
reclaimed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>External<wbr>Data<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tableexternaldataconfiguration">Table<wbr>External<wbr>Data<wbr>Configuration<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Describes the data format,
location, and other properties of a table stored outside of BigQuery.
By defining these properties, the data source can then be queried as
if it were a standard BigQuery table. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Friendly<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A descriptive name for the table.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}A mapping of labels to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Last<wbr>Modified<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The time when this table was last modified, in milliseconds since the epoch.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The geographic location where the table resides. This value is inherited from the dataset.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Num<wbr>Bytes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The size of this table in bytes, excluding any data in the streaming buffer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Num<wbr>Long<wbr>Term<wbr>Bytes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The number of bytes in the table that are considered "long-term storage".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Num<wbr>Rows</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The number of rows of data in this table, excluding any data in the streaming buffer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Range<wbr>Partitioning</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tablerangepartitioning">Table<wbr>Range<wbr>Partitioning<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}If specified, configures range-based
partitioning for this table. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Schema</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A JSON schema for the table. Schema is required
for CSV and JSON formats and is disallowed for Google Cloud
Bigtable, Cloud Datastore backups, and Avro formats when using
external tables. For more information see the
[BigQuery API documentation](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#resource).
~>**NOTE**: Because this field expects a JSON string, any changes to the
string will create a diff, even if the JSON itself hasn't changed.
If the API returns a different value for the same schema, e.g. it
switched the order of values or replaced `STRUCT` field type with `RECORD`
field type, we currently cannot suppress the recurring diff this causes.
As a workaround, we recommend using the schema as returned by the API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Table<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A unique ID for the resource.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time<wbr>Partitioning</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tabletimepartitioning">Table<wbr>Time<wbr>Partitioning<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}If specified, configures time-based
partitioning for this table. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The only type supported is DAY, which will generate
one partition per day based on data loading time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>View</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tableview">Table<wbr>View<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}If specified, configures this table as a view.
Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Clusterings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}Specifies column names to use for data clustering.
Up to four top-level columns are allowed, and should be specified in
descending priority order.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Creation<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The time when this table was created, in milliseconds since the epoch.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dataset<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The dataset ID to create the table in.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The field description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Encryption<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tableencryptionconfiguration">Table<wbr>Encryption<wbr>Configuration</a></span>
    </dt>
    <dd>{{% md %}}Specifies how the table should be encrypted.
If left blank, the table will be encrypted with a Google-managed key; that process
is transparent to the user.  Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Etag</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A hash of the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expiration<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The time when this table expires, in
milliseconds since the epoch. If not present, the table will persist
indefinitely. Expired tables will be deleted and their storage
reclaimed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>External<wbr>Data<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tableexternaldataconfiguration">Table<wbr>External<wbr>Data<wbr>Configuration</a></span>
    </dt>
    <dd>{{% md %}}Describes the data format,
location, and other properties of a table stored outside of BigQuery.
By defining these properties, the data source can then be queried as
if it were a standard BigQuery table. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Friendly<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A descriptive name for the table.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}A mapping of labels to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Last<wbr>Modified<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The time when this table was last modified, in milliseconds since the epoch.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The geographic location where the table resides. This value is inherited from the dataset.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Num<wbr>Bytes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The size of this table in bytes, excluding any data in the streaming buffer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Num<wbr>Long<wbr>Term<wbr>Bytes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The number of bytes in the table that are considered "long-term storage".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Num<wbr>Rows</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The number of rows of data in this table, excluding any data in the streaming buffer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Range<wbr>Partitioning</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tablerangepartitioning">Table<wbr>Range<wbr>Partitioning</a></span>
    </dt>
    <dd>{{% md %}}If specified, configures range-based
partitioning for this table. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Schema</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A JSON schema for the table. Schema is required
for CSV and JSON formats and is disallowed for Google Cloud
Bigtable, Cloud Datastore backups, and Avro formats when using
external tables. For more information see the
[BigQuery API documentation](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#resource).
~>**NOTE**: Because this field expects a JSON string, any changes to the
string will create a diff, even if the JSON itself hasn't changed.
If the API returns a different value for the same schema, e.g. it
switched the order of values or replaced `STRUCT` field type with `RECORD`
field type, we currently cannot suppress the recurring diff this causes.
As a workaround, we recommend using the schema as returned by the API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Table<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A unique ID for the resource.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Time<wbr>Partitioning</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tabletimepartitioning">Table<wbr>Time<wbr>Partitioning</a></span>
    </dt>
    <dd>{{% md %}}If specified, configures time-based
partitioning for this table. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The only type supported is DAY, which will generate
one partition per day based on data loading time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>View</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tableview">Table<wbr>View</a></span>
    </dt>
    <dd>{{% md %}}If specified, configures this table as a view.
Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>clusterings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}Specifies column names to use for data clustering.
Up to four top-level columns are allowed, and should be specified in
descending priority order.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>creation<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The time when this table was created, in milliseconds since the epoch.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dataset<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The dataset ID to create the table in.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The field description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>encryption<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tableencryptionconfiguration">Table<wbr>Encryption<wbr>Configuration</a></span>
    </dt>
    <dd>{{% md %}}Specifies how the table should be encrypted.
If left blank, the table will be encrypted with a Google-managed key; that process
is transparent to the user.  Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>etag</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A hash of the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expiration<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The time when this table expires, in
milliseconds since the epoch. If not present, the table will persist
indefinitely. Expired tables will be deleted and their storage
reclaimed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>external<wbr>Data<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tableexternaldataconfiguration">Table<wbr>External<wbr>Data<wbr>Configuration</a></span>
    </dt>
    <dd>{{% md %}}Describes the data format,
location, and other properties of a table stored outside of BigQuery.
By defining these properties, the data source can then be queried as
if it were a standard BigQuery table. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>friendly<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A descriptive name for the table.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}A mapping of labels to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>last<wbr>Modified<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The time when this table was last modified, in milliseconds since the epoch.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The geographic location where the table resides. This value is inherited from the dataset.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>num<wbr>Bytes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The size of this table in bytes, excluding any data in the streaming buffer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>num<wbr>Long<wbr>Term<wbr>Bytes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The number of bytes in the table that are considered "long-term storage".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>num<wbr>Rows</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The number of rows of data in this table, excluding any data in the streaming buffer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>range<wbr>Partitioning</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tablerangepartitioning">Table<wbr>Range<wbr>Partitioning</a></span>
    </dt>
    <dd>{{% md %}}If specified, configures range-based
partitioning for this table. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>schema</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A JSON schema for the table. Schema is required
for CSV and JSON formats and is disallowed for Google Cloud
Bigtable, Cloud Datastore backups, and Avro formats when using
external tables. For more information see the
[BigQuery API documentation](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#resource).
~>**NOTE**: Because this field expects a JSON string, any changes to the
string will create a diff, even if the JSON itself hasn't changed.
If the API returns a different value for the same schema, e.g. it
switched the order of values or replaced `STRUCT` field type with `RECORD`
field type, we currently cannot suppress the recurring diff this causes.
As a workaround, we recommend using the schema as returned by the API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>table<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A unique ID for the resource.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>time<wbr>Partitioning</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tabletimepartitioning">Table<wbr>Time<wbr>Partitioning</a></span>
    </dt>
    <dd>{{% md %}}If specified, configures time-based
partitioning for this table. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The only type supported is DAY, which will generate
one partition per day based on data loading time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>view</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tableview">Table<wbr>View</a></span>
    </dt>
    <dd>{{% md %}}If specified, configures this table as a view.
Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>clusterings</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}Specifies column names to use for data clustering.
Up to four top-level columns are allowed, and should be specified in
descending priority order.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>creation_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The time when this table was created, in milliseconds since the epoch.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dataset_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The dataset ID to create the table in.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The field description.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>encryption_<wbr>configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tableencryptionconfiguration">Dict[Table<wbr>Encryption<wbr>Configuration]</a></span>
    </dt>
    <dd>{{% md %}}Specifies how the table should be encrypted.
If left blank, the table will be encrypted with a Google-managed key; that process
is transparent to the user.  Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>etag</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A hash of the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expiration_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The time when this table expires, in
milliseconds since the epoch. If not present, the table will persist
indefinitely. Expired tables will be deleted and their storage
reclaimed.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>external_<wbr>data_<wbr>configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tableexternaldataconfiguration">Dict[Table<wbr>External<wbr>Data<wbr>Configuration]</a></span>
    </dt>
    <dd>{{% md %}}Describes the data format,
location, and other properties of a table stored outside of BigQuery.
By defining these properties, the data source can then be queried as
if it were a standard BigQuery table. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>friendly_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A descriptive name for the table.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}A mapping of labels to assign to the resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>last_<wbr>modified_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The time when this table was last modified, in milliseconds since the epoch.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The geographic location where the table resides. This value is inherited from the dataset.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>num_<wbr>bytes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The size of this table in bytes, excluding any data in the streaming buffer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>num_<wbr>long_<wbr>term_<wbr>bytes</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The number of bytes in the table that are considered "long-term storage".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>num_<wbr>rows</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The number of rows of data in this table, excluding any data in the streaming buffer.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>project</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>range_<wbr>partitioning</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tablerangepartitioning">Dict[Table<wbr>Range<wbr>Partitioning]</a></span>
    </dt>
    <dd>{{% md %}}If specified, configures range-based
partitioning for this table. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>schema</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A JSON schema for the table. Schema is required
for CSV and JSON formats and is disallowed for Google Cloud
Bigtable, Cloud Datastore backups, and Avro formats when using
external tables. For more information see the
[BigQuery API documentation](https://cloud.google.com/bigquery/docs/reference/rest/v2/tables#resource).
~>**NOTE**: Because this field expects a JSON string, any changes to the
string will create a diff, even if the JSON itself hasn't changed.
If the API returns a different value for the same schema, e.g. it
switched the order of values or replaced `STRUCT` field type with `RECORD`
field type, we currently cannot suppress the recurring diff this causes.
As a workaround, we recommend using the schema as returned by the API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>self_<wbr>link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>table_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A unique ID for the resource.
Changing this forces a new resource to be created.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>time_<wbr>partitioning</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tabletimepartitioning">Dict[Table<wbr>Time<wbr>Partitioning]</a></span>
    </dt>
    <dd>{{% md %}}If specified, configures time-based
partitioning for this table. Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The only type supported is DAY, which will generate
one partition per day based on data loading time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>view</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tableview">Dict[Table<wbr>View]</a></span>
    </dt>
    <dd>{{% md %}}If specified, configures this table as a view.
Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Table<wbr>Encryption<wbr>Configuration</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#TableEncryptionConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#TableEncryptionConfiguration">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/bigquery?tab=doc#TableEncryptionConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/bigquery?tab=doc#TableEncryptionConfigurationOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Kms<wbr>Key<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The self link or full name of a key which should be used to
encrypt this table.  Note that the default bigquery service account will need to have
encrypt/decrypt permissions on this key - you may want to see the
`gcp.bigquery.getDefaultServiceAccount` datasource and the
`gcp.kms.CryptoKeyIAMBinding` resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Kms<wbr>Key<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The self link or full name of a key which should be used to
encrypt this table.  Note that the default bigquery service account will need to have
encrypt/decrypt permissions on this key - you may want to see the
`gcp.bigquery.getDefaultServiceAccount` datasource and the
`gcp.kms.CryptoKeyIAMBinding` resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>kms<wbr>Key<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The self link or full name of a key which should be used to
encrypt this table.  Note that the default bigquery service account will need to have
encrypt/decrypt permissions on this key - you may want to see the
`gcp.bigquery.getDefaultServiceAccount` datasource and the
`gcp.kms.CryptoKeyIAMBinding` resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>kms_<wbr>key_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The self link or full name of a key which should be used to
encrypt this table.  Note that the default bigquery service account will need to have
encrypt/decrypt permissions on this key - you may want to see the
`gcp.bigquery.getDefaultServiceAccount` datasource and the
`gcp.kms.CryptoKeyIAMBinding` resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Table<wbr>External<wbr>Data<wbr>Configuration</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#TableExternalDataConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#TableExternalDataConfiguration">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/bigquery?tab=doc#TableExternalDataConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/bigquery?tab=doc#TableExternalDataConfigurationOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Autodetect</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}- Let BigQuery try to autodetect the schema
and format of the table.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Source<wbr>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The data format. Supported values are:
"CSV", "GOOGLE_SHEETS", "NEWLINE_DELIMITED_JSON", "AVRO", "PARQUET",
and "DATSTORE_BACKUP". To use "GOOGLE_SHEETS"
the `scopes` must include
"https://www.googleapis.com/auth/drive.readonly".
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Source<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">List&lt;string&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of the fully-qualified URIs that point to
your data in Google Cloud.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Compression</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The compression type of the data source.
Valid values are "NONE" or "GZIP".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Csv<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tableexternaldataconfigurationcsvoptions">Table<wbr>External<wbr>Data<wbr>Configuration<wbr>Csv<wbr>Options<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Additional properties to set if
`source_format` is set to "CSV". Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Google<wbr>Sheets<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tableexternaldataconfigurationgooglesheetsoptions">Table<wbr>External<wbr>Data<wbr>Configuration<wbr>Google<wbr>Sheets<wbr>Options<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Additional options if
`source_format` is set to "GOOGLE_SHEETS". Structure is
documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ignore<wbr>Unknown<wbr>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicates if BigQuery should
allow extra values that are not represented in the table schema.
If true, the extra values are ignored. If false, records with
extra columns are treated as bad records, and if there are too
many bad records, an invalid error is returned in the job result.
The default value is false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Bad<wbr>Records</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The maximum number of bad records that
BigQuery can ignore when reading data.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Autodetect</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}- Let BigQuery try to autodetect the schema
and format of the table.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Source<wbr>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The data format. Supported values are:
"CSV", "GOOGLE_SHEETS", "NEWLINE_DELIMITED_JSON", "AVRO", "PARQUET",
and "DATSTORE_BACKUP". To use "GOOGLE_SHEETS"
the `scopes` must include
"https://www.googleapis.com/auth/drive.readonly".
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Source<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">[]string</a></span>
    </dt>
    <dd>{{% md %}}A list of the fully-qualified URIs that point to
your data in Google Cloud.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Compression</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The compression type of the data source.
Valid values are "NONE" or "GZIP".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Csv<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tableexternaldataconfigurationcsvoptions">Table<wbr>External<wbr>Data<wbr>Configuration<wbr>Csv<wbr>Options</a></span>
    </dt>
    <dd>{{% md %}}Additional properties to set if
`source_format` is set to "CSV". Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Google<wbr>Sheets<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tableexternaldataconfigurationgooglesheetsoptions">Table<wbr>External<wbr>Data<wbr>Configuration<wbr>Google<wbr>Sheets<wbr>Options</a></span>
    </dt>
    <dd>{{% md %}}Additional options if
`source_format` is set to "GOOGLE_SHEETS". Structure is
documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ignore<wbr>Unknown<wbr>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicates if BigQuery should
allow extra values that are not represented in the table schema.
If true, the extra values are ignored. If false, records with
extra columns are treated as bad records, and if there are too
many bad records, an invalid error is returned in the job result.
The default value is false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Max<wbr>Bad<wbr>Records</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The maximum number of bad records that
BigQuery can ignore when reading data.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>autodetect</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}- Let BigQuery try to autodetect the schema
and format of the table.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>source<wbr>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The data format. Supported values are:
"CSV", "GOOGLE_SHEETS", "NEWLINE_DELIMITED_JSON", "AVRO", "PARQUET",
and "DATSTORE_BACKUP". To use "GOOGLE_SHEETS"
the `scopes` must include
"https://www.googleapis.com/auth/drive.readonly".
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>source<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string[]</a></span>
    </dt>
    <dd>{{% md %}}A list of the fully-qualified URIs that point to
your data in Google Cloud.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>compression</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The compression type of the data source.
Valid values are "NONE" or "GZIP".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>csv<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tableexternaldataconfigurationcsvoptions">Table<wbr>External<wbr>Data<wbr>Configuration<wbr>Csv<wbr>Options</a></span>
    </dt>
    <dd>{{% md %}}Additional properties to set if
`source_format` is set to "CSV". Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>google<wbr>Sheets<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tableexternaldataconfigurationgooglesheetsoptions">Table<wbr>External<wbr>Data<wbr>Configuration<wbr>Google<wbr>Sheets<wbr>Options</a></span>
    </dt>
    <dd>{{% md %}}Additional options if
`source_format` is set to "GOOGLE_SHEETS". Structure is
documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ignore<wbr>Unknown<wbr>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Indicates if BigQuery should
allow extra values that are not represented in the table schema.
If true, the extra values are ignored. If false, records with
extra columns are treated as bad records, and if there are too
many bad records, an invalid error is returned in the job result.
The default value is false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Bad<wbr>Records</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The maximum number of bad records that
BigQuery can ignore when reading data.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>autodetect</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}- Let BigQuery try to autodetect the schema
and format of the table.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>source<wbr>Format</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The data format. Supported values are:
"CSV", "GOOGLE_SHEETS", "NEWLINE_DELIMITED_JSON", "AVRO", "PARQUET",
and "DATSTORE_BACKUP". To use "GOOGLE_SHEETS"
the `scopes` must include
"https://www.googleapis.com/auth/drive.readonly".
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>source<wbr>Uris</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">List[str]</a></span>
    </dt>
    <dd>{{% md %}}A list of the fully-qualified URIs that point to
your data in Google Cloud.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>compression</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The compression type of the data source.
Valid values are "NONE" or "GZIP".
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>csv<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tableexternaldataconfigurationcsvoptions">Dict[Table<wbr>External<wbr>Data<wbr>Configuration<wbr>Csv<wbr>Options]</a></span>
    </dt>
    <dd>{{% md %}}Additional properties to set if
`source_format` is set to "CSV". Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>google<wbr>Sheets<wbr>Options</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tableexternaldataconfigurationgooglesheetsoptions">Dict[Table<wbr>External<wbr>Data<wbr>Configuration<wbr>Google<wbr>Sheets<wbr>Options]</a></span>
    </dt>
    <dd>{{% md %}}Additional options if
`source_format` is set to "GOOGLE_SHEETS". Structure is
documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ignore<wbr>Unknown<wbr>Values</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicates if BigQuery should
allow extra values that are not represented in the table schema.
If true, the extra values are ignored. If false, records with
extra columns are treated as bad records, and if there are too
many bad records, an invalid error is returned in the job result.
The default value is false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>max<wbr>Bad<wbr>Records</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The maximum number of bad records that
BigQuery can ignore when reading data.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Table<wbr>External<wbr>Data<wbr>Configuration<wbr>Csv<wbr>Options</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#TableExternalDataConfigurationCsvOptions">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#TableExternalDataConfigurationCsvOptions">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/bigquery?tab=doc#TableExternalDataConfigurationCsvOptionsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/bigquery?tab=doc#TableExternalDataConfigurationCsvOptionsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Quote</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The value that is used to quote data sections in a
CSV file. If your data does not contain quoted sections, set the
property value to an empty string. If your data contains quoted newline
characters, you must also set the `allow_quoted_newlines` property to true.
The API-side default is `"`, specified in the provider escaped as `\"`. Due to
limitations with default values, this value is required to be
explicitly set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Jagged<wbr>Rows</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicates if BigQuery should accept rows
that are missing trailing optional columns.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Quoted<wbr>Newlines</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicates if BigQuery should allow
quoted data sections that contain newline characters in a CSV file.
The default value is false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The character encoding of the data. The supported
values are UTF-8 or ISO-8859-1.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Field<wbr>Delimiter</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The separator for fields in a CSV file.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Skip<wbr>Leading<wbr>Rows</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The number of rows at the top of the sheet
that BigQuery will skip when reading the data. At least one of `range` or
`skip_leading_rows` must be set.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Quote</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The value that is used to quote data sections in a
CSV file. If your data does not contain quoted sections, set the
property value to an empty string. If your data contains quoted newline
characters, you must also set the `allow_quoted_newlines` property to true.
The API-side default is `"`, specified in the provider escaped as `\"`. Due to
limitations with default values, this value is required to be
explicitly set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Jagged<wbr>Rows</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicates if BigQuery should accept rows
that are missing trailing optional columns.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Allow<wbr>Quoted<wbr>Newlines</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicates if BigQuery should allow
quoted data sections that contain newline characters in a CSV file.
The default value is false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The character encoding of the data. The supported
values are UTF-8 or ISO-8859-1.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Field<wbr>Delimiter</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The separator for fields in a CSV file.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Skip<wbr>Leading<wbr>Rows</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The number of rows at the top of the sheet
that BigQuery will skip when reading the data. At least one of `range` or
`skip_leading_rows` must be set.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>quote</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The value that is used to quote data sections in a
CSV file. If your data does not contain quoted sections, set the
property value to an empty string. If your data contains quoted newline
characters, you must also set the `allow_quoted_newlines` property to true.
The API-side default is `"`, specified in the provider escaped as `\"`. Due to
limitations with default values, this value is required to be
explicitly set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Jagged<wbr>Rows</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Indicates if BigQuery should accept rows
that are missing trailing optional columns.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Quoted<wbr>Newlines</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Indicates if BigQuery should allow
quoted data sections that contain newline characters in a CSV file.
The default value is false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The character encoding of the data. The supported
values are UTF-8 or ISO-8859-1.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>field<wbr>Delimiter</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The separator for fields in a CSV file.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>skip<wbr>Leading<wbr>Rows</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The number of rows at the top of the sheet
that BigQuery will skip when reading the data. At least one of `range` or
`skip_leading_rows` must be set.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>quote</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The value that is used to quote data sections in a
CSV file. If your data does not contain quoted sections, set the
property value to an empty string. If your data contains quoted newline
characters, you must also set the `allow_quoted_newlines` property to true.
The API-side default is `"`, specified in the provider escaped as `\"`. Due to
limitations with default values, this value is required to be
explicitly set.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Jagged<wbr>Rows</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicates if BigQuery should accept rows
that are missing trailing optional columns.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>allow<wbr>Quoted<wbr>Newlines</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Indicates if BigQuery should allow
quoted data sections that contain newline characters in a CSV file.
The default value is false.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>encoding</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The character encoding of the data. The supported
values are UTF-8 or ISO-8859-1.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>field<wbr>Delimiter</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The separator for fields in a CSV file.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>skip<wbr>Leading<wbr>Rows</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The number of rows at the top of the sheet
that BigQuery will skip when reading the data. At least one of `range` or
`skip_leading_rows` must be set.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Table<wbr>External<wbr>Data<wbr>Configuration<wbr>Google<wbr>Sheets<wbr>Options</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#TableExternalDataConfigurationGoogleSheetsOptions">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#TableExternalDataConfigurationGoogleSheetsOptions">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/bigquery?tab=doc#TableExternalDataConfigurationGoogleSheetsOptionsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/bigquery?tab=doc#TableExternalDataConfigurationGoogleSheetsOptionsOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}Information required to partition based on ranges.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Skip<wbr>Leading<wbr>Rows</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The number of rows at the top of the sheet
that BigQuery will skip when reading the data. At least one of `range` or
`skip_leading_rows` must be set.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}Information required to partition based on ranges.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Skip<wbr>Leading<wbr>Rows</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The number of rows at the top of the sheet
that BigQuery will skip when reading the data. At least one of `range` or
`skip_leading_rows` must be set.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>range</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}Information required to partition based on ranges.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>skip<wbr>Leading<wbr>Rows</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The number of rows at the top of the sheet
that BigQuery will skip when reading the data. At least one of `range` or
`skip_leading_rows` must be set.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>range</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}Information required to partition based on ranges.
Structure is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>skip<wbr>Leading<wbr>Rows</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The number of rows at the top of the sheet
that BigQuery will skip when reading the data. At least one of `range` or
`skip_leading_rows` must be set.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Table<wbr>Range<wbr>Partitioning</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#TableRangePartitioning">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#TableRangePartitioning">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/bigquery?tab=doc#TableRangePartitioningArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/bigquery?tab=doc#TableRangePartitioningOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The field used to determine how to create a range-based
partition.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tablerangepartitioningrange">Table<wbr>Range<wbr>Partitioning<wbr>Range<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}Information required to partition based on ranges.
Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The field used to determine how to create a range-based
partition.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Range</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tablerangepartitioningrange">Table<wbr>Range<wbr>Partitioning<wbr>Range</a></span>
    </dt>
    <dd>{{% md %}}Information required to partition based on ranges.
Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>field</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The field used to determine how to create a range-based
partition.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>range</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tablerangepartitioningrange">Table<wbr>Range<wbr>Partitioning<wbr>Range</a></span>
    </dt>
    <dd>{{% md %}}Information required to partition based on ranges.
Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>field</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The field used to determine how to create a range-based
partition.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>range</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#tablerangepartitioningrange">Dict[Table<wbr>Range<wbr>Partitioning<wbr>Range]</a></span>
    </dt>
    <dd>{{% md %}}Information required to partition based on ranges.
Structure is documented below.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Table<wbr>Range<wbr>Partitioning<wbr>Range</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#TableRangePartitioningRange">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#TableRangePartitioningRange">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/bigquery?tab=doc#TableRangePartitioningRangeArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/bigquery?tab=doc#TableRangePartitioningRangeOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>End</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}End of the range partitioning, exclusive.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The width of each range within the partition.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Start</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Start of the range partitioning, inclusive.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>End</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}End of the range partitioning, exclusive.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Interval</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The width of each range within the partition.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Start</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Start of the range partitioning, inclusive.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>end</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}End of the range partitioning, exclusive.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>interval</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The width of each range within the partition.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>start</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Start of the range partitioning, inclusive.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>end</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}End of the range partitioning, exclusive.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>interval</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The width of each range within the partition.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>start</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Start of the range partitioning, inclusive.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Table<wbr>Time<wbr>Partitioning</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#TableTimePartitioning">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#TableTimePartitioning">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/bigquery?tab=doc#TableTimePartitioningArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/bigquery?tab=doc#TableTimePartitioningOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The only type supported is DAY, which will generate
one partition per day based on data loading time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expiration<wbr>Ms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}Number of milliseconds for which to keep the
storage for a partition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The field used to determine how to create a range-based
partition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Require<wbr>Partition<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}If set to true, queries over this table
require a partition filter that can be used for partition elimination to be
specified.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The only type supported is DAY, which will generate
one partition per day based on data loading time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Expiration<wbr>Ms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}Number of milliseconds for which to keep the
storage for a partition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The field used to determine how to create a range-based
partition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Require<wbr>Partition<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}If set to true, queries over this table
require a partition filter that can be used for partition elimination to be
specified.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The only type supported is DAY, which will generate
one partition per day based on data loading time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expiration<wbr>Ms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}Number of milliseconds for which to keep the
storage for a partition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>field</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The field used to determine how to create a range-based
partition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>require<wbr>Partition<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}If set to true, queries over this table
require a partition filter that can be used for partition elimination to be
specified.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The only type supported is DAY, which will generate
one partition per day based on data loading time.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>expiration<wbr>Ms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}Number of milliseconds for which to keep the
storage for a partition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>field</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The field used to determine how to create a range-based
partition.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>require<wbr>Partition<wbr>Filter</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}If set to true, queries over this table
require a partition filter that can be used for partition elimination to be
specified.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Table<wbr>View</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#TableView">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#TableView">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/bigquery?tab=doc#TableViewArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/bigquery?tab=doc#TableViewOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Query</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A query that BigQuery executes when the view is referenced.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Use<wbr>Legacy<wbr>Sql</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}Specifies whether to use BigQuery's legacy SQL for this view.
The default value is true. If set to false, the view will use BigQuery's standard SQL.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Query</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A query that BigQuery executes when the view is referenced.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Use<wbr>Legacy<wbr>Sql</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}Specifies whether to use BigQuery's legacy SQL for this view.
The default value is true. If set to false, the view will use BigQuery's standard SQL.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>query</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A query that BigQuery executes when the view is referenced.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>use<wbr>Legacy<wbr>Sql</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}Specifies whether to use BigQuery's legacy SQL for this view.
The default value is true. If set to false, the view will use BigQuery's standard SQL.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>query</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A query that BigQuery executes when the view is referenced.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>use<wbr>Legacy<wbr>Sql</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}Specifies whether to use BigQuery's legacy SQL for this view.
The default value is true. If set to false, the view will use BigQuery's standard SQL.
{{% /md %}}</dd>

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

