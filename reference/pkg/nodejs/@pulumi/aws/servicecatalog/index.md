---
title: Module servicecatalog
---

<a href="../index.html">@pulumi/aws</a> &gt; servicecatalog

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Portfolio">class Portfolio</a>
* <a href="#PortfolioArgs">interface PortfolioArgs</a>
* <a href="#PortfolioState">interface PortfolioState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicecatalog/portfolio.ts">servicecatalog/portfolio.ts</a> 


<h2 class="pdoc-module-header" id="Portfolio">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicecatalog/portfolio.ts#L9">class Portfolio</a>
</h2>

Provides a resource to create a Service Catalog Portfolio.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicecatalog/portfolio.ts#L39">constructor</a>
</h3>

```typescript
new Portfolio(name: string, args?: PortfolioArgs, opts?: pulumi.ResourceOptions)
```


Create a Portfolio resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicecatalog/portfolio.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: PortfolioState): Portfolio
```


Get an existing Portfolio resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicecatalog/portfolio.ts#L22">property arn</a>
</h3>

```typescript
public arn: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicecatalog/portfolio.ts#L23">property createdTime</a>
</h3>

```typescript
public createdTime: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicecatalog/portfolio.ts#L27">property description</a>
</h3>

```typescript
public description: pulumi.Output<string>;
```


Description of the portfolio

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicecatalog/portfolio.ts#L31">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the portfolio.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicecatalog/portfolio.ts#L35">property providerName</a>
</h3>

```typescript
public providerName: pulumi.Output<string | undefined>;
```


Name of the person or organization who owns the portfolio.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicecatalog/portfolio.ts#L39">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... } | undefined>;
```


Tags to apply to the connection.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="PortfolioArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicecatalog/portfolio.ts#L99">interface PortfolioArgs</a>
</h2>

The set of arguments for constructing a Portfolio resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicecatalog/portfolio.ts#L103">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the portfolio

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicecatalog/portfolio.ts#L107">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the portfolio.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicecatalog/portfolio.ts#L111">property providerName</a>
</h3>

```typescript
providerName?: pulumi.Input<string>;
```


Name of the person or organization who owns the portfolio.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicecatalog/portfolio.ts#L115">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


Tags to apply to the connection.

<h2 class="pdoc-module-header" id="PortfolioState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicecatalog/portfolio.ts#L75">interface PortfolioState</a>
</h2>

Input properties used for looking up and filtering Portfolio resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicecatalog/portfolio.ts#L76">property arn</a>
</h3>

```typescript
arn?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicecatalog/portfolio.ts#L77">property createdTime</a>
</h3>

```typescript
createdTime?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicecatalog/portfolio.ts#L81">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


Description of the portfolio

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicecatalog/portfolio.ts#L85">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the portfolio.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicecatalog/portfolio.ts#L89">property providerName</a>
</h3>

```typescript
providerName?: pulumi.Input<string>;
```


Name of the person or organization who owns the portfolio.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/servicecatalog/portfolio.ts#L93">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


Tags to apply to the connection.

