---
title: Module automation
---

<a href="../index.html">@pulumi/azure</a> &gt; automation

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Account">class Account</a>
* <a href="#Credential">class Credential</a>
* <a href="#RunBook">class RunBook</a>
* <a href="#Schedule">class Schedule</a>
* <a href="#AccountArgs">interface AccountArgs</a>
* <a href="#AccountState">interface AccountState</a>
* <a href="#CredentialArgs">interface CredentialArgs</a>
* <a href="#CredentialState">interface CredentialState</a>
* <a href="#RunBookArgs">interface RunBookArgs</a>
* <a href="#RunBookState">interface RunBookState</a>
* <a href="#ScheduleArgs">interface ScheduleArgs</a>
* <a href="#ScheduleState">interface ScheduleState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/account.ts">automation/account.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/credential.ts">automation/credential.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts">automation/runBook.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts">automation/schedule.ts</a> 


<h2 class="pdoc-module-header" id="Account">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/account.ts#L10">class Account</a>
</h2>

Manages a Automation Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/account.ts#L42">constructor</a>
</h3>

```typescript
new Account(name: string, args: AccountArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Account resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/account.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AccountState): Account
```


Get an existing Account resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/account.ts#L26">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/account.ts#L30">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The SKU name of the account - only `Basic` is supported at this time. Defaults to `Basic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/account.ts#L34">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the Automation Account is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/account.ts#L38">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<{ ... }>;
```


A `sku` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/account.ts#L42">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Credential">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/credential.ts#L10">class Credential</a>
</h2>

Manages a Automation Credential.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/credential.ts#L46">constructor</a>
</h3>

```typescript
new Credential(name: string, args: CredentialArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Credential resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/credential.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CredentialState): Credential
```


Get an existing Credential resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/credential.ts#L26">property accountName</a>
</h3>

```typescript
public accountName: pulumi.Output<string>;
```


The name of the automation account in which the Credential is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/credential.ts#L30">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description associated with this Automation Credential.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/credential.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Credential. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/credential.ts#L38">property password</a>
</h3>

```typescript
public password: pulumi.Output<string>;
```


The password associated with this Automation Credential.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/credential.ts#L42">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the Credential is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/credential.ts#L46">property username</a>
</h3>

```typescript
public username: pulumi.Output<string>;
```


The username associated with this Automation Credential.

<h2 class="pdoc-module-header" id="RunBook">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L10">class RunBook</a>
</h2>

Manages a Automation Runbook.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L63">constructor</a>
</h3>

```typescript
new RunBook(name: string, args: RunBookArgs, opts?: pulumi.CustomResourceOptions)
```


Create a RunBook resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RunBookState): RunBook
```


Get an existing RunBook resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L26">property accountName</a>
</h3>

```typescript
public accountName: pulumi.Output<string>;
```


The name of the automation account in which the Runbook is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L30">property content</a>
</h3>

```typescript
public content: pulumi.Output<string>;
```


The desired content of the runbook.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L34">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description for this credential.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L38">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L42">property logProgress</a>
</h3>

```typescript
public logProgress: pulumi.Output<boolean>;
```


Progress log option.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L46">property logVerbose</a>
</h3>

```typescript
public logVerbose: pulumi.Output<boolean>;
```


Verbose log option.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L50">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Runbook. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L54">property publishContentLink</a>
</h3>

```typescript
public publishContentLink: pulumi.Output<{ ... }>;
```


The published runbook content link.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L58">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the Runbook is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L62">property runbookType</a>
</h3>

```typescript
public runbookType: pulumi.Output<string>;
```


The type of the runbook - can be either `Graph`, `GraphPowerShell`, `GraphPowerShellWorkflow`, `PowerShellWorkflow`, `PowerShell` or `Script`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L63">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Schedule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L10">class Schedule</a>
</h2>

Manages a Automation Schedule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L71">constructor</a>
</h3>

```typescript
new Schedule(name: string, args: ScheduleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Schedule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ScheduleState): Schedule
```


Get an existing Schedule resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L23">property accountName</a>
</h3>

```typescript
public accountName: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L27">property automationAccountName</a>
</h3>

```typescript
public automationAccountName: pulumi.Output<string>;
```


The name of the automation account in which the Schedule is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L31">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description for this Schedule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L35">property expiryTime</a>
</h3>

```typescript
public expiryTime: pulumi.Output<string>;
```


The end time of the schedule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L39">property frequency</a>
</h3>

```typescript
public frequency: pulumi.Output<string>;
```


The frequency of the schedule. - can be either `OneTime`, `Day`, `Hour`, `Week`, or `Month`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L43">property interval</a>
</h3>

```typescript
public interval: pulumi.Output<number>;
```


The number of `frequency`s between runs. Only valid when frequency is `Day`, `Hour`, `Week`, or `Month` and defaults to `1`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L47">property monthDays</a>
</h3>

```typescript
public monthDays: pulumi.Output<number[] | undefined>;
```


List of days of the month that the job should execute on. Must be between `1` and `31`. `-1` for last day of the month. Only valid when frequency is `Month`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L51">property monthlyOccurrences</a>
</h3>

```typescript
public monthlyOccurrences: pulumi.Output<{ ... }[] | undefined>;
```


List of occurrences of days within a month. Only valid when frequency is `Month`. The `monthly_occurrence` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L55">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Schedule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L59">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the Schedule is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L63">property startTime</a>
</h3>

```typescript
public startTime: pulumi.Output<string>;
```


Start time of the schedule. Must be at least five minutes in the future. Defaults to seven minutes in the future from the time the resource is created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L67">property timezone</a>
</h3>

```typescript
public timezone: pulumi.Output<string | undefined>;
```


The timezone of the start time. Defaults to `UTC`. For possible values see: https://msdn.microsoft.com/en-us/library/ms912391(v=winembedded.11).aspx

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L71">property weekDays</a>
</h3>

```typescript
public weekDays: pulumi.Output<string[] | undefined>;
```


List of days of the week that the job should execute on. Only valid when frequency is `Week`.

<h2 class="pdoc-module-header" id="AccountArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/account.ts#L111">interface AccountArgs</a>
</h2>

The set of arguments for constructing a Account resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/account.ts#L115">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/account.ts#L119">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The SKU name of the account - only `Basic` is supported at this time. Defaults to `Basic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/account.ts#L123">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the Automation Account is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/account.ts#L127">property sku</a>
</h3>

```typescript
sku: pulumi.Input<{ ... }>;
```


A `sku` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/account.ts#L131">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="AccountState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/account.ts#L85">interface AccountState</a>
</h2>

Input properties used for looking up and filtering Account resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/account.ts#L89">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/account.ts#L93">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The SKU name of the account - only `Basic` is supported at this time. Defaults to `Basic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/account.ts#L97">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the Automation Account is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/account.ts#L101">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<{ ... }>;
```


A `sku` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/account.ts#L105">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="CredentialArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/credential.ts#L124">interface CredentialArgs</a>
</h2>

The set of arguments for constructing a Credential resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/credential.ts#L128">property accountName</a>
</h3>

```typescript
accountName: pulumi.Input<string>;
```


The name of the automation account in which the Credential is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/credential.ts#L132">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description associated with this Automation Credential.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/credential.ts#L136">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Credential. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/credential.ts#L140">property password</a>
</h3>

```typescript
password: pulumi.Input<string>;
```


The password associated with this Automation Credential.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/credential.ts#L144">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the Credential is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/credential.ts#L148">property username</a>
</h3>

```typescript
username: pulumi.Input<string>;
```


The username associated with this Automation Credential.

<h2 class="pdoc-module-header" id="CredentialState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/credential.ts#L94">interface CredentialState</a>
</h2>

Input properties used for looking up and filtering Credential resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/credential.ts#L98">property accountName</a>
</h3>

```typescript
accountName?: pulumi.Input<string>;
```


The name of the automation account in which the Credential is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/credential.ts#L102">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description associated with this Automation Credential.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/credential.ts#L106">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Credential. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/credential.ts#L110">property password</a>
</h3>

```typescript
password?: pulumi.Input<string>;
```


The password associated with this Automation Credential.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/credential.ts#L114">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the Credential is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/credential.ts#L118">property username</a>
</h3>

```typescript
username?: pulumi.Input<string>;
```


The username associated with this Automation Credential.

<h2 class="pdoc-module-header" id="RunBookArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L177">interface RunBookArgs</a>
</h2>

The set of arguments for constructing a RunBook resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L181">property accountName</a>
</h3>

```typescript
accountName: pulumi.Input<string>;
```


The name of the automation account in which the Runbook is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L185">property content</a>
</h3>

```typescript
content?: pulumi.Input<string>;
```


The desired content of the runbook.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L189">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for this credential.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L193">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L197">property logProgress</a>
</h3>

```typescript
logProgress: pulumi.Input<boolean>;
```


Progress log option.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L201">property logVerbose</a>
</h3>

```typescript
logVerbose: pulumi.Input<boolean>;
```


Verbose log option.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L205">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Runbook. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L209">property publishContentLink</a>
</h3>

```typescript
publishContentLink: pulumi.Input<{ ... }>;
```


The published runbook content link.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L213">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the Runbook is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L217">property runbookType</a>
</h3>

```typescript
runbookType: pulumi.Input<string>;
```


The type of the runbook - can be either `Graph`, `GraphPowerShell`, `GraphPowerShellWorkflow`, `PowerShellWorkflow`, `PowerShell` or `Script`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L218">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h2 class="pdoc-module-header" id="RunBookState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L130">interface RunBookState</a>
</h2>

Input properties used for looking up and filtering RunBook resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L134">property accountName</a>
</h3>

```typescript
accountName?: pulumi.Input<string>;
```


The name of the automation account in which the Runbook is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L138">property content</a>
</h3>

```typescript
content?: pulumi.Input<string>;
```


The desired content of the runbook.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L142">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for this credential.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L146">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L150">property logProgress</a>
</h3>

```typescript
logProgress?: pulumi.Input<boolean>;
```


Progress log option.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L154">property logVerbose</a>
</h3>

```typescript
logVerbose?: pulumi.Input<boolean>;
```


Verbose log option.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L158">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Runbook. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L162">property publishContentLink</a>
</h3>

```typescript
publishContentLink?: pulumi.Input<{ ... }>;
```


The published runbook content link.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L166">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the Runbook is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L170">property runbookType</a>
</h3>

```typescript
runbookType?: pulumi.Input<string>;
```


The type of the runbook - can be either `Graph`, `GraphPowerShell`, `GraphPowerShellWorkflow`, `PowerShellWorkflow`, `PowerShell` or `Script`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/runBook.ts#L171">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h2 class="pdoc-module-header" id="ScheduleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L182">interface ScheduleArgs</a>
</h2>

The set of arguments for constructing a Schedule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L183">property accountName</a>
</h3>

```typescript
accountName?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L187">property automationAccountName</a>
</h3>

```typescript
automationAccountName?: pulumi.Input<string>;
```


The name of the automation account in which the Schedule is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L191">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for this Schedule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L195">property expiryTime</a>
</h3>

```typescript
expiryTime?: pulumi.Input<string>;
```


The end time of the schedule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L199">property frequency</a>
</h3>

```typescript
frequency: pulumi.Input<string>;
```


The frequency of the schedule. - can be either `OneTime`, `Day`, `Hour`, `Week`, or `Month`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L203">property interval</a>
</h3>

```typescript
interval?: pulumi.Input<number>;
```


The number of `frequency`s between runs. Only valid when frequency is `Day`, `Hour`, `Week`, or `Month` and defaults to `1`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L207">property monthDays</a>
</h3>

```typescript
monthDays?: pulumi.Input<pulumi.Input<number>[]>;
```


List of days of the month that the job should execute on. Must be between `1` and `31`. `-1` for last day of the month. Only valid when frequency is `Month`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L211">property monthlyOccurrences</a>
</h3>

```typescript
monthlyOccurrences?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


List of occurrences of days within a month. Only valid when frequency is `Month`. The `monthly_occurrence` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L215">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Schedule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L219">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the Schedule is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L223">property startTime</a>
</h3>

```typescript
startTime?: pulumi.Input<string>;
```


Start time of the schedule. Must be at least five minutes in the future. Defaults to seven minutes in the future from the time the resource is created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L227">property timezone</a>
</h3>

```typescript
timezone?: pulumi.Input<string>;
```


The timezone of the start time. Defaults to `UTC`. For possible values see: https://msdn.microsoft.com/en-us/library/ms912391(v=winembedded.11).aspx

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L231">property weekDays</a>
</h3>

```typescript
weekDays?: pulumi.Input<pulumi.Input<string>[]>;
```


List of days of the week that the job should execute on. Only valid when frequency is `Week`.

<h2 class="pdoc-module-header" id="ScheduleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L127">interface ScheduleState</a>
</h2>

Input properties used for looking up and filtering Schedule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L128">property accountName</a>
</h3>

```typescript
accountName?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L132">property automationAccountName</a>
</h3>

```typescript
automationAccountName?: pulumi.Input<string>;
```


The name of the automation account in which the Schedule is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L136">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for this Schedule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L140">property expiryTime</a>
</h3>

```typescript
expiryTime?: pulumi.Input<string>;
```


The end time of the schedule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L144">property frequency</a>
</h3>

```typescript
frequency?: pulumi.Input<string>;
```


The frequency of the schedule. - can be either `OneTime`, `Day`, `Hour`, `Week`, or `Month`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L148">property interval</a>
</h3>

```typescript
interval?: pulumi.Input<number>;
```


The number of `frequency`s between runs. Only valid when frequency is `Day`, `Hour`, `Week`, or `Month` and defaults to `1`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L152">property monthDays</a>
</h3>

```typescript
monthDays?: pulumi.Input<pulumi.Input<number>[]>;
```


List of days of the month that the job should execute on. Must be between `1` and `31`. `-1` for last day of the month. Only valid when frequency is `Month`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L156">property monthlyOccurrences</a>
</h3>

```typescript
monthlyOccurrences?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


List of occurrences of days within a month. Only valid when frequency is `Month`. The `monthly_occurrence` block supports fields documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L160">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Schedule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L164">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the Schedule is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L168">property startTime</a>
</h3>

```typescript
startTime?: pulumi.Input<string>;
```


Start time of the schedule. Must be at least five minutes in the future. Defaults to seven minutes in the future from the time the resource is created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L172">property timezone</a>
</h3>

```typescript
timezone?: pulumi.Input<string>;
```


The timezone of the start time. Defaults to `UTC`. For possible values see: https://msdn.microsoft.com/en-us/library/ms912391(v=winembedded.11).aspx

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/automation/schedule.ts#L176">property weekDays</a>
</h3>

```typescript
weekDays?: pulumi.Input<pulumi.Input<string>[]>;
```


List of days of the week that the job should execute on. Only valid when frequency is `Week`.

