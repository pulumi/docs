---
title: Module keyvault
---

<a href="../index.html">@pulumi/azure</a> &gt; keyvault

<h2 class="pdoc-module-header">Index</h2>

* <a href="#AccessPolicy">class AccessPolicy</a>
* <a href="#Certifiate">class Certifiate</a>
* <a href="#Key">class Key</a>
* <a href="#KeyVault">class KeyVault</a>
* <a href="#Secret">class Secret</a>
* <a href="#getAccessPolicy">function getAccessPolicy</a>
* <a href="#getKeyVault">function getKeyVault</a>
* <a href="#getSecret">function getSecret</a>
* <a href="#AccessPolicyArgs">interface AccessPolicyArgs</a>
* <a href="#AccessPolicyState">interface AccessPolicyState</a>
* <a href="#CertifiateArgs">interface CertifiateArgs</a>
* <a href="#CertifiateState">interface CertifiateState</a>
* <a href="#GetAccessPolicyArgs">interface GetAccessPolicyArgs</a>
* <a href="#GetAccessPolicyResult">interface GetAccessPolicyResult</a>
* <a href="#GetKeyVaultArgs">interface GetKeyVaultArgs</a>
* <a href="#GetKeyVaultResult">interface GetKeyVaultResult</a>
* <a href="#GetSecretArgs">interface GetSecretArgs</a>
* <a href="#GetSecretResult">interface GetSecretResult</a>
* <a href="#KeyArgs">interface KeyArgs</a>
* <a href="#KeyState">interface KeyState</a>
* <a href="#KeyVaultArgs">interface KeyVaultArgs</a>
* <a href="#KeyVaultState">interface KeyVaultState</a>
* <a href="#SecretArgs">interface SecretArgs</a>
* <a href="#SecretState">interface SecretState</a>

<a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/accessPolicy.ts">keyvault/accessPolicy.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/certifiate.ts">keyvault/certifiate.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/getAccessPolicy.ts">keyvault/getAccessPolicy.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/getKeyVault.ts">keyvault/getKeyVault.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/getSecret.ts">keyvault/getSecret.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/key.ts">keyvault/key.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts">keyvault/keyVault.ts</a> <a href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/secret.ts">keyvault/secret.ts</a> 


<h2 class="pdoc-module-header" id="AccessPolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/accessPolicy.ts#L13">class AccessPolicy</a>
</h2>

Manages a Key Vault Access Policy.

~> **NOTE:** It's possible to define Key Vault Access Policies both within [the `azurerm_key_vault` resource](key_vault.html) via the `access_policy` block and by using [the `azurerm_key_vault_access_policy` resource](key_vault_access_policy.html). However it's not possible to use both methods to manage Access Policies within a KeyVault, since there'll be conflicts.

-> **NOTE:** Azure permits a maximum of 16 Access Policies per Key Vault - [more information can be found in this document](https://docs.microsoft.com/en-us/azure/key-vault/key-vault-secure-your-key-vault#data-plane-access-control).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/accessPolicy.ts#L69">constructor</a>
</h3>

```typescript
new AccessPolicy(name: string, args: AccessPolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a AccessPolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/accessPolicy.ts#L22">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AccessPolicyState): AccessPolicy
```


Get an existing AccessPolicy resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/accessPolicy.ts#L29">property applicationId</a>
</h3>

```typescript
public applicationId: pulumi.Output<string | undefined>;
```


The object ID of an Application in Azure Active Directory.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/accessPolicy.ts#L35">property certificatePermissions</a>
</h3>

```typescript
public certificatePermissions: pulumi.Output<string[] | undefined>;
```


List of certificate permissions, must be one or more from
the following: `create`, `delete`, `deleteissuers`, `get`, `getissuers`, `import`, `list`, `listissuers`,
`managecontacts`, `manageissuers`, `purge`, `recover`, `setissuers` and `update`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/accessPolicy.ts#L41">property keyPermissions</a>
</h3>

```typescript
public keyPermissions: pulumi.Output<string[]>;
```


List of key permissions, must be one or more from
the following: `backup`, `create`, `decrypt`, `delete`, `encrypt`, `get`, `import`, `list`, `purge`,
`recover`, `restore`, `sign`, `unwrapKey`, `update`, `verify` and `wrapKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/accessPolicy.ts#L48">property objectId</a>
</h3>

```typescript
public objectId: pulumi.Output<string>;
```


The object ID of a user, service principal or security
group in the Azure Active Directory tenant for the vault. The object ID must
be unique for the list of access policies. Changing this forces a new resource
to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/accessPolicy.ts#L53">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/accessPolicy.ts#L58">property secretPermissions</a>
</h3>

```typescript
public secretPermissions: pulumi.Output<string[]>;
```


List of secret permissions, must be one or more
from the following: `backup`, `delete`, `get`, `list`, `purge`, `recover`, `restore` and `set`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/accessPolicy.ts#L64">property tenantId</a>
</h3>

```typescript
public tenantId: pulumi.Output<string>;
```


The Azure Active Directory tenant ID that should be used
for authenticating requests to the key vault. Changing this forces a new resource
to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/accessPolicy.ts#L69">property vaultName</a>
</h3>

```typescript
public vaultName: pulumi.Output<string>;
```


Specifies the name of the Key Vault resource. Changing this
forces a new resource to be created.

<h2 class="pdoc-module-header" id="Certifiate">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/certifiate.ts#L9">class Certifiate</a>
</h2>

Manages a Key Vault Certificate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/certifiate.ts#L53">constructor</a>
</h3>

```typescript
new Certifiate(name: string, args: CertifiateArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Certifiate resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/certifiate.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CertifiateState): Certifiate
```


Get an existing Certifiate resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/certifiate.ts#L25">property certificate</a>
</h3>

```typescript
public certificate: pulumi.Output<{ ... } | undefined>;
```


A `certificate` block as defined below, used to Import an existing certificate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/certifiate.ts#L29">property certificateData</a>
</h3>

```typescript
public certificateData: pulumi.Output<string>;
```


The raw Key Vault Certificate

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/certifiate.ts#L33">property certificatePolicy</a>
</h3>

```typescript
public certificatePolicy: pulumi.Output<{ ... }>;
```


A `certificate_policy` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/certifiate.ts#L37">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The name of the Certificate Issuer. Possible values include `Self`, or the name of a certificate issuing authority supported by Azure. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/certifiate.ts#L41">property secretId</a>
</h3>

```typescript
public secretId: pulumi.Output<string>;
```


The ID of the associated Key Vault Secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/certifiate.ts#L45">property tags</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/certifiate.ts#L49">property vaultUri</a>
</h3>

```typescript
public vaultUri: pulumi.Output<string>;
```


Specifies the URI used to access the Key Vault instance, available on the `azurerm_key_vault` resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/certifiate.ts#L53">property version</a>
</h3>

```typescript
public version: pulumi.Output<string>;
```


The current version of the Key Vault Certificate.

<h2 class="pdoc-module-header" id="Key">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/key.ts#L9">class Key</a>
</h2>

Manages a Key Vault Key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/key.ts#L57">constructor</a>
</h3>

```typescript
new Key(name: string, args: KeyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Key resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/key.ts#L18">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: KeyState): Key
```


Get an existing Key resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/key.ts#L25">property e</a>
</h3>

```typescript
public e: pulumi.Output<string>;
```


The RSA public exponent of this Key Vault Key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/key.ts#L29">property keyOpts</a>
</h3>

```typescript
public keyOpts: pulumi.Output<string[]>;
```


A list of JSON web key operations. Possible values include: `decrypt`, `encrypt`, `sign`, `unwrapKey`, `verify` and `wrapKey`. Please note these values are case sensitive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/key.ts#L33">property keySize</a>
</h3>

```typescript
public keySize: pulumi.Output<number>;
```


Specifies the Size of the Key to create in bytes. For example, 1024 or 2048. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/key.ts#L37">property keyType</a>
</h3>

```typescript
public keyType: pulumi.Output<string>;
```


Specifies the Key Type to use for this Key Vault Key. Possible values are `EC` (Elliptic Curve), `Oct` (Octet), `RSA` and `RSA-HSM`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/key.ts#L41">property n</a>
</h3>

```typescript
public n: pulumi.Output<string>;
```


The RSA modulus of this Key Vault Key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/key.ts#L45">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Key Vault Key. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/key.ts#L49">property tags</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/key.ts#L53">property vaultUri</a>
</h3>

```typescript
public vaultUri: pulumi.Output<string>;
```


Specifies the URI used to access the Key Vault instance, available on the `azurerm_key_vault` resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/key.ts#L57">property version</a>
</h3>

```typescript
public version: pulumi.Output<string>;
```


The current version of the Key Vault Key.

<h2 class="pdoc-module-header" id="KeyVault">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts#L11">class KeyVault</a>
</h2>

Manages a Key Vault.

~> **NOTE:** It's possible to define Key Vault Access Policies both within [the `azurerm_key_vault` resource](key_vault.html) via the `access_policy` block and by using [the `azurerm_key_vault_access_policy` resource](key_vault_access_policy.html). However it's not possible to use both methods to manage Access Policies within a KeyVault, since there'll be conflicts.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts#L79">constructor</a>
</h3>

```typescript
new KeyVault(name: string, args: KeyVaultArgs, opts?: pulumi.CustomResourceOptions)
```


Create a KeyVault resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts#L20">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: KeyVaultState): KeyVault
```


Get an existing KeyVault resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts#L28">property accessPolicies</a>
</h3>

```typescript
public accessPolicies: pulumi.Output<{ ... }[]>;
```


An access policy block as described below. A maximum of 16
may be declared.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts#L34">property enabledForDeployment</a>
</h3>

```typescript
public enabledForDeployment: pulumi.Output<boolean | undefined>;
```


Boolean flag to specify whether Azure Virtual
Machines are permitted to retrieve certificates stored as secrets from the key
vault. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts#L40">property enabledForDiskEncryption</a>
</h3>

```typescript
public enabledForDiskEncryption: pulumi.Output<boolean | undefined>;
```


Boolean flag to specify whether Azure
Disk Encryption is permitted to retrieve secrets from the vault and unwrap keys.
Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts#L46">property enabledForTemplateDeployment</a>
</h3>

```typescript
public enabledForTemplateDeployment: pulumi.Output<boolean | undefined>;
```


Boolean flag to specify whether
Azure Resource Manager is permitted to retrieve secrets from the key vault.
Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts#L51">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


Specifies the supported Azure location where the resource exists.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts#L56">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


SKU name to specify whether the key vault is a `standard`
or `premium` vault.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts#L61">property resourceGroupName</a>
</h3>

```typescript
public resourceGroupName: pulumi.Output<string>;
```


The name of the resource group in which to
create the Key Vault. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts#L65">property sku</a>
</h3>

```typescript
public sku: pulumi.Output<{ ... }>;
```


An SKU block as described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts#L69">property tags</a>
</h3>

```typescript
public tags: pulumi.Output<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts#L75">property tenantId</a>
</h3>

```typescript
public tenantId: pulumi.Output<string>;
```


The Azure Active Directory tenant ID that should be used
for authenticating requests to the key vault. Must match the `tenant_id` used
above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts#L79">property vaultUri</a>
</h3>

```typescript
public vaultUri: pulumi.Output<string>;
```


The URI of the vault for performing operations on keys and secrets.

<h2 class="pdoc-module-header" id="Secret">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/secret.ts#L12">class Secret</a>
</h2>

Manages a Key Vault Secret.

~> **Note:** All arguments including the secret value will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/secret.ts#L48">constructor</a>
</h3>

```typescript
new Secret(name: string, args: SecretArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Secret resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/secret.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: SecretState): Secret
```


Get an existing Secret resource's state with the given name, ID, and optional extra
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/secret.ts#L28">property contentType</a>
</h3>

```typescript
public contentType: pulumi.Output<string | undefined>;
```


Specifies the content type for the Key Vault Secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/secret.ts#L32">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


Specifies the name of the Key Vault Secret. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/secret.ts#L36">property tags</a>
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
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/secret.ts#L40">property value</a>
</h3>

```typescript
public value: pulumi.Output<string>;
```


Specifies the value of the Key Vault Secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/secret.ts#L44">property vaultUri</a>
</h3>

```typescript
public vaultUri: pulumi.Output<string>;
```


Specifies the URI used to access the Key Vault instance, available on the `azurerm_key_vault` resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/secret.ts#L48">property version</a>
</h3>

```typescript
public version: pulumi.Output<string>;
```


The current version of the Key Vault Secret.

<h2 class="pdoc-module-header" id="getAccessPolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/getAccessPolicy.ts#L9">function getAccessPolicy</a>
</h2>

```typescript
getAccessPolicy(args: GetAccessPolicyArgs, opts?: pulumi.InvokeOptions): Promise<GetAccessPolicyResult>
```


Use this data source to access information about the permissions from the Management Key Vault Templates.

<h2 class="pdoc-module-header" id="getKeyVault">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/getKeyVault.ts#L9">function getKeyVault</a>
</h2>

```typescript
getKeyVault(args: GetKeyVaultArgs, opts?: pulumi.InvokeOptions): Promise<GetKeyVaultResult>
```


Gets information about a Key Vault.

<h2 class="pdoc-module-header" id="getSecret">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/getSecret.ts#L12">function getSecret</a>
</h2>

```typescript
getSecret(args: GetSecretArgs, opts?: pulumi.InvokeOptions): Promise<GetSecretResult>
```


Returns information about the specified Key Vault Secret.

~> **Note:** All arguments including the secret value will be stored in the raw state as plain-text.
[Read more about sensitive data in state](/docs/state/sensitive-data.html).

<h2 class="pdoc-module-header" id="AccessPolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/accessPolicy.ts#L177">interface AccessPolicyArgs</a>
</h2>

The set of arguments for constructing a AccessPolicy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/accessPolicy.ts#L181">property applicationId</a>
</h3>

```typescript
applicationId?: pulumi.Input<string>;
```


The object ID of an Application in Azure Active Directory.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/accessPolicy.ts#L187">property certificatePermissions</a>
</h3>

```typescript
certificatePermissions?: pulumi.Input<pulumi.Input<string>[]>;
```


List of certificate permissions, must be one or more from
the following: `create`, `delete`, `deleteissuers`, `get`, `getissuers`, `import`, `list`, `listissuers`,
`managecontacts`, `manageissuers`, `purge`, `recover`, `setissuers` and `update`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/accessPolicy.ts#L193">property keyPermissions</a>
</h3>

```typescript
keyPermissions: pulumi.Input<pulumi.Input<string>[]>;
```


List of key permissions, must be one or more from
the following: `backup`, `create`, `decrypt`, `delete`, `encrypt`, `get`, `import`, `list`, `purge`,
`recover`, `restore`, `sign`, `unwrapKey`, `update`, `verify` and `wrapKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/accessPolicy.ts#L200">property objectId</a>
</h3>

```typescript
objectId: pulumi.Input<string>;
```


The object ID of a user, service principal or security
group in the Azure Active Directory tenant for the vault. The object ID must
be unique for the list of access policies. Changing this forces a new resource
to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/accessPolicy.ts#L205">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/accessPolicy.ts#L210">property secretPermissions</a>
</h3>

```typescript
secretPermissions: pulumi.Input<pulumi.Input<string>[]>;
```


List of secret permissions, must be one or more
from the following: `backup`, `delete`, `get`, `list`, `purge`, `recover`, `restore` and `set`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/accessPolicy.ts#L216">property tenantId</a>
</h3>

```typescript
tenantId: pulumi.Input<string>;
```


The Azure Active Directory tenant ID that should be used
for authenticating requests to the key vault. Changing this forces a new resource
to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/accessPolicy.ts#L221">property vaultName</a>
</h3>

```typescript
vaultName: pulumi.Input<string>;
```


Specifies the name of the Key Vault resource. Changing this
forces a new resource to be created.

<h2 class="pdoc-module-header" id="AccessPolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/accessPolicy.ts#L127">interface AccessPolicyState</a>
</h2>

Input properties used for looking up and filtering AccessPolicy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/accessPolicy.ts#L131">property applicationId</a>
</h3>

```typescript
applicationId?: pulumi.Input<string>;
```


The object ID of an Application in Azure Active Directory.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/accessPolicy.ts#L137">property certificatePermissions</a>
</h3>

```typescript
certificatePermissions?: pulumi.Input<pulumi.Input<string>[]>;
```


List of certificate permissions, must be one or more from
the following: `create`, `delete`, `deleteissuers`, `get`, `getissuers`, `import`, `list`, `listissuers`,
`managecontacts`, `manageissuers`, `purge`, `recover`, `setissuers` and `update`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/accessPolicy.ts#L143">property keyPermissions</a>
</h3>

```typescript
keyPermissions?: pulumi.Input<pulumi.Input<string>[]>;
```


List of key permissions, must be one or more from
the following: `backup`, `create`, `decrypt`, `delete`, `encrypt`, `get`, `import`, `list`, `purge`,
`recover`, `restore`, `sign`, `unwrapKey`, `update`, `verify` and `wrapKey`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/accessPolicy.ts#L150">property objectId</a>
</h3>

```typescript
objectId?: pulumi.Input<string>;
```


The object ID of a user, service principal or security
group in the Azure Active Directory tenant for the vault. The object ID must
be unique for the list of access policies. Changing this forces a new resource
to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/accessPolicy.ts#L155">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the namespace. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/accessPolicy.ts#L160">property secretPermissions</a>
</h3>

```typescript
secretPermissions?: pulumi.Input<pulumi.Input<string>[]>;
```


List of secret permissions, must be one or more
from the following: `backup`, `delete`, `get`, `list`, `purge`, `recover`, `restore` and `set`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/accessPolicy.ts#L166">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The Azure Active Directory tenant ID that should be used
for authenticating requests to the key vault. Changing this forces a new resource
to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/accessPolicy.ts#L171">property vaultName</a>
</h3>

```typescript
vaultName?: pulumi.Input<string>;
```


Specifies the name of the Key Vault resource. Changing this
forces a new resource to be created.

<h2 class="pdoc-module-header" id="CertifiateArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/certifiate.ts#L137">interface CertifiateArgs</a>
</h2>

The set of arguments for constructing a Certifiate resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/certifiate.ts#L141">property certificate</a>
</h3>

```typescript
certificate?: pulumi.Input<{ ... }>;
```


A `certificate` block as defined below, used to Import an existing certificate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/certifiate.ts#L145">property certificatePolicy</a>
</h3>

```typescript
certificatePolicy: pulumi.Input<{ ... }>;
```


A `certificate_policy` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/certifiate.ts#L149">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Certificate Issuer. Possible values include `Self`, or the name of a certificate issuing authority supported by Azure. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/certifiate.ts#L153">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/certifiate.ts#L157">property vaultUri</a>
</h3>

```typescript
vaultUri: pulumi.Input<string>;
```


Specifies the URI used to access the Key Vault instance, available on the `azurerm_key_vault` resource.

<h2 class="pdoc-module-header" id="CertifiateState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/certifiate.ts#L99">interface CertifiateState</a>
</h2>

Input properties used for looking up and filtering Certifiate resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/certifiate.ts#L103">property certificate</a>
</h3>

```typescript
certificate?: pulumi.Input<{ ... }>;
```


A `certificate` block as defined below, used to Import an existing certificate.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/certifiate.ts#L107">property certificateData</a>
</h3>

```typescript
certificateData?: pulumi.Input<string>;
```


The raw Key Vault Certificate

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/certifiate.ts#L111">property certificatePolicy</a>
</h3>

```typescript
certificatePolicy?: pulumi.Input<{ ... }>;
```


A `certificate_policy` block as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/certifiate.ts#L115">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The name of the Certificate Issuer. Possible values include `Self`, or the name of a certificate issuing authority supported by Azure. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/certifiate.ts#L119">property secretId</a>
</h3>

```typescript
secretId?: pulumi.Input<string>;
```


The ID of the associated Key Vault Secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/certifiate.ts#L123">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/certifiate.ts#L127">property vaultUri</a>
</h3>

```typescript
vaultUri?: pulumi.Input<string>;
```


Specifies the URI used to access the Key Vault instance, available on the `azurerm_key_vault` resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/certifiate.ts#L131">property version</a>
</h3>

```typescript
version?: pulumi.Input<string>;
```


The current version of the Key Vault Certificate.

<h2 class="pdoc-module-header" id="GetAccessPolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/getAccessPolicy.ts#L18">interface GetAccessPolicyArgs</a>
</h2>

A collection of arguments for invoking getAccessPolicy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/getAccessPolicy.ts#L24">property name</a>
</h3>

```typescript
name: string;
```


Specifies the name of the Management Template. Possible values are: `Key Management`,
`Secret Management`, `Certificate Management`, `Key & Secret Management`, `Key & Certificate Management`,
`Secret & Certificate Management`,  `Key, Secret, & Certificate Management`

<h2 class="pdoc-module-header" id="GetAccessPolicyResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/getAccessPolicy.ts#L30">interface GetAccessPolicyResult</a>
</h2>

A collection of values returned by getAccessPolicy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/getAccessPolicy.ts#L34">property certificatePermissions</a>
</h3>

```typescript
certificatePermissions: string[];
```


the certificate permissions for the access policy

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/getAccessPolicy.ts#L46">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/getAccessPolicy.ts#L38">property keyPermissions</a>
</h3>

```typescript
keyPermissions: string[];
```


the key permissions for the access policy

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/getAccessPolicy.ts#L42">property secretPermissions</a>
</h3>

```typescript
secretPermissions: string[];
```


the secret permissions for the access policy

<h2 class="pdoc-module-header" id="GetKeyVaultArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/getKeyVault.ts#L19">interface GetKeyVaultArgs</a>
</h2>

A collection of arguments for invoking getKeyVault.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/getKeyVault.ts#L23">property name</a>
</h3>

```typescript
name: string;
```


Specifies the name of the Key Vault.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/getKeyVault.ts#L27">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: string;
```


The name of the Resource Group in which the Key Vault exists.

<h2 class="pdoc-module-header" id="GetKeyVaultResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/getKeyVault.ts#L33">interface GetKeyVaultResult</a>
</h2>

A collection of values returned by getKeyVault.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/getKeyVault.ts#L37">property accessPolicies</a>
</h3>

```typescript
accessPolicies: { ... }[];
```


One or more `access_policy` blocks as defined below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/getKeyVault.ts#L41">property enabledForDeployment</a>
</h3>

```typescript
enabledForDeployment: boolean;
```


Can Azure Virtual Machines retrieve certificates stored as secrets from the Key Vault?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/getKeyVault.ts#L45">property enabledForDiskEncryption</a>
</h3>

```typescript
enabledForDiskEncryption: boolean;
```


Can Azure Disk Encryption retrieve secrets from the Key Vault?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/getKeyVault.ts#L49">property enabledForTemplateDeployment</a>
</h3>

```typescript
enabledForTemplateDeployment: boolean;
```


Can Azure Resource Manager retrieve secrets from the Key Vault?

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/getKeyVault.ts#L73">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/getKeyVault.ts#L53">property location</a>
</h3>

```typescript
location: string;
```


The Azure Region in which the Key Vault exists.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/getKeyVault.ts#L57">property sku</a>
</h3>

```typescript
sku: { ... };
```


A `sku` block as described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/getKeyVault.ts#L61">property tags</a>
</h3>

```typescript
tags: { ... };
```


A mapping of tags assigned to the Key Vault.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/getKeyVault.ts#L65">property tenantId</a>
</h3>

```typescript
tenantId: string;
```


The Azure Active Directory Tenant ID used to authenticate requests for this Key Vault.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/getKeyVault.ts#L69">property vaultUri</a>
</h3>

```typescript
vaultUri: string;
```


The URI of the vault for performing operations on keys and secrets.

<h2 class="pdoc-module-header" id="GetSecretArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/getSecret.ts#L22">interface GetSecretArgs</a>
</h2>

A collection of arguments for invoking getSecret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/getSecret.ts#L26">property name</a>
</h3>

```typescript
name: string;
```


Specifies the name of the Key Vault Secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/getSecret.ts#L30">property vaultUri</a>
</h3>

```typescript
vaultUri: string;
```


Specifies the URI used to access the Key Vault instance, available on the `azurerm_key_vault` Data Source / Resource.

<h2 class="pdoc-module-header" id="GetSecretResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/getSecret.ts#L36">interface GetSecretResult</a>
</h2>

A collection of values returned by getSecret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/getSecret.ts#L40">property contentType</a>
</h3>

```typescript
contentType: string;
```


The content type for the Key Vault Secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/getSecret.ts#L56">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/getSecret.ts#L44">property tags</a>
</h3>

```typescript
tags: { ... };
```


Any tags assigned to this resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/getSecret.ts#L48">property value</a>
</h3>

```typescript
value: string;
```


The value of the Key Vault Secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/getSecret.ts#L52">property version</a>
</h3>

```typescript
version: string;
```


The current version of the Key Vault Secret.

<h2 class="pdoc-module-header" id="KeyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/key.ts#L153">interface KeyArgs</a>
</h2>

The set of arguments for constructing a Key resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/key.ts#L157">property keyOpts</a>
</h3>

```typescript
keyOpts: pulumi.Input<pulumi.Input<string>[]>;
```


A list of JSON web key operations. Possible values include: `decrypt`, `encrypt`, `sign`, `unwrapKey`, `verify` and `wrapKey`. Please note these values are case sensitive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/key.ts#L161">property keySize</a>
</h3>

```typescript
keySize: pulumi.Input<number>;
```


Specifies the Size of the Key to create in bytes. For example, 1024 or 2048. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/key.ts#L165">property keyType</a>
</h3>

```typescript
keyType: pulumi.Input<string>;
```


Specifies the Key Type to use for this Key Vault Key. Possible values are `EC` (Elliptic Curve), `Oct` (Octet), `RSA` and `RSA-HSM`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/key.ts#L169">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Key Vault Key. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/key.ts#L173">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/key.ts#L177">property vaultUri</a>
</h3>

```typescript
vaultUri: pulumi.Input<string>;
```


Specifies the URI used to access the Key Vault instance, available on the `azurerm_key_vault` resource.

<h2 class="pdoc-module-header" id="KeyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/key.ts#L111">interface KeyState</a>
</h2>

Input properties used for looking up and filtering Key resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/key.ts#L115">property e</a>
</h3>

```typescript
e?: pulumi.Input<string>;
```


The RSA public exponent of this Key Vault Key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/key.ts#L119">property keyOpts</a>
</h3>

```typescript
keyOpts?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of JSON web key operations. Possible values include: `decrypt`, `encrypt`, `sign`, `unwrapKey`, `verify` and `wrapKey`. Please note these values are case sensitive.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/key.ts#L123">property keySize</a>
</h3>

```typescript
keySize?: pulumi.Input<number>;
```


Specifies the Size of the Key to create in bytes. For example, 1024 or 2048. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/key.ts#L127">property keyType</a>
</h3>

```typescript
keyType?: pulumi.Input<string>;
```


Specifies the Key Type to use for this Key Vault Key. Possible values are `EC` (Elliptic Curve), `Oct` (Octet), `RSA` and `RSA-HSM`. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/key.ts#L131">property n</a>
</h3>

```typescript
n?: pulumi.Input<string>;
```


The RSA modulus of this Key Vault Key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/key.ts#L135">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Key Vault Key. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/key.ts#L139">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/key.ts#L143">property vaultUri</a>
</h3>

```typescript
vaultUri?: pulumi.Input<string>;
```


Specifies the URI used to access the Key Vault instance, available on the `azurerm_key_vault` resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/key.ts#L147">property version</a>
</h3>

```typescript
version?: pulumi.Input<string>;
```


The current version of the Key Vault Key.

<h2 class="pdoc-module-header" id="KeyVaultArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts#L199">interface KeyVaultArgs</a>
</h2>

The set of arguments for constructing a KeyVault resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts#L204">property accessPolicies</a>
</h3>

```typescript
accessPolicies?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An access policy block as described below. A maximum of 16
may be declared.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts#L210">property enabledForDeployment</a>
</h3>

```typescript
enabledForDeployment?: pulumi.Input<boolean>;
```


Boolean flag to specify whether Azure Virtual
Machines are permitted to retrieve certificates stored as secrets from the key
vault. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts#L216">property enabledForDiskEncryption</a>
</h3>

```typescript
enabledForDiskEncryption?: pulumi.Input<boolean>;
```


Boolean flag to specify whether Azure
Disk Encryption is permitted to retrieve secrets from the vault and unwrap keys.
Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts#L222">property enabledForTemplateDeployment</a>
</h3>

```typescript
enabledForTemplateDeployment?: pulumi.Input<boolean>;
```


Boolean flag to specify whether
Azure Resource Manager is permitted to retrieve secrets from the key vault.
Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts#L227">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts#L232">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


SKU name to specify whether the key vault is a `standard`
or `premium` vault.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts#L237">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName: pulumi.Input<string>;
```


The name of the resource group in which to
create the Key Vault. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts#L241">property sku</a>
</h3>

```typescript
sku: pulumi.Input<{ ... }>;
```


An SKU block as described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts#L245">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts#L251">property tenantId</a>
</h3>

```typescript
tenantId: pulumi.Input<string>;
```


The Azure Active Directory tenant ID that should be used
for authenticating requests to the key vault. Must match the `tenant_id` used
above.

<h2 class="pdoc-module-header" id="KeyVaultState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts#L137">interface KeyVaultState</a>
</h2>

Input properties used for looking up and filtering KeyVault resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts#L142">property accessPolicies</a>
</h3>

```typescript
accessPolicies?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


An access policy block as described below. A maximum of 16
may be declared.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts#L148">property enabledForDeployment</a>
</h3>

```typescript
enabledForDeployment?: pulumi.Input<boolean>;
```


Boolean flag to specify whether Azure Virtual
Machines are permitted to retrieve certificates stored as secrets from the key
vault. Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts#L154">property enabledForDiskEncryption</a>
</h3>

```typescript
enabledForDiskEncryption?: pulumi.Input<boolean>;
```


Boolean flag to specify whether Azure
Disk Encryption is permitted to retrieve secrets from the vault and unwrap keys.
Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts#L160">property enabledForTemplateDeployment</a>
</h3>

```typescript
enabledForTemplateDeployment?: pulumi.Input<boolean>;
```


Boolean flag to specify whether
Azure Resource Manager is permitted to retrieve secrets from the key vault.
Defaults to false.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts#L165">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


Specifies the supported Azure location where the resource exists.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts#L170">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


SKU name to specify whether the key vault is a `standard`
or `premium` vault.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts#L175">property resourceGroupName</a>
</h3>

```typescript
resourceGroupName?: pulumi.Input<string>;
```


The name of the resource group in which to
create the Key Vault. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts#L179">property sku</a>
</h3>

```typescript
sku?: pulumi.Input<{ ... }>;
```


An SKU block as described below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts#L183">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts#L189">property tenantId</a>
</h3>

```typescript
tenantId?: pulumi.Input<string>;
```


The Azure Active Directory tenant ID that should be used
for authenticating requests to the key vault. Must match the `tenant_id` used
above.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/keyVault.ts#L193">property vaultUri</a>
</h3>

```typescript
vaultUri?: pulumi.Input<string>;
```


The URI of the vault for performing operations on keys and secrets.

<h2 class="pdoc-module-header" id="SecretArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/secret.ts#L120">interface SecretArgs</a>
</h2>

The set of arguments for constructing a Secret resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/secret.ts#L124">property contentType</a>
</h3>

```typescript
contentType?: pulumi.Input<string>;
```


Specifies the content type for the Key Vault Secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/secret.ts#L128">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Key Vault Secret. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/secret.ts#L132">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/secret.ts#L136">property value</a>
</h3>

```typescript
value: pulumi.Input<string>;
```


Specifies the value of the Key Vault Secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/secret.ts#L140">property vaultUri</a>
</h3>

```typescript
vaultUri: pulumi.Input<string>;
```


Specifies the URI used to access the Key Vault instance, available on the `azurerm_key_vault` resource.

<h2 class="pdoc-module-header" id="SecretState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/secret.ts#L90">interface SecretState</a>
</h2>

Input properties used for looking up and filtering Secret resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/secret.ts#L94">property contentType</a>
</h3>

```typescript
contentType?: pulumi.Input<string>;
```


Specifies the content type for the Key Vault Secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/secret.ts#L98">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


Specifies the name of the Key Vault Secret. Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/secret.ts#L102">property tags</a>
</h3>

```typescript
tags?: pulumi.Input<{ ... }>;
```


A mapping of tags to assign to the resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/secret.ts#L106">property value</a>
</h3>

```typescript
value?: pulumi.Input<string>;
```


Specifies the value of the Key Vault Secret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/secret.ts#L110">property vaultUri</a>
</h3>

```typescript
vaultUri?: pulumi.Input<string>;
```


Specifies the URI used to access the Key Vault instance, available on the `azurerm_key_vault` resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-azure/blob/master/sdk/nodejs/keyvault/secret.ts#L114">property version</a>
</h3>

```typescript
version?: pulumi.Input<string>;
```


The current version of the Key Vault Secret.

