
---
title: "Resolver"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Provides an AppSync Resolver.

## Example Usage

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

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/appsync_resolver.html.markdown.



## Create a Resolver Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/appsync/#Resolver">Resolver</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/appsync/#ResolverArgs">ResolverArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Resolver</span><span class="p">(resource_name, opts=None, </span>api_id=None<span class="p">, </span>data_source=None<span class="p">, </span>field=None<span class="p">, </span>kind=None<span class="p">, </span>pipeline_config=None<span class="p">, </span>request_template=None<span class="p">, </span>response_template=None<span class="p">, </span>type=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewResolver<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#ResolverArgs">ResolverArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#Resolver">Resolver</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.Resolver.html">Resolver</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.ResolverArgs.html">ResolverArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a Resolver resource with the given unique name, arguments, and options.

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
The API ID for the GraphQL API.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Data<wbr>Source</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The DataSource name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Field</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The field name from the schema defined in the GraphQL API.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kind</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The resolver type. Valid values are `UNIT` and `PIPELINE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Pipeline<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#resolverpipelineconfig">Pulumi.<wbr>Aws.<wbr>Appsync.<wbr>Resolver<wbr>Pipeline<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The PipelineConfig. A `pipeline_config` block is documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Request<wbr>Template</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The request mapping template for UNIT resolver or &#39;before mapping template&#39; for PIPELINE resolver.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Response<wbr>Template</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The response mapping template for UNIT resolver or &#39;after mapping template&#39; for PIPELINE resolver.
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
The type name from the schema defined in the GraphQL API.
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
The API ID for the GraphQL API.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Data<wbr>Source</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The DataSource name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Field</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The field name from the schema defined in the GraphQL API.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kind</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The resolver type. Valid values are `UNIT` and `PIPELINE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Pipeline<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#resolverpipelineconfig">*appsync.<wbr>Resolver<wbr>Pipeline<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The PipelineConfig. A `pipeline_config` block is documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Request<wbr>Template</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The request mapping template for UNIT resolver or &#39;before mapping template&#39; for PIPELINE resolver.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Response<wbr>Template</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The response mapping template for UNIT resolver or &#39;after mapping template&#39; for PIPELINE resolver.
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
The type name from the schema defined in the GraphQL API.
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
The API ID for the GraphQL API.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">data<wbr>Source</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The DataSource name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">field</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The field name from the schema defined in the GraphQL API.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kind</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The resolver type. Valid values are `UNIT` and `PIPELINE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">pipeline<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#resolverpipelineconfig">appsync.<wbr>Resolver<wbr>Pipeline<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The PipelineConfig. A `pipeline_config` block is documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">request<wbr>Template</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The request mapping template for UNIT resolver or &#39;before mapping template&#39; for PIPELINE resolver.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">response<wbr>Template</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The response mapping template for UNIT resolver or &#39;after mapping template&#39; for PIPELINE resolver.
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
The type name from the schema defined in the GraphQL API.
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
The API ID for the GraphQL API.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">data_<wbr>source</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The DataSource name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">field</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The field name from the schema defined in the GraphQL API.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kind</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The resolver type. Valid values are `UNIT` and `PIPELINE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">pipeline_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#resolverpipelineconfig">Dict[Resolver<wbr>Pipeline<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The PipelineConfig. A `pipeline_config` block is documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">request_<wbr>template</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The request mapping template for UNIT resolver or &#39;before mapping template&#39; for PIPELINE resolver.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">response_<wbr>template</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The response mapping template for UNIT resolver or &#39;after mapping template&#39; for PIPELINE resolver.
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
The type name from the schema defined in the GraphQL API.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## Resolver Output Properties

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
            <td class="align-top">{{% md %}} The API ID for the GraphQL API.
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
            <td class="align-top">Data<wbr>Source</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The DataSource name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Field</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The field name from the schema defined in the GraphQL API.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kind</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The resolver type. Valid values are `UNIT` and `PIPELINE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Pipeline<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#resolverpipelineconfig">Pulumi.<wbr>Aws.<wbr>Appsync.<wbr>Resolver<wbr>Pipeline<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} The PipelineConfig. A `pipeline_config` block is documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Request<wbr>Template</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The request mapping template for UNIT resolver or &#39;before mapping template&#39; for PIPELINE resolver.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Response<wbr>Template</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The response mapping template for UNIT resolver or &#39;after mapping template&#39; for PIPELINE resolver.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The type name from the schema defined in the GraphQL API.
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
            <td class="align-top">{{% md %}} The API ID for the GraphQL API.
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
            <td class="align-top">Data<wbr>Source</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The DataSource name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Field</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The field name from the schema defined in the GraphQL API.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kind</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} The resolver type. Valid values are `UNIT` and `PIPELINE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Pipeline<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#resolverpipelineconfig">*appsync.<wbr>Resolver<wbr>Pipeline<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} The PipelineConfig. A `pipeline_config` block is documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Request<wbr>Template</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The request mapping template for UNIT resolver or &#39;before mapping template&#39; for PIPELINE resolver.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Response<wbr>Template</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The response mapping template for UNIT resolver or &#39;after mapping template&#39; for PIPELINE resolver.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The type name from the schema defined in the GraphQL API.
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
            <td class="align-top">{{% md %}} The API ID for the GraphQL API.
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
            <td class="align-top">data<wbr>Source</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The DataSource name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">field</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The field name from the schema defined in the GraphQL API.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kind</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} The resolver type. Valid values are `UNIT` and `PIPELINE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">pipeline<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#resolverpipelineconfig">appsync.<wbr>Resolver<wbr>Pipeline<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} The PipelineConfig. A `pipeline_config` block is documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">request<wbr>Template</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The request mapping template for UNIT resolver or &#39;before mapping template&#39; for PIPELINE resolver.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">response<wbr>Template</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The response mapping template for UNIT resolver or &#39;after mapping template&#39; for PIPELINE resolver.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The type name from the schema defined in the GraphQL API.
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
            <td class="align-top">{{% md %}} The API ID for the GraphQL API.
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
            <td class="align-top">data_<wbr>source</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The DataSource name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">field</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The field name from the schema defined in the GraphQL API.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kind</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The resolver type. Valid values are `UNIT` and `PIPELINE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">pipeline_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#resolverpipelineconfig">Dict[Resolver<wbr>Pipeline<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} The PipelineConfig. A `pipeline_config` block is documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">request_<wbr>template</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The request mapping template for UNIT resolver or &#39;before mapping template&#39; for PIPELINE resolver.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">response_<wbr>template</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The response mapping template for UNIT resolver or &#39;after mapping template&#39; for PIPELINE resolver.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">type</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The type name from the schema defined in the GraphQL API.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing Resolver Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/appsync/#ResolverState">ResolverState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/appsync/#Resolver">Resolver</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>api_id=None<span class="p">, </span>arn=None<span class="p">, </span>data_source=None<span class="p">, </span>field=None<span class="p">, </span>kind=None<span class="p">, </span>pipeline_config=None<span class="p">, </span>request_template=None<span class="p">, </span>response_template=None<span class="p">, </span>type=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetResolver<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#ResolverState">ResolverState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#Resolver">Resolver</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.Resolver.html">Resolver</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.ResolverState.html">ResolverState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing Resolver resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
The API ID for the GraphQL API.
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
            <td class="align-top">Data<wbr>Source</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The DataSource name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Field</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The field name from the schema defined in the GraphQL API.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kind</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The resolver type. Valid values are `UNIT` and `PIPELINE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Pipeline<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#resolverpipelineconfig">Pulumi.<wbr>Aws.<wbr>Appsync.<wbr>Resolver<wbr>Pipeline<wbr>Config<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The PipelineConfig. A `pipeline_config` block is documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Request<wbr>Template</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The request mapping template for UNIT resolver or &#39;before mapping template&#39; for PIPELINE resolver.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Response<wbr>Template</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The response mapping template for UNIT resolver or &#39;after mapping template&#39; for PIPELINE resolver.
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
The type name from the schema defined in the GraphQL API.
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
The API ID for the GraphQL API.
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
            <td class="align-top">Data<wbr>Source</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The DataSource name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Field</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The field name from the schema defined in the GraphQL API.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Kind</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The resolver type. Valid values are `UNIT` and `PIPELINE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Pipeline<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#resolverpipelineconfig">*appsync.<wbr>Resolver<wbr>Pipeline<wbr>Config</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The PipelineConfig. A `pipeline_config` block is documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Request<wbr>Template</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The request mapping template for UNIT resolver or &#39;before mapping template&#39; for PIPELINE resolver.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Response<wbr>Template</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The response mapping template for UNIT resolver or &#39;after mapping template&#39; for PIPELINE resolver.
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
The type name from the schema defined in the GraphQL API.
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
The API ID for the GraphQL API.
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
            <td class="align-top">data<wbr>Source</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The DataSource name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">field</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The field name from the schema defined in the GraphQL API.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kind</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The resolver type. Valid values are `UNIT` and `PIPELINE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">pipeline<wbr>Config</td>
            <td class="align-top">
                
                <code><a href="#resolverpipelineconfig">appsync.<wbr>Resolver<wbr>Pipeline<wbr>Config?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The PipelineConfig. A `pipeline_config` block is documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">request<wbr>Template</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The request mapping template for UNIT resolver or &#39;before mapping template&#39; for PIPELINE resolver.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">response<wbr>Template</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The response mapping template for UNIT resolver or &#39;after mapping template&#39; for PIPELINE resolver.
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
The type name from the schema defined in the GraphQL API.
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
The API ID for the GraphQL API.
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
            <td class="align-top">data_<wbr>source</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The DataSource name.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">field</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The field name from the schema defined in the GraphQL API.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">kind</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The resolver type. Valid values are `UNIT` and `PIPELINE`.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">pipeline_<wbr>config</td>
            <td class="align-top">
                
                <code><a href="#resolverpipelineconfig">Dict[Resolver<wbr>Pipeline<wbr>Config]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The PipelineConfig. A `pipeline_config` block is documented below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">request_<wbr>template</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The request mapping template for UNIT resolver or &#39;before mapping template&#39; for PIPELINE resolver.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">response_<wbr>template</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The response mapping template for UNIT resolver or &#39;after mapping template&#39; for PIPELINE resolver.
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
The type name from the schema defined in the GraphQL API.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### ResolverPipelineConfig
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#ResolverPipelineConfig">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#ResolverPipelineConfig">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#ResolverPipelineConfigArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/appsync?tab=doc#ResolverPipelineConfigOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.ResolverPipelineConfigArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Appsync.ResolverPipelineConfig.html">output</a> API doc for this type.
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
            <td class="align-top">Functions</td>
            <td class="align-top">
                
                <code>List&lt;string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
            <td class="align-top">Functions</td>
            <td class="align-top">
                
                <code>[]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
            <td class="align-top">functions</td>
            <td class="align-top">
                
                <code>string[]?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
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
            <td class="align-top">functions</td>
            <td class="align-top">
                
                <code>List[str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







