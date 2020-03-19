
---
title: "MethodResponse"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Provides an HTTP Method Response for an API Gateway Resource.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const myDemoAPI = new aws.apigateway.RestApi("MyDemoAPI", {
    description: "This is my API for demonstration purposes",
});
const myDemoResource = new aws.apigateway.Resource("MyDemoResource", {
    parentId: myDemoAPI.rootResourceId,
    pathPart: "mydemoresource",
    restApi: myDemoAPI.id,
});
const myDemoMethod = new aws.apigateway.Method("MyDemoMethod", {
    authorization: "NONE",
    httpMethod: "GET",
    resourceId: myDemoResource.id,
    restApi: myDemoAPI.id,
});
const myDemoIntegration = new aws.apigateway.Integration("MyDemoIntegration", {
    httpMethod: myDemoMethod.httpMethod,
    resourceId: myDemoResource.id,
    restApi: myDemoAPI.id,
    type: "MOCK",
});
const response200 = new aws.apigateway.MethodResponse("response_200", {
    httpMethod: myDemoMethod.httpMethod,
    resourceId: myDemoResource.id,
    restApi: myDemoAPI.id,
    statusCode: "200",
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/r/api_gateway_method_response.html.markdown.



## Create a MethodResponse Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/apigateway/#MethodResponse">MethodResponse</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/apigateway/#MethodResponseArgs">MethodResponseArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">MethodResponse</span><span class="p">(resource_name, opts=None, </span>http_method=None<span class="p">, </span>resource_id=None<span class="p">, </span>response_models=None<span class="p">, </span>response_parameters=None<span class="p">, </span>rest_api=None<span class="p">, </span>status_code=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewMethodResponse<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#MethodResponseArgs">MethodResponseArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#MethodResponse">MethodResponse</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Apigateway.MethodResponse.html">MethodResponse</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Apigateway.MethodResponseArgs.html">MethodResponseArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Creates a MethodResponse resource with the given unique name, arguments, and options.

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
            <td class="align-top">Http<wbr>Method</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The HTTP Method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Resource<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The API resource ID
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Response<wbr>Models</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of the API models used for the response&#39;s content type
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Response<wbr>Parameters</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, bool&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of response parameters that can be sent to the caller.
For example: `response_parameters = { &#34;method.response.header.X-Some-Header&#34; = true }`
would define that the header `X-Some-Header` can be provided on the response.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rest<wbr>Api</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the associated REST API
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status<wbr>Code</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The HTTP status code
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
            <td class="align-top">Http<wbr>Method</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The HTTP Method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Resource<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The API resource ID
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Response<wbr>Models</td>
            <td class="align-top">
                
                <code>map[string]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of the API models used for the response&#39;s content type
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Response<wbr>Parameters</td>
            <td class="align-top">
                
                <code>map[string]bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of response parameters that can be sent to the caller.
For example: `response_parameters = { &#34;method.response.header.X-Some-Header&#34; = true }`
would define that the header `X-Some-Header` can be provided on the response.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rest<wbr>Api</td>
            <td class="align-top">
                
                <code>interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the associated REST API
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status<wbr>Code</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The HTTP status code
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
            <td class="align-top">http<wbr>Method</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The HTTP Method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">resource<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The API resource ID
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">response<wbr>Models</td>
            <td class="align-top">
                
                <code>{[key: string]: string}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of the API models used for the response&#39;s content type
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">response<wbr>Parameters</td>
            <td class="align-top">
                
                <code>{[key: string]: boolean}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of response parameters that can be sent to the caller.
For example: `response_parameters = { &#34;method.response.header.X-Some-Header&#34; = true }`
would define that the header `X-Some-Header` can be provided on the response.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rest<wbr>Api</td>
            <td class="align-top">
                
                <code>string | Rest<wbr>Api</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the associated REST API
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status<wbr>Code</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The HTTP status code
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
            <td class="align-top">http_<wbr>method</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The HTTP Method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">resource_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The API resource ID
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">response_<wbr>models</td>
            <td class="align-top">
                
                <code>Dict[str, str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of the API models used for the response&#39;s content type
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">response_<wbr>parameters</td>
            <td class="align-top">
                
                <code>Dict[str, Boolean]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of response parameters that can be sent to the caller.
For example: `response_parameters = { &#34;method.response.header.X-Some-Header&#34; = true }`
would define that the header `X-Some-Header` can be provided on the response.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rest_<wbr>api</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The ID of the associated REST API
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status_<wbr>code</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The HTTP status code
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







## MethodResponse Output Properties

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
            <td class="align-top">Http<wbr>Method</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The HTTP Method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Resource<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The API resource ID
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Response<wbr>Models</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A map of the API models used for the response&#39;s content type
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Response<wbr>Parameters</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, bool&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} A map of response parameters that can be sent to the caller.
For example: `response_parameters = { &#34;method.response.header.X-Some-Header&#34; = true }`
would define that the header `X-Some-Header` can be provided on the response.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rest<wbr>Api</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the associated REST API
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status<wbr>Code</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The HTTP status code
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
            <td class="align-top">Http<wbr>Method</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The HTTP Method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Resource<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The API resource ID
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Response<wbr>Models</td>
            <td class="align-top">
                
                <code>map[string]string</code>
            </td>
            <td class="align-top">{{% md %}} A map of the API models used for the response&#39;s content type
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Response<wbr>Parameters</td>
            <td class="align-top">
                
                <code>map[string]bool</code>
            </td>
            <td class="align-top">{{% md %}} A map of response parameters that can be sent to the caller.
For example: `response_parameters = { &#34;method.response.header.X-Some-Header&#34; = true }`
would define that the header `X-Some-Header` can be provided on the response.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rest<wbr>Api</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the associated REST API
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Status<wbr>Code</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The HTTP status code
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
            <td class="align-top">http<wbr>Method</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The HTTP Method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">resource<wbr>Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The API resource ID
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">response<wbr>Models</td>
            <td class="align-top">
                
                <code>{[key: string]: string}?</code>
            </td>
            <td class="align-top">{{% md %}} A map of the API models used for the response&#39;s content type
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">response<wbr>Parameters</td>
            <td class="align-top">
                
                <code>{[key: string]: boolean}?</code>
            </td>
            <td class="align-top">{{% md %}} A map of response parameters that can be sent to the caller.
For example: `response_parameters = { &#34;method.response.header.X-Some-Header&#34; = true }`
would define that the header `X-Some-Header` can be provided on the response.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rest<wbr>Api</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the associated REST API
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status<wbr>Code</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} The HTTP status code
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
            <td class="align-top">http_<wbr>method</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The HTTP Method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">resource_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The API resource ID
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">response_<wbr>models</td>
            <td class="align-top">
                
                <code>Dict[str, str]</code>
            </td>
            <td class="align-top">{{% md %}} A map of the API models used for the response&#39;s content type
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">response_<wbr>parameters</td>
            <td class="align-top">
                
                <code>Dict[str, Boolean]</code>
            </td>
            <td class="align-top">{{% md %}} A map of response parameters that can be sent to the caller.
For example: `response_parameters = { &#34;method.response.header.X-Some-Header&#34; = true }`
would define that the header `X-Some-Header` can be provided on the response.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rest_<wbr>api</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The ID of the associated REST API
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">status_<wbr>code</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} The HTTP status code
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Look up an Existing MethodResponse Resource

{{< langchoose csharp nojavascript >}}

<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">pulumi.Input&lt;pulumi.ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/apigateway/#MethodResponseState">MethodResponseState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/apigateway/#MethodResponse">MethodResponse</a></span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>http_method=None<span class="p">, </span>resource_id=None<span class="p">, </span>response_models=None<span class="p">, </span>response_parameters=None<span class="p">, </span>rest_api=None<span class="p">, </span>status_code=None<span class="p">, __props__=None);</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetMethodResponse<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">pulumi.IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#MethodResponseState">MethodResponseState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/apigateway?tab=doc#MethodResponse">MethodResponse</a></span>, error)</span></code></pre></div>

<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Apigateway.MethodResponse.html">MethodResponse</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Pulumi.Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Apigateway.MethodResponseState.html">MethodResponseState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">Pulumi.CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>

Get an existing MethodResponse resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

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
            <td class="align-top">Http<wbr>Method</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The HTTP Method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Resource<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The API resource ID
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Response<wbr>Models</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, string&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of the API models used for the response&#39;s content type
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Response<wbr>Parameters</td>
            <td class="align-top">
                
                <code>Dictionary&lt;string, bool&gt;?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of response parameters that can be sent to the caller.
For example: `response_parameters = { &#34;method.response.header.X-Some-Header&#34; = true }`
would define that the header `X-Some-Header` can be provided on the response.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rest<wbr>Api</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the associated REST API
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
The HTTP status code
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
            <td class="align-top">Http<wbr>Method</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The HTTP Method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Resource<wbr>Id</td>
            <td class="align-top">
                
                <code>*string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The API resource ID
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Response<wbr>Models</td>
            <td class="align-top">
                
                <code>map[string]string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of the API models used for the response&#39;s content type
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Response<wbr>Parameters</td>
            <td class="align-top">
                
                <code>map[string]bool</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of response parameters that can be sent to the caller.
For example: `response_parameters = { &#34;method.response.header.X-Some-Header&#34; = true }`
would define that the header `X-Some-Header` can be provided on the response.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Rest<wbr>Api</td>
            <td class="align-top">
                
                <code>interface{}</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the associated REST API
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
The HTTP status code
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
            <td class="align-top">http<wbr>Method</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The HTTP Method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">resource<wbr>Id</td>
            <td class="align-top">
                
                <code>string?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The API resource ID
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">response<wbr>Models</td>
            <td class="align-top">
                
                <code>{[key: string]: string}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of the API models used for the response&#39;s content type
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">response<wbr>Parameters</td>
            <td class="align-top">
                
                <code>{[key: string]: boolean}?</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of response parameters that can be sent to the caller.
For example: `response_parameters = { &#34;method.response.header.X-Some-Header&#34; = true }`
would define that the header `X-Some-Header` can be provided on the response.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rest<wbr>Api</td>
            <td class="align-top">
                
                <code>string | Rest<wbr>Api</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the associated REST API
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
The HTTP status code
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
            <td class="align-top">http_<wbr>method</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The HTTP Method (`GET`, `POST`, `PUT`, `DELETE`, `HEAD`, `OPTIONS`, `ANY`)
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">resource_<wbr>id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The API resource ID
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">response_<wbr>models</td>
            <td class="align-top">
                
                <code>Dict[str, str]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of the API models used for the response&#39;s content type
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">response_<wbr>parameters</td>
            <td class="align-top">
                
                <code>Dict[str, Boolean]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
A map of response parameters that can be sent to the caller.
For example: `response_parameters = { &#34;method.response.header.X-Some-Header&#34; = true }`
would define that the header `X-Some-Header` can be provided on the response.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">rest_<wbr>api</td>
            <td class="align-top">
                
                <code>Dict[str, Any]</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Optional)
The ID of the associated REST API
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
The HTTP status code
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}









