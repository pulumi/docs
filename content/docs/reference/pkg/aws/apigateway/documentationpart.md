
---
title: "DocumentationPart"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Provides a settings of an API Gateway Documentation Part.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const exampleRestApi = new aws.apigateway.RestApi("example", {});
const exampleDocumentationPart = new aws.apigateway.DocumentationPart("example", {
    location: {
        method: "GET",
        path: "/example",
        type: "METHOD",
    },
    properties: "{\"description\":\"Example description\"}",
    restApiId: exampleRestApi.id,
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_documentation_part.html.markdown.



## Create a DocumentationPart Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/apigateway/#DocumentationPart">DocumentationPart</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/apigateway/#DocumentationPartArgs">DocumentationPartArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">DocumentationPart</span><span class="p">(resource_name, opts=None, </span>location=None<span class="p">, </span>properties=None<span class="p">, </span>rest_api_id=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewDocumentationPart<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#DocumentationPartArgs">DocumentationPartArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#DocumentationPart">DocumentationPart</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Apigateway.DocumentationPart.html">DocumentationPart</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Apigateway.DocumentationPartArgs.html">DocumentationPartArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a DocumentationPart resource with the given unique name, arguments, and options.

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
            <td class="align-top">Location</td>
            <td class="align-top">
                
                <code><a href="#documentationpartlocation">Pulumi.<wbr>Aws.<wbr>Apigateway.<wbr>Documentation<wbr>Part<wbr>Location<wbr>Args</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The location of the targeted API entity of the to-be-created documentation part. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Properties</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A content map of API-specific key-value pairs describing the targeted API entity. The map must be encoded as a JSON string, e.g., &#34;{ \&#34;description\&#34;: \&#34;The API does ...\&#34; }&#34;. Only Swagger-compliant key-value pairs can be exported and, hence, published.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rest<wbr>Api<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the associated Rest API
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
            <td class="align-top">Location</td>
            <td class="align-top">
                
                <code><a href="#documentationpartlocation">apigateway.<wbr>Documentation<wbr>Part<wbr>Location</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The location of the targeted API entity of the to-be-created documentation part. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Properties</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A content map of API-specific key-value pairs describing the targeted API entity. The map must be encoded as a JSON string, e.g., &#34;{ \&#34;description\&#34;: \&#34;The API does ...\&#34; }&#34;. Only Swagger-compliant key-value pairs can be exported and, hence, published.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rest<wbr>Api<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the associated Rest API
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
            <td class="align-top">location</td>
            <td class="align-top">
                
                <code><a href="#documentationpartlocation">apigateway.<wbr>Documentation<wbr>Part<wbr>Location</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The location of the targeted API entity of the to-be-created documentation part. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">properties</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A content map of API-specific key-value pairs describing the targeted API entity. The map must be encoded as a JSON string, e.g., &#34;{ \&#34;description\&#34;: \&#34;The API does ...\&#34; }&#34;. Only Swagger-compliant key-value pairs can be exported and, hence, published.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rest<wbr>Api<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the associated Rest API
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
            <td class="align-top">location</td>
            <td class="align-top">
                
                <code><a href="#documentationpartlocation">Dict[documentation_<wbr>part_<wbr>location]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The location of the targeted API entity of the to-be-created documentation part. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">properties</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A content map of API-specific key-value pairs describing the targeted API entity. The map must be encoded as a JSON string, e.g., &#34;{ \&#34;description\&#34;: \&#34;The API does ...\&#34; }&#34;. Only Swagger-compliant key-value pairs can be exported and, hence, published.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rest_<wbr>api_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the associated Rest API
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## DocumentationPart Output Properties

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
            <td class="align-top">Location</td>
            <td class="align-top">
                
                <code><a href="#documentationpartlocation">Pulumi.<wbr>Aws.<wbr>Apigateway.<wbr>Documentation<wbr>Part<wbr>Location</a></code>
            </td>
            <td class="align-top">{{% md %}} The location of the targeted API entity of the to-be-created documentation part. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Properties</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A content map of API-specific key-value pairs describing the targeted API entity. The map must be encoded as a JSON string, e.g., &#34;{ \&#34;description\&#34;: \&#34;The API does ...\&#34; }&#34;. Only Swagger-compliant key-value pairs can be exported and, hence, published.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rest<wbr>Api<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the associated Rest API
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
            <td class="align-top">Location</td>
            <td class="align-top">
                
                <code><a href="#documentationpartlocation">apigateway.<wbr>Documentation<wbr>Part<wbr>Location</a></code>
            </td>
            <td class="align-top">{{% md %}} The location of the targeted API entity of the to-be-created documentation part. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Properties</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A content map of API-specific key-value pairs describing the targeted API entity. The map must be encoded as a JSON string, e.g., &#34;{ \&#34;description\&#34;: \&#34;The API does ...\&#34; }&#34;. Only Swagger-compliant key-value pairs can be exported and, hence, published.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rest<wbr>Api<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the associated Rest API
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
            <td class="align-top">location</td>
            <td class="align-top">
                
                <code><a href="#documentationpartlocation">apigateway.<wbr>Documentation<wbr>Part<wbr>Location</a></code>
            </td>
            <td class="align-top">{{% md %}} The location of the targeted API entity of the to-be-created documentation part. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">properties</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} A content map of API-specific key-value pairs describing the targeted API entity. The map must be encoded as a JSON string, e.g., &#34;{ \&#34;description\&#34;: \&#34;The API does ...\&#34; }&#34;. Only Swagger-compliant key-value pairs can be exported and, hence, published.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rest<wbr>Api<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the associated Rest API
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
            <td class="align-top">location</td>
            <td class="align-top">
                
                <code><a href="#documentationpartlocation">Dict[documentation_<wbr>part_<wbr>location]</a></code>
            </td>
            <td class="align-top">{{% md %}} The location of the targeted API entity of the to-be-created documentation part. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">properties</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} A content map of API-specific key-value pairs describing the targeted API entity. The map must be encoded as a JSON string, e.g., &#34;{ \&#34;description\&#34;: \&#34;The API does ...\&#34; }&#34;. Only Swagger-compliant key-value pairs can be exported and, hence, published.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rest_<wbr>api_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the associated Rest API
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing DocumentationPart Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/apigateway/#DocumentationPartState">DocumentationPartState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/apigateway/#DocumentationPart">DocumentationPart</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>location=None<span class="p">, </span>properties=None<span class="p">, </span>rest_api_id=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetDocumentationPart<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#DocumentationPartState">DocumentationPartState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#DocumentationPart">DocumentationPart</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Apigateway.DocumentationPart.html">DocumentationPart</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Apigateway.DocumentationPartState.html">DocumentationPartState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing DocumentationPart resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Location</td>
            <td class="align-top">
                
                <code><a href="#documentationpartlocation">Pulumi.<wbr>Aws.<wbr>Apigateway.<wbr>Documentation<wbr>Part<wbr>Location<wbr>Args?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The location of the targeted API entity of the to-be-created documentation part. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Properties</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A content map of API-specific key-value pairs describing the targeted API entity. The map must be encoded as a JSON string, e.g., &#34;{ \&#34;description\&#34;: \&#34;The API does ...\&#34; }&#34;. Only Swagger-compliant key-value pairs can be exported and, hence, published.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rest<wbr>Api<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the associated Rest API
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
            <td class="align-top">Location</td>
            <td class="align-top">
                
                <code><a href="#documentationpartlocation">*apigateway.<wbr>Documentation<wbr>Part<wbr>Location</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The location of the targeted API entity of the to-be-created documentation part. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Properties</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A content map of API-specific key-value pairs describing the targeted API entity. The map must be encoded as a JSON string, e.g., &#34;{ \&#34;description\&#34;: \&#34;The API does ...\&#34; }&#34;. Only Swagger-compliant key-value pairs can be exported and, hence, published.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rest<wbr>Api<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the associated Rest API
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
            <td class="align-top">location</td>
            <td class="align-top">
                
                <code><a href="#documentationpartlocation">apigateway.<wbr>Documentation<wbr>Part<wbr>Location?</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The location of the targeted API entity of the to-be-created documentation part. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">properties</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A content map of API-specific key-value pairs describing the targeted API entity. The map must be encoded as a JSON string, e.g., &#34;{ \&#34;description\&#34;: \&#34;The API does ...\&#34; }&#34;. Only Swagger-compliant key-value pairs can be exported and, hence, published.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rest<wbr>Api<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the associated Rest API
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
            <td class="align-top">location</td>
            <td class="align-top">
                
                <code><a href="#documentationpartlocation">Dict[documentation_<wbr>part_<wbr>location]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The location of the targeted API entity of the to-be-created documentation part. See below.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">properties</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A content map of API-specific key-value pairs describing the targeted API entity. The map must be encoded as a JSON string, e.g., &#34;{ \&#34;description\&#34;: \&#34;The API does ...\&#34; }&#34;. Only Swagger-compliant key-value pairs can be exported and, hence, published.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rest_<wbr>api_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the associated Rest API
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}










## Supporting Types

#### DocumentationPartLocation
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#DocumentationPartLocation">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#DocumentationPartLocation">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#DocumentationPartLocationArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#DocumentationPartLocationOutput">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Apigateway.DocumentationPartLocationArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Apigateway.DocumentationPartLocation.html">output</a> API doc for this type.
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
            <td class="align-top">Method</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The HTTP verb of a method. The default value is `*` for any method.
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
The name of the targeted API entity.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Path</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The URL path of the target. The default value is `/` for the root resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status<wbr>Code</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The HTTP status code of a response. The default value is `*` for any status code.
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
The type of API entity to which the documentation content applies. e.g. `API`, `METHOD` or `REQUEST_BODY`
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
            <td class="align-top">Method</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The HTTP verb of a method. The default value is `*` for any method.
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
The name of the targeted API entity.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Path</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The URL path of the target. The default value is `/` for the root resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status<wbr>Code</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The HTTP status code of a response. The default value is `*` for any status code.
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
The type of API entity to which the documentation content applies. e.g. `API`, `METHOD` or `REQUEST_BODY`
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
            <td class="align-top">method</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The HTTP verb of a method. The default value is `*` for any method.
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
The name of the targeted API entity.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">path</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The URL path of the target. The default value is `/` for the root resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status<wbr>Code</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The HTTP status code of a response. The default value is `*` for any status code.
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
The type of API entity to which the documentation content applies. e.g. `API`, `METHOD` or `REQUEST_BODY`
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
            <td class="align-top">method</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The HTTP verb of a method. The default value is `*` for any method.
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
The name of the targeted API entity.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">path</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The URL path of the target. The default value is `/` for the root resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status_<wbr>code</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The HTTP status code of a response. The default value is `*` for any status code.
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
The type of API entity to which the documentation content applies. e.g. `API`, `METHOD` or `REQUEST_BODY`
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







