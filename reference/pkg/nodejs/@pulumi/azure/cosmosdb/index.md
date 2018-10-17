---
title: Module cosmosdb
---

<a href="../index.html">@pulumi/azure</a> &gt; cosmosdb

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Account">class Account</a>
* <a href="#getAccount">function getAccount</a>
* <a href="#AccountArgs">interface AccountArgs</a>
* <a href="#AccountState">interface AccountState</a>
* <a href="#GetAccountArgs">interface GetAccountArgs</a>
* <a href="#GetAccountResult">interface GetAccountResult</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts">cosmosdb/account.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts">cosmosdb/getAccount.ts</a> 


<h2 class="pdoc-module-header" id="Account">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L10">class Account</a>
</h2>

Manages a CosmosDB (formally DocumentDB) Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L101">constructor</a>
</h3>

```typescript
new Account(name: string, args: AccountArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Account resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L19">method get</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L26">property capabilities</a>
</h3>

```typescript
public capabilities: pulumi.Output<{ ... }[] | undefined>;
```


Enable capabilities for this Cosmos DB account. Possible values are `EnableTable` and `EnableGremlin`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L30">property connectionStrings</a>
</h3>

```typescript
public connectionStrings: pulumi.Output<string[]>;
```


A list of connection strings available for this CosmosDB account. If the kind is `GlobalDocumentDB`, this will be empty.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L34">property consistencyPolicy</a>
</h3>

```typescript
public consistencyPolicy: pulumi.Output<{ ... }>;
```


Specifies a `consistency_policy` resource, used to define the consistency policy for this CosmosDB account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L38">property enableAutomaticFailover</a>
</h3>

```typescript
public enableAutomaticFailover: pulumi.Output<boolean | undefined>;
```


Enable automatic fail over for this Cosmos DB account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L42">property endpoint</a>
</h3>

```typescript
public endpoint: pulumi.Output<string>;
```


The endpoint used to connect to the CosmosDB account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L43">property failoverPolicies</a>
</h3>

```typescript
public failoverPolicies: pulumi.Output<{ ... }[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L47">property geoLocations</a>
</h3>

```typescript
public geoLocations: pulumi.Output<{ ... }[]>;
```


Specifies a `geo_location` resource, used to define where data should be replicated with the `failover_priority` 0 specifying the primary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L51">property ipRangeFilter</a>
</h3>

```typescript
public ipRangeFilter: pulumi.Output<string | undefined>;
```


CosmosDB Firewall Support: This value specifies the set of IP addresses or IP address ranges in CIDR form to be included as the allowed list of client IP's for a given database account. IP addresses/ranges must be comma separated and must not contain any spaces.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L52">property isVirtualNetworkFilterEnabled</a>
</h3>

```typescript
public isVirtualNetworkFilterEnabled: pulumi.Output<boolean | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L56">property kind</a>
</h3>

```typescript
public kind: pulumi.Output<string | undefined>;
```


Specifies the Kind of CosmosDB to create - possible values are `GlobalDocumentDB` and `MongoDB`. Defaults to `GlobalDocumentDB`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L60">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The name of the Azure region to host replicated data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L64">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the CosmosDB Account. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L68">property offerType</a>
</h3>

```typescript
public offerType: pulumi.Output<string>;
```


Specifies the Offer Type to use for this CosmosDB Account - currently this can only be set to `Standard`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L72">property primaryMasterKey</a>
</h3>

```typescript
public primaryMasterKey: pulumi.Output<string>;
```


The Primary master key for the CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L76">property primaryReadonlyMasterKey</a>
</h3>

```typescript
public primaryReadonlyMasterKey: pulumi.Output<string>;
```


The Primary read-only master Key for the CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L80">property readEndpoints</a>
</h3>

```typescript
public readEndpoints: pulumi.Output<string[]>;
```


A list of read endpoints available for this CosmosDB account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L84">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the CosmosDB Account is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L88">property secondaryMasterKey</a>
</h3>

```typescript
public secondaryMasterKey: pulumi.Output<string>;
```


The Secondary master key for the CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L92">property secondaryReadonlyMasterKey</a>
</h3>

```typescript
public secondaryReadonlyMasterKey: pulumi.Output<string>;
```


The Secondary read-only master key for the CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L96">property tags</a>
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

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L97">property virtualNetworkRules</a>
</h3>

```typescript
public virtualNetworkRules: pulumi.Output<{ ... }[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L101">property writeEndpoints</a>
</h3>

```typescript
public writeEndpoints: pulumi.Output<string[]>;
```


A list of write endpoints available for this CosmosDB account.

<h2 class="pdoc-module-header" id="getAccount">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L10">function getAccount</a>
</h2>

```typescript
getAccount(args: GetAccountArgs, opts?: pulumi.InvokeOptions): Promise<GetAccountResult>
```


Use this data source to access the properties of an Azure CosmosDB (formally DocumentDB) Account.

<h2 class="pdoc-module-header" id="AccountArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L266">interface AccountArgs</a>
</h2>

The set of arguments for constructing a Account resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L270">property capabilities</a>
</h3>

```typescript
capabilities?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Enable capabilities for this Cosmos DB account. Possible values are `EnableTable` and `EnableGremlin`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L274">property consistencyPolicy</a>
</h3>

```typescript
consistencyPolicy: pulumi.Input<{ ... }>;
```


Specifies a `consistency_policy` resource, used to define the consistency policy for this CosmosDB account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L278">property enableAutomaticFailover</a>
</h3>

```typescript
enableAutomaticFailover?: pulumi.Input<boolean>;
```


Enable automatic fail over for this Cosmos DB account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L279">property failoverPolicies</a>
</h3>

```typescript
failoverPolicies?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L283">property geoLocations</a>
</h3>

```typescript
geoLocations?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Specifies a `geo_location` resource, used to define where data should be replicated with the `failover_priority` 0 specifying the primary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L287">property ipRangeFilter</a>
</h3>

```typescript
ipRangeFilter?: pulumi.Input<string>;
```


CosmosDB Firewall Support: This value specifies the set of IP addresses or IP address ranges in CIDR form to be included as the allowed list of client IP's for a given database account. IP addresses/ranges must be comma separated and must not contain any spaces.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L288">property isVirtualNetworkFilterEnabled</a>
</h3>

```typescript
isVirtualNetworkFilterEnabled?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L292">property kind</a>
</h3>

```typescript
kind?: pulumi.Input<string>;
```


Specifies the Kind of CosmosDB to create - possible values are `GlobalDocumentDB` and `MongoDB`. Defaults to `GlobalDocumentDB`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L296">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


The name of the Azure region to host replicated data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L300">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the CosmosDB Account. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L304">property offerType</a>
</h3>

```typescript
offerType: pulumi.Input<string>;
```


Specifies the Offer Type to use for this CosmosDB Account - currently this can only be set to `Standard`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L308">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the CosmosDB Account is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L312">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L313">property virtualNetworkRules</a>
</h3>

```typescript
virtualNetworkRules?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h2 class="pdoc-module-header" id="AccountState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L181">interface AccountState</a>
</h2>

Input properties used for looking up and filtering Account resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L185">property capabilities</a>
</h3>

```typescript
capabilities?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Enable capabilities for this Cosmos DB account. Possible values are `EnableTable` and `EnableGremlin`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L189">property connectionStrings</a>
</h3>

```typescript
connectionStrings?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of connection strings available for this CosmosDB account. If the kind is `GlobalDocumentDB`, this will be empty.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L193">property consistencyPolicy</a>
</h3>

```typescript
consistencyPolicy?: pulumi.Input<{ ... }>;
```


Specifies a `consistency_policy` resource, used to define the consistency policy for this CosmosDB account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L197">property enableAutomaticFailover</a>
</h3>

```typescript
enableAutomaticFailover?: pulumi.Input<boolean>;
```


Enable automatic fail over for this Cosmos DB account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L201">property endpoint</a>
</h3>

```typescript
endpoint?: pulumi.Input<string>;
```


The endpoint used to connect to the CosmosDB account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L202">property failoverPolicies</a>
</h3>

```typescript
failoverPolicies?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L206">property geoLocations</a>
</h3>

```typescript
geoLocations?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


Specifies a `geo_location` resource, used to define where data should be replicated with the `failover_priority` 0 specifying the primary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L210">property ipRangeFilter</a>
</h3>

```typescript
ipRangeFilter?: pulumi.Input<string>;
```


CosmosDB Firewall Support: This value specifies the set of IP addresses or IP address ranges in CIDR form to be included as the allowed list of client IP's for a given database account. IP addresses/ranges must be comma separated and must not contain any spaces.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L211">property isVirtualNetworkFilterEnabled</a>
</h3>

```typescript
isVirtualNetworkFilterEnabled?: pulumi.Input<boolean>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L215">property kind</a>
</h3>

```typescript
kind?: pulumi.Input<string>;
```


Specifies the Kind of CosmosDB to create - possible values are `GlobalDocumentDB` and `MongoDB`. Defaults to `GlobalDocumentDB`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L219">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The name of the Azure region to host replicated data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L223">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the CosmosDB Account. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L227">property offerType</a>
</h3>

```typescript
offerType?: pulumi.Input<string>;
```


Specifies the Offer Type to use for this CosmosDB Account - currently this can only be set to `Standard`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L231">property primaryMasterKey</a>
</h3>

```typescript
primaryMasterKey?: pulumi.Input<string>;
```


The Primary master key for the CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L235">property primaryReadonlyMasterKey</a>
</h3>

```typescript
primaryReadonlyMasterKey?: pulumi.Input<string>;
```


The Primary read-only master Key for the CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L239">property readEndpoints</a>
</h3>

```typescript
readEndpoints?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of read endpoints available for this CosmosDB account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L243">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the CosmosDB Account is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L247">property secondaryMasterKey</a>
</h3>

```typescript
secondaryMasterKey?: pulumi.Input<string>;
```


The Secondary master key for the CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L251">property secondaryReadonlyMasterKey</a>
</h3>

```typescript
secondaryReadonlyMasterKey?: pulumi.Input<string>;
```


The Secondary read-only master key for the CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L255">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L256">property virtualNetworkRules</a>
</h3>

```typescript
virtualNetworkRules?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L260">property writeEndpoints</a>
</h3>

```typescript
writeEndpoints?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of write endpoints available for this CosmosDB account.

<h2 class="pdoc-module-header" id="GetAccountArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L20">interface GetAccountArgs</a>
</h2>

A collection of arguments for invoking getAccount.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L24">property name</a>
</h3>

```typescript
name: string;
```


Specifies the name of the CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L28">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


Specifies the name of the resource group in which the CosmosDB Account resides.

<h2 class="pdoc-module-header" id="GetAccountResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L34">interface GetAccountResult</a>
</h2>

A collection of values returned by getAccount.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L38">property capabilities</a>
</h3>

```typescript
capabilities: { ... }[];
```


Capabilities enabled on this Cosmos DB account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L39">property consistencyPolicies</a>
</h3>

```typescript
consistencyPolicies: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L43">property enableAutomaticFailover</a>
</h3>

```typescript
enableAutomaticFailover: boolean;
```


If automatic failover is enabled for this CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L47">property endpoint</a>
</h3>

```typescript
endpoint: string;
```


The endpoint used to connect to the CosmosDB account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L48">property geoLocations</a>
</h3>

```typescript
geoLocations: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L96">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L52">property ipRangeFilter</a>
</h3>

```typescript
ipRangeFilter: string;
```


The current IP Filter for this CosmosDB account

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L56">property kind</a>
</h3>

```typescript
kind: string;
```


The Kind of the CosmosDB account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L60">property location</a>
</h3>

```typescript
location: string;
```


The name of the Azure region hosting replicated data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L64">property offerType</a>
</h3>

```typescript
offerType: string;
```


The Offer Type to used by this CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L68">property primaryMasterKey</a>
</h3>

```typescript
primaryMasterKey: string;
```


The Primary master key for the CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L72">property primaryReadonlyMasterKey</a>
</h3>

```typescript
primaryReadonlyMasterKey: string;
```


The Primary read-only master Key for the CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L76">property readEndpoints</a>
</h3>

```typescript
readEndpoints: string[];
```


A list of read endpoints available for this CosmosDB account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L80">property secondaryMasterKey</a>
</h3>

```typescript
secondaryMasterKey: string;
```


The Secondary master key for the CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L84">property secondaryReadonlyMasterKey</a>
</h3>

```typescript
secondaryReadonlyMasterKey: string;
```


The Secondary read-only master key for the CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L88">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags assigned to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L92">property writeEndpoints</a>
</h3>

```typescript
writeEndpoints: string[];
```


A list of write endpoints available for this CosmosDB account.

