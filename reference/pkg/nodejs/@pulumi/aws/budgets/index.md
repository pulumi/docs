---
title: Module budgets
---

<a href="../index.html">@pulumi/aws</a> &gt; budgets

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Budget">class Budget</a>
* <a href="#BudgetArgs">interface BudgetArgs</a>
* <a href="#BudgetState">interface BudgetState</a>

<a href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts">budgets/budget.ts</a> 


<h2 class="pdoc-module-header" id="Budget">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L10">class Budget</a>
</h2>

Provides a budgets budget resource. Budgets use the cost visualisation provided by Cost Explorer to show you the status of your budgets, to provide forecasts of your estimated costs, and to track your AWS usage, including your free tier usage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L66">constructor</a>
</h3>

```typescript
new Budget(name: string, args: BudgetArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Budget resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: BudgetState): Budget
```


Get an existing Budget resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L26">property accountId</a>
</h3>

```typescript
public accountId: pulumi.Output<string>;
```


The ID of the target account for budget. Will use current user's account_id by default if omitted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L30">property budgetType</a>
</h3>

```typescript
public budgetType: pulumi.Output<string>;
```


Whether this budget tracks monetary cost or usage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L34">property costFilters</a>
</h3>

```typescript
public costFilters: pulumi.Output<{ ... }>;
```


Map of CostFilters key/value pairs to apply to the budget.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L38">property costTypes</a>
</h3>

```typescript
public costTypes: pulumi.Output<{ ... }>;
```


Object containing CostTypes The types of cost included in a budget, such as tax and subscriptions..

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L42">property limitAmount</a>
</h3>

```typescript
public limitAmount: pulumi.Output<string>;
```


The amount of cost or usage being measured for a budget.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L46">property limitUnit</a>
</h3>

```typescript
public limitUnit: pulumi.Output<string>;
```


The unit of measurement used for the budget forecast, actual spend, or budget threshold, such as dollars or GB. See [Spend ](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/data-type-spend.html) documentation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L50">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of a budget. Unique within accounts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L54">property namePrefix</a>
</h3>

```typescript
public namePrefix: pulumi.Output<string>;
```


The prefix of the name of a budget. Unique within accounts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L58">property timePeriodEnd</a>
</h3>

```typescript
public timePeriodEnd: pulumi.Output<string | undefined>;
```


The end of the time period covered by the budget. There are no restrictions on the end date. Format: `2017-01-01_12:00`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L62">property timePeriodStart</a>
</h3>

```typescript
public timePeriodStart: pulumi.Output<string>;
```


The start of the time period covered by the budget. The start date must come before the end date. Format: `2017-01-01_12:00`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L66">property timeUnit</a>
</h3>

```typescript
public timeUnit: pulumi.Output<string>;
```


The length of time until a budget resets the actual and forecasted spend. Valid values: `MONTHLY`, `QUARTERLY`, `ANNUALLY`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="BudgetArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L177">interface BudgetArgs</a>
</h2>

The set of arguments for constructing a Budget resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L181">property accountId</a>
</h3>

```typescript
accountId?: pulumi.Input<string>;
```


The ID of the target account for budget. Will use current user's account_id by default if omitted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L185">property budgetType</a>
</h3>

```typescript
budgetType: pulumi.Input<string>;
```


Whether this budget tracks monetary cost or usage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L189">property costFilters</a>
</h3>

```typescript
costFilters?: pulumi.Input<{ ... }>;
```


Map of CostFilters key/value pairs to apply to the budget.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L193">property costTypes</a>
</h3>

```typescript
costTypes?: pulumi.Input<{ ... }>;
```


Object containing CostTypes The types of cost included in a budget, such as tax and subscriptions..

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L197">property limitAmount</a>
</h3>

```typescript
limitAmount: pulumi.Input<string>;
```


The amount of cost or usage being measured for a budget.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L201">property limitUnit</a>
</h3>

```typescript
limitUnit: pulumi.Input<string>;
```


The unit of measurement used for the budget forecast, actual spend, or budget threshold, such as dollars or GB. See [Spend ](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/data-type-spend.html) documentation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L205">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of a budget. Unique within accounts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L209">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


The prefix of the name of a budget. Unique within accounts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L213">property timePeriodEnd</a>
</h3>

```typescript
timePeriodEnd?: pulumi.Input<string>;
```


The end of the time period covered by the budget. There are no restrictions on the end date. Format: `2017-01-01_12:00`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L217">property timePeriodStart</a>
</h3>

```typescript
timePeriodStart: pulumi.Input<string>;
```


The start of the time period covered by the budget. The start date must come before the end date. Format: `2017-01-01_12:00`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L221">property timeUnit</a>
</h3>

```typescript
timeUnit: pulumi.Input<string>;
```


The length of time until a budget resets the actual and forecasted spend. Valid values: `MONTHLY`, `QUARTERLY`, `ANNUALLY`.

<h2 class="pdoc-module-header" id="BudgetState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L127">interface BudgetState</a>
</h2>

Input properties used for looking up and filtering Budget resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L131">property accountId</a>
</h3>

```typescript
accountId?: pulumi.Input<string>;
```


The ID of the target account for budget. Will use current user's account_id by default if omitted.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L135">property budgetType</a>
</h3>

```typescript
budgetType?: pulumi.Input<string>;
```


Whether this budget tracks monetary cost or usage.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L139">property costFilters</a>
</h3>

```typescript
costFilters?: pulumi.Input<{ ... }>;
```


Map of CostFilters key/value pairs to apply to the budget.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L143">property costTypes</a>
</h3>

```typescript
costTypes?: pulumi.Input<{ ... }>;
```


Object containing CostTypes The types of cost included in a budget, such as tax and subscriptions..

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L147">property limitAmount</a>
</h3>

```typescript
limitAmount?: pulumi.Input<string>;
```


The amount of cost or usage being measured for a budget.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L151">property limitUnit</a>
</h3>

```typescript
limitUnit?: pulumi.Input<string>;
```


The unit of measurement used for the budget forecast, actual spend, or budget threshold, such as dollars or GB. See [Spend ](http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/data-type-spend.html) documentation.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L155">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of a budget. Unique within accounts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L159">property namePrefix</a>
</h3>

```typescript
namePrefix?: pulumi.Input<string>;
```


The prefix of the name of a budget. Unique within accounts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L163">property timePeriodEnd</a>
</h3>

```typescript
timePeriodEnd?: pulumi.Input<string>;
```


The end of the time period covered by the budget. There are no restrictions on the end date. Format: `2017-01-01_12:00`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L167">property timePeriodStart</a>
</h3>

```typescript
timePeriodStart?: pulumi.Input<string>;
```


The start of the time period covered by the budget. The start date must come before the end date. Format: `2017-01-01_12:00`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-aws/blob/master/sdk/nodejs/budgets/budget.ts#L171">property timeUnit</a>
</h3>

```typescript
timeUnit?: pulumi.Input<string>;
```


The length of time until a budget resets the actual and forecasted spend. Valid values: `MONTHLY`, `QUARTERLY`, `ANNUALLY`.

