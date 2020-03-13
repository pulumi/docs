
---
title: "CatalogTable"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Provides a Glue Catalog Table Resource. You can refer to the [Glue Developer Guide](http://docs.aws.amazon.com/glue/latest/dg/populate-data-catalog.html) for a full explanation of the Glue Data Catalog functionality.

## Example Usage

### Basic Table

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const awsGlueCatalogTable = new aws.glue.CatalogTable("aws.glue.CatalogTable", {
    databaseName: "MyCatalogDatabase",
    name: "MyCatalogTable",
});
```

### Parquet Table for Athena

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const awsGlueCatalogTable = new aws.glue.CatalogTable("aws.glue.CatalogTable", {
    databaseName: "MyCatalogDatabase",
    name: "MyCatalogTable",
    parameters: {
        EXTERNAL: "TRUE",
        "parquet.compression": "SNAPPY",
    },
    storageDescriptor: {
        columns: [
            {
                name: "my_string",
                type: "string",
            },
            {
                name: "my_double",
                type: "double",
            },
            {
                comment: "",
                name: "my_date",
                type: "date",
            },
            {
                comment: "",
                name: "my_bigint",
                type: "bigint",
            },
            {
                comment: "",
                name: "my_struct",
                type: "struct<my_nested_string:string>",
            },
        ],
        inputFormat: "org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat",
        location: "s3://my-bucket/event-streams/my-stream",
        outputFormat: "org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat",
        serDeInfo: {
            name: "my-stream",
            parameters: {
                "serialization.format": 1,
            },
            serializationLibrary: "org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe",
        },
    },
    tableType: "EXTERNAL_TABLE",
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_catalog_table.html.markdown.



## Create a CatalogTable Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/glue/#CatalogTable">CatalogTable</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/glue/#CatalogTableArgs">CatalogTableArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">CatalogTable</span><span class="p">(resource_name, id, opts=None, </span>catalog_id=None<span class="p">, </span>database_name=None<span class="p">, </span>description=None<span class="p">, </span>name=None<span class="p">, </span>owner=None<span class="p">, </span>parameters=None<span class="p">, </span>partition_keys=None<span class="p">, </span>retention=None<span class="p">, </span>storage_descriptor=None<span class="p">, </span>table_type=None<span class="p">, </span>view_expanded_text=None<span class="p">, </span>view_original_text=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewCatalogTable<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#CatalogTableArgs">CatalogTableArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#CatalogTable">CatalogTable</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.CatalogTable.html">CatalogTable</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.CatalogTableArgs.html">CatalogTableArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a CatalogTable resource with the given unique name, arguments, and options.

{{% lang nodejs %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang go %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang csharp %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>args</strong> &ndash;  (Optional)  The arguments to use to populate this resource's properties.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

The following arguments are supported:


{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Catalog<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ID of the Glue Catalog and database to create the table in. If omitted, this defaults to the AWS Account ID plus the database name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Database<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Name of the metadata database where the table metadata resides. For Hive compatibility, this must be all lowercase.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Description of the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the SerDe.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Owner</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Owner of the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parameters</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of initialization parameters for the SerDe, in key-value form.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Partition<wbr>Keys</td>
            <td class="align-top">
                
                <code><a href="#catalogtablepartitionkey">List&lt;Pulumi.<wbr>Aws.<wbr>Glue.<wbr>Catalog<wbr>Table<wbr>Partition<wbr>Key<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Retention</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Retention time for this table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Storage<wbr>Descriptor</td>
            <td class="align-top">
                
                <code><a href="#catalogtablestoragedescriptor">Pulumi.<wbr>Aws.<wbr>Glue.<wbr>Catalog<wbr>Table<wbr>Storage<wbr>Descriptor<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A storage descriptor object containing information about the physical storage of this table. You can refer to the [Glue Developer Guide](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-StorageDescriptor) for a full explanation of this object.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Table<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of this table (EXTERNAL_TABLE, VIRTUAL_VIEW, etc.).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">View<wbr>Expanded<wbr>Text</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If the table is a view, the expanded text of the view; otherwise null.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">View<wbr>Original<wbr>Text</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If the table is a view, the original text of the view; otherwise null.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Catalog<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ID of the Glue Catalog and database to create the table in. If omitted, this defaults to the AWS Account ID plus the database name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Database<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Name of the metadata database where the table metadata resides. For Hive compatibility, this must be all lowercase.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Description of the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the SerDe.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Owner</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Owner of the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parameters</td>
            <td class="align-top">
                
                <code>map[string]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of initialization parameters for the SerDe, in key-value form.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Partition<wbr>Keys</td>
            <td class="align-top">
                
                <code><a href="#catalogtablepartitionkey">[]glue.<wbr>Catalog<wbr>Table<wbr>Partition<wbr>Key</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Retention</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Retention time for this table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Storage<wbr>Descriptor</td>
            <td class="align-top">
                
                <code><a href="#catalogtablestoragedescriptor">*glue.<wbr>Catalog<wbr>Table<wbr>Storage<wbr>Descriptor</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A storage descriptor object containing information about the physical storage of this table. You can refer to the [Glue Developer Guide](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-StorageDescriptor) for a full explanation of this object.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Table<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of this table (EXTERNAL_TABLE, VIRTUAL_VIEW, etc.).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">View<wbr>Expanded<wbr>Text</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If the table is a view, the expanded text of the view; otherwise null.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">View<wbr>Original<wbr>Text</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If the table is a view, the original text of the view; otherwise null.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">catalog<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ID of the Glue Catalog and database to create the table in. If omitted, this defaults to the AWS Account ID plus the database name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">database<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Name of the metadata database where the table metadata resides. For Hive compatibility, this must be all lowercase.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Description of the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the SerDe.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">owner</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Owner of the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parameters</td>
            <td class="align-top">
                
                <code>{[key: string]: string}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of initialization parameters for the SerDe, in key-value form.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">partition<wbr>Keys</td>
            <td class="align-top">
                
                <code><a href="#catalogtablepartitionkey">glue.<wbr>Catalog<wbr>Table<wbr>Partition<wbr>Key[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">retention</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Retention time for this table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">storage<wbr>Descriptor</td>
            <td class="align-top">
                
                <code><a href="#catalogtablestoragedescriptor">glue.<wbr>Catalog<wbr>Table<wbr>Storage<wbr>Descriptor?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A storage descriptor object containing information about the physical storage of this table. You can refer to the [Glue Developer Guide](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-StorageDescriptor) for a full explanation of this object.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">table<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of this table (EXTERNAL_TABLE, VIRTUAL_VIEW, etc.).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">view<wbr>Expanded<wbr>Text</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If the table is a view, the expanded text of the view; otherwise null.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">view<wbr>Original<wbr>Text</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If the table is a view, the original text of the view; otherwise null.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">catalog_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ID of the Glue Catalog and database to create the table in. If omitted, this defaults to the AWS Account ID plus the database name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">database_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Name of the metadata database where the table metadata resides. For Hive compatibility, this must be all lowercase.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Description of the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the SerDe.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">owner</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Owner of the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parameters</td>
            <td class="align-top">
                
                <code>dict{string}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of initialization parameters for the SerDe, in key-value form.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">partition_<wbr>keys</td>
            <td class="align-top">
                
                <code><a href="#catalogtablepartitionkey">list[catalog_<wbr>table_<wbr>partition_<wbr>key]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">retention</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Retention time for this table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">storage_<wbr>descriptor</td>
            <td class="align-top">
                
                <code><a href="#catalogtablestoragedescriptor">dict{catalog_<wbr>table_<wbr>storage_<wbr>descriptor}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A storage descriptor object containing information about the physical storage of this table. You can refer to the [Glue Developer Guide](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-StorageDescriptor) for a full explanation of this object.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">table_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of this table (EXTERNAL_TABLE, VIRTUAL_VIEW, etc.).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">view_<wbr>expanded_<wbr>text</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If the table is a view, the expanded text of the view; otherwise null.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">view_<wbr>original_<wbr>text</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If the table is a view, the original text of the view; otherwise null.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## CatalogTable Output Properties

The following output properties are available:



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Catalog<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} ID of the Glue Catalog and database to create the table in. If omitted, this defaults to the AWS Account ID plus the database name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Database<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the metadata database where the table metadata resides. For Hive compatibility, this must be all lowercase.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Description of the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the SerDe.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Owner</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Owner of the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parameters</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A map of initialization parameters for the SerDe, in key-value form.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Partition<wbr>Keys</td>
            <td class="align-top">
                
                <code><a href="#catalogtablepartitionkey">List&lt;Pulumi.<wbr>Aws.<wbr>Glue.<wbr>Catalog<wbr>Table<wbr>Partition<wbr>Key&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Retention</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} Retention time for this table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Storage<wbr>Descriptor</td>
            <td class="align-top">
                
                <code><a href="#catalogtablestoragedescriptor">Pulumi.<wbr>Aws.<wbr>Glue.<wbr>Catalog<wbr>Table<wbr>Storage<wbr>Descriptor?</a></code>
            </td>
            <td class="align-top">{{% md %}} A storage descriptor object containing information about the physical storage of this table. You can refer to the [Glue Developer Guide](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-StorageDescriptor) for a full explanation of this object.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Table<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The type of this table (EXTERNAL_TABLE, VIRTUAL_VIEW, etc.).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">View<wbr>Expanded<wbr>Text</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} If the table is a view, the expanded text of the view; otherwise null.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">View<wbr>Original<wbr>Text</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} If the table is a view, the original text of the view; otherwise null.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Catalog<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} ID of the Glue Catalog and database to create the table in. If omitted, this defaults to the AWS Account ID plus the database name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Database<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the metadata database where the table metadata resides. For Hive compatibility, this must be all lowercase.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Description of the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the SerDe.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Owner</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Owner of the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parameters</td>
            <td class="align-top">
                
                <code>map[string]string</code>
            </td>
            <td class="align-top">{{% md %}} A map of initialization parameters for the SerDe, in key-value form.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Partition<wbr>Keys</td>
            <td class="align-top">
                
                <code><a href="#catalogtablepartitionkey">[]glue.<wbr>Catalog<wbr>Table<wbr>Partition<wbr>Key</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Retention</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} Retention time for this table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Storage<wbr>Descriptor</td>
            <td class="align-top">
                
                <code><a href="#catalogtablestoragedescriptor">*glue.<wbr>Catalog<wbr>Table<wbr>Storage<wbr>Descriptor</a></code>
            </td>
            <td class="align-top">{{% md %}} A storage descriptor object containing information about the physical storage of this table. You can refer to the [Glue Developer Guide](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-StorageDescriptor) for a full explanation of this object.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Table<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The type of this table (EXTERNAL_TABLE, VIRTUAL_VIEW, etc.).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">View<wbr>Expanded<wbr>Text</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} If the table is a view, the expanded text of the view; otherwise null.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">View<wbr>Original<wbr>Text</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} If the table is a view, the original text of the view; otherwise null.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">catalog<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} ID of the Glue Catalog and database to create the table in. If omitted, this defaults to the AWS Account ID plus the database name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">database<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the metadata database where the table metadata resides. For Hive compatibility, this must be all lowercase.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Description of the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Name of the SerDe.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">owner</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Owner of the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parameters</td>
            <td class="align-top">
                
                <code>{[key: string]: string}?</code>
            </td>
            <td class="align-top">{{% md %}} A map of initialization parameters for the SerDe, in key-value form.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">partition<wbr>Keys</td>
            <td class="align-top">
                
                <code><a href="#catalogtablepartitionkey">glue.<wbr>Catalog<wbr>Table<wbr>Partition<wbr>Key[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">retention</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} Retention time for this table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">storage<wbr>Descriptor</td>
            <td class="align-top">
                
                <code><a href="#catalogtablestoragedescriptor">glue.<wbr>Catalog<wbr>Table<wbr>Storage<wbr>Descriptor?</a></code>
            </td>
            <td class="align-top">{{% md %}} A storage descriptor object containing information about the physical storage of this table. You can refer to the [Glue Developer Guide](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-StorageDescriptor) for a full explanation of this object.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">table<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The type of this table (EXTERNAL_TABLE, VIRTUAL_VIEW, etc.).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">view<wbr>Expanded<wbr>Text</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} If the table is a view, the expanded text of the view; otherwise null.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">view<wbr>Original<wbr>Text</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} If the table is a view, the original text of the view; otherwise null.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">catalog_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} ID of the Glue Catalog and database to create the table in. If omitted, this defaults to the AWS Account ID plus the database name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">database_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Name of the metadata database where the table metadata resides. For Hive compatibility, this must be all lowercase.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Description of the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Name of the SerDe.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">owner</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Owner of the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parameters</td>
            <td class="align-top">
                
                <code>dict{string}</code>
            </td>
            <td class="align-top">{{% md %}} A map of initialization parameters for the SerDe, in key-value form.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">partition_<wbr>keys</td>
            <td class="align-top">
                
                <code><a href="#catalogtablepartitionkey">list[catalog_<wbr>table_<wbr>partition_<wbr>key]</a></code>
            </td>
            <td class="align-top">{{% md %}} A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">retention</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} Retention time for this table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">storage_<wbr>descriptor</td>
            <td class="align-top">
                
                <code><a href="#catalogtablestoragedescriptor">dict{catalog_<wbr>table_<wbr>storage_<wbr>descriptor}</a></code>
            </td>
            <td class="align-top">{{% md %}} A storage descriptor object containing information about the physical storage of this table. You can refer to the [Glue Developer Guide](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-StorageDescriptor) for a full explanation of this object.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">table_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The type of this table (EXTERNAL_TABLE, VIRTUAL_VIEW, etc.).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">view_<wbr>expanded_<wbr>text</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} If the table is a view, the expanded text of the view; otherwise null.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">view_<wbr>original_<wbr>text</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} If the table is a view, the original text of the view; otherwise null.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing CatalogTable Resource

{{< langchoose csharp nojavascript >}}

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CatalogTableState, opts?: pulumi.CustomResourceOptions): CatalogTable;
```

```python
def get(resource_name, id, opts=None, catalog_<wbr>id=None, database_<wbr>name=None, description=None, name=None, owner=None, parameters=None, partition_<wbr>keys=None, retention=None, storage_<wbr>descriptor=None, table_<wbr>type=None, view_<wbr>expanded_<wbr>text=None, view_<wbr>original_<wbr>text=None)
```

```go
func GetCatalogTable(ctx *pulumi.Context, name string, id pulumi.IDInput, state *CatalogTableState, opts ...pulumi.ResourceOption) (*Bucket, error)
```

```csharp
public static CatalogTable Get(string name, Input<string> id, CatalogTableState? state = null, CustomResourceOptions? options = null);
```

Get an existing CatalogTable resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{% lang nodejs %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang go %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

{{% lang csharp %}}

<ul class="pl-10">
    <li><strong>name</strong> &ndash; (Required) The unique name of the resulting resource.</li>
    <li><strong>id</strong> &ndash; (Required) The _unique_ provider ID of the resource to lookup.</li>
    <li><strong>state</strong> &ndash; (Optional) Any extra arguments used during the lookup.</li>
    <li><strong>opts</strong> &ndash; (Optional) A bag of options that control this resource's behavior.</li>
</ul>

{{% /lang %}}

The following state arguments are supported:


{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Catalog<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ID of the Glue Catalog and database to create the table in. If omitted, this defaults to the AWS Account ID plus the database name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Database<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the metadata database where the table metadata resides. For Hive compatibility, this must be all lowercase.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Description of the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the SerDe.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Owner</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Owner of the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parameters</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of initialization parameters for the SerDe, in key-value form.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Partition<wbr>Keys</td>
            <td class="align-top">
                
                <code><a href="#catalogtablepartitionkey">List&lt;Pulumi.<wbr>Aws.<wbr>Glue.<wbr>Catalog<wbr>Table<wbr>Partition<wbr>Key<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Retention</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Retention time for this table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Storage<wbr>Descriptor</td>
            <td class="align-top">
                
                <code><a href="#catalogtablestoragedescriptor">Pulumi.<wbr>Aws.<wbr>Glue.<wbr>Catalog<wbr>Table<wbr>Storage<wbr>Descriptor<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A storage descriptor object containing information about the physical storage of this table. You can refer to the [Glue Developer Guide](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-StorageDescriptor) for a full explanation of this object.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Table<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of this table (EXTERNAL_TABLE, VIRTUAL_VIEW, etc.).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">View<wbr>Expanded<wbr>Text</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If the table is a view, the expanded text of the view; otherwise null.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">View<wbr>Original<wbr>Text</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If the table is a view, the original text of the view; otherwise null.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Catalog<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ID of the Glue Catalog and database to create the table in. If omitted, this defaults to the AWS Account ID plus the database name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Database<wbr>Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the metadata database where the table metadata resides. For Hive compatibility, this must be all lowercase.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Description of the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the SerDe.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Owner</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Owner of the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parameters</td>
            <td class="align-top">
                
                <code>map[string]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of initialization parameters for the SerDe, in key-value form.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Partition<wbr>Keys</td>
            <td class="align-top">
                
                <code><a href="#catalogtablepartitionkey">[]glue.<wbr>Catalog<wbr>Table<wbr>Partition<wbr>Key</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Retention</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Retention time for this table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Storage<wbr>Descriptor</td>
            <td class="align-top">
                
                <code><a href="#catalogtablestoragedescriptor">*glue.<wbr>Catalog<wbr>Table<wbr>Storage<wbr>Descriptor</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A storage descriptor object containing information about the physical storage of this table. You can refer to the [Glue Developer Guide](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-StorageDescriptor) for a full explanation of this object.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Table<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of this table (EXTERNAL_TABLE, VIRTUAL_VIEW, etc.).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">View<wbr>Expanded<wbr>Text</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If the table is a view, the expanded text of the view; otherwise null.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">View<wbr>Original<wbr>Text</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If the table is a view, the original text of the view; otherwise null.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">catalog<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ID of the Glue Catalog and database to create the table in. If omitted, this defaults to the AWS Account ID plus the database name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">database<wbr>Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the metadata database where the table metadata resides. For Hive compatibility, this must be all lowercase.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Description of the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the SerDe.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">owner</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Owner of the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parameters</td>
            <td class="align-top">
                
                <code>{[key: string]: string}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of initialization parameters for the SerDe, in key-value form.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">partition<wbr>Keys</td>
            <td class="align-top">
                
                <code><a href="#catalogtablepartitionkey">glue.<wbr>Catalog<wbr>Table<wbr>Partition<wbr>Key[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">retention</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Retention time for this table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">storage<wbr>Descriptor</td>
            <td class="align-top">
                
                <code><a href="#catalogtablestoragedescriptor">glue.<wbr>Catalog<wbr>Table<wbr>Storage<wbr>Descriptor?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A storage descriptor object containing information about the physical storage of this table. You can refer to the [Glue Developer Guide](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-StorageDescriptor) for a full explanation of this object.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">table<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of this table (EXTERNAL_TABLE, VIRTUAL_VIEW, etc.).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">view<wbr>Expanded<wbr>Text</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If the table is a view, the expanded text of the view; otherwise null.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">view<wbr>Original<wbr>Text</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If the table is a view, the original text of the view; otherwise null.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">catalog_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
ID of the Glue Catalog and database to create the table in. If omitted, this defaults to the AWS Account ID plus the database name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">database_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the metadata database where the table metadata resides. For Hive compatibility, this must be all lowercase.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Description of the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the SerDe.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">owner</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Owner of the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parameters</td>
            <td class="align-top">
                
                <code>dict{string}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of initialization parameters for the SerDe, in key-value form.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">partition_<wbr>keys</td>
            <td class="align-top">
                
                <code><a href="#catalogtablepartitionkey">list[catalog_<wbr>table_<wbr>partition_<wbr>key]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of columns by which the table is partitioned. Only primitive types are supported as partition keys.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">retention</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Retention time for this table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">storage_<wbr>descriptor</td>
            <td class="align-top">
                
                <code><a href="#catalogtablestoragedescriptor">dict{catalog_<wbr>table_<wbr>storage_<wbr>descriptor}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A storage descriptor object containing information about the physical storage of this table. You can refer to the [Glue Developer Guide](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-catalog-tables.html#aws-glue-api-catalog-tables-StorageDescriptor) for a full explanation of this object.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">table_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of this table (EXTERNAL_TABLE, VIRTUAL_VIEW, etc.).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">view_<wbr>expanded_<wbr>text</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If the table is a view, the expanded text of the view; otherwise null.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">view_<wbr>original_<wbr>text</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
If the table is a view, the original text of the view; otherwise null.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### CatalogTablePartitionKey
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#CatalogTablePartitionKey">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#CatalogTablePartitionKey">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#CatalogTablePartitionKeyArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#CatalogTablePartitionKeyOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.CatalogTablePartitionKeyArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.CatalogTablePartitionKey.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Comment</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Free-form text comment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Name of the SerDe.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The datatype of data in the Column.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Comment</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Free-form text comment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Name of the SerDe.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The datatype of data in the Column.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">comment</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Free-form text comment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Name of the SerDe.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The datatype of data in the Column.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">comment</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Free-form text comment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Name of the SerDe.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The datatype of data in the Column.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### CatalogTableStorageDescriptor
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#CatalogTableStorageDescriptor">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#CatalogTableStorageDescriptor">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#CatalogTableStorageDescriptorArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#CatalogTableStorageDescriptorOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.CatalogTableStorageDescriptorArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.CatalogTableStorageDescriptor.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Bucket<wbr>Columns</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of reducer grouping columns, clustering columns, and bucketing columns in the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Columns</td>
            <td class="align-top">
                
                <code><a href="#catalogtablestoragedescriptorcolumn">List&lt;Pulumi.<wbr>Aws.<wbr>Glue.<wbr>Catalog<wbr>Table<wbr>Storage<wbr>Descriptor<wbr>Column<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of the Columns in the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Compressed</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
True if the data in the table is compressed, or False if not.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Input<wbr>Format</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The input format: SequenceFileInputFormat (binary), or TextInputFormat, or a custom format.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Location</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The physical location of the table. By default this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Number<wbr>Of<wbr>Buckets</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Must be specified if the table contains any dimension columns.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Output<wbr>Format</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The output format: SequenceFileOutputFormat (binary), or IgnoreKeyTextOutputFormat, or a custom format.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parameters</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of initialization parameters for the SerDe, in key-value form.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ser<wbr>De<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#catalogtablestoragedescriptorserdeinfo">Pulumi.<wbr>Aws.<wbr>Glue.<wbr>Catalog<wbr>Table<wbr>Storage<wbr>Descriptor<wbr>Ser<wbr>De<wbr>Info<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Serialization/deserialization (SerDe) information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Skewed<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#catalogtablestoragedescriptorskewedinfo">Pulumi.<wbr>Aws.<wbr>Glue.<wbr>Catalog<wbr>Table<wbr>Storage<wbr>Descriptor<wbr>Skewed<wbr>Info<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about values that appear very frequently in a column (skewed values).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sort<wbr>Columns</td>
            <td class="align-top">
                
                <code><a href="#catalogtablestoragedescriptorsortcolumn">List&lt;Pulumi.<wbr>Aws.<wbr>Glue.<wbr>Catalog<wbr>Table<wbr>Storage<wbr>Descriptor<wbr>Sort<wbr>Column<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Order objects specifying the sort order of each bucket in the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stored<wbr>As<wbr>Sub<wbr>Directories</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
True if the table data is stored in subdirectories, or False if not.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Bucket<wbr>Columns</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of reducer grouping columns, clustering columns, and bucketing columns in the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Columns</td>
            <td class="align-top">
                
                <code><a href="#catalogtablestoragedescriptorcolumn">[]glue.<wbr>Catalog<wbr>Table<wbr>Storage<wbr>Descriptor<wbr>Column</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of the Columns in the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Compressed</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
True if the data in the table is compressed, or False if not.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Input<wbr>Format</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The input format: SequenceFileInputFormat (binary), or TextInputFormat, or a custom format.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Location</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The physical location of the table. By default this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Number<wbr>Of<wbr>Buckets</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Must be specified if the table contains any dimension columns.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Output<wbr>Format</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The output format: SequenceFileOutputFormat (binary), or IgnoreKeyTextOutputFormat, or a custom format.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parameters</td>
            <td class="align-top">
                
                <code>map[string]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of initialization parameters for the SerDe, in key-value form.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ser<wbr>De<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#catalogtablestoragedescriptorserdeinfo">*glue.<wbr>Catalog<wbr>Table<wbr>Storage<wbr>Descriptor<wbr>Ser<wbr>De<wbr>Info</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Serialization/deserialization (SerDe) information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Skewed<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#catalogtablestoragedescriptorskewedinfo">*glue.<wbr>Catalog<wbr>Table<wbr>Storage<wbr>Descriptor<wbr>Skewed<wbr>Info</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about values that appear very frequently in a column (skewed values).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sort<wbr>Columns</td>
            <td class="align-top">
                
                <code><a href="#catalogtablestoragedescriptorsortcolumn">[]glue.<wbr>Catalog<wbr>Table<wbr>Storage<wbr>Descriptor<wbr>Sort<wbr>Column</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Order objects specifying the sort order of each bucket in the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stored<wbr>As<wbr>Sub<wbr>Directories</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
True if the table data is stored in subdirectories, or False if not.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">bucket<wbr>Columns</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of reducer grouping columns, clustering columns, and bucketing columns in the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">columns</td>
            <td class="align-top">
                
                <code><a href="#catalogtablestoragedescriptorcolumn">glue.<wbr>Catalog<wbr>Table<wbr>Storage<wbr>Descriptor<wbr>Column[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of the Columns in the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">compressed</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
True if the data in the table is compressed, or False if not.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">input<wbr>Format</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The input format: SequenceFileInputFormat (binary), or TextInputFormat, or a custom format.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">location</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The physical location of the table. By default this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">number<wbr>Of<wbr>Buckets</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Must be specified if the table contains any dimension columns.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">output<wbr>Format</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The output format: SequenceFileOutputFormat (binary), or IgnoreKeyTextOutputFormat, or a custom format.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parameters</td>
            <td class="align-top">
                
                <code>{[key: string]: string}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of initialization parameters for the SerDe, in key-value form.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ser<wbr>De<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#catalogtablestoragedescriptorserdeinfo">glue.<wbr>Catalog<wbr>Table<wbr>Storage<wbr>Descriptor<wbr>Ser<wbr>De<wbr>Info?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Serialization/deserialization (SerDe) information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">skewed<wbr>Info</td>
            <td class="align-top">
                
                <code><a href="#catalogtablestoragedescriptorskewedinfo">glue.<wbr>Catalog<wbr>Table<wbr>Storage<wbr>Descriptor<wbr>Skewed<wbr>Info?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about values that appear very frequently in a column (skewed values).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sort<wbr>Columns</td>
            <td class="align-top">
                
                <code><a href="#catalogtablestoragedescriptorsortcolumn">glue.<wbr>Catalog<wbr>Table<wbr>Storage<wbr>Descriptor<wbr>Sort<wbr>Column[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Order objects specifying the sort order of each bucket in the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stored<wbr>As<wbr>Sub<wbr>Directories</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
True if the table data is stored in subdirectories, or False if not.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">bucket_<wbr>columns</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of reducer grouping columns, clustering columns, and bucketing columns in the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">columns</td>
            <td class="align-top">
                
                <code><a href="#catalogtablestoragedescriptorcolumn">list[catalog_<wbr>table_<wbr>storage_<wbr>descriptor_<wbr>column]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of the Columns in the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">compressed</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
True if the data in the table is compressed, or False if not.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">input_<wbr>format</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The input format: SequenceFileInputFormat (binary), or TextInputFormat, or a custom format.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">location</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The physical location of the table. By default this takes the form of the warehouse location, followed by the database location in the warehouse, followed by the table name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">number_<wbr>of_<wbr>buckets</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Must be specified if the table contains any dimension columns.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">output_<wbr>format</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The output format: SequenceFileOutputFormat (binary), or IgnoreKeyTextOutputFormat, or a custom format.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parameters</td>
            <td class="align-top">
                
                <code>dict{string}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of initialization parameters for the SerDe, in key-value form.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ser_<wbr>de_<wbr>info</td>
            <td class="align-top">
                
                <code><a href="#catalogtablestoragedescriptorserdeinfo">dict{catalog_<wbr>table_<wbr>storage_<wbr>descriptor_<wbr>ser_<wbr>de_<wbr>info}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Serialization/deserialization (SerDe) information.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">skewed_<wbr>info</td>
            <td class="align-top">
                
                <code><a href="#catalogtablestoragedescriptorskewedinfo">dict{catalog_<wbr>table_<wbr>storage_<wbr>descriptor_<wbr>skewed_<wbr>info}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Information about values that appear very frequently in a column (skewed values).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sort_<wbr>columns</td>
            <td class="align-top">
                
                <code><a href="#catalogtablestoragedescriptorsortcolumn">list[catalog_<wbr>table_<wbr>storage_<wbr>descriptor_<wbr>sort_<wbr>column]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of Order objects specifying the sort order of each bucket in the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stored_<wbr>as_<wbr>sub_<wbr>directories</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
True if the table data is stored in subdirectories, or False if not.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### CatalogTableStorageDescriptorColumn
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#CatalogTableStorageDescriptorColumn">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#CatalogTableStorageDescriptorColumn">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#CatalogTableStorageDescriptorColumnArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#CatalogTableStorageDescriptorColumnOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.CatalogTableStorageDescriptorColumnArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.CatalogTableStorageDescriptorColumn.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Comment</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Free-form text comment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Name of the SerDe.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The datatype of data in the Column.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Comment</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Free-form text comment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Name of the SerDe.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The datatype of data in the Column.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">comment</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Free-form text comment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Name of the SerDe.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The datatype of data in the Column.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">comment</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Free-form text comment.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Name of the SerDe.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The datatype of data in the Column.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### CatalogTableStorageDescriptorSerDeInfo
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#CatalogTableStorageDescriptorSerDeInfo">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#CatalogTableStorageDescriptorSerDeInfo">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#CatalogTableStorageDescriptorSerDeInfoArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#CatalogTableStorageDescriptorSerDeInfoOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.CatalogTableStorageDescriptorSerDeInfoArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.CatalogTableStorageDescriptorSerDeInfo.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the SerDe.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parameters</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of initialization parameters for the SerDe, in key-value form.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Serialization<wbr>Library</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Usually the class that implements the SerDe. An example is: org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the SerDe.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Parameters</td>
            <td class="align-top">
                
                <code>map[string]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of initialization parameters for the SerDe, in key-value form.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Serialization<wbr>Library</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Usually the class that implements the SerDe. An example is: org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the SerDe.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parameters</td>
            <td class="align-top">
                
                <code>{[key: string]: string}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of initialization parameters for the SerDe, in key-value form.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">serialization<wbr>Library</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Usually the class that implements the SerDe. An example is: org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Name of the SerDe.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">parameters</td>
            <td class="align-top">
                
                <code>dict{string}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of initialization parameters for the SerDe, in key-value form.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">serialization_<wbr>library</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Usually the class that implements the SerDe. An example is: org.apache.hadoop.hive.serde2.columnar.ColumnarSerDe.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### CatalogTableStorageDescriptorSkewedInfo
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#CatalogTableStorageDescriptorSkewedInfo">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#CatalogTableStorageDescriptorSkewedInfo">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#CatalogTableStorageDescriptorSkewedInfoArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#CatalogTableStorageDescriptorSkewedInfoOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.CatalogTableStorageDescriptorSkewedInfoArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.CatalogTableStorageDescriptorSkewedInfo.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Skewed<wbr>Column<wbr>Names</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of names of columns that contain skewed values.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Skewed<wbr>Column<wbr>Value<wbr>Location<wbr>Maps</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of values that appear so frequently as to be considered skewed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Skewed<wbr>Column<wbr>Values</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of skewed values to the columns that contain them.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Skewed<wbr>Column<wbr>Names</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of names of columns that contain skewed values.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Skewed<wbr>Column<wbr>Value<wbr>Location<wbr>Maps</td>
            <td class="align-top">
                
                <code>map[string]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of values that appear so frequently as to be considered skewed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Skewed<wbr>Column<wbr>Values</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of skewed values to the columns that contain them.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">skewed<wbr>Column<wbr>Names</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of names of columns that contain skewed values.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">skewed<wbr>Column<wbr>Value<wbr>Location<wbr>Maps</td>
            <td class="align-top">
                
                <code>{[key: string]: string}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of values that appear so frequently as to be considered skewed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">skewed<wbr>Column<wbr>Values</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of skewed values to the columns that contain them.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">skewed_<wbr>column_<wbr>names</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of names of columns that contain skewed values.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">skewed_<wbr>column_<wbr>value_<wbr>location_<wbr>maps</td>
            <td class="align-top">
                
                <code>dict{string}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of values that appear so frequently as to be considered skewed.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">skewed_<wbr>column_<wbr>values</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A mapping of skewed values to the columns that contain them.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### CatalogTableStorageDescriptorSortColumn
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#CatalogTableStorageDescriptorSortColumn">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#CatalogTableStorageDescriptorSortColumn">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#CatalogTableStorageDescriptorSortColumnArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#CatalogTableStorageDescriptorSortColumnOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.CatalogTableStorageDescriptorSortColumnArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.CatalogTableStorageDescriptorSortColumn.html">output</a> API doc for this type.
{{% /lang %}}



{{< langchoose csharp nojavascript >}}


{{% lang csharp %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Column</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the column.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sort<wbr>Order</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Indicates that the column is sorted in ascending order (== 1), or in descending order (==0).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang go %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">Column</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the column.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Sort<wbr>Order</td>
            <td class="align-top">
                
                <code>int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Indicates that the column is sorted in ascending order (== 1), or in descending order (==0).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang nodejs %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">column</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the column.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sort<wbr>Order</td>
            <td class="align-top">
                
                <code>number</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Indicates that the column is sorted in ascending order (== 1), or in descending order (==0).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}


{{% lang python %}}


<table class="ml-6">
    <thead>
        <tr>
            <th>Argument</th>
            <th>Type</th>
            <th>Description</th>
        </tr>
    </thead>
    <tbody>
    
        <tr>
            <td class="align-top">column</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the column.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">sort_<wbr>order</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Indicates that the column is sorted in ascending order (== 1), or in descending order (==0).
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







