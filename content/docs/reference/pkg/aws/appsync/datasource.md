
---
title: "DataSource"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Provides an AppSync DataSource.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const exampleTable = new aws.dynamodb.Table("example", {
    attributes: [{
        name: "UserId",
        type: "S",
    }],
    hashKey: "UserId",
    readCapacity: 1,
    writeCapacity: 1,
});
const exampleRole = new aws.iam.Role("example", {
    assumeRolePolicy: `{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "appsync.amazonaws.com"
      },
      "Effect": "Allow"
    }
  ]
}
`,
});
const exampleRolePolicy = new aws.iam.RolePolicy("example", {
    policy: pulumi.interpolate`{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": [
        "dynamodb:*"
      ],
      "Effect": "Allow",
      "Resource": [
        "${exampleTable.arn}"
      ]
    }
  ]
}
`,
    role: exampleRole.id,
});
const exampleGraphQLApi = new aws.appsync.GraphQLApi("example", {
    authenticationType: "API_KEY",
});
const exampleDataSource = new aws.appsync.DataSource("example", {
    apiId: exampleGraphQLApi.id,
    dynamodbConfig: {
        tableName: exampleTable.name,
    },
    serviceRoleArn: exampleRole.arn,
    type: "AMAZON_DYNAMODB",
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appsync_datasource.html.markdown.



## Create a DataSource Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/appsync/#DataSource">DataSource</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/appsync/#DataSourceArgs">DataSourceArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">DataSource</span><span class="p">(resource_name, opts=None, </span>api_id=None<span class="p">, </span>description=None<span class="p">, </span>dynamodb_config=None<span class="p">, </span>elasticsearch_config=None<span class="p">, </span>http_config=None<span class="p">, </span>lambda_config=None<span class="p">, </span>name=None<span class="p">, </span>service_role_arn=None<span class="p">, </span>type=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewDataSource<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#DataSourceArgs">DataSourceArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#DataSource">DataSource</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.DataSource.html">DataSource</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.DataSourceArgs.html">DataSourceArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a DataSource resource with the given unique name, arguments, and options.

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
            <td class="align-top">Api<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The API ID for the GraphQL API for the DataSource.
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
A description of the DataSource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dynamodb<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#datasourcedynamodbconfig">Pulumi.<wbr>Aws.<wbr>Appsync.<wbr>Data<wbr>Source<wbr>Dynamodb<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
DynamoDB settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elasticsearch<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#datasourceelasticsearchconfig">Pulumi.<wbr>Aws.<wbr>Appsync.<wbr>Data<wbr>Source<wbr>Elasticsearch<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Elasticsearch settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Http<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#datasourcehttpconfig">Pulumi.<wbr>Aws.<wbr>Appsync.<wbr>Data<wbr>Source<wbr>Http<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
HTTP settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#datasourcelambdaconfig">Pulumi.<wbr>Aws.<wbr>Appsync.<wbr>Data<wbr>Source<wbr>Lambda<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
AWS Lambda settings. See below
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
A user-supplied name for the DataSource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IAM service role ARN for the data source.
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
The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
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
            <td class="align-top">Api<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The API ID for the GraphQL API for the DataSource.
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
A description of the DataSource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dynamodb<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#datasourcedynamodbconfig">*appsync.<wbr>Data<wbr>Source<wbr>Dynamodb<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
DynamoDB settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elasticsearch<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#datasourceelasticsearchconfig">*appsync.<wbr>Data<wbr>Source<wbr>Elasticsearch<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Elasticsearch settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Http<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#datasourcehttpconfig">*appsync.<wbr>Data<wbr>Source<wbr>Http<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
HTTP settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#datasourcelambdaconfig">*appsync.<wbr>Data<wbr>Source<wbr>Lambda<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
AWS Lambda settings. See below
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
A user-supplied name for the DataSource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IAM service role ARN for the data source.
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
The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
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
            <td class="align-top">api<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The API ID for the GraphQL API for the DataSource.
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
A description of the DataSource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dynamodb<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#datasourcedynamodbconfig">appsync.<wbr>Data<wbr>Source<wbr>Dynamodb<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
DynamoDB settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elasticsearch<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#datasourceelasticsearchconfig">appsync.<wbr>Data<wbr>Source<wbr>Elasticsearch<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Elasticsearch settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">http<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#datasourcehttpconfig">appsync.<wbr>Data<wbr>Source<wbr>Http<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
HTTP settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#datasourcelambdaconfig">appsync.<wbr>Data<wbr>Source<wbr>Lambda<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
AWS Lambda settings. See below
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
A user-supplied name for the DataSource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IAM service role ARN for the data source.
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
The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
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
            <td class="align-top">api_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The API ID for the GraphQL API for the DataSource.
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
A description of the DataSource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dynamodb_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#datasourcedynamodbconfig">Dict[Data<wbr>Source<wbr>Dynamodb<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
DynamoDB settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elasticsearch_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#datasourceelasticsearchconfig">Dict[Data<wbr>Source<wbr>Elasticsearch<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Elasticsearch settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">http_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#datasourcehttpconfig">Dict[Data<wbr>Source<wbr>Http<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
HTTP settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#datasourcelambdaconfig">Dict[Data<wbr>Source<wbr>Lambda<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
AWS Lambda settings. See below
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
A user-supplied name for the DataSource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service_<wbr>role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IAM service role ARN for the data source.
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
The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## DataSource Output Properties

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
            <td class="align-top">Api<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The API ID for the GraphQL API for the DataSource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} A description of the DataSource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dynamodb<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#datasourcedynamodbconfig">Pulumi.<wbr>Aws.<wbr>Appsync.<wbr>Data<wbr>Source<wbr>Dynamodb<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} DynamoDB settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elasticsearch<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#datasourceelasticsearchconfig">Pulumi.<wbr>Aws.<wbr>Appsync.<wbr>Data<wbr>Source<wbr>Elasticsearch<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} Amazon Elasticsearch settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Http<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#datasourcehttpconfig">Pulumi.<wbr>Aws.<wbr>Appsync.<wbr>Data<wbr>Source<wbr>Http<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} HTTP settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#datasourcelambdaconfig">Pulumi.<wbr>Aws.<wbr>Appsync.<wbr>Data<wbr>Source<wbr>Lambda<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} AWS Lambda settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A user-supplied name for the DataSource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The IAM service role ARN for the data source.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
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
            <td class="align-top">Api<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The API ID for the GraphQL API for the DataSource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Description</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} A description of the DataSource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dynamodb<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#datasourcedynamodbconfig">*appsync.<wbr>Data<wbr>Source<wbr>Dynamodb<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} DynamoDB settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elasticsearch<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#datasourceelasticsearchconfig">*appsync.<wbr>Data<wbr>Source<wbr>Elasticsearch<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} Amazon Elasticsearch settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Http<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#datasourcehttpconfig">*appsync.<wbr>Data<wbr>Source<wbr>Http<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} HTTP settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#datasourcelambdaconfig">*appsync.<wbr>Data<wbr>Source<wbr>Lambda<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} AWS Lambda settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A user-supplied name for the DataSource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The IAM service role ARN for the data source.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
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
            <td class="align-top">api<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The API ID for the GraphQL API for the DataSource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ARN
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} A description of the DataSource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dynamodb<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#datasourcedynamodbconfig">appsync.<wbr>Data<wbr>Source<wbr>Dynamodb<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} DynamoDB settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elasticsearch<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#datasourceelasticsearchconfig">appsync.<wbr>Data<wbr>Source<wbr>Elasticsearch<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} Amazon Elasticsearch settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">http<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#datasourcehttpconfig">appsync.<wbr>Data<wbr>Source<wbr>Http<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} HTTP settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#datasourcelambdaconfig">appsync.<wbr>Data<wbr>Source<wbr>Lambda<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} AWS Lambda settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A user-supplied name for the DataSource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The IAM service role ARN for the data source.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
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
            <td class="align-top">api_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The API ID for the GraphQL API for the DataSource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ARN
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">description</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A description of the DataSource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dynamodb_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#datasourcedynamodbconfig">Dict[Data<wbr>Source<wbr>Dynamodb<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} DynamoDB settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elasticsearch_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#datasourceelasticsearchconfig">Dict[Data<wbr>Source<wbr>Elasticsearch<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} Amazon Elasticsearch settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">http_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#datasourcehttpconfig">Dict[Data<wbr>Source<wbr>Http<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} HTTP settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#datasourcelambdaconfig">Dict[Data<wbr>Source<wbr>Lambda<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} AWS Lambda settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A user-supplied name for the DataSource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service_<wbr>role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The IAM service role ARN for the data source.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing DataSource Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/appsync/#DataSourceState">DataSourceState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/appsync/#DataSource">DataSource</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>api_id=None<span class="p">, </span>arn=None<span class="p">, </span>description=None<span class="p">, </span>dynamodb_config=None<span class="p">, </span>elasticsearch_config=None<span class="p">, </span>http_config=None<span class="p">, </span>lambda_config=None<span class="p">, </span>name=None<span class="p">, </span>service_role_arn=None<span class="p">, </span>type=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetDataSource<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#DataSourceState">DataSourceState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#DataSource">DataSource</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.DataSource.html">DataSource</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.DataSourceState.html">DataSourceState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing DataSource resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Api<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The API ID for the GraphQL API for the DataSource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN
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
A description of the DataSource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dynamodb<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#datasourcedynamodbconfig">Pulumi.<wbr>Aws.<wbr>Appsync.<wbr>Data<wbr>Source<wbr>Dynamodb<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
DynamoDB settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elasticsearch<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#datasourceelasticsearchconfig">Pulumi.<wbr>Aws.<wbr>Appsync.<wbr>Data<wbr>Source<wbr>Elasticsearch<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Elasticsearch settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Http<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#datasourcehttpconfig">Pulumi.<wbr>Aws.<wbr>Appsync.<wbr>Data<wbr>Source<wbr>Http<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
HTTP settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#datasourcelambdaconfig">Pulumi.<wbr>Aws.<wbr>Appsync.<wbr>Data<wbr>Source<wbr>Lambda<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
AWS Lambda settings. See below
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
A user-supplied name for the DataSource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IAM service role ARN for the data source.
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
The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
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
            <td class="align-top">Api<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The API ID for the GraphQL API for the DataSource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN
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
A description of the DataSource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Dynamodb<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#datasourcedynamodbconfig">*appsync.<wbr>Data<wbr>Source<wbr>Dynamodb<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
DynamoDB settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Elasticsearch<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#datasourceelasticsearchconfig">*appsync.<wbr>Data<wbr>Source<wbr>Elasticsearch<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Elasticsearch settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Http<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#datasourcehttpconfig">*appsync.<wbr>Data<wbr>Source<wbr>Http<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
HTTP settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Lambda<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#datasourcelambdaconfig">*appsync.<wbr>Data<wbr>Source<wbr>Lambda<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
AWS Lambda settings. See below
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
A user-supplied name for the DataSource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IAM service role ARN for the data source.
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
The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
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
            <td class="align-top">api<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The API ID for the GraphQL API for the DataSource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN
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
A description of the DataSource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dynamodb<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#datasourcedynamodbconfig">appsync.<wbr>Data<wbr>Source<wbr>Dynamodb<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
DynamoDB settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elasticsearch<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#datasourceelasticsearchconfig">appsync.<wbr>Data<wbr>Source<wbr>Elasticsearch<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Elasticsearch settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">http<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#datasourcehttpconfig">appsync.<wbr>Data<wbr>Source<wbr>Http<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
HTTP settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#datasourcelambdaconfig">appsync.<wbr>Data<wbr>Source<wbr>Lambda<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
AWS Lambda settings. See below
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
A user-supplied name for the DataSource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service<wbr>Role<wbr>Arn</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IAM service role ARN for the data source.
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
The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
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
            <td class="align-top">api_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The API ID for the GraphQL API for the DataSource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ARN
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
A description of the DataSource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">dynamodb_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#datasourcedynamodbconfig">Dict[Data<wbr>Source<wbr>Dynamodb<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
DynamoDB settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">elasticsearch_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#datasourceelasticsearchconfig">Dict[Data<wbr>Source<wbr>Elasticsearch<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Amazon Elasticsearch settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">http_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#datasourcehttpconfig">Dict[Data<wbr>Source<wbr>Http<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
HTTP settings. See below
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">lambda_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#datasourcelambdaconfig">Dict[Data<wbr>Source<wbr>Lambda<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
AWS Lambda settings. See below
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
A user-supplied name for the DataSource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service_<wbr>role_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The IAM service role ARN for the data source.
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
The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### DataSourceDynamodbConfig
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DataSourceDynamodbConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DataSourceDynamodbConfig">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#DataSourceDynamodbConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#DataSourceDynamodbConfigOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.DataSourceDynamodbConfigArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.DataSourceDynamodbConfig.html">output</a> API doc for this type.
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
            <td class="align-top">Region</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
AWS region of Elasticsearch domain. Defaults to current region.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Table<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Name of the DynamoDB table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Use<wbr>Caller<wbr>Credentials</td>
            <td class="align-top">
                
                <code>bool?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set to `true` to use Amazon Cognito credentials with this data source.
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
            <td class="align-top">Region</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
AWS region of Elasticsearch domain. Defaults to current region.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Table<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Name of the DynamoDB table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Use<wbr>Caller<wbr>Credentials</td>
            <td class="align-top">
                
                <code>*bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set to `true` to use Amazon Cognito credentials with this data source.
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
            <td class="align-top">region</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
AWS region of Elasticsearch domain. Defaults to current region.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">table<wbr>Name</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Name of the DynamoDB table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">use<wbr>Caller<wbr>Credentials</td>
            <td class="align-top">
                
                <code>boolean?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set to `true` to use Amazon Cognito credentials with this data source.
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
            <td class="align-top">region</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
AWS region of Elasticsearch domain. Defaults to current region.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">table_<wbr>name</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
Name of the DynamoDB table.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">use<wbr>Caller<wbr>Credentials</td>
            <td class="align-top">
                
                <code>bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
Set to `true` to use Amazon Cognito credentials with this data source.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DataSourceElasticsearchConfig
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DataSourceElasticsearchConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DataSourceElasticsearchConfig">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#DataSourceElasticsearchConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#DataSourceElasticsearchConfigOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.DataSourceElasticsearchConfigArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.DataSourceElasticsearchConfig.html">output</a> API doc for this type.
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
            <td class="align-top">Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
HTTP URL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Region</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
AWS region of Elasticsearch domain. Defaults to current region.
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
            <td class="align-top">Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
HTTP URL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Region</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
AWS region of Elasticsearch domain. Defaults to current region.
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
            <td class="align-top">endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
HTTP URL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">region</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
AWS region of Elasticsearch domain. Defaults to current region.
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
            <td class="align-top">endpoint</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
HTTP URL.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">region</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
AWS region of Elasticsearch domain. Defaults to current region.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DataSourceHttpConfig
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DataSourceHttpConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DataSourceHttpConfig">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#DataSourceHttpConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#DataSourceHttpConfigOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.DataSourceHttpConfigArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.DataSourceHttpConfig.html">output</a> API doc for this type.
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
            <td class="align-top">Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
HTTP URL.
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
            <td class="align-top">Endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
HTTP URL.
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
            <td class="align-top">endpoint</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
HTTP URL.
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
            <td class="align-top">endpoint</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
HTTP URL.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}





#### DataSourceLambdaConfig
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DataSourceLambdaConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DataSourceLambdaConfig">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#DataSourceLambdaConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#DataSourceLambdaConfigOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.DataSourceLambdaConfigArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.DataSourceLambdaConfig.html">output</a> API doc for this type.
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
            <td class="align-top">Function<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN for the Lambda function.
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
            <td class="align-top">Function<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN for the Lambda function.
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
            <td class="align-top">function<wbr>Arn</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN for the Lambda function.
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
            <td class="align-top">function_<wbr>arn</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ARN for the Lambda function.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







