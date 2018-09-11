---
title: Module recoveryservices
---

<a href="../index.html">@pulumi/azure</a> &gt; recoveryservices

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Vault">class Vault</a>
* <a href="#getVault">function getVault</a>
* <a href="#GetVaultArgs">interface GetVaultArgs</a>
* <a href="#GetVaultResult">interface GetVaultResult</a>
* <a href="#VaultArgs">interface VaultArgs</a>
* <a href="#VaultState">interface VaultState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/getVault.ts">recoveryservices/getVault.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/vault.ts">recoveryservices/vault.ts</a> 


<h2 class="pdoc-module-header" id="Vault">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/vault.ts#L10">class Vault</a>
</h2>

Create an Recovery Services Vault.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/vault.ts#L42">constructor</a>
</h3>

```typescript
new Vault(name: string, args: VaultArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Vault resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/vault.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VaultState): Vault
```


Get an existing Vault resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/vault.ts#L26">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/vault.ts#L30">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Recovery Services Vault. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/vault.ts#L34">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the Recovery Services Vault. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/vault.ts#L38">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<string>;
```


Sets the vault's SKU. Possible values include: `Standard`, `RS0`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/vault.ts#L42">property tags</a>
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

<h2 class="pdoc-module-header" id="getVault">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/getVault.ts#L10">function getVault</a>
</h2>

```typescript
getVault(args: GetVaultArgs, opts?: pulumi.InvokeOptions): Promise<GetVaultResult>
```


Use this data source to access the properties of a Recovery Services Vault.

<h2 class="pdoc-module-header" id="GetVaultArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/getVault.ts#L20">interface GetVaultArgs</a>
</h2>

A collection of arguments for invoking getVault.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/getVault.ts#L24">property name</a>
</h3>

```typescript
name: string;
```


Specifies the name of the Recovery Services Vault.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/getVault.ts#L28">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


The name of the resource group in which the Recovery Services Vault resides.

<h2 class="pdoc-module-header" id="GetVaultResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/getVault.ts#L34">interface GetVaultResult</a>
</h2>

A collection of values returned by getVault.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/getVault.ts#L50">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/getVault.ts#L38">property location</a>
</h3>

```typescript
location: string;
```


The Azure location where the resource resides.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/getVault.ts#L42">property sku</a>
</h3>

```typescript
sku: string;
```


The vault's current SKU.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/getVault.ts#L46">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags assigned to the resource.

<h2 class="pdoc-module-header" id="VaultArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/vault.ts#L111">interface VaultArgs</a>
</h2>

The set of arguments for constructing a Vault resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/vault.ts#L115">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/vault.ts#L119">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Recovery Services Vault. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/vault.ts#L123">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the Recovery Services Vault. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/vault.ts#L127">property sku</a>
</h3>

```typescript
sku: pulumi.Input<string>;
```


Sets the vault's SKU. Possible values include: `Standard`, `RS0`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/vault.ts#L131">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="VaultState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/vault.ts#L85">interface VaultState</a>
</h2>

Input properties used for looking up and filtering Vault resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/vault.ts#L89">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/vault.ts#L93">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Recovery Services Vault. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/vault.ts#L97">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the Recovery Services Vault. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/vault.ts#L101">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<string>;
```


Sets the vault's SKU. Possible values include: `Standard`, `RS0`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/vault.ts#L105">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

