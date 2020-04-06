
---
title: "GetProducts"
block_external_search_index: true
---



This data source provides the Market product items of Alibaba Cloud.

> **NOTE:** Available in 1.64.0+

> This content is derived from https://github.com/terraform-providers/terraform-provider-alicloud/blob/master/website/docs/d/market_products.html.markdown.





## Using GetProducts

{{< chooser language "javascript,typescript,python,go,csharp" / >}}


{{% choosable language typescript %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">function </span>getProducts<span class="p">(</span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/marketplace/#GetProductsArgs">GetProductsArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#InvokeOptions">InvokeOptions</a></span><span class="p">): Promise&lt;<span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/marketplace/#GetProductsResult">GetProductsResult</a></span>></span></code></pre></div>
{{% /choosable %}}


{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">function </span> get_products(</span>category_id=None<span class="p">, </span>ids=None<span class="p">, </span>name_regex=None<span class="p">, </span>output_file=None<span class="p">, </span>product_type=None<span class="p">, </span>search_term=None<span class="p">, </span>sort=None<span class="p">, </span>suggested_price=None<span class="p">, </span>supplier_id=None<span class="p">, </span>supplier_name_keyword=None<span class="p">, </span>opts=None<span class="p">)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>LookupProducts<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/marketplace?tab=doc#LookupProductsArgs">LookupProductsArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#InvokeOption">InvokeOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/marketplace?tab=doc#LookupProductsResult">LookupProductsResult</a></span>, error)</span></code></pre></div>
{{% /choosable %}}


{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static class </span><span class="nx">GetProducts </span><span class="p">{</span><span class="k">
    public static </span>Task&lt;<span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Marketplace.GetProductsResult.html">GetProductsResult</a></span>> <span class="p">InvokeAsync(</span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.MarketPlace.GetProductsArgs.html">GetProductsArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.InvokeOptions.html">InvokeOptions</a></span>? <span class="nx">opts = null<span class="p">)</span><span class="p">
}</span></code></pre></div>
{{% /choosable %}}



The following arguments are supported:



{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Category<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Category ID of products. For more information, see [DescribeProducts](https://help.aliyun.com/document_detail/89834.htm). 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string>?</span>
    </dt>
    <dd>{{% md %}}A list of product code.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A regex string to apply to the product name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Product<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of products, Valid values: `APP`, `SERVICE`, `MIRROR`, `DOWNLOAD` and `API_SERVICE`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Search<wbr>Term</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Search term in this query.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sort</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}This field determines how to sort the filtered results, Valid values: `user_count-desc`, `created_on-desc`, `price-desc` and `score-desc`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Suggested<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}The suggested price of the product.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Supplier<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The supplier id of the product.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Supplier<wbr>Name<wbr>Keyword</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The supplier name keyword of the product.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Category<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The Category ID of products. For more information, see [DescribeProducts](https://help.aliyun.com/document_detail/89834.htm). 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of product code.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}A regex string to apply to the product name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Product<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The type of products, Valid values: `APP`, `SERVICE`, `MIRROR`, `DOWNLOAD` and `API_SERVICE`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Search<wbr>Term</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Search term in this query.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Sort</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}This field determines how to sort the filtered results, Valid values: `user_count-desc`, `created_on-desc`, `price-desc` and `score-desc`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Suggested<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}The suggested price of the product.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Supplier<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The supplier id of the product.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Supplier<wbr>Name<wbr>Keyword</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The supplier name keyword of the product.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>category<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The Category ID of products. For more information, see [DescribeProducts](https://help.aliyun.com/document_detail/89834.htm). 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]?</span>
    </dt>
    <dd>{{% md %}}A list of product code.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}A regex string to apply to the product name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>product<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The type of products, Valid values: `APP`, `SERVICE`, `MIRROR`, `DOWNLOAD` and `API_SERVICE`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>search<wbr>Term</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Search term in this query.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sort</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}This field determines how to sort the filtered results, Valid values: `user_count-desc`, `created_on-desc`, `price-desc` and `score-desc`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>suggested<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The suggested price of the product.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>supplier<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The supplier id of the product.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>supplier<wbr>Name<wbr>Keyword</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The supplier name keyword of the product.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>category_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The Category ID of products. For more information, see [DescribeProducts](https://help.aliyun.com/document_detail/89834.htm). 
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of product code.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>name_<wbr>regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}A regex string to apply to the product name.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>output_<wbr>file</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>product_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The type of products, Valid values: `APP`, `SERVICE`, `MIRROR`, `DOWNLOAD` and `API_SERVICE`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>search_<wbr>term</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Search term in this query.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>sort</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}This field determines how to sort the filtered results, Valid values: `user_count-desc`, `created_on-desc`, `price-desc` and `score-desc`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>suggested_<wbr>price</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The suggested price of the product.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>supplier_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The supplier id of the product.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>supplier_<wbr>name_<wbr>keyword</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The supplier name keyword of the product.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## GetProducts Result

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Category<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The category id of the product.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List<string></span>
    </dt>
    <dd>{{% md %}}A list of product codes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Product<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Products</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getproductsproduct">List&lt;Get<wbr>Products<wbr>Product&gt;</a></span>
    </dt>
    <dd>{{% md %}}A list of products. Each element contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Search<wbr>Term</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sort</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Suggested<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">double?</span>
    </dt>
    <dd>{{% md %}}The suggested price of the product.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Supplier<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The supplier id of the product.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Supplier<wbr>Name<wbr>Keyword</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Category<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The category id of the product.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">[]string</span>
    </dt>
    <dd>{{% md %}}A list of product codes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Product<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Products</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getproductsproduct">[]Get<wbr>Products<wbr>Product</a></span>
    </dt>
    <dd>{{% md %}}A list of products. Each element contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Search<wbr>Term</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Sort</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Suggested<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">*float64</span>
    </dt>
    <dd>{{% md %}}The suggested price of the product.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Supplier<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The supplier id of the product.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Supplier<wbr>Name<wbr>Keyword</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>category<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The category id of the product.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">string[]</span>
    </dt>
    <dd>{{% md %}}A list of product codes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name<wbr>Regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>output<wbr>File</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>product<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>products</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getproductsproduct">Get<wbr>Products<wbr>Product[]</a></span>
    </dt>
    <dd>{{% md %}}A list of products. Each element contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>search<wbr>Term</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sort</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>suggested<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The suggested price of the product.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>supplier<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The supplier id of the product.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>supplier<wbr>Name<wbr>Keyword</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>category_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The category id of the product.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}id is the provider-assigned unique ID for this managed resource.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>ids</span>
        <span class="property-indicator"></span>
        <span class="property-type">List[str]</span>
    </dt>
    <dd>{{% md %}}A list of product codes.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>name_<wbr>regex</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>output_<wbr>file</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>product_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>products</span>
        <span class="property-indicator"></span>
        <span class="property-type"><a href="#getproductsproduct">List[Get<wbr>Products<wbr>Product]</a></span>
    </dt>
    <dd>{{% md %}}A list of products. Each element contains the following attributes:
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>search_<wbr>term</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>sort</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>suggested_<wbr>price</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The suggested price of the product.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>supplier_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The supplier id of the product.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>supplier_<wbr>name_<wbr>keyword</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Supporting Types

<h4>Get<wbr>Products<wbr>Product</h4>
{{% choosable language nodejs %}}
> See the   <a href="/docs/reference/pkg/nodejs/pulumi/alicloud/types/output/#GetProductsProduct">output</a> API doc for this type.
{{% /choosable %}}

{{% choosable language go %}}
> See the   <a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/marketplace?tab=doc#GetProductsProduct">output</a> API doc for this type.
{{% /choosable %}}




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Category<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The Category ID of products. For more information, see [DescribeProducts](https://help.aliyun.com/document_detail/89834.htm). 
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The code of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Delivery<wbr>Date</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The delivery date of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Delivery<wbr>Way</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The delivery way of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Image<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The image URL of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Operation<wbr>System</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The operation system of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Score</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The rating information of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Short<wbr>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The short description of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Suggested<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The suggested price of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Supplier<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The supplier id of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Supplier<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The supplier name of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The tags of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Target<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The detail page URL of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Warranty<wbr>Date</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The warranty date of the product.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>Category<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The Category ID of products. For more information, see [DescribeProducts](https://help.aliyun.com/document_detail/89834.htm). 
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The code of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Delivery<wbr>Date</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The delivery date of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Delivery<wbr>Way</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The delivery way of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Image<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The image URL of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Operation<wbr>System</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The operation system of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Score</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The rating information of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Short<wbr>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The short description of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Suggested<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The suggested price of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Supplier<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">int</span>
    </dt>
    <dd>{{% md %}}The supplier id of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Supplier<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The supplier name of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The tags of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Target<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The detail page URL of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Warranty<wbr>Date</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The warranty date of the product.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>category<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The Category ID of products. For more information, see [DescribeProducts](https://help.aliyun.com/document_detail/89834.htm). 
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The code of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>delivery<wbr>Date</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The delivery date of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>delivery<wbr>Way</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The delivery way of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>image<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The image URL of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The name of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>operation<wbr>System</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The operation system of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>score</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The rating information of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>short<wbr>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The short description of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>suggested<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The suggested price of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>supplier<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">number</span>
    </dt>
    <dd>{{% md %}}The supplier id of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>supplier<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The supplier name of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The tags of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>target<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The detail page URL of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>warranty<wbr>Date</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The warranty date of the product.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-required"
            title="Required">
        <span>category<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The Category ID of products. For more information, see [DescribeProducts](https://help.aliyun.com/document_detail/89834.htm). 
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>code</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The code of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>delivery<wbr>Date</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The delivery date of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>delivery<wbr>Way</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The delivery way of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>image<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The image URL of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The name of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>operation<wbr>System</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The operation system of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>score</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The rating information of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>short<wbr>Description</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The short description of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>suggested<wbr>Price</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The suggested price of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>supplier<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The supplier id of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>supplier<wbr>Name</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The supplier name of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>tags</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The tags of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>target<wbr>Url</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The detail page URL of the product.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>warranty<wbr>Date</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The warranty date of the product.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







