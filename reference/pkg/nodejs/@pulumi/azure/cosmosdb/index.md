---
title: Module cosmosdb
---

<a href="..">@pulumi/azure</a>

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Account">class Account</a>
* <a href="#AccountArgs">interface AccountArgs</a>
* <a href="#AccountState">interface AccountState</a>

<a href="/cosmosdb/account.ts">cosmosdb/account.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>


<h2 class="pdoc-module-header" id="Account">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L9">class Account</a>
</h2>

Creates a new CosmosDB (formally DocumentDB) Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L73">constructor</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L18">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L25">property consistencyPolicy</a>
</h3>

```typescript
public consistencyPolicy: pulumi.Output<{ ... }>;
```


Specifies a `consistency_policy` resource, used to define the consistency policy for this CosmosDB account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L29">property failoverPolicies</a>
</h3>

```typescript
public failoverPolicies: pulumi.Output<{ ... }[]>;
```


Specifies a `failover_policy` resource, used to define where data should be replicated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L33">property ipRangeFilter</a>
</h3>

```typescript
public ipRangeFilter: pulumi.Output<string | undefined>;
```


CosmosDB Firewall Support: This value specifies the set of IP addresses or IP address ranges in CIDR form to be included as the allowed list of client IP's for a given database account. IP addresses/ranges must be comma separated and must not contain any spaces.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L37">property kind</a>
</h3>

```typescript
public kind: pulumi.Output<string | undefined>;
```


Specifies the Kind of CosmosDB to create - possible values are `GlobalDocumentDB` and `MongoDB`. Defaults to `GlobalDocumentDB`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L41">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The name of the Azure region to host replicated data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L45">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the CosmosDB Account. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L49">property offerType</a>
</h3>

```typescript
public offerType: pulumi.Output<string>;
```


Specifies the Offer Type to use for this CosmosDB Account - currently this can only be set to `Standard`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L53">property primaryMasterKey</a>
</h3>

```typescript
public primaryMasterKey: pulumi.Output<string>;
```


The Primary master key for the CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L57">property primaryReadonlyMasterKey</a>
</h3>

```typescript
public primaryReadonlyMasterKey: pulumi.Output<string>;
```


The Primary read-only master Key for the CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L61">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the CosmosDB Account is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L65">property secondaryMasterKey</a>
</h3>

```typescript
public secondaryMasterKey: pulumi.Output<string>;
```


The Secondary master key for the CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L69">property secondaryReadonlyMasterKey</a>
</h3>

```typescript
public secondaryReadonlyMasterKey: pulumi.Output<string>;
```


The Secondary read-only master key for the CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L73">property tags</a>
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

<h2 class="pdoc-module-header" id="AccountArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L198">interface AccountArgs</a>
</h2>

The set of arguments for constructing a Account resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L202">property consistencyPolicy</a>
</h3>

```typescript
consistencyPolicy: pulumi.Input<{ ... }>;
```


Specifies a `consistency_policy` resource, used to define the consistency policy for this CosmosDB account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L206">property failoverPolicies</a>
</h3>

```typescript
failoverPolicies: pulumi.Input<{ ... }[]>;
```


Specifies a `failover_policy` resource, used to define where data should be replicated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L210">property ipRangeFilter</a>
</h3>

```typescript
ipRangeFilter?: pulumi.Input<string>;
```


CosmosDB Firewall Support: This value specifies the set of IP addresses or IP address ranges in CIDR form to be included as the allowed list of client IP's for a given database account. IP addresses/ranges must be comma separated and must not contain any spaces.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L214">property kind</a>
</h3>

```typescript
kind?: pulumi.Input<string>;
```


Specifies the Kind of CosmosDB to create - possible values are `GlobalDocumentDB` and `MongoDB`. Defaults to `GlobalDocumentDB`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L218">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


The name of the Azure region to host replicated data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L222">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the CosmosDB Account. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L226">property offerType</a>
</h3>

```typescript
offerType: pulumi.Input<string>;
```


Specifies the Offer Type to use for this CosmosDB Account - currently this can only be set to `Standard`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L230">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the CosmosDB Account is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L234">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="AccountState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L140">interface AccountState</a>
</h2>

Input properties used for looking up and filtering Account resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L144">property consistencyPolicy</a>
</h3>

```typescript
consistencyPolicy?: pulumi.Input<{ ... }>;
```


Specifies a `consistency_policy` resource, used to define the consistency policy for this CosmosDB account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L148">property failoverPolicies</a>
</h3>

```typescript
failoverPolicies?: pulumi.Input<{ ... }[]>;
```


Specifies a `failover_policy` resource, used to define where data should be replicated.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L152">property ipRangeFilter</a>
</h3>

```typescript
ipRangeFilter?: pulumi.Input<string>;
```


CosmosDB Firewall Support: This value specifies the set of IP addresses or IP address ranges in CIDR form to be included as the allowed list of client IP's for a given database account. IP addresses/ranges must be comma separated and must not contain any spaces.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L156">property kind</a>
</h3>

```typescript
kind?: pulumi.Input<string>;
```


Specifies the Kind of CosmosDB to create - possible values are `GlobalDocumentDB` and `MongoDB`. Defaults to `GlobalDocumentDB`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L160">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The name of the Azure region to host replicated data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L164">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the CosmosDB Account. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L168">property offerType</a>
</h3>

```typescript
offerType?: pulumi.Input<string>;
```


Specifies the Offer Type to use for this CosmosDB Account - currently this can only be set to `Standard`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L172">property primaryMasterKey</a>
</h3>

```typescript
primaryMasterKey?: pulumi.Input<string>;
```


The Primary master key for the CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L176">property primaryReadonlyMasterKey</a>
</h3>

```typescript
primaryReadonlyMasterKey?: pulumi.Input<string>;
```


The Primary read-only master Key for the CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L180">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the CosmosDB Account is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L184">property secondaryMasterKey</a>
</h3>

```typescript
secondaryMasterKey?: pulumi.Input<string>;
```


The Secondary master key for the CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L188">property secondaryReadonlyMasterKey</a>
</h3>

```typescript
secondaryReadonlyMasterKey?: pulumi.Input<string>;
```


The Secondary read-only master key for the CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/cosmosdb/account.ts#L192">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

