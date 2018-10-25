---
title: Module recoveryservices
---

<a href="../index.html">@pulumi/azure</a> &gt; recoveryservices

<h2 class="pdoc-module-header">Index</h2>

* <a href="#ProtectedVM">class ProtectedVM</a>
* <a href="#ProtectionPolicyVM">class ProtectionPolicyVM</a>
* <a href="#Vault">class Vault</a>
* <a href="#getVault">function getVault</a>
* <a href="#GetVaultArgs">interface GetVaultArgs</a>
* <a href="#GetVaultResult">interface GetVaultResult</a>
* <a href="#ProtectedVMArgs">interface ProtectedVMArgs</a>
* <a href="#ProtectedVMState">interface ProtectedVMState</a>
* <a href="#ProtectionPolicyVMArgs">interface ProtectionPolicyVMArgs</a>
* <a href="#ProtectionPolicyVMState">interface ProtectionPolicyVMState</a>
* <a href="#VaultArgs">interface VaultArgs</a>
* <a href="#VaultState">interface VaultState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/getVault.ts">recoveryservices/getVault.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectedVM.ts">recoveryservices/protectedVM.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectionPolicyVM.ts">recoveryservices/protectionPolicyVM.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/vault.ts">recoveryservices/vault.ts</a> 


<h2 class="pdoc-module-header" id="ProtectedVM">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectedVM.ts#L10">class ProtectedVM</a>
</h2>

Manages an Recovery Protected VM.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectedVM.ts#L39">constructor</a>
</h3>

```typescript
new ProtectedVM(name: string, args: ProtectedVMArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ProtectedVM resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectedVM.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ProtectedVMState): ProtectedVM
```


Get an existing ProtectedVM resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectedVM.ts#L23">property backupPolicyId</a>
</h3>

```typescript
public backupPolicyId: pulumi.Output<string | undefined>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectedVM.ts#L27">property recoveryVaultName</a>
</h3>

```typescript
public recoveryVaultName: pulumi.Output<string>;
```


Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectedVM.ts#L31">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the Recovery Services Protected VM. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectedVM.ts#L35">property sourceVmId</a>
</h3>

```typescript
public sourceVmId: pulumi.Output<string>;
```


Specifies the ID of the VM to backup. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectedVM.ts#L39">property tags</a>
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

<h2 class="pdoc-module-header" id="ProtectionPolicyVM">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectionPolicyVM.ts#L10">class ProtectionPolicyVM</a>
</h2>

Manages an Recovery Services VM Protection Policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectionPolicyVM.ts#L55">constructor</a>
</h3>

```typescript
new ProtectionPolicyVM(name: string, args: ProtectionPolicyVMArgs, opts?: pulumi.CustomResourceOptions)
```


Create a ProtectionPolicyVM resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectionPolicyVM.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ProtectionPolicyVMState): ProtectionPolicyVM
```


Get an existing ProtectionPolicyVM resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectionPolicyVM.ts#L26">property backup</a>
</h3>

```typescript
public backup: pulumi.Output<{ ... }>;
```


Configures the Policy backup frequecent, times & days as documented in the `backup` block below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectionPolicyVM.ts#L30">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Recovery Services Vault Policy. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectionPolicyVM.ts#L34">property recoveryVaultName</a>
</h3>

```typescript
public recoveryVaultName: pulumi.Output<string>;
```


Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectionPolicyVM.ts#L38">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to create the Recovery Services Protected VM. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectionPolicyVM.ts#L42">property retentionDaily</a>
</h3>

```typescript
public retentionDaily: pulumi.Output<{ ... } | undefined>;
```


Configures the policy daily retention as documented in the `retention_daily` block below. Required when backup frequency is `Daily`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectionPolicyVM.ts#L46">property retentionMonthly</a>
</h3>

```typescript
public retentionMonthly: pulumi.Output<{ ... } | undefined>;
```


Configures the policy monthly retention as documented in the `retention_monthly` block below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectionPolicyVM.ts#L50">property retentionWeekly</a>
</h3>

```typescript
public retentionWeekly: pulumi.Output<{ ... } | undefined>;
```


Configures the policy weekly retention as documented in the `retention_weekly` block below. Required when backup frequency is `Weekly`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectionPolicyVM.ts#L54">property retentionYearly</a>
</h3>

```typescript
public retentionYearly: pulumi.Output<{ ... } | undefined>;
```


Configures the policy yearly retention as documented in the `retention_yearly` block below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectionPolicyVM.ts#L55">property tags</a>
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

<h2 class="pdoc-module-header" id="Vault">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/vault.ts#L10">class Vault</a>
</h2>

Manage an Recovery Services Vault.

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


Use this data source to access information about an existing Recovery Services Vault.

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

<h2 class="pdoc-module-header" id="ProtectedVMArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectedVM.ts#L105">interface ProtectedVMArgs</a>
</h2>

The set of arguments for constructing a ProtectedVM resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectedVM.ts#L106">property backupPolicyId</a>
</h3>

```typescript
backupPolicyId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectedVM.ts#L110">property recoveryVaultName</a>
</h3>

```typescript
recoveryVaultName: pulumi.Input<string>;
```


Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectedVM.ts#L114">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the Recovery Services Protected VM. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectedVM.ts#L118">property sourceVmId</a>
</h3>

```typescript
sourceVmId: pulumi.Input<string>;
```


Specifies the ID of the VM to backup. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectedVM.ts#L122">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ProtectedVMState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectedVM.ts#L82">interface ProtectedVMState</a>
</h2>

Input properties used for looking up and filtering ProtectedVM resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectedVM.ts#L83">property backupPolicyId</a>
</h3>

```typescript
backupPolicyId?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectedVM.ts#L87">property recoveryVaultName</a>
</h3>

```typescript
recoveryVaultName?: pulumi.Input<string>;
```


Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectedVM.ts#L91">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the Recovery Services Protected VM. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectedVM.ts#L95">property sourceVmId</a>
</h3>

```typescript
sourceVmId?: pulumi.Input<string>;
```


Specifies the ID of the VM to backup. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectedVM.ts#L99">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h2 class="pdoc-module-header" id="ProtectionPolicyVMArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectionPolicyVM.ts#L145">interface ProtectionPolicyVMArgs</a>
</h2>

The set of arguments for constructing a ProtectionPolicyVM resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectionPolicyVM.ts#L149">property backup</a>
</h3>

```typescript
backup: pulumi.Input<{ ... }>;
```


Configures the Policy backup frequecent, times & days as documented in the `backup` block below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectionPolicyVM.ts#L153">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Recovery Services Vault Policy. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectionPolicyVM.ts#L157">property recoveryVaultName</a>
</h3>

```typescript
recoveryVaultName: pulumi.Input<string>;
```


Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectionPolicyVM.ts#L161">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to create the Recovery Services Protected VM. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectionPolicyVM.ts#L165">property retentionDaily</a>
</h3>

```typescript
retentionDaily?: pulumi.Input<{ ... }>;
```


Configures the policy daily retention as documented in the `retention_daily` block below. Required when backup frequency is `Daily`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectionPolicyVM.ts#L169">property retentionMonthly</a>
</h3>

```typescript
retentionMonthly?: pulumi.Input<{ ... }>;
```


Configures the policy monthly retention as documented in the `retention_monthly` block below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectionPolicyVM.ts#L173">property retentionWeekly</a>
</h3>

```typescript
retentionWeekly?: pulumi.Input<{ ... }>;
```


Configures the policy weekly retention as documented in the `retention_weekly` block below. Required when backup frequency is `Weekly`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectionPolicyVM.ts#L177">property retentionYearly</a>
</h3>

```typescript
retentionYearly?: pulumi.Input<{ ... }>;
```


Configures the policy yearly retention as documented in the `retention_yearly` block below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectionPolicyVM.ts#L178">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

<h2 class="pdoc-module-header" id="ProtectionPolicyVMState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectionPolicyVM.ts#L106">interface ProtectionPolicyVMState</a>
</h2>

Input properties used for looking up and filtering ProtectionPolicyVM resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectionPolicyVM.ts#L110">property backup</a>
</h3>

```typescript
backup?: pulumi.Input<{ ... }>;
```


Configures the Policy backup frequecent, times & days as documented in the `backup` block below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectionPolicyVM.ts#L114">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Recovery Services Vault Policy. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectionPolicyVM.ts#L118">property recoveryVaultName</a>
</h3>

```typescript
recoveryVaultName?: pulumi.Input<string>;
```


Specifies the name of the Recovery Services Vault to use. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectionPolicyVM.ts#L122">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to create the Recovery Services Protected VM. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectionPolicyVM.ts#L126">property retentionDaily</a>
</h3>

```typescript
retentionDaily?: pulumi.Input<{ ... }>;
```


Configures the policy daily retention as documented in the `retention_daily` block below. Required when backup frequency is `Daily`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectionPolicyVM.ts#L130">property retentionMonthly</a>
</h3>

```typescript
retentionMonthly?: pulumi.Input<{ ... }>;
```


Configures the policy monthly retention as documented in the `retention_monthly` block below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectionPolicyVM.ts#L134">property retentionWeekly</a>
</h3>

```typescript
retentionWeekly?: pulumi.Input<{ ... }>;
```


Configures the policy weekly retention as documented in the `retention_weekly` block below. Required when backup frequency is `Weekly`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectionPolicyVM.ts#L138">property retentionYearly</a>
</h3>

```typescript
retentionYearly?: pulumi.Input<{ ... }>;
```


Configures the policy yearly retention as documented in the `retention_yearly` block below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/recoveryservices/protectionPolicyVM.ts#L139">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```

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

