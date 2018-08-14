---
title: Module kms
---

<a href="../index.html">@pulumi/gcp</a> &gt; kms

<h2 class="pdoc-module-header">Index</h2>

* <a href="#CryptoKey">class CryptoKey</a>
* <a href="#CryptoKeyIAMBinding">class CryptoKeyIAMBinding</a>
* <a href="#CryptoKeyIAMMember">class CryptoKeyIAMMember</a>
* <a href="#KeyRing">class KeyRing</a>
* <a href="#KeyRingIAMBinding">class KeyRingIAMBinding</a>
* <a href="#KeyRingIAMMember">class KeyRingIAMMember</a>
* <a href="#KeyRingIAMPolicy">class KeyRingIAMPolicy</a>
* <a href="#Registry">class Registry</a>
* <a href="#getKMSSecret">function getKMSSecret</a>
* <a href="#CryptoKeyArgs">interface CryptoKeyArgs</a>
* <a href="#CryptoKeyIAMBindingArgs">interface CryptoKeyIAMBindingArgs</a>
* <a href="#CryptoKeyIAMBindingState">interface CryptoKeyIAMBindingState</a>
* <a href="#CryptoKeyIAMMemberArgs">interface CryptoKeyIAMMemberArgs</a>
* <a href="#CryptoKeyIAMMemberState">interface CryptoKeyIAMMemberState</a>
* <a href="#CryptoKeyState">interface CryptoKeyState</a>
* <a href="#GetKMSSecretArgs">interface GetKMSSecretArgs</a>
* <a href="#GetKMSSecretResult">interface GetKMSSecretResult</a>
* <a href="#KeyRingArgs">interface KeyRingArgs</a>
* <a href="#KeyRingIAMBindingArgs">interface KeyRingIAMBindingArgs</a>
* <a href="#KeyRingIAMBindingState">interface KeyRingIAMBindingState</a>
* <a href="#KeyRingIAMMemberArgs">interface KeyRingIAMMemberArgs</a>
* <a href="#KeyRingIAMMemberState">interface KeyRingIAMMemberState</a>
* <a href="#KeyRingIAMPolicyArgs">interface KeyRingIAMPolicyArgs</a>
* <a href="#KeyRingIAMPolicyState">interface KeyRingIAMPolicyState</a>
* <a href="#KeyRingState">interface KeyRingState</a>
* <a href="#RegistryArgs">interface RegistryArgs</a>
* <a href="#RegistryState">interface RegistryState</a>

<a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKey.ts">kms/cryptoKey.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKeyIAMBinding.ts">kms/cryptoKeyIAMBinding.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKeyIAMMember.ts">kms/cryptoKeyIAMMember.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/getKMSSecret.ts">kms/getKMSSecret.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRing.ts">kms/keyRing.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMBinding.ts">kms/keyRingIAMBinding.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMMember.ts">kms/keyRingIAMMember.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMPolicy.ts">kms/keyRingIAMPolicy.ts</a> <a href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/registry.ts">kms/registry.ts</a> 


<h2 class="pdoc-module-header" id="CryptoKey">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKey.ts#L18">class CryptoKey</a>
</h2>

Allows creation of a Google Cloud Platform KMS CryptoKey. For more information see
[the official documentation](https://cloud.google.com/kms/docs/object-hierarchy#cryptokey)
and
[API](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys).

A CryptoKey is an interface to key material which can be used to encrypt and decrypt data. A CryptoKey belongs to a
Google Cloud KMS KeyRing.

~> Note: CryptoKeys cannot be deleted from Google Cloud Platform. Destroying a Terraform-managed CryptoKey will remove it
from state and delete all CryptoKeyVersions, rendering the key unusable, but **will not delete the resource on the server**.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKey.ts#L46">constructor</a>
</h3>

```typescript
new CryptoKey(name: string, args: CryptoKeyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a CryptoKey resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKey.ts#L27">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CryptoKeyState): CryptoKey
```


Get an existing CryptoKey resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKey.ts#L34">property keyRing</a>
</h3>

```typescript
public keyRing: pulumi.Output<string>;
```


The id of the Google Cloud Platform KeyRing to which the key shall belong.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKey.ts#L39">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The CryptoKey's name.
A CryptoKey’s name must be unique within a location and match the regular expression `[a-zA-Z0-9_-]{1,63}`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKey.ts#L46">property rotationPeriod</a>
</h3>

```typescript
public rotationPeriod: pulumi.Output<string | undefined>;
```


Every time this period passes, generate a new CryptoKeyVersion and set it as
the primary. The first rotation will take place after the specified period. The rotation period has the format
of a decimal number with up to 9 fractional digits, followed by the letter s (seconds). It must be greater than
a day (ie, 83400).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="CryptoKeyIAMBinding">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKeyIAMBinding.ts#L10">class CryptoKeyIAMBinding</a>
</h2>

Allows creation and management of a single binding within IAM policy for
an existing Google Cloud KMS crypto key.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKeyIAMBinding.ts#L43">constructor</a>
</h3>

```typescript
new CryptoKeyIAMBinding(name: string, args: CryptoKeyIAMBindingArgs, opts?: pulumi.CustomResourceOptions)
```


Create a CryptoKeyIAMBinding resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKeyIAMBinding.ts#L19">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CryptoKeyIAMBindingState): CryptoKeyIAMBinding
```


Get an existing CryptoKeyIAMBinding resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKeyIAMBinding.ts#L29">property cryptoKeyId</a>
</h3>

```typescript
public cryptoKeyId: pulumi.Output<string>;
```


The crypto key ID, in the form
`{project_id}/{location_name}/{key_ring_name}/{crypto_key_name}` or
`{location_name}/{key_ring_name}/{crypto_key_name}`.
In the second form, the provider's project setting will be used as a fallback.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKeyIAMBinding.ts#L33">property etag</a>
</h3>

```typescript
public etag: pulumi.Output<string>;
```


(Computed) The etag of the crypto key's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKeyIAMBinding.ts#L37">property members</a>
</h3>

```typescript
public members: pulumi.Output<string[]>;
```


A list of users that the role should apply to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKeyIAMBinding.ts#L43">property role</a>
</h3>

```typescript
public role: pulumi.Output<string>;
```


The role that should be applied. Only one
`google_kms_crypto_key_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="CryptoKeyIAMMember">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKeyIAMMember.ts#L15">class CryptoKeyIAMMember</a>
</h2>

Allows creation and management of a single member for a single binding within
the IAM policy for an existing Google Cloud KMS crypto key.

~> **Note:** This resource _must not_ be used in conjunction with
   `google_kms_crypto_key_iam_policy` or they will fight over what your policy
   should be. Similarly, roles controlled by `google_kms_crypto_key_iam_binding`
   should not be assigned to using `google_kms_crypto_key_iam_member`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKeyIAMMember.ts#L47">constructor</a>
</h3>

```typescript
new CryptoKeyIAMMember(name: string, args: CryptoKeyIAMMemberArgs, opts?: pulumi.CustomResourceOptions)
```


Create a CryptoKeyIAMMember resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKeyIAMMember.ts#L24">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: CryptoKeyIAMMemberState): CryptoKeyIAMMember
```


Get an existing CryptoKeyIAMMember resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKeyIAMMember.ts#L34">property cryptoKeyId</a>
</h3>

```typescript
public cryptoKeyId: pulumi.Output<string>;
```


The key ring ID, in the form
`{project_id}/{location_name}/{key_ring_name}/{crypto_key_name}` or
`{location_name}/{key_ring_name}/{crypto_key_name}`. In the second form,
the provider's project setting will be used as a fallback.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKeyIAMMember.ts#L38">property etag</a>
</h3>

```typescript
public etag: pulumi.Output<string>;
```


(Computed) The etag of the project's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKeyIAMMember.ts#L42">property member</a>
</h3>

```typescript
public member: pulumi.Output<string>;
```


The user that the role should apply to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKeyIAMMember.ts#L47">property role</a>
</h3>

```typescript
public role: pulumi.Output<string>;
```


The role that should be applied. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="KeyRing">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRing.ts#L18">class KeyRing</a>
</h2>

Allows creation of a Google Cloud Platform KMS KeyRing. For more information see
[the official documentation](https://cloud.google.com/kms/docs/object-hierarchy#keyring)
and
[API](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings).

A KeyRing is a grouping of CryptoKeys for organizational purposes. A KeyRing belongs to a Google Cloud Platform Project
and resides in a specific location.

~> Note: KeyRings cannot be deleted from Google Cloud Platform. Destroying a Terraform-managed KeyRing will remove it
from state but **will not delete the resource on the server**.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRing.ts#L45">constructor</a>
</h3>

```typescript
new KeyRing(name: string, args: KeyRingArgs, opts?: pulumi.CustomResourceOptions)
```


Create a KeyRing resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRing.ts#L27">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: KeyRingState): KeyRing
```


Get an existing KeyRing resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRing.ts#L35">property location</a>
</h3>

```typescript
public location: pulumi.Output<string>;
```


The Google Cloud Platform location for the KeyRing.
A full list of valid locations can be found by running `gcloud kms locations list`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRing.ts#L40">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


The KeyRing's name.
A KeyRing’s name must be unique within a location and match the regular expression `[a-zA-Z0-9_-]{1,63}`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRing.ts#L45">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The project in which the resource belongs. If it
is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="KeyRingIAMBinding">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMBinding.ts#L17">class KeyRingIAMBinding</a>
</h2>

Three different resources help you manage your IAM policy for KMS key ring. Each of these resources serves a different use case:

* `google_kms_key_ring_iam_policy`: Authoritative. Sets the IAM policy for the key ring and replaces any existing policy already attached.
* `google_kms_key_ring_iam_binding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the key ring are preserved.
* `google_kms_key_ring_iam_member`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the key ring are preserved.

~> **Note:** `google_kms_key_ring_iam_policy` **cannot** be used in conjunction with `google_kms_key_ring_iam_binding` and `google_kms_key_ring_iam_member` or they will fight over what your policy should be.

~> **Note:** `google_kms_key_ring_iam_binding` resources **can be** used in conjunction with `google_kms_key_ring_iam_member` resources **only if** they do not grant privilege to the same role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMBinding.ts#L47">constructor</a>
</h3>

```typescript
new KeyRingIAMBinding(name: string, args: KeyRingIAMBindingArgs, opts?: pulumi.CustomResourceOptions)
```


Create a KeyRingIAMBinding resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMBinding.ts#L26">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: KeyRingIAMBindingState): KeyRingIAMBinding
```


Get an existing KeyRingIAMBinding resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMBinding.ts#L33">property etag</a>
</h3>

```typescript
public etag: pulumi.Output<string>;
```


(Computed) The etag of the key ring's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMBinding.ts#L40">property keyRingId</a>
</h3>

```typescript
public keyRingId: pulumi.Output<string>;
```


The key ring ID, in the form
`{project_id}/{location_name}/{key_ring_name}` or
`{location_name}/{key_ring_name}`. In the second form, the provider's
project setting will be used as a fallback.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMBinding.ts#L41">property members</a>
</h3>

```typescript
public members: pulumi.Output<string[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMBinding.ts#L47">property role</a>
</h3>

```typescript
public role: pulumi.Output<string>;
```


The role that should be applied. Only one
`google_kms_key_ring_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="KeyRingIAMMember">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMMember.ts#L17">class KeyRingIAMMember</a>
</h2>

Three different resources help you manage your IAM policy for KMS key ring. Each of these resources serves a different use case:

* `google_kms_key_ring_iam_policy`: Authoritative. Sets the IAM policy for the key ring and replaces any existing policy already attached.
* `google_kms_key_ring_iam_binding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the key ring are preserved.
* `google_kms_key_ring_iam_member`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the key ring are preserved.

~> **Note:** `google_kms_key_ring_iam_policy` **cannot** be used in conjunction with `google_kms_key_ring_iam_binding` and `google_kms_key_ring_iam_member` or they will fight over what your policy should be.

~> **Note:** `google_kms_key_ring_iam_binding` resources **can be** used in conjunction with `google_kms_key_ring_iam_member` resources **only if** they do not grant privilege to the same role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMMember.ts#L47">constructor</a>
</h3>

```typescript
new KeyRingIAMMember(name: string, args: KeyRingIAMMemberArgs, opts?: pulumi.CustomResourceOptions)
```


Create a KeyRingIAMMember resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMMember.ts#L26">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: KeyRingIAMMemberState): KeyRingIAMMember
```


Get an existing KeyRingIAMMember resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMMember.ts#L33">property etag</a>
</h3>

```typescript
public etag: pulumi.Output<string>;
```


(Computed) The etag of the key ring's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMMember.ts#L40">property keyRingId</a>
</h3>

```typescript
public keyRingId: pulumi.Output<string>;
```


The key ring ID, in the form
`{project_id}/{location_name}/{key_ring_name}` or
`{location_name}/{key_ring_name}`. In the second form, the provider's
project setting will be used as a fallback.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMMember.ts#L41">property member</a>
</h3>

```typescript
public member: pulumi.Output<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMMember.ts#L47">property role</a>
</h3>

```typescript
public role: pulumi.Output<string>;
```


The role that should be applied. Only one
`google_kms_key_ring_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="KeyRingIAMPolicy">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMPolicy.ts#L17">class KeyRingIAMPolicy</a>
</h2>

Three different resources help you manage your IAM policy for KMS key ring. Each of these resources serves a different use case:

* `google_kms_key_ring_iam_policy`: Authoritative. Sets the IAM policy for the key ring and replaces any existing policy already attached.
* `google_kms_key_ring_iam_binding`: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the key ring are preserved.
* `google_kms_key_ring_iam_member`: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the key ring are preserved.

~> **Note:** `google_kms_key_ring_iam_policy` **cannot** be used in conjunction with `google_kms_key_ring_iam_binding` and `google_kms_key_ring_iam_member` or they will fight over what your policy should be.

~> **Note:** `google_kms_key_ring_iam_binding` resources **can be** used in conjunction with `google_kms_key_ring_iam_member` resources **only if** they do not grant privilege to the same role.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMPolicy.ts#L45">constructor</a>
</h3>

```typescript
new KeyRingIAMPolicy(name: string, args: KeyRingIAMPolicyArgs, opts?: pulumi.CustomResourceOptions)
```


Create a KeyRingIAMPolicy resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMPolicy.ts#L26">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: KeyRingIAMPolicyState): KeyRingIAMPolicy
```


Get an existing KeyRingIAMPolicy resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMPolicy.ts#L33">property etag</a>
</h3>

```typescript
public etag: pulumi.Output<string>;
```


(Computed) The etag of the key ring's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMPolicy.ts#L40">property keyRingId</a>
</h3>

```typescript
public keyRingId: pulumi.Output<string>;
```


The key ring ID, in the form
`{project_id}/{location_name}/{key_ring_name}` or
`{location_name}/{key_ring_name}`. In the second form, the provider's
project setting will be used as a fallback.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMPolicy.ts#L45">property policyData</a>
</h3>

```typescript
public policyData: pulumi.Output<string>;
```


The policy data generated by
a `google_iam_policy` data source.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="Registry">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/registry.ts#L12">class Registry</a>
</h2>

 Creates a device registry in Google's Cloud IoT Core platform. For more information see
[the official documentation](https://cloud.google.com/iot/docs/) and
[API](https://cloud.google.com/iot/docs/reference/cloudiot/rest/v1/projects.locations.registries).

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/registry.ts#L57">constructor</a>
</h3>

```typescript
new Registry(name: string, args?: RegistryArgs, opts?: pulumi.CustomResourceOptions)
```


Create a Registry resource with the given unique name, arguments, and options.

* `name` The _unique_ name of the resource.
* `args` The arguments to use to populate this resource&#39;s properties.
* `opts` A bag of options that control this resource&#39;s behavior.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/registry.ts#L21">method get</a>
</h3>

```typescript
public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RegistryState): Registry
```


Get an existing Registry resource's state with the given name, ID, and optional extra
properties used to qualify the lookup.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L13">method getProvider</a>
</h3>

```typescript
getProvider(moduleMember: string): ProviderResource | undefined
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L85">method isInstance</a>
</h3>

```typescript
static isInstance(obj: any): boolean
```


Returns true if the given object is an instance of CustomResource.  This is designed to work even when
multiple copies of the Pulumi SDK have been loaded into the same process.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/registry.ts#L28">property credentials</a>
</h3>

```typescript
public credentials: pulumi.Output<{ ... }[] | undefined>;
```


List of public key certificates to authenticate devices. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/registry.ts#L32">property eventNotificationConfig</a>
</h3>

```typescript
public eventNotificationConfig: pulumi.Output<{ ... } | undefined>;
```


A PubSub topics to publish device events. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/registry.ts#L36">property httpConfig</a>
</h3>

```typescript
public httpConfig: pulumi.Output<{ ... } | undefined>;
```


Activate or deactivate HTTP. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L80">property id</a>
</h3>

```typescript
id: Output<ID>;
```


id is the provider-assigned unique ID for this managed resource.  It is set during
deployments and may be missing (undefined) during planning phases.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/registry.ts#L40">property mqttConfig</a>
</h3>

```typescript
public mqttConfig: pulumi.Output<{ ... } | undefined>;
```


Activate or deactivate MQTT. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/registry.ts#L45">property name</a>
</h3>

```typescript
public name: pulumi.Output<string>;
```


A unique name for the resource, required by device registry.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/registry.ts#L49">property project</a>
</h3>

```typescript
public project: pulumi.Output<string>;
```


The project in which the resource belongs. If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/registry.ts#L53">property region</a>
</h3>

```typescript
public region: pulumi.Output<string>;
```


The Region in which the created address should reside. If it is not provided, the provider region is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/registry.ts#L57">property stateNotificationConfig</a>
</h3>

```typescript
public stateNotificationConfig: pulumi.Output<{ ... } | undefined>;
```


A PubSub topic to publish device state updates. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/node_modules/@pulumi/pulumi/resource.d.ts#L11">property urn</a>
</h3>

```typescript
urn: Output<URN>;
```


urn is the stable logical URN used to distinctly address a resource, both before and after
deployments.

<h2 class="pdoc-module-header" id="getKMSSecret">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/getKMSSecret.ts#L18">function getKMSSecret</a>
</h2>

```typescript
getKMSSecret(args: GetKMSSecretArgs, opts?: pulumi.InvokeOptions): Promise<GetKMSSecretResult>
```


This data source allows you to use data encrypted with Google Cloud KMS
within your resource definitions.

For more information see
[the official documentation](https://cloud.google.com/kms/docs/encrypt-decrypt).

~> **NOTE**: Using this data provider will allow you to conceal secret data within your
resource definitions, but it does not take care of protecting that data in the
logging output, plan output, or state output.  Please take care to secure your secret
data outside of resource definitions.

<h2 class="pdoc-module-header" id="CryptoKeyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKey.ts#L101">interface CryptoKeyArgs</a>
</h2>

The set of arguments for constructing a CryptoKey resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKey.ts#L105">property keyRing</a>
</h3>

```typescript
keyRing: pulumi.Input<string>;
```


The id of the Google Cloud Platform KeyRing to which the key shall belong.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKey.ts#L110">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The CryptoKey's name.
A CryptoKey’s name must be unique within a location and match the regular expression `[a-zA-Z0-9_-]{1,63}`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKey.ts#L117">property rotationPeriod</a>
</h3>

```typescript
rotationPeriod?: pulumi.Input<string>;
```


Every time this period passes, generate a new CryptoKeyVersion and set it as
the primary. The first rotation will take place after the specified period. The rotation period has the format
of a decimal number with up to 9 fractional digits, followed by the letter s (seconds). It must be greater than
a day (ie, 83400).

<h2 class="pdoc-module-header" id="CryptoKeyIAMBindingArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKeyIAMBinding.ts#L111">interface CryptoKeyIAMBindingArgs</a>
</h2>

The set of arguments for constructing a CryptoKeyIAMBinding resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKeyIAMBinding.ts#L118">property cryptoKeyId</a>
</h3>

```typescript
cryptoKeyId: pulumi.Input<string>;
```


The crypto key ID, in the form
`{project_id}/{location_name}/{key_ring_name}/{crypto_key_name}` or
`{location_name}/{key_ring_name}/{crypto_key_name}`.
In the second form, the provider's project setting will be used as a fallback.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKeyIAMBinding.ts#L122">property members</a>
</h3>

```typescript
members: pulumi.Input<pulumi.Input<string>[]>;
```


A list of users that the role should apply to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKeyIAMBinding.ts#L128">property role</a>
</h3>

```typescript
role: pulumi.Input<string>;
```


The role that should be applied. Only one
`google_kms_crypto_key_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h2 class="pdoc-module-header" id="CryptoKeyIAMBindingState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKeyIAMBinding.ts#L84">interface CryptoKeyIAMBindingState</a>
</h2>

Input properties used for looking up and filtering CryptoKeyIAMBinding resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKeyIAMBinding.ts#L91">property cryptoKeyId</a>
</h3>

```typescript
cryptoKeyId?: pulumi.Input<string>;
```


The crypto key ID, in the form
`{project_id}/{location_name}/{key_ring_name}/{crypto_key_name}` or
`{location_name}/{key_ring_name}/{crypto_key_name}`.
In the second form, the provider's project setting will be used as a fallback.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKeyIAMBinding.ts#L95">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


(Computed) The etag of the crypto key's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKeyIAMBinding.ts#L99">property members</a>
</h3>

```typescript
members?: pulumi.Input<pulumi.Input<string>[]>;
```


A list of users that the role should apply to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKeyIAMBinding.ts#L105">property role</a>
</h3>

```typescript
role?: pulumi.Input<string>;
```


The role that should be applied. Only one
`google_kms_crypto_key_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h2 class="pdoc-module-header" id="CryptoKeyIAMMemberArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKeyIAMMember.ts#L114">interface CryptoKeyIAMMemberArgs</a>
</h2>

The set of arguments for constructing a CryptoKeyIAMMember resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKeyIAMMember.ts#L121">property cryptoKeyId</a>
</h3>

```typescript
cryptoKeyId: pulumi.Input<string>;
```


The key ring ID, in the form
`{project_id}/{location_name}/{key_ring_name}/{crypto_key_name}` or
`{location_name}/{key_ring_name}/{crypto_key_name}`. In the second form,
the provider's project setting will be used as a fallback.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKeyIAMMember.ts#L125">property member</a>
</h3>

```typescript
member: pulumi.Input<string>;
```


The user that the role should apply to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKeyIAMMember.ts#L130">property role</a>
</h3>

```typescript
role: pulumi.Input<string>;
```


The role that should be applied. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h2 class="pdoc-module-header" id="CryptoKeyIAMMemberState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKeyIAMMember.ts#L88">interface CryptoKeyIAMMemberState</a>
</h2>

Input properties used for looking up and filtering CryptoKeyIAMMember resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKeyIAMMember.ts#L95">property cryptoKeyId</a>
</h3>

```typescript
cryptoKeyId?: pulumi.Input<string>;
```


The key ring ID, in the form
`{project_id}/{location_name}/{key_ring_name}/{crypto_key_name}` or
`{location_name}/{key_ring_name}/{crypto_key_name}`. In the second form,
the provider's project setting will be used as a fallback.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKeyIAMMember.ts#L99">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


(Computed) The etag of the project's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKeyIAMMember.ts#L103">property member</a>
</h3>

```typescript
member?: pulumi.Input<string>;
```


The user that the role should apply to.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKeyIAMMember.ts#L108">property role</a>
</h3>

```typescript
role?: pulumi.Input<string>;
```


The role that should be applied. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h2 class="pdoc-module-header" id="CryptoKeyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKey.ts#L79">interface CryptoKeyState</a>
</h2>

Input properties used for looking up and filtering CryptoKey resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKey.ts#L83">property keyRing</a>
</h3>

```typescript
keyRing?: pulumi.Input<string>;
```


The id of the Google Cloud Platform KeyRing to which the key shall belong.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKey.ts#L88">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The CryptoKey's name.
A CryptoKey’s name must be unique within a location and match the regular expression `[a-zA-Z0-9_-]{1,63}`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/cryptoKey.ts#L95">property rotationPeriod</a>
</h3>

```typescript
rotationPeriod?: pulumi.Input<string>;
```


Every time this period passes, generate a new CryptoKeyVersion and set it as
the primary. The first rotation will take place after the specified period. The rotation period has the format
of a decimal number with up to 9 fractional digits, followed by the letter s (seconds). It must be greater than
a day (ie, 83400).

<h2 class="pdoc-module-header" id="GetKMSSecretArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/getKMSSecret.ts#L28">interface GetKMSSecretArgs</a>
</h2>

A collection of arguments for invoking getKMSSecret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/getKMSSecret.ts#L32">property ciphertext</a>
</h3>

```typescript
ciphertext: string;
```


The ciphertext to be decrypted, encoded in base64

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/getKMSSecret.ts#L38">property cryptoKey</a>
</h3>

```typescript
cryptoKey: string;
```


The id of the CryptoKey that will be used to
decrypt the provided ciphertext. This is represented by the format
`{projectId}/{location}/{keyRingName}/{cryptoKeyName}`.

<h2 class="pdoc-module-header" id="GetKMSSecretResult">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/getKMSSecret.ts#L44">interface GetKMSSecretResult</a>
</h2>

A collection of values returned by getKMSSecret.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/getKMSSecret.ts#L52">property id</a>
</h3>

```typescript
id: string;
```


id is the provider-assigned unique ID for this managed resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/getKMSSecret.ts#L48">property plaintext</a>
</h3>

```typescript
plaintext: string;
```


Contains the result of decrypting the provided ciphertext.

<h2 class="pdoc-module-header" id="KeyRingArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRing.ts#L99">interface KeyRingArgs</a>
</h2>

The set of arguments for constructing a KeyRing resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRing.ts#L104">property location</a>
</h3>

```typescript
location: pulumi.Input<string>;
```


The Google Cloud Platform location for the KeyRing.
A full list of valid locations can be found by running `gcloud kms locations list`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRing.ts#L109">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The KeyRing's name.
A KeyRing’s name must be unique within a location and match the regular expression `[a-zA-Z0-9_-]{1,63}`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRing.ts#L114">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project in which the resource belongs. If it
is not provided, the provider project is used.

<h2 class="pdoc-module-header" id="KeyRingIAMBindingArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMBinding.ts#L112">interface KeyRingIAMBindingArgs</a>
</h2>

The set of arguments for constructing a KeyRingIAMBinding resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMBinding.ts#L119">property keyRingId</a>
</h3>

```typescript
keyRingId: pulumi.Input<string>;
```


The key ring ID, in the form
`{project_id}/{location_name}/{key_ring_name}` or
`{location_name}/{key_ring_name}`. In the second form, the provider's
project setting will be used as a fallback.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMBinding.ts#L120">property members</a>
</h3>

```typescript
members: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMBinding.ts#L126">property role</a>
</h3>

```typescript
role: pulumi.Input<string>;
```


The role that should be applied. Only one
`google_kms_key_ring_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h2 class="pdoc-module-header" id="KeyRingIAMBindingState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMBinding.ts#L88">interface KeyRingIAMBindingState</a>
</h2>

Input properties used for looking up and filtering KeyRingIAMBinding resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMBinding.ts#L92">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


(Computed) The etag of the key ring's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMBinding.ts#L99">property keyRingId</a>
</h3>

```typescript
keyRingId?: pulumi.Input<string>;
```


The key ring ID, in the form
`{project_id}/{location_name}/{key_ring_name}` or
`{location_name}/{key_ring_name}`. In the second form, the provider's
project setting will be used as a fallback.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMBinding.ts#L100">property members</a>
</h3>

```typescript
members?: pulumi.Input<pulumi.Input<string>[]>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMBinding.ts#L106">property role</a>
</h3>

```typescript
role?: pulumi.Input<string>;
```


The role that should be applied. Only one
`google_kms_key_ring_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h2 class="pdoc-module-header" id="KeyRingIAMMemberArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMMember.ts#L112">interface KeyRingIAMMemberArgs</a>
</h2>

The set of arguments for constructing a KeyRingIAMMember resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMMember.ts#L119">property keyRingId</a>
</h3>

```typescript
keyRingId: pulumi.Input<string>;
```


The key ring ID, in the form
`{project_id}/{location_name}/{key_ring_name}` or
`{location_name}/{key_ring_name}`. In the second form, the provider's
project setting will be used as a fallback.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMMember.ts#L120">property member</a>
</h3>

```typescript
member: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMMember.ts#L126">property role</a>
</h3>

```typescript
role: pulumi.Input<string>;
```


The role that should be applied. Only one
`google_kms_key_ring_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h2 class="pdoc-module-header" id="KeyRingIAMMemberState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMMember.ts#L88">interface KeyRingIAMMemberState</a>
</h2>

Input properties used for looking up and filtering KeyRingIAMMember resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMMember.ts#L92">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


(Computed) The etag of the key ring's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMMember.ts#L99">property keyRingId</a>
</h3>

```typescript
keyRingId?: pulumi.Input<string>;
```


The key ring ID, in the form
`{project_id}/{location_name}/{key_ring_name}` or
`{location_name}/{key_ring_name}`. In the second form, the provider's
project setting will be used as a fallback.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMMember.ts#L100">property member</a>
</h3>

```typescript
member?: pulumi.Input<string>;
```

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMMember.ts#L106">property role</a>
</h3>

```typescript
role?: pulumi.Input<string>;
```


The role that should be applied. Only one
`google_kms_key_ring_iam_binding` can be used per role. Note that custom roles must be of the format
`[projects|organizations]/{parent-name}/roles/{role-name}`.

<h2 class="pdoc-module-header" id="KeyRingIAMPolicyArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMPolicy.ts#L103">interface KeyRingIAMPolicyArgs</a>
</h2>

The set of arguments for constructing a KeyRingIAMPolicy resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMPolicy.ts#L110">property keyRingId</a>
</h3>

```typescript
keyRingId: pulumi.Input<string>;
```


The key ring ID, in the form
`{project_id}/{location_name}/{key_ring_name}` or
`{location_name}/{key_ring_name}`. In the second form, the provider's
project setting will be used as a fallback.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMPolicy.ts#L115">property policyData</a>
</h3>

```typescript
policyData: pulumi.Input<string>;
```


The policy data generated by
a `google_iam_policy` data source.

<h2 class="pdoc-module-header" id="KeyRingIAMPolicyState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMPolicy.ts#L81">interface KeyRingIAMPolicyState</a>
</h2>

Input properties used for looking up and filtering KeyRingIAMPolicy resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMPolicy.ts#L85">property etag</a>
</h3>

```typescript
etag?: pulumi.Input<string>;
```


(Computed) The etag of the key ring's IAM policy.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMPolicy.ts#L92">property keyRingId</a>
</h3>

```typescript
keyRingId?: pulumi.Input<string>;
```


The key ring ID, in the form
`{project_id}/{location_name}/{key_ring_name}` or
`{location_name}/{key_ring_name}`. In the second form, the provider's
project setting will be used as a fallback.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRingIAMPolicy.ts#L97">property policyData</a>
</h3>

```typescript
policyData?: pulumi.Input<string>;
```


The policy data generated by
a `google_iam_policy` data source.

<h2 class="pdoc-module-header" id="KeyRingState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRing.ts#L78">interface KeyRingState</a>
</h2>

Input properties used for looking up and filtering KeyRing resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRing.ts#L83">property location</a>
</h3>

```typescript
location?: pulumi.Input<string>;
```


The Google Cloud Platform location for the KeyRing.
A full list of valid locations can be found by running `gcloud kms locations list`.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRing.ts#L88">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


The KeyRing's name.
A KeyRing’s name must be unique within a location and match the regular expression `[a-zA-Z0-9_-]{1,63}`

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/keyRing.ts#L93">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project in which the resource belongs. If it
is not provided, the provider project is used.

<h2 class="pdoc-module-header" id="RegistryArgs">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/registry.ts#L136">interface RegistryArgs</a>
</h2>

The set of arguments for constructing a Registry resource.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/registry.ts#L140">property credentials</a>
</h3>

```typescript
credentials?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


List of public key certificates to authenticate devices. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/registry.ts#L144">property eventNotificationConfig</a>
</h3>

```typescript
eventNotificationConfig?: pulumi.Input<{ ... }>;
```


A PubSub topics to publish device events. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/registry.ts#L148">property httpConfig</a>
</h3>

```typescript
httpConfig?: pulumi.Input<{ ... }>;
```


Activate or deactivate HTTP. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/registry.ts#L152">property mqttConfig</a>
</h3>

```typescript
mqttConfig?: pulumi.Input<{ ... }>;
```


Activate or deactivate MQTT. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/registry.ts#L157">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource, required by device registry.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/registry.ts#L161">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project in which the resource belongs. If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/registry.ts#L165">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The Region in which the created address should reside. If it is not provided, the provider region is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/registry.ts#L169">property stateNotificationConfig</a>
</h3>

```typescript
stateNotificationConfig?: pulumi.Input<{ ... }>;
```


A PubSub topic to publish device state updates. Structure is documented below.

<h2 class="pdoc-module-header" id="RegistryState">
<a class="pdoc-member-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/registry.ts#L97">interface RegistryState</a>
</h2>

Input properties used for looking up and filtering Registry resources.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/registry.ts#L101">property credentials</a>
</h3>

```typescript
credentials?: pulumi.Input<pulumi.Input<{ ... }>[]>;
```


List of public key certificates to authenticate devices. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/registry.ts#L105">property eventNotificationConfig</a>
</h3>

```typescript
eventNotificationConfig?: pulumi.Input<{ ... }>;
```


A PubSub topics to publish device events. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/registry.ts#L109">property httpConfig</a>
</h3>

```typescript
httpConfig?: pulumi.Input<{ ... }>;
```


Activate or deactivate HTTP. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/registry.ts#L113">property mqttConfig</a>
</h3>

```typescript
mqttConfig?: pulumi.Input<{ ... }>;
```


Activate or deactivate MQTT. Structure is documented below.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/registry.ts#L118">property name</a>
</h3>

```typescript
name?: pulumi.Input<string>;
```


A unique name for the resource, required by device registry.
Changing this forces a new resource to be created.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/registry.ts#L122">property project</a>
</h3>

```typescript
project?: pulumi.Input<string>;
```


The project in which the resource belongs. If it is not provided, the provider project is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/registry.ts#L126">property region</a>
</h3>

```typescript
region?: pulumi.Input<string>;
```


The Region in which the created address should reside. If it is not provided, the provider region is used.

<h3 class="pdoc-member-header">
<a class="pdoc-child-name" href="https://github.com/pulumi/pulumi-gcp/blob/master/sdk/nodejs/kms/registry.ts#L130">property stateNotificationConfig</a>
</h3>

```typescript
stateNotificationConfig?: pulumi.Input<{ ... }>;
```


A PubSub topic to publish device state updates. Structure is documented below.

