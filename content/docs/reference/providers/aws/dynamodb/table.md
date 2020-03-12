
---
title: "Table"
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>


Provides a DynamoDB table resource

> **Note:** It is recommended to use `lifecycle` [`ignore_changes`](https://www.terraform.io/docs/configuration/resources.html#ignore_changes) for `read_capacity` and/or `write_capacity` if there's [autoscaling policy](https://www.terraform.io/docs/providers/aws/r/appautoscaling_policy.html) attached to the table.

## Example Usage

The following dynamodb table description models the table and GSI shown
in the [AWS SDK example documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GSI.html)

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const basic_dynamodb_table = new aws.dynamodb.Table("basic-dynamodb-table", {
    attributes: [
        {
            name: "UserId",
            type: "S",
        },
        {
            name: "GameTitle",
            type: "S",
        },
        {
            name: "TopScore",
            type: "N",
        },
    ],
    billingMode: "PROVISIONED",
    globalSecondaryIndexes: [{
        hashKey: "GameTitle",
        name: "GameTitleIndex",
        nonKeyAttributes: ["UserId"],
        projectionType: "INCLUDE",
        rangeKey: "TopScore",
        readCapacity: 10,
        writeCapacity: 10,
    }],
    hashKey: "UserId",
    rangeKey: "GameTitle",
    readCapacity: 20,
    tags: {
        Environment: "production",
        Name: "dynamodb-table-1",
    },
    ttl: {
        attributeName: "TimeToExist",
        enabled: false,
    },
    writeCapacity: 20,
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/dynamodb_table.html.markdown.



## Create a Table Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/dynamodb/#Table">Table</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/dynamodb/#TableArgs">TableArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

```python
def Table(resource_name, id, opts=None, attributes=None, billing_<wbr>mode=None, global_<wbr>secondary_<wbr>indexes=None, hash_<wbr>key=None, local_<wbr>secondary_<wbr>indexes=None, name=None, point_<wbr>in_<wbr>time_<wbr>recovery=None, range_<wbr>key=None, read_<wbr>capacity=None, server_<wbr>side_<wbr>encryption=None, stream_<wbr>enabled=None, stream_<wbr>view_<wbr>type=None, tags=None, ttl=None, write_<wbr>capacity=None, __props__=None)
```

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewTable<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/dynamodb?tab=doc#TableArgs">TableArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/dynamodb?tab=doc#Table">Table</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Dynamodb.Table.html">Table</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Dynamodb.TableArgs.html">TableArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a Table resource with the given unique name, arguments, and options.

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
            <td class="align-top">Attributes</td>
            <td class="align-top">
                
                <code><a href="#tableattribute">List&lt;Pulumi.<wbr>Aws.<wbr>Dynamodb.<wbr>Table<wbr>Attribute<wbr>Args&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
List of nested attribute definitions. Only required for `hash_key` and `range_key` attributes. Each attribute has two properties:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Billing<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Controls how you are charged for read and write throughput and how you manage capacity. The valid values are `PROVISIONED` and `PAY_PER_REQUEST`. Defaults to `PROVISIONED`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Global<wbr>Secondary<wbr>Indexes</td>
            <td class="align-top">
                
                <code><a href="#tableglobalsecondaryindex">List&lt;Pulumi.<wbr>Aws.<wbr>Dynamodb.<wbr>Table<wbr>Global<wbr>Secondary<wbr>Index<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Describe a GSI for the table;
subject to the normal limits on the number of GSIs, projected
attributes, etc.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hash<wbr>Key</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the hash key in the index; must be
defined as an attribute in the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Local<wbr>Secondary<wbr>Indexes</td>
            <td class="align-top">
                
                <code><a href="#tablelocalsecondaryindex">List&lt;Pulumi.<wbr>Aws.<wbr>Dynamodb.<wbr>Table<wbr>Local<wbr>Secondary<wbr>Index<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Describe an LSI on the table;
these can only be allocated *at creation* so you cannot change this
definition after you have created the resource.
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
The name of the index
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Point<wbr>In<wbr>Time<wbr>Recovery</td>
            <td class="align-top">
                
                <code><a href="#tablepointintimerecovery">Pulumi.<wbr>Aws.<wbr>Dynamodb.<wbr>Table<wbr>Point<wbr>In<wbr>Time<wbr>Recovery<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Point-in-time recovery options.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Range<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the range key; must be defined
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Read<wbr>Capacity</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of read units for this index. Must be set if billing_mode is set to PROVISIONED.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Server<wbr>Side<wbr>Encryption</td>
            <td class="align-top">
                
                <code><a href="#tableserversideencryption">Pulumi.<wbr>Aws.<wbr>Dynamodb.<wbr>Table<wbr>Server<wbr>Side<wbr>Encryption<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Encryption at rest options. AWS DynamoDB tables are automatically encrypted at rest with an AWS owned Customer Master Key if this argument isn&#39;t specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stream<wbr>Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether Streams are to be enabled (true) or disabled (false).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stream<wbr>View<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When an item in the table is modified, StreamViewType determines what information is written to the table&#39;s stream. Valid values are `KEYS_ONLY`, `NEW_IMAGE`, `OLD_IMAGE`, `NEW_AND_OLD_IMAGES`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of tags to populate on the created table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ttl</td>
            <td class="align-top">
                
                <code><a href="#tablettl">Pulumi.<wbr>Aws.<wbr>Dynamodb.<wbr>Table<wbr>Ttl<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defines ttl, has two properties, and can only be specified once:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Write<wbr>Capacity</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of write units for this index. Must be set if billing_mode is set to PROVISIONED.
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
            <td class="align-top">Attributes</td>
            <td class="align-top">
                
                <code><a href="#tableattribute">[]dynamodb.<wbr>Table<wbr>Attribute</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
List of nested attribute definitions. Only required for `hash_key` and `range_key` attributes. Each attribute has two properties:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Billing<wbr>Mode</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Controls how you are charged for read and write throughput and how you manage capacity. The valid values are `PROVISIONED` and `PAY_PER_REQUEST`. Defaults to `PROVISIONED`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Global<wbr>Secondary<wbr>Indexes</td>
            <td class="align-top">
                
                <code><a href="#tableglobalsecondaryindex">[]dynamodb.<wbr>Table<wbr>Global<wbr>Secondary<wbr>Index</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Describe a GSI for the table;
subject to the normal limits on the number of GSIs, projected
attributes, etc.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hash<wbr>Key</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the hash key in the index; must be
defined as an attribute in the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Local<wbr>Secondary<wbr>Indexes</td>
            <td class="align-top">
                
                <code><a href="#tablelocalsecondaryindex">[]dynamodb.<wbr>Table<wbr>Local<wbr>Secondary<wbr>Index</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Describe an LSI on the table;
these can only be allocated *at creation* so you cannot change this
definition after you have created the resource.
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
The name of the index
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Point<wbr>In<wbr>Time<wbr>Recovery</td>
            <td class="align-top">
                
                <code><a href="#tablepointintimerecovery">*dynamodb.<wbr>Table<wbr>Point<wbr>In<wbr>Time<wbr>Recovery</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Point-in-time recovery options.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Range<wbr>Key</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the range key; must be defined
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Read<wbr>Capacity</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of read units for this index. Must be set if billing_mode is set to PROVISIONED.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Server<wbr>Side<wbr>Encryption</td>
            <td class="align-top">
                
                <code><a href="#tableserversideencryption">*dynamodb.<wbr>Table<wbr>Server<wbr>Side<wbr>Encryption</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Encryption at rest options. AWS DynamoDB tables are automatically encrypted at rest with an AWS owned Customer Master Key if this argument isn&#39;t specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stream<wbr>Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether Streams are to be enabled (true) or disabled (false).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stream<wbr>View<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When an item in the table is modified, StreamViewType determines what information is written to the table&#39;s stream. Valid values are `KEYS_ONLY`, `NEW_IMAGE`, `OLD_IMAGE`, `NEW_AND_OLD_IMAGES`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of tags to populate on the created table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ttl</td>
            <td class="align-top">
                
                <code><a href="#tablettl">*dynamodb.<wbr>Table<wbr>Ttl</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defines ttl, has two properties, and can only be specified once:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Write<wbr>Capacity</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of write units for this index. Must be set if billing_mode is set to PROVISIONED.
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
            <td class="align-top">attributes</td>
            <td class="align-top">
                
                <code><a href="#tableattribute">dynamodb.<wbr>Table<wbr>Attribute[]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
List of nested attribute definitions. Only required for `hash_key` and `range_key` attributes. Each attribute has two properties:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">billing<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Controls how you are charged for read and write throughput and how you manage capacity. The valid values are `PROVISIONED` and `PAY_PER_REQUEST`. Defaults to `PROVISIONED`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">global<wbr>Secondary<wbr>Indexes</td>
            <td class="align-top">
                
                <code><a href="#tableglobalsecondaryindex">dynamodb.<wbr>Table<wbr>Global<wbr>Secondary<wbr>Index[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Describe a GSI for the table;
subject to the normal limits on the number of GSIs, projected
attributes, etc.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hash<wbr>Key</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the hash key in the index; must be
defined as an attribute in the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">local<wbr>Secondary<wbr>Indexes</td>
            <td class="align-top">
                
                <code><a href="#tablelocalsecondaryindex">dynamodb.<wbr>Table<wbr>Local<wbr>Secondary<wbr>Index[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Describe an LSI on the table;
these can only be allocated *at creation* so you cannot change this
definition after you have created the resource.
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
The name of the index
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">point<wbr>In<wbr>Time<wbr>Recovery</td>
            <td class="align-top">
                
                <code><a href="#tablepointintimerecovery">dynamodb.<wbr>Table<wbr>Point<wbr>In<wbr>Time<wbr>Recovery?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Point-in-time recovery options.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">range<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the range key; must be defined
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">read<wbr>Capacity</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of read units for this index. Must be set if billing_mode is set to PROVISIONED.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">server<wbr>Side<wbr>Encryption</td>
            <td class="align-top">
                
                <code><a href="#tableserversideencryption">dynamodb.<wbr>Table<wbr>Server<wbr>Side<wbr>Encryption?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Encryption at rest options. AWS DynamoDB tables are automatically encrypted at rest with an AWS owned Customer Master Key if this argument isn&#39;t specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stream<wbr>Enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether Streams are to be enabled (true) or disabled (false).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stream<wbr>View<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When an item in the table is modified, StreamViewType determines what information is written to the table&#39;s stream. Valid values are `KEYS_ONLY`, `NEW_IMAGE`, `OLD_IMAGE`, `NEW_AND_OLD_IMAGES`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of tags to populate on the created table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ttl</td>
            <td class="align-top">
                
                <code><a href="#tablettl">dynamodb.<wbr>Table<wbr>Ttl?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defines ttl, has two properties, and can only be specified once:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">write<wbr>Capacity</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of write units for this index. Must be set if billing_mode is set to PROVISIONED.
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
            <td class="align-top">attributes</td>
            <td class="align-top">
                
                <code><a href="#tableattribute">list[table_<wbr>attribute]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
List of nested attribute definitions. Only required for `hash_key` and `range_key` attributes. Each attribute has two properties:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">billing_<wbr>mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Controls how you are charged for read and write throughput and how you manage capacity. The valid values are `PROVISIONED` and `PAY_PER_REQUEST`. Defaults to `PROVISIONED`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">global_<wbr>secondary_<wbr>indexes</td>
            <td class="align-top">
                
                <code><a href="#tableglobalsecondaryindex">list[table_<wbr>global_<wbr>secondary_<wbr>index]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Describe a GSI for the table;
subject to the normal limits on the number of GSIs, projected
attributes, etc.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hash_<wbr>key</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the hash key in the index; must be
defined as an attribute in the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">local_<wbr>secondary_<wbr>indexes</td>
            <td class="align-top">
                
                <code><a href="#tablelocalsecondaryindex">list[table_<wbr>local_<wbr>secondary_<wbr>index]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Describe an LSI on the table;
these can only be allocated *at creation* so you cannot change this
definition after you have created the resource.
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
The name of the index
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">point_<wbr>in_<wbr>time_<wbr>recovery</td>
            <td class="align-top">
                
                <code><a href="#tablepointintimerecovery">dict{table_<wbr>point_<wbr>in_<wbr>time_<wbr>recovery}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Point-in-time recovery options.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">range_<wbr>key</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the range key; must be defined
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">read_<wbr>capacity</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of read units for this index. Must be set if billing_mode is set to PROVISIONED.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">server_<wbr>side_<wbr>encryption</td>
            <td class="align-top">
                
                <code><a href="#tableserversideencryption">dict{table_<wbr>server_<wbr>side_<wbr>encryption}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Encryption at rest options. AWS DynamoDB tables are automatically encrypted at rest with an AWS owned Customer Master Key if this argument isn&#39;t specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stream_<wbr>enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether Streams are to be enabled (true) or disabled (false).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stream_<wbr>view_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When an item in the table is modified, StreamViewType determines what information is written to the table&#39;s stream. Valid values are `KEYS_ONLY`, `NEW_IMAGE`, `OLD_IMAGE`, `NEW_AND_OLD_IMAGES`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>dict{any}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of tags to populate on the created table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ttl</td>
            <td class="align-top">
                
                <code><a href="#tablettl">dict{table_<wbr>ttl}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defines ttl, has two properties, and can only be specified once:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">write_<wbr>capacity</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of write units for this index. Must be set if billing_mode is set to PROVISIONED.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## Table Output Properties

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
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The arn of the table
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Attributes</td>
            <td class="align-top">
                
                <code><a href="#tableattribute">List&lt;Pulumi.<wbr>Aws.<wbr>Dynamodb.<wbr>Table<wbr>Attribute&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} List of nested attribute definitions. Only required for `hash_key` and `range_key` attributes. Each attribute has two properties:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Billing<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Controls how you are charged for read and write throughput and how you manage capacity. The valid values are `PROVISIONED` and `PAY_PER_REQUEST`. Defaults to `PROVISIONED`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Global<wbr>Secondary<wbr>Indexes</td>
            <td class="align-top">
                
                <code><a href="#tableglobalsecondaryindex">List&lt;Pulumi.<wbr>Aws.<wbr>Dynamodb.<wbr>Table<wbr>Global<wbr>Secondary<wbr>Index&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} Describe a GSI for the table;
subject to the normal limits on the number of GSIs, projected
attributes, etc.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hash<wbr>Key</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the hash key in the index; must be
defined as an attribute in the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Local<wbr>Secondary<wbr>Indexes</td>
            <td class="align-top">
                
                <code><a href="#tablelocalsecondaryindex">List&lt;Pulumi.<wbr>Aws.<wbr>Dynamodb.<wbr>Table<wbr>Local<wbr>Secondary<wbr>Index&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} Describe an LSI on the table;
these can only be allocated *at creation* so you cannot change this
definition after you have created the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the index
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Point<wbr>In<wbr>Time<wbr>Recovery</td>
            <td class="align-top">
                
                <code><a href="#tablepointintimerecovery">Pulumi.<wbr>Aws.<wbr>Dynamodb.<wbr>Table<wbr>Point<wbr>In<wbr>Time<wbr>Recovery</a></code>
            </td>
            <td class="align-top">{{% md %}} Point-in-time recovery options.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Range<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The name of the range key; must be defined
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Read<wbr>Capacity</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} The number of read units for this index. Must be set if billing_mode is set to PROVISIONED.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Server<wbr>Side<wbr>Encryption</td>
            <td class="align-top">
                
                <code><a href="#tableserversideencryption">Pulumi.<wbr>Aws.<wbr>Dynamodb.<wbr>Table<wbr>Server<wbr>Side<wbr>Encryption</a></code>
            </td>
            <td class="align-top">{{% md %}} Encryption at rest options. AWS DynamoDB tables are automatically encrypted at rest with an AWS owned Customer Master Key if this argument isn&#39;t specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stream<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the Table Stream. Only available when `stream_enabled = true`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stream<wbr>Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} Indicates whether Streams are to be enabled (true) or disabled (false).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stream<wbr>Label</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A timestamp, in ISO 8601 format, for this stream. Note that this timestamp is not
a unique identifier for the stream on its own. However, the combination of AWS customer ID,
table name and this field is guaranteed to be unique.
It can be used for creating CloudWatch Alarms. Only available when `stream_enabled = true`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stream<wbr>View<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} When an item in the table is modified, StreamViewType determines what information is written to the table&#39;s stream. Valid values are `KEYS_ONLY`, `NEW_IMAGE`, `OLD_IMAGE`, `NEW_AND_OLD_IMAGES`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A map of tags to populate on the created table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ttl</td>
            <td class="align-top">
                
                <code><a href="#tablettl">Pulumi.<wbr>Aws.<wbr>Dynamodb.<wbr>Table<wbr>Ttl?</a></code>
            </td>
            <td class="align-top">{{% md %}} Defines ttl, has two properties, and can only be specified once:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Write<wbr>Capacity</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} The number of write units for this index. Must be set if billing_mode is set to PROVISIONED.
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
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The arn of the table
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Attributes</td>
            <td class="align-top">
                
                <code><a href="#tableattribute">[]dynamodb.<wbr>Table<wbr>Attribute</a></code>
            </td>
            <td class="align-top">{{% md %}} List of nested attribute definitions. Only required for `hash_key` and `range_key` attributes. Each attribute has two properties:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Billing<wbr>Mode</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Controls how you are charged for read and write throughput and how you manage capacity. The valid values are `PROVISIONED` and `PAY_PER_REQUEST`. Defaults to `PROVISIONED`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Global<wbr>Secondary<wbr>Indexes</td>
            <td class="align-top">
                
                <code><a href="#tableglobalsecondaryindex">[]dynamodb.<wbr>Table<wbr>Global<wbr>Secondary<wbr>Index</a></code>
            </td>
            <td class="align-top">{{% md %}} Describe a GSI for the table;
subject to the normal limits on the number of GSIs, projected
attributes, etc.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hash<wbr>Key</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the hash key in the index; must be
defined as an attribute in the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Local<wbr>Secondary<wbr>Indexes</td>
            <td class="align-top">
                
                <code><a href="#tablelocalsecondaryindex">[]dynamodb.<wbr>Table<wbr>Local<wbr>Secondary<wbr>Index</a></code>
            </td>
            <td class="align-top">{{% md %}} Describe an LSI on the table;
these can only be allocated *at creation* so you cannot change this
definition after you have created the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the index
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Point<wbr>In<wbr>Time<wbr>Recovery</td>
            <td class="align-top">
                
                <code><a href="#tablepointintimerecovery">dynamodb.<wbr>Table<wbr>Point<wbr>In<wbr>Time<wbr>Recovery</a></code>
            </td>
            <td class="align-top">{{% md %}} Point-in-time recovery options.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Range<wbr>Key</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the range key; must be defined
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Read<wbr>Capacity</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} The number of read units for this index. Must be set if billing_mode is set to PROVISIONED.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Server<wbr>Side<wbr>Encryption</td>
            <td class="align-top">
                
                <code><a href="#tableserversideencryption">dynamodb.<wbr>Table<wbr>Server<wbr>Side<wbr>Encryption</a></code>
            </td>
            <td class="align-top">{{% md %}} Encryption at rest options. AWS DynamoDB tables are automatically encrypted at rest with an AWS owned Customer Master Key if this argument isn&#39;t specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stream<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the Table Stream. Only available when `stream_enabled = true`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stream<wbr>Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} Indicates whether Streams are to be enabled (true) or disabled (false).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stream<wbr>Label</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A timestamp, in ISO 8601 format, for this stream. Note that this timestamp is not
a unique identifier for the stream on its own. However, the combination of AWS customer ID,
table name and this field is guaranteed to be unique.
It can be used for creating CloudWatch Alarms. Only available when `stream_enabled = true`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stream<wbr>View<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} When an item in the table is modified, StreamViewType determines what information is written to the table&#39;s stream. Valid values are `KEYS_ONLY`, `NEW_IMAGE`, `OLD_IMAGE`, `NEW_AND_OLD_IMAGES`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} A map of tags to populate on the created table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ttl</td>
            <td class="align-top">
                
                <code><a href="#tablettl">*dynamodb.<wbr>Table<wbr>Ttl</a></code>
            </td>
            <td class="align-top">{{% md %}} Defines ttl, has two properties, and can only be specified once:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Write<wbr>Capacity</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} The number of write units for this index. Must be set if billing_mode is set to PROVISIONED.
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
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The arn of the table
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">attributes</td>
            <td class="align-top">
                
                <code><a href="#tableattribute">dynamodb.<wbr>Table<wbr>Attribute[]</a></code>
            </td>
            <td class="align-top">{{% md %}} List of nested attribute definitions. Only required for `hash_key` and `range_key` attributes. Each attribute has two properties:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">billing<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Controls how you are charged for read and write throughput and how you manage capacity. The valid values are `PROVISIONED` and `PAY_PER_REQUEST`. Defaults to `PROVISIONED`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">global<wbr>Secondary<wbr>Indexes</td>
            <td class="align-top">
                
                <code><a href="#tableglobalsecondaryindex">dynamodb.<wbr>Table<wbr>Global<wbr>Secondary<wbr>Index[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} Describe a GSI for the table;
subject to the normal limits on the number of GSIs, projected
attributes, etc.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hash<wbr>Key</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the hash key in the index; must be
defined as an attribute in the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">local<wbr>Secondary<wbr>Indexes</td>
            <td class="align-top">
                
                <code><a href="#tablelocalsecondaryindex">dynamodb.<wbr>Table<wbr>Local<wbr>Secondary<wbr>Index[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} Describe an LSI on the table;
these can only be allocated *at creation* so you cannot change this
definition after you have created the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the index
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">point<wbr>In<wbr>Time<wbr>Recovery</td>
            <td class="align-top">
                
                <code><a href="#tablepointintimerecovery">dynamodb.<wbr>Table<wbr>Point<wbr>In<wbr>Time<wbr>Recovery</a></code>
            </td>
            <td class="align-top">{{% md %}} Point-in-time recovery options.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">range<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The name of the range key; must be defined
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">read<wbr>Capacity</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} The number of read units for this index. Must be set if billing_mode is set to PROVISIONED.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">server<wbr>Side<wbr>Encryption</td>
            <td class="align-top">
                
                <code><a href="#tableserversideencryption">dynamodb.<wbr>Table<wbr>Server<wbr>Side<wbr>Encryption</a></code>
            </td>
            <td class="align-top">{{% md %}} Encryption at rest options. AWS DynamoDB tables are automatically encrypted at rest with an AWS owned Customer Master Key if this argument isn&#39;t specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stream<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the Table Stream. Only available when `stream_enabled = true`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stream<wbr>Enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} Indicates whether Streams are to be enabled (true) or disabled (false).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stream<wbr>Label</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A timestamp, in ISO 8601 format, for this stream. Note that this timestamp is not
a unique identifier for the stream on its own. However, the combination of AWS customer ID,
table name and this field is guaranteed to be unique.
It can be used for creating CloudWatch Alarms. Only available when `stream_enabled = true`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stream<wbr>View<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} When an item in the table is modified, StreamViewType determines what information is written to the table&#39;s stream. Valid values are `KEYS_ONLY`, `NEW_IMAGE`, `OLD_IMAGE`, `NEW_AND_OLD_IMAGES`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} A map of tags to populate on the created table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ttl</td>
            <td class="align-top">
                
                <code><a href="#tablettl">dynamodb.<wbr>Table<wbr>Ttl?</a></code>
            </td>
            <td class="align-top">{{% md %}} Defines ttl, has two properties, and can only be specified once:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">write<wbr>Capacity</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} The number of write units for this index. Must be set if billing_mode is set to PROVISIONED.
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
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The arn of the table
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">attributes</td>
            <td class="align-top">
                
                <code><a href="#tableattribute">list[table_<wbr>attribute]</a></code>
            </td>
            <td class="align-top">{{% md %}} List of nested attribute definitions. Only required for `hash_key` and `range_key` attributes. Each attribute has two properties:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">billing_<wbr>mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Controls how you are charged for read and write throughput and how you manage capacity. The valid values are `PROVISIONED` and `PAY_PER_REQUEST`. Defaults to `PROVISIONED`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">global_<wbr>secondary_<wbr>indexes</td>
            <td class="align-top">
                
                <code><a href="#tableglobalsecondaryindex">list[table_<wbr>global_<wbr>secondary_<wbr>index]</a></code>
            </td>
            <td class="align-top">{{% md %}} Describe a GSI for the table;
subject to the normal limits on the number of GSIs, projected
attributes, etc.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hash_<wbr>key</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the hash key in the index; must be
defined as an attribute in the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">local_<wbr>secondary_<wbr>indexes</td>
            <td class="align-top">
                
                <code><a href="#tablelocalsecondaryindex">list[table_<wbr>local_<wbr>secondary_<wbr>index]</a></code>
            </td>
            <td class="align-top">{{% md %}} Describe an LSI on the table;
these can only be allocated *at creation* so you cannot change this
definition after you have created the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the index
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">point_<wbr>in_<wbr>time_<wbr>recovery</td>
            <td class="align-top">
                
                <code><a href="#tablepointintimerecovery">dict{table_<wbr>point_<wbr>in_<wbr>time_<wbr>recovery}</a></code>
            </td>
            <td class="align-top">{{% md %}} Point-in-time recovery options.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">range_<wbr>key</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the range key; must be defined
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">read_<wbr>capacity</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The number of read units for this index. Must be set if billing_mode is set to PROVISIONED.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">server_<wbr>side_<wbr>encryption</td>
            <td class="align-top">
                
                <code><a href="#tableserversideencryption">dict{table_<wbr>server_<wbr>side_<wbr>encryption}</a></code>
            </td>
            <td class="align-top">{{% md %}} Encryption at rest options. AWS DynamoDB tables are automatically encrypted at rest with an AWS owned Customer Master Key if this argument isn&#39;t specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stream_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ARN of the Table Stream. Only available when `stream_enabled = true`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stream_<wbr>enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} Indicates whether Streams are to be enabled (true) or disabled (false).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stream_<wbr>label</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A timestamp, in ISO 8601 format, for this stream. Note that this timestamp is not
a unique identifier for the stream on its own. However, the combination of AWS customer ID,
table name and this field is guaranteed to be unique.
It can be used for creating CloudWatch Alarms. Only available when `stream_enabled = true`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stream_<wbr>view_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} When an item in the table is modified, StreamViewType determines what information is written to the table&#39;s stream. Valid values are `KEYS_ONLY`, `NEW_IMAGE`, `OLD_IMAGE`, `NEW_AND_OLD_IMAGES`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>dict{any}</code>
            </td>
            <td class="align-top">{{% md %}} A map of tags to populate on the created table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ttl</td>
            <td class="align-top">
                
                <code><a href="#tablettl">dict{table_<wbr>ttl}</a></code>
            </td>
            <td class="align-top">{{% md %}} Defines ttl, has two properties, and can only be specified once:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">write_<wbr>capacity</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} The number of write units for this index. Must be set if billing_mode is set to PROVISIONED.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing Table Resource

{{< langchoose csharp nojavascript >}}

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TableState, opts?: pulumi.CustomResourceOptions): Table;
```

```python
def get(resource_name, id, opts=None, arn=None, attributes=None, billing_<wbr>mode=None, global_<wbr>secondary_<wbr>indexes=None, hash_<wbr>key=None, local_<wbr>secondary_<wbr>indexes=None, name=None, point_<wbr>in_<wbr>time_<wbr>recovery=None, range_<wbr>key=None, read_<wbr>capacity=None, server_<wbr>side_<wbr>encryption=None, stream_<wbr>arn=None, stream_<wbr>enabled=None, stream_<wbr>label=None, stream_<wbr>view_<wbr>type=None, tags=None, ttl=None, write_<wbr>capacity=None)
```

```go
func GetTable(ctx *pulumi.Context, name string, id pulumi.IDInput, state *TableState, opts ...pulumi.ResourceOption) (*Bucket, error)
```

```csharp
public static Table Get(string name, Input<string> id, TableState? state = null, CustomResourceOptions? options = null);
```

Get an existing Table resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The arn of the table
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Attributes</td>
            <td class="align-top">
                
                <code><a href="#tableattribute">List&lt;Pulumi.<wbr>Aws.<wbr>Dynamodb.<wbr>Table<wbr>Attribute<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of nested attribute definitions. Only required for `hash_key` and `range_key` attributes. Each attribute has two properties:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Billing<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Controls how you are charged for read and write throughput and how you manage capacity. The valid values are `PROVISIONED` and `PAY_PER_REQUEST`. Defaults to `PROVISIONED`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Global<wbr>Secondary<wbr>Indexes</td>
            <td class="align-top">
                
                <code><a href="#tableglobalsecondaryindex">List&lt;Pulumi.<wbr>Aws.<wbr>Dynamodb.<wbr>Table<wbr>Global<wbr>Secondary<wbr>Index<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Describe a GSI for the table;
subject to the normal limits on the number of GSIs, projected
attributes, etc.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hash<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the hash key in the index; must be
defined as an attribute in the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Local<wbr>Secondary<wbr>Indexes</td>
            <td class="align-top">
                
                <code><a href="#tablelocalsecondaryindex">List&lt;Pulumi.<wbr>Aws.<wbr>Dynamodb.<wbr>Table<wbr>Local<wbr>Secondary<wbr>Index<wbr>Args&gt;?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Describe an LSI on the table;
these can only be allocated *at creation* so you cannot change this
definition after you have created the resource.
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
The name of the index
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Point<wbr>In<wbr>Time<wbr>Recovery</td>
            <td class="align-top">
                
                <code><a href="#tablepointintimerecovery">Pulumi.<wbr>Aws.<wbr>Dynamodb.<wbr>Table<wbr>Point<wbr>In<wbr>Time<wbr>Recovery<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Point-in-time recovery options.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Range<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the range key; must be defined
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Read<wbr>Capacity</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of read units for this index. Must be set if billing_mode is set to PROVISIONED.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Server<wbr>Side<wbr>Encryption</td>
            <td class="align-top">
                
                <code><a href="#tableserversideencryption">Pulumi.<wbr>Aws.<wbr>Dynamodb.<wbr>Table<wbr>Server<wbr>Side<wbr>Encryption<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Encryption at rest options. AWS DynamoDB tables are automatically encrypted at rest with an AWS owned Customer Master Key if this argument isn&#39;t specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stream<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the Table Stream. Only available when `stream_enabled = true`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stream<wbr>Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether Streams are to be enabled (true) or disabled (false).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stream<wbr>Label</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A timestamp, in ISO 8601 format, for this stream. Note that this timestamp is not
a unique identifier for the stream on its own. However, the combination of AWS customer ID,
table name and this field is guaranteed to be unique.
It can be used for creating CloudWatch Alarms. Only available when `stream_enabled = true`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stream<wbr>View<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When an item in the table is modified, StreamViewType determines what information is written to the table&#39;s stream. Valid values are `KEYS_ONLY`, `NEW_IMAGE`, `OLD_IMAGE`, `NEW_AND_OLD_IMAGES`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of tags to populate on the created table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ttl</td>
            <td class="align-top">
                
                <code><a href="#tablettl">Pulumi.<wbr>Aws.<wbr>Dynamodb.<wbr>Table<wbr>Ttl<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defines ttl, has two properties, and can only be specified once:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Write<wbr>Capacity</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of write units for this index. Must be set if billing_mode is set to PROVISIONED.
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
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The arn of the table
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Attributes</td>
            <td class="align-top">
                
                <code><a href="#tableattribute">[]dynamodb.<wbr>Table<wbr>Attribute</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of nested attribute definitions. Only required for `hash_key` and `range_key` attributes. Each attribute has two properties:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Billing<wbr>Mode</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Controls how you are charged for read and write throughput and how you manage capacity. The valid values are `PROVISIONED` and `PAY_PER_REQUEST`. Defaults to `PROVISIONED`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Global<wbr>Secondary<wbr>Indexes</td>
            <td class="align-top">
                
                <code><a href="#tableglobalsecondaryindex">[]dynamodb.<wbr>Table<wbr>Global<wbr>Secondary<wbr>Index</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Describe a GSI for the table;
subject to the normal limits on the number of GSIs, projected
attributes, etc.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Hash<wbr>Key</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the hash key in the index; must be
defined as an attribute in the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Local<wbr>Secondary<wbr>Indexes</td>
            <td class="align-top">
                
                <code><a href="#tablelocalsecondaryindex">[]dynamodb.<wbr>Table<wbr>Local<wbr>Secondary<wbr>Index</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Describe an LSI on the table;
these can only be allocated *at creation* so you cannot change this
definition after you have created the resource.
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
The name of the index
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Point<wbr>In<wbr>Time<wbr>Recovery</td>
            <td class="align-top">
                
                <code><a href="#tablepointintimerecovery">*dynamodb.<wbr>Table<wbr>Point<wbr>In<wbr>Time<wbr>Recovery</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Point-in-time recovery options.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Range<wbr>Key</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the range key; must be defined
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Read<wbr>Capacity</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of read units for this index. Must be set if billing_mode is set to PROVISIONED.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Server<wbr>Side<wbr>Encryption</td>
            <td class="align-top">
                
                <code><a href="#tableserversideencryption">*dynamodb.<wbr>Table<wbr>Server<wbr>Side<wbr>Encryption</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Encryption at rest options. AWS DynamoDB tables are automatically encrypted at rest with an AWS owned Customer Master Key if this argument isn&#39;t specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stream<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the Table Stream. Only available when `stream_enabled = true`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stream<wbr>Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether Streams are to be enabled (true) or disabled (false).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stream<wbr>Label</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A timestamp, in ISO 8601 format, for this stream. Note that this timestamp is not
a unique identifier for the stream on its own. However, the combination of AWS customer ID,
table name and this field is guaranteed to be unique.
It can be used for creating CloudWatch Alarms. Only available when `stream_enabled = true`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Stream<wbr>View<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When an item in the table is modified, StreamViewType determines what information is written to the table&#39;s stream. Valid values are `KEYS_ONLY`, `NEW_IMAGE`, `OLD_IMAGE`, `NEW_AND_OLD_IMAGES`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Tags</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of tags to populate on the created table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Ttl</td>
            <td class="align-top">
                
                <code><a href="#tablettl">*dynamodb.<wbr>Table<wbr>Ttl</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defines ttl, has two properties, and can only be specified once:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Write<wbr>Capacity</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of write units for this index. Must be set if billing_mode is set to PROVISIONED.
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
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The arn of the table
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">attributes</td>
            <td class="align-top">
                
                <code><a href="#tableattribute">dynamodb.<wbr>Table<wbr>Attribute[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of nested attribute definitions. Only required for `hash_key` and `range_key` attributes. Each attribute has two properties:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">billing<wbr>Mode</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Controls how you are charged for read and write throughput and how you manage capacity. The valid values are `PROVISIONED` and `PAY_PER_REQUEST`. Defaults to `PROVISIONED`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">global<wbr>Secondary<wbr>Indexes</td>
            <td class="align-top">
                
                <code><a href="#tableglobalsecondaryindex">dynamodb.<wbr>Table<wbr>Global<wbr>Secondary<wbr>Index[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Describe a GSI for the table;
subject to the normal limits on the number of GSIs, projected
attributes, etc.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hash<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the hash key in the index; must be
defined as an attribute in the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">local<wbr>Secondary<wbr>Indexes</td>
            <td class="align-top">
                
                <code><a href="#tablelocalsecondaryindex">dynamodb.<wbr>Table<wbr>Local<wbr>Secondary<wbr>Index[]?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Describe an LSI on the table;
these can only be allocated *at creation* so you cannot change this
definition after you have created the resource.
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
The name of the index
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">point<wbr>In<wbr>Time<wbr>Recovery</td>
            <td class="align-top">
                
                <code><a href="#tablepointintimerecovery">dynamodb.<wbr>Table<wbr>Point<wbr>In<wbr>Time<wbr>Recovery?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Point-in-time recovery options.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">range<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the range key; must be defined
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">read<wbr>Capacity</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of read units for this index. Must be set if billing_mode is set to PROVISIONED.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">server<wbr>Side<wbr>Encryption</td>
            <td class="align-top">
                
                <code><a href="#tableserversideencryption">dynamodb.<wbr>Table<wbr>Server<wbr>Side<wbr>Encryption?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Encryption at rest options. AWS DynamoDB tables are automatically encrypted at rest with an AWS owned Customer Master Key if this argument isn&#39;t specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stream<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the Table Stream. Only available when `stream_enabled = true`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stream<wbr>Enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether Streams are to be enabled (true) or disabled (false).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stream<wbr>Label</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A timestamp, in ISO 8601 format, for this stream. Note that this timestamp is not
a unique identifier for the stream on its own. However, the combination of AWS customer ID,
table name and this field is guaranteed to be unique.
It can be used for creating CloudWatch Alarms. Only available when `stream_enabled = true`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stream<wbr>View<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When an item in the table is modified, StreamViewType determines what information is written to the table&#39;s stream. Valid values are `KEYS_ONLY`, `NEW_IMAGE`, `OLD_IMAGE`, `NEW_AND_OLD_IMAGES`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of tags to populate on the created table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ttl</td>
            <td class="align-top">
                
                <code><a href="#tablettl">dynamodb.<wbr>Table<wbr>Ttl?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defines ttl, has two properties, and can only be specified once:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">write<wbr>Capacity</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of write units for this index. Must be set if billing_mode is set to PROVISIONED.
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
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The arn of the table
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">attributes</td>
            <td class="align-top">
                
                <code><a href="#tableattribute">list[table_<wbr>attribute]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
List of nested attribute definitions. Only required for `hash_key` and `range_key` attributes. Each attribute has two properties:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">billing_<wbr>mode</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Controls how you are charged for read and write throughput and how you manage capacity. The valid values are `PROVISIONED` and `PAY_PER_REQUEST`. Defaults to `PROVISIONED`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">global_<wbr>secondary_<wbr>indexes</td>
            <td class="align-top">
                
                <code><a href="#tableglobalsecondaryindex">list[table_<wbr>global_<wbr>secondary_<wbr>index]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Describe a GSI for the table;
subject to the normal limits on the number of GSIs, projected
attributes, etc.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">hash_<wbr>key</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the hash key in the index; must be
defined as an attribute in the resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">local_<wbr>secondary_<wbr>indexes</td>
            <td class="align-top">
                
                <code><a href="#tablelocalsecondaryindex">list[table_<wbr>local_<wbr>secondary_<wbr>index]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Describe an LSI on the table;
these can only be allocated *at creation* so you cannot change this
definition after you have created the resource.
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
The name of the index
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">point_<wbr>in_<wbr>time_<wbr>recovery</td>
            <td class="align-top">
                
                <code><a href="#tablepointintimerecovery">dict{table_<wbr>point_<wbr>in_<wbr>time_<wbr>recovery}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Point-in-time recovery options.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">range_<wbr>key</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the range key; must be defined
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">read_<wbr>capacity</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of read units for this index. Must be set if billing_mode is set to PROVISIONED.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">server_<wbr>side_<wbr>encryption</td>
            <td class="align-top">
                
                <code><a href="#tableserversideencryption">dict{table_<wbr>server_<wbr>side_<wbr>encryption}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Encryption at rest options. AWS DynamoDB tables are automatically encrypted at rest with an AWS owned Customer Master Key if this argument isn&#39;t specified.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stream_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the Table Stream. Only available when `stream_enabled = true`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stream_<wbr>enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Indicates whether Streams are to be enabled (true) or disabled (false).
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stream_<wbr>label</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A timestamp, in ISO 8601 format, for this stream. Note that this timestamp is not
a unique identifier for the stream on its own. However, the combination of AWS customer ID,
table name and this field is guaranteed to be unique.
It can be used for creating CloudWatch Alarms. Only available when `stream_enabled = true`
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">stream_<wbr>view_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
When an item in the table is modified, StreamViewType determines what information is written to the table&#39;s stream. Valid values are `KEYS_ONLY`, `NEW_IMAGE`, `OLD_IMAGE`, `NEW_AND_OLD_IMAGES`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">tags</td>
            <td class="align-top">
                
                <code>dict{any}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of tags to populate on the created table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">ttl</td>
            <td class="align-top">
                
                <code><a href="#tablettl">dict{table_<wbr>ttl}</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Defines ttl, has two properties, and can only be specified once:
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">write_<wbr>capacity</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of write units for this index. Must be set if billing_mode is set to PROVISIONED.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### TableAttribute
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#TableAttribute">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#TableAttribute">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/dynamodb?tab=doc#TableAttributeArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/dynamodb?tab=doc#TableAttributeOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Dynamodb.TableAttributeArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Dynamodb.TableAttribute.html">output</a> API doc for this type.
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
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the index
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Attribute type, which must be a scalar type: `S`, `N`, or `B` for (S)tring, (N)umber or (B)inary data
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
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the index
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Attribute type, which must be a scalar type: `S`, `N`, or `B` for (S)tring, (N)umber or (B)inary data
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
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the index
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Attribute type, which must be a scalar type: `S`, `N`, or `B` for (S)tring, (N)umber or (B)inary data
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
 (Required)
The name of the index
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Attribute type, which must be a scalar type: `S`, `N`, or `B` for (S)tring, (N)umber or (B)inary data
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### TableGlobalSecondaryIndex
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#TableGlobalSecondaryIndex">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#TableGlobalSecondaryIndex">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/dynamodb?tab=doc#TableGlobalSecondaryIndexArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/dynamodb?tab=doc#TableGlobalSecondaryIndexOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Dynamodb.TableGlobalSecondaryIndexArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Dynamodb.TableGlobalSecondaryIndex.html">output</a> API doc for this type.
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
            <td class="align-top">Hash<wbr>Key</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the hash key in the index; must be
defined as an attribute in the resource.
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
The name of the index
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Non<wbr>Key<wbr>Attributes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Only required with `INCLUDE` as a
projection type; a list of attributes to project into the index. These
do not need to be defined as attributes on the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Projection<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
One of `ALL`, `INCLUDE` or `KEYS_ONLY`
where `ALL` projects every attribute into the index, `KEYS_ONLY`
projects just the hash and range key into the index, and `INCLUDE`
projects only the keys specified in the _non_key_attributes_
parameter.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Range<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the range key; must be defined
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Read<wbr>Capacity</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of read units for this index. Must be set if billing_mode is set to PROVISIONED.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Write<wbr>Capacity</td>
            <td class="align-top">
                
                <code>int?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of write units for this index. Must be set if billing_mode is set to PROVISIONED.
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
            <td class="align-top">Hash<wbr>Key</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the hash key in the index; must be
defined as an attribute in the resource.
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
The name of the index
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Non<wbr>Key<wbr>Attributes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Only required with `INCLUDE` as a
projection type; a list of attributes to project into the index. These
do not need to be defined as attributes on the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Projection<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
One of `ALL`, `INCLUDE` or `KEYS_ONLY`
where `ALL` projects every attribute into the index, `KEYS_ONLY`
projects just the hash and range key into the index, and `INCLUDE`
projects only the keys specified in the _non_key_attributes_
parameter.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Range<wbr>Key</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the range key; must be defined
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Read<wbr>Capacity</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of read units for this index. Must be set if billing_mode is set to PROVISIONED.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Write<wbr>Capacity</td>
            <td class="align-top">
                
                <code>*int</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of write units for this index. Must be set if billing_mode is set to PROVISIONED.
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
            <td class="align-top">hash<wbr>Key</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the hash key in the index; must be
defined as an attribute in the resource.
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
The name of the index
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">non<wbr>Key<wbr>Attributes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Only required with `INCLUDE` as a
projection type; a list of attributes to project into the index. These
do not need to be defined as attributes on the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">projection<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
One of `ALL`, `INCLUDE` or `KEYS_ONLY`
where `ALL` projects every attribute into the index, `KEYS_ONLY`
projects just the hash and range key into the index, and `INCLUDE`
projects only the keys specified in the _non_key_attributes_
parameter.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">range<wbr>Key</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the range key; must be defined
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">read<wbr>Capacity</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of read units for this index. Must be set if billing_mode is set to PROVISIONED.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">write<wbr>Capacity</td>
            <td class="align-top">
                
                <code>number?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of write units for this index. Must be set if billing_mode is set to PROVISIONED.
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
            <td class="align-top">hash_<wbr>key</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the hash key in the index; must be
defined as an attribute in the resource.
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
The name of the index
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">non_<wbr>key_<wbr>attributes</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Only required with `INCLUDE` as a
projection type; a list of attributes to project into the index. These
do not need to be defined as attributes on the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">projection_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
One of `ALL`, `INCLUDE` or `KEYS_ONLY`
where `ALL` projects every attribute into the index, `KEYS_ONLY`
projects just the hash and range key into the index, and `INCLUDE`
projects only the keys specified in the _non_key_attributes_
parameter.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">range_<wbr>key</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The name of the range key; must be defined
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">read_<wbr>capacity</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of read units for this index. Must be set if billing_mode is set to PROVISIONED.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">write_<wbr>capacity</td>
            <td class="align-top">
                
                <code>float</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The number of write units for this index. Must be set if billing_mode is set to PROVISIONED.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### TableLocalSecondaryIndex
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#TableLocalSecondaryIndex">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#TableLocalSecondaryIndex">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/dynamodb?tab=doc#TableLocalSecondaryIndexArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/dynamodb?tab=doc#TableLocalSecondaryIndexOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Dynamodb.TableLocalSecondaryIndexArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Dynamodb.TableLocalSecondaryIndex.html">output</a> API doc for this type.
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
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the index
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Non<wbr>Key<wbr>Attributes</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Only required with `INCLUDE` as a
projection type; a list of attributes to project into the index. These
do not need to be defined as attributes on the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Projection<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
One of `ALL`, `INCLUDE` or `KEYS_ONLY`
where `ALL` projects every attribute into the index, `KEYS_ONLY`
projects just the hash and range key into the index, and `INCLUDE`
projects only the keys specified in the _non_key_attributes_
parameter.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Range<wbr>Key</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the range key; must be defined
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
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the index
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Non<wbr>Key<wbr>Attributes</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Only required with `INCLUDE` as a
projection type; a list of attributes to project into the index. These
do not need to be defined as attributes on the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Projection<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
One of `ALL`, `INCLUDE` or `KEYS_ONLY`
where `ALL` projects every attribute into the index, `KEYS_ONLY`
projects just the hash and range key into the index, and `INCLUDE`
projects only the keys specified in the _non_key_attributes_
parameter.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Range<wbr>Key</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the range key; must be defined
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
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the index
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">non<wbr>Key<wbr>Attributes</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Only required with `INCLUDE` as a
projection type; a list of attributes to project into the index. These
do not need to be defined as attributes on the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">projection<wbr>Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
One of `ALL`, `INCLUDE` or `KEYS_ONLY`
where `ALL` projects every attribute into the index, `KEYS_ONLY`
projects just the hash and range key into the index, and `INCLUDE`
projects only the keys specified in the _non_key_attributes_
parameter.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">range<wbr>Key</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the range key; must be defined
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
 (Required)
The name of the index
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">non_<wbr>key_<wbr>attributes</td>
            <td class="align-top">
                
                <code>list[string]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Only required with `INCLUDE` as a
projection type; a list of attributes to project into the index. These
do not need to be defined as attributes on the table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">projection_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
One of `ALL`, `INCLUDE` or `KEYS_ONLY`
where `ALL` projects every attribute into the index, `KEYS_ONLY`
projects just the hash and range key into the index, and `INCLUDE`
projects only the keys specified in the _non_key_attributes_
parameter.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">range_<wbr>key</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the range key; must be defined
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### TablePointInTimeRecovery
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#TablePointInTimeRecovery">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#TablePointInTimeRecovery">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/dynamodb?tab=doc#TablePointInTimeRecoveryArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/dynamodb?tab=doc#TablePointInTimeRecoveryOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Dynamodb.TablePointInTimeRecoveryArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Dynamodb.TablePointInTimeRecovery.html">output</a> API doc for this type.
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
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Whether to enable point-in-time recovery - note that it can take up to 10 minutes to enable for new tables. If the `point_in_time_recovery` block is not provided then this defaults to `false`.
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
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Whether to enable point-in-time recovery - note that it can take up to 10 minutes to enable for new tables. If the `point_in_time_recovery` block is not provided then this defaults to `false`.
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
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Whether to enable point-in-time recovery - note that it can take up to 10 minutes to enable for new tables. If the `point_in_time_recovery` block is not provided then this defaults to `false`.
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
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Whether to enable point-in-time recovery - note that it can take up to 10 minutes to enable for new tables. If the `point_in_time_recovery` block is not provided then this defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### TableServerSideEncryption
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#TableServerSideEncryption">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#TableServerSideEncryption">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/dynamodb?tab=doc#TableServerSideEncryptionArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/dynamodb?tab=doc#TableServerSideEncryptionOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Dynamodb.TableServerSideEncryptionArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Dynamodb.TableServerSideEncryption.html">output</a> API doc for this type.
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
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Whether to enable point-in-time recovery - note that it can take up to 10 minutes to enable for new tables. If the `point_in_time_recovery` block is not provided then this defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the CMK that should be used for the AWS KMS encryption.
This attribute should only be specified if the key is different from the default DynamoDB CMK, `alias/aws/dynamodb`.
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
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Whether to enable point-in-time recovery - note that it can take up to 10 minutes to enable for new tables. If the `point_in_time_recovery` block is not provided then this defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the CMK that should be used for the AWS KMS encryption.
This attribute should only be specified if the key is different from the default DynamoDB CMK, `alias/aws/dynamodb`.
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
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>boolean</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Whether to enable point-in-time recovery - note that it can take up to 10 minutes to enable for new tables. If the `point_in_time_recovery` block is not provided then this defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms<wbr>Key<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the CMK that should be used for the AWS KMS encryption.
This attribute should only be specified if the key is different from the default DynamoDB CMK, `alias/aws/dynamodb`.
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
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Whether to enable point-in-time recovery - note that it can take up to 10 minutes to enable for new tables. If the `point_in_time_recovery` block is not provided then this defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kms_<wbr>key_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN of the CMK that should be used for the AWS KMS encryption.
This attribute should only be specified if the key is different from the default DynamoDB CMK, `alias/aws/dynamodb`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### TableTtl
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#TableTtl">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#TableTtl">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/dynamodb?tab=doc#TableTtlArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/dynamodb?tab=doc#TableTtlOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Dynamodb.TableTtlArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Dynamodb.TableTtl.html">output</a> API doc for this type.
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
            <td class="align-top">Attribute<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the table attribute to store the TTL timestamp in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to enable point-in-time recovery - note that it can take up to 10 minutes to enable for new tables. If the `point_in_time_recovery` block is not provided then this defaults to `false`.
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
            <td class="align-top">Attribute<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the table attribute to store the TTL timestamp in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Enabled</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to enable point-in-time recovery - note that it can take up to 10 minutes to enable for new tables. If the `point_in_time_recovery` block is not provided then this defaults to `false`.
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
            <td class="align-top">attribute<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the table attribute to store the TTL timestamp in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to enable point-in-time recovery - note that it can take up to 10 minutes to enable for new tables. If the `point_in_time_recovery` block is not provided then this defaults to `false`.
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
            <td class="align-top">attribute_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The name of the table attribute to store the TTL timestamp in.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">enabled</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Whether to enable point-in-time recovery - note that it can take up to 10 minutes to enable for new tables. If the `point_in_time_recovery` block is not provided then this defaults to `false`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







