---
title: Module keyvault
---

<a href="..">@pulumi/azure</a>

<h2 class="pdoc-module-header">Index</h2>

* <a href="#Certifiate">class Certifiate</a>
* <a href="#Key">class Key</a>
* <a href="#KeyVault">class KeyVault</a>
* <a href="#Secret">class Secret</a>
* <a href="#getAccessPolicy">function getAccessPolicy</a>
* <a href="#CertifiateArgs">interface CertifiateArgs</a>
* <a href="#CertifiateState">interface CertifiateState</a>
* <a href="#GetAccessPolicyArgs">interface GetAccessPolicyArgs</a>
* <a href="#GetAccessPolicyResult">interface GetAccessPolicyResult</a>
* <a href="#KeyArgs">interface KeyArgs</a>
* <a href="#KeyState">interface KeyState</a>
* <a href="#KeyVaultArgs">interface KeyVaultArgs</a>
* <a href="#KeyVaultState">interface KeyVaultState</a>
* <a href="#SecretArgs">interface SecretArgs</a>
* <a href="#SecretState">interface SecretState</a>

<a href="/keyvault/certifiate.ts">keyvault/certifiate.ts</a> <a href="/keyvault/getAccessPolicy.ts">keyvault/getAccessPolicy.ts</a> <a href="/keyvault/key.ts">keyvault/key.ts</a> <a href="/keyvault/keyVault.ts">keyvault/keyVault.ts</a> <a href="/keyvault/secret.ts">keyvault/secret.ts</a> 

<h2 class="pdoc-module-header">Modules</h2>


<h2 class="pdoc-module-header" id="Certifiate">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/certifiate.ts#L9">class Certifiate</a>
</h2>

Manages a Key Vault Certificate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/certifiate.ts#L45">constructor</a>
</h3>

```typescript
new Certifiate(name: string, args: CertifiateArgs, opts?: pulumi.ResourceOptions)
```


Create a Certifiate resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Certifiate(name: string, state?: CertifiateState, opts?: pulumi.ResourceOptions)
```


Create a Certifiate resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/certifiate.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CertifiateState): Certifiate
```


Get an existing Certifiate resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/certifiate.ts#L25">property certificate</a>
</h3>

```typescript
public certificate: pulumi.Output<{ ... } | undefined>;
```


A `certificate` block as defined below, used to Import an existing certificate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/certifiate.ts#L29">property certificatePolicy</a>
</h3>

```typescript
public certificatePolicy: pulumi.Output<{ ... }>;
```


A `certificate_policy` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/certifiate.ts#L33">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the Certificate Issuer. Possible values include `Self`, or the name of a certificate issuing authority supported by Azure. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/certifiate.ts#L37">property tags</a>
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

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/certifiate.ts#L41">property vaultUri</a>
</h3>

```typescript
public vaultUri: pulumi.Output<string>;
```


Specifies the URI used to access the Key Vault instance, available on the `azurerm_key_vault` resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/certifiate.ts#L45">property version</a>
</h3>

```typescript
public version: pulumi.Output<string>;
```


The current version of the Key Vault Certificate.

<h2 class="pdoc-module-header" id="Key">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/key.ts#L9">class Key</a>
</h2>

Manages a Key Vault Key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/key.ts#L57">constructor</a>
</h3>

```typescript
new Key(name: string, args: KeyArgs, opts?: pulumi.ResourceOptions)
```


Create a Key resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Key(name: string, state?: KeyState, opts?: pulumi.ResourceOptions)
```


Create a Key resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/key.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: KeyState): Key
```


Get an existing Key resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/key.ts#L25">property e</a>
</h3>

```typescript
public e: pulumi.Output<string>;
```


The RSA public exponent of this Key Vault Key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/key.ts#L29">property keyOpts</a>
</h3>

```typescript
public keyOpts: pulumi.Output<string[]>;
```


A list of JSON web key operations. Possible values include: `decrypt`, `encrypt`, `sign`, `unwrapKey`, `verify` and `wrapKey`. Please note these values are case sensitive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/key.ts#L33">property keySize</a>
</h3>

```typescript
public keySize: pulumi.Output<number>;
```


Specifies the Size of the Key to create in bytes. For example, 1024 or 2048. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/key.ts#L37">property keyType</a>
</h3>

```typescript
public keyType: pulumi.Output<string>;
```


Specifies the Key Type to use for this Key Vault Key. Possible values are `EC` (Elliptic Curve), `Oct` (Octet), `RSA` and `RSA-HSM`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/key.ts#L41">property n</a>
</h3>

```typescript
public n: pulumi.Output<string>;
```


The RSA modulus of this Key Vault Key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/key.ts#L45">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Key Vault Key. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/key.ts#L49">property tags</a>
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

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/key.ts#L53">property vaultUri</a>
</h3>

```typescript
public vaultUri: pulumi.Output<string>;
```


Specifies the URI used to access the Key Vault instance, available on the `azurerm_key_vault` resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/key.ts#L57">property version</a>
</h3>

```typescript
public version: pulumi.Output<string>;
```


The current version of the Key Vault Key.

<h2 class="pdoc-module-header" id="KeyVault">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/keyVault.ts#L9">class KeyVault</a>
</h2>

Create a Key Vault.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/keyVault.ts#L77">constructor</a>
</h3>

```typescript
new KeyVault(name: string, args: KeyVaultArgs, opts?: pulumi.ResourceOptions)
```


Create a KeyVault resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new KeyVault(name: string, state?: KeyVaultState, opts?: pulumi.ResourceOptions)
```


Create a KeyVault resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/keyVault.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: KeyVaultState): KeyVault
```


Get an existing KeyVault resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/keyVault.ts#L26">property accessPolicies</a>
</h3>

```typescript
public accessPolicies: pulumi.Output<{ ... }[] | undefined>;
```


An access policy block as described below. At least
one policy is required up to a maximum of 16.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/keyVault.ts#L32">property enabledForDeployment</a>
</h3>

```typescript
public enabledForDeployment: pulumi.Output<boolean | undefined>;
```


Boolean flag to specify whether Azure Virtual
Machines are permitted to retrieve certificates stored as secrets from the key
vault. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/keyVault.ts#L38">property enabledForDiskEncryption</a>
</h3>

```typescript
public enabledForDiskEncryption: pulumi.Output<boolean | undefined>;
```


Boolean flag to specify whether Azure
Disk Encryption is permitted to retrieve secrets from the vault and unwrap keys.
Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/keyVault.ts#L44">property enabledForTemplateDeployment</a>
</h3>

```typescript
public enabledForTemplateDeployment: pulumi.Output<boolean | undefined>;
```


Boolean flag to specify whether
Azure Resource Manager is permitted to retrieve secrets from the key vault.
Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/keyVault.ts#L49">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/keyVault.ts#L54">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


SKU name to specify whether the key vault is a `standard`
or `premium` vault.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/keyVault.ts#L59">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/keyVault.ts#L63">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<{ ... }[]>;
```


An SKU block as described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/keyVault.ts#L67">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/keyVault.ts#L73">property tenantId</a>
</h3>

```typescript
public tenantId: pulumi.Output<string>;
```


The Azure Active Directory tenant ID that should be used
for authenticating requests to the key vault. Must match the `tenant_id` used
above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L15">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/keyVault.ts#L77">property vaultUri</a>
</h3>

```typescript
public vaultUri: pulumi.Output<string>;
```


The URI of the vault for performing operations on keys and secrets.

<h2 class="pdoc-module-header" id="Secret">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/secret.ts#L9">class Secret</a>
</h2>

Manages a Key Vault Secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/secret.ts#L45">constructor</a>
</h3>

```typescript
new Secret(name: string, args: SecretArgs, opts?: pulumi.ResourceOptions)
```


Create a Secret resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.


```typescript
new Secret(name: string, state?: SecretState, opts?: pulumi.ResourceOptions)
```


Create a Secret resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `state` The state to use when looking up an instance of this resource.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/secret.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SecretState): Secret
```


Get an existing Secret resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/secret.ts#L25">property contentType</a>
</h3>

```typescript
public contentType: pulumi.Output<string | undefined>;
```


Specifies the content type for the Key Vault Secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L67">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/secret.ts#L29">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Key Vault Secret. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/secret.ts#L33">property tags</a>
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

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/secret.ts#L37">property value</a>
</h3>

```typescript
public value: pulumi.Output<string>;
```


Specifies the value of the Key Vault Secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/secret.ts#L41">property vaultUri</a>
</h3>

```typescript
public vaultUri: pulumi.Output<string>;
```


Specifies the URI used to access the Key Vault instance, available on the `azurerm_key_vault` resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/secret.ts#L45">property version</a>
</h3>

```typescript
public version: pulumi.Output<string>;
```


The current version of the Key Vault Secret.

<h2 class="pdoc-module-header" id="getAccessPolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/getAccessPolicy.ts#L9">function getAccessPolicy</a>
</h2>

```typescript
getAccessPolicy(args: GetAccessPolicyArgs): Promise<GetAccessPolicyResult>
```


Use this data source to access information about the permissions from the Management Key Vault Templates.

<h2 class="pdoc-module-header" id="CertifiateArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/certifiate.ts#L119">interface CertifiateArgs</a>
</h2>

The set of arguments for constructing a Certifiate resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/certifiate.ts#L123">property certificate</a>
</h3>

```typescript
certificate?: pulumi.Input<{ ... }>;
```


A `certificate` block as defined below, used to Import an existing certificate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/certifiate.ts#L127">property certificatePolicy</a>
</h3>

```typescript
certificatePolicy: pulumi.Input<{ ... }>;
```


A `certificate_policy` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/certifiate.ts#L131">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Certificate Issuer. Possible values include `Self`, or the name of a certificate issuing authority supported by Azure. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/certifiate.ts#L135">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/certifiate.ts#L139">property vaultUri</a>
</h3>

```typescript
vaultUri: pulumi.Input<string>;
```


Specifies the URI used to access the Key Vault instance, available on the `azurerm_key_vault` resource.

<h2 class="pdoc-module-header" id="CertifiateState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/certifiate.ts#L89">interface CertifiateState</a>
</h2>

Input properties used for looking up and filtering Certifiate resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/certifiate.ts#L93">property certificate</a>
</h3>

```typescript
certificate?: pulumi.Input<{ ... }>;
```


A `certificate` block as defined below, used to Import an existing certificate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/certifiate.ts#L97">property certificatePolicy</a>
</h3>

```typescript
certificatePolicy?: pulumi.Input<{ ... }>;
```


A `certificate_policy` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/certifiate.ts#L101">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Certificate Issuer. Possible values include `Self`, or the name of a certificate issuing authority supported by Azure. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/certifiate.ts#L105">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/certifiate.ts#L109">property vaultUri</a>
</h3>

```typescript
vaultUri?: pulumi.Input<string>;
```


Specifies the URI used to access the Key Vault instance, available on the `azurerm_key_vault` resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/certifiate.ts#L113">property version</a>
</h3>

```typescript
version?: pulumi.Input<string>;
```


The current version of the Key Vault Certificate.

<h2 class="pdoc-module-header" id="GetAccessPolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/getAccessPolicy.ts#L18">interface GetAccessPolicyArgs</a>
</h2>

A collection of arguments for invoking getAccessPolicy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/getAccessPolicy.ts#L24">property name</a>
</h3>

```typescript
name: pulumi.Input<string>;
```


Specifies the name of the Management Tempalte. Possible values are: `Key Management`,
`Secret Management`, `Certificate Management`, `Key & Secret Management`, `Key & Certificate Management`,
`Secret & Certificate Management`,  `Key, Secret, & Certificate Management`

<h2 class="pdoc-module-header" id="GetAccessPolicyResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/getAccessPolicy.ts#L30">interface GetAccessPolicyResult</a>
</h2>

A collection of values returned by getAccessPolicy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/getAccessPolicy.ts#L34">property certificatePermissions</a>
</h3>

```typescript
certificatePermissions: string[];
```


the certificate permissions for the access policy

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/getAccessPolicy.ts#L38">property keyPermissions</a>
</h3>

```typescript
keyPermissions: string[];
```


the key permissions for the access policy

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/getAccessPolicy.ts#L42">property secretPermissions</a>
</h3>

```typescript
secretPermissions: string[];
```


the secret permissions for the access policy

<h2 class="pdoc-module-header" id="KeyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/key.ts#L155">interface KeyArgs</a>
</h2>

The set of arguments for constructing a Key resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/key.ts#L159">property keyOpts</a>
</h3>

```typescript
keyOpts: pulumi.Input<pulumi.Input<string>[]>;
```


A list of JSON web key operations. Possible values include: `decrypt`, `encrypt`, `sign`, `unwrapKey`, `verify` and `wrapKey`. Please note these values are case sensitive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/key.ts#L163">property keySize</a>
</h3>

```typescript
keySize: pulumi.Input<number>;
```


Specifies the Size of the Key to create in bytes. For example, 1024 or 2048. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/key.ts#L167">property keyType</a>
</h3>

```typescript
keyType: pulumi.Input<string>;
```


Specifies the Key Type to use for this Key Vault Key. Possible values are `EC` (Elliptic Curve), `Oct` (Octet), `RSA` and `RSA-HSM`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/key.ts#L171">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Key Vault Key. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/key.ts#L175">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/key.ts#L179">property vaultUri</a>
</h3>

```typescript
vaultUri: pulumi.Input<string>;
```


Specifies the URI used to access the Key Vault instance, available on the `azurerm_key_vault` resource.

<h2 class="pdoc-module-header" id="KeyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/key.ts#L113">interface KeyState</a>
</h2>

Input properties used for looking up and filtering Key resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/key.ts#L117">property e</a>
</h3>

```typescript
e?: pulumi.Input<string>;
```


The RSA public exponent of this Key Vault Key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/key.ts#L121">property keyOpts</a>
</h3>

```typescript
keyOpts?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of JSON web key operations. Possible values include: `decrypt`, `encrypt`, `sign`, `unwrapKey`, `verify` and `wrapKey`. Please note these values are case sensitive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/key.ts#L125">property keySize</a>
</h3>

```typescript
keySize?: pulumi.Input<number>;
```


Specifies the Size of the Key to create in bytes. For example, 1024 or 2048. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/key.ts#L129">property keyType</a>
</h3>

```typescript
keyType?: pulumi.Input<string>;
```


Specifies the Key Type to use for this Key Vault Key. Possible values are `EC` (Elliptic Curve), `Oct` (Octet), `RSA` and `RSA-HSM`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/key.ts#L133">property n</a>
</h3>

```typescript
n?: pulumi.Input<string>;
```


The RSA modulus of this Key Vault Key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/key.ts#L137">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Key Vault Key. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/key.ts#L141">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/key.ts#L145">property vaultUri</a>
</h3>

```typescript
vaultUri?: pulumi.Input<string>;
```


Specifies the URI used to access the Key Vault instance, available on the `azurerm_key_vault` resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/key.ts#L149">property version</a>
</h3>

```typescript
version?: pulumi.Input<string>;
```


The current version of the Key Vault Key.

<h2 class="pdoc-module-header" id="KeyVaultArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/keyVault.ts#L199">interface KeyVaultArgs</a>
</h2>

The set of arguments for constructing a KeyVault resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/keyVault.ts#L204">property accessPolicies</a>
</h3>

```typescript
accessPolicies?: pulumi.Input<{ ... }[]>;
```


An access policy block as described below. At least
one policy is required up to a maximum of 16.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/keyVault.ts#L210">property enabledForDeployment</a>
</h3>

```typescript
enabledForDeployment?: pulumi.Input<boolean>;
```


Boolean flag to specify whether Azure Virtual
Machines are permitted to retrieve certificates stored as secrets from the key
vault. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/keyVault.ts#L216">property enabledForDiskEncryption</a>
</h3>

```typescript
enabledForDiskEncryption?: pulumi.Input<boolean>;
```


Boolean flag to specify whether Azure
Disk Encryption is permitted to retrieve secrets from the vault and unwrap keys.
Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/keyVault.ts#L222">property enabledForTemplateDeployment</a>
</h3>

```typescript
enabledForTemplateDeployment?: pulumi.Input<boolean>;
```


Boolean flag to specify whether
Azure Resource Manager is permitted to retrieve secrets from the key vault.
Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/keyVault.ts#L227">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/keyVault.ts#L232">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


SKU name to specify whether the key vault is a `standard`
or `premium` vault.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/keyVault.ts#L237">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/keyVault.ts#L241">property sku</a>
</h3>

```typescript
sku: pulumi.Input<{ ... }[]>;
```


An SKU block as described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/keyVault.ts#L245">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/keyVault.ts#L251">property tenantId</a>
</h3>

```typescript
tenantId: pulumi.Input<string>;
```


The Azure Active Directory tenant ID that should be used
for authenticating requests to the key vault. Must match the `tenant_id` used
above.

<h2 class="pdoc-module-header" id="KeyVaultState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/keyVault.ts#L137">interface KeyVaultState</a>
</h2>

Input properties used for looking up and filtering KeyVault resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/keyVault.ts#L142">property accessPolicies</a>
</h3>

```typescript
accessPolicies?: pulumi.Input<{ ... }[]>;
```


An access policy block as described below. At least
one policy is required up to a maximum of 16.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/keyVault.ts#L148">property enabledForDeployment</a>
</h3>

```typescript
enabledForDeployment?: pulumi.Input<boolean>;
```


Boolean flag to specify whether Azure Virtual
Machines are permitted to retrieve certificates stored as secrets from the key
vault. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/keyVault.ts#L154">property enabledForDiskEncryption</a>
</h3>

```typescript
enabledForDiskEncryption?: pulumi.Input<boolean>;
```


Boolean flag to specify whether Azure
Disk Encryption is permitted to retrieve secrets from the vault and unwrap keys.
Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/keyVault.ts#L160">property enabledForTemplateDeployment</a>
</h3>

```typescript
enabledForTemplateDeployment?: pulumi.Input<boolean>;
```


Boolean flag to specify whether
Azure Resource Manager is permitted to retrieve secrets from the key vault.
Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/keyVault.ts#L165">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/keyVault.ts#L170">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


SKU name to specify whether the key vault is a `standard`
or `premium` vault.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/keyVault.ts#L175">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/keyVault.ts#L179">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<{ ... }[]>;
```


An SKU block as described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/keyVault.ts#L183">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/keyVault.ts#L189">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The Azure Active Directory tenant ID that should be used
for authenticating requests to the key vault. Must match the `tenant_id` used
above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/keyVault.ts#L193">property vaultUri</a>
</h3>

```typescript
vaultUri?: pulumi.Input<string>;
```


The URI of the vault for performing operations on keys and secrets.

<h2 class="pdoc-module-header" id="SecretArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/secret.ts#L119">interface SecretArgs</a>
</h2>

The set of arguments for constructing a Secret resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/secret.ts#L123">property contentType</a>
</h3>

```typescript
contentType?: pulumi.Input<string>;
```


Specifies the content type for the Key Vault Secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/secret.ts#L127">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Key Vault Secret. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/secret.ts#L131">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/secret.ts#L135">property value</a>
</h3>

```typescript
value: pulumi.Input<string>;
```


Specifies the value of the Key Vault Secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/secret.ts#L139">property vaultUri</a>
</h3>

```typescript
vaultUri: pulumi.Input<string>;
```


Specifies the URI used to access the Key Vault instance, available on the `azurerm_key_vault` resource.

<h2 class="pdoc-module-header" id="SecretState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/secret.ts#L89">interface SecretState</a>
</h2>

Input properties used for looking up and filtering Secret resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/secret.ts#L93">property contentType</a>
</h3>

```typescript
contentType?: pulumi.Input<string>;
```


Specifies the content type for the Key Vault Secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/secret.ts#L97">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Key Vault Secret. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/secret.ts#L101">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/secret.ts#L105">property value</a>
</h3>

```typescript
value?: pulumi.Input<string>;
```


Specifies the value of the Key Vault Secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/secret.ts#L109">property vaultUri</a>
</h3>

```typescript
vaultUri?: pulumi.Input<string>;
```


Specifies the URI used to access the Key Vault instance, available on the `azurerm_key_vault` resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/pack/nodejs/keyvault/secret.ts#L113">property version</a>
</h3>

```typescript
version?: pulumi.Input<string>;
```


The current version of the Key Vault Secret.

