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
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L9">class Account</a>
</h2>

Manages a new CosmosDB (formally DocumentDB) Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L94">constructor</a>
</h3>

```typescript
new Account(name: string, args: AccountArgs, opts?: pulumi.ResourceOptions)
```


Create a Account resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AccountState): Account
```


Get an existing Account resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L64">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L25">property connectionStrings</a>
</h3>

```typescript
public connectionStrings: pulumi.Output<string[]>;
```


A list of connection strings available for this CosmosDB account. If the kind is `GlobalDocumentDB`, this will be empty.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L29">property consistencyPolicy</a>
</h3>

```typescript
public consistencyPolicy: pulumi.Output<{ ... }>;
```


Specifies a `consistency_policy` resource, used to define the consistency policy for this CosmosDB account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L33">property enableAutomaticFailover</a>
</h3>

```typescript
public enableAutomaticFailover: pulumi.Output<boolean | undefined>;
```


Enable automatic fail over for this Cosmos DB account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L37">property endpoint</a>
</h3>

```typescript
public endpoint: pulumi.Output<string>;
```


The endpoint used to connect to the CosmosDB account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L38">property failoverPolicies</a>
</h3>

```typescript
public failoverPolicies: pulumi.Output<{ ... }[] | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L42">property geoLocations</a>
</h3>

```typescript
public geoLocations: pulumi.Output<{ ... }[]>;
```


Specifies a `geo_location` resource, used to define where data should be replicated with the `failover_priority` 0 specifying the primary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L59">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L46">property ipRangeFilter</a>
</h3>

```typescript
public ipRangeFilter: pulumi.Output<string | undefined>;
```


CosmosDB Firewall Support: This value specifies the set of IP addresses or IP address ranges in CIDR form to be included as the allowed list of client IP's for a given database account. IP addresses/ranges must be comma separated and must not contain any spaces.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L50">property kind</a>
</h3>

```typescript
public kind: pulumi.Output<string | undefined>;
```


Specifies the Kind of CosmosDB to create - possible values are `GlobalDocumentDB` and `MongoDB`. Defaults to `GlobalDocumentDB`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L54">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The name of the Azure region to host replicated data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L58">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the CosmosDB Account. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L62">property offerType</a>
</h3>

```typescript
public offerType: pulumi.Output<string>;
```


Specifies the Offer Type to use for this CosmosDB Account - currently this can only be set to `Standard`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L66">property primaryMasterKey</a>
</h3>

```typescript
public primaryMasterKey: pulumi.Output<string>;
```


The Primary master key for the CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L70">property primaryReadonlyMasterKey</a>
</h3>

```typescript
public primaryReadonlyMasterKey: pulumi.Output<string>;
```


The Primary read-only master Key for the CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L74">property readEndpoints</a>
</h3>

```typescript
public readEndpoints: pulumi.Output<string[]>;
```


A list of read endpoints available for this CosmosDB account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L78">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which the CosmosDB Account is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L82">property secondaryMasterKey</a>
</h3>

```typescript
public secondaryMasterKey: pulumi.Output<string>;
```


The Secondary master key for the CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L86">property secondaryReadonlyMasterKey</a>
</h3>

```typescript
public secondaryReadonlyMasterKey: pulumi.Output<string>;
```


The Secondary read-only master key for the CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L90">property tags</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L94">property writeEndpoints</a>
</h3>

```typescript
public writeEndpoints: pulumi.Output<string[]>;
```


A list of write endpoints available for this CosmosDB account.

<h2 class="pdoc-module-header" id="getAccount">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L9">function getAccount</a>
</h2>

```typescript
getAccount(args: GetAccountArgs): Promise<GetAccountResult>
```


Use this data source to access the properties of an Azure CosmosDB (formally DocumentDB) Account.

<h2 class="pdoc-module-header" id="AccountArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L247">interface AccountArgs</a>
</h2>

The set of arguments for constructing a Account resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L251">property consistencyPolicy</a>
</h3>

```typescript
consistencyPolicy: pulumi.Input<{ ... }>;
```


Specifies a `consistency_policy` resource, used to define the consistency policy for this CosmosDB account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L255">property enableAutomaticFailover</a>
</h3>

```typescript
enableAutomaticFailover?: pulumi.Input<boolean>;
```


Enable automatic fail over for this Cosmos DB account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L256">property failoverPolicies</a>
</h3>

```typescript
failoverPolicies?: pulumi.Input<{ ... }[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L260">property geoLocations</a>
</h3>

```typescript
geoLocations?: pulumi.Input<{ ... }[]>;
```


Specifies a `geo_location` resource, used to define where data should be replicated with the `failover_priority` 0 specifying the primary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L264">property ipRangeFilter</a>
</h3>

```typescript
ipRangeFilter?: pulumi.Input<string>;
```


CosmosDB Firewall Support: This value specifies the set of IP addresses or IP address ranges in CIDR form to be included as the allowed list of client IP's for a given database account. IP addresses/ranges must be comma separated and must not contain any spaces.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L268">property kind</a>
</h3>

```typescript
kind?: pulumi.Input<string>;
```


Specifies the Kind of CosmosDB to create - possible values are `GlobalDocumentDB` and `MongoDB`. Defaults to `GlobalDocumentDB`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L272">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


The name of the Azure region to host replicated data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L276">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the CosmosDB Account. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L280">property offerType</a>
</h3>

```typescript
offerType: pulumi.Input<string>;
```


Specifies the Offer Type to use for this CosmosDB Account - currently this can only be set to `Standard`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L284">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which the CosmosDB Account is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L288">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="AccountState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L168">interface AccountState</a>
</h2>

Input properties used for looking up and filtering Account resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L172">property connectionStrings</a>
</h3>

```typescript
connectionStrings?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of connection strings available for this CosmosDB account. If the kind is `GlobalDocumentDB`, this will be empty.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L176">property consistencyPolicy</a>
</h3>

```typescript
consistencyPolicy?: pulumi.Input<{ ... }>;
```


Specifies a `consistency_policy` resource, used to define the consistency policy for this CosmosDB account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L180">property enableAutomaticFailover</a>
</h3>

```typescript
enableAutomaticFailover?: pulumi.Input<boolean>;
```


Enable automatic fail over for this Cosmos DB account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L184">property endpoint</a>
</h3>

```typescript
endpoint?: pulumi.Input<string>;
```


The endpoint used to connect to the CosmosDB account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L185">property failoverPolicies</a>
</h3>

```typescript
failoverPolicies?: pulumi.Input<{ ... }[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L189">property geoLocations</a>
</h3>

```typescript
geoLocations?: pulumi.Input<{ ... }[]>;
```


Specifies a `geo_location` resource, used to define where data should be replicated with the `failover_priority` 0 specifying the primary location.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L193">property ipRangeFilter</a>
</h3>

```typescript
ipRangeFilter?: pulumi.Input<string>;
```


CosmosDB Firewall Support: This value specifies the set of IP addresses or IP address ranges in CIDR form to be included as the allowed list of client IP's for a given database account. IP addresses/ranges must be comma separated and must not contain any spaces.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L197">property kind</a>
</h3>

```typescript
kind?: pulumi.Input<string>;
```


Specifies the Kind of CosmosDB to create - possible values are `GlobalDocumentDB` and `MongoDB`. Defaults to `GlobalDocumentDB`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L201">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The name of the Azure region to host replicated data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L205">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the CosmosDB Account. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L209">property offerType</a>
</h3>

```typescript
offerType?: pulumi.Input<string>;
```


Specifies the Offer Type to use for this CosmosDB Account - currently this can only be set to `Standard`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L213">property primaryMasterKey</a>
</h3>

```typescript
primaryMasterKey?: pulumi.Input<string>;
```


The Primary master key for the CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L217">property primaryReadonlyMasterKey</a>
</h3>

```typescript
primaryReadonlyMasterKey?: pulumi.Input<string>;
```


The Primary read-only master Key for the CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L221">property readEndpoints</a>
</h3>

```typescript
readEndpoints?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of read endpoints available for this CosmosDB account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L225">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which the CosmosDB Account is created. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L229">property secondaryMasterKey</a>
</h3>

```typescript
secondaryMasterKey?: pulumi.Input<string>;
```


The Secondary master key for the CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L233">property secondaryReadonlyMasterKey</a>
</h3>

```typescript
secondaryReadonlyMasterKey?: pulumi.Input<string>;
```


The Secondary read-only master key for the CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L237">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/account.ts#L241">property writeEndpoints</a>
</h3>

```typescript
writeEndpoints?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of write endpoints available for this CosmosDB account.

<h2 class="pdoc-module-header" id="GetAccountArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L19">interface GetAccountArgs</a>
</h2>

A collection of arguments for invoking getAccount.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L23">property name</a>
</h3>

```typescript
name: pulumi.Input<string>;
```


Specifies the name of the CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L27">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


Specifies the name of the resource group in which the CosmosDB Account resides.

<h2 class="pdoc-module-header" id="GetAccountResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L33">interface GetAccountResult</a>
</h2>

A collection of values returned by getAccount.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L34">property consistencyPolicies</a>
</h3>

```typescript
consistencyPolicies: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L38">property enableAutomaticFailover</a>
</h3>

```typescript
enableAutomaticFailover: boolean;
```


If automatic failover is enabled for this CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L42">property endpoint</a>
</h3>

```typescript
endpoint: string;
```


The endpoint used to connect to the CosmosDB account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L43">property geoLocations</a>
</h3>

```typescript
geoLocations: { ... }[];
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L91">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L47">property ipRangeFilter</a>
</h3>

```typescript
ipRangeFilter: string;
```


The current IP Filter for this CosmosDB account

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L51">property kind</a>
</h3>

```typescript
kind: string;
```


The Kind of the CosmosDB account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L55">property location</a>
</h3>

```typescript
location: string;
```


The name of the Azure region hosting replicated data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L59">property offerType</a>
</h3>

```typescript
offerType: string;
```


The Offer Type to used by this CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L63">property primaryMasterKey</a>
</h3>

```typescript
primaryMasterKey: string;
```


The Primary master key for the CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L67">property primaryReadonlyMasterKey</a>
</h3>

```typescript
primaryReadonlyMasterKey: string;
```


The Primary read-only master Key for the CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L71">property readEndpoints</a>
</h3>

```typescript
readEndpoints: string[];
```


A list of read endpoints available for this CosmosDB account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L75">property secondaryMasterKey</a>
</h3>

```typescript
secondaryMasterKey: string;
```


The Secondary master key for the CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L79">property secondaryReadonlyMasterKey</a>
</h3>

```typescript
secondaryReadonlyMasterKey: string;
```


The Secondary read-only master key for the CosmosDB Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L83">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags assigned to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/cosmosdb/getAccount.ts#L87">property writeEndpoints</a>
</h3>

```typescript
writeEndpoints: string[];
```


A list of write endpoints available for this CosmosDB account.

