---
title: Module automation
---

<a href="..">@pulumi/azure</a>

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

<a href="/automation/account.ts">automation/account.ts</a> <a href="/automation/credential.ts">automation/credential.ts</a> <a href="/automation/runBook.ts">automation/runBook.ts</a> <a href="/automation/schedule.ts">automation/schedule.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>


<h2 class="pdoc-module-header" id="Account">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/account.ts#L9">class Account</a>
</h2>

Creates a new Automation Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/account.ts#L41">constructor</a>
</h3>

```typescript
new Account(name: string, args: AccountArgs, opts?: pulumi.ResourceOptions)
```


Create a Account resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Account(name: string, state?: AccountState, opts?: pulumi.ResourceOptions)
```


Create a Account resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/account.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AccountState): Account
```


Get an existing Account resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/account.ts#L25">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/account.ts#L29">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The SKU name of the account - only `Basic` is supported at this time. Defaults to `Basic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/account.ts#L33">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the Automation Account is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/account.ts#L37">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<{ ... }>;
```


A `sku` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/account.ts#L41">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Credential">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/credential.ts#L9">class Credential</a>
</h2>

Creates a new Automation Credential.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/credential.ts#L45">constructor</a>
</h3>

```typescript
new Credential(name: string, args: CredentialArgs, opts?: pulumi.ResourceOptions)
```


Create a Credential resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Credential(name: string, state?: CredentialState, opts?: pulumi.ResourceOptions)
```


Create a Credential resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/credential.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CredentialState): Credential
```


Get an existing Credential resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/credential.ts#L25">property accountName</a>
</h3>

```typescript
public accountName: pulumi.Output<string>;
```


The name of the automation account in which the Credential is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/credential.ts#L29">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


The description associated with this Automation Credential.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/credential.ts#L33">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Credential. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/credential.ts#L37">property password</a>
</h3>

```typescript
public password: pulumi.Output<string>;
```


The password associated with this Automation Credential.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/credential.ts#L41">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the Credential is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/credential.ts#L45">property username</a>
</h3>

```typescript
public username: pulumi.Output<string>;
```


The username associated with this Automation Credential.

<h2 class="pdoc-module-header" id="RunBook">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/runBook.ts#L9">class RunBook</a>
</h2>

Creates a new Automation Runbook.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/runBook.ts#L58">constructor</a>
</h3>

```typescript
new RunBook(name: string, args: RunBookArgs, opts?: pulumi.ResourceOptions)
```


Create a RunBook resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new RunBook(name: string, state?: RunBookState, opts?: pulumi.ResourceOptions)
```


Create a RunBook resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/runBook.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RunBookState): RunBook
```


Get an existing RunBook resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/runBook.ts#L25">property accountName</a>
</h3>

```typescript
public accountName: pulumi.Output<string>;
```


The name of the automation account in which the Runbook is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/runBook.ts#L29">property description</a>
</h3>

```typescript
public description: pulumi.Output<string | undefined>;
```


A description for this credential.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/runBook.ts#L33">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/runBook.ts#L37">property logProgress</a>
</h3>

```typescript
public logProgress: pulumi.Output<boolean>;
```


Progress log option.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/runBook.ts#L41">property logVerbose</a>
</h3>

```typescript
public logVerbose: pulumi.Output<boolean>;
```


Verbose log option.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/runBook.ts#L45">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Runbook. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/runBook.ts#L49">property publishContentLink</a>
</h3>

```typescript
public publishContentLink: pulumi.Output<{ ... }>;
```


The published runbook content link.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/runBook.ts#L53">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the Runbook is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/runBook.ts#L57">property runbookType</a>
</h3>

```typescript
public runbookType: pulumi.Output<string>;
```


The type of the runbook - can be either `Graph`, `GraphPowerShell`, `GraphPowerShellWorkflow`, `PowerShellWorkflow`, `PowerShell` or `Script`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/runBook.ts#L58">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Schedule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/schedule.ts#L9">class Schedule</a>
</h2>

Creates a new Automation Schedule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/schedule.ts#L53">constructor</a>
</h3>

```typescript
new Schedule(name: string, args: ScheduleArgs, opts?: pulumi.ResourceOptions)
```


Create a Schedule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Schedule(name: string, state?: ScheduleState, opts?: pulumi.ResourceOptions)
```


Create a Schedule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/schedule.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ScheduleState): Schedule
```


Get an existing Schedule resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L72">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/schedule.ts#L25">property accountName</a>
</h3>

```typescript
public accountName: pulumi.Output<string>;
```


The name of the automation account in which the Schedule is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/schedule.ts#L29">property description</a>
</h3>

```typescript
public description: pulumi.Output<string>;
```


A description for this Schedule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/schedule.ts#L33">property expiryTime</a>
</h3>

```typescript
public expiryTime: pulumi.Output<string>;
```


The end time of the schedule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/schedule.ts#L37">property frequency</a>
</h3>

```typescript
public frequency: pulumi.Output<string>;
```


The frequency of the schedule. - can be either `OneTime`, `Day`, `Hour`, `Week`, or `Month`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/schedule.ts#L41">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Schedule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/schedule.ts#L45">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the Schedule is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/schedule.ts#L49">property startTime</a>
</h3>

```typescript
public startTime: pulumi.Output<string>;
```


Start time of the schedule. Must be at least five minutes in the future.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/schedule.ts#L53">property timezone</a>
</h3>

```typescript
public timezone: pulumi.Output<string | undefined>;
```


The timezone of the start time. For possible values see: https://msdn.microsoft.com/en-us/library/ms912391(v=winembedded.11).aspx

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="AccountArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/account.ts#L112">interface AccountArgs</a>
</h2>

The set of arguments for constructing a Account resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/account.ts#L116">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/account.ts#L120">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The SKU name of the account - only `Basic` is supported at this time. Defaults to `Basic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/account.ts#L124">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the Automation Account is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/account.ts#L128">property sku</a>
</h3>

```typescript
sku: pulumi.Input<{ ... }>;
```


A `sku` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/account.ts#L132">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="AccountState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/account.ts#L86">interface AccountState</a>
</h2>

Input properties used for looking up and filtering Account resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/account.ts#L90">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/account.ts#L94">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The SKU name of the account - only `Basic` is supported at this time. Defaults to `Basic`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/account.ts#L98">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the Automation Account is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/account.ts#L102">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<{ ... }>;
```


A `sku` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/account.ts#L106">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="CredentialArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/credential.ts#L125">interface CredentialArgs</a>
</h2>

The set of arguments for constructing a Credential resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/credential.ts#L129">property accountName</a>
</h3>

```typescript
accountName: pulumi.Input<string>;
```


The name of the automation account in which the Credential is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/credential.ts#L133">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description associated with this Automation Credential.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/credential.ts#L137">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Credential. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/credential.ts#L141">property password</a>
</h3>

```typescript
password: pulumi.Input<string>;
```


The password associated with this Automation Credential.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/credential.ts#L145">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the Credential is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/credential.ts#L149">property username</a>
</h3>

```typescript
username: pulumi.Input<string>;
```


The username associated with this Automation Credential.

<h2 class="pdoc-module-header" id="CredentialState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/credential.ts#L95">interface CredentialState</a>
</h2>

Input properties used for looking up and filtering Credential resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/credential.ts#L99">property accountName</a>
</h3>

```typescript
accountName?: pulumi.Input<string>;
```


The name of the automation account in which the Credential is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/credential.ts#L103">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


The description associated with this Automation Credential.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/credential.ts#L107">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Credential. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/credential.ts#L111">property password</a>
</h3>

```typescript
password?: pulumi.Input<string>;
```


The password associated with this Automation Credential.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/credential.ts#L115">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the Credential is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/credential.ts#L119">property username</a>
</h3>

```typescript
username?: pulumi.Input<string>;
```


The username associated with this Automation Credential.

<h2 class="pdoc-module-header" id="RunBookArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/runBook.ts#L168">interface RunBookArgs</a>
</h2>

The set of arguments for constructing a RunBook resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/runBook.ts#L172">property accountName</a>
</h3>

```typescript
accountName: pulumi.Input<string>;
```


The name of the automation account in which the Runbook is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/runBook.ts#L176">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for this credential.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/runBook.ts#L180">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/runBook.ts#L184">property logProgress</a>
</h3>

```typescript
logProgress: pulumi.Input<boolean>;
```


Progress log option.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/runBook.ts#L188">property logVerbose</a>
</h3>

```typescript
logVerbose: pulumi.Input<boolean>;
```


Verbose log option.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/runBook.ts#L192">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Runbook. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/runBook.ts#L196">property publishContentLink</a>
</h3>

```typescript
publishContentLink: pulumi.Input<{ ... }>;
```


The published runbook content link.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/runBook.ts#L200">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the Runbook is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/runBook.ts#L204">property runbookType</a>
</h3>

```typescript
runbookType: pulumi.Input<string>;
```


The type of the runbook - can be either `Graph`, `GraphPowerShell`, `GraphPowerShellWorkflow`, `PowerShellWorkflow`, `PowerShell` or `Script`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/runBook.ts#L205">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h2 class="pdoc-module-header" id="RunBookState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/runBook.ts#L125">interface RunBookState</a>
</h2>

Input properties used for looking up and filtering RunBook resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/runBook.ts#L129">property accountName</a>
</h3>

```typescript
accountName?: pulumi.Input<string>;
```


The name of the automation account in which the Runbook is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/runBook.ts#L133">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for this credential.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/runBook.ts#L137">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/runBook.ts#L141">property logProgress</a>
</h3>

```typescript
logProgress?: pulumi.Input<boolean>;
```


Progress log option.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/runBook.ts#L145">property logVerbose</a>
</h3>

```typescript
logVerbose?: pulumi.Input<boolean>;
```


Verbose log option.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/runBook.ts#L149">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Runbook. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/runBook.ts#L153">property publishContentLink</a>
</h3>

```typescript
publishContentLink?: pulumi.Input<{ ... }>;
```


The published runbook content link.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/runBook.ts#L157">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the Runbook is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/runBook.ts#L161">property runbookType</a>
</h3>

```typescript
runbookType?: pulumi.Input<string>;
```


The type of the runbook - can be either `Graph`, `GraphPowerShell`, `GraphPowerShellWorkflow`, `PowerShellWorkflow`, `PowerShell` or `Script`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/runBook.ts#L162">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h2 class="pdoc-module-header" id="ScheduleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/schedule.ts#L145">interface ScheduleArgs</a>
</h2>

The set of arguments for constructing a Schedule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/schedule.ts#L149">property accountName</a>
</h3>

```typescript
accountName: pulumi.Input<string>;
```


The name of the automation account in which the Schedule is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/schedule.ts#L153">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for this Schedule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/schedule.ts#L157">property expiryTime</a>
</h3>

```typescript
expiryTime?: pulumi.Input<string>;
```


The end time of the schedule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/schedule.ts#L161">property frequency</a>
</h3>

```typescript
frequency: pulumi.Input<string>;
```


The frequency of the schedule. - can be either `OneTime`, `Day`, `Hour`, `Week`, or `Month`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/schedule.ts#L165">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Schedule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/schedule.ts#L169">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the Schedule is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/schedule.ts#L173">property startTime</a>
</h3>

```typescript
startTime: pulumi.Input<string>;
```


Start time of the schedule. Must be at least five minutes in the future.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/schedule.ts#L177">property timezone</a>
</h3>

```typescript
timezone?: pulumi.Input<string>;
```


The timezone of the start time. For possible values see: https://msdn.microsoft.com/en-us/library/ms912391(v=winembedded.11).aspx

<h2 class="pdoc-module-header" id="ScheduleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/schedule.ts#L107">interface ScheduleState</a>
</h2>

Input properties used for looking up and filtering Schedule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/schedule.ts#L111">property accountName</a>
</h3>

```typescript
accountName?: pulumi.Input<string>;
```


The name of the automation account in which the Schedule is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/schedule.ts#L115">property description</a>
</h3>

```typescript
description?: pulumi.Input<string>;
```


A description for this Schedule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/schedule.ts#L119">property expiryTime</a>
</h3>

```typescript
expiryTime?: pulumi.Input<string>;
```


The end time of the schedule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/schedule.ts#L123">property frequency</a>
</h3>

```typescript
frequency?: pulumi.Input<string>;
```


The frequency of the schedule. - can be either `OneTime`, `Day`, `Hour`, `Week`, or `Month`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/schedule.ts#L127">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Schedule. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/schedule.ts#L131">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the Schedule is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/schedule.ts#L135">property startTime</a>
</h3>

```typescript
startTime?: pulumi.Input<string>;
```


Start time of the schedule. Must be at least five minutes in the future.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/automation/schedule.ts#L139">property timezone</a>
</h3>

```typescript
timezone?: pulumi.Input<string>;
```


The timezone of the start time. For possible values see: https://msdn.microsoft.com/en-us/library/ms912391(v=winembedded.11).aspx

