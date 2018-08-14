---
title: Module pricing
---

<a href="../index.html">@pulumi/aws</a> &gt; pricing

<h2 class="pdoc-module-header">Index</h2>

* <a href="#getProduct">function getProduct</a>
* <a href="#GetProductArgs">interface GetProductArgs</a>
* <a href="#GetProductResult">interface GetProductResult</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pricing/getProduct.ts">pricing/getProduct.ts</a> 


<h2 class="pdoc-module-header" id="getProduct">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pricing/getProduct.ts#L10">function getProduct</a>
</h2>

```typescript
getProduct(args: GetProductArgs, opts?: pulumi.InvokeOptions): Promise<GetProductResult>
```


Use this data source to get the pricing information of all products in AWS.
This data source is only available in a us-east-1 or ap-south-1 provider.

<h2 class="pdoc-module-header" id="GetProductArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pricing/getProduct.ts#L20">interface GetProductArgs</a>
</h2>

A collection of arguments for invoking getProduct.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pricing/getProduct.ts#L24">property filters</a>
</h3>

```typescript
filters: { ... }[];
```


A list of filters. Passed directly to the API (see GetProducts API reference). These filters must describe a single product, this resource will fail if more than one product is returned by the API.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pricing/getProduct.ts#L28">property serviceCode</a>
</h3>

```typescript
serviceCode: string;
```


The code of the service. Available service codes can be fetched using the DescribeServices pricing API call.

<h2 class="pdoc-module-header" id="GetProductResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pricing/getProduct.ts#L34">interface GetProductResult</a>
</h2>

A collection of values returned by getProduct.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pricing/getProduct.ts#L42">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/pricing/getProduct.ts#L38">property result</a>
</h3>

```typescript
result: string;
```


Set to the product returned from the API.

