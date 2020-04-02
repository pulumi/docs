
---
title: "DataSource"
block_external_search_index: true
---

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

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/appsync/#DataSource">DataSource</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/appsync/#DataSourceArgs">DataSourceArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">DataSource</span><span class="p">(resource_name, opts=None, </span>api_id=None<span class="p">, </span>description=None<span class="p">, </span>dynamodb_config=None<span class="p">, </span>elasticsearch_config=None<span class="p">, </span>http_config=None<span class="p">, </span>lambda_config=None<span class="p">, </span>name=None<span class="p">, </span>service_role_arn=None<span class="p">, </span>type=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewDataSource<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#DataSourceArgs">DataSourceArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#DataSource">DataSource</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.DataSource.html">DataSource</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.AppSync.DataSourceArgs.html">DataSourceArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Api<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The API ID for the GraphQL API for the DataSource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A description of the DataSource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dynamodb<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourcedynamodbconfig">Data<wbr>Source<wbr>Dynamodb<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}DynamoDB settings. See below
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Elasticsearch<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourceelasticsearchconfig">Data<wbr>Source<wbr>Elasticsearch<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Amazon Elasticsearch settings. See below
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourcehttpconfig">Data<wbr>Source<wbr>Http<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}HTTP settings. See below
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lambda<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourcelambdaconfig">Data<wbr>Source<wbr>Lambda<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}AWS Lambda settings. See below
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A user-supplied name for the DataSource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IAM service role ARN for the data source.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Api<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The API ID for the GraphQL API for the DataSource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A description of the DataSource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dynamodb<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourcedynamodbconfig">*Data<wbr>Source<wbr>Dynamodb<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}DynamoDB settings. See below
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Elasticsearch<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourceelasticsearchconfig">*Data<wbr>Source<wbr>Elasticsearch<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Amazon Elasticsearch settings. See below
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourcehttpconfig">*Data<wbr>Source<wbr>Http<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}HTTP settings. See below
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lambda<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourcelambdaconfig">*Data<wbr>Source<wbr>Lambda<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}AWS Lambda settings. See below
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A user-supplied name for the DataSource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The IAM service role ARN for the data source.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>api<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The API ID for the GraphQL API for the DataSource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A description of the DataSource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dynamodb<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourcedynamodbconfig">Data<wbr>Source<wbr>Dynamodb<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}DynamoDB settings. See below
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>elasticsearch<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourceelasticsearchconfig">Data<wbr>Source<wbr>Elasticsearch<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Amazon Elasticsearch settings. See below
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourcehttpconfig">Data<wbr>Source<wbr>Http<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}HTTP settings. See below
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lambda<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourcelambdaconfig">Data<wbr>Source<wbr>Lambda<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}AWS Lambda settings. See below
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A user-supplied name for the DataSource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IAM service role ARN for the data source.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>api_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The API ID for the GraphQL API for the DataSource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A description of the DataSource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dynamodb_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourcedynamodbconfig">Dict[Data<wbr>Source<wbr>Dynamodb<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}DynamoDB settings. See below
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>elasticsearch_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourceelasticsearchconfig">Dict[Data<wbr>Source<wbr>Elasticsearch<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Amazon Elasticsearch settings. See below
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourcehttpconfig">Dict[Data<wbr>Source<wbr>Http<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}HTTP settings. See below
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lambda_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourcelambdaconfig">Dict[Data<wbr>Source<wbr>Lambda<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}AWS Lambda settings. See below
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A user-supplied name for the DataSource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service_<wbr>role_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IAM service role ARN for the data source.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## DataSource Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Api<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The API ID for the GraphQL API for the DataSource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A description of the DataSource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Dynamodb<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourcedynamodbconfig">Data<wbr>Source<wbr>Dynamodb<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}DynamoDB settings. See below
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Elasticsearch<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourceelasticsearchconfig">Data<wbr>Source<wbr>Elasticsearch<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Amazon Elasticsearch settings. See below
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Http<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourcehttpconfig">Data<wbr>Source<wbr>Http<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}HTTP settings. See below
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Lambda<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourcelambdaconfig">Data<wbr>Source<wbr>Lambda<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}AWS Lambda settings. See below
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A user-supplied name for the DataSource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Service<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IAM service role ARN for the data source.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Api<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The API ID for the GraphQL API for the DataSource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A description of the DataSource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Dynamodb<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourcedynamodbconfig">*Data<wbr>Source<wbr>Dynamodb<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}DynamoDB settings. See below
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Elasticsearch<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourceelasticsearchconfig">*Data<wbr>Source<wbr>Elasticsearch<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Amazon Elasticsearch settings. See below
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Http<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourcehttpconfig">*Data<wbr>Source<wbr>Http<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}HTTP settings. See below
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Lambda<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourcelambdaconfig">*Data<wbr>Source<wbr>Lambda<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}AWS Lambda settings. See below
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A user-supplied name for the DataSource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Service<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The IAM service role ARN for the data source.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>api<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The API ID for the GraphQL API for the DataSource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A description of the DataSource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>dynamodb<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourcedynamodbconfig">Data<wbr>Source<wbr>Dynamodb<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}DynamoDB settings. See below
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>elasticsearch<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourceelasticsearchconfig">Data<wbr>Source<wbr>Elasticsearch<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Amazon Elasticsearch settings. See below
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>http<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourcehttpconfig">Data<wbr>Source<wbr>Http<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}HTTP settings. See below
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>lambda<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourcelambdaconfig">Data<wbr>Source<wbr>Lambda<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}AWS Lambda settings. See below
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}A user-supplied name for the DataSource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>service<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IAM service role ARN for the data source.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>api_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The API ID for the GraphQL API for the DataSource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ARN
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A description of the DataSource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>dynamodb_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourcedynamodbconfig">Dict[Data<wbr>Source<wbr>Dynamodb<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}DynamoDB settings. See below
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>elasticsearch_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourceelasticsearchconfig">Dict[Data<wbr>Source<wbr>Elasticsearch<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Amazon Elasticsearch settings. See below
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>http_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourcehttpconfig">Dict[Data<wbr>Source<wbr>Http<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}HTTP settings. See below
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>lambda_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourcelambdaconfig">Dict[Data<wbr>Source<wbr>Lambda<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}AWS Lambda settings. See below
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A user-supplied name for the DataSource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>service_<wbr>role_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IAM service role ARN for the data source.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing DataSource Resource

Get an existing DataSource resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/appsync/#DataSourceState">DataSourceState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/appsync/#DataSource">DataSource</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>api_id=None<span class="p">, </span>arn=None<span class="p">, </span>description=None<span class="p">, </span>dynamodb_config=None<span class="p">, </span>elasticsearch_config=None<span class="p">, </span>http_config=None<span class="p">, </span>lambda_config=None<span class="p">, </span>name=None<span class="p">, </span>service_role_arn=None<span class="p">, </span>type=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetDataSource<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#DataSourceState">DataSourceState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#DataSource">DataSource</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.DataSource.html">DataSource</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.DataSourceState.html">DataSourceState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Api<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The API ID for the GraphQL API for the DataSource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ARN
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A description of the DataSource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dynamodb<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourcedynamodbconfig">Data<wbr>Source<wbr>Dynamodb<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}DynamoDB settings. See below
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Elasticsearch<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourceelasticsearchconfig">Data<wbr>Source<wbr>Elasticsearch<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}Amazon Elasticsearch settings. See below
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourcehttpconfig">Data<wbr>Source<wbr>Http<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}HTTP settings. See below
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lambda<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourcelambdaconfig">Data<wbr>Source<wbr>Lambda<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}AWS Lambda settings. See below
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A user-supplied name for the DataSource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IAM service role ARN for the data source.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Api<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The API ID for the GraphQL API for the DataSource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The ARN
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A description of the DataSource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Dynamodb<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourcedynamodbconfig">*Data<wbr>Source<wbr>Dynamodb<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}DynamoDB settings. See below
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Elasticsearch<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourceelasticsearchconfig">*Data<wbr>Source<wbr>Elasticsearch<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}Amazon Elasticsearch settings. See below
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Http<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourcehttpconfig">*Data<wbr>Source<wbr>Http<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}HTTP settings. See below
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Lambda<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourcelambdaconfig">*Data<wbr>Source<wbr>Lambda<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}AWS Lambda settings. See below
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A user-supplied name for the DataSource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Service<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The IAM service role ARN for the data source.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>api<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The API ID for the GraphQL API for the DataSource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The ARN
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A description of the DataSource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dynamodb<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourcedynamodbconfig">Data<wbr>Source<wbr>Dynamodb<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}DynamoDB settings. See below
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>elasticsearch<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourceelasticsearchconfig">Data<wbr>Source<wbr>Elasticsearch<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}Amazon Elasticsearch settings. See below
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourcehttpconfig">Data<wbr>Source<wbr>Http<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}HTTP settings. See below
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lambda<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourcelambdaconfig">Data<wbr>Source<wbr>Lambda<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}AWS Lambda settings. See below
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A user-supplied name for the DataSource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service<wbr>Role<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The IAM service role ARN for the data source.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>api_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The API ID for the GraphQL API for the DataSource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ARN
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A description of the DataSource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>dynamodb_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourcedynamodbconfig">Dict[Data<wbr>Source<wbr>Dynamodb<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}DynamoDB settings. See below
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>elasticsearch_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourceelasticsearchconfig">Dict[Data<wbr>Source<wbr>Elasticsearch<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}Amazon Elasticsearch settings. See below
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>http_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourcehttpconfig">Dict[Data<wbr>Source<wbr>Http<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}HTTP settings. See below
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>lambda_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#datasourcelambdaconfig">Dict[Data<wbr>Source<wbr>Lambda<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}AWS Lambda settings. See below
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A user-supplied name for the DataSource.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>service_<wbr>role_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The IAM service role ARN for the data source.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of the DataSource. Valid values: `AWS_LAMBDA`, `AMAZON_DYNAMODB`, `AMAZON_ELASTICSEARCH`, `HTTP`, `NONE`.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Data<wbr>Source<wbr>Dynamodb<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DataSourceDynamodbConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DataSourceDynamodbConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#DataSourceDynamodbConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#DataSourceDynamodbConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}AWS region of Elasticsearch domain. Defaults to current region.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Table<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the DynamoDB table.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Use<wbr>Caller<wbr>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool?</span>
    </dt>
    <dd>{{% md %}}Set to `true` to use Amazon Cognito credentials with this data source.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}AWS region of Elasticsearch domain. Defaults to current region.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Table<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the DynamoDB table.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Use<wbr>Caller<wbr>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type">*bool</span>
    </dt>
    <dd>{{% md %}}Set to `true` to use Amazon Cognito credentials with this data source.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}AWS region of Elasticsearch domain. Defaults to current region.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>table<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}Name of the DynamoDB table.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>use<wbr>Caller<wbr>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type">boolean?</span>
    </dt>
    <dd>{{% md %}}Set to `true` to use Amazon Cognito credentials with this data source.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}AWS region of Elasticsearch domain. Defaults to current region.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>table_<wbr>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Name of the DynamoDB table.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>use<wbr>Caller<wbr>Credentials</span>
        <span class="property-indicator"></span>
        <span class="property-type">bool</span>
    </dt>
    <dd>{{% md %}}Set to `true` to use Amazon Cognito credentials with this data source.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Data<wbr>Source<wbr>Elasticsearch<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DataSourceElasticsearchConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DataSourceElasticsearchConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#DataSourceElasticsearchConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#DataSourceElasticsearchConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}HTTP URL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}AWS region of Elasticsearch domain. Defaults to current region.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}HTTP URL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Region</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}AWS region of Elasticsearch domain. Defaults to current region.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}HTTP URL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}AWS region of Elasticsearch domain. Defaults to current region.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}HTTP URL.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>region</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}AWS region of Elasticsearch domain. Defaults to current region.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Data<wbr>Source<wbr>Http<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DataSourceHttpConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DataSourceHttpConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#DataSourceHttpConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#DataSourceHttpConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}HTTP URL.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}HTTP URL.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}HTTP URL.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>endpoint</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}HTTP URL.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}





<h4>Data<wbr>Source<wbr>Lambda<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DataSourceLambdaConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DataSourceLambdaConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#DataSourceLambdaConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#DataSourceLambdaConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Function<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN for the Lambda function.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Function<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN for the Lambda function.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>function<wbr>Arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The ARN for the Lambda function.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>function_<wbr>arn</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The ARN for the Lambda function.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-aws">https://github.com/pulumi/pulumi-aws</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd></dl>
