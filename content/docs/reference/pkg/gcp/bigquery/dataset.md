
---
title: "Dataset"
block_external_search_index: true
---



Datasets allow you to organize and control access to your tables.



## Create a Dataset Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/bigquery/#Dataset">Dataset</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/bigquery/#DatasetArgs">DatasetArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Dataset</span><span class="p">(resource_name, opts=None, </span>accesses=None<span class="p">, </span>dataset_id=None<span class="p">, </span>default_encryption_configuration=None<span class="p">, </span>default_partition_expiration_ms=None<span class="p">, </span>default_table_expiration_ms=None<span class="p">, </span>delete_contents_on_destroy=None<span class="p">, </span>description=None<span class="p">, </span>friendly_name=None<span class="p">, </span>labels=None<span class="p">, </span>location=None<span class="p">, </span>project=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewDataset<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/bigquery?tab=doc#DatasetArgs">DatasetArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/bigquery?tab=doc#Dataset">Dataset</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.BigQuery.Dataset.html">Dataset</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.BigQuery.DatasetArgs.html">DatasetArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
    <dd>{{% md %}}A unique ID for this dataset, without the project name. The ID must contain only letters (a-z, A-Z), numbers (0-9), or
underscores (_). The maximum length is 1,024 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Accesses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasetaccess">List&lt;Dataset<wbr>Access<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}An array of objects that define dataset access for one or more entities.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Encryption<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasetdefaultencryptionconfiguration">Dataset<wbr>Default<wbr>Encryption<wbr>Configuration<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}The default encryption key for all tables in the dataset. Once this property is set, all newly-created partitioned
tables in the dataset will have encryption key set to this value, unless table creation request (or query) overrides the
key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Partition<wbr>Expiration<wbr>Ms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The default partition expiration for all partitioned tables in the dataset, in milliseconds. Once this property is set,
all newly-created partitioned tables in the dataset will have an 'expirationMs' property in the 'timePartitioning'
settings set to this value, and changing the value will only affect new tables, not existing ones. The storage in a
partition will have an expiration time of its partition time plus this value. Setting this property overrides the use of
'defaultTableExpirationMs' for partitioned tables: only one of 'defaultTableExpirationMs' and
'defaultPartitionExpirationMs' will be used for any new partitioned table. If you provide an explicit
'timePartitioning.expirationMs' when creating or updating a partitioned table, that value takes precedence over the
default partition expiration time indicated by this property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Table<wbr>Expiration<wbr>Ms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The default lifetime of all tables in the dataset, in milliseconds. The minimum value is 3600000 milliseconds (one
hour). Once this property is set, all newly-created tables in the dataset will have an 'expirationTime' property set to
the creation time plus the value in this property, and changing the value will only affect new tables, not existing
ones. When the 'expirationTime' for a given table is reached, that table will be deleted automatically. If a table's
'expirationTime' is modified or removed before the table expires, or if you provide an explicit 'expirationTime' when
creating a table, that value takes precedence over the default expiration time indicated by this property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Delete<wbr>Contents<wbr>On<wbr>Destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}If set to `true`, delete all the tables in the
dataset when destroying the resource; otherwise,
destroying the resource will fail if tables are present.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A user-friendly description of the dataset
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Friendly<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A descriptive name for the dataset
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}The labels associated with this dataset. You can use these to organize and group your datasets
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The geographic location where the dataset should reside. See [official
docs](https://cloud.google.com/bigquery/docs/dataset-locations). There are two types of locations, regional or
multi-regional. A regional location is a specific geographic place, such as Tokyo, and a multi-regional location is a
large geographic area, such as the United States, that contains at least two geographic places. Possible regional values
include: 'asia-east1', 'asia-northeast1', 'asia-southeast1', 'australia-southeast1', 'europe-north1', 'europe-west2' and
'us-east4'. Possible multi-regional values: 'EU' and 'US'. The default value is multi-regional location 'US'. Changing
this forces a new resource to be created.
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
    <dd>{{% md %}}A unique ID for this dataset, without the project name. The ID must contain only letters (a-z, A-Z), numbers (0-9), or
underscores (_). The maximum length is 1,024 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Accesses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasetaccess">[]Dataset<wbr>Access</a></span>
    </dt>
    <dd>{{% md %}}An array of objects that define dataset access for one or more entities.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Encryption<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasetdefaultencryptionconfiguration">Dataset<wbr>Default<wbr>Encryption<wbr>Configuration</a></span>
    </dt>
    <dd>{{% md %}}The default encryption key for all tables in the dataset. Once this property is set, all newly-created partitioned
tables in the dataset will have encryption key set to this value, unless table creation request (or query) overrides the
key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Partition<wbr>Expiration<wbr>Ms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The default partition expiration for all partitioned tables in the dataset, in milliseconds. Once this property is set,
all newly-created partitioned tables in the dataset will have an 'expirationMs' property in the 'timePartitioning'
settings set to this value, and changing the value will only affect new tables, not existing ones. The storage in a
partition will have an expiration time of its partition time plus this value. Setting this property overrides the use of
'defaultTableExpirationMs' for partitioned tables: only one of 'defaultTableExpirationMs' and
'defaultPartitionExpirationMs' will be used for any new partitioned table. If you provide an explicit
'timePartitioning.expirationMs' when creating or updating a partitioned table, that value takes precedence over the
default partition expiration time indicated by this property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Table<wbr>Expiration<wbr>Ms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The default lifetime of all tables in the dataset, in milliseconds. The minimum value is 3600000 milliseconds (one
hour). Once this property is set, all newly-created tables in the dataset will have an 'expirationTime' property set to
the creation time plus the value in this property, and changing the value will only affect new tables, not existing
ones. When the 'expirationTime' for a given table is reached, that table will be deleted automatically. If a table's
'expirationTime' is modified or removed before the table expires, or if you provide an explicit 'expirationTime' when
creating a table, that value takes precedence over the default expiration time indicated by this property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Delete<wbr>Contents<wbr>On<wbr>Destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}If set to `true`, delete all the tables in the
dataset when destroying the resource; otherwise,
destroying the resource will fail if tables are present.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A user-friendly description of the dataset
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Friendly<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A descriptive name for the dataset
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}The labels associated with this dataset. You can use these to organize and group your datasets
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The geographic location where the dataset should reside. See [official
docs](https://cloud.google.com/bigquery/docs/dataset-locations). There are two types of locations, regional or
multi-regional. A regional location is a specific geographic place, such as Tokyo, and a multi-regional location is a
large geographic area, such as the United States, that contains at least two geographic places. Possible regional values
include: 'asia-east1', 'asia-northeast1', 'asia-southeast1', 'australia-southeast1', 'europe-north1', 'europe-west2' and
'us-east4'. Possible multi-regional values: 'EU' and 'US'. The default value is multi-regional location 'US'. Changing
this forces a new resource to be created.
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
    <dd>{{% md %}}A unique ID for this dataset, without the project name. The ID must contain only letters (a-z, A-Z), numbers (0-9), or
underscores (_). The maximum length is 1,024 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>accesses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasetaccess">Dataset<wbr>Access[]</a></span>
    </dt>
    <dd>{{% md %}}An array of objects that define dataset access for one or more entities.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Encryption<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasetdefaultencryptionconfiguration">Dataset<wbr>Default<wbr>Encryption<wbr>Configuration</a></span>
    </dt>
    <dd>{{% md %}}The default encryption key for all tables in the dataset. Once this property is set, all newly-created partitioned
tables in the dataset will have encryption key set to this value, unless table creation request (or query) overrides the
key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Partition<wbr>Expiration<wbr>Ms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The default partition expiration for all partitioned tables in the dataset, in milliseconds. Once this property is set,
all newly-created partitioned tables in the dataset will have an 'expirationMs' property in the 'timePartitioning'
settings set to this value, and changing the value will only affect new tables, not existing ones. The storage in a
partition will have an expiration time of its partition time plus this value. Setting this property overrides the use of
'defaultTableExpirationMs' for partitioned tables: only one of 'defaultTableExpirationMs' and
'defaultPartitionExpirationMs' will be used for any new partitioned table. If you provide an explicit
'timePartitioning.expirationMs' when creating or updating a partitioned table, that value takes precedence over the
default partition expiration time indicated by this property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Table<wbr>Expiration<wbr>Ms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The default lifetime of all tables in the dataset, in milliseconds. The minimum value is 3600000 milliseconds (one
hour). Once this property is set, all newly-created tables in the dataset will have an 'expirationTime' property set to
the creation time plus the value in this property, and changing the value will only affect new tables, not existing
ones. When the 'expirationTime' for a given table is reached, that table will be deleted automatically. If a table's
'expirationTime' is modified or removed before the table expires, or if you provide an explicit 'expirationTime' when
creating a table, that value takes precedence over the default expiration time indicated by this property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>delete<wbr>Contents<wbr>On<wbr>Destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}If set to `true`, delete all the tables in the
dataset when destroying the resource; otherwise,
destroying the resource will fail if tables are present.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A user-friendly description of the dataset
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>friendly<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A descriptive name for the dataset
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}The labels associated with this dataset. You can use these to organize and group your datasets
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The geographic location where the dataset should reside. See [official
docs](https://cloud.google.com/bigquery/docs/dataset-locations). There are two types of locations, regional or
multi-regional. A regional location is a specific geographic place, such as Tokyo, and a multi-regional location is a
large geographic area, such as the United States, that contains at least two geographic places. Possible regional values
include: 'asia-east1', 'asia-northeast1', 'asia-southeast1', 'australia-southeast1', 'europe-north1', 'europe-west2' and
'us-east4'. Possible multi-regional values: 'EU' and 'US'. The default value is multi-regional location 'US'. Changing
this forces a new resource to be created.
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
    <dd>{{% md %}}A unique ID for this dataset, without the project name. The ID must contain only letters (a-z, A-Z), numbers (0-9), or
underscores (_). The maximum length is 1,024 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>accesses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasetaccess">List[Dataset<wbr>Access]</a></span>
    </dt>
    <dd>{{% md %}}An array of objects that define dataset access for one or more entities.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default_<wbr>encryption_<wbr>configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasetdefaultencryptionconfiguration">Dict[Dataset<wbr>Default<wbr>Encryption<wbr>Configuration]</a></span>
    </dt>
    <dd>{{% md %}}The default encryption key for all tables in the dataset. Once this property is set, all newly-created partitioned
tables in the dataset will have encryption key set to this value, unless table creation request (or query) overrides the
key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default_<wbr>partition_<wbr>expiration_<wbr>ms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The default partition expiration for all partitioned tables in the dataset, in milliseconds. Once this property is set,
all newly-created partitioned tables in the dataset will have an 'expirationMs' property in the 'timePartitioning'
settings set to this value, and changing the value will only affect new tables, not existing ones. The storage in a
partition will have an expiration time of its partition time plus this value. Setting this property overrides the use of
'defaultTableExpirationMs' for partitioned tables: only one of 'defaultTableExpirationMs' and
'defaultPartitionExpirationMs' will be used for any new partitioned table. If you provide an explicit
'timePartitioning.expirationMs' when creating or updating a partitioned table, that value takes precedence over the
default partition expiration time indicated by this property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default_<wbr>table_<wbr>expiration_<wbr>ms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The default lifetime of all tables in the dataset, in milliseconds. The minimum value is 3600000 milliseconds (one
hour). Once this property is set, all newly-created tables in the dataset will have an 'expirationTime' property set to
the creation time plus the value in this property, and changing the value will only affect new tables, not existing
ones. When the 'expirationTime' for a given table is reached, that table will be deleted automatically. If a table's
'expirationTime' is modified or removed before the table expires, or if you provide an explicit 'expirationTime' when
creating a table, that value takes precedence over the default expiration time indicated by this property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>delete_<wbr>contents_<wbr>on_<wbr>destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}If set to `true`, delete all the tables in the
dataset when destroying the resource; otherwise,
destroying the resource will fail if tables are present.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A user-friendly description of the dataset
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>friendly_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A descriptive name for the dataset
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}The labels associated with this dataset. You can use these to organize and group your datasets
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The geographic location where the dataset should reside. See [official
docs](https://cloud.google.com/bigquery/docs/dataset-locations). There are two types of locations, regional or
multi-regional. A regional location is a specific geographic place, such as Tokyo, and a multi-regional location is a
large geographic area, such as the United States, that contains at least two geographic places. Possible regional values
include: 'asia-east1', 'asia-northeast1', 'asia-southeast1', 'australia-southeast1', 'europe-north1', 'europe-west2' and
'us-east4'. Possible multi-regional values: 'EU' and 'US'. The default value is multi-regional location 'US'. Changing
this forces a new resource to be created.
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

</dl>
{{% /choosable %}}







## Dataset Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Creation<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The time when this dataset was created, in milliseconds since the epoch.
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
    <dd>{{% md %}}The date when this dataset or any of its tables was last modified, in milliseconds since the epoch.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
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
    <dd>{{% md %}}The time when this dataset was created, in milliseconds since the epoch.
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
    <dd>{{% md %}}The date when this dataset or any of its tables was last modified, in milliseconds since the epoch.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
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
    <dd>{{% md %}}The time when this dataset was created, in milliseconds since the epoch.
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
    <dd>{{% md %}}The date when this dataset or any of its tables was last modified, in milliseconds since the epoch.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
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
    <dd>{{% md %}}The time when this dataset was created, in milliseconds since the epoch.
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
    <dd>{{% md %}}The date when this dataset or any of its tables was last modified, in milliseconds since the epoch.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>self_<wbr>link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Dataset Resource

Get an existing Dataset resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/bigquery/#DatasetState">DatasetState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/gcp/bigquery/#Dataset">Dataset</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>accesses=None<span class="p">, </span>creation_time=None<span class="p">, </span>dataset_id=None<span class="p">, </span>default_encryption_configuration=None<span class="p">, </span>default_partition_expiration_ms=None<span class="p">, </span>default_table_expiration_ms=None<span class="p">, </span>delete_contents_on_destroy=None<span class="p">, </span>description=None<span class="p">, </span>etag=None<span class="p">, </span>friendly_name=None<span class="p">, </span>labels=None<span class="p">, </span>last_modified_time=None<span class="p">, </span>location=None<span class="p">, </span>project=None<span class="p">, </span>self_link=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetDataset<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/bigquery?tab=doc#DatasetState">DatasetState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/bigquery?tab=doc#Dataset">Dataset</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.BigQuery.Dataset.html">Dataset</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Gcp/Pulumi.Gcp.BigQuery.DatasetState.html">DatasetState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Accesses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasetaccess">List&lt;Dataset<wbr>Access<wbr>Args&gt;</a></span>
    </dt>
    <dd>{{% md %}}An array of objects that define dataset access for one or more entities.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Creation<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The time when this dataset was created, in milliseconds since the epoch.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dataset<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A unique ID for this dataset, without the project name. The ID must contain only letters (a-z, A-Z), numbers (0-9), or
underscores (_). The maximum length is 1,024 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Encryption<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasetdefaultencryptionconfiguration">Dataset<wbr>Default<wbr>Encryption<wbr>Configuration<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}The default encryption key for all tables in the dataset. Once this property is set, all newly-created partitioned
tables in the dataset will have encryption key set to this value, unless table creation request (or query) overrides the
key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Partition<wbr>Expiration<wbr>Ms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The default partition expiration for all partitioned tables in the dataset, in milliseconds. Once this property is set,
all newly-created partitioned tables in the dataset will have an 'expirationMs' property in the 'timePartitioning'
settings set to this value, and changing the value will only affect new tables, not existing ones. The storage in a
partition will have an expiration time of its partition time plus this value. Setting this property overrides the use of
'defaultTableExpirationMs' for partitioned tables: only one of 'defaultTableExpirationMs' and
'defaultPartitionExpirationMs' will be used for any new partitioned table. If you provide an explicit
'timePartitioning.expirationMs' when creating or updating a partitioned table, that value takes precedence over the
default partition expiration time indicated by this property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Table<wbr>Expiration<wbr>Ms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The default lifetime of all tables in the dataset, in milliseconds. The minimum value is 3600000 milliseconds (one
hour). Once this property is set, all newly-created tables in the dataset will have an 'expirationTime' property set to
the creation time plus the value in this property, and changing the value will only affect new tables, not existing
ones. When the 'expirationTime' for a given table is reached, that table will be deleted automatically. If a table's
'expirationTime' is modified or removed before the table expires, or if you provide an explicit 'expirationTime' when
creating a table, that value takes precedence over the default expiration time indicated by this property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Delete<wbr>Contents<wbr>On<wbr>Destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">bool</a></span>
    </dt>
    <dd>{{% md %}}If set to `true`, delete all the tables in the
dataset when destroying the resource; otherwise,
destroying the resource will fail if tables are present.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A user-friendly description of the dataset
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
        <span>Friendly<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}A descriptive name for the dataset
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary&lt;string, string&gt;</span>
    </dt>
    <dd>{{% md %}}The labels associated with this dataset. You can use these to organize and group your datasets
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Last<wbr>Modified<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">int</a></span>
    </dt>
    <dd>{{% md %}}The date when this dataset or any of its tables was last modified, in milliseconds since the epoch.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The geographic location where the dataset should reside. See [official
docs](https://cloud.google.com/bigquery/docs/dataset-locations). There are two types of locations, regional or
multi-regional. A regional location is a specific geographic place, such as Tokyo, and a multi-regional location is a
large geographic area, such as the United States, that contains at least two geographic places. Possible regional values
include: 'asia-east1', 'asia-northeast1', 'asia-southeast1', 'australia-southeast1', 'europe-north1', 'europe-west2' and
'us-east4'. Possible multi-regional values: 'EU' and 'US'. The default value is multi-regional location 'US'. Changing
this forces a new resource to be created.
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
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Accesses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasetaccess">[]Dataset<wbr>Access</a></span>
    </dt>
    <dd>{{% md %}}An array of objects that define dataset access for one or more entities.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Creation<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The time when this dataset was created, in milliseconds since the epoch.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dataset<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A unique ID for this dataset, without the project name. The ID must contain only letters (a-z, A-Z), numbers (0-9), or
underscores (_). The maximum length is 1,024 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Encryption<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasetdefaultencryptionconfiguration">Dataset<wbr>Default<wbr>Encryption<wbr>Configuration</a></span>
    </dt>
    <dd>{{% md %}}The default encryption key for all tables in the dataset. Once this property is set, all newly-created partitioned
tables in the dataset will have encryption key set to this value, unless table creation request (or query) overrides the
key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Partition<wbr>Expiration<wbr>Ms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The default partition expiration for all partitioned tables in the dataset, in milliseconds. Once this property is set,
all newly-created partitioned tables in the dataset will have an 'expirationMs' property in the 'timePartitioning'
settings set to this value, and changing the value will only affect new tables, not existing ones. The storage in a
partition will have an expiration time of its partition time plus this value. Setting this property overrides the use of
'defaultTableExpirationMs' for partitioned tables: only one of 'defaultTableExpirationMs' and
'defaultPartitionExpirationMs' will be used for any new partitioned table. If you provide an explicit
'timePartitioning.expirationMs' when creating or updating a partitioned table, that value takes precedence over the
default partition expiration time indicated by this property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Default<wbr>Table<wbr>Expiration<wbr>Ms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The default lifetime of all tables in the dataset, in milliseconds. The minimum value is 3600000 milliseconds (one
hour). Once this property is set, all newly-created tables in the dataset will have an 'expirationTime' property set to
the creation time plus the value in this property, and changing the value will only affect new tables, not existing
ones. When the 'expirationTime' for a given table is reached, that table will be deleted automatically. If a table's
'expirationTime' is modified or removed before the table expires, or if you provide an explicit 'expirationTime' when
creating a table, that value takes precedence over the default expiration time indicated by this property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Delete<wbr>Contents<wbr>On<wbr>Destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#boolean">bool</a></span>
    </dt>
    <dd>{{% md %}}If set to `true`, delete all the tables in the
dataset when destroying the resource; otherwise,
destroying the resource will fail if tables are present.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A user-friendly description of the dataset
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
        <span>Friendly<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}A descriptive name for the dataset
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]string</span>
    </dt>
    <dd>{{% md %}}The labels associated with this dataset. You can use these to organize and group your datasets
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Last<wbr>Modified<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#integer">int</a></span>
    </dt>
    <dd>{{% md %}}The date when this dataset or any of its tables was last modified, in milliseconds since the epoch.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The geographic location where the dataset should reside. See [official
docs](https://cloud.google.com/bigquery/docs/dataset-locations). There are two types of locations, regional or
multi-regional. A regional location is a specific geographic place, such as Tokyo, and a multi-regional location is a
large geographic area, such as the United States, that contains at least two geographic places. Possible regional values
include: 'asia-east1', 'asia-northeast1', 'asia-southeast1', 'australia-southeast1', 'europe-north1', 'europe-west2' and
'us-east4'. Possible multi-regional values: 'EU' and 'US'. The default value is multi-regional location 'US'. Changing
this forces a new resource to be created.
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
        <span>Self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>accesses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasetaccess">Dataset<wbr>Access[]</a></span>
    </dt>
    <dd>{{% md %}}An array of objects that define dataset access for one or more entities.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>creation<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The time when this dataset was created, in milliseconds since the epoch.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dataset<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A unique ID for this dataset, without the project name. The ID must contain only letters (a-z, A-Z), numbers (0-9), or
underscores (_). The maximum length is 1,024 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Encryption<wbr>Configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasetdefaultencryptionconfiguration">Dataset<wbr>Default<wbr>Encryption<wbr>Configuration</a></span>
    </dt>
    <dd>{{% md %}}The default encryption key for all tables in the dataset. Once this property is set, all newly-created partitioned
tables in the dataset will have encryption key set to this value, unless table creation request (or query) overrides the
key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Partition<wbr>Expiration<wbr>Ms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The default partition expiration for all partitioned tables in the dataset, in milliseconds. Once this property is set,
all newly-created partitioned tables in the dataset will have an 'expirationMs' property in the 'timePartitioning'
settings set to this value, and changing the value will only affect new tables, not existing ones. The storage in a
partition will have an expiration time of its partition time plus this value. Setting this property overrides the use of
'defaultTableExpirationMs' for partitioned tables: only one of 'defaultTableExpirationMs' and
'defaultPartitionExpirationMs' will be used for any new partitioned table. If you provide an explicit
'timePartitioning.expirationMs' when creating or updating a partitioned table, that value takes precedence over the
default partition expiration time indicated by this property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default<wbr>Table<wbr>Expiration<wbr>Ms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The default lifetime of all tables in the dataset, in milliseconds. The minimum value is 3600000 milliseconds (one
hour). Once this property is set, all newly-created tables in the dataset will have an 'expirationTime' property set to
the creation time plus the value in this property, and changing the value will only affect new tables, not existing
ones. When the 'expirationTime' for a given table is reached, that table will be deleted automatically. If a table's
'expirationTime' is modified or removed before the table expires, or if you provide an explicit 'expirationTime' when
creating a table, that value takes precedence over the default expiration time indicated by this property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>delete<wbr>Contents<wbr>On<wbr>Destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/boolean">boolean</a></span>
    </dt>
    <dd>{{% md %}}If set to `true`, delete all the tables in the
dataset when destroying the resource; otherwise,
destroying the resource will fail if tables are present.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A user-friendly description of the dataset
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
        <span>friendly<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}A descriptive name for the dataset
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: string}</span>
    </dt>
    <dd>{{% md %}}The labels associated with this dataset. You can use these to organize and group your datasets
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>last<wbr>Modified<wbr>Time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/integer">number</a></span>
    </dt>
    <dd>{{% md %}}The date when this dataset or any of its tables was last modified, in milliseconds since the epoch.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The geographic location where the dataset should reside. See [official
docs](https://cloud.google.com/bigquery/docs/dataset-locations). There are two types of locations, regional or
multi-regional. A regional location is a specific geographic place, such as Tokyo, and a multi-regional location is a
large geographic area, such as the United States, that contains at least two geographic places. Possible regional values
include: 'asia-east1', 'asia-northeast1', 'asia-southeast1', 'australia-southeast1', 'europe-north1', 'europe-west2' and
'us-east4'. Possible multi-regional values: 'EU' and 'US'. The default value is multi-regional location 'US'. Changing
this forces a new resource to be created.
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
        <span>self<wbr>Link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>accesses</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasetaccess">List[Dataset<wbr>Access]</a></span>
    </dt>
    <dd>{{% md %}}An array of objects that define dataset access for one or more entities.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>creation_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The time when this dataset was created, in milliseconds since the epoch.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dataset_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A unique ID for this dataset, without the project name. The ID must contain only letters (a-z, A-Z), numbers (0-9), or
underscores (_). The maximum length is 1,024 characters.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default_<wbr>encryption_<wbr>configuration</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasetdefaultencryptionconfiguration">Dict[Dataset<wbr>Default<wbr>Encryption<wbr>Configuration]</a></span>
    </dt>
    <dd>{{% md %}}The default encryption key for all tables in the dataset. Once this property is set, all newly-created partitioned
tables in the dataset will have encryption key set to this value, unless table creation request (or query) overrides the
key.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default_<wbr>partition_<wbr>expiration_<wbr>ms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The default partition expiration for all partitioned tables in the dataset, in milliseconds. Once this property is set,
all newly-created partitioned tables in the dataset will have an 'expirationMs' property in the 'timePartitioning'
settings set to this value, and changing the value will only affect new tables, not existing ones. The storage in a
partition will have an expiration time of its partition time plus this value. Setting this property overrides the use of
'defaultTableExpirationMs' for partitioned tables: only one of 'defaultTableExpirationMs' and
'defaultPartitionExpirationMs' will be used for any new partitioned table. If you provide an explicit
'timePartitioning.expirationMs' when creating or updating a partitioned table, that value takes precedence over the
default partition expiration time indicated by this property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>default_<wbr>table_<wbr>expiration_<wbr>ms</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The default lifetime of all tables in the dataset, in milliseconds. The minimum value is 3600000 milliseconds (one
hour). Once this property is set, all newly-created tables in the dataset will have an 'expirationTime' property set to
the creation time plus the value in this property, and changing the value will only affect new tables, not existing
ones. When the 'expirationTime' for a given table is reached, that table will be deleted automatically. If a table's
'expirationTime' is modified or removed before the table expires, or if you provide an explicit 'expirationTime' when
creating a table, that value takes precedence over the default expiration time indicated by this property.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>delete_<wbr>contents_<wbr>on_<wbr>destroy</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">bool</a></span>
    </dt>
    <dd>{{% md %}}If set to `true`, delete all the tables in the
dataset when destroying the resource; otherwise,
destroying the resource will fail if tables are present.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A user-friendly description of the dataset
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
        <span>friendly_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}A descriptive name for the dataset
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>labels</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, str]</span>
    </dt>
    <dd>{{% md %}}The labels associated with this dataset. You can use these to organize and group your datasets
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>last_<wbr>modified_<wbr>time</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">float</a></span>
    </dt>
    <dd>{{% md %}}The date when this dataset or any of its tables was last modified, in milliseconds since the epoch.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>location</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The geographic location where the dataset should reside. See [official
docs](https://cloud.google.com/bigquery/docs/dataset-locations). There are two types of locations, regional or
multi-regional. A regional location is a specific geographic place, such as Tokyo, and a multi-regional location is a
large geographic area, such as the United States, that contains at least two geographic places. Possible regional values
include: 'asia-east1', 'asia-northeast1', 'asia-southeast1', 'australia-southeast1', 'europe-north1', 'europe-west2' and
'us-east4'. Possible multi-regional values: 'EU' and 'US'. The default value is multi-regional location 'US'. Changing
this forces a new resource to be created.
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
        <span>self_<wbr>link</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}The URI of the created resource.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Dataset<wbr>Access</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#DatasetAccess">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#DatasetAccess">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/bigquery?tab=doc#DatasetAccessArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/bigquery?tab=doc#DatasetAccessOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Group<wbr>By<wbr>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Special<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>User<wbr>By<wbr>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>View</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasetaccessview">Dataset<wbr>Access<wbr>View<wbr>Args</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Group<wbr>By<wbr>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Role</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Special<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>User<wbr>By<wbr>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>View</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasetaccessview">Dataset<wbr>Access<wbr>View</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>group<wbr>By<wbr>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>special<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>user<wbr>By<wbr>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>view</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasetaccessview">Dataset<wbr>Access<wbr>View</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>domain</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>group<wbr>By<wbr>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>role</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>special<wbr>Group</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>user<wbr>By<wbr>Email</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>view</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasetaccessview">Dict[Dataset<wbr>Access<wbr>View]</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Dataset<wbr>Access<wbr>View</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#DatasetAccessView">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#DatasetAccessView">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/bigquery?tab=doc#DatasetAccessViewArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/bigquery?tab=doc#DatasetAccessViewOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Dataset<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Table<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Table<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://golang.org/pkg/builtin/#string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>project<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>table<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>project_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>table_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.python.org/3/library/stdtypes.html">str</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Dataset<wbr>Default<wbr>Encryption<wbr>Configuration</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/input/#DatasetDefaultEncryptionConfiguration">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/gcp/types/output/#DatasetDefaultEncryptionConfiguration">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/bigquery?tab=doc#DatasetDefaultEncryptionConfigurationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/bigquery?tab=doc#DatasetDefaultEncryptionConfigurationOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Kms<wbr>Key<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

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
    <dd>{{% md %}}{{% /md %}}</dd>

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
    <dd>{{% md %}}{{% /md %}}</dd>

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

