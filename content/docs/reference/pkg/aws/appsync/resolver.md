
---
title: "Resolver"
block_external_search_index: true
---



Provides an AppSync Resolver.

{{% examples %}}
## Example Usage
{{% example %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const testGraphQLApi = new aws.appsync.GraphQLApi("test", {
    authenticationType: "API_KEY",
    schema: `type Mutation {
	putPost(id: ID!, title: String!): Post
}

type Post {
	id: ID!
	title: String!
}

type Query {
	singlePost(id: ID!): Post
}

schema {
	query: Query
	mutation: Mutation
}
`,
});
const testDataSource = new aws.appsync.DataSource("test", {
    apiId: testGraphQLApi.id,
    httpConfig: {
        endpoint: "http://example.com",
    },
    type: "HTTP",
});
// UNIT type resolver (default)
const testResolver = new aws.appsync.Resolver("test", {
    apiId: testGraphQLApi.id,
    dataSource: testDataSource.name,
    field: "singlePost",
    requestTemplate: `{
    "version": "2018-05-29",
    "method": "GET",
    "resourcePath": "/",
    "params":{
        "headers": $utils.http.copyheaders($ctx.request.headers)
    }
}
`,
    responseTemplate: `#if($ctx.result.statusCode == 200)
    $ctx.result.body
#else
    $utils.appendError($ctx.result.body, $ctx.result.statusCode)
#end
`,
    type: "Query",
});
// PIPELINE type resolver
const mutationPipelineTest = new aws.appsync.Resolver("Mutation_pipelineTest", {
    apiId: testGraphQLApi.id,
    field: "pipelineTest",
    kind: "PIPELINE",
    pipelineConfig: {
        functions: [
            aws_appsync_function_test1.functionId,
            aws_appsync_function_test2.functionId,
            aws_appsync_function_test3.functionId,
        ],
    },
    requestTemplate: "{}",
    responseTemplate: "$util.toJson($ctx.result)",
    type: "Mutation",
});
```

{{% /example %}}
{{% /examples %}}



## Create a Resolver Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/appsync/#Resolver">Resolver</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/appsync/#ResolverArgs">ResolverArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Resolver</span><span class="p">(resource_name, opts=None, </span>api_id=None<span class="p">, </span>data_source=None<span class="p">, </span>field=None<span class="p">, </span>kind=None<span class="p">, </span>pipeline_config=None<span class="p">, </span>request_template=None<span class="p">, </span>response_template=None<span class="p">, </span>type=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewResolver<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#ResolverArgs">ResolverArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#Resolver">Resolver</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.Resolver.html">Resolver</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.AppSync.ResolverArgs.html">ResolverArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
    <dd>{{% md %}}The API ID for the GraphQL API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Data<wbr>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The DataSource name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The field name from the schema defined in the GraphQL API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The resolver type. Valid values are `UNIT` and `PIPELINE`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pipeline<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#resolverpipelineconfig">Resolver<wbr>Pipeline<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The PipelineConfig. A `pipeline_config` block is documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Request<wbr>Template</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The request mapping template for UNIT resolver or 'before mapping template' for PIPELINE resolver.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Response<wbr>Template</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The response mapping template for UNIT resolver or 'after mapping template' for PIPELINE resolver.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type name from the schema defined in the GraphQL API.
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
    <dd>{{% md %}}The API ID for the GraphQL API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Data<wbr>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The DataSource name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The field name from the schema defined in the GraphQL API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The resolver type. Valid values are `UNIT` and `PIPELINE`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pipeline<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#resolverpipelineconfig">*Resolver<wbr>Pipeline<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The PipelineConfig. A `pipeline_config` block is documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Request<wbr>Template</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The request mapping template for UNIT resolver or 'before mapping template' for PIPELINE resolver.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Response<wbr>Template</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The response mapping template for UNIT resolver or 'after mapping template' for PIPELINE resolver.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type name from the schema defined in the GraphQL API.
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
    <dd>{{% md %}}The API ID for the GraphQL API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>data<wbr>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The DataSource name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The field name from the schema defined in the GraphQL API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The resolver type. Valid values are `UNIT` and `PIPELINE`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pipeline<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#resolverpipelineconfig">Resolver<wbr>Pipeline<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}The PipelineConfig. A `pipeline_config` block is documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>request<wbr>Template</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The request mapping template for UNIT resolver or 'before mapping template' for PIPELINE resolver.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>response<wbr>Template</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The response mapping template for UNIT resolver or 'after mapping template' for PIPELINE resolver.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type name from the schema defined in the GraphQL API.
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
    <dd>{{% md %}}The API ID for the GraphQL API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>data_<wbr>source</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The DataSource name.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>field</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The field name from the schema defined in the GraphQL API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The resolver type. Valid values are `UNIT` and `PIPELINE`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pipeline_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#resolverpipelineconfig">Dict[Resolver<wbr>Pipeline<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The PipelineConfig. A `pipeline_config` block is documented below.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>request_<wbr>template</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The request mapping template for UNIT resolver or 'before mapping template' for PIPELINE resolver.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>response_<wbr>template</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The response mapping template for UNIT resolver or 'after mapping template' for PIPELINE resolver.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type name from the schema defined in the GraphQL API.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Resolver Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Api<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The API ID for the GraphQL API.
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
        <span>Data<wbr>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The DataSource name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The field name from the schema defined in the GraphQL API.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The resolver type. Valid values are `UNIT` and `PIPELINE`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Pipeline<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#resolverpipelineconfig">Resolver<wbr>Pipeline<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}The PipelineConfig. A `pipeline_config` block is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Request<wbr>Template</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The request mapping template for UNIT resolver or 'before mapping template' for PIPELINE resolver.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Response<wbr>Template</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The response mapping template for UNIT resolver or 'after mapping template' for PIPELINE resolver.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type name from the schema defined in the GraphQL API.
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
    <dd>{{% md %}}The API ID for the GraphQL API.
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
        <span>Data<wbr>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The DataSource name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The field name from the schema defined in the GraphQL API.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The resolver type. Valid values are `UNIT` and `PIPELINE`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Pipeline<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#resolverpipelineconfig">*Resolver<wbr>Pipeline<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The PipelineConfig. A `pipeline_config` block is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Request<wbr>Template</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The request mapping template for UNIT resolver or 'before mapping template' for PIPELINE resolver.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Response<wbr>Template</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The response mapping template for UNIT resolver or 'after mapping template' for PIPELINE resolver.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type name from the schema defined in the GraphQL API.
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
    <dd>{{% md %}}The API ID for the GraphQL API.
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
        <span>data<wbr>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The DataSource name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The field name from the schema defined in the GraphQL API.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The resolver type. Valid values are `UNIT` and `PIPELINE`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>pipeline<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#resolverpipelineconfig">Resolver<wbr>Pipeline<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}The PipelineConfig. A `pipeline_config` block is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>request<wbr>Template</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The request mapping template for UNIT resolver or 'before mapping template' for PIPELINE resolver.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>response<wbr>Template</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The response mapping template for UNIT resolver or 'after mapping template' for PIPELINE resolver.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The type name from the schema defined in the GraphQL API.
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
    <dd>{{% md %}}The API ID for the GraphQL API.
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
        <span>data_<wbr>source</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The DataSource name.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>field</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The field name from the schema defined in the GraphQL API.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The resolver type. Valid values are `UNIT` and `PIPELINE`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>pipeline_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#resolverpipelineconfig">Dict[Resolver<wbr>Pipeline<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The PipelineConfig. A `pipeline_config` block is documented below.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>request_<wbr>template</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The request mapping template for UNIT resolver or 'before mapping template' for PIPELINE resolver.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>response_<wbr>template</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The response mapping template for UNIT resolver or 'after mapping template' for PIPELINE resolver.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type name from the schema defined in the GraphQL API.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Resolver Resource

Get an existing Resolver resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/appsync/#ResolverState">ResolverState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/appsync/#Resolver">Resolver</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>api_id=None<span class="p">, </span>arn=None<span class="p">, </span>data_source=None<span class="p">, </span>field=None<span class="p">, </span>kind=None<span class="p">, </span>pipeline_config=None<span class="p">, </span>request_template=None<span class="p">, </span>response_template=None<span class="p">, </span>type=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetResolver<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#ResolverState">ResolverState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#Resolver">Resolver</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.Resolver.html">Resolver</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.ResolverState.html">ResolverState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
    <dd>{{% md %}}The API ID for the GraphQL API.
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
        <span>Data<wbr>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The DataSource name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The field name from the schema defined in the GraphQL API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The resolver type. Valid values are `UNIT` and `PIPELINE`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pipeline<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#resolverpipelineconfig">Resolver<wbr>Pipeline<wbr>Config<wbr>Args?</a></span>
    </dt>
    <dd>{{% md %}}The PipelineConfig. A `pipeline_config` block is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Template</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The request mapping template for UNIT resolver or 'before mapping template' for PIPELINE resolver.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Response<wbr>Template</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The response mapping template for UNIT resolver or 'after mapping template' for PIPELINE resolver.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type name from the schema defined in the GraphQL API.
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
    <dd>{{% md %}}The API ID for the GraphQL API.
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
        <span>Data<wbr>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The DataSource name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Field</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The field name from the schema defined in the GraphQL API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The resolver type. Valid values are `UNIT` and `PIPELINE`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pipeline<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#resolverpipelineconfig">*Resolver<wbr>Pipeline<wbr>Config</a></span>
    </dt>
    <dd>{{% md %}}The PipelineConfig. A `pipeline_config` block is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Request<wbr>Template</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The request mapping template for UNIT resolver or 'before mapping template' for PIPELINE resolver.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Response<wbr>Template</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The response mapping template for UNIT resolver or 'after mapping template' for PIPELINE resolver.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The type name from the schema defined in the GraphQL API.
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
    <dd>{{% md %}}The API ID for the GraphQL API.
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
        <span>data<wbr>Source</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The DataSource name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>field</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The field name from the schema defined in the GraphQL API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The resolver type. Valid values are `UNIT` and `PIPELINE`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pipeline<wbr>Config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#resolverpipelineconfig">Resolver<wbr>Pipeline<wbr>Config?</a></span>
    </dt>
    <dd>{{% md %}}The PipelineConfig. A `pipeline_config` block is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>request<wbr>Template</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The request mapping template for UNIT resolver or 'before mapping template' for PIPELINE resolver.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>response<wbr>Template</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The response mapping template for UNIT resolver or 'after mapping template' for PIPELINE resolver.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type name from the schema defined in the GraphQL API.
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
    <dd>{{% md %}}The API ID for the GraphQL API.
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
        <span>data_<wbr>source</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The DataSource name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>field</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The field name from the schema defined in the GraphQL API.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>kind</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The resolver type. Valid values are `UNIT` and `PIPELINE`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pipeline_<wbr>config</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#resolverpipelineconfig">Dict[Resolver<wbr>Pipeline<wbr>Config]</a></span>
    </dt>
    <dd>{{% md %}}The PipelineConfig. A `pipeline_config` block is documented below.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>request_<wbr>template</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The request mapping template for UNIT resolver or 'before mapping template' for PIPELINE resolver.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>response_<wbr>template</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The response mapping template for UNIT resolver or 'after mapping template' for PIPELINE resolver.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type name from the schema defined in the GraphQL API.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}










## Supporting Types

<h4>Resolver<wbr>Pipeline<wbr>Config</h4>
{{% choosable language nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ResolverPipelineConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ResolverPipelineConfig">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#ResolverPipelineConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#ResolverPipelineConfigOutput">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Functions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}The list of Function ID.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Functions</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}The list of Function ID.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>functions</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}The list of Function ID.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>functions</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}The list of Function ID.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}









<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-aws">https://github.com/pulumi/pulumi-aws</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    <dt>Notes</dt>
	<dd>This Pulumi package is based on the [`aws` Terraform Provider](https://github.com/terraform-providers/terraform-provider-aws).</dd>
</dl>

