
---
title: "Connection"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Provides a Glue Connection resource.

## Example Usage

### Non-VPC Connection

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = new aws.glue.Connection("example", {
    connectionProperties: {
        JDBC_CONNECTION_URL: "jdbc:mysql://example.com/exampledatabase",
        PASSWORD: "examplepassword",
        USERNAME: "exampleusername",
    },
});
```

### VPC Connection

For more information, see the [AWS Documentation](https://docs.aws.amazon.com/glue/latest/dg/populate-add-connection.html#connection-JDBC-VPC).

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = new aws.glue.Connection("example", {
    connectionProperties: {
        JDBC_CONNECTION_URL: pulumi.interpolate`jdbc:mysql://${aws_rds_cluster_example.endpoint}/exampledatabase`,
        PASSWORD: "examplepassword",
        USERNAME: "exampleusername",
    },
    physicalConnectionRequirements: {
        availabilityZone: aws_subnet_example.availabilityZone,
        securityGroupIdLists: [aws_security_group_example.id],
        subnetId: aws_subnet_example.id,
    },
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/glue_connection.html.markdown.



## Create a Connection Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/glue/#Connection">Connection</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/glue/#ConnectionArgs">ConnectionArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Connection</span><span class="p">(resource_name, opts=None, </span>catalog_id=None<span class="p">, </span>connection_properties=None<span class="p">, </span>connection_type=None<span class="p">, </span>description=None<span class="p">, </span>match_criterias=None<span class="p">, </span>name=None<span class="p">, </span>physical_connection_requirements=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewConnection<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#ConnectionArgs">ConnectionArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#Connection">Connection</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.Connection.html">Connection</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.ConnectionArgs.html">ConnectionArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a Connection resource with the given unique name, arguments, and options.

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
The ID of the Data Catalog in which to create the connection. If none is supplied, the AWS account ID is used by default.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Connection<wbr>Properties</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A map of key-value pairs used as parameters for this connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Connection<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of the connection. Defaults to `JBDC`.
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
Description of the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Match<wbr>Criterias</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of criteria that can be used in selecting this connection.
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
The name of the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Physical<wbr>Connection<wbr>Requirements</td>
            <td class="align-top">
                
                <code><a href="#connectionphysicalconnectionrequirements">Pulumi.<wbr>Aws.<wbr>Glue.<wbr>Connection<wbr>Physical<wbr>Connection<wbr>Requirements<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of physical connection requirements, such as VPC and SecurityGroup. Defined below.
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
The ID of the Data Catalog in which to create the connection. If none is supplied, the AWS account ID is used by default.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Connection<wbr>Properties</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A map of key-value pairs used as parameters for this connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Connection<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of the connection. Defaults to `JBDC`.
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
Description of the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Match<wbr>Criterias</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of criteria that can be used in selecting this connection.
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
The name of the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Physical<wbr>Connection<wbr>Requirements</td>
            <td class="align-top">
                
                <code><a href="#connectionphysicalconnectionrequirements">*Connection<wbr>Physical<wbr>Connection<wbr>Requirements</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of physical connection requirements, such as VPC and SecurityGroup. Defined below.
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
The ID of the Data Catalog in which to create the connection. If none is supplied, the AWS account ID is used by default.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">connection<wbr>Properties</td>
            <td class="align-top">
                
                <code>{[key: string]: any}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A map of key-value pairs used as parameters for this connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">connection<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of the connection. Defaults to `JBDC`.
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
Description of the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">match<wbr>Criterias</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of criteria that can be used in selecting this connection.
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
The name of the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">physical<wbr>Connection<wbr>Requirements</td>
            <td class="align-top">
                
                <code><a href="#connectionphysicalconnectionrequirements">glue.<wbr>Connection<wbr>Physical<wbr>Connection<wbr>Requirements?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of physical connection requirements, such as VPC and SecurityGroup. Defined below.
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
The ID of the Data Catalog in which to create the connection. If none is supplied, the AWS account ID is used by default.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">connection_<wbr>properties</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A map of key-value pairs used as parameters for this connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">connection_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of the connection. Defaults to `JBDC`.
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
Description of the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">match_<wbr>criterias</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of criteria that can be used in selecting this connection.
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
The name of the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">physical_<wbr>connection_<wbr>requirements</td>
            <td class="align-top">
                
                <code><a href="#connectionphysicalconnectionrequirements">Dict[Connection<wbr>Physical<wbr>Connection<wbr>Requirements]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of physical connection requirements, such as VPC and SecurityGroup. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## Connection Output Properties

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
            <td class="align-top">{{% md %}} The ID of the Data Catalog in which to create the connection. If none is supplied, the AWS account ID is used by default.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Connection<wbr>Properties</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;</code>
            </td>
            <td class="align-top">{{% md %}} A map of key-value pairs used as parameters for this connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Connection<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The type of the connection. Defaults to `JBDC`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Description of the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Match<wbr>Criterias</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A list of criteria that can be used in selecting this connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Physical<wbr>Connection<wbr>Requirements</td>
            <td class="align-top">
                
                <code><a href="#connectionphysicalconnectionrequirements">Pulumi.<wbr>Aws.<wbr>Glue.<wbr>Connection<wbr>Physical<wbr>Connection<wbr>Requirements?</a></code>
            </td>
            <td class="align-top">{{% md %}} A map of physical connection requirements, such as VPC and SecurityGroup. Defined below.
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
            <td class="align-top">{{% md %}} The ID of the Data Catalog in which to create the connection. If none is supplied, the AWS account ID is used by default.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Connection<wbr>Properties</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} A map of key-value pairs used as parameters for this connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Connection<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The type of the connection. Defaults to `JBDC`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} Description of the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Match<wbr>Criterias</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} A list of criteria that can be used in selecting this connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Physical<wbr>Connection<wbr>Requirements</td>
            <td class="align-top">
                
                <code><a href="#connectionphysicalconnectionrequirements">*Connection<wbr>Physical<wbr>Connection<wbr>Requirements</a></code>
            </td>
            <td class="align-top">{{% md %}} A map of physical connection requirements, such as VPC and SecurityGroup. Defined below.
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
            <td class="align-top">{{% md %}} The ID of the Data Catalog in which to create the connection. If none is supplied, the AWS account ID is used by default.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">connection<wbr>Properties</td>
            <td class="align-top">
                
                <code>{[key: string]: any}</code>
            </td>
            <td class="align-top">{{% md %}} A map of key-value pairs used as parameters for this connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">connection<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The type of the connection. Defaults to `JBDC`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} Description of the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">match<wbr>Criterias</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} A list of criteria that can be used in selecting this connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The name of the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">physical<wbr>Connection<wbr>Requirements</td>
            <td class="align-top">
                
                <code><a href="#connectionphysicalconnectionrequirements">glue.<wbr>Connection<wbr>Physical<wbr>Connection<wbr>Requirements?</a></code>
            </td>
            <td class="align-top">{{% md %}} A map of physical connection requirements, such as VPC and SecurityGroup. Defined below.
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
            <td class="align-top">{{% md %}} The ID of the Data Catalog in which to create the connection. If none is supplied, the AWS account ID is used by default.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">connection_<wbr>properties</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} A map of key-value pairs used as parameters for this connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">connection_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The type of the connection. Defaults to `JBDC`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Description of the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">match_<wbr>criterias</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} A list of criteria that can be used in selecting this connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The name of the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">physical_<wbr>connection_<wbr>requirements</td>
            <td class="align-top">
                
                <code><a href="#connectionphysicalconnectionrequirements">Dict[Connection<wbr>Physical<wbr>Connection<wbr>Requirements]</a></code>
            </td>
            <td class="align-top">{{% md %}} A map of physical connection requirements, such as VPC and SecurityGroup. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing Connection Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/glue/#ConnectionState">ConnectionState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/glue/#Connection">Connection</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>catalog_id=None<span class="p">, </span>connection_properties=None<span class="p">, </span>connection_type=None<span class="p">, </span>description=None<span class="p">, </span>match_criterias=None<span class="p">, </span>name=None<span class="p">, </span>physical_connection_requirements=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetConnection<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#ConnectionState">ConnectionState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#Connection">Connection</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.Connection.html">Connection</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.ConnectionState.html">ConnectionState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing Connection resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
The ID of the Data Catalog in which to create the connection. If none is supplied, the AWS account ID is used by default.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Connection<wbr>Properties</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, object&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of key-value pairs used as parameters for this connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Connection<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of the connection. Defaults to `JBDC`.
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
Description of the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Match<wbr>Criterias</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of criteria that can be used in selecting this connection.
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
The name of the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Physical<wbr>Connection<wbr>Requirements</td>
            <td class="align-top">
                
                <code><a href="#connectionphysicalconnectionrequirements">Pulumi.<wbr>Aws.<wbr>Glue.<wbr>Connection<wbr>Physical<wbr>Connection<wbr>Requirements<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of physical connection requirements, such as VPC and SecurityGroup. Defined below.
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
The ID of the Data Catalog in which to create the connection. If none is supplied, the AWS account ID is used by default.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Connection<wbr>Properties</td>
            <td class="align-top">
                
                <code>map[string]interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of key-value pairs used as parameters for this connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Connection<wbr>Type</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of the connection. Defaults to `JBDC`.
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
Description of the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Match<wbr>Criterias</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of criteria that can be used in selecting this connection.
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
The name of the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Physical<wbr>Connection<wbr>Requirements</td>
            <td class="align-top">
                
                <code><a href="#connectionphysicalconnectionrequirements">*Connection<wbr>Physical<wbr>Connection<wbr>Requirements</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of physical connection requirements, such as VPC and SecurityGroup. Defined below.
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
The ID of the Data Catalog in which to create the connection. If none is supplied, the AWS account ID is used by default.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">connection<wbr>Properties</td>
            <td class="align-top">
                
                <code>{[key: string]: any}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of key-value pairs used as parameters for this connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">connection<wbr>Type</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of the connection. Defaults to `JBDC`.
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
Description of the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">match<wbr>Criterias</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of criteria that can be used in selecting this connection.
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
The name of the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">physical<wbr>Connection<wbr>Requirements</td>
            <td class="align-top">
                
                <code><a href="#connectionphysicalconnectionrequirements">glue.<wbr>Connection<wbr>Physical<wbr>Connection<wbr>Requirements?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of physical connection requirements, such as VPC and SecurityGroup. Defined below.
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
The ID of the Data Catalog in which to create the connection. If none is supplied, the AWS account ID is used by default.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">connection_<wbr>properties</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of key-value pairs used as parameters for this connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">connection_<wbr>type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The type of the connection. Defaults to `JBDC`.
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
Description of the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">match_<wbr>criterias</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A list of criteria that can be used in selecting this connection.
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
The name of the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">physical_<wbr>connection_<wbr>requirements</td>
            <td class="align-top">
                
                <code><a href="#connectionphysicalconnectionrequirements">Dict[Connection<wbr>Physical<wbr>Connection<wbr>Requirements]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of physical connection requirements, such as VPC and SecurityGroup. Defined below.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### ConnectionPhysicalConnectionRequirements
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ConnectionPhysicalConnectionRequirements">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ConnectionPhysicalConnectionRequirements">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#ConnectionPhysicalConnectionRequirementsArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/glue?tab=doc#ConnectionPhysicalConnectionRequirementsOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.ConnectionPhysicalConnectionRequirementsArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Glue.ConnectionPhysicalConnectionRequirements.html">output</a> API doc for this type.
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
            <td class="align-top">Availability<wbr>Zone</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The availability zone of the connection. This field is redundant and implied by `subnet_id`, but is currently an api requirement.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Group<wbr>Id<wbr>Lists</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The security group ID list used by the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The subnet ID used by the connection.
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
            <td class="align-top">Availability<wbr>Zone</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The availability zone of the connection. This field is redundant and implied by `subnet_id`, but is currently an api requirement.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Security<wbr>Group<wbr>Id<wbr>Lists</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The security group ID list used by the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Subnet<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The subnet ID used by the connection.
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
            <td class="align-top">availability<wbr>Zone</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The availability zone of the connection. This field is redundant and implied by `subnet_id`, but is currently an api requirement.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security<wbr>Group<wbr>Id<wbr>Lists</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The security group ID list used by the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The subnet ID used by the connection.
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
            <td class="align-top">availability_<wbr>zone</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The availability zone of the connection. This field is redundant and implied by `subnet_id`, but is currently an api requirement.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">security<wbr>Group<wbr>Id<wbr>Lists</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The security group ID list used by the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">subnet_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The subnet ID used by the connection.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







