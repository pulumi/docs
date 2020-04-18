
---
title: "Order"
block_external_search_index: true
---






## Create a Order Resource

{{< chooser language "javascript,typescript,python,go,csharp" / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">new </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/marketplace/#Order">Order</a></span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">args</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/marketplace/#OrderArgs">OrderArgs</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">pulumi.CustomResourceOptions</a></span><span class="p">);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">def </span><span class="nf">Order</span><span class="p">(resource_name, opts=None, </span>components=None<span class="p">, </span>coupon_id=None<span class="p">, </span>duration=None<span class="p">, </span>package_version=None<span class="p">, </span>pay_type=None<span class="p">, </span>pricing_cycle=None<span class="p">, </span>product_code=None<span class="p">, </span>quantity=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>NewOrder<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">pulumi.Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">args</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/marketplace?tab=doc#OrderArgs">OrderArgs</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">pulumi.ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/marketplace?tab=doc#Order">Order</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Marketplace.Order.html">Order</a></span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.MarketPlace.OrderArgs.html">OrderArgs</a></span> <span class="nx">args<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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

    <dt class="property-optional"
            title="Optional">
        <span>Components</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Service providers customize additional components.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Coupon<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The coupon id of the market product.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of purchase cycles.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Package<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The package version of the market product.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pay<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Valid values are `PrePaid`, `PostPaid`,System default to `PostPaid`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Pricing<wbr>Cycle</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The purchase cycle of the product, valid values are `Day`, `Month` and `Year`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Product<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The product_code of market place product.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Quantity</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The quantity of the market product will be purchased.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Components</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Service providers customize additional components.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Coupon<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The coupon id of the market product.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of purchase cycles.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Package<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The package version of the market product.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pay<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Valid values are `PrePaid`, `PostPaid`,System default to `PostPaid`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Pricing<wbr>Cycle</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The purchase cycle of the product, valid values are `Day`, `Month` and `Year`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>Product<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The product_code of market place product.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Quantity</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The quantity of the market product will be purchased.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>components</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Service providers customize additional components.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>coupon<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The coupon id of the market product.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of purchase cycles.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>package<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The package version of the market product.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pay<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Valid values are `PrePaid`, `PostPaid`,System default to `PostPaid`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>pricing<wbr>Cycle</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The purchase cycle of the product, valid values are `Day`, `Month` and `Year`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>product<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The product_code of market place product.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>quantity</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The quantity of the market product will be purchased.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>components</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Service providers customize additional components.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>coupon_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The coupon id of the market product.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of purchase cycles.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>package_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The package version of the market product.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pay_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Valid values are `PrePaid`, `PostPaid`,System default to `PostPaid`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>pricing_<wbr>cycle</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The purchase cycle of the product, valid values are `Day`, `Month` and `Year`.
{{% /md %}}</dd>

    <dt class="property-required"
            title="Required">
        <span>product_<wbr>code</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The product_code of market place product.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>quantity</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The quantity of the market product will be purchased.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}







## Order Output Properties

The following output properties are available:




{{% choosable language csharp %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Components</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Service providers customize additional components.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Coupon<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The coupon id of the market product.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of purchase cycles.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Package<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The package version of the market product.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Pay<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Valid values are `PrePaid`, `PostPaid`,System default to `PostPaid`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Pricing<wbr>Cycle</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The purchase cycle of the product, valid values are `Day`, `Month` and `Year`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Product<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The product_code of market place product.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Quantity</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The quantity of the market product will be purchased.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>Components</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Service providers customize additional components.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Coupon<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The coupon id of the market product.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of purchase cycles.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Package<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The package version of the market product.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Pay<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Valid values are `PrePaid`, `PostPaid`,System default to `PostPaid`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Pricing<wbr>Cycle</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The purchase cycle of the product, valid values are `Day`, `Month` and `Year`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Product<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The product_code of market place product.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>Quantity</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The quantity of the market product will be purchased.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>components</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Service providers customize additional components.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>coupon<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The coupon id of the market product.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of purchase cycles.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>package<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The package version of the market product.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>pay<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Valid values are `PrePaid`, `PostPaid`,System default to `PostPaid`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>pricing<wbr>Cycle</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The purchase cycle of the product, valid values are `Day`, `Month` and `Year`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>product<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string</span>
    </dt>
    <dd>{{% md %}}The product_code of market place product.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>quantity</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The quantity of the market product will be purchased.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-"
            title="">
        <span>components</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Service providers customize additional components.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>coupon_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The coupon id of the market product.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of purchase cycles.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>package_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The package version of the market product.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>pay_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Valid values are `PrePaid`, `PostPaid`,System default to `PostPaid`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>pricing_<wbr>cycle</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The purchase cycle of the product, valid values are `Day`, `Month` and `Year`.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>product_<wbr>code</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The product_code of market place product.
{{% /md %}}</dd>

    <dt class="property-"
            title="">
        <span>quantity</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The quantity of the market product will be purchased.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}








## Look up an Existing Order Resource

Get an existing Order resource's state with the given name, ID, and optional extra properties used to qualify the lookup.

{{< chooser language "javascript,typescript,python,go,csharp  " / >}}

{{% choosable language nodejs %}}
<div class="highlight"><pre class="chroma"><code class="language-typescript" data-lang="typescript"><span class="k">public static </span><span class="nf">get</span><span class="p">(</span><span class="nx">name</span>: <span class="nx"><a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/string">string</a></span><span class="p">, </span><span class="nx">id</span>: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#ID">Input&lt;ID&gt;</a></span><span class="p">, </span><span class="nx">state</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/marketplace/#OrderState">OrderState</a></span><span class="p">, </span><span class="nx">opts</span>?: <span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/pulumi/#CustomResourceOptions">CustomResourceOptions</a></span><span class="p">): </span><span class="nx"><a href="/docs/reference/pkg/nodejs/pulumi/alicloud/marketplace/#Order">Order</a></span></code></pre></div>
{{% /choosable %}}

{{% choosable language python %}}
<div class="highlight"><pre class="chroma"><code class="language-python" data-lang="python"><span class="k">static </span><span class="nf">get</span><span class="p">(resource_name, id, opts=None, </span>components=None<span class="p">, </span>coupon_id=None<span class="p">, </span>duration=None<span class="p">, </span>package_version=None<span class="p">, </span>pay_type=None<span class="p">, </span>pricing_cycle=None<span class="p">, </span>product_code=None<span class="p">, </span>quantity=None<span class="p">, __props__=None);</span></code></pre></div>
{{% /choosable %}}

{{% choosable language go %}}
<div class="highlight"><pre class="chroma"><code class="language-go" data-lang="go"><span class="k">func </span>GetOrder<span class="p">(</span><span class="nx">ctx</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#Context">Context</a></span><span class="p">, </span><span class="nx">name</span> <span class="nx"><a href="https://golang.org/pkg/builtin/#string">string</a></span><span class="p">, </span><span class="nx">id</span> <span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#IDInput">IDInput</a></span><span class="p">, </span><span class="nx">state</span> *<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/marketplace?tab=doc#OrderState">OrderState</a></span><span class="p">, </span><span class="nx">opts</span> ...<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi/sdk/go/pulumi?tab=doc#ResourceOption">ResourceOption</a></span><span class="p">) (*<span class="nx"><a href="https://pkg.go.dev/github.com/pulumi/pulumi-alicloud/sdk/go/alicloud/marketplace?tab=doc#Order">Order</a></span>, error)</span></code></pre></div>
{{% /choosable %}}

{{% choosable language csharp %}}
<div class="highlight"><pre class="chroma"><code class="language-csharp" data-lang="csharp"><span class="k">public static </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Marketplace.Order.html">Order</a></span><span class="nf"> Get</span><span class="p">(</span><span class="nx"><a href="https://docs.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/built-in-types">string</a></span> <span class="nx">name<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.Input.html">Input&lt;string&gt;</a></span> <span class="nx">id<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi.Alicloud/Pulumi.Alicloud.Marketplace.OrderState.html">OrderState</a></span>? <span class="nx">state<span class="p">, </span><span class="nx"><a href="/docs/reference/pkg/dotnet/Pulumi/Pulumi.CustomResourceOptions.html">CustomResourceOptions</a></span>? <span class="nx">opts = null<span class="p">)</span></code></pre></div>
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
        <span>Components</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dictionary<string, object>?</span>
    </dt>
    <dd>{{% md %}}Service providers customize additional components.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Coupon<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The coupon id of the market product.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The number of purchase cycles.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Package<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The package version of the market product.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pay<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Valid values are `PrePaid`, `PostPaid`,System default to `PostPaid`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pricing<wbr>Cycle</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The purchase cycle of the product, valid values are `Day`, `Month` and `Year`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Product<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The product_code of market place product.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Quantity</span>
        <span class="property-indicator"></span>
        <span class="property-type">int?</span>
    </dt>
    <dd>{{% md %}}The quantity of the market product will be purchased.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language go %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>Components</span>
        <span class="property-indicator"></span>
        <span class="property-type">map[string]interface{}</span>
    </dt>
    <dd>{{% md %}}Service providers customize additional components.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Coupon<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The coupon id of the market product.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The number of purchase cycles.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Package<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The package version of the market product.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pay<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}Valid values are `PrePaid`, `PostPaid`,System default to `PostPaid`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Pricing<wbr>Cycle</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The purchase cycle of the product, valid values are `Day`, `Month` and `Year`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Product<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">*string</span>
    </dt>
    <dd>{{% md %}}The product_code of market place product.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>Quantity</span>
        <span class="property-indicator"></span>
        <span class="property-type">*int</span>
    </dt>
    <dd>{{% md %}}The quantity of the market product will be purchased.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language nodejs %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>components</span>
        <span class="property-indicator"></span>
        <span class="property-type">{[key: string]: any}?</span>
    </dt>
    <dd>{{% md %}}Service providers customize additional components.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>coupon<wbr>Id</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The coupon id of the market product.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The number of purchase cycles.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>package<wbr>Version</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The package version of the market product.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pay<wbr>Type</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}Valid values are `PrePaid`, `PostPaid`,System default to `PostPaid`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pricing<wbr>Cycle</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The purchase cycle of the product, valid values are `Day`, `Month` and `Year`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>product<wbr>Code</span>
        <span class="property-indicator"></span>
        <span class="property-type">string?</span>
    </dt>
    <dd>{{% md %}}The product_code of market place product.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>quantity</span>
        <span class="property-indicator"></span>
        <span class="property-type">number?</span>
    </dt>
    <dd>{{% md %}}The quantity of the market product will be purchased.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}


{{% choosable language python %}}
<dl class="resources-properties">

    <dt class="property-optional"
            title="Optional">
        <span>components</span>
        <span class="property-indicator"></span>
        <span class="property-type">Dict[str, Any]</span>
    </dt>
    <dd>{{% md %}}Service providers customize additional components.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>coupon_<wbr>id</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The coupon id of the market product.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>duration</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The number of purchase cycles.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>package_<wbr>version</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The package version of the market product.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pay_<wbr>type</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}Valid values are `PrePaid`, `PostPaid`,System default to `PostPaid`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>pricing_<wbr>cycle</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The purchase cycle of the product, valid values are `Day`, `Month` and `Year`.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>product_<wbr>code</span>
        <span class="property-indicator"></span>
        <span class="property-type">str</span>
    </dt>
    <dd>{{% md %}}The product_code of market place product.
{{% /md %}}</dd>

    <dt class="property-optional"
            title="Optional">
        <span>quantity</span>
        <span class="property-indicator"></span>
        <span class="property-type">float</span>
    </dt>
    <dd>{{% md %}}The quantity of the market product will be purchased.
{{% /md %}}</dd>

</dl>
{{% /choosable %}}











<h3>Package Details</h3>
<dl class="package-details">
	<dt>Repository</dt>
	<dd><a href="https://github.com/pulumi/pulumi-alicloud">https://github.com/pulumi/pulumi-alicloud</a></dd>
	<dt>License</dt>
	<dd>Apache-2.0</dd>
    
</dl>

