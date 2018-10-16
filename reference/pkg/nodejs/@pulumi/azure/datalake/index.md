---
title: Module datalake
---

<a href="../index.html">@pulumi/azure</a> &gt; datalake

<h2 class="pdoc-module-header">Index</h2>

* <a href="#AnalyticsAccount">class AnalyticsAccount</a>
* <a href="#AnalyticsFirewallRule">class AnalyticsFirewallRule</a>
* <a href="#Store">class Store</a>
* <a href="#StoreFile">class StoreFile</a>
* <a href="#StoreFirewallRule">class StoreFirewallRule</a>
* <a href="#getStore">function getStore</a>
* <a href="#AnalyticsAccountArgs">interface AnalyticsAccountArgs</a>
* <a href="#AnalyticsAccountState">interface AnalyticsAccountState</a>
* <a href="#AnalyticsFirewallRuleArgs">interface AnalyticsFirewallRuleArgs</a>
* <a href="#AnalyticsFirewallRuleState">interface AnalyticsFirewallRuleState</a>
* <a href="#GetStoreArgs">interface GetStoreArgs</a>
* <a href="#GetStoreResult">interface GetStoreResult</a>
* <a href="#StoreArgs">interface StoreArgs</a>
* <a href="#StoreFileArgs">interface StoreFileArgs</a>
* <a href="#StoreFileState">interface StoreFileState</a>
* <a href="#StoreFirewallRuleArgs">interface StoreFirewallRuleArgs</a>
* <a href="#StoreFirewallRuleState">interface StoreFirewallRuleState</a>
* <a href="#StoreState">interface StoreState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsAccount.ts">datalake/analyticsAccount.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsFirewallRule.ts">datalake/analyticsFirewallRule.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/getStore.ts">datalake/getStore.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts">datalake/store.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/storeFile.ts">datalake/storeFile.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/storeFirewallRule.ts">datalake/storeFirewallRule.ts</a> 


<h2 class="pdoc-module-header" id="AnalyticsAccount">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsAccount.ts#L10">class AnalyticsAccount</a>
</h2>

Manage an Azure Data Lake Analytics Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsAccount.ts#L46">constructor</a>
</h3>

```typescript
new AnalyticsAccount(name: string, args: AnalyticsAccountArgs, opts?: pulumi.CustomResourceOptions)
```


Create a AnalyticsAccount resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsAccount.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AnalyticsAccountState): AnalyticsAccount
```


Get an existing AnalyticsAccount resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsAccount.ts#L26">property defaultStoreAccountName</a>
</h3>

```typescript
public defaultStoreAccountName: pulumi.Output<string>;
```


Specifies the data lake store to use by default. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsAccount.ts#L30">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsAccount.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Data Lake Analytics Account. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsAccount.ts#L38">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the Data Lake Analytics Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsAccount.ts#L42">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsAccount.ts#L46">property tier</a>
</h3>

```typescript
public tier: pulumi.Output<string | undefined>;
```


The monthly commitment tier for Data Lake Analytics Account. Accepted values are `Consumption`, `Commitment_100000AUHours`, `Commitment_10000AUHours`, `Commitment_1000AUHours`, `Commitment_100AUHours`, `Commitment_500000AUHours`, `Commitment_50000AUHours`, `Commitment_5000AUHours`, or `Commitment_500AUHours`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="AnalyticsFirewallRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsFirewallRule.ts#L10">class AnalyticsFirewallRule</a>
</h2>

Manage a Azure Data Lake Analytics Firewall Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsFirewallRule.ts#L42">constructor</a>
</h3>

```typescript
new AnalyticsFirewallRule(name: string, args: AnalyticsFirewallRuleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a AnalyticsFirewallRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsFirewallRule.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AnalyticsFirewallRuleState): AnalyticsFirewallRule
```


Get an existing AnalyticsFirewallRule resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsFirewallRule.ts#L26">property accountName</a>
</h3>

```typescript
public accountName: pulumi.Output<string>;
```


Specifies the name of the Data Lake Analytics for which the Firewall Rule should take effect.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsFirewallRule.ts#L30">property endIpAddress</a>
</h3>

```typescript
public endIpAddress: pulumi.Output<string>;
```


The End IP Address for the firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsFirewallRule.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Data Lake Analytics. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsFirewallRule.ts#L38">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the Data Lake Analytics.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsFirewallRule.ts#L42">property startIpAddress</a>
</h3>

```typescript
public startIpAddress: pulumi.Output<string>;
```


The Start IP address for the firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Store">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L10">class Store</a>
</h2>

Manage an Azure Data Lake Store.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L62">constructor</a>
</h3>

```typescript
new Store(name: string, args: StoreArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Store resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: StoreState): Store
```


Get an existing Store resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L26">property encryptionState</a>
</h3>

```typescript
public encryptionState: pulumi.Output<string | undefined>;
```


Is Encryption enabled on this Data Lake Store Account? Possible values are `Enabled` or `Disabled`. Defaults to `Enabled`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L30">property encryptionType</a>
</h3>

```typescript
public encryptionType: pulumi.Output<string>;
```


The Encryption Type used for this Data Lake Store Account. Currently can be set to `SystemManaged` when `encryption_state` is `Enabled` - and must be a blank string when it's Disabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L34">property endpoint</a>
</h3>

```typescript
public endpoint: pulumi.Output<string>;
```


The Endpoint for the Data Lake Store.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L38">property firewallAllowAzureIps</a>
</h3>

```typescript
public firewallAllowAzureIps: pulumi.Output<string | undefined>;
```


are Azure Service IP's allowed through the firewall? Possible values are `Enabled` and `Disabled`. Defaults to `Enabled.`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L42">property firewallState</a>
</h3>

```typescript
public firewallState: pulumi.Output<string | undefined>;
```


the state of the Firewall. Possible values are `Enabled` and `Disabled`. Defaults to `Enabled.`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L46">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L50">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Data Lake Store. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L54">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the Data Lake Store.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L58">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L62">property tier</a>
</h3>

```typescript
public tier: pulumi.Output<string | undefined>;
```


The monthly commitment tier for Data Lake Store. Accepted values are `Consumption`, `Commitment_1TB`, `Commitment_10TB`, `Commitment_100TB`, `Commitment_500TB`, `Commitment_1PB` or `Commitment_5PB`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="StoreFile">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/storeFile.ts#L13">class StoreFile</a>
</h2>

Manage a Azure Data Lake Store File.

~> **Note:** If you want to change the data in the remote file without changing the `local_file_path`, then
taint the resource so the `azurerm_data_lake_store_file` gets recreated with the new data.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/storeFile.ts#L37">constructor</a>
</h3>

```typescript
new StoreFile(name: string, args: StoreFileArgs, opts?: pulumi.CustomResourceOptions)
```


Create a StoreFile resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/storeFile.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: StoreFileState): StoreFile
```


Get an existing StoreFile resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/storeFile.ts#L29">property accountName</a>
</h3>

```typescript
public accountName: pulumi.Output<string>;
```


Specifies the name of the Data Lake Store for which the File should created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/storeFile.ts#L33">property localFilePath</a>
</h3>

```typescript
public localFilePath: pulumi.Output<string>;
```


The path to the local file to be added to the Data Lake Store.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/storeFile.ts#L37">property remoteFilePath</a>
</h3>

```typescript
public remoteFilePath: pulumi.Output<string>;
```


The path created for the file on the Data Lake Store.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="StoreFirewallRule">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/storeFirewallRule.ts#L10">class StoreFirewallRule</a>
</h2>

Manage a Azure Data Lake Store Firewall Rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/storeFirewallRule.ts#L42">constructor</a>
</h3>

```typescript
new StoreFirewallRule(name: string, args: StoreFirewallRuleArgs, opts?: pulumi.CustomResourceOptions)
```


Create a StoreFirewallRule resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/storeFirewallRule.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: StoreFirewallRuleState): StoreFirewallRule
```


Get an existing StoreFirewallRule resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/storeFirewallRule.ts#L26">property accountName</a>
</h3>

```typescript
public accountName: pulumi.Output<string>;
```


Specifies the name of the Data Lake Store for which the Firewall Rule should take effect.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/storeFirewallRule.ts#L30">property endIpAddress</a>
</h3>

```typescript
public endIpAddress: pulumi.Output<string>;
```


The End IP Address for the firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/storeFirewallRule.ts#L34">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Data Lake Store. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/storeFirewallRule.ts#L38">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the Data Lake Store.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/storeFirewallRule.ts#L42">property startIpAddress</a>
</h3>

```typescript
public startIpAddress: pulumi.Output<string>;
```


The Start IP address for the firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getStore">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/getStore.ts#L10">function getStore</a>
</h2>

```typescript
getStore(args: GetStoreArgs, opts?: pulumi.InvokeOptions): Promise<GetStoreResult>
```


Use this data source to obtain information about a Data Lake Store.

<h2 class="pdoc-module-header" id="AnalyticsAccountArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsAccount.ts#L121">interface AnalyticsAccountArgs</a>
</h2>

The set of arguments for constructing a AnalyticsAccount resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsAccount.ts#L125">property defaultStoreAccountName</a>
</h3>

```typescript
defaultStoreAccountName: pulumi.Input<string>;
```


Specifies the data lake store to use by default. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsAccount.ts#L129">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsAccount.ts#L133">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Data Lake Analytics Account. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsAccount.ts#L137">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the Data Lake Analytics Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsAccount.ts#L141">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsAccount.ts#L145">property tier</a>
</h3>

```typescript
tier?: pulumi.Input<string>;
```


The monthly commitment tier for Data Lake Analytics Account. Accepted values are `Consumption`, `Commitment_100000AUHours`, `Commitment_10000AUHours`, `Commitment_1000AUHours`, `Commitment_100AUHours`, `Commitment_500000AUHours`, `Commitment_50000AUHours`, `Commitment_5000AUHours`, or `Commitment_500AUHours`.

<h2 class="pdoc-module-header" id="AnalyticsAccountState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsAccount.ts#L91">interface AnalyticsAccountState</a>
</h2>

Input properties used for looking up and filtering AnalyticsAccount resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsAccount.ts#L95">property defaultStoreAccountName</a>
</h3>

```typescript
defaultStoreAccountName?: pulumi.Input<string>;
```


Specifies the data lake store to use by default. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsAccount.ts#L99">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsAccount.ts#L103">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Data Lake Analytics Account. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsAccount.ts#L107">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the Data Lake Analytics Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsAccount.ts#L111">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsAccount.ts#L115">property tier</a>
</h3>

```typescript
tier?: pulumi.Input<string>;
```


The monthly commitment tier for Data Lake Analytics Account. Accepted values are `Consumption`, `Commitment_100000AUHours`, `Commitment_10000AUHours`, `Commitment_1000AUHours`, `Commitment_100AUHours`, `Commitment_500000AUHours`, `Commitment_50000AUHours`, `Commitment_5000AUHours`, or `Commitment_500AUHours`.

<h2 class="pdoc-module-header" id="AnalyticsFirewallRuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsFirewallRule.ts#L114">interface AnalyticsFirewallRuleArgs</a>
</h2>

The set of arguments for constructing a AnalyticsFirewallRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsFirewallRule.ts#L118">property accountName</a>
</h3>

```typescript
accountName: pulumi.Input<string>;
```


Specifies the name of the Data Lake Analytics for which the Firewall Rule should take effect.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsFirewallRule.ts#L122">property endIpAddress</a>
</h3>

```typescript
endIpAddress: pulumi.Input<string>;
```


The End IP Address for the firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsFirewallRule.ts#L126">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Data Lake Analytics. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsFirewallRule.ts#L130">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the Data Lake Analytics.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsFirewallRule.ts#L134">property startIpAddress</a>
</h3>

```typescript
startIpAddress: pulumi.Input<string>;
```


The Start IP address for the firewall rule.

<h2 class="pdoc-module-header" id="AnalyticsFirewallRuleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsFirewallRule.ts#L88">interface AnalyticsFirewallRuleState</a>
</h2>

Input properties used for looking up and filtering AnalyticsFirewallRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsFirewallRule.ts#L92">property accountName</a>
</h3>

```typescript
accountName?: pulumi.Input<string>;
```


Specifies the name of the Data Lake Analytics for which the Firewall Rule should take effect.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsFirewallRule.ts#L96">property endIpAddress</a>
</h3>

```typescript
endIpAddress?: pulumi.Input<string>;
```


The End IP Address for the firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsFirewallRule.ts#L100">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Data Lake Analytics. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsFirewallRule.ts#L104">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the Data Lake Analytics.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/analyticsFirewallRule.ts#L108">property startIpAddress</a>
</h3>

```typescript
startIpAddress?: pulumi.Input<string>;
```


The Start IP address for the firewall rule.

<h2 class="pdoc-module-header" id="GetStoreArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/getStore.ts#L20">interface GetStoreArgs</a>
</h2>

A collection of arguments for invoking getStore.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/getStore.ts#L24">property name</a>
</h3>

```typescript
name: string;
```


The name of the Data Lake Store.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/getStore.ts#L28">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


The Name of the Resource Group where the Data Lake Store exists.

<h2 class="pdoc-module-header" id="GetStoreResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/getStore.ts#L34">interface GetStoreResult</a>
</h2>

A collection of values returned by getStore.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/getStore.ts#L38">property encryptionState</a>
</h3>

```typescript
encryptionState: string;
```


the Encryption State of this Data Lake Store Account, such as `Enabled` or `Disabled`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/getStore.ts#L42">property encryptionType</a>
</h3>

```typescript
encryptionType: string;
```


the Encryption Type used for this Data Lake Store Account.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/getStore.ts#L46">property firewallAllowAzureIps</a>
</h3>

```typescript
firewallAllowAzureIps: string;
```


are Azure Service IP's allowed through the firewall?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/getStore.ts#L50">property firewallState</a>
</h3>

```typescript
firewallState: string;
```


the state of the firewall, such as `Enabled` or `Disabled`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/getStore.ts#L63">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/getStore.ts#L51">property location</a>
</h3>

```typescript
location: string;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/getStore.ts#L55">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags to assign to the Data Lake Store.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/getStore.ts#L59">property tier</a>
</h3>

```typescript
tier: string;
```


Current monthly commitment tier for the account.

<h2 class="pdoc-module-header" id="StoreArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L158">interface StoreArgs</a>
</h2>

The set of arguments for constructing a Store resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L162">property encryptionState</a>
</h3>

```typescript
encryptionState?: pulumi.Input<string>;
```


Is Encryption enabled on this Data Lake Store Account? Possible values are `Enabled` or `Disabled`. Defaults to `Enabled`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L166">property encryptionType</a>
</h3>

```typescript
encryptionType?: pulumi.Input<string>;
```


The Encryption Type used for this Data Lake Store Account. Currently can be set to `SystemManaged` when `encryption_state` is `Enabled` - and must be a blank string when it's Disabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L170">property firewallAllowAzureIps</a>
</h3>

```typescript
firewallAllowAzureIps?: pulumi.Input<string>;
```


are Azure Service IP's allowed through the firewall? Possible values are `Enabled` and `Disabled`. Defaults to `Enabled.`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L174">property firewallState</a>
</h3>

```typescript
firewallState?: pulumi.Input<string>;
```


the state of the Firewall. Possible values are `Enabled` and `Disabled`. Defaults to `Enabled.`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L178">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L182">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Data Lake Store. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L186">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the Data Lake Store.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L190">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L194">property tier</a>
</h3>

```typescript
tier?: pulumi.Input<string>;
```


The monthly commitment tier for Data Lake Store. Accepted values are `Consumption`, `Commitment_1TB`, `Commitment_10TB`, `Commitment_100TB`, `Commitment_500TB`, `Commitment_1PB` or `Commitment_5PB`.

<h2 class="pdoc-module-header" id="StoreFileArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/storeFile.ts#L94">interface StoreFileArgs</a>
</h2>

The set of arguments for constructing a StoreFile resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/storeFile.ts#L98">property accountName</a>
</h3>

```typescript
accountName: pulumi.Input<string>;
```


Specifies the name of the Data Lake Store for which the File should created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/storeFile.ts#L102">property localFilePath</a>
</h3>

```typescript
localFilePath: pulumi.Input<string>;
```


The path to the local file to be added to the Data Lake Store.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/storeFile.ts#L106">property remoteFilePath</a>
</h3>

```typescript
remoteFilePath: pulumi.Input<string>;
```


The path created for the file on the Data Lake Store.

<h2 class="pdoc-module-header" id="StoreFileState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/storeFile.ts#L76">interface StoreFileState</a>
</h2>

Input properties used for looking up and filtering StoreFile resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/storeFile.ts#L80">property accountName</a>
</h3>

```typescript
accountName?: pulumi.Input<string>;
```


Specifies the name of the Data Lake Store for which the File should created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/storeFile.ts#L84">property localFilePath</a>
</h3>

```typescript
localFilePath?: pulumi.Input<string>;
```


The path to the local file to be added to the Data Lake Store.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/storeFile.ts#L88">property remoteFilePath</a>
</h3>

```typescript
remoteFilePath?: pulumi.Input<string>;
```


The path created for the file on the Data Lake Store.

<h2 class="pdoc-module-header" id="StoreFirewallRuleArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/storeFirewallRule.ts#L114">interface StoreFirewallRuleArgs</a>
</h2>

The set of arguments for constructing a StoreFirewallRule resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/storeFirewallRule.ts#L118">property accountName</a>
</h3>

```typescript
accountName: pulumi.Input<string>;
```


Specifies the name of the Data Lake Store for which the Firewall Rule should take effect.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/storeFirewallRule.ts#L122">property endIpAddress</a>
</h3>

```typescript
endIpAddress: pulumi.Input<string>;
```


The End IP Address for the firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/storeFirewallRule.ts#L126">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Data Lake Store. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/storeFirewallRule.ts#L130">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the Data Lake Store.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/storeFirewallRule.ts#L134">property startIpAddress</a>
</h3>

```typescript
startIpAddress: pulumi.Input<string>;
```


The Start IP address for the firewall rule.

<h2 class="pdoc-module-header" id="StoreFirewallRuleState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/storeFirewallRule.ts#L88">interface StoreFirewallRuleState</a>
</h2>

Input properties used for looking up and filtering StoreFirewallRule resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/storeFirewallRule.ts#L92">property accountName</a>
</h3>

```typescript
accountName?: pulumi.Input<string>;
```


Specifies the name of the Data Lake Store for which the Firewall Rule should take effect.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/storeFirewallRule.ts#L96">property endIpAddress</a>
</h3>

```typescript
endIpAddress?: pulumi.Input<string>;
```


The End IP Address for the firewall rule.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/storeFirewallRule.ts#L100">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Data Lake Store. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/storeFirewallRule.ts#L104">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the Data Lake Store.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/storeFirewallRule.ts#L108">property startIpAddress</a>
</h3>

```typescript
startIpAddress?: pulumi.Input<string>;
```


The Start IP address for the firewall rule.

<h2 class="pdoc-module-header" id="StoreState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L112">interface StoreState</a>
</h2>

Input properties used for looking up and filtering Store resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L116">property encryptionState</a>
</h3>

```typescript
encryptionState?: pulumi.Input<string>;
```


Is Encryption enabled on this Data Lake Store Account? Possible values are `Enabled` or `Disabled`. Defaults to `Enabled`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L120">property encryptionType</a>
</h3>

```typescript
encryptionType?: pulumi.Input<string>;
```


The Encryption Type used for this Data Lake Store Account. Currently can be set to `SystemManaged` when `encryption_state` is `Enabled` - and must be a blank string when it's Disabled.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L124">property endpoint</a>
</h3>

```typescript
endpoint?: pulumi.Input<string>;
```


The Endpoint for the Data Lake Store.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L128">property firewallAllowAzureIps</a>
</h3>

```typescript
firewallAllowAzureIps?: pulumi.Input<string>;
```


are Azure Service IP's allowed through the firewall? Possible values are `Enabled` and `Disabled`. Defaults to `Enabled.`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L132">property firewallState</a>
</h3>

```typescript
firewallState?: pulumi.Input<string>;
```


the state of the Firewall. Possible values are `Enabled` and `Disabled`. Defaults to `Enabled.`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L136">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L140">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Data Lake Store. Changing this forces a new resource to be created. Has to be between 3 to 24 characters.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L144">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the Data Lake Store.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L148">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/datalake/store.ts#L152">property tier</a>
</h3>

```typescript
tier?: pulumi.Input<string>;
```


The monthly commitment tier for Data Lake Store. Accepted values are `Consumption`, `Commitment_1TB`, `Commitment_10TB`, `Commitment_100TB`, `Commitment_500TB`, `Commitment_1PB` or `Commitment_5PB`.

