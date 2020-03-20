
---
title: "GetProduct"
block_external_search_index: true
---
<style>
table td p { margin-top: 0; margin-bottom: 0; }
</style>

Use this data source to get the pricing information of all products in AWS.
This data source is only available in a us-east-1 or ap-south-1 provider.

## Example Usage

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = aws.pricing.getProduct({
    filters: [
        {
            field: "instanceType",
            value: "c5.xlarge",
        },
        {
            field: "operatingSystem",
            value: "Linux",
        },
        {
            field: "location",
            value: "US East (N. Virginia)",
        },
        {
            field: "preInstalledSw",
            value: "NA",
        },
        {
            field: "licenseModel",
            value: "No License required",
        },
        {
            field: "tenancy",
            value: "Shared",
        },
        {
            field: "capacitystatus",
            value: "Used",
        },
    ],
    serviceCode: "AmazonEC2",
});
```

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

const example = aws.pricing.getProduct({
    filters: [
        {
            field: "instanceType",
            value: "ds1.xlarge",
        },
        {
            field: "location",
            value: "US East (N. Virginia)",
        },
    ],
    serviceCode: "AmazonRedshift",
});
```

> This content is derived from https://github.com/terraform-providers/terraform-provider-aws/blob/master/website/docs/d/pricing_product.html.markdown.





## Using GetProduct

{{< langchoose csharp nojavascript >}}


<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getProduct<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/pricing/#GetProductArgs">GetProductArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/pulumi/#InvokeOptions">pulumi.InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/aws/pricing/#GetProductResult">GetProductResult</a></span>></span></code></pre></div>


<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_product(</span>filters=None<span class="p">, </span>service_code=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>


<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupProduct<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/pricing?tab=doc#LookupProductArgs">LookupProductArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">pulumi.InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/pricing?tab=doc#LookupProductResult">LookupProductResult</a></span>, error)</span></code></pre></div>


<div class="highlight">
<pre class="chroma">
<code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetProduct </span><span class="p">{</span>
    <span class="k">public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Pricing.GetProductResult.html">Pulumi.Aws.Pricing.GetProductResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Pricing.GetProductArgs.html">GetProductArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span>
<span class="p">}</span></code></pre>
</div>



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
            <td class="align-top">Filters</td>
            <td class="align-top">
                
                <code><a href="#getproductfilter">List&lt;Pulumi.<wbr>Aws.<wbr>Pricing.<wbr>Get<wbr>Product<wbr>Filter<wbr>Args&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of filters. Passed directly to the API (see GetProducts API reference). These filters must describe a single product, this resource will fail if more than one product is returned by the API.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Code</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The code of the service. Available service codes can be fetched using the DescribeServices pricing API call.
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
            <td class="align-top">Filters</td>
            <td class="align-top">
                
                <code><a href="#getproductfilter">[]Get<wbr>Product<wbr>Filter</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of filters. Passed directly to the API (see GetProducts API reference). These filters must describe a single product, this resource will fail if more than one product is returned by the API.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Code</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The code of the service. Available service codes can be fetched using the DescribeServices pricing API call.
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
            <td class="align-top">filters</td>
            <td class="align-top">
                
                <code><a href="#getproductfilter">pricing.<wbr>Get<wbr>Product<wbr>Filter[]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of filters. Passed directly to the API (see GetProducts API reference). These filters must describe a single product, this resource will fail if more than one product is returned by the API.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service<wbr>Code</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The code of the service. Available service codes can be fetched using the DescribeServices pricing API call.
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
            <td class="align-top">filters</td>
            <td class="align-top">
                
                <code><a href="#getproductfilter">List[Get<wbr>Product<wbr>Filter]</a></code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
A list of filters. Passed directly to the API (see GetProducts API reference). These filters must describe a single product, this resource will fail if more than one product is returned by the API.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service_<wbr>code</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The code of the service. Available service codes can be fetched using the DescribeServices pricing API call.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## GetProduct Result

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
            <td class="align-top">Filters</td>
            <td class="align-top">
                
                <code><a href="#getproductfilter">List&lt;Pulumi.<wbr>Aws.<wbr>Pricing.<wbr>Get<wbr>Product<wbr>Filter&gt;</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} id is the provider-assigned unique ID for this managed resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Result</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Set to the product returned from the API.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Code</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
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
            <td class="align-top">Filters</td>
            <td class="align-top">
                
                <code><a href="#getproductfilter">[]Get<wbr>Product<wbr>Filter</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} id is the provider-assigned unique ID for this managed resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Result</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Set to the product returned from the API.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Service<wbr>Code</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
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
            <td class="align-top">filters</td>
            <td class="align-top">
                
                <code><a href="#getproductfilter">pricing.<wbr>Get<wbr>Product<wbr>Filter[]</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} id is the provider-assigned unique ID for this managed resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">result</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} Set to the product returned from the API.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service<wbr>Code</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
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
            <td class="align-top">filters</td>
            <td class="align-top">
                
                <code><a href="#getproductfilter">List[Get<wbr>Product<wbr>Filter]</a></code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">id</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} id is the provider-assigned unique ID for this managed resource.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">result</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} Set to the product returned from the API.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">service_<wbr>code</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}}  {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}








## Supporting Types

#### GetProductFilter
{{% lang nodejs %}}
> See the <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/input/#GetProductFilter">input</a> and <a href="/docs/reference/pkg/nodejs/pulumi/aws/types/output/#GetProductFilter">output</a> API doc for this type.
{{% /lang %}}

{{% lang go %}}
> See the <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/pricing?tab=doc#GetProductFilterArgs">input</a> and <a href="https://pkg.go.dev/github.com/pulumi/pulumi-aws/sdk/go/aws/pricing?tab=doc#GetProductFilter">output</a> API doc for this type.
{{% /lang %}}

{{% lang csharp %}}
> See the <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Pricing.GetProductFilterArgs.html">input</a> and <a href="/docs/reference/pkg/dotnet/Pulumi.Aws/Pulumi.Aws.Pricing.GetProductFilter.html">output</a> API doc for this type.
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
            <td class="align-top">Field</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The product attribute name that you want to filter on.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The product attribute value that you want to filter on.
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
            <td class="align-top">Field</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The product attribute name that you want to filter on.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">Value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The product attribute value that you want to filter on.
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
            <td class="align-top">field</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The product attribute name that you want to filter on.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">value</td>
            <td class="align-top">
                
                <code>string</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The product attribute value that you want to filter on.
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
            <td class="align-top">field</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The product attribute name that you want to filter on.
 {{% /md %}}

            
            </td>
        </tr>
    
        <tr>
            <td class="align-top">value</td>
            <td class="align-top">
                
                <code>str</code>
            </td>
            <td class="align-top">{{% md %}} 
 (Required)
The product attribute value that you want to filter on.
 {{% /md %}}

            
            </td>
        </tr>
    
    </tbody>
</table>


{{% /lang %}}







